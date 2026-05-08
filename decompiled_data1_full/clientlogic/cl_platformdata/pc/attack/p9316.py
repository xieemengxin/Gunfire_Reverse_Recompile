# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9316.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9316.pyc
# Source Generated with Decompyle++
# File: p9316.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillServerCache(skill, 'HitTimes') >= 1:
            if not cl_action.CheckHasState(skill, 1908) or cl_action.CheckHasSkillCollect(skill, 'AddStateCount'):
                cl_action.SetSkillServerCache(skill, 'AddStateCount', 1)
                cl_action.AddAttackerStateCount(skill, 1908, 1, iTime = 0)
            else:
                cl_action.AttackerAddState(skill, 1908, 0, 0, { })
                if not cl_action.CheckHasSkillCollect(skill, 'AddStateCount'):
                    cl_action.SetSkillServerCache(skill, 'AddStateCount', 1)
                    cl_action.AddAttackerStateCount(skill, 1908, 1, iTime = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.SetSkillServerCache(skill, 'HitTimes', int(cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))

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
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0.15, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'HitTimes', 0)
    for i1 in range(0, cl_action.GetTrajectory(skill), 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


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
    m_SID = 9316
    m_Name = '#NT#锯轮'
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
        'AttDistance': 0,
        'ChargeTime': 0,
        'MaxPFBullet': 1,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

