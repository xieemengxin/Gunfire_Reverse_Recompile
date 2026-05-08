# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21811.pyc
# Source Generated with Decompyle++
# File: pfai21811.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21811
    m_Name = '【第三幕】重型锁链怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21811,
                1,
                1,
                0] },
        1002: {
            0: [
                21812,
                1,
                1,
                0] },
        1003: {
            0: [
                21813,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21811: [
            1001],
        21812: [
            1002],
        21813: [
            1003] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 } }],
            (4, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST }

