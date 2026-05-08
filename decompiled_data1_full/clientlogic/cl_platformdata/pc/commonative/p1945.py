# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1945.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1945.pyc
# Source Generated with Decompyle++
# File: p1945.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import LightningChainCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_WEAKNESS, SKILLCACHE_INT, WATER_BUBBLE_DAMAGE

class CCartoon1(LightningChainCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'EnHanceLightChain', defaultValue = '0') == 1:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, True, cl_action.GetCameraDirPos(skill, 0), 1, 40, 0, 0, 0, 0, 0, False, [
                'Bip001 L Forearm',
                'Bip001 R Forearm',
                'Bip001 HeadNub'], cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 'Bip001 Spine', 1, True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.GetSkillVID(skill) == 0:
            cl_action.SetSkillVictim(skill, cl_action.GetNearestMonsterInRange(skill, 40, 0, 0, 1, 0.7, 0.5, iUseVictim = 0, iExcludeState = 0, iExcludeStateCountMin = 0, iExcludeStateFromAttack = 0))

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
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        WATER_BUBBLE_DAMAGE][0])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'StateOwner', defaultValue = cl_action.GetSkillAID(skill)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1945
    m_Name = '雷刹闪电链'
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
        'AttDistance': 40,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 1
    m_ForbidRule = 0

