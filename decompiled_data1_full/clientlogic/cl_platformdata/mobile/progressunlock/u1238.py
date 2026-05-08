# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/progressunlock/u1238.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/progressunlock/u1238.pyc
# Source Generated with Decompyle++
# File: u1238.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import PROGRESSUNLOCK_WEAPON, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


class CProgressUnlockData(object):
    m_SID = 1238
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 30
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2222]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = None
    m_RewardSID = 1402

