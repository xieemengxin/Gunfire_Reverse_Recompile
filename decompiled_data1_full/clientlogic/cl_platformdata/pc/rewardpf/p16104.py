# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16104.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16104.pyc
# Source Generated with Decompyle++
# File: p16104.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import CREATE_PLANT, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CLIENTACTIVE, PLANT_PHASE_NORMAL
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CLIENTACTIVE, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CLIENTACTIVE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 5, 0, 0)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12031, 0, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ThrowType' }))) == 6:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.EventCBCheckSeedOrPlantPos(oWarrior, oEventCB, 1, None):
        cl_evact.EventCBCreateSeed(oWarrior, oEventCB, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12031, 0, 0):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 500)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.CommonCheckGardenerFieldSeedInfo(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.CommonHatchTargetSeed(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonRandomGetFieldSeed(oWarrior, oEventCB.GetCBLifeCycle()), PLANT_PHASE_NORMAL)
    else:
        cl_evact.EventCBCreatePlantInPos(oWarrior, oEventCB, 1, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33859, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 16104
    m_Name = '园丁灵气模块1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

