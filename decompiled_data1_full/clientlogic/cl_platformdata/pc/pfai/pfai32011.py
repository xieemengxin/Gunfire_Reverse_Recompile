# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai32011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai32011.pyc
# Source Generated with Decompyle++
# File: pfai32011.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32011
    m_Name = '【第二幕】精英喷火怪'
    m_FillBulletData = (38013, 0, 100)
    m_UseBulletPF = (32011,)
    m_PFGroup = {
        1004: {
            0: [
                38013,
                1,
                1,
                0] },
        1101: {
            0: [
                32011,
                1,
                1,
                0] },
        1201: {
            0: [
                32012,
                1,
                1,
                0] },
        1202: {
            0: [
                32012,
                1,
                1,
                0] },
        1301: {
            0: [
                32013,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        38013: [
            1004],
        32011: [
            1101],
        32012: [
            1201,
            1202],
        32013: [
            1301] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (4, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 100 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1301: 100 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1004: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1202: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST }

