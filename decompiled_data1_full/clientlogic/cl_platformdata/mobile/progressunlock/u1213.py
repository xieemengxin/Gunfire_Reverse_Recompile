# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/progressunlock/u1213.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/progressunlock/u1213.pyc
# Source Generated with Decompyle++
# File: u1213.pyc (Python 3.6)

import cl_evcon
import cl_evact
from cl_commondefines import DAM_TYPE_CORRISION, PROGRESSUNLOCK_WEAPON
from cl_progressunlock.mobject import CProgressUnlockData as CCustom

def CBFunc(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION):
        cl_evact.EventCBAddUnlockProgress(oWarrior, oEventCB, 1)


def CountFunc(dKillInfo):
    return 0


class CProgressUnlockData(CCustom):
    m_SID = 1213
    m_Type = PROGRESSUNLOCK_WEAPON
    m_TargetValue = 40
    m_RoundLimit = 1
    m_TargetMonsterBase = [
        2124]
    m_CBFunc = CBFunc
    m_CountFunc = CountFunc
    m_RewardSID = 1309

