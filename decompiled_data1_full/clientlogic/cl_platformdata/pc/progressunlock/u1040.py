# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1040.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1040.pyc
# Source Generated with Decompyle++
# File: u1040.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import LEVEL_TYPE_HIDE, PROGRESSUNLOCK_RELIC, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    if cl_evcon.CheckLayerAndLevel(oWarrior, oEventCB, 1, 1) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1040
    m_Type = PROGRESSUNLOCK_RELIC
    m_TargetValue = 3
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2141]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 5710

