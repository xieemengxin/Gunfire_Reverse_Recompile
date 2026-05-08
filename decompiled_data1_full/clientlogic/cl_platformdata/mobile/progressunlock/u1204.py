# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/progressunlock/u1204.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/progressunlock/u1204.pyc
# Source Generated with Decompyle++
# File: u1204.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import PROGRESSUNLOCK_WEAPON
from cl_progressunlock.mobject import CProgressUnlockData as CCustom

def CBFunc(oEventCB, oWarrior):
    if not cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(CCustom):
    m_SID = 1204
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 10
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2123]
    m_CBFunc = CBFunc
    m_CountFunc = CountFunc
    m_RewardSID = 1010

