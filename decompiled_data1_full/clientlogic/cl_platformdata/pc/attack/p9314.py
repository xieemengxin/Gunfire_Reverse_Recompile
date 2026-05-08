# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9314.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9314.pyc
# Source Generated with Decompyle++
# File: p9314.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowLogicCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, MONSTER_PART_BARRIAR, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetDictValueFromSkillCustomData(skill, '9314HitWeakness', cl_action.GetCartoonLoopID(skill, 2), iDefault = 0) == 1:
            if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
                cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 1), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ThrowLogicCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if skill.m_Cache['Radius'] >= 1:
            cl_action.UpdateDictSkillCustomData(skill, '9314HitWeakness', cl_action.GetCartoonLoopID(skill, 1), 1 if cl_action.CheckHitWeakness(skill) else 0)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if skill.m_Cache['Radius'] >= 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 300, pierce = skill.m_Cache['Pierce'], fallAccVec = 9.8, radius = skill.m_Cache['BulletSize'], rebound = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        for i2 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9314
    m_Name = '#NT#老虎机'
    m_ExtPerform = (5322, 1028)
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

