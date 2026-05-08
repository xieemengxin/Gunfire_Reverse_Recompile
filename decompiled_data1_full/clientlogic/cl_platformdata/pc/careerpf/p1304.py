# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1304.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1304.pyc
# Source Generated with Decompyle++
# File: p1304.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, JumpAttackCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_BUILD, WARRIOR_MONSTER, WARRIOR_SUMMON

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
        else:
            cls.EnableCtrl(skill, 30, 1)

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
        else:
            cls.EnableCtrl(skill, 40, 1)

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
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon), end = cl_action.GetEndPositionInCrt(skill, 3)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                14,
                360], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetEndPositionInCrt(skill, 3), [
                skill.m_Cache['Radius'],
                14,
                360], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        else:
            cls.EnableCtrl(skill, 10, 1)

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
        else:
            cls.EnableCtrl(skill, 30, 1)

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
        if not (skill.m_CheckType == CRT_CHECK_SERVER):
            cls.EnableShow(skill, 5, 20, 60, 20, (20 if cl_action.GetTalentLevel(skill, 2220) == 1 else 24 if cl_action.GetTalentLevel(skill, 2220) == 2 else 28 if cl_action.CheckHasTalent(skill, 2220) else 16) * ((1 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100 > 1 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100) + 1), (0.7 if cl_action.GetTalentLevel(skill, 2220) == 1 else 0.65 if cl_action.GetTalentLevel(skill, 2220) == 2 else 0.6 if cl_action.CheckHasTalent(skill, 2220) else 0.75) * (20 if cl_action.GetTalentLevel(skill, 2220) == 1 else 24 if cl_action.GetTalentLevel(skill, 2220) == 2 else 28 if cl_action.CheckHasTalent(skill, 2220) else 16) * ((1 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100 > 1 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100) + 1))
        elif cl_action.CheckHasTalent(skill, 2220):
            pass
        
        skill(cl_action.CalCameraDir(skill), 5, 20, 60, 20, 20 if cl_action.GetTalentLevel(skill, 2220) == 1 else 24 if cl_action.GetTalentLevel(skill, 2220) == 2 else 28, 16 * ((1 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100 > 1 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100) + 1), (0.7 if cl_action.GetTalentLevel(skill, 2220) == 1 else 0.65 if cl_action.GetTalentLevel(skill, 2220) == 2 else 0.6 if cl_action.CheckHasTalent(skill, 2220) else 0.75) * (20 if cl_action.GetTalentLevel(skill, 2220) == 1 else 24 if cl_action.GetTalentLevel(skill, 2220) == 2 else 28 if cl_action.CheckHasTalent(skill, 2220) else 16) * ((1 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100 > 1 else (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) - 550) / 1100) + 1), 1.5)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.AttackerAddState(skill, 32215, 0, 0, { })
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerRemoveState(skill, 32215, bSameItem = False)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


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
        'DebuffProb': 7000,
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

