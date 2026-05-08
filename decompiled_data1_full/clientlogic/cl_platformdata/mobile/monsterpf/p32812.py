# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p32812.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p32812.pyc
# Source Generated with Decompyle++
# File: p32812.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityCurveCartoon, MonsterLiftLandCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_NORMAL, DAM_TYPE_THUNDER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON

class CCartoon6(EntityCurveCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.TargetAddState(skill, cl_action.CrtArgRandomNum(skill, 1172, 1174), 0, 0, { }, cl_action.GetCartoonEntityID(skill, 6))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetCartoonEnd(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgMissingPos(skill, 0), 0.3, 1042, 180, 14, 45, 0.3, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 4)], forceDel = True)

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
        cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 4)], True, 0, (0, 0, 0), parentName = '')
        cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = False))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, ((i1 - (1 if i1 % 2 >= 1 else 0)) / 2) * 100 + 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 0, index = i1)
            

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 300, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MonsterLiftLandCartoon):
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, False, 5, True)

    InitSuccess = classmethod(InitSuccess)


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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 1, 7969)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 50, 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CrtArgDestPosDirPoint(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1, 0)), cl_action.CrtArgGetCustomDir(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1, 10)), (0, 0, 0)), 10, cl_action.GetAllHeroCnt(skill, False) * 4 + 2, 360 / (cl_action.GetAllHeroCnt(skill, False) * 4 + 2), False), WARRIOR_SUMMON, {
            1042: 10 }, {
            'Radius': 0.3 })
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT,
            SKILLCACHE_LSTINT])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

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
        cl_action.AttackerAddState(skill, 7964, 3000, 0, { })
        cl_action.AttackerAddState(skill, 7969, 510, 1, { })
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(MonsterLiftLandCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'ifHasState', cl_action.CheckHasState(skill, 7964))
        if cl_action.CheckHasState(skill, 7962):
            if cl_action.CheckHasState(skill, 7964):
                cl_action.AttackerAddState(skill, 7969, 510, 1, { })
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon9.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.AttackerAddState(skill, 7962, 0, 0, { })
            if cl_action.CheckHasState(skill, 7964):
                cl_action.AttackerAddState(skill, 7969, 510, 1, { })
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 15, True, 5, True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 33, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ResetMonsterPerformRecord(skill)
    cl_action.SetSkillVarCache(skill, 'jump', cl_action.CrtArgSelfPos(skill))
    cartoon = { }
    CCartoon7.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 32812
    m_Name = '【第三幕】精英定点法师怪-炮台形态'
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
        'ColdTime': 200,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

