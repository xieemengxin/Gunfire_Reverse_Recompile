# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13731.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13731.pyc
# Source Generated with Decompyle++
# File: p13731.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COMMONACTIVE_TAG_S7_ATTACKPERFORM, DAM_MASK_ELEMENT, OBJ_ATTACK, PET_ENTER_BATTLE, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func839, Func840

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33954, 0, {
        'StatusEffect': 800 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerfromInActivePerformTag(oWarrior, oEventCB, COMMONACTIVE_TAG_S7_ATTACKPERFORM):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 10000 + Func717(*a, **{
'sArg': 'ExtraAddDam' })), DAM_MASK_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraAddDam', (lambda *a: 800 * min(50, Func839(*a) + Func840(*a) * 4)))
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33954, (lambda *a: min(50, Func839(*a) + Func840(*a) * 4)), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetEventPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33947, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'ExtraAddDam' }) + 10000) }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 13731
    m_Name = '符力回响'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

