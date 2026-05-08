# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39298.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39298.pyc
# Source Generated with Decompyle++
# File: pfai39298.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7351(oOwner, dInfo):
    return cl_condition.JudgeEnemyInSight(oOwner, 0.5, 0.85)


def Condition7338(oOwner, dInfo):
    return not cl_condition.CheckTargetHasFlag(oOwner, 'ForceNoDest')


def Condition7339(oOwner, dInfo):
    return not cl_condition.CheckTargetHasFlag(oOwner, 'ForceNoDest')


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39298
    m_Name = '招潮蟹'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7351,
                1,
                1,
                0] },
        1003: {
            0: [
                7338,
                1,
                1,
                0] },
        1004: {
            0: [
                7339,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7351: [
            1001],
        7338: [
            1003],
        7339: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10000,
                        1004: 10000,
                        1001: 10 } }] } }
    m_CheckPFCanUse = {
        7351: Condition7351,
        7338: Condition7338,
        7339: Condition7339 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

