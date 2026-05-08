# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai24011.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai24011.pyc
# Source Generated with Decompyle++
# File: pfai24011.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition24012(oOwner, dInfo):
    if cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 0) <= cl_condition.GetGamePlayerCnt(oOwner) * 1 + cl_condition.GetRound(oOwner) * 1 + 3 and cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 0) <= cl_condition.GetGamePlayerCnt(oOwner) * 1 + cl_condition.GetRound(oOwner) * 1 + 10:
        pass
    return cl_condition.AICheckHasState(oOwner, dInfo, 7123) == 0


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 24011
    m_Name = '【第四幕】巨型召唤怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                24011,
                1,
                1,
                0] },
        1002: {
            0: [
                24013,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        24011: [
            1001],
        24013: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1002: 50 } }] } }
    m_CheckPFCanUse = {
        24012: Condition24012 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

