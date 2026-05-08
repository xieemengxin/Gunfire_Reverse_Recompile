# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4148.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4148.pyc
# Source Generated with Decompyle++
# File: p4148.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func419

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 6, WARRIOR_MONSTER, 1, 0, 0, None, None, { }, None, None, None, None, None)
    cl_evact.CommonCBSetMonsterDis(oWarrior, oEventCB, 'pf4148')
    if cl_evcon.GetRecentDis(oWarrior, oEventCB, 'pf4148') >= 6:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'MoveSpeed', 0, 0)
    elif cl_evcon.GetRecentDis(oWarrior, oEventCB, 'pf4148') >= 2:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1003, 50, {
            'MoveSpeedMul': (lambda *a: Func419(*a, **{
'sBaseKey': 'pf4148' }) * 1000 - 7000) }, 1, 0, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1211, 50, { }, 1, None, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1003, 50, {
            'MoveSpeedMul': -5000 }, 1, 0, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1211, 50, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4148
    m_Name = '腐化反噬'
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

