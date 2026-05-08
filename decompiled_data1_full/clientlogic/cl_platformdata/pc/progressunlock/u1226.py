# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1226.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1226.pyc
# Source Generated with Decompyle++
# File: u1226.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import PROGRESSUNLOCK_WEAPON, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    if not cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(object):
    m_SID = 1226
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 10
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2123]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 1010

