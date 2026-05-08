# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21251.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21251.pyc
# Source Generated with Decompyle++
# File: pfai21251.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21251
    m_Name = '【第二幕】中型近战-中型盾兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21251,
                1,
                1,
                0] },
        1002: {
            0: [
                21252,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21251: [
            1001],
        21252: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (4, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 70,
                        1002: 15 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

