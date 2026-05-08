# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_state/__init__.pyc
# RelativePath: clientlogic/cl_state/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from __future__ import absolute_import
from cl_only import PythonError, Time2Frame, SendAlert, GAME_FRAME_TIME, GAME_FRAME, TraceLog
from cl_commondefines import STATE_TYPE_NORMAL, STATE_CLS_HELP, STATE_ADD_REPLACE, STATE_TIME_LIMIT, STATE_TIME_FOREVER, FIGHT_KEY_IGNOREDEBUFF, STATE_CLS_ABNORMAL, STATE_ADD_EXCLUDE, STATE_EFF_SUBSPD
from cl_commondefines import STATE_EFF_TOUGHNESS, STATE_ADD_OVERTIME, STATE_ADD_REFRESH, STATE_ADD_EXTENDTIME, STATE_IDX_DELAY, STATE_IDX_COUNT, STATE_IDX_LIMITCOUNT, WARRIOR_MONSTER, IGNORESTATE_EFF_FLAG
from cl_object.logging import ErrLog
from cl_object.reason import REASON_TYPE_PERFORM
import importlib
import cl_formula
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cl_object.lifecycle
import cl_abnormalconf
import cl_platformdata

class CState(object):
    m_SID = 0
    m_Name = '状态'
    m_ClassType = STATE_TYPE_NORMAL
    m_Type = STATE_CLS_HELP
    m_AddType = STATE_ADD_REPLACE
    m_Action = (None, None)
    m_DelayAction = { }
    m_CountFunc = { }
    m_RefreshFunc = { }
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_DieRemove = 0
    m_DyingRemove = 0
    m_CanDispel = 0
    m_IsShow = 0
    m_SaveToRecord = 0
    m_OnlyShowTarget = ()
    m_GameBroadcast = 0
    m_ClientData = { }
    m_CBFuncAction = { }
    m_Item = 0
    m_SendExtraInfo = 0
    m_OnlyLocalShow = 0
    
    def __init__(self):
        pass

    
    def Init(self, oGame):
        self.m_ID = oGame.NewStateID()
        self.m_Key = 'ST%d-%d' % (self.m_SID, self.m_ID)
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_Game = oGame
        self.m_Data = { }
        self.m_StateInfo = { }
        self.m_Apply = { }
        self.m_DelayInfo = { }
        self.m_DelayFirstFrame = 0
        self.m_Owner = 0
        self.m_Attacker = 0
        self.m_Enable = 0
        self.m_WaitEnable = 0
        self.m_Time = 100
        self.m_AllTime = 100
        self.m_TimeType = STATE_TIME_LIMIT
        self.m_CreateFrame = oGame.GetFrameNum()
        self.m_Reason = None
        self.m_StartCountTime = 0
        self.m_CurCount = self.m_StartCount
        self.m_LimitTimeCount = { }
        self.m_NextRefreshCountFrame = 0
        self.m_DoDelayAction = 0
        self.m_AddStateTarget = { }
        self.m_FollowState = { }
        self.m_IsFollowState = False
        self.m_LiteCD = 0
        self.m_LifeCycle = cl_object.lifecycle.CLifeCycle()
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])
        delayFunc = self.m_DelayAction['action'] if 'action' in self.m_DelayAction else None
        if delayFunc:
            self.m_LifeCycle.RegisterFunc('Delay', delayFunc)
        countFunc = self.m_CountFunc['action'] if 'action' in self.m_CountFunc else None
        if countFunc:
            self.m_LifeCycle.RegisterFunc('Count', countFunc)
        refreshFunc = self.m_RefreshFunc['action'] if 'action' in self.m_RefreshFunc else None
        if refreshFunc:
            self.m_LifeCycle.RegisterFunc('Refresh', refreshFunc)

    
    def Release(self):
        if not self.m_Game:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            oOwner.DelStateTime(self.m_ID)
        self.m_LifeCycle.Release()
        self.m_LifeCycle = None
        self.m_Game = None

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def GetTime(self):
        return self.m_Time

    
    def GetAllTime(self):
        return self.m_AllTime

    
    def GetRemainTime(self):
        if not self.m_Game:
            return 0
        iTime = self.m_Time - self.m_Game.GetFrameNum() - self.m_StartTime
        if iTime < 0:
            iTime = 0
        return iTime

    
    def GetArg(self):
        if 'arg' not in self.m_StateInfo:
            return { }
        return self.m_StateInfo['arg']

    
    def UpdateArgValue(self, dData):
        if 'arg' not in self.m_StateInfo:
            self.m_StateInfo['arg'] = { }
        self.m_StateInfo['arg'].update(dData)

    
    def AddArgValue(self, key, iAdd):
        if 'arg' not in self.m_StateInfo:
            return None
        if key in self.m_StateInfo['arg']:
            self.m_StateInfo['arg'][key] += iAdd

    
    def GetArgValue(self, key, default = 0):
        if 'arg' not in self.m_StateInfo:
            return default
        if key in self.m_StateInfo['arg']:
            return self.m_StateInfo['arg'][key]
        return default

    
    def SetArgValueDefault(self, key, default = 0):
        if 'arg' not in self.m_StateInfo:
            self.m_StateInfo['arg'] = { }
        if key not in self.m_StateInfo['arg']:
            self.m_StateInfo['arg'][key] = default
            return default
        return self.m_StateInfo['arg'][key]

    
    def SetArgValue(self, key, val):
        if 'arg' not in self.m_StateInfo:
            self.m_StateInfo['arg'] = { }
        self.m_StateInfo['arg'][key] = val

    
    def DelArgValue(self, key):
        if 'arg' not in self.m_StateInfo:
            self.m_StateInfo['arg'] = { }
            ErrLog.Alert('%s delargvalue not arg %s %s' % (self.m_Game.m_ID, self.m_SID, key))
            return None
        if key in self.m_StateInfo['arg']:
            self.m_StateInfo['arg'].pop(key)

    
    def PopArgValue(self, key, default = 0):
        if 'arg' not in self.m_StateInfo:
            return default
        return self.m_StateInfo['arg'].pop(key, default)

    
    def GetPerformID(self):
        if 'pfid' not in self.m_StateInfo:
            return 0
        return self.m_StateInfo['pfid']

    
    def GetDelayIdx(self):
        return self.m_ID + STATE_IDX_DELAY

    
    def GetCountIdx(self):
        return self.m_ID + STATE_IDX_COUNT

    
    def GetLimitCountIdx(self):
        return self.m_ID + STATE_IDX_LIMITCOUNT

    
    def GetOutShowInfo(self):
        dShow = { }
        return dShow

    
    def GetMyItem(self):
        if not self.m_Attacker:
            return None
        oItem = None
        oAttacker = self.m_Game.GetObject(self.m_Attacker)
        if oAttacker and self.m_Item:
            oItem = oAttacker.m_WieldCon.GetItemByID(self.m_Item)
            if not oItem and oAttacker.m_WandCon:
                oItem = oAttacker.m_WandCon.GetWandByID(self.m_Item)
            elif not oItem and oAttacker.m_DiceCon:
                oItem = oAttacker.m_DiceCon.GetDiceByID(self.m_Item)
            elif not oItem and oAttacker.m_SeasonCon:
                oItem = oAttacker.m_SeasonCon.GetItemByID(self.m_Item)
        return oItem

    
    def Key(self):
        return self.m_Key

    
    def Reason(self):
        return self.m_Reason

    
    def GetClientData(self):
        dData = { }
        for sKey, iValue in self.m_ClientData.items():
            if iValue is None:
                SendAlert('err', '%d状态%d客户端属性%s为空' % (self.m_Owner, self.m_SID, sKey))
                continue
            dData[sKey] = iValue
        
        return dData

    
    def AddFollowState(self, oState):
        self.m_FollowState[oState.m_ID] = oState.m_SID

    
    def NeedToSendMsg(self):
        return not (self.m_IsFollowState)

    
    def Enable(self, oTarget):
        if self.m_Enable or self.m_WaitEnable or not (self.m_LifeCycle):
            return None
        self.m_Enable = 1
        self.StartCount(oTarget)
        self.m_LifeCycle.Enable(oTarget)
        if not self.m_Enable:
            return None
        for iStateID in self.m_FollowState:
            oFollowState = oTarget.m_State.GetItem(iStateID)
            if oFollowState:
                oFollowState.Enable(oTarget)
        
        if self.m_DelayAction:
            iFirstFrame = self.GetFirstFrame()
            if iFirstFrame:
                oTarget.AddStateTime(self.GetDelayIdx(), iFirstFrame, {
                    'SID': self.m_SID,
                    'DelayCnt': 0 })
            else:
                self.DelayAction(oTarget, {
                    'SID': self.m_SID,
                    'DelayCnt': 0 })
        if self.m_TimeType == STATE_TIME_LIMIT and not oTarget.HasStateTime(self.m_ID):
            oTarget.AddStateTime(self.m_ID, self.GetRemainTime(), {
                'SID': self.m_SID,
                'idx': self.m_ID })

    
    def Disable(self, oTarget, iRefresh, iReleaseFlag = 0):
        if not self.m_Enable:
            return None
        self.m_Enable = 0
        self.StopCount(oTarget)
        oTarget.ClearStateTime(self.m_ID)
        for iStateID in self.m_FollowState:
            oFollowState = oTarget.m_State.GetItem(iStateID)
            if oFollowState:
                oTarget.m_State.RemoveItem(oFollowState.m_ID)
        
        if iReleaseFlag:
            self.m_LifeCycle.PFAndStateDisable(oTarget, iRefresh)
        else:
            self.m_LifeCycle.Disable(oTarget, iRefresh)
        self.m_FollowState = { }
        self.m_DelayInfo = { }
        self.m_Data = { }
        self.m_LimitTimeCount = { }
        self.m_NextRefreshCountFrame = 0

    
    def AddTime(self, oTarget, iTime, iMaxTime):
        if self.m_TimeType == STATE_TIME_FOREVER:
            self.m_TimeType = STATE_TIME_LIMIT
        iRemainTime = self.GetRemainTime()
        self.m_Time = iTime + iRemainTime
        if self.m_Time < 0:
            self.m_Time = 0
            iTime = 0 - iRemainTime
        elif self.m_Time > iMaxTime:
            self.m_Time = iMaxTime
            iTime = iMaxTime - iRemainTime
        self.m_AllTime += iTime
        if self.m_AllTime < 0:
            self.m_AllTime = 0
        self.m_StartTime = self.m_Game.GetFrameNum()
        iRefresh = 0 if iTime >= 0 else 1
        oTarget.DelStateTime(self.m_ID)
        oTarget.AddStateTime(self.m_ID, self.m_Time, {
            'SID': self.m_SID,
            'idx': self.m_ID })
        if self.m_Time:
            oTarget.m_State.GS2CRefreshState(oTarget, self, iRefresh)
        else:
            oTarget.m_State.GS2CItemDel(self, iRefresh)

    
    def SetTime(self, oTarget, iTime, iRefreshDelay, iRefresh = 1):
        if self.m_TimeType == STATE_TIME_FOREVER:
            self.m_TimeType = STATE_TIME_LIMIT
        iRemainTime = self.GetRemainTime()
        if iRefreshDelay:
            self.m_AllTime = iTime
        else:
            iPassTime = self.m_AllTime - iRemainTime
            self.m_AllTime = iTime + iPassTime
        self.m_StartTime = self.m_Game.GetFrameNum()
        self.m_Time = iTime
        oTarget.DelStateTime(self.m_ID)
        oTarget.AddStateTime(self.m_ID, self.m_Time, {
            'SID': self.m_SID,
            'idx': self.m_ID })
        if iRefresh:
            oTarget.m_State.GS2CRefreshState(oTarget, self)
        if iRefreshDelay and self.m_DelayAction:
            if not oTarget.HasStateTime(self.GetDelayIdx()) and not (self.m_DoDelayAction):
                self.DelayAction(oTarget, {
                    'SID': self.m_SID,
                    'DelayCnt': 0 })
                return None
            if self.m_DelayInfo and self.m_DelayInfo['DelayCnt']:
                self.m_DelayInfo['DelayCnt'] = 0

    
    def SetForever(self, oTarget):
        if self.m_TimeType == STATE_TIME_FOREVER:
            return None
        self.m_TimeType = STATE_TIME_FOREVER
        self.m_Time = 0
        self.m_AllTime = 0
        self.m_StartTime = self.m_Game.GetFrameNum()
        oTarget.DelStateTime(self.m_ID)
        oTarget.m_State.GS2CRefreshState(oTarget, self, iRefresh = 1)

    
    def SetMaxCount(self, oTarget, iCount):
        self.m_MaxCount = iCount
        iOldCount = self.m_CurCount
        if iOldCount > iCount:
            self.AddCount(oTarget, iCount - iOldCount)
        oTarget.m_State.GS2CRefreshState(oTarget, self, iRefresh = 1)

    
    def SetMinCount(self, oTarget, iCount):
        self.m_MinCount = iCount
        iOldCount = self.m_CurCount
        if iOldCount < iCount:
            self.AddCount(oTarget, iCount - iOldCount)

    
    def StopCount(self, oTarget):
        if not self.m_StartCountTime:
            return None
        self.AddCountByTime()
        self.m_StartCountTime = 0
        oTarget.m_State.GS2CRefreshCnt(self)
        oTarget.DelStateTime(self.GetCountIdx())

    
    def StartCount(self, oTarget):
        if not self.m_PerCountTime:
            return None
        if self.m_StartCountTime:
            return None
        self.m_StartCountTime = self.m_Game.GetFrameNum()
        if self.m_CurCount:
            self.m_LifeCycle.CallFunc('Count', oTarget)
        oTarget.m_State.GS2CRefreshCnt(self)
        if self.m_MaxCount and not self.IsCountFull() and self.m_PerCountTime:
            iTime = (self.m_MaxCount - self.m_CurCount) * Time2Frame(self.m_PerCountTime)
            iCountIdx = self.GetCountIdx()
            oTarget.DelStateTime(iCountIdx)
            oTarget.AddStateTime(iCountIdx, iTime, {
                'SID': self.m_SID,
                'idx': self.m_ID })

    
    def IsOpenCount(self):
        return self.m_StartCountTime

    
    def IsCountFull(self):
        return self.GetCount() >= self.m_MaxCount

    
    def OnCountFull(self, oTarget, dInfo):
        pass

    
    def GetCount(self):
        self.AddCountByTime()
        return self.m_CurCount

    
    def SetCount(self, oTarget, iNewCount):
        iOldCount = self.GetCount()
        iAddCount = iNewCount - iOldCount
        self.AddCount(oTarget, iAddCount)

    
    def AddCount(self, oTarget, iCnt, iFrame = 0):
        if iFrame < 0:
            return None
        iOldCount = self.m_CurCount
        self.m_CurCount += iCnt
        if self.m_CurCount < self.m_MinCount:
            self.m_CurCount = self.m_MinCount
        iOverFlowCount = 0
        if self.m_MaxCount and self.m_CurCount >= self.m_MaxCount:
            iOverFlowCount = self.m_CurCount - self.m_MaxCount
            self.m_CurCount = self.m_MaxCount
        if self.m_CurCount != iOldCount:
            if not self.m_LifeCycle:
                sText = '%s Warrior %s %s State %s LifeCycle is None' % (self.m_Game, oTarget.m_SID, oTarget.m_PlayerID, self.m_Key)
                ErrLog.Alert(sText)
                TraceLog('err', sText)
                return None
            self.m_LifeCycle.CallFunc('Count', oTarget)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_STATECOUNTCHANGE, oTarget, { })
            oTarget.m_State.GS2CRefreshCnt(self)
        if self.m_MaxCount and not self.IsCountFull() and self.m_PerCountTime:
            iTime = (self.m_MaxCount - self.m_CurCount) * Time2Frame(self.m_PerCountTime)
            iCountIdx = self.GetCountIdx()
            oTarget.DelStateTime(iCountIdx)
            oTarget.AddStateTime(iCountIdx, iTime, {
                'SID': self.m_SID,
                'idx': self.m_ID })
        iChange = self.m_CurCount - iOldCount
        if iFrame and iChange >= 0:
            self.AddLimitCount(oTarget, iCnt, iFrame, iOverFlowCount)

    
    def AddLimitCount(self, oTarget, iAddCount, iAddFrame, iDeadCount = 0):
        iNowFrame = self.m_Game.GetFrameNum()
        iAddDeadFrame = iNowFrame + iAddFrame
        if self.m_TimeType == STATE_TIME_LIMIT and self.GetRemainTime() < iAddFrame:
            self.SetTime(oTarget, iAddFrame, 0)
        dLimitCount = self.m_LimitTimeCount
        if iAddDeadFrame not in dLimitCount:
            dLimitCount[iAddDeadFrame] = iAddCount
        else:
            dLimitCount[iAddDeadFrame] += iAddCount
        iNextFefreshFrame = 0
        if iDeadCount > 0:
            dDeadCount = { }
            for iDeadFrame, iCnt in dLimitCount.items():
                if not iDeadCount:
                    if iDeadFrame < iNowFrame:
                        dDeadCount[iDeadFrame] = 1
                        continue
                    iNextFefreshFrame = iDeadFrame
                    break
                if iCnt > iDeadCount:
                    dLimitCount[iDeadFrame] -= iDeadCount
                    iNextFefreshFrame = iDeadFrame
                    break
                if iCnt == iDeadCount:
                    dDeadCount[iDeadFrame] = 1
                    iDeadCount = 0
                    continue
                iDeadCount -= iCnt
                dDeadCount[iDeadFrame] = 1
            
            for iDeadFrame in dDeadCount:
                dLimitCount.pop(iDeadFrame)
            
        if iNextFefreshFrame:
            self.SetNextRefreshCountTimer(oTarget, iNextFefreshFrame)
        elif not self.m_NextRefreshCountFrame:
            self.SetNextRefreshCountTimer(oTarget, iAddDeadFrame)

    
    def SetNextRefreshCountTimer(self, oTarget, iRefreshFrame):
        if self.m_NextRefreshCountFrame == iRefreshFrame:
            return None
        self.m_NextRefreshCountFrame = iRefreshFrame
        iNextFrame = iRefreshFrame - self.m_Game.GetFrameNum()
        iLimitCountIdx = self.GetLimitCountIdx()
        oTarget.DelStateTime(iLimitCountIdx)
        oTarget.AddStateTime(iLimitCountIdx, iNextFrame, {
            'SID': self.m_SID })

    
    def RefreshLimitCount(self, oTarget):
        self.m_NextRefreshCountFrame = 0
        if not self.m_LimitTimeCount:
            return None
        iSubCnt = 0
        iNextRefreshFrame = 0
        iCurFrame = self.m_Game.GetFrameNum()
        dDeadCount = { }
        for iDeadFrame, iCount in self.m_LimitTimeCount.items():
            if iDeadFrame > iCurFrame:
                iNextRefreshFrame = iDeadFrame
                break
            iSubCnt += iCount
            dDeadCount[iDeadFrame] = 1
        
        for iDeadFrame in dDeadCount:
            self.m_LimitTimeCount.pop(iDeadFrame)
        
        if iSubCnt:
            self.AddCount(oTarget, -iSubCnt)
        if iNextRefreshFrame:
            self.SetNextRefreshCountTimer(oTarget, iNextRefreshFrame)

    
    def AddCountByTime(self):
        if not self.m_StartCountTime:
            return None
        if self.m_PerCountTime == 0:
            return None
        iNowTime = self.m_Game.GetFrameNum()
        if self.m_MaxCount and self.m_CurCount >= self.m_MaxCount:
            self.m_StartCountTime = iNowTime
            return None
        iOldCount = self.m_CurCount
        self.m_CurCount += (iNowTime - self.m_StartCountTime) // Time2Frame(self.m_PerCountTime)
        if self.m_MaxCount and self.m_CurCount >= self.m_MaxCount:
            self.m_CurCount = self.m_MaxCount
            self.m_StartCountTime = iNowTime
        else:
            self.m_StartCountTime += (self.m_CurCount - iOldCount) * Time2Frame(self.m_PerCountTime)

    
    def GetFirstFrame(self):
        iFirstFrame = self.m_DelayFirstFrame
        if not iFirstFrame:
            iFirstTime = self.m_DelayAction['firsttime'] if 'firsttime' in self.m_DelayAction else 0
            iFirstFrame = Time2Frame(iFirstTime)
        return iFirstFrame

    
    def CalNextDelay(self, iOver = 1):
        if self.m_DelayAction:
            iFirstFrame = self.GetFirstFrame()
            iIntervalFrame = Time2Frame(self.m_DelayAction['delay'])
            if iOver:
                iPassFrame = self.m_Time - iFirstFrame
            else:
                iPassFrame = self.m_Game.GetFrameNum() - iFirstFrame - self.m_StartTime
            if iPassFrame < 0:
                iRestFrame = -iPassFrame
            elif iPassFrame > iIntervalFrame:
                iRestFrame = iPassFrame % iIntervalFrame
            else:
                iRestFrame = iIntervalFrame - iPassFrame
            return iRestFrame
        return 0

    
    def SetDelayFirstFrame(self, iFrame):
        self.m_DelayFirstFrame = iFrame

    
    def GetDelayCnt(self, oTarget):
        if 'cnt' in self.m_DelayAction:
            return self.m_DelayAction['cnt']
        return 0

    
    def DelayAction(self, oTarget, dInfo):
        if not self.m_Enable:
            return None
        iCnt = self.GetDelayCnt(oTarget)
        if iCnt and iCnt <= dInfo['DelayCnt']:
            return None
        self.m_DoDelayAction = 1
        dInfo['DelayCnt'] += 1
        self.m_DelayInfo = dInfo
        self.m_LifeCycle.CallFunc('Delay', oTarget)
        if not self.m_Enable:
            self.m_DoDelayAction = 0
            return None
        iDelay = self.m_DelayAction['delay']
        iDelay = cl_formula.GetResultByData(oTarget, iDelay, self.AttrCache())
        iFrame = Time2Frame(iDelay)
        if iFrame <= 0:
            iFrame = 1
        oTarget.AddStateTime(self.GetDelayIdx(), iFrame, dInfo)
        self.m_DoDelayAction = 0

    
    def CheckHighAttr(self, oTarget, oOldState):
        return 0

    
    def GetCustomFormulaResult(self, objWarrior, lstFormula, dArgs):
        return 0

    
    def CustomCondition(self, dArgs):
        return 1

    
    def CustomAction(self, oTarget, dArgs):
        pass

    
    def ClearCustomAction(self, oTarget):
        pass

    
    def GetStateAddInfo(self):
        iTime = self.m_Time * GAME_FRAME_TIME
        iRemainTime = self.GetRemainTime() * GAME_FRAME_TIME
        iCreateTime = self.m_CreateFrame * GAME_FRAME_TIME
        return [
            self.m_Owner,
            self.m_ID,
            self.m_SID,
            self.m_Attacker,
            iTime,
            iRemainTime,
            iCreateTime,
            self.m_MaxCount,
            self.GetCount()]

    
    def GetStateRefreshInfo(self):
        iTime = self.m_Time * GAME_FRAME_TIME
        iRemainTime = self.GetRemainTime() * GAME_FRAME_TIME
        return [
            self.m_Owner,
            self.m_ID,
            self.m_SID,
            iTime,
            iRemainTime,
            self.m_MaxCount,
            self.GetCount()]

    
    def AttrCache(self):
        dEvent = {
            'StateInfo': self.m_StateInfo,
            'ItemID': self.m_Item,
            'RS': self.m_Reason,
            'StateKey': self.m_Key,
            'StateID': self.m_ID,
            'StateSID': self.m_SID,
            'AID': self.m_Attacker }
        if 'arg' in self.m_StateInfo:
            dEvent['ArgData'] = self.m_StateInfo['arg']
        return dEvent

    
    def GetEventDamFactor(self):
        if 'arg' in self.m_StateInfo:
            dArgData = self.m_StateInfo['arg']
            if 'DamFactor' in dArgData:
                dDamFactor = { }
                for key, value in dArgData['DamFactor'].items():
                    dDamFactor[key] = { }
                    dDamFactor[key].update(value)
                
                return dDamFactor

    
    def GetStateStatistics(self):
        return self.m_Data

    
    def SetStateStatistics(self, dStatistics):
        self.m_Data = dStatistics

    
    def UpdateStateInfo(self, dStateInfo):
        self.m_StateInfo.update(dStateInfo)

    
    def SetLiteCD(self, iTime):
        iFrame = Time2Frame(iTime)
        iMarkFrame = self.m_Game.GetFrameNum()
        self.m_LiteCD = iFrame + iMarkFrame

    
    def CheckLiteCD(self):
        if not self.m_LiteCD:
            return 0
        iCurFrame = self.m_Game.GetFrameNum()
        if self.m_LiteCD < iCurFrame:
            return 0
        return 1



