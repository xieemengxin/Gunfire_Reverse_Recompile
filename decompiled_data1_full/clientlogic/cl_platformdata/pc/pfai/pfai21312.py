# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21312.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21312.pyc
# Source Generated with Decompyle++
# File: pfai21312.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition21311(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 7152) == 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21312
    m_Name = '<二周目>【新第二幕】蚂蚁盾兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21311,
                2,
                3,
                0] },
        1002: {
            0: [
                21312,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21311: [
            1001],
        21312: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 6, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (5, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 100 } }] } }
    m_CheckPFCanUse = {
        21311: Condition21311 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

