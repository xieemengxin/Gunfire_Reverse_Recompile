# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39247.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39247.pyc
# Source Generated with Decompyle++
# File: pfai39247.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, WARRIOR_MONSTER

def Condition7171(oOwner, dInfo):
    return cl_condition.AIGetRangeWarriorNum(oOwner, dInfo, 8, WARRIOR_MONSTER, 0, 0) >= 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39247
    m_Name = '园丁植物'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7168,
                1,
                1,
                0] },
        1002: {
            0: [
                7171,
                1,
                1,
                0] },
        1003: {
            0: [
                7170,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7168: [
            1001],
        7171: [
            1002],
        7170: [
            1003] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 100, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        1001: 10 } }],
            (0, 100, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1002: 1000,
                        1003: 10 } }],
            (0, 100, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = {
        7171: Condition7171 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL,
        1002: PF_GROUP_CHECK_ALL,
        1003: PF_GROUP_CHECK_ALL }

