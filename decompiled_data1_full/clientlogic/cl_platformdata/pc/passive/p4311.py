# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4311.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4311.pyc
# Source Generated with Decompyle++
# File: p4311.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, WARRIOR_SUMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 6, WARRIOR_SUMMON, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
    cl_evact.CommonCBSetMonsterDis(oWarrior, oEventCB, 'pf4148')
    if cl_evcon.GetRecentDis(oWarrior, oEventCB, 'pf4148') <= 6:
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 4253, 0)
    else:
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 4252, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 6, WARRIOR_SUMMON, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
    cl_evact.CommonCBSetMonsterDis(oWarrior, oEventCB, 'pf4148')
    if cl_evcon.GetRecentDis(oWarrior, oEventCB, 'pf4148') <= 6:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -5000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4311
    m_Name = '精英弱点怪-减伤被动'
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
    m_DieDisable = 1

