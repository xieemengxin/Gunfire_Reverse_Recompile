# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1738.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1738.pyc
# Source Generated with Decompyle++
# File: p1738.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL_PLAYER, SKILLCACHE_LSTPOS, SKILLCACHE_POS, WARRIOR_HERO

class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cl_action.DeleteClientEffect(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 175, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 50 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 1) - 1)], (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL_PLAYER, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 1) - 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 46, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)))

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 2037, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 311, (0, 0, 0))
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 140, 1, {
            'Radius': 3 }, 32248, 311, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)

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
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) > 0:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 90, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cl_action.SetSkillServerCache(skill, 'ChooseHeros', cl_action.GetRangeTargetByPointTarget(skill, cl_action.GetSkillAID(skill), 20, True, 1, bSort = False, bChooseHero = True))
        if len(cl_action.GetSkillServerCache(skill, 'ChooseHeros')) > 0:
            cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetGroundPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillServerCache(skill, 'ChooseHeros')[0])))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.RandomPointSectorInMeshList(skill, cl_action.GetGroundPos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillServerCache(skill, 'ChooseHeros')[0])), (1, 0, 1), 0, 3, 1, 179, cl_action.GetSkillCustomData(skill, 'MeteorNum', defaultValue = 5)))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_POS,
                SKILLCACHE_LSTPOS])
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.RandomPointSectorInMesh(skill, 0, 20, 1, 179))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.RandomPointSectorInMeshList(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (1, 0, 1), 0, 3, 1, 179, cl_action.GetSkillCustomData(skill, 'MeteorNum', defaultValue = 5)))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_POS,
                SKILLCACHE_LSTPOS])
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1738
    m_Name = 'S5-流星法杖'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

