# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39071.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39071.pyc
# Source Generated with Decompyle++
# File: pfai39071.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition39071(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39072(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39073(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39074(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39075(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39076(oOwner, dInfo):
    return oOwner.Phase() == 3


def Condition39077(oOwner, dInfo):
    return oOwner.Phase() == 3


def Condition39078(oOwner, dInfo):
    return oOwner.Phase() == 3


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39071
    m_Name = '组队boss-罗睺'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1011: {
            0: (39071, 1, 1, 0) },
        2021: {
            0: (39072, 1, 1, 0),
            1: (39072, 1, 1, 0),
            2: (39073, 1, 1, 0),
            3: (39074, 1, 1, 0) },
        2022: {
            0: (39072, 1, 1, 0),
            1: (39072, 1, 1, 0),
            2: (39073, 1, 1, 0),
            3: (39075, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1011: 10,
                    2021: 10,
                    2022: 10 } },) } }
    m_CheckPFCanUse = {
        39071: Condition39071,
        39072: Condition39072,
        39073: Condition39073,
        39074: Condition39074,
        39075: Condition39075,
        39076: Condition39076,
        39077: Condition39077,
        39078: Condition39078 }
    m_PFGroupCheck = {
        1011: PF_GROUP_CHECK_FIRST,
        2021: PF_GROUP_CHECK_FIRST,
        2022: PF_GROUP_CHECK_FIRST }

