# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai300126.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai300126.pyc
# Source Generated with Decompyle++
# File: pfai300126.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7147(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7020)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300126
    m_Name = '位面兽'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7147, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10 } },) } }
    m_CheckPFCanUse = {
        7147: Condition7147 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST }

