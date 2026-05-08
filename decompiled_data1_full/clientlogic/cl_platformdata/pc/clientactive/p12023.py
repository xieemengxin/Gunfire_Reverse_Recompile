# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12023.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12023.pyc
# Source Generated with Decompyle++
# File: p12023.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTINT

class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 50) }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100)):
                return None
            cls.EnableShow(skill, 1, 100, 50, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = cl_action.GetSkillCustomArg(skill, 'Target'), extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        if not cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1] == cl_action.GetSkillCustomArg(skill, 'Target'):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12023
    m_Name = '#NT#冰晶溅射'
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
        'ColdTime': 10,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_UseCurWeapon = 1
    m_ForbidRule = 0