def ImportdStateMod(sImport, iState):
    
    try:
        mod = importlib.import_module('%s.st%d' % (sImport, iState))
    except:
        PythonError()
        return None

    return mod

if 'g_StateModule' not in globals():
    g_StateModule = { }

def GetStateClass(iState):
    if iState not in g_StateModule:
        if cl_platformdata.IsRunPCData():
            if not cl_platformdata.pc.ValidState(iState):
                return None
            sImport = 'cl_platformdata.pc.state'
        elif not cl_platformdata.mobile.ValidState(iState):
            return None
        sImport = 'cl_platformdata.mobile.state'
        mod = ImportdStateMod(sImport, iState)
        if not mod:
            return None
        g_StateModule[iState] = mod
    return g_StateModule[iState].CState


def LoadAll():
    if cl_platformdata.IsRunPCData():
        lstAllState = cl_platformdata.pc.GetAllState()
    else:
        lstAllState = cl_platformdata.mobile.GetAllState()
    for iState in lstAllState:
        GetStateClass(iState)
    


def ValidState(oTarget, iState, clsState, dState):
    if oTarget.m_ReleaseFlag:
        return 0
    if oTarget.m_State.m_ReleaseFlag:
        return 0
    iType = clsState.m_Type
    if oTarget.QueryBitAttr('SpecialKey') & FIGHT_KEY_IGNOREDEBUFF and iType & STATE_CLS_ABNORMAL:
        return 0
    if oTarget.QueryMaxAttr('IgnoreST%d' % iType):
        return 0
    iIgnoreEff = oTarget.QueryBitAttr('IgnoreSTEff')
    iEffType = clsState.m_EffType
    if iIgnoreEff and iEffType and iEffType & iIgnoreEff == iEffType and oTarget.JudgeIgnoreStateEff(dState['AID'], iEffType):
        return 0
    if iState not in cl_abnormalconf.g_AllEleAbnormalState:
        return 1
    if not oTarget.m_EleAbnormal.CheckDirectAddEleAbnormal(iState):
        return 0
    return 1


