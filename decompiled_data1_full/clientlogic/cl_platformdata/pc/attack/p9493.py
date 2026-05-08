# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9493.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9493.pyc
# Source Generated with Decompyle++
# File: p9493.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_commondefines import SKILLCACHE_PERFORMMODE

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

from cl_perform.attack import CContinuousPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9493
    m_Name = 's毒手套'
    m_ExtPerform = (9492,)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 30,
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1045
    m_PassRule = {
        1012: 1 }
    m_CheckForbid = 1019
    
    def UsePerform(self, oWarrior, oSkill):
        super().UsePerform(oWarrior, oSkill)
        iPerformMode = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PERFORMMODE)
        if iPerformMode:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERQTE, oWarrior, { })


