# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai22851.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai22851.pyc
# Source Generated with Decompyle++
# File: pfai22851.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition22851(oOwner, dInfo):
    return cl_condition.CheckMonsterHinderNum(oOwner, 12, 1)


def Condition22851_3_9(oOwner, dInfo):
    return cl_condition.CheckMonsterHinderNum(oOwner, 15, 1)


def Condition22851_3_10(oOwner, dInfo):
    return cl_condition.CheckMonsterHinderNum(oOwner, 15, 1)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22851
    m_Name = '明雷法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                22851,
                1,
                1,
                0] },
        1002: {
            0: [
                22852,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22851: [
            1001],
        22852: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 100,
                        1002: 1 } }] } }
    m_CheckPFCanUse = {
        22851: Condition22851 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }
    m_CheckPFCanUseByDifficulty = {
        (3, 10): {
            22851: Condition22851_3_10 },
        (3, 9): {
            22851: Condition22851_3_9 } }

