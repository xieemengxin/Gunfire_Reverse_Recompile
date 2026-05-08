# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50330.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50330.pyc
# Source Generated with Decompyle++
# File: p50330.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILLCACHE_POS

def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
        if cl_action.CountDistance(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) <= 5:
            cl_action.SwitchDeviceFollowMoveStatus(skill, 1)
            cl_action.ArrangeDevice(skill, cl_action.GetGroundPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)), cl_action.CrtArgSelfFace(skill), { }, 0)
        else:
            cl_action.ArrangeDevice(skill, cl_action.GetNearestSpaceByPos(skill, cl_action.GetPosByPointDistance(skill, 5)), cl_action.CrtArgSelfFace(skill), { }, 0)
            cl_action.SwitchDeviceFollowMoveStatus(skill, 0)
            cl_action.SetDeviceMovePos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_PERFORM_POS_ARRANGE

class CPerform(CCustomPerform):
    m_SID = 50330
    m_Name = '炮台部署'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = { }
    m_Pos = DEVICE_PERFORM_POS_ARRANGE
    m_ForbidRule = 1091

