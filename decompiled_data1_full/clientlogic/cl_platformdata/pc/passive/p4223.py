# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4223.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4223.pyc
# Source Generated with Decompyle++
# File: p4223.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FIGHT3_KEY_IGNELBEEXECUTED, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, OBJ_SELF, STATE_CLS_ABNORMAL, WARRIOR_MONSTER
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 5, 1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7986, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7990, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 6, 0, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNELBEEXECUTED)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)


def DoCallBackAction0(oEventCB, oWarrior):
    if not oWarrior.Energy() < 30000 and not cl_evcon.CheckHasState(oWarrior, oEventCB, 7995) or cl_evcon.CheckHasState(oWarrior, oEventCB, 8031):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 7990 }) * 100))
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7995, 0, { }, 0, 0, None)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 100, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, None, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeEnergy(oWarrior, oEventCB, 300)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 7982)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeEnergy(oWarrior, oEventCB, -30000)


def DoCallBackAction4(oEventCB, oWarrior):
    if oWarrior.Energy() == 30000:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7995, 0, { }, 0, 0, None)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 7994, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonSetSkillCheckArgs(oWarrior, oEventCB.GetCBLifeCycle(), 5, 15)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39245, 1, None):
        cl_action.CommonRemoveAllStateByType(oWarrior, oEventCB.GetCBLifeCycle(), STATE_CLS_ABNORMAL)


class CPerform(CCustomPerform):
    m_SID = 4223
    m_Name = '妖王时光流逝'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

