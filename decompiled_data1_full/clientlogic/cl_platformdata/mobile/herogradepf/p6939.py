# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6939.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6939.pyc
# Source Generated with Decompyle++
# File: p6939.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1329, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1331, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1335, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1435, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1332, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1334, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1337, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Att', 0, 10000)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 0, 1, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 6939
    m_Name = '#NT#游猎者lvl.4'
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

