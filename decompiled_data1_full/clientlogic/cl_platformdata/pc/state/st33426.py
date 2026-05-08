# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33426.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33426.pyc
# Source Generated with Decompyle++
# File: st33426.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, '33425_NoTrigger') == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 20:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33425_Count', (lambda *a: Func404(*a)))
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func437(*a, **{
'sKey': '33425_Count' })),
'b': 20 })))
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33424, (lambda *a: Func437(*a, **{
'sKey': '33425_Count' }) // 20), 0)


class CState(cl_state.CState):
    m_SID = 33426
    m_Name = '#NT#损余奉缺投掷技能已强化状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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

