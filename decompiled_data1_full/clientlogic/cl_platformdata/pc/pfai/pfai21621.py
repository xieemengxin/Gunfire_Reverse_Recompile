# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21621.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21621.pyc
# Source Generated with Decompyle++
# File: pfai21621.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21621
    m_Name = '狙击怪-破盾狙击怪'
    m_FillBulletData = (38015, 3, 33)
    m_UseBulletPF = (21621,)
    m_PFGroup = {
        1001: {
            0: [
                21621,
                1,
                1,
                0] },
        1002: {
            0: [
                21612,
                1,
                1,
                0] },
        1003: {
            0: [
                38015,
                1,
                1,
                0] },
        1004: {
            0: [
                21622,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21621: [
            1001],
        21612: [
            1002],
        38015: [
            1003],
        21622: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (4, 15, 0, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 10 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }],
            (15, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

