# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1029.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1029.pyc
# Source Generated with Decompyle++
# File: u1029.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import OBJ_VICTIM, PROGRESSUNLOCK_RELIC, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20026, None, None, None, None):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1029
    m_Type = PROGRESSUNLOCK_RELIC
    m_TargetValue = 30
    m_RoundLimit = 2
    m_TargetMonsterBase = [
        2282]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 5779

