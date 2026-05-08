# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39300.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39300.pyc
# Source Generated with Decompyle++
# File: pfai39300.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7355(oOwner, dInfo):
    return cl_condition.JudgeEnemyInSight(oOwner, 1, 0.5)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39300
    m_Name = '第六赛季硝石勇士'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7355,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7355: [
            1001] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = {
        7355: Condition7355 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST }

