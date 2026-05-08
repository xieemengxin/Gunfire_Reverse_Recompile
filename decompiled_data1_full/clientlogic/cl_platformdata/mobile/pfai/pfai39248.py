# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39248.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39248.pyc
# Source Generated with Decompyle++
# File: pfai39248.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, WARRIOR_MONSTER

def Condition7171(oOwner, dInfo):
    return cl_condition.AIGetRangeWarriorNum(oOwner, dInfo, 8, WARRIOR_MONSTER, 0, 0) >= 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39248
    m_Name = '园丁巨树植物'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7171,
                1,
                1,
                0] },
        1002: {
            0: [
                7170,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7171: [
            1001],
        7170: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 100, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 1000,
                        1002: 10 } }] } }
    m_CheckPFCanUse = {
        7171: Condition7171 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL,
        1002: PF_GROUP_CHECK_ALL }

