# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5373.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5373.pyc
# Source Generated with Decompyle++
# File: p5373.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, NWARRIOR_DROP_SUMMONSOUL, STATE_EFF_CONTROL
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, 0)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_CONTROL, 1)
    cl_action.CommonSetPyFlag(oWarrior, oLifeCycle, PY_FLAG_EXCLUDEMONSTERHATE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7356, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AttCount', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttCount') >= 20:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AttCount', -20)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7357, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_SUMMONSOUL):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PickCount', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PickCount') >= 5:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PickCount', -5)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 7357, { })


class CPerform(CCustomPerform):
    m_SID = 5373
    m_Name = '#NT#召唤法杖魂体初始被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

