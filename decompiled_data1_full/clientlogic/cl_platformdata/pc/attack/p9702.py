# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9702.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9702.pyc
# Source Generated with Decompyle++
# File: p9702.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9702
    m_Name = 's回旋镖'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1066
    m_CheckForbid = 1019
    
    def CanUse(self, oWarrior, dInfo):
        oSkillMgr = oWarrior.m_Game.m_SkillMgr
        lstSkill = oSkillMgr.GetSkillBySID(9213)
        for oSkill in lstSkill:
            if oSkill.m_Base['AID'] == oWarrior.m_ID:
                return 1
        
        return 0


