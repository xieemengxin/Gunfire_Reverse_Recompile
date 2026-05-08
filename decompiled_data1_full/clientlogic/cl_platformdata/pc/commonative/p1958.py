# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1958.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1958.pyc
# Source Generated with Decompyle++
# File: p1958.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import SectorDiffuseCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, WARRIOR_BUILD

class CCartoon3(SectorDiffuseCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 20 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 5, 2, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetGroundPos(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (cl_action.GetPerformArgValue(skill, 'OffsetX', iDefault = 0), cl_action.GetPerformArgValue(skill, 'OffsetY', iDefault = 0), cl_action.GetPerformArgValue(skill, 'OffsetZ', iDefault = 0)))), cl_action.CrtArgSkillEndPos(skill), 0, 60, 1, 20, 0.5, 360, targettype = OBJ_ENEMY, isOverByFightType = False, fightType = WARRIOR_BUILD, isUseSector = False)

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
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1958
    m_Name = '首领秘卷鱼龙冲击波-原地'
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
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

