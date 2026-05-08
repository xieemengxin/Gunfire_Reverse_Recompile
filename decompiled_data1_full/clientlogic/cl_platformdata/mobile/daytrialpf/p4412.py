# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4412.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4412.pyc
# Source Generated with Decompyle++
# File: p4412.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MG_SOURCE_KILLMONSTER, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func426

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.CommonCBTargetDropReward(oWarrior, oEventCB, {
            103: (lambda *a: Func426(*a) + 1) }, {
            103: 10000 }, 0, MG_SOURCE_KILLMONSTER, None, None)


class CPerform(CCustomPerform):
    m_SID = 4412
    m_Name = '怪物额外掉落'
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

