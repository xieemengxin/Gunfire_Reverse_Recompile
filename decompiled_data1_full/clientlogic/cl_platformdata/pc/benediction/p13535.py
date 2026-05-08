# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13535.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13535.pyc
# Source Generated with Decompyle++
# File: p13535.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32470) == 0:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1781):
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }) * 5), 0, DAM_TYPE_PERFORM, None, None)
        else:
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }) * 4), 0, DAM_TYPE_PERFORM, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1304, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }) / 10), 0)
        cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'Armor' })))
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32470, 10, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 13535
    m_Name = '孤注一掷'
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
    m_Career = 103

