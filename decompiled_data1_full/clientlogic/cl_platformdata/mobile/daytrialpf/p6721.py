# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6721.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6721.pyc
# Source Generated with Decompyle++
# File: p6721.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX, WARRIOR_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0 and cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3165: 1 }) == 0:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 100)
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0)
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0)
    else:
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, -5000)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3165: 1 }):
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, -7000)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', 0, -8000)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', 0, -8000)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, -6000)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', 0, -6000)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', 0, -6000)


class CPerform(CCustomPerform):
    m_SID = 6721
    m_Name = '怪物血量降低'
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

