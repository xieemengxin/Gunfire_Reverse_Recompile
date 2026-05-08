# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9415.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9415.pyc
# Source Generated with Decompyle++
# File: p9415.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import AnnulusTriggerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_EXTRATRAJECTORY

class CCartoon0(AnnulusTriggerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimInPointList(skill, cl_action.GetSkillServerCache(skill, 'AnnulusTriggerFisrtHitHight')):
            cl_action.PushVictim(skill, cl_action.CrtArgSelfPos(skill), 20, 0, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 1)
            for i1 in range(0, cl_action.GetTrajectory(skill), 1):
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.FloatToIntFloor(skill, (cl_action.GetAttackerStateCount(skill, 32833) * 0.01 + 1) * 150) if cl_action.CheckVictimInPointList(skill, cl_action.GetSkillServerCache(skill, 'AnnulusTriggerFisrtHitHight')) else 100 if cl_action.CheckVictimInPointList(skill, cl_action.GetSkillServerCache(skill, 'AnnulusTriggerFisrtHit')) else 10 }, { }, sendPFMsg = False)
            
        else:
            for i2 in range(0, cl_action.GetTrajectory(skill), 1):
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.FloatToIntFloor(skill, (cl_action.GetAttackerStateCount(skill, 32833) * 0.01 + 1) * 150) if cl_action.CheckVictimInPointList(skill, cl_action.GetSkillServerCache(skill, 'AnnulusTriggerFisrtHitHight')) else 100 if cl_action.CheckVictimInPointList(skill, cl_action.GetSkillServerCache(skill, 'AnnulusTriggerFisrtHit')) else 10 }, { }, sendPFMsg = False)
            

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 48)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CContinuousPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9415
    m_Name = '#NT#磁暴线圈'
    m_ExtPerform = (4348,)
    m_HaltInfo = {
        40108: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_PassRule = {
        1062: 1,
        1012: 1,
        1073: 1,
        1064: 1 }
    m_CheckForbid = 1034

