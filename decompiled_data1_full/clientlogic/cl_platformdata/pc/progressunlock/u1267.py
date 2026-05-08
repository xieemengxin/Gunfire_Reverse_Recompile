# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1267.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1267.pyc
# Source Generated with Decompyle++
# File: u1267.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import OBJ_VICTIM, PROGRESSUNLOCK_WEAPON, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 5, 0, 0):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1267
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 5
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2091]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 1608