def AddFollowState(oTarget, oMainState, iState, iTimeType, iTime, dArgs):
    oState = AddState(oTarget, iState, iTimeType, iTime, dArgs, bIsFollowState = True)
    if not oState:
        return None
    oMainState.AddFollowState(oState)
    if oMainState.m_Enable:
        oState.Enable(oTarget)
    return oState


def AddState(oTarget, iState, iTimeType, iTime, dState, bIsFollowState = False):
    clsState = GetStateClass(iState)
    if not clsState or not ValidState(oTarget, iState, clsState, dState):
        return None
    oStateCon = oTarget.m_State
    if iTimeType == STATE_TIME_LIMIT:
        if clsState.m_EffType & STATE_EFF_TOUGHNESS:
            iTime = iTime * (100 - oTarget.QueryAttr('Toughness')) // 100
        if iTime < 0:
            iTime = 1
    bCheckTrigger = True
    if clsState.m_AddType == STATE_ADD_EXCLUDE and oStateCon.HasState(iState):
        return None
    if clsState.m_SyncMax and clsState.m_SyncMax <= oStateCon.GetStateNum(iState):
        return None
    if clsState.m_AddType in (STATE_ADD_OVERTIME, STATE_ADD_REFRESH, STATE_ADD_EXTENDTIME):
        if iState in cl_abnormalconf.g_AllAbnormalStateSID:
            oTarget.m_EleAbnormal.TryTriggerMixtureStatus(iState, dState)
            bCheckTrigger = False
        lstState = oStateCon.GetItems(iState)
        if lstState:
            oOldState = lstState[0]
            if clsState.m_AddType in (STATE_ADD_OVERTIME, STATE_ADD_REFRESH):
                if clsState.m_AddType == STATE_ADD_REFRESH:
                    iTime = iTime - oOldState.GetRemainTime()
                    oOldState.m_StateInfo.update(dState)
                    oOldState.m_LifeCycle.CallFunc('Refresh', oTarget)
                if oOldState.m_TimeType != STATE_TIME_FOREVER and iTime != 0 and oOldState.m_Enable:
                    oOldState.AddTime(oTarget, iTime, 180 * GAME_FRAME)
                return None
            if oOldState.m_TimeType == STATE_TIME_FOREVER:
                return None
            if clsState.m_AddType == STATE_ADD_EXTENDTIME:
                iTime = iTime - oOldState.GetRemainTime()
                if iTime > 0:
                    oOldState.AddTime(oTarget, iTime, 180 * GAME_FRAME)
                return None
    iAttack = dState['AID']
    oState = NewState(iState, oTarget.m_Game)
    oState.m_Owner = oTarget.m_ID
    oState.m_TimeType = iTimeType
    oState.m_Time = iTime
    oState.m_AllTime = iTime
    oState.m_Attacker = iAttack
    oState.m_Reason = dState['RS']
    oState.m_Item = dState['RS'].Query('Item', 0)
    oState.m_StateInfo = dState
    oState.m_IsFollowState = bIsFollowState
    if iState in cl_abnormalconf.g_AllAbnormalStateSID and bCheckTrigger:
        oTarget.m_EleAbnormal.TryTriggerMixtureStatus(iState, dState)
    oState = oTarget.m_State.AddItem(oState)
    return oState


