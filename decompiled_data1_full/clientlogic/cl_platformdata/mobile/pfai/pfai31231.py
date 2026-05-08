# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai31231.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai31231.pyc
# Source Generated with Decompyle++
# File: pfai31231.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition31233(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 21013) <= 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31231
    m_Name = '中型近战-精英中型盾兵'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                31231,
                1,
                1,
                0] },
        1002: {
            0: [
                31232,
                1,
                1,
                0] },
        1003: {
            0: [
                31233,
                1,
                1,
                0] },
        1004: {
            0: [
                31233,
                2,
                2,
                0] },
        1005: {
            0: [
                31233,
                3,
                3,
                0] } }
    m_GroupOfPF = {
        31231: [
            1001],
        31232: [
            1002],
        31233: [
            1003,
            1004,
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (4, 99, -1, 30, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1005: 999 } }],
            (0, 4, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (4, 99, 30, 60, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1004: 999 } }],
            (0, 4, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (4, 99, 60, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1003: 999 } }] } }
    m_CheckPFCanUse = {
        31233: Condition31233 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

