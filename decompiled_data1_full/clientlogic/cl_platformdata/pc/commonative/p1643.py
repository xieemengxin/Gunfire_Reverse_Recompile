# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1643.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1643.pyc
# Source Generated with Decompyle++
# File: p1643.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform.skillcache
from cl_perform.cartoon.defines import ChooseMonsterCartoon, CurveCartoon, ThrowByPowerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CHOOSE_RANDOM, CRT_CHECK_SERVER, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_LSTINT, SKILLCACHE_RANDOM

class CCartoon2(CurveCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'Damage')[cl_action.GetCartoonLoopID(skill, 2)] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[cl_action.GetCartoonLoopID(skill, 0)], cl_action.CrtArgTargetPos(skill, notContainDying = False), 1, 100, 30, 360, 0.5, targettype = OBJ_ENEMY, pierceblock = True, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, hittarger = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 0)])

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(ThrowByPowerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[cl_action.GetCartoonLoopID(skill, 4)], (cl_action.GetRandomInRange(skill, 1, 100), 0, cl_action.GetRandomInRange(skill, 1, 100)), 30, 0.3, (0, 18, 0), (1, 0), 2000, False, True, 0, 0, None, 0, innerRadius = 0, pierce = 1, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ChooseMonsterCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[cl_action.GetCartoonLoopID(skill, 3)], (0, 0, 0), [
                80], attshape = ATT_SHAPE_SPHERE, pierceStatic = False, ChooseType = CHOOSE_RANDOM, chooseSelfIfNoTargetInRange = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 3)])

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(ChooseMonsterCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 3))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[cl_action.GetCartoonLoopID(skill, 1)], (0, 0, 0), [
                30], attshape = ATT_SHAPE_SPHERE, pierceStatic = False, ChooseType = CHOOSE_RANDOM, chooseSelfIfNoTargetInRange = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 1)])

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ChooseMonsterCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[cl_action.GetCartoonLoopID(skill, 0)], (0, 0, 0), [
                20], attshape = ATT_SHAPE_SPHERE, pierceStatic = False, ChooseType = CHOOSE_RANDOM, chooseSelfIfNoTargetInRange = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 0)])

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChooseMonsterCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'Pos')[i1], (0, 0, 0), [
                10], attshape = ATT_SHAPE_SPHERE, pierceStatic = False, ChooseType = CHOOSE_RANDOM, chooseSelfIfNoTargetInRange = False, iVictim = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1643
    m_Name = '铭刻召唤跳弹'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    
    def UsePerform(self, oWarrior, oSkill):
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, SKILLCACHE_LSTINT, oSkill.m_Custom['Victim'])
        super().UsePerform(oWarrior, oSkill)


