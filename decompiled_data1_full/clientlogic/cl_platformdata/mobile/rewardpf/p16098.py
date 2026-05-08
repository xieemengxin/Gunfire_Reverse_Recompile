# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16098.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16098.pyc
# Source Generated with Decompyle++
# File: p16098.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func590

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1854, 0, 0, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, None, None)
        cl_evact.EventExcludeTargetByState(oWarrior, oEventCB, 1854)
        cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, 1, 1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1854, (lambda *a: Func590(*a)), { }, 1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 16098
    m_Name = '处决大师2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

