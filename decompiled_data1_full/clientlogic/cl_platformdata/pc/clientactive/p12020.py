# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12020.pyc
# Source Generated with Decompyle++
# File: p12020.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ThrowByPowerCartoon
from cl_commondefines import CRT_CHECK_SERVER, HIT_OVER_NORMAL, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon3(ThrowByPowerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetCartoonLoopID(skill, 3) >= skill.m_Cache['MaxCover'] - 1:
            cl_action.AttackerRemoveState(skill, 33025, bSameItem = False)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_UNTAGGED):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'isHitStatic') and cl_math.CalDistance3D(cl_action.CrtArgHitPos(skill), cl_action.GetStartPositionInCrt(skill, 3)) <= 4.8 and cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillVarCache(skill, 'isHitStatic', True)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100)):
                return None
            cls.EnableShow(skill, skill.m_Cache['AttDistance'], (0, 0, 0), (0.5, 0.5), 110, True, False, 5, innerRadius = 0.1, pierce = 99, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AttackerAddState(skill, 33025, 0, 1, { })
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    cl_action.WeaponDamage(skill, {
        'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)
    cl_action.AddIgnoreTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    for i1 in range(0, skill.m_Cache['MaxCover'], 1):
        cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 12020
    m_Name = '秘能觉醒元素之环二-剑气'
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
        'AttDistance': 4,
        'ChargeTime': 0,
        'MaxCover': 1 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'Att': 100,
        'CrazyEff': 20000,
        'DebuffProb': 3000 }

