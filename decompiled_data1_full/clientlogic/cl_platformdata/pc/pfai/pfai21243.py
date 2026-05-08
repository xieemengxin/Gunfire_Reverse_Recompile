# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21243.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21243.pyc
# Source Generated with Decompyle++
# File: pfai21243.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21243
    m_Name = '<三周目>中型近战-霰弹枪兵'
    m_FillBulletData = (38012, 999, 0)
    m_UseBulletPF = (21241,)
    m_PFGroup = {
        1001: {
            0: [
                21241,
                1,
                1,
                0] },
        1004: {
            0: [
                38012,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21241: [
            1001],
        38012: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

