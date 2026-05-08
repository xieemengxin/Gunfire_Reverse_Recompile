# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1734.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1734.pyc
# Source Generated with Decompyle++
# File: p1734.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALLNOSELF, SIDE_TYPE_HERO, SIDE_TYPE_MONSTER, WARRIOR_HERO, WARRIOR_MONSTER, WARRIOR_PET, WARRIOR_SERVANT, WARRIOR_SUMMON

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
                'Att': 5000 })
        elif cl_action.CheckVictimSide(skill, WARRIOR_HERO, SIDE_TYPE_HERO) or cl_action.CheckVictimSide(skill, WARRIOR_SERVANT, SIDE_TYPE_HERO) or cl_action.CheckVictimSide(skill, WARRIOR_PET, SIDE_TYPE_HERO):
            cl_action.PerformDamage(skill, {
                'Att': 5000 })
        else:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, ((cl_action.GetGamePlayerCnt(skill) + -1) * 2 * (cl_action.GetPlayCycle(skill) // 8 + 1) + 1) * (cl_action.GetPlayCycle(skill) * 1.6 + 1 + 0.7 * (cl_action.GetPlayRound(skill) + -1)) * (cl_action.GetLevelMonsterGrade(skill) * 41600 + 36400)) })

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
                6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
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
        if cl_action.CheckVictimSide(skill, WARRIOR_MONSTER, SIDE_TYPE_MONSTER):
            cl_action.TrapThumpVictim(skill, cl_action.GetCurVID(skill))
            cl_action.VictimAddState(skill, 33543, 100, 0, { })
        cl_action.PerformDamage(skill, {
            'Att': 1000 })
        cl_action.VictimAddState(skill, 20028, 500, 0, { })

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
                6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 20)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1734
    m_Name = '电击区域放电'
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
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_Resend = 1

