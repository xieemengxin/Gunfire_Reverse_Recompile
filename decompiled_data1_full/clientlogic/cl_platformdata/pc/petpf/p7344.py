# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7344.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7344.pyc
# Source Generated with Decompyle++
# File: p7344.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityParabolaCartoon, ExternalDriveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALLNOSELF, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_MONSTER, WARRIOR_SUMMON

class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)
        cl_action.UnlockMonsterAttackerFace(skill)

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
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ExternalDriveCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.PushVictim(skill, (0, 0, 0), 30, 12, 10000, angle = 180, iCartoonSID = 0, iIgnoreStruckCD = 1, iClient = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), True, cl_action.GetCurVID(skill), (0, 0, 0), parentName = '')
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 0, 'default', 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(EntityParabolaCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.GetSkillVarCache(skill, 'hit') == 1:
            if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALLNOSELF):
                if cl_action.CheckHookPullBack(skill):
                    cl_action.SetSkillVarCache(skill, 'hit', 1)
                    cl_action.VictimAddState(skill, 8127, 0, 1, { })
                    cl_action.PerformDamage(skill, {
                        'Att': skill.m_Cache['Att'] * 3 }, dArgs = { })
                    if cl_action.CheckHasState(skill, 8128):
                        cl_action.SkillHaltSelf(skill)
                    else:
                        cl_action.VictimAddState(skill, 8128, 0, 1, { })
                        cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), False, cl_action.GetCurVID(skill), (0, 0.5, 0), parentName = '')
                        cartoon = { }
                        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cl_action.PerformDamage(skill, {
                        'Att': skill.m_Cache['Att'] * 3 }, dArgs = { })
                    cl_action.SkillHaltSelf(skill)
            else:
                cl_action.PerformDamage(skill, {
                    'Att': skill.m_Cache['Att'] * 3 }, dArgs = { })
                cl_action.SkillHaltSelf(skill)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SkillHaltSelf(skill)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_math.Vec3Minus(cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 0.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))), 50, 0.4, (0, 18, 0), (0, 0), (0, 0), 75, False, True, 0, True if cl_action.CheckTargetSID(skill, 1169) else False, cl_action.GetSkillSummonCreate(skill)[0], 0, targetType = OBJ_ENEMY, maxDistance = 15, hitHeroOver = False, forceSpeed = True, innerRadius = 0.1, scale = 1, hitmonsterover = True)

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
        cl_action.SetSkillVarCache(skill, 'hit', 0)
        cl_action.AttackerAddState(skill, 33267, 0, 1, { })
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))], WARRIOR_SUMMON, {
            1025: 10 }, {
            'Radius': 0.4 })
        cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetSkillSummonCreate(skill)[0])
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_EXTRATRAJECTORY])
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 43, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)


def End(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, PETPF_ACTIVE_SPELL

class CPerform(CCustomPerform):
    m_SID = 7344
    m_Name = '白鲛钩子'
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
        'ColdTime': 0,
        'AttDistance': 12,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_SPELL
    m_SpellPower = 100
    m_NeedTarget = 0
    m_ForbidRule = 0

