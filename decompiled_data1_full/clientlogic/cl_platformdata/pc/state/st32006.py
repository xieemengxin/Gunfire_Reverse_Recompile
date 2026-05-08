# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32006.pyc
# Source Generated with Decompyle++
# File: st32006.pyc (Python 3.6)

from cl_platformdata.custom.state.customaction import CustomAction32006 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, MAIN_SKILL_DURATION_BEGIN, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_COMMON, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 3000, 0, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 1)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, {
        'StateSID': 32006,
        'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oLifeCycle) })
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, {
        'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oLifeCycle) })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 8, 0, 0)
    cl_action.CommonPerformPauseColdTime(oTarget, oLifeCycle, 1305)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })
    cl_action.StateAddState(oTarget, oLifeCycle, 32007, 100, { }, None)
    if cl_condition.HasState(oTarget, oLifeCycle, 32686):
        cl_action.StatePerformRestartColdDown(oTarget, oLifeCycle)
        cl_action.CommonSubCareerPerformColdTime(oTarget, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 32686 }) * 150), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 32011, 0, None, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st32006_fire', 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9214: 1,
        9510: 1 }, 1, 0):
        cl_evact.EventCBAddDamSign(oTarget, oEventCB, '32006Buff', 0)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 10000, 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
            'CareerPf': 1,
            'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()),
            'ParentActNum': (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })) }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.EventCBAddDamSign(oTarget, oEventCB, '32006Buff', 1)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 10000, 0, DAM_TYPE_WEAPON, None, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
            'CareerPf': 1,
            'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()),
            'ParentActNum': (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })) }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0 and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st32006_fire', 0) and cl_evcon.EventCBCheckDamSign(oTarget, oEventCB, '32006Buff') == 0:
        if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
            9214: 1,
            9510: 1 }, 1, 0):
            cl_evact.EventCBAddDamSign(oTarget, oEventCB, '32006Buff', 0)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 10000, 0, DAM_TYPE_WEAPON, '')
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
                'CareerPf': 1,
                'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()),
                'ParentActNum': (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })) }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.EventCBAddDamSign(oTarget, oEventCB, '32006Buff', 1)
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 10000, 0, DAM_TYPE_WEAPON, None, 0)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
                'CareerPf': 1,
                'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()),
                'ParentActNum': (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })) }, None)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 5000, 0, DAM_TYPE_PERFORM, '')


def CallBack7(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9098: 1,
        9495: 1,
        9097: 1,
        9498: 1,
        1910: 1,
        1973: 1 }, 1, 0):
        cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 32011, 0, None, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st32006_fire', 1)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9293: 1 }, 1, 0):
        cl_action.CommonTriggerClientBehavior(oTarget, oEventCB.GetCBLifeCycle(), 32011, 0, None, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st32006_fire', 1)


class CState(cl_state.CState):
    m_SID = 32006
    m_Name = '#NT#雷神附体'
    m_DieRemove = 1
    m_IsShow = 1
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8 }

