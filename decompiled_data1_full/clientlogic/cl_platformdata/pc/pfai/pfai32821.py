# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai32821.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai32821.pyc
# Source Generated with Decompyle++
# File: pfai32821.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition32821(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 30041) <= 10


def Condition32822(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 32822) <= 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32821
    m_Name = '<一周目>精英召唤法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                32821,
                1,
                1,
                0] },
        1102: {
            0: [
                32821,
                2,
                2,
                0] },
        1103: {
            0: [
                32821,
                3,
                3,
                0] },
        1104: {
            0: [
                32825,
                1,
                1,
                0] },
        1201: {
            0: [
                32822,
                1,
                1,
                0] },
        1202: {
            0: [
                32822,
                2,
                2,
                0] },
        1203: {
            0: [
                32822,
                3,
                3,
                0] } }
    m_GroupOfPF = {
        32821: [
            1101,
            1102,
            1103],
        32825: [
            1104],
        32822: [
            1201,
            1202,
            1203] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 35, 0): [
                {
                    'choose': {
                        1103: 20,
                        1203: 1000 } }],
            (0, 99, -1, 100, 35, 60, 0): [
                {
                    'choose': {
                        1102: 20,
                        1202: 1000 } }],
            (0, 99, -1, 100, 60, 80, 0): [
                {
                    'choose': {
                        1101: 20,
                        1201: 1000,
                        1102: 20 } }],
            (0, 99, -1, 100, 80, 100, 0): [
                {
                    'choose': {
                        1101: 20,
                        1201: 1000,
                        1104: 20 } }] } }
    m_CheckPFCanUse = {
        32821: Condition32821,
        32822: Condition32822 }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST,
        1104: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1202: PF_GROUP_CHECK_FIRST,
        1203: PF_GROUP_CHECK_FIRST }

