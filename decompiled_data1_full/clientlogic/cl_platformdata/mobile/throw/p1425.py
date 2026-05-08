# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1425.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1425.pyc
# Source Generated with Decompyle++
# File: p1425.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TraceCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_LSTPOS

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 1:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 1024 })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 2:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 256 })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 3:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 512 })
        else:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCartoonEnd(skill, 6), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasBenediction(skill, 13544):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 1:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 1024 })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 2:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 256 })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[cl_action.GetCartoonLoopID(skill, 6)] % 10 == 3:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') }, dArgs = {
                'AddElementType': 512 })
        else:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1424, 'Att') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1]):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 30, targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 100, lockWeakness = False, lockAngle = 19, lockDis = 35, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)), 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        for i2 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)), 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1425
    m_Name = '#NT#占星飞牌'
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
        'CrazyEff': 0,
        'BulletSpeed': 100,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 1,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_PassRule = {
        1012: 1 }
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        iUseCardCnt = len(cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTINT))
        oSkill.m_Collect['UseCardCnt'] = iUseCardCnt
        super().UsePerform(oWarrior, oSkill)


