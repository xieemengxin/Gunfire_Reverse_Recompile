# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai300123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai300123.pyc
# Source Generated with Decompyle++
# File: pfai300123.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition7104(oOwner, dInfo):
    return cl_condition.GetFallBackPos(oOwner, dInfo, 3, 5, 170, 180)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 300123
    m_Name = '美术A游击怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: (7123, 3, 5, 0) },
        1002: {
            0: (7109, 1, 1, 0) },
        1003: {
            0: (7110, 1, 1, 0) },
        1004: {
            0: (7102, 1, 1, 0) },
        1005: {
            0: (7104, 1, 1, 0) } }
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
            (0, 5, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1004: 10,
                    1005: 100 } },),
            (5, 99, -1, 100, -1, 100, 0): ({
                'choose': {
                    1001: 10,
                    1004: 10 } },) } }
    m_CheckPFCanUse = {
        7104: Condition7104 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

