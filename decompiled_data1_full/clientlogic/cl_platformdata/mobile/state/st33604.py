# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33604.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33604.pyc
# Source Generated with Decompyle++
# File: st33604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33604 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BIGLION_STATE_BEGIN, BIGLION_STATE_END, DAM_USE_ALL, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func425, Func518, Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonHeroSwitchPerform(oTarget, oLifeCycle, 'Career', 1334)
    cl_action.CommonHeroSwitchPerform(oTarget, oLifeCycle, 'Throw', 1435)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 3, 0, 0)
    cl_action.CommonSetPerformForceAttr(oTarget, oLifeCycle, 1336, 'MinUseEnergy', 3000)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, { })
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.ImmunitySubSpdState(oTarget, oLifeCycle)
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func589(*a)), 0, DAM_USE_ALL)
    cl_action.CommonChangeAttrFixedAddition(oTarget, oLifeCycle, 'HPMax', 25000)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 2, 0, 99)
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATESKILLCOUNT, -1, 7, 0, 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1310, 'ColdTime', 30000, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'JumpHeight', 3000, 0, 0)
    cl_action.CommonSetPerformForceAttr(oTarget, oLifeCycle, 1330, 'MinUseEnergy', 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonAddState(oTarget, oLifeCycle, 33604, 33633, { }, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, { })
    cl_action.CommonHeroSwitchPerform(oTarget, oLifeCycle, 'Career', 1329)
    cl_action.CommonHeroSwitchPerform(oTarget, oLifeCycle, 'Throw', 1434)
    cl_action.CommonSetPerformArgs(oTarget, oLifeCycle, 1330, 'SkillCount', 0, 0)
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func589(*a)), 0, DAM_USE_ALL)
    cl_action.CommonSetPerformArgs(oTarget, oLifeCycle, 1336, 'SkillCount', 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 33883, 150, { }, None)
    if cl_condition.HasState(oTarget, oLifeCycle, 33711):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33711, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckReenter(oTarget, oEventCB):
        cl_action.CommonSwitchPerform(oTarget, oEventCB.GetCBLifeCycle(), 1334)
        cl_action.CommonSwitchPerform(oTarget, oEventCB.GetCBLifeCycle(), 1435)
        cl_action.CommonHeroSwitchPerform(oTarget, oEventCB.GetCBLifeCycle(), 'Career', 1334)
        cl_action.CommonHeroSwitchPerform(oTarget, oEventCB.GetCBLifeCycle(), 'Throw', 1435)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33757) == 1 or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1435, 1, 0) == 1 or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1334, 1, 0) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 1165) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33604) or cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33863):
        cl_evact.EventCBChangeCure(oTarget, oEventCB, 0, -9000, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBReducePredictDam(oTarget, oEventCB, (lambda *a: Func425(*a) * 0.9), 1)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonHPModify(oTarget, oEventCB.GetCBLifeCycle(), 'HP', 100, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1336: 1,
        1330: 1,
        1331: 1,
        1332: 1,
        1337: 1,
        1310: 1,
        1435: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckMonsterIsPetrochemical(oTarget, oEventCB) == 0:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33827, (lambda *a: max(400, int(Func518(*a, **{
'sAttr': 'ContHitKeepTime' })))), { }, 0)
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33827, 1, 0)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1336: 1 }, 1, 0):
        CustomAction(oTarget, oEventCB, {
            'HeavyCount': 2,
            'HeavyPerform': 1336,
            'HeavyUseEnergy': 3000,
            'Talent': 3709,
            'TalentLevel': 2,
            'HitState': 33827,
            'NoCostCount': 30 })


class CState(cl_state.CState):
    m_SID = 33604
    m_Name = '#NT#苍玦变身'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_GameBroadcast = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        7: CallBack7 }

