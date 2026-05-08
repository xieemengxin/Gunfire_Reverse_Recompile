# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/progressunlock/u1057.pyc
# RelativePath: clientlogic/cl_platformdata/pc/progressunlock/u1057.pyc
# Source Generated with Decompyle++
# File: u1057.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import PROGRESSUNLOCK_RELIC, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


class CProgressUnlockData(object):
    m_SID = 1057
    m_Type = PROGRESSUNLOCK_RELIC
    m_TargetValue = 20
    m_RoundLimit = 2
    m_TargetMonsterBase = [
        2122]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = None
    m_RewardSID = 5820

