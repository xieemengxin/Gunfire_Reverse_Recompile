# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21831.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21831.pyc
# Source Generated with Decompyle++
# File: pfai21831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21831
    m_Name = '重型近战-蟹先锋'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21833,
                1,
                1,
                0] },
        1002: {
            0: [
                21831,
                1,
                1,
                0] },
        1003: {
            0: [
                21832,
                1,
                1,
                0] },
        1004: {
            0: [
                21831,
                1,
                1,
                0],
            1: [
                21832,
                1,
                1,
                0] },
        1005: {
            0: [
                21833,
                1,
                1,
                0],
            1: [
                21832,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21833: [
            1001,
            1005],
        21831: [
            1002,
            1004],
        21832: [
            1003,
            1004,
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 1,
                        1004: 150,
                        1005: 50 } }],
            (8, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        1002: 40,
                        1003: 70 } }],
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 100,
                        1002: 1,
                        1003: 50 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

