# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai32822.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai32822.pyc
# Source Generated with Decompyle++
# File: pfai32822.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition32821(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 30041) <= 10


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32822
    m_Name = '精英召唤法师怪分身'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1301: {
            0: [
                32823,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        32823: [
            1301] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1301: 10 } }] } }
    m_CheckPFCanUse = {
        32821: Condition32821 }
    m_PFGroupCheck = {
        1301: PF_GROUP_CHECK_FIRST }

