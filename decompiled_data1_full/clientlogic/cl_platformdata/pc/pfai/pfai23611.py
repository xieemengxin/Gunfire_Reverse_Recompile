# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai23611.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai23611.pyc
# Source Generated with Decompyle++
# File: pfai23611.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 23611
    m_Name = '炮灰怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                23611,
                1,
                1,
                0] },
        1004: {
            0: [
                38028,
                1,
                1,
                0] },
        1005: {
            0: [
                38029,
                1,
                1,
                0] },
        1002: {
            0: [
                23612,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        23611: [
            1001],
        38028: [
            1004],
        38029: [
            1005],
        23612: [
            1002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1005: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (5, 9, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 100 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST }

