# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1242.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1242.pyc
# Source Generated with Decompyle++
# File: u1242.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import DAM_TYPE_FIRE, OBJ_VICTIM, PROGRESSUNLOCK_WEAPON, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, None) or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20026, 0, 0, None, None):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1242
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 40
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2203]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 1104

