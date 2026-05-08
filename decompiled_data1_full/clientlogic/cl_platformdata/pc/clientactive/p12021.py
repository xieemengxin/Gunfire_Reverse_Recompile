# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12021.pyc
# Source Generated with Decompyle++
# File: p12021.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import LightningChainCartoon, RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon0(LightningChainCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 1, 20, 20, cl_action.GetCartoonHitTargetInOrder(skill, 1), 'Bip001 Prop2', 2, True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = False)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'StartX') / 100, cl_action.GetSkillCustomArg(skill, 'StartY') / 100, cl_action.GetSkillCustomArg(skill, 'StartZ') / 100)):
                return None
            cls.EnableShow(skill, 1, 300, 20, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    cl_action.WeaponDamage(skill, {
        'Att': cl_action.GetPerformArgValue(skill, 'Att', iDefault = 0) }, { }, sendPFMsg = True)
    cl_action.AddIgnoreTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    for i1 in range(0, skill.m_Cache['MaxCover'], 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


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
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 12021
    m_Name = '秘能觉醒元素之环二-雷弹'
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
        'ChargeTime': 0,
        'MaxCover': 1 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'Att': 100,
        'CrazyEff': 30000,
        'DebuffProb': 2000 }

