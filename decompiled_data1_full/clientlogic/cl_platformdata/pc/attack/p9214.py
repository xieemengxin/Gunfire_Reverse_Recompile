# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9214.pyc
# Source Generated with Decompyle++
# File: p9214.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import WARRIOR_OBSTACLE_NORMAL, OBSTACLE_JAR
from cl_commondefines import SKILLCACHE_LSTINT, SKILLCACHE_POS, SKILLCACHE_SIGNSPEED

def Action(skill):
    lstCache = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)
    vPosCache = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_SIGNSPEED)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.SetDirectHitInfo(skill, lstCache[0])
    cl_action.ModifySkillHitArea(skill, lstCache[1])
    cl_action.ModifySkillHitPos(skill, vPosCache)
    cl_action.WeaponDamage(skill, {
        'Att': 100 }, { }, sendPFMsg = False)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS,
        SKILLCACHE_LSTINT,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9214
    m_Name = '斩仙飞刀'
    m_ExtPerform = (4282, 9290)
    m_HaltInfo = {
        40108: 1,
        10214: 1,
        143: 1 }
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
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 0
    
    def GetSteadyCD(self, obj):
        return 0

    
    def CostBullet(self, oWarrior, oSkill):
        oCacheData = oSkill.m_CacheData
        lstCache = oCacheData.m_IntParaList
        if not lstCache:
            return None
        iVictim = lstCache[0]
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if not oVictim:
            return None
        if oVictim.m_FightType & WARRIOR_OBSTACLE_NORMAL == WARRIOR_OBSTACLE_NORMAL and OBSTACLE_JAR in oVictim.m_ClassifyList:
            oSkill.m_Collect['NoBulletUse'] = 1
        super(CPerform, self).CostBullet(oWarrior, oSkill)


