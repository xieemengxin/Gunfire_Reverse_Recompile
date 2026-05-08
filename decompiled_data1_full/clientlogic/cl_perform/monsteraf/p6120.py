# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6120.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6120.pyc
# Source Generated with Decompyle++
# File: p6120.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_SEASONWAND, PF_SUBMSG_COMMON, WARRIOR_ELIBADGER, WARRIOR_ELIDART, WARRIOR_ELIFOOT, WARRIOR_ELIHEVFAR, WARRIOR_ELIHEVNEAR, WARRIOR_ELIMAGIC, WARRIOR_ELIMEDFAR, WARRIOR_ELIMEDNEAR, WARRIOR_ELIRIDE, WARRIOR_ELISMAFAR, WARRIOR_ELISMANEAR, WARRIOR_ELISNIPE, WARRIOR_ELITHROW, WARRIOR_NORBADGER, WARRIOR_NORFOOT, WARRIOR_NORHEVFAR, WARRIOR_NORHEVNEAR, WARRIOR_NORSMAFAR, WARRIOR_NORSMANEAR
from cl_newformula import Func767

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1741, 'Count', 3, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func767(*a))):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1741)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1741, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1741, 1, 1):
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1741, { })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMANEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORFOOT) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMAFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORSMAFAR):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1741, 'OutRadius', 500, None)
    elif cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORBADGER):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1741, 'OutRadius', 300, None)
    elif cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIBADGER) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIDART) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIFOOT) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIHEVFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIHEVNEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMAGIC) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMEDFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIMEDNEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELIRIDE) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISMAFAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISMANEAR) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELISNIPE) or cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITHROW):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1741, 'OutRadius', 1000, 1)
    elif not cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORHEVFAR):
        pass
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_NORHEVNEAR):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1741, 'OutRadius', 800, 1)
    else:
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1741, 'OutRadius', 700, 1)


class CPerform(CCustomPerform):
    m_SID = 6120
    m_Name = '星轨'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (1741,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_SEASONWAND

