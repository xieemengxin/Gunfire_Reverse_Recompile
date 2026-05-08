# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8008.pyc
# Source Generated with Decompyle++
# File: p8008.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_commondefines import SKILLCACHE_INT, SKILLCACHE_LSTINT
from cl_commondefines import SKILLCACHE_LSTINT

def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'DamAtt', defaultValue = 0) * cl_action.GetSkillCustomData(skill, 'DamTimes', defaultValue = 0) })
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8008
    m_Name = '被动触爆手雷'
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
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 10000,
        'BulletSpeed': 60,
        'DebuffProb': 1500,
        'ExplodeDelay': 170,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 1,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, SKILLCACHE_LSTINT, oSkill.m_Custom['LockTarget'])
        super().UsePerform(oWarrior, oSkill)


