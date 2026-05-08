# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1053.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1053.pyc
# Source Generated with Decompyle++
# File: u1053.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import PROGRESSUNLOCK_RELIC, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1053
    m_Type = PROGRESSUNLOCK_RELIC
    m_TargetValue = 30
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2041,
        2042]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 5814

