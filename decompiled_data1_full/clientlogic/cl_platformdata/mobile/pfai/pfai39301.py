# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39301.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39301.pyc
# Source Generated with Decompyle++
# File: pfai39301.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39301
    m_Name = '天袭分身'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                7176,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        7176: [
            1001] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 100, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL }

