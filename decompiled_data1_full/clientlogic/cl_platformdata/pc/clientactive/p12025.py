# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12025.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12025.pyc
# Source Generated with Decompyle++
# File: p12025.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ThrowByPowerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, MONSTER_PART_BARRIAR, MONSTER_PART_UNTAGGED, OBJ_ENEMY

class CCartoon3(ThrowByPowerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.AttackerUsePerform(skill, 8012, {
            'vEnd': cl_action.CrtArgHitPos(skill),
            'PassCrtBuff': cl_action.GetSkillCrtBuff(skill) }, 0, 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'isHitStatic') and cl_math.CalDistance3D(cl_action.CrtArgHitPos(skill), cl_action.GetStartPositionInCrt(skill, 3)) <= 4.8 and cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.5, (0, 0, 0), (0.5, 0.5), 167, True, True, 0, innerRadius = 0.1, pierce = 3, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
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

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12025
    m_Name = '#NT#屏障英雄专属9-冲击波'
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
    m_UseCurWeapon = 0
    m_ForbidRule = 0

