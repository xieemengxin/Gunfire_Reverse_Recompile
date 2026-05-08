# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai22831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai22831.pyc
# Source Generated with Decompyle++
# File: pfai22831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22831
    m_Name = '吸血法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                22837,
                1,
                1,
                0],
            1: [
                22832,
                1,
                1,
                0],
            2: [
                22836,
                1,
                1,
                0] },
        1002: {
            0: [
                22831,
                1,
                1,
                0] },
        1003: {
            0: [
                22833,
                1,
                1,
                0] },
        1004: {
            0: [
                22834,
                1,
                1,
                0] },
        1005: {
            0: [
                22836,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22837: [
            1001],
        22832: [
            1001],
        22836: [
            1001,
            1005],
        22831: [
            1002],
        22833: [
            1003],
        22834: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1005: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 999,
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

