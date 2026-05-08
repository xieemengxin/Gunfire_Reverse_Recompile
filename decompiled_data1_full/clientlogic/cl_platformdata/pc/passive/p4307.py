# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4307.pyc
# Source Generated with Decompyle++
# File: p4307.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, STATE_EFF_SUBSPD, STATE_EFF_VERTIGO, WARRIOR_NORBOX
from cl_newformula import Func204, Func205, Func518, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 400, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8041, 0, { }, -1)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_VERTIGO, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 1, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func205(*a))) >= 3 and cl_condition.CheckInPointLayerNewLevel(oWarrior, oLifeCycle, 0):
        cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGESTART, -1, 11)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 8074, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 100, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7944, 1000, { }, 1, None, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 1000, { }, 1, 0, None)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 8074, 0)
    cl_action.CommonOwnSummonDie(oWarrior, oEventCB.GetCBLifeCycle(), 1062)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 8073, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 8062) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 8073) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 8062, 250, { }, 1, 0, None)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 23414, 0, { })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 4:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 6000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 2)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 60)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 6500)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 70)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 1:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 7000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RemainTime'):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 10, 1, (lambda *a: max(4, Func518(*a, **{
'sAttr': 'ChallengeTime' }) - Func717(*a, **{
'sArg': 'RemainTime' }))), 0, 0, { })
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KillCloneMonsterNum'):
        cl_action.CommonListenGlobalMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, -1, 8)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MonsterHpThreshold'):
        cl_action.CommonListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'MonsterHpThreshold' })), HP_RADIO_SUB, 10)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AlreadyKillNum', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AlreadyKillNum') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KillCloneMonsterNum'):
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RemainTime'):
            cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KillCloneMonsterNum'):
            cl_action.CommonDoneGlobalMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, -1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MonsterHpThreshold'):
            cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'MonsterHpThreshold' })), HP_RADIO_SUB)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 8074) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8074, 0, {
                'DirectDelayAction': 1 }, 1)


def DoCallBackAction10(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RemainTime'):
        cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KillCloneMonsterNum'):
        cl_action.CommonDoneGlobalMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, -1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MonsterHpThreshold'):
        cl_action.CommonDoneListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'MonsterHpThreshold' })), HP_RADIO_SUB)
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 8074) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8074, 0, {
            'DirectDelayAction': 1 }, 1)


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 4:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 6000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 2)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 60)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 6500)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 70)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) >= 1:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RemainTime', 7000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'KillCloneMonsterNum', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'MonsterHpThreshold', 0)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RemainTime'):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 10, 1, (lambda *a: max(4, Func518(*a, **{
'sAttr': 'ChallengeTime' }) - Func717(*a, **{
'sArg': 'RemainTime' }))), 0, 0, { })
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KillCloneMonsterNum'):
        cl_action.CommonListenGlobalMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, -1, 8)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MonsterHpThreshold'):
        cl_action.CommonListenHPThreshold(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'MonsterHpThreshold' })), HP_RADIO_SUB, 10)


class CPerform(CCustomPerform):
    m_SID = 4307
    m_Name = '【迭代】宝箱怪被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        6: DoCallBackAction6,
        8: DoCallBackAction8,
        10: DoCallBackAction10,
        11: DoCallBackAction11 }
    m_BaseArgData = { }
    m_DieDisable = 0

