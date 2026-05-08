# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33129.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33129.pyc
# Source Generated with Decompyle++
# File: st33129.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func638

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1326: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20000 + 4000 * abs(cl_action.CommonGetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1326, 'PFBulletUse') - 15), 0, '')
    elif cl_evcon.CheckPerformIsInkPerform(oTarget, oEventCB):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20000, 0, '')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1326: 1 }, 1, 0):
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1326, 'PFBulletUse', 0, 0)
        cl_action.CommonSetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1326, 'PFBulletUse', (lambda *a: max(15, min(Func638(*a), 30))))


class CState(cl_state.CState):
    m_SID = 33129
    m_Name = '#NT#染墨新生加成效果'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

