# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9491.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9491.pyc
# Source Generated with Decompyle++
# File: p9491.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import AnnulusChangeCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(AnnulusChangeCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 2, (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 16) * -40, (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 16) * -40, 0, False, 30)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9491
    m_Name = 's磁暴线圈'
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
        'ColdTime': 70,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClassifyTag = (1,)
    m_BulletUse = 10
    m_IsMinor = 1
    m_ForbidRule = 1082
    m_CheckForbid = 1019
    
    def WeaponFire(self, oWarrior, oSkill):
        pass

    
    def UsePerform(self, oWarrior, oSkill):
        iWeapon = oSkill.m_Base['Weapon']
        oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
        if oWeapon:
            oSkill.m_Collect['ChargeLevel'] = oWeapon.Query('CurAnnulusRadius', 0)
        super().UsePerform(oWarrior, oSkill)


