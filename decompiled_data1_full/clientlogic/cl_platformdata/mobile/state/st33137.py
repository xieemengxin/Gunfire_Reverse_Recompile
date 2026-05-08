# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33137.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33137.pyc
# Source Generated with Decompyle++
# File: st33137.pyc (Python 3.6)

from cl_platformdata.custom.state.customaction import CustomAction33120 as CustomAction
from cl_platformdata.custom.state.customaction import CustomActionTocixEnd
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_object.logging import ErrLog
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_REFRESHORSYNC, STATE_CLS_SPECIAL, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })


def StateRemoveAction(oTarget, oLifeCycle):
    CustomActionTocixEnd(oTarget, oLifeCycle, { })


class CState(cl_state.CState):
    m_SID = 33137
    m_Name = '#NT#毒气-迭代版毒气状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_ENEMY
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    
    def AddCount(self, oTarget, iCnt, iFrame = 0):
        if iFrame < 0:
            return None
        self.m_OldCount = self.m_CurCount
        iOldCount = self.m_CurCount
        self.m_CurCount += iCnt
        if self.m_CurCount < self.m_MinCount:
            self.m_CurCount = self.m_MinCount
        iChange = self.m_CurCount - iOldCount
        if self.m_CurCount != iOldCount:
            if not self.m_LifeCycle:
                ErrLog.Alert('Warrior %s State %s LifeCycle is None' % (oTarget.m_SID, self.m_Key))
                return None
            oAttack = self.m_Game.GetObject(self.m_StateInfo['AID'])
            if oAttack:
                oAttack.Add('AllTocixCount', iChange)
            oTarget.m_State.GS2CRefreshCnt(self)
        if iFrame and iChange >= 0:
            self.AddLimitCount(oTarget, iCnt, iFrame)


