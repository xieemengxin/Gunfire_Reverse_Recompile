# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9213.pyc
# Source Generated with Decompyle++
# File: p9213.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ConvolutionCartoon, RaycastTimerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, MONSTER_PART_BARRIAR, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon8(TimerCartoon):
    m_SID = 8
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
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
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

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
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        if cl_action.CheckIsAllBulletRecycled(skill):
            cartoon = { }
            CCartoon10.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 6, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(ConvolutionCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.GetCartoonLoopID(skill, 1) == 0:
            cl_action.SkillForbid(skill, True, 1066)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'hittime') == 1:
            if not cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
                cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.SetSkillVarCache(skill, 'HitCount', cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) + 1))
            cl_action.WeaponDamage(skill, {
                'Att': (cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) * 15 + 225 if cl_action.CheckHasInscription(skill, 4954) else 150 }, { }, sendPFMsg = False)
        else:
            cl_action.SetSkillVarCache(skill, 'hittime', 1)
            cl_action.SetSkillVarCache(skill, 'HitCount', cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) + 1))
            cl_action.WeaponDamage(skill, {
                'Att': (cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) * 15 + 225 if cl_action.CheckHasInscription(skill, 4954) else 150 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 5)):
                return None
            cls.EnableShow(skill, 0.1, [
                10,
                15,
                20,
                25], cl_action.GetSkillAID(skill), skill.m_Cache['BulletSpeed'] * (3 if cl_action.CheckIsHover(skill, 5) else cl_math.CalDistance3D(cl_action.GetEndPositionInCrt(skill, 5), cl_action.GetCameraCenterPosition(skill, cartoon)) / 12), targettype = OBJ_ENEMY, radius = 1, angle = 180, effect = 0, traileffect = 0, trailexisttime = 0.3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(RaycastTimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckIsHover(skill, 5):
            if cl_action.CheckIsHover(skill, 5):
                if cl_action.CheckHasInscription(skill, 13027):
                    pass
                
            elif cl_action.CheckHasInscription(skill, 4954):
                pass
            
            'Att'(cl_action.ToInt, {
                skill: 35((cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) * 10 + 100, 100) }, { }, sendPFMsg = False)
        elif cl_action.CheckHasSkillVarCache(skill, 'HitCount'):
            pass
        
        skill('HitCount', cl_action.ToInt, skill(cl_action.GetSkillVarCache(skill, 'HitCount'), 0 + 1))
        if cl_action.CheckIsHover(skill, 5):
            if cl_action.CheckHasInscription(skill, 13027):
                pass
            
        elif cl_action.CheckHasInscription(skill, 4954):
            pass
        
        'Att'(cl_action.ToInt, {
            skill: 35((cl_action.GetSkillVarCache(skill, 'HitCount') if cl_action.CheckHasSkillVarCache(skill, 'HitCount') else 0) * 10 + 100, 100) }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if cl_action.CheckHasInscription(skill, 4955):
            cl_action.AttackerAddState(skill, 1440, 0, 0, { })
            cl_action.SetSkillVarCache(skill, 'hittime', 0)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 5))
        else:
            cl_action.SetSkillVarCache(skill, 'hittime', 0)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetCartoonLoopID(skill, 5))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 20, 18, [
                1.5], ATT_SHAPE_SPHERE, OBJ_ENEMY, cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], 0, [
                None,
                None][cl_action.ToInt(skill, cl_action.GetNowLayer(skill) % 2)], 0, 0.2, raycastradius = 0.5, rebounddis = 0.01)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasInscription(skill, 13027):
        cl_action.AttackerAddState(skill, 1501, 0, 1, { })
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1066)


def End(skill):
    cl_action.SkillForbid(skill, False, 1066)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9213
    m_Name = '回旋镖'
    m_ExtPerform = ()
    m_HaltInfo = {
        10214: 1,
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
    m_ForbidRule = 1094
    m_CheckForbid = 1001

