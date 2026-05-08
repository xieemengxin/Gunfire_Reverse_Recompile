# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51338.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51338.pyc
# Source Generated with Decompyle++
# File: p51338.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, PF_SUBMSG_CAREERPF
from cl_newformula import Func717, Func804, Func805

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12033)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12033)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12033)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12033)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12033)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12033)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12033)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 7)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12033)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12033)
    cl_action.CommonSetDiceAttackTimes(oWarrior, oLifeCycle, 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonHaltDicePointPerform(oWarrior, oLifeCycle, 12033)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12033, '', 0, 1, {
            'DiceID': (lambda *a: Func805(*a)),
            'AttDis': (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })) })
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51338,
            'Item': (lambda *a: Func804(*a)),
            'TriggerPerformID': 12033 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 25)


class CPerform(CCustomPerform):
    m_SID = 51338
    m_Name = '腐蚀尖刺'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

