# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai300121.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai300121.pyc
# Source Generated with Decompyle++
# File: pfai300121.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300121
    m_Name = '美术B精英怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7129, 1, 1, 0) },
        1002: {
            0: (7109, 1, 1, 0) },
        1003: {
            0: (7110, 1, 1, 0) },
        1004: {
            0: (7130, 1, 1, 0) },
        1005: {
            0: (7131, 1, 1, 0) } }
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
            (8, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1004: 30 } },),
            (5, 8, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 30,
                    1004: 10 } },),
            (0, 5, -1, 100, -1, 100, 0): ({
                'choose': {
                    1005: 10 } },) } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

