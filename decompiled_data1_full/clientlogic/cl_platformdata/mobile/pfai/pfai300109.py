# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai300109.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai300109.pyc
# Source Generated with Decompyle++
# File: pfai300109.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300109
    m_Name = '投射怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7148, 1, 1, 0) },
        1004: {
            0: (7149, 1, 1, 0) },
        1002: {
            0: (7109, 1, 1, 0) },
        1003: {
            0: (7110, 1, 1, 0) },
        1005: {
            0: (7151, 1, 1, 0) },
        1006: {
            0: (7152, 1, 1, 0) } }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1002: 10 },
                'angle': (0, 135) }, {
                'choose': {
                    1003: 10 },
                'angle': (-135, 0) }, {
                'choose': {
                    1006: 10 },
                'angle': (135, 180) }, {
                'choose': {
                    1006: 10 },
                'angle': (-180, -135) }) },
        MONSTER_PFAI_CATCH: {
            (0, 3, 0, 100, -1, 100, 0): ({
                'choose': {
                    1005: 10 } },),
            (3, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1004: 10 } },) } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

