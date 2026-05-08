# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51679.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51679.pyc
# Source Generated with Decompyle++
# File: p51679.pyc (Python 3.6)

from cl_platformdata.custom.passive.customaction import CustomAction51679 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import MAIN_HOLD, S7_MODULE_POINT_CHANGE
from cl_newformula import Func524, Func717, Func839, Func843, Func857

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Time', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Time', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', (lambda *a: 45 + min(int(Func839(*a)), 20)))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Time', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CommonCheckInPointWandByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, 1202):
        CustomAction(oWarrior, oEventCB, {
            'CostRatio': (lambda *a: Func717(*a, **{
'sArg': 'CostRatio' })),
            'Time': (lambda *a: Func717(*a, **{
'sArg': 'Time' })),
            'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })),
            'TupleBullet': (4502, 4503, 4504),
            'StateId': 39758 })
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func857(*a) - Func524(*a) * Func717(*a, **{
'sArg': 'CostRatio' }) // 100)) >= 0:
        cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func843(*a)), (lambda *a: -Func524(*a) * Func717(*a, **{
'sArg': 'CostRatio' }) // 100), 0)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39758, (lambda *a: Func717(*a, **{
'sArg': 'Time' })), {
            'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })) }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'SpeedAddRatio', (lambda *a: 45 + min(int(Func839(*a)), 20)))


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB):
        if cl_condition.CommonCheckInPointWandByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, 1202):
            CustomAction(oWarrior, oEventCB, {
                'CostRatio': (lambda *a: Func717(*a, **{
'sArg': 'CostRatio' })),
                'Time': (lambda *a: Func717(*a, **{
'sArg': 'Time' })),
                'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })),
                'TupleBullet': (4502, 4503, 4504),
                'StateId': 39758 })
        elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func857(*a) - Func524(*a) * Func717(*a, **{
'sArg': 'CostRatio' }) // 100)) >= 0:
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func843(*a)), (lambda *a: -Func524(*a) * Func717(*a, **{
'sArg': 'CostRatio' }) // 100), 0)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39758, (lambda *a: Func717(*a, **{
'sArg': 'Time' })), {
                'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51679
    m_Name = '次要技能-轻装上阵'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

