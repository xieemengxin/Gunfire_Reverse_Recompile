# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9399.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9399.pyc
# Source Generated with Decompyle++
# File: p9399.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

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
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, 25, 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9399
    m_Name = 's刺猬'
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
        'ColdTime': 100,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = (1,)
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

