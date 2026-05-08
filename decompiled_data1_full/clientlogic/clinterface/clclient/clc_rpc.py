# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_rpc.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_rpc.pyc
# Source Generated with Decompyle++
# File: clc_rpc.pyc (Python 3.6)

from C_logic import CreateLObject, TimerCall
from cl_protocol import L2S_FUNC, L2S_RESPOND, L2S_CALL, L2S_RESP, L2F_CALL, L2F_RESP
from cllib.lib_net import *
from cllib.lib_rpc import CLogicRpcClass, CBaseRpcClass
import cllib.lib_json as json

class CLogicRpcServer(CLogicRpcClass):
    m_CallCmd = L2S_FUNC
    m_ResCmd = L2S_RESPOND
    m_CheckTimeOutFlag = 'L2STimeOut'
    
    def __init__(self):
        self.m_ID = CreateLObject(0, {
            'object': self })
        super(CLogicRpcServer, self).__init__()

    
    def RpcPacketSend(self):
        LocalSend()

    
    def Call_Out(self, func, iDelay, sFlag):
        TimerCall(self.m_ID, func, iDelay * 100, sFlag)



class CLogicToSrvRpc(CBaseRpcClass):
    m_CallCmd = L2S_CALL
    m_ResCmd = L2S_RESP
    m_CheckTimeOutFlag = 'CheckL2STimeOut'
    
    def __init__(self):
        self.m_ID = CreateLObject(0, {
            'object': self })
        super(CLogicToSrvRpc, self).__init__()

    
    def RpcPacketSend(self):
        LocalSend()

    
    def Call_Out(self, func, iDelay, sFlag):
        TimerCall(self.m_ID, func, iDelay * 100, sFlag)



class CLogicToFsRpc(CBaseRpcClass):
    m_CallCmd = L2F_CALL
    m_ResCmd = L2F_RESP
    m_CheckTimeOutFlag = 'CheckL2FTimeOut'
    
    def __init__(self):
        self.m_ID = CreateLObject(0, {
            'object': self })
        super(CLogicToFsRpc, self).__init__()

    
    def RpcPacketSend(self):
        LocalSend()

    
    def Call_Out(self, func, iDelay, sFlag):
        TimerCall(self.m_ID, func, iDelay * 100, sFlag)


if 'g_Logic2Server' not in globals():
    g_Logic2Server = CLogicRpcServer()
    g_Logic2SrvRpc = CLogicToSrvRpc()
    g_Logic2FsRpc = CLogicToFsRpc()

def SendSvrMsg(iTargetServer, sFunc, lstArgs, resfunc):
    g_Logic2Server.RemoteCallFunc(sFunc, lstArgs, resfunc)


def OnCallFunction():
    g_Logic2Server.OnCallFunction()


def OnRespond():
    g_Logic2Server.OnRespond()


def CallFunc(iTargetServer, sFunc, lstArgs, resfunc, iTimeout = 60):
    g_Logic2SrvRpc.RemoteCallFunc(sFunc, lstArgs, resfunc, iTimeout)


def OnRpcCallFunc():
    g_Logic2SrvRpc.OnCallFunction()


def OnRpcRespond():
    g_Logic2SrvRpc.OnRespond()


def OnFsCallFunc():
    g_Logic2FsRpc.OnCallFunction()


def OnFsRespond():
    g_Logic2FsRpc.OnRespond()


def OnClientCall(*args):
    iLen = UnpackInt(1)
    sFunc = UnpackString(iLen)
    sArg = UnpackString(0)
    if not sArg:
        lstArgs = []
    else:
        lstArgs = json.loads(sArg)
    func = g_Logic2Server.GetFunc(sFunc)
    if not func:
        return None
    if isinstance(lstArgs, (list, tuple)):
        func(*lstArgs)
    else:
        func(lstArgs)

