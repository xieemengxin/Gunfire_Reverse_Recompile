# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50017.pyc
# Source Generated with Decompyle++
# File: p50017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12019, 1, 0) and cl_evcon.CheckSelfAllBagBulletRatio(oWarrior, oEventCB, 60):
        cl_action.CommonRandomDeductWeaponBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 2, 0, 1)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 25000, DAM_TYPE_PERFORM, None, None)


class CPerform(CCustomPerform):
    m_SID = 50017
    m_Name = '剧毒针刺'
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
    m_GrowPF = []
    m_DamagePF = []

