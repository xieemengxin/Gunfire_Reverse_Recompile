# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai300107.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai300107.pyc
# Source Generated with Decompyle++
# File: pfai300107.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7141(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7012)


def Condition7102(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7013)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300107
    m_Name = '小盾兵举盾连射'
    m_FillBulletData = (7136, 15, 3)
    m_UseBulletPF = (7102, 7141)
    m_PFGroup = {
        1001: {
            0: (7102, 1, 1, 0) },
        1002: {
            0: (7136, 1, 1, 0) },
        1003: {
            0: (7141, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1003: 10 } },) } }
    m_CheckPFCanUse = {
        7141: Condition7141,
        7102: Condition7102 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST }

