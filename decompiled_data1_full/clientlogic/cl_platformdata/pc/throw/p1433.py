# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1433.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1433.pyc
# Source Generated with Decompyle++
# File: p1433.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_FLAW, OBJ_ALL, OBJ_ENEMY, OBJ_FRIEND, SKILLCACHE_BEACONCOUNT, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_PARENTACTNUM, SKILLCACHE_PERFORMMODE, WARRIOR_MONSTER

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY):
            if cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)):
                cl_action.VictimAddState(skill, 1860, cl_action.GetSpecificPerformArgValue(skill, 1429, 'SlowDownTime', iDefault = 200), 0, { })
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == cl_action.GetCurVID(skill):
                    cl_action.SetHitFlaw(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT), iBreakFlaw = 1)
                    cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.ToInt(skill, (cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') * 0.5 if cl_action.GetSkillCustomData(skill, '3516SureNothrow', defaultValue = False) else cl_action.GetAttackerPerformAttr(skill, 1429, 'Att')) / cl_action.Power(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) - 1)) })
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == cl_action.GetCurVID(skill):
                cl_action.SetHitFlaw(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_BEACONCOUNT), iBreakFlaw = 1)
                cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, (cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') * 0.5 if cl_action.GetSkillCustomData(skill, '3516SureNothrow', defaultValue = False) else cl_action.GetAttackerPerformAttr(skill, 1429, 'Att')) / cl_action.Power(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) - 1)) })
        elif cl_action.GetSkillCustomData(skill, 'HasP3518', defaultValue = False) and cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
            cl_action.VictimAddState(skill, 33041, 500, 0, {
                'TalentLevel': cl_action.GetSkillCustomData(skill, '3518PFLV', defaultValue = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (0, 0, 0), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetAttackerPerformAttr(skill, 1429, 'Radius') / cl_action.Power(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) - 1)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, (0, 0, 0), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1429, 'Radius') / cl_action.Power(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) - 1)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyPFTransDamFactor(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PARENTACTNUM)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BEACONCOUNT,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_PARENTACTNUM,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1433
    m_Name = '#NT#13553破绽爆炸'
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
        'ColdTime': 15,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

