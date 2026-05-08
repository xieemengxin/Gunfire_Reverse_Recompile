# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39245.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39245.pyc
# Source Generated with Decompyle++
# File: pfai39245.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL

def Condition7142(oOwner, dInfo):
    if cl_condition.JudgeEnemyInSight(oOwner, 0.6, 0.5):
        pass
    return cl_condition.JudgeEnemyAccessible(oOwner)


def Condition7143(oOwner, dInfo):
    if cl_condition.JudgeEnemyAccessible(oOwner) == False:
        pass
    return cl_condition.JudgeEnemyInSight(oOwner, 0.7, 0.5)


def Condition7141(oOwner, dInfo):
    if cl_condition.JudgeEnemyInSight(oOwner, 0.5, 0.5):
        pass
    return cl_condition.JudgeEnemyAccessible(oOwner)


def Condition7150(oOwner, dInfo):
    return cl_condition.JudgeEnemyInSight(oOwner, 0.7, 0.5)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39245
    m_Name = '御灵师机甲'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7141,
                1,
                1,
                0] },
        1002: {
            0: [
                7142,
                1,
                1,
                0] },
        1003: {
            0: [
                7144,
                1,
                1,
                0] },
        1005: {
            0: [
                7148,
                1,
                1,
                0] },
        1006: {
            0: [
                7143,
                1,
                1,
                0] },
        1007: {
            0: [
                7150,
                1,
                1,
                0] },
        1008: {
            0: [
                7151,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7141: [
            1001],
        7142: [
            1002],
        7144: [
            1003],
        7148: [
            1005],
        7143: [
            1006],
        7150: [
            1007],
        7151: [
            1008] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 7, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1007: 1000,
                        1006: 1,
                        1005: 100,
                        1001: 10 } }],
            (7, 18, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1007: 1000,
                        1006: 1,
                        1002: 10 } }],
            (18, 40, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1007: 1000,
                        1006: 1 } }],
            (0, 40, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        1008: 1000,
                        1003: 1 } }] } }
    m_CheckPFCanUse = {
        7142: Condition7142,
        7143: Condition7143,
        7141: Condition7141,
        7150: Condition7150 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL,
        1002: PF_GROUP_CHECK_ALL,
        1003: PF_GROUP_CHECK_ALL,
        1005: PF_GROUP_CHECK_ALL,
        1006: PF_GROUP_CHECK_ALL,
        1007: PF_GROUP_CHECK_ALL,
        1008: PF_GROUP_CHECK_ALL }

