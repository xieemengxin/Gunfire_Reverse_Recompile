# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1638.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1638.pyc
# Source Generated with Decompyle++
# File: p1638.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import FlyLinePathCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, WARRIOR_HERO

class CCartoon1(FlyLinePathCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL):
            cl_action.PushHeroVictim(skill, cl_action.GetEndPositionInCrt(skill, 1), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_hero', 3000) * (cl_action.GetPlayRound(skill) * cl_action.GetTrapPerformCustomParam(skill, 'damage_round_percentage', 0.25) + 1) })
        else:
            cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 1), 20, 5, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetTrapPerformCustomParam(skill, 'damage_to_monster', 3000) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, skill.m_Cache['RollLineID'], 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 1638
    m_Name = '二幕滚石-短'
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
    m_Resend = 1

