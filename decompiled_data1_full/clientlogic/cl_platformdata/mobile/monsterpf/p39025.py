# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39025.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39025.pyc
# Source Generated with Decompyle++
# File: p39025.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, SectorDiffuseCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, DAM_USE_HP, OBJ_ALL, OBJ_ENEMY, WARRIOR_BUILD, WARRIOR_LUOHOU_PILLAR

class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 11, 1)

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
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 146, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 18, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(SectorDiffuseCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHasSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCurVID(skill))):
            cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCurVID(skill)), 1)
            if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL) or cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -0.5), DAM_USE_HP)
            else:
                cl_action.WeaponDamage(skill, {
                    'Att': 80 }, { }, sendPFMsg = False)
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
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetCartoonEnd(skill, 3), (0, 0.2, 0)), cl_action.GetSkillVarCache(skill, 'EndPos'), 0, 60, 1.2, 30, 0.5, 20, targettype = OBJ_ENEMY, effect = 0, isOverByFightType = True, fightType = WARRIOR_LUOHOU_PILLAR, isUseSector = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 100 if cl_action.GetMonsterPhase(skill) >= 3 else 150 if cl_action.GetMonsterPhase(skill) >= 2 else 200)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'EndPosList', cl_action.CreatePosOnCircle(skill, cl_math.Vec3Add(cl_action.GetCartoonEnd(skill, 3), (0, 0.2, 0)), 10, cl_action.ToInt(skill, 18)))
        for i1 in range(0, cl_action.ToInt(skill, 18), 1):
            cl_action.SetSkillVarCache(skill, 'EndPos', cl_action.GetSkillVarCache(skill, 'EndPosList')[i1])
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL) or cl_action.CheckVictimSID(skill, 1185):
            cl_action.ChangeVictimDefValue(skill, cl_action.ToInt(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -0.5), DAM_USE_HP)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = False)
            cl_action.PushHeroVictim(skill, (0, 0, 0), 5, 5, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 25, 0), cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 25, 0), [
                8], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.LockMonsterAttackerFace(skill)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39025
    m_Name = '罗睺快速中拳'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 600,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_BaseArgData = {
        'buildatk': 50 }
    m_CacheAttr = [
        'DebuffProb']

