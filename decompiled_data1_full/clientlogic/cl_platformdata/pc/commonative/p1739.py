# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1739.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1739.pyc
# Source Generated with Decompyle++
# File: p1739.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, SKILLCACHE_INT, SKILLCACHE_LSTPOS, WARRIOR_HERO

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i2], (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        for i2 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = i2)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'ThunderNum', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetThunderWandThunderPos(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), cl_action.GetSkillCustomData(skill, 'ThunderNum', defaultValue = 0), cl_action.GetSkillCustomData(skill, 'StartAngle', defaultValue = 0), cl_action.GetSkillCustomData(skill, 'StartDis', defaultValue = 0) / 100, cl_action.GetSkillCustomData(skill, 'ChangeAngle', defaultValue = 40), cl_action.GetSkillCustomData(skill, 'ChangeDis', defaultValue = 2) / 100))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS])
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
        cl_action.AddClientEffect(skill, 1037, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 150, (0, 0, 0))
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 200, 1, {
            'Radius': 2 }, 32248, 150, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)
    
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1739
    m_Name = 'S5-落雷法杖'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

