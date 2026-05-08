# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai300108.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai300108.pyc
# Source Generated with Decompyle++
# File: pfai300108.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7116(oOwner, dInfo):
    return cl_condition.GetMonsterSummonCnt(oOwner, dInfo, 0) <= 4


def Condition7126(oOwner, dInfo):
    return cl_condition.GetWinkDisSubTargetDis(oOwner, dInfo) <= 0.5


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300108
    m_Name = 'BOSS'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7137, 1, 1, 0) },
        1002: {
            0: (7116, 1, 1, 0) },
        1003: {
            0: (7112, 1, 1, 0) },
        1004: {
            0: (7138, 1, 1, 0) },
        1005: {
            0: (7139, 1, 1, 0) },
        1006: {
            0: (7140, 1, 1, 0) },
        1008: {
            0: (7126, 1, 1, 0) },
        1009: {
            0: (7170, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 5, -1, 50, -1, 100, 0): ({
                'choose': {
                    1003: 10 } },),
            (5, 99, -1, 50, -1, 100, 0): ({
                'choose': {
                    1001: 5,
                    1004: 5,
                    1008: 10 } },),
            (0, 99, 50, 75, -1, 100, 0): ({
                'choose': {
                    1002: 5,
                    1001: 1,
                    1004: 1,
                    1005: 10,
                    1006: 75,
                    1009: 10 } },),
            (0, 99, 75, 85, -1, 100, 0): ({
                'choose': {
                    1002: 10,
                    1001: 1,
                    1004: 1,
                    1005: 45,
                    1006: 10,
                    1009: 35 } },),
            (0, 99, 85, 95, -1, 100, 0): ({
                'choose': {
                    1002: 60,
                    1001: 1,
                    1004: 1,
                    1005: 15,
                    1006: 5,
                    1009: 20 } },),
            (0, 5, 95, 100, -1, 100, 0): ({
                'choose': {
                    1003: 10 } },),
            (5, 99, 95, 100, -1, 100, 0): ({
                'choose': {
                    1004: 10,
                    1001: 10 } },) } }
    m_CheckPFCanUse = {
        7116: Condition7116,
        7126: Condition7126 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST }

