# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21823.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21823.pyc
# Source Generated with Decompyle++
# File: pfai21823.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21823
    m_Name = '<三周目>重型近战-大胖坦克兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21822,
                1,
                1,
                0] },
        1002: {
            0: [
                21821,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21822: [
            1001],
        21821: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 15,
                        1002: 85 } }],
            (8, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 25,
                        1002: 75 } }],
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 55,
                        1002: 45 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

