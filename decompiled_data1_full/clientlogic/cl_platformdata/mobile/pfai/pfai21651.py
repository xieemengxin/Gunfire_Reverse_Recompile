# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21651.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21651.pyc
# Source Generated with Decompyle++
# File: pfai21651.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21651
    m_Name = '【第四幕】电狙击怪'
    m_FillBulletData = (38061, 10, 20)
    m_UseBulletPF = (21641,)
    m_PFGroup = {
        1001: {
            0: [
                21651,
                3,
                3,
                0] },
        1002: {
            0: [
                21652,
                1,
                1,
                0] },
        1003: {
            0: [
                21653,
                1,
                1,
                0] },
        1009: {
            0: [
                38061,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21651: [
            1001],
        21652: [
            1002],
        21653: [
            1003],
        38061: [
            1009] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (4, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST }

