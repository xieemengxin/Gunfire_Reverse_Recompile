# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4312.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4312.pyc
# Source Generated with Decompyle++
# File: p4312.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 6, WARRIOR_HERO, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
    cl_evact.CommonCBSetMonsterDis(oWarrior, oEventCB, 'pf4148')
    if cl_evcon.GetRecentDis(oWarrior, oEventCB, 'pf4148') <= 6:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1003, 200, {
            'MoveSpeedMul': -3000 }, -1, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1205, 300, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 4312
    m_Name = '精英弱点怪-冰刃减速被动'
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
    m_DieDisable = 1

