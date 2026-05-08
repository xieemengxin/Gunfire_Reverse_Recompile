# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p22813.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p22813.pyc
# Source Generated with Decompyle++
# File: p22813.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityCurveCartoon, MonsterLiftLandCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_NORMAL, DAM_TYPE_THUNDER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, OBJ_ENEMY, PLAYMODE_DAYLY_TRIAL, SKILLCACHE_INT, SKILLCACHE_LSTINT, STATE_EFF_DEBAR, WARRIOR_SUMMON

class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 200)

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
            cls.EnableCtrl(skill, 90, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MonsterLiftLandCartoon):
    m_SID = 3
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 9, False, 3, False)

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
        cl_action.SendCurCartoonTriggerMsg(skill)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


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
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgTargetBodyShiftPos(skill, 1, 0, 0, 0, 0, 0, 1.5, 1.5), 0, 0, 150, 18, 25, 0.6, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetTimerCartoonCurTimes(skill, 5) - 1], forceDel = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 5, 7078)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetTimerCartoonCurTimes(skill, 5) - 1], True, 0, (0, 0, 0), parentName = '')
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetAttackerAttr(skill, 'AttSpeed'), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

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
        for i1 in range(0, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 1):
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1], False, cl_action.GetSkillAID(skill), (0, 0, 0), parentName = 'Bip001 Spine')
        
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.SendCurCartoonTriggerMsg(skill)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.AttackerAddState(skill, 7078, 0, 1, { })
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSummonPosByBoxSplit(skill, 6, 3, 0.5, False, {
            6 if cl_action.CheckGamePlayMode(skill, PLAYMODE_DAYLY_TRIAL) else 8: 10,
            5 if cl_action.CheckGamePlayMode(skill, PLAYMODE_DAYLY_TRIAL) else 7: 10,
            4 if cl_action.CheckGamePlayMode(skill, PLAYMODE_DAYLY_TRIAL) else 6: 10 }, {
            'CenterY': 1.01,
            'FloatY': 1.5 }, False, iAngle = 0), WARRIOR_SUMMON, {
            1023: 10 }, {
            'Radius': 0.5 })
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, len(cl_action.GetSkillSummonCreate(skill)))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT,
            SKILLCACHE_LSTINT])
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 9, True, 3, False)

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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 33, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cartoon = { }
    CCartoon8.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 22813
    m_Name = '定点法师怪升空召唤-上升召唤法球'
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
        'ColdTime': 400,
        'AttDistance': 40,
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

