# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9217.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9217.pyc
# Source Generated with Decompyle++
# File: p9217.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, SendDataCartoon, WaitDataCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, CRT_EXTCHECK_PENETRATION, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_CHARGELEVEL, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_LSTINTSPECIAL

class CCartoon3(SendDataCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)) > 0:
            cl_action.UpdateSkillWeaponSpecialAttr(skill, 'Enable', -1)
            for i3 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)) if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)) <= (6 if cl_action.CheckHasInscription(skill, 13114) else 3) else 6 if cl_action.CheckHasInscription(skill, 13114) else 3, 1):
                cl_action.SetCurVictim(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[i3])
                cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
                cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[i3]))
                cl_action.WeaponDamage(skill, {
                    'Att': 70 }, { }, sendPFMsg = False)
            

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(WaitDataCartoon):
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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetSkillServerCache(skill, 'HitCrazy') == 1:
                pass
            cls.EnableShow(skill, 2, cl_action.GetCurWeaponAttr(skill, 'Enable') == 1, {
                'hitvictim': cl_action.IntToString(skill, cl_action.GetCurVID(skill)) })

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0.4, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_PENETRATION if cl_action.IsOpenSnipe(skill) or cl_action.CheckHasInscription(skill, 13115) else CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, cl_action.GetTrajectory(skill), 1):
        cl_action.SetSkillServerCache(skill, 'HitCrazy', 0)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_LSTINTSPECIAL]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9217
    m_Name = '#NT#机瞄手枪'
    m_ExtPerform = (5320,)
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
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

