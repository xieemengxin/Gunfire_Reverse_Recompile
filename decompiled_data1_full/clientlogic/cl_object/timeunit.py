# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/timeunit.pyc
# RelativePath: clientlogic/cl_object/timeunit.pyc
# Source Generated with Decompyle++
# File: timeunit.pyc (Python 3.6)

from cl_only import PythonError, WeakProxy
from cl_object.logging import ErrLog
from cl_commondefines import MAX_STATE_TYPE
import cllib.lib_flag

class CNewTimeUnit(object):
    m_TimeFlag = 'NewTimeUnit'
    
    def __init__(self, oOwner):
        self.m_Owner = WeakProxy(oOwner)
        self.m_Game = oOwner.m_Game
        self.m_WaitFrame = { }
        self.m_Idx2Frame = { }
        self.m_RemovedIdx = { }
        self.m_CallFrame = 0
        self.m_NeedToSort = 0
        self.m_HeartBeating = 0
        self.m_CurCallIndex = { }

    
    def Release(self):
        self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
        self.m_WaitFrame = { }
        self.m_Idx2Frame = { }
        self.m_RemovedIdx = { }
        self.m_Owner = None
        self.m_Game = None

    
    def Reset(self):
        self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
        self.m_WaitFrame = { }
        self.m_Idx2Frame = { }
        self.m_RemovedIdx = { }
        self.m_CallFrame = 0

    
    def HasUnit(self, idx):
        return idx in self.m_Idx2Frame

    
    def AddQueue(self, idx, iDelayFrame, info):
        if idx in self.m_Idx2Frame:
            iPreFrame = self.m_Idx2Frame[idx]
            if idx in self.m_RemovedIdx:
                del self.m_RemovedIdx[idx]
                if iPreFrame in self.m_WaitFrame:
                    self.m_WaitFrame[iPreFrame].pop(idx, None)
                    if not self.m_WaitFrame[iPreFrame]:
                        del self.m_WaitFrame[iPreFrame]
                    else:
                        dPreInfo = self.m_WaitFrame[iPreFrame][idx]
                        ErrLog.Error('timeunit adderr at %s %s %s %s' % (self.m_TimeFlag, idx, info, dPreInfo))
                        return None
        if not None:
            self.Execute(idx, info)
            return None
        if iDelayFrame < 0:
            ErrLog.Error('timeunit delayerr at %s %s %s %s' % (self.m_TimeFlag, idx, info, iDelayFrame))
            return None
        iCallFrame = iDelayFrame + self.m_Game.GetFrameNum()
        if iCallFrame not in self.m_WaitFrame:
            self.m_WaitFrame[iCallFrame] = { }
        self.m_Idx2Frame[idx] = iCallFrame
        self.m_WaitFrame[iCallFrame][idx] = info
        if not (self.m_CallFrame == 0 or iCallFrame < self.m_CallFrame) and self.m_HeartBeating:
            self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
            self.HeartBeat()

    
    def HeartBeat(self):
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame in self.m_WaitFrame:
            self.m_CallFrame = 0
            self.m_HeartBeating = 1
            self.m_CurCallIndex = self.m_WaitFrame.pop(iCurFrame)
            for idx, info in self.m_CurCallIndex.items():
                if idx in self.m_Idx2Frame:
                    del self.m_Idx2Frame[idx]
                if idx in self.m_RemovedIdx:
                    continue
                
                try:
                    self.Execute(idx, info)
                except:
                    PythonError()

            
            self.m_HeartBeating = 0
            if self.m_RemovedIdx:
                for idx in self.m_RemovedIdx:
                    if idx in self.m_Idx2Frame:
                        iFrame = self.m_Idx2Frame.pop(idx)
                        if iFrame in self.m_WaitFrame:
                            self.m_WaitFrame[iFrame].pop(idx, None)
                            if not self.m_WaitFrame[iFrame]:
                                del self.m_WaitFrame[iFrame]
                
                self.m_RemovedIdx = { }
        if self.m_WaitFrame:
            iNextFrame = min(self.m_WaitFrame)
            self.m_CallFrame = iNextFrame
            self.m_Owner.Call_Out(self.HeartBeat, iNextFrame - iCurFrame, self.m_TimeFlag)

    
    def StopWait(self, idx):
        if idx not in self.m_Idx2Frame:
            return None
        if self.m_HeartBeating:
            self.m_RemovedIdx[idx] = 1
        else:
            iFrame = self.m_Idx2Frame.pop(idx)
            if iFrame not in self.m_WaitFrame:
                return None
            self.m_WaitFrame[iFrame].pop(idx)
            if not self.m_WaitFrame[iFrame]:
                self.m_WaitFrame.pop(iFrame)
                if not self.m_WaitFrame:
                    self.m_CallFrame = 0
                    self.m_Owner.Remove_Call_Out(self.m_TimeFlag)

    
    def Execute(self, idx, info):
        pass

    
    def OnTimeOut(self, oObj, fTime, oLogFunc):
        pass



