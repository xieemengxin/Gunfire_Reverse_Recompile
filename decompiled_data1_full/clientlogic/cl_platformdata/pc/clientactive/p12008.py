# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12008.pyc
# Source Generated with Decompyle++
# File: p12008.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE

def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    cl_action.SetSkillCustomDataInt(skill, 'TriggerOrigin', cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
        cl_action.SendUseThrowPFMsg(skill)
        cl_action.CacheCountTransDamFactor(skill, 'pf1424', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12008
    m_Name = '赌侠召唤卡牌'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    
    def UsePerform(self, oWarrior, oSkill):
        iCardCnt = cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTINT)[0]
        oSkill.m_Collect['CardCnt'] = iCardCnt
        super().UsePerform(oWarrior, oSkill)


