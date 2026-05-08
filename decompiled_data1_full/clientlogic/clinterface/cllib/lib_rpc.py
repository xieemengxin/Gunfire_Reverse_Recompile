# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_rpc.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_rpc.pyc
# Source Generated with Decompyle++
# File: lib_rpc.pyc (Python 3.6)

from cl_only import Functor, GetFrameTime
from cllib.lib_net import *
import marshal
import importlib

class RPC_Functor(object):
    
    def __init__(self, resfunc, timeoutfunc, *lstArgs):
        self.m_ResFunc = resfunc
        self.m_TimeoutFunc = timeoutfunc
        self.m_SelfArgs = lstArgs

    
    def CallRet(self, *lstRes):
        lstArgs = self.m_SelfArgs
        if self.m_ResFunc:
            self.m_ResFunc(*lstArgs + lstRes)

    
    def CallTimeOut(self):
        lstArgs = self.m_SelfArgs
        if self.m_TimeoutFunc:
            self.m_TimeoutFunc(*lstArgs)



class CLogicRpcClass(object):
    m_CallCmd = 0
    m_ResCmd = 0
    m_CheckTimeOutFlag = 'CheckLogicRpcTimeOut'
    m_PackageSize = 500
    m_TypeSplit = 1
    m_TypeEnd = 2
    m_TypeHead = 4
    
    def __init__(self):
        self.m_CurSeq = 0
        self.m_Data = b''
        self.m_FuncCache = { }
        self.m_CallBack = { }
        self.CheckTimeOut()

    
    def CheckTimeOut(self):
        self.Call_Out(self.CheckTimeOut, 4, self.m_CheckTimeOutFlag)
        iNowTime = GetFrameTime()
        for iSeq, v in list(self.m_CallBack.items()):
            if iNowTime >= v[1]:
                del self.m_CallBack[iSeq]
                func = v[0]
                func.CallTimeOut()
        

    
    def NewSeq(self):
        self.m_CurSeq += 1
        if self.m_CurSeq >= 2147483647:
            self.m_CurSeq = 0
        return self.m_CurSeq

    
    def AddCallBack(self, func, iTimeout):
        if not func:
            return 0
        iSeq = self.NewSeq()
        iEndTime = GetFrameTime() + iTimeout * 100
        self.m_CallBack[iSeq] = (func, iEndTime)
        return iSeq

    
    def PopCallBack(self, iSeq):
        tp = self.m_CallBack.pop(iSeq, None)
        if not tp:
            return None
        return tp[0]

    
    def GetFunc(self, sFunc):
        if sFunc not in self.m_FuncCache:
            SubList = sFunc.split('.')
            if len(SubList) < 2:
                return None
            sMod = '.'.join(SubList[:-1])
            obj = importlib.import_module(sMod)
            self.m_FuncCache[sFunc] = getattr(obj, SubList[-1])
        return self.m_FuncCache[sFunc]

    
    def RemoteCallFunc(self, sFunc, lstArgs, cbfunc, iTimeout = 60):
        sArg = marshal.dumps(lstArgs)
        iSeq = self.AddCallBack(cbfunc, iTimeout)
        bFirst = True
        if len(sArg) > self.m_PackageSize - len(sFunc):
            while True:
                if len(sArg) > self.m_PackageSize - len(sFunc):
                    if bFirst:
                        iType = self.m_TypeSplit | self.m_TypeHead
                        bFirst = False
                    else:
                        iType = self.m_TypeSplit
                    PacketPrepare(self.m_CallCmd)
                    PacketAddI(iType, 1)
                    PacketAddBinaryS(sArg[:self.m_PackageSize], 0)
                    self.RpcPacketSend()
                    sArg = sArg[self.m_PackageSize:]
                    continue
        if not sArg:
            sArg = b'\x00'
        if bFirst:
            iType = self.m_TypeEnd | self.m_TypeHead
        else:
            iType = self.m_TypeEnd
        PacketPrepare(self.m_CallCmd)
        PacketAddI(iType, 1)
        PacketAddI(iSeq, 4)
        PacketAddSL(sFunc, 1)
        PacketAddBinaryS(sArg, len(sArg))
        self.RpcPacketSend()

    
    def OnCallFunction(self):
        iType = UnpackInt(1)
        if iType & self.m_TypeEnd:
            iSeq = UnpackInt(4)
            iLen = UnpackInt(1)
            sFunc = UnpackString(iLen)
            sArg = UnpackBinaryString(0)
            if self.m_Data:
                if not iType & self.m_TypeHead:
                    sArg = self.m_Data + sArg
                self.m_Data = b''
            lstArgs = marshal.loads(sArg)
            func = self.GetFunc(sFunc)
            if func:
                resfunc = Functor(self.CallRespond, iSeq)
                resfunc.m_FromServer = 0
                if isinstance(lstArgs, (list, tuple)):
                    func(resfunc, *lstArgs)
                else:
                    func(resfunc, lstArgs)
            elif iType & self.m_TypeSplit:
                if iType & self.m_TypeHead:
                    self.m_Data = UnpackBinaryString(0)
                else:
                    self.m_Data += UnpackBinaryString(0)

    
    def CallRespond(self, iSeq, *lstArgs):
        if not iSeq:
            return None
        sRes = marshal.dumps(lstArgs)
        PacketPrepare(self.m_ResCmd)
        PacketAddI(iSeq, 4)
        PacketAddBinaryS(sRes, len(sRes))
        self.RpcPacketSend()

    
    def OnRespond(self):
        iSeq = UnpackInt(4)
        func = self.PopCallBack(iSeq)
        if func:
            sRet = UnpackBinaryString(0)
            lstRet = marshal.loads(sRet)
            if isinstance(lstRet, (list, tuple)):
                func.CallRet(*lstRet)
            else:
                func.CallRet(lstRet)

    
    def RpcPacketSend(self):
        raise NotImplementedError('RpcPacketSend')

    
    def Call_Out(self, func, iDelay, sFlag):
        raise NotImplementedError('RpcCall_Out')



