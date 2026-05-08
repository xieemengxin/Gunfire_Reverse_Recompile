# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1609.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1609.pyc
# Source Generated with Decompyle++
# File: p1609.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, OBJ_ALLNOSELF, SIDE_TYPE_HERO, WARRIOR_HERO, WARRIOR_SERVANT, WARRIOR_SUMMON

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendInteraceHitTargetMsg(skill, cl_action.GetSkillCustomData(skill, 'TriggerID', defaultValue = 0), dInfo = {
            'OriginID': cl_action.GetSkillCustomData(skill, 'OriginID', defaultValue = 0),
            'TriggerFrame': cl_action.GetSkillCustomData(skill, 'TriggerFrame', defaultValue = 0) })
        if cl_action.CheckVictimSide(skill, WARRIOR_SUMMON, SIDE_TYPE_HERO):
            cl_action.PerformDamage(skill, {
                'Att': 2000 })
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL):
            cl_action.PerformDamage(skill, {
                'Att': 2000 })
        else:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetLevelMonsterGrade(skill) * 2133 + 4000 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendInteraceHitTargetMsg(skill, cl_action.GetSkillCustomData(skill, 'TriggerID', defaultValue = 0), dInfo = {
            'OriginID': cl_action.GetSkillCustomData(skill, 'OriginID', defaultValue = 0),
            'TriggerFrame': cl_action.GetSkillCustomData(skill, 'TriggerFrame', defaultValue = 0) })
        if cl_action.CheckVictimSide(skill, WARRIOR_SUMMON, SIDE_TYPE_HERO):
            cl_action.PerformDamage(skill, {
                'Att': 2000 })
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL) or cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL):
            cl_action.PerformDamage(skill, {
                'Att': 2000 })
        else:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetLevelMonsterGrade(skill) * 2133 + 4000 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 12)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1609
    m_Name = '毒雾区域'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 10000 }
    m_Resend = 1

