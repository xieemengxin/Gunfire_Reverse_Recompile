# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai300112.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai300112.pyc
# Source Generated with Decompyle++
# File: pfai300112.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300112
    m_Name = 'DOOM测试'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7102, 1, 1, 0) },
        1002: {
            0: (7109, 1, 1, 0) },
        1003: {
            0: (7110, 1, 1, 0) },
        1004: {
            0: (7123, 3, 5, 0) },
        1005: {
            0: (7102, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1002: 10 },
                'angle': (0, 180) }, {
                'choose': {
                    1003: 10 },
                'angle': (-180, 0) }) },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): ({
                'choose': {
                    1005: 10 } },),
            (4, 10, -1, 50, -1, 100, 0): ({
                'choose': {
                    1004: 20,
                    1001: 10 } },),
            (4, 10, 50, 100, -1, 100, 0): ({
                'choose': {
                    1004: 10,
                    1001: 20 } },),
            (10, 20, -1, 100, -1, 100, 0): ({
                'choose': {
                    1004: 30,
                    1001: 10 } },),
            (20, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1004: 10 } },) } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

