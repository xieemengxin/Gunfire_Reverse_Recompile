# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai22011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai22011.pyc
# Source Generated with Decompyle++
# File: pfai22011.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22011
    m_Name = '重型远程-喷火怪'
    m_FillBulletData = (38013, 0, 100)
    m_UseBulletPF = (22011, 22012)
    m_PFGroup = {
        1001: {
            0: [
                22011,
                1,
                1,
                0] },
        1004: {
            0: [
                38013,
                1,
                1,
                0] },
        1005: {
            0: [
                22012,
                1,
                1,
                0] },
        1006: {
            0: [
                22013,
                1,
                1,
                0],
            1: [
                22012,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22011: [
            1001],
        38013: [
            1004],
        22012: [
            1005,
            1006],
        22013: [
            1006] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (8, 100, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 100 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1006: 80 } }],
            (5, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 30,
                        1005: 70 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

