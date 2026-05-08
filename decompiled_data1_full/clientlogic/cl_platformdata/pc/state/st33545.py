# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33545.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33545.pyc
# Source Generated with Decompyle++
# File: st33545.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonDisableMonsterSuper(oTarget, oLifeCycle)
    cl_action.CommonDisableMonsterRelic(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 33545
    m_Name = '怪物通用虚弱状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
    m_TargetType = OBJ_SELF
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }
    
    def CheckHighAttr(self, oTarget, oOldState):
        iOldVal = oOldState.GetArgValue('DamAdd')
        iCurVal = self.GetArgValue('DamAdd')
        return iOldVal < iCurVal


