# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai300105.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai300105.pyc
# Source Generated with Decompyle++
# File: pfai300105.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300105
    m_Name = '投雷'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7107, 1, 1, 0) },
        1002: {
            0: (7119, 1, 1, 0) },
        1003: {
            0: (7120, 1, 1, 0) },
        1004: {
            0: (7121, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1002: 10,
                    1003: 10,
                    1004: 10 } },) } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