class CPacketData(object):
    
    def __init__(self):
        self.m_Seq = 0
        self.m_Sum = 0
        self.m_Data = b''
        self.m_HasStart = 0



class CBaseRpcClass(object):
    m_CallCmd = 0
    m_ResCmd = 0
    m_CheckTimeOutFlag = 'CheckBaseRpcTimeOut'
    m_PackageSize = 500
    m_MaxPackSerial = 200
    m_TypeSplit = 1
    m_TypeEnd = 2
    m_TypeHead = 4
    
    def __init__(self):
        self.m_CurSeq = 0
        self.m_FuncCache = { }
        self.m_CallBack = { }
        self.m_CallData = CPacketData()
        self.m_RespData = CPacketData()
        self.CheckTimeOut()

    
    def CheckTimeOut(self):
        self.Call_Out(self.CheckTimeOut, 4, self.m_CheckTimeOutFlag)
        iNowTime = GetFrameTime()
        for iSeq, v in list(self.m_CallBack.items()):
            if iNowTime >= v[1]:
                del self.m_CallBack[iSeq]
                func = v[0]
                func.CallTimeOut()
        

    
    def NewSeq(self):
        self.m_CurSeq += 1
        if self.m_CurSeq >= 2147483647:
            self.m_CurSeq = 0
        return self.m_CurSeq

    
    def AddCallBack(self, func, iTimeout):
        if not func:
            return 0
        iSeq = self.NewSeq()
        iEndTime = GetFrameTime() + iTimeout * 100
        self.m_CallBack[iSeq] = (func, iEndTime)
        return iSeq

    
    def PopCallBack(self, iSeq):
        tp = self.m_CallBack.pop(iSeq, None)
        if not tp:
            return None
        return tp[0]

    
    def GetFunc(self, sFunc):
        if sFunc not in self.m_FuncCache:
            SubList = sFunc.split('.')
            if len(SubList) < 2:
                return None
            sMod = '.'.join(SubList[:-1])
            obj = importlib.import_module(sMod)
            self.m_FuncCache[sFunc] = getattr(obj, SubList[-1])
        return self.m_FuncCache[sFunc]

    
    def RemoteCallFunc(self, sFunc, lstArgs, cbfunc, iTimeout = 60):
        sArg = marshal.dumps(lstArgs)
        iCheckSerial = len(sArg) // self.m_PackageSize
        if iCheckSerial > self.m_MaxPackSerial:
            return None
        iSeq = self.AddCallBack(cbfunc, iTimeout)
        bFirst = True
        iSerial = 1
        if len(sArg) > self.m_PackageSize - len(sFunc):
            while True:
                if len(sArg) > self.m_PackageSize - len(sFunc):
                    if bFirst:
                        iType = self.m_TypeHead
                        bFirst = False
                    else:
                        iType = self.m_TypeSplit
                    iSerial += 1
                    PacketPrepare(self.m_CallCmd)
                    PacketAddI(iSeq, 4)
                    PacketAddI(iType, 1)
                    PacketAddBinaryS(sArg[:self.m_PackageSize], 0)
                    self.RpcPacketSend()
                    sArg = sArg[self.m_PackageSize:]
                    continue
        if not sArg:
            sArg = b'\x00'
        if bFirst:
            iType = self.m_TypeEnd | self.m_TypeHead
        else:
            iType = self.m_TypeEnd
        PacketPrepare(self.m_CallCmd)
        PacketAddI(iSeq, 4)
        PacketAddI(iType, 1)
        PacketAddI(iSerial, 1)
        PacketAddSL(sFunc, 1)
        PacketAddBinaryS(sArg, len(sArg))
        self.RpcPacketSend()

    
    def OnCallFunction(self):
        iSeq = UnpackInt(4)
        iType = UnpackInt(1)
        if iType & self.m_TypeHead:
            self.m_CallData.m_HasStart = 1
            self.m_CallData.m_Sum = 0
            self.m_CallData.m_Seq = iSeq
            self.m_CallData.m_Data = b''
            if not iType & self.m_TypeEnd:
                self.m_CallData.m_Data = UnpackBinaryString(0)
                self.m_CallData.m_Sum = 1
        if iType & self.m_TypeSplit:
            if iSeq != self.m_CallData.m_Seq:
                return None
            self.m_CallData.m_Data += UnpackBinaryString(0)
            self.m_CallData.m_Sum += 1
        if iType & self.m_TypeEnd:
            if iSeq != self.m_CallData.m_Seq:
                return None
            if not self.m_CallData.m_HasStart:
                return None
            self.m_CallData.m_HasStart = 0
            iSerial = UnpackInt(1)
            iLen = UnpackInt(1)
            sFunc = UnpackString(iLen)
            self.m_CallData.m_Data += UnpackBinaryString(0)
            sArg = self.m_CallData.m_Data
            self.m_CallData.m_Data = b''
            self.m_CallData.m_Sum += 1
            if iSerial != self.m_CallData.m_Sum:
                return None
            (bRet, lstArgs) = self.LoadMarshal(sArg)
            if not bRet:
                return None
            func = self.GetFunc(sFunc)
            if func:
                resfunc = Functor(self.CallRespond, iSeq)
                resfunc.m_FromServer = 0
                self.CustomResfuncVar(resfunc)
                if isinstance(lstArgs, (list, tuple)):
                    func(resfunc, *lstArgs)
                else:
                    func(resfunc, lstArgs)

    
    def CallRespond(self, iSeq, *lstArgs):
        if not iSeq:
            return None
        sRes = marshal.dumps(lstArgs)
        bFirst = True
        iSerial = 1
        if len(sRes) > self.m_PackageSize:
            while True:
                if len(sRes) > self.m_PackageSize:
                    if bFirst:
                        iType = self.m_TypeHead
                        bFirst = False
                    else:
                        iType = self.m_TypeSplit
                    iSerial += 1
                    PacketPrepare(self.m_ResCmd)
                    PacketAddI(iSeq, 4)
                    PacketAddI(iType, 1)
                    PacketAddBinaryS(sRes[:self.m_PackageSize], 0)
                    self.RpcPacketSend()
                    sRes = sRes[self.m_PackageSize:]
                    continue
        if not sRes:
            sRes = b'\x00'
        if bFirst:
            iType = self.m_TypeEnd | self.m_TypeHead
        else:
            iType = self.m_TypeEnd
        PacketPrepare(self.m_ResCmd)
        PacketAddI(iSeq, 4)
        PacketAddI(iType, 1)
        PacketAddI(iSerial, 1)
        PacketAddBinaryS(sRes, len(sRes))
        self.RpcPacketSend()

    
    def OnRespond(self):
        iSeq = UnpackInt(4)
        iType = UnpackInt(1)
        if iType & self.m_TypeHead:
            self.m_RespData.m_HasStart = 1
            self.m_RespData.m_Sum = 0
            self.m_RespData.m_Seq = iSeq
            self.m_RespData.m_Data = b''
            if not iType & self.m_TypeEnd:
                self.m_RespData.m_Data = UnpackBinaryString(0)
                self.m_RespData.m_Sum = 1
        if iType & self.m_TypeSplit:
            if iSeq != self.m_RespData.m_Seq:
                return None
            self.m_RespData.m_Data += UnpackBinaryString(0)
            self.m_RespData.m_Sum += 1
        if iType & self.m_TypeEnd:
            if iSeq != self.m_RespData.m_Seq:
                return None
            if not self.m_RespData.m_HasStart:
                return None
            self.m_RespData.m_HasStart = 0
            iSerial = UnpackInt(1)
            self.m_RespData.m_Data += UnpackBinaryString(0)
            sRes = self.m_RespData.m_Data
            self.m_RespData.m_Data = b''
            self.m_RespData.m_Sum += 1
            if iSerial != self.m_RespData.m_Sum:
                return None
            func = self.PopCallBack(iSeq)
            (bRet, lstRes) = self.LoadMarshal(sRes)
            if not bRet:
                return None
            if func:
                if isinstance(lstRes, (list, tuple)):
                    func.CallRet(*lstRes)
                else:
                    func.CallRet(lstRes)

    
    def CustomResfuncVar(self, resfunc):
        pass

    
    def LoadMarshal(self, sArg):
        
        try:
            lstArgs = marshal.loads(sArg)
            return (True, lstArgs)
        except:
            return (False, None)


    
    def RpcPacketSend(self):
        raise NotImplementedError('RpcPacketSend')

    
    def Call_Out(self, func, iDelay, sFlag):
        raise NotImplementedError('RpcCall_Out')


