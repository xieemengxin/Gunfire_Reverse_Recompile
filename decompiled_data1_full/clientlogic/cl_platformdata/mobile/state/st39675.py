# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39675.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39675.pyc
# Source Generated with Decompyle++
# File: st39675.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CREATE_PLANT, LEVEL_TYPE_BOSS, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSS
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE
from cl_newformula import Func429, Func604

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)
    cl_action.CommonSetPyFlag(oTarget, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 1)
    cl_action.CommonAddCustomIntData(oTarget, oLifeCycle, 'ActiveHiding', 1, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 16, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 8, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'Speed' })), 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 11, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 12, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 220):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 13, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 221):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 18, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1 }, 0, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12013, 1, 0) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1325: 1,
        1301: 1,
        1305: 1,
        1918: 1 }, 0, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1326: 1 }, 0, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEMONSTERHATE, 0)
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonAddMonterHateInfo(oTarget, oEventCB.GetCBLifeCycle(), WARRIOR_BOSS)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33559, 0, 1, { }, 0, 0, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12013, 1, 0) == 0:
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1 }, 0, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack11(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1670: 1 }, 0, 0) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': 'TalentSkill' }))):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack12(oEventCB, oTarget):
    cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack13(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1,
        1330: 1,
        1331: 1,
        1332: 1,
        1336: 1,
        1337: 1,
        1435: 1 }, 1, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack16(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.StateCBSendInvisibleEndMsg(oTarget, oEventCB)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack18(oEventCB, oTarget):
    cl_evact.EventGetTargetByPlants(oTarget, oEventCB)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33403, 0, 1, { }, 0, 0, None)
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 19, 0, 0)


def CallBack19(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33403, 0, 1, { }, 0, 0, None)


class CState(cl_state.CState):
    m_SID = 39675
    m_Name = '隐身（测试用，无UI无表现）'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        8: CallBack8,
        11: CallBack11,
        12: CallBack12,
        13: CallBack13,
        16: CallBack16,
        18: CallBack18,
        19: CallBack19 }

