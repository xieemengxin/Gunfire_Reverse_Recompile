# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai20061.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai20061.pyc
# Source Generated with Decompyle++
# File: pfai20061.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 20061
    m_Name = '【新三幕】跳脸怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                20061,
                1,
                1,
                0] },
        1002: {
            0: [
                20062,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        20061: [
            1001],
        20062: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }],
            (8, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

