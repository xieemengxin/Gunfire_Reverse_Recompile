# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai300106.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai300106.pyc
# Source Generated with Decompyle++
# File: pfai300106.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300106
    m_Name = '举盾连射'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7134, 1, 1, 0) },
        1003: {
            0: (7143, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): ({
                'choose': {
                    1003: 10 } },),
            (4, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10 } },) } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST }

