# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1304.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1304.pyc
# Source Generated with Decompyle++
# File: p1304.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, JumpAttackCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ALL, OBJ_ENEMY, WARRIOR_BUILD, WARRIOR_MONSTER, WARRIOR_SUMMON

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
        cl_action.AttackerRemoveState(skill, 32215, bSameItem = False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 3)

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
            cls.EnableShow(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetCartoonHitTargetCount(skill, 1) == 0:
            if cl_action.GetTalentLevel(skill, 2205) == 1:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 20 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 2:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 25 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 3:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALL):
            if cl_action.GetTalentLevel(skill, 2205) == 0:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 20 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 1:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 40 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 2:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 3:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)
        if cl_action.CheckVictimType(skill, WARRIOR_SUMMON, OBJ_ALL):
            if cl_action.GetTalentLevel(skill, 2205) == 0:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 20 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 1:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 40 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 2:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 3:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.GetTalentLevel(skill, 2205) == 0:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 20 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 1:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 40 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 2:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)
            elif cl_action.GetTalentLevel(skill, 2205) == 3:
                cl_action.ChangeAttackerArmor(skill, skill.m_Cache['ArmorMax'] * 100 // 100)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon), end = cl_action.CrtArgSightCentrePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                14,
                360], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(JumpAttackCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.CheckHasTalent(skill, 2220):
                if cl_action.GetTalentLevel(skill, 2220) == 1:
                    pass
                elif cl_action.GetTalentLevel(skill, 2220) == 2:
                    pass
                
            
            skill(5, 20, 60, 20, 33.1, 16, 12)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 32215, 0, 0, { })
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerRemoveState(skill, 32215, bSameItem = False)


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1304
    m_Name = '跃击'
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
        'ColdTime': 1500,
        'AttDistance': 7,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 7,
        'BulletVerticalAcc': 0,
        'ThumpProb': 10000,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1051
    m_PassRule = {
        1044: 1 }
    m_CheckForbid = 1013
    m_AIPerformDam = 3000