class CTimeUnit(object):
    m_TimeFlag = 'TimeUnit'
    
    def __init__(self, oOwner):
        self.m_Owner = WeakProxy(oOwner)
        self.m_Game = oOwner.m_Game
        self.m_WaitList = []
        self.m_WaitIdx = 0
        self.m_UnitList = { }
        self.m_CallTime = 0
        self.m_Sort = 0
        self.m_HeartBeating = 0

    
    def Release(self):
        self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
        self.m_UnitList = { }
        self.m_WaitList = []
        self.m_CallTime = 0
        self.m_Owner = None
        self.m_Game = None

    
    def Reset(self):
        self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
        self.m_UnitList = { }
        self.m_WaitList = []
        self.m_CallTime = 0

    
    def GetUnit(self, idx):
        if idx in self.m_UnitList:
            return self.m_UnitList[idx]

    
    def AddQueue(self, idx, iCallTime, info):
        if idx in self.m_UnitList:
            ErrLog.Error('timeunit adderr at %s %s %s %s' % (self.m_TimeFlag, idx, info, self.m_UnitList[idx]))
        iCur = self.m_Game.GetFrameNum()
        iCallTime = iCallTime + iCur
        if iCallTime <= iCur:
            self.Execute(idx, info)
            return None
        if not info:
            info = { }
        if self.m_WaitList:
            self.m_Sort = 1
        self.m_WaitIdx += 1
        info['_WaitIdx'] = self.m_WaitIdx
        self.m_UnitList[idx] = info
        self.m_WaitList.append((iCallTime, self.m_WaitIdx, idx))
        if self.m_CallTime == 0 or iCallTime < self.m_CallTime:
            if not self.m_HeartBeating:
                self.m_Owner.Remove_Call_Out(self.m_TimeFlag)
            self.HeartBeat()

    
    def GetWaitTime(self, iFrame):
        dWait = self.m_Owner.Query('LeftTime', { })
        lstWait = []
        for iCallTime, iWaitIdx, idx in self.m_WaitList:
            if idx in dWait:
                iCallTime = iFrame + dWait[idx]
            lstWait.append((iCallTime, iWaitIdx, idx))
        
        self.m_WaitList = lstWait

    
    def SetWaitTime(self):
        dWait = { }
        for _iCallTime, _, iWait in self.m_WaitList:
            dWait[iWait] = self.GetLeftTime(iWait)
        
        self.m_Owner.Set('LeftTime', dWait)

    
    def HeartBeat(self):
        if not self.m_WaitList:
            return None
        if self.m_HeartBeating == 1:
            return None
        if self.m_Sort:
            self.m_Sort = 0
            self.m_WaitList.sort()
        iNowTime = self.m_Game.GetFrameNum()
        (iCallTime, iWaitIdx, idx) = self.m_WaitList[0]
        if iCallTime <= iNowTime:
            self.m_HeartBeating = 1
            self.m_CallTime = 0
            del self.m_WaitList[0]
            if idx in self.m_UnitList and self.m_UnitList[idx]['_WaitIdx'] == iWaitIdx:
                info = self.m_UnitList[idx]
                del self.m_UnitList[idx]
                
                try:
                    self.Execute(idx, info)
                except:
                    PythonError()

            self.m_HeartBeating = 0
            self.HeartBeat()
        else:
            self.m_CallTime = iCallTime
            self.m_Owner.Call_Out(self.HeartBeat, iCallTime - iNowTime, self.m_TimeFlag)

    
    def StopWait(self, idx):
        if idx in self.m_UnitList:
            del self.m_UnitList[idx]
            iPos = -1
            for _, _, iWait in self.m_WaitList:
                iPos += 1
                if iWait == idx:
                    break
            
            if iPos >= 0:
                del self.m_WaitList[iPos]
                if len(self.m_WaitList) == 0:
                    self.m_CallTime = 0
                    self.m_Owner.Remove_Call_Out(self.m_TimeFlag)

    
    def GetLeftTime(self, idx):
        for iCallTime, _, iWait in self.m_WaitList:
            if idx == iWait:
                return max(iCallTime - self.m_Owner.m_Game.GetFrameNum(), 0)
        
        return 0

    
    def Execute(self, idx, info):
        pass



class CStateTimeUnit(CNewTimeUnit):
    m_TimeFlag = 'TU.State'
    
    def Execute(self, idx, info):
        if self.m_Owner:
            self.m_Owner.DoStateTimeUnit(idx, info)

    
    def OnTimeOut(self, oObj, fTime, oLogFunc):
        lstInfo = []
        for idx, dInfo in self.m_CurCallIndex.items():
            iStateSID = dInfo.get('SID', 0)
            iFlag = idx % MAX_STATE_TYPE
            lstInfo.append((iStateSID, iFlag))
        
        oLogFunc('%s %s %s state timeout %s time:%s' % (self.m_Game.m_ID, oObj.m_PlayerID, oObj.m_SID, lstInfo, fTime))



class CPassiveTimeUnit(CNewTimeUnit):
    m_TimeFlag = 'TU.Passive'
    
    def Execute(self, idx, info):
        if self.m_Owner:
            self.m_Owner.DoPFPassTimeUnit(idx, info)

    
    def OnTimeOut(self, oObj, fTime, oLogFunc):
        lstInfo = []
        for dPFInfo in self.m_CurCallIndex.values():
            iPerform = dPFInfo['pfid']
            iType = dPFInfo['Type']
            lstInfo.append((iPerform, iType))
        
        oLogFunc('%s %s %s passive timeout %s time:%s' % (self.m_Game.m_ID, oObj.m_PlayerID, oObj.m_SID, lstInfo, fTime))



class CWarMgrTimeUnit(CNewTimeUnit):
    m_TimeFlag = 'TU.WarManager'
    
    def Execute(self, idx, info):
        if self.m_Owner:
            self.m_Owner.DoStep(idx)


