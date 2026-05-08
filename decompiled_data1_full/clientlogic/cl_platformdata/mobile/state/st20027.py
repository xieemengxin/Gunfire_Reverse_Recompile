# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st20027.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st20027.pyc
# Source Generated with Decompyle++
# File: st20027.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction20027 as CustomAction
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendRemoveDeBuffStateMessage(oTarget, oLifeCycle)


class CState(cl_state.CState):
    m_SID = 20027
    m_Name = '腐化异常'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_Action = (StateActAction, StateRemoveAction)
    
    def CheckHighAttr(self, oTarget, oOldState):
        iOldVal = oOldState.GetArgValue('AbnormalSourceDam', None)
        if iOldVal is None:
            dOldCache = oOldState.GetArgValue('Cache')
            iOldVal = dOldCache['Att'] if dOldCache else 0
        iCurVal = self.GetArgValue('AbnormalSourceDam', None)
        if iCurVal is None:
            dCurCache = self.GetArgValue('Cache')
            iCurVal = dCurCache['Att'] if dCurCache else 0
        return iOldVal < iCurVal


