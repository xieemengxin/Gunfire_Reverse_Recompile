# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1426.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1426.pyc
# Source Generated with Decompyle++
# File: p1426.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_SERVANT, OBJ_ALL, OBJ_ALLNOSELF, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_OBSTACLE_NORMAL, WARRIOR_SERVANT

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { }, sSubMsgKey = '')
        cl_action.UseExtraThrowPerform(skill, {
            'vEnd': cl_action.GetStartPositionInCrt(skill, 3),
            'DirectPos': 1 }, 30, 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 33944):
            if cl_action.GetTalentLevel(skill, 3318) == 0:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.25), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 1:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.4), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 2:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.45), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 3:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.5), iPointTarget = 0)
            else:
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 2), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF if cl_action.CheckClientCtrl(skill) else OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_action.GetEndPositionInCrt(skill, 2), (0, 0, 0), [
            skill.m_Cache['Radius']], ATT_SHAPE_SPHERE, attshape = OBJ_ALLNOSELF, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_SERVANT, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { }, sSubMsgKey = '')
        cl_action.UseExtraThrowPerform(skill, {
            'vEnd': cl_action.GetStartPositionInCrt(skill, 6),
            'DirectPos': 1 }, 30, 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL) or cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 33944):
            if cl_action.GetTalentLevel(skill, 3318) == 0:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.25), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 1:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.4), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 2:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.45), iPointTarget = 0)
            elif cl_action.GetTalentLevel(skill, 3318) == 3:
                cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.5), iPointTarget = 0)
            else:
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 2), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALLNOSELF if cl_action.CheckClientCtrl(skill) else OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_action.GetEndPositionInCrt(skill, 2), (0, 0, 0), [
            skill.m_Cache['Radius']], ATT_SHAPE_SPHERE, attshape = OBJ_ALLNOSELF, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_SERVANT, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(RayCastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'RayActive': 1 }, sSubMsgKey = '')

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_OBSTACLE_NORMAL, OBJ_ENEMY):
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        elif cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ALL):
            cl_action.IgnoreCurVictimOnceAfterHit(skill)
            if not cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 33944):
                if cl_action.GetTalentLevel(skill, 3318) == 0:
                    cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.25), iPointTarget = 0)
                elif cl_action.GetTalentLevel(skill, 3318) == 1:
                    cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.4), iPointTarget = 0)
                elif cl_action.GetTalentLevel(skill, 3318) == 2:
                    cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.45), iPointTarget = 0)
                elif cl_action.GetTalentLevel(skill, 3318) == 3:
                    cl_action.PerformCure(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * 0.5), iPointTarget = 0)
                else:
                    cartoon = { }
                    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePos(skill)):
                return None
            cls.EnableShow(skill, 1, 90, skill.m_Cache['BulletSpeed'], targettype = OBJ_ALLNOSELF if cl_action.CheckClientCtrl(skill) else OBJ_ENEMY, liveTime = 0, radius = 0.11, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_SERVANT)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_action.GetMuzzlePos(skill), cl_action.GetMuzzlePos(skill), cl_action.GetSceneCenterPosition(skill, cartoon), 1, 90, skill.m_Cache['BulletSpeed'], OBJ_ALLNOSELF, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.11, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_SERVANT)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 29, 1)
        else:
            cls.EnableCtrl(skill, 29, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10 if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1 else 50, 1)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            pass
        
        skill(10, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1426
    m_Name = '硬木飞弹'
    m_ExtPerform = (8009,)
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
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 50000,
        'CrazyEff': 10000,
        'BulletSpeed': 80,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 4,
        'Pierce': 1,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1112
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

