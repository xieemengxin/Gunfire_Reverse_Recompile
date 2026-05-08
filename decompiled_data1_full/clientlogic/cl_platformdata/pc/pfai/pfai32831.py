# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai32831.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai32831.pyc
# Source Generated with Decompyle++
# File: pfai32831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST, WARRIOR_MONSTER

def Condition32838(oOwner, dInfo):
    if cl_condition.AICheckHasState(oOwner, dInfo, 7067):
        pass
    return cl_condition.AIGetRangeWarriorNum(oOwner, dInfo, 30, WARRIOR_MONSTER, 1, 0) > 0


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32831
    m_Name = '【第三幕】精英吸血法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                32837,
                1,
                1,
                0],
            1: [
                32832,
                1,
                1,
                0],
            2: [
                32836,
                1,
                1,
                0] },
        1002: {
            0: [
                32831,
                1,
                1,
                0] },
        1003: {
            0: [
                32833,
                1,
                1,
                0] },
        1004: {
            0: [
                32834,
                1,
                1,
                0] },
        1005: {
            0: [
                32838,
                1,
                1,
                0],
            1: [
                32835,
                1,
                1,
                0] },
        1006: {
            0: [
                32836,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        32837: [
            1001],
        32832: [
            1001],
        32836: [
            1001,
            1006],
        32831: [
            1002],
        32833: [
            1003],
        32834: [
            1004],
        32838: [
            1005],
        32835: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1006: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1006: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 99,
                        1002: 10,
                        1005: 9999 } }] } }
    m_CheckPFCanUse = {
        32838: Condition32838 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

