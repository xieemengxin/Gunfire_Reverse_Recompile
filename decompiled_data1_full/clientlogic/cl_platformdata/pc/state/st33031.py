# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33031.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33031.pyc
# Source Generated with Decompyle++
# File: st33031.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MONSTER_PART_FLAW, MONSTER_PART_WEAKNESSFLAW, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_FLAW) or cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_WEAKNESSFLAW):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3503) == 3:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 2, None)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33031energy', 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3503) == 3:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33031energy', (lambda *a: Func404(*a)))
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33031energy', (lambda *a: Func404(*a) // 2))


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3503) == 3:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33031energy', (lambda *a: Func404(*a)))
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33031energy', (lambda *a: Func404(*a) // 2))


def CallBack5(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'st33031energy'), None)


class CState(cl_state.CState):
    m_SID = 33031
    m_Name = '#NT#处决大师冰刃能量'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