def RemoveState(oTarget, iState):
    oTargetState = oTarget.m_State.GetItemBySID(iState)
    if oTargetState:
        oTarget.m_State.RemoveItem(oTargetState.m_ID)


def ValidModifyStateInfo(oTarget, oState):
    if oState.m_Type & STATE_CLS_ABNORMAL and oTarget.QueryBitAttr('SpecialKey') & FIGHT_KEY_IGNOREDEBUFF:
        return 0
    return 1


def ValidSubSpeedEnable(oTarget, oState):
    if oTarget.QueryBitAttr('ForbidEnableSTEff') & STATE_EFF_SUBSPD:
        return 1
    oReason = oState.Reason()
    if oTarget.QueryBitAttr('ForbidEnableSTEffByMonster') & STATE_EFF_SUBSPD and oReason and oReason.m_Type == REASON_TYPE_PERFORM:
        iFightType = oReason.m_FightType
        if iFightType & WARRIOR_MONSTER:
            return 1
    return 0


def SetTime(oState, oTarget, iTime, iRefreshDelay):
    if not ValidModifyStateInfo(oTarget, oState):
        return None
    oState.SetTime(oTarget, iTime, iRefreshDelay)


def AddTime(oState, oTarget, iTime, iMaxTime):
    if not ValidModifyStateInfo(oTarget, oState):
        return None
    oState.AddTime(oTarget, iTime, iMaxTime)


def SetForever(oState, oTarget):
    oState.SetForever(oTarget)


def NewState(iState, oGame):
    clsState = GetStateClass(iState)
    if not clsState:
        return None
    oState = clsState()
    oState.Init(oGame)
    return oState

