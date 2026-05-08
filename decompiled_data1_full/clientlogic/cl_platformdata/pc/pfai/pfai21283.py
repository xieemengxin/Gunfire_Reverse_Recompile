# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21283.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21283.pyc
# Source Generated with Decompyle++
# File: pfai21283.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21283
    m_Name = '<三周目>【第四幕】弱点怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                21281,
                1,
                1,
                0] },
        1002: {
            0: [
                21282,
                2,
                2,
                0] },
        1003: {
            0: [
                38039,
                1,
                1,
                0] },
        1004: {
            0: [
                38040,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21281: [
            1001],
        21282: [
            1002],
        38039: [
            1003],
        38040: [
            1004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1004: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (8, 17, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }],
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

