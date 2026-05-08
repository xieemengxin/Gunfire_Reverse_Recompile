# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33329.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33329.pyc
# Source Generated with Decompyle++
# File: st33329.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_DEBUFF, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 0)
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 1944)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemovePerform(oTarget, oLifeCycle, 1944)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 5 and cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 25, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, 0, None, None, None, None)
        if cl_evcon.GetTargetNum(oTarget, oEventCB) > 0:
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 30)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1944, {
                'Att': (lambda *a: Func304(*a, **{
'sAttr': 'Att' })) }, None)
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ElementExceptionNum'):
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ElementExceptionNum', 0)
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 1)
            else:
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ElementExceptionNum', 1)


class CState(cl_state.CState):
    m_SID = 33329
    m_Name = '#NT#E3元素异常计数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

