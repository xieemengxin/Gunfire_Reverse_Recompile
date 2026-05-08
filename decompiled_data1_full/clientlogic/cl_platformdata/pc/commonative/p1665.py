# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1665.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1665.pyc
# Source Generated with Decompyle++
# File: p1665.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CastingPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_CYLINDER, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON

class CCartoon2(CastingPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'ComAtt': 25 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), (0, 0, 0), 50, 500, [
                10,
                5], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, bindbone = '', PauseForSkill = True, AttackDieBreak = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), True)

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
        cl_action.BindSummonFollowTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), False)
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, 1 if cl_action.CheckSummonIsDestroy(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else 0)
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        if not cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cl_action.DestroyAssignSummon(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT), 0)
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            if cl_action.GetPlayCycle(skill) >= 9:
                if cl_action.GetNowLayer(skill) == 1:
                    pass
                elif cl_action.GetNowLayer(skill) == 2:
                    pass
                
            
            skill(100, 300, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, 4.2, 0)), (1.1, 1.1, 1.1), 1, 0.5, 0), WARRIOR_SUMMON, {
        1038: 10 }, {
        'Radius': 0.5 })
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1665
    m_Name = '怪物强化词条-腐蚀'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 5000 }

