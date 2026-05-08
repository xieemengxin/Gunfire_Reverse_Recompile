# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p21812.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p21812.pyc
# Source Generated with Decompyle++
# File: p21812.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityParabolaCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALLNOSELF, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_HERO, WARRIOR_MONSTER

class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 80)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 80, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(EntityParabolaCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 4)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALLNOSELF):
            cl_action.PushVictim(skill, cl_action.GetCartoonCurPos(skill, 4), 10, 3, 10000, angle = 315)
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALLNOSELF):
            cl_action.PushHeroVictim(skill, cl_action.GetCartoonCurPos(skill, 4), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 315)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_math.Vec3Minus(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY))), 20, 0.1, (0, 18, 0), (0, 0), (0, 0), 500, False, False, 0, False, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), 0, targetType = OBJ_ALLNOSELF, maxDistance = cl_math.CalDistance3D(cl_action.GetSceneObjPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY)), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))) + 0.01, hitHeroOver = False, forceSpeed = True, innerRadius = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) != 0:
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), True, 0, (0, 0, 0), parentName = '')
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 7966, 0, 1, { })
    cl_action.AttackerAddState(skill, 7075, 0, 1, { })
    cl_action.LockMonsterAttackerFace(skill)
    cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetSkillCustomData(skill, 'summoncreate'))
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 21812
    m_Name = '【第三幕】重型锁链兵-打断回收锁链'
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
        'AttDistance': 20,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_THUNDER
    m_UseHeight = 2
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1050
    m_CacheAttr = [
        'DebuffProb']

