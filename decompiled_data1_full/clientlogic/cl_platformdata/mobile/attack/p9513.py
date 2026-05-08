# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9513.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9513.pyc
# Source Generated with Decompyle++
# File: p9513.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.pc.attack.p9513 import IsSuperAttack
from cl_perform.cartoon.defines import CheckTeammateRaycastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, OBJ_FRIEND, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_HERO, WARRIOR_PROTEGE_NORMAL, WARRIOR_SERVANT

class CCartoon2(CheckTeammateRaycastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_FRIEND) or cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL):
            cl_action.VictimAddState(skill, 1515, 1000, 0, { })
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE) == 1:
                cl_action.AddWeaponPFBullet(skill, cl_action.GetAttackerWeaponPerformAttr(skill, 9513, 'PFBulletUse'))
            elif not cl_action.CheckVictimType(skill, WARRIOR_PROTEGE_NORMAL, OBJ_FRIEND):
                cl_action.WeaponDamage(skill, {
                    'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], liveTime = 0, radius = 0.3, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.IsOpenSnipe(skill):
            for i1 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 0, index = i1)
            
        else:
            for i2 in range(0, cl_action.GetTrajectory(skill), 1):
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 0, index = i2)
            

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_BALLISTICTYPE,
        SKILLCACHE_ATTACKSTATUS]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9513
    m_Name = '电弧狙'
    m_ExtPerform = (4293, 4296)
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
        'ChargeTime': 0,
        'MaxPFBullet': 10000,
        'PFBulletUse': 2000,
        'PFBulletRecover': 2000,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001
    
    def CanUse(self, oWarrior, dData):
        if not IsSuperAttack(dData['CtrlCache']):
            dData['NoPFBulletUse'] = 1
        return super(CPerform, self).CanUse(oWarrior, dData)

    
    def CostBullet(self, oWarrior, oSkill):
        if not IsSuperAttack(oSkill.m_CacheData):
            oSkill.m_Collect['NoPFBulletUse'] = 1
        super(CPerform, self).CostBullet(oWarrior, oSkill)


