# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51226.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51226.pyc
# Source Generated with Decompyle++
# File: p51226.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction51226 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, WARRIOR_BOSS, WARRIOR_MONSTER, WARRIOR_NORMAL
from cl_newformula import Func518, Func717, Func738

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 8167):
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 8167, 0)
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORMAL):
        cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransferIntval', 240)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransferIntval', 500)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'AlreadyMutant', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 4, 0, 0)
    if cl_condition.CheckHasLockEnemy(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'AlreadyMutant', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'TransferIntval' })), (lambda *a: Func717(*a, **{
'sArg': 'TransferIntval' })), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckHasLockEnemy(oWarrior, oEventCB.GetCBLifeCycle()) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'MutantNum' }) + Func738(*a, **{
'sKey': 'MutantTransLockNum' }))) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MutantMaxNum'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 50, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, (lambda *a: 1 - Func518(*a, **{
'sAttr': 'AlreadyMutant' })))
        cl_evact.EventCBRemoveMonsterfromTargetList(oWarrior, oEventCB, WARRIOR_BOSS, FIGHT_KEY_WUDI)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8167, 1000, { }, 0, 0, 0)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1753, 0, { }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction4(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'PerformSID': 1753 })


class CPerform(CCustomPerform):
    m_SID = 51226
    m_Name = 'S7房间挑战异化传递'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

