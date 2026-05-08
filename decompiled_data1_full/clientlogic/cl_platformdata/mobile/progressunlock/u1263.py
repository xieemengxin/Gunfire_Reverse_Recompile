# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/progressunlock/u1263.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/progressunlock/u1263.pyc
# Source Generated with Decompyle++
# File: u1263.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_evcon import CountByKillInfo
from cl_commondefines import KILL_INFO_DAM3_WEAKNESS, PROGRESSUNLOCK_WEAPON, UNLOCK_TRIGGER_KILL

def CBFunc(oEventCB, oWarrior):
    if cl_evcon.CheckConformKillMethod(oWarrior, oEventCB, KILL_INFO_DAM3_WEAKNESS):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return CountByKillInfo(dKillInfo, KILL_INFO_DAM3_WEAKNESS)


class CProgressUnlockData(object):
    m_SID = 1263
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 15
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2021]
    m_CBFunc = CBFunc
    m_TriggerType = UNLOCK_TRIGGER_KILL
    m_CountFunc = CountFunc
    m_RewardSID = 1016

