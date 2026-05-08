# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33871.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33871.pyc
# Source Generated with Decompyle++
# File: st33871.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomActionThunderByDurativeSkill as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BIGLION_STATE_BEGIN, BIGLION_STATE_END, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 2, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33018 }))) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'UseThunderCount' }))):
        CustomAction(oTarget, oEventCB, {
            'CareerStart': 1,
            'UseThunderCount': (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'UseThunderCount' })),
            'ThunderStateID': 33018 })
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack2(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'CareerEnd': 1,
        'ThunderStateID': 33018 })
    cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1330, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1331, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1332, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1336, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1337, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1435, 1, -1) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, -1):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        CustomAction(oTarget, oEventCB, {
            'Perform': 1911,
            'CareerDam': 1,
            'ThunderCD': 600,
            'ThunderStateID': 33018 })


class CState(cl_state.CState):
    m_SID = 33871
    m_Name = '#NT#步步惊雷基础效果-苍玦'
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

