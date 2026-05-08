# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai22821.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai22821.pyc
# Source Generated with Decompyle++
# File: pfai22821.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition22821(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 20041) + cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 30041) <= 10


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22821
    m_Name = '召唤法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                22821,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22821: [
            1101] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }] } }
    m_CheckPFCanUse = {
        22821: Condition22821 }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST }

