# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1605.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1605.pyc
# Source Generated with Decompyle++
# File: p1605.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALLNOSELF, SIDE_TYPE_HERO, WARRIOR_HERO, WARRIOR_SERVANT, WARRIOR_SUMMON

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSide(skill, WARRIOR_SUMMON, SIDE_TYPE_HERO):
            cl_action.PerformDamage(skill, {
                'Att': 5000 })
        elif cl_action.CheckVictimSide(skill, WARRIOR_HERO, SIDE_TYPE_HERO) or cl_action.CheckVictimSide(skill, WARRIOR_SERVANT, SIDE_TYPE_HERO):
            cl_action.PushHeroVictim(skill, cl_action.GetCartoonEnd(skill, 1), 10, 4, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
            cl_action.PerformDamage(skill, {
                'Att': 5000 })
        else:
            cl_action.PushVictim(skill, cl_action.GetCartoonEnd(skill, 1), 20, 8, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
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
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1605
    m_Name = '可破坏物爆炸'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

