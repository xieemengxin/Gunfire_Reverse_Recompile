# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1929.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1929.pyc
# Source Generated with Decompyle++
# File: p1929.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityCurveCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_SUMMON

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * 3 }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 6), (0, 0, 0), [
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(EntityCurveCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetCurCartoonEntitySID(skill) == 1039:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 1024)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetCurCartoonEntitySID(skill) == 1040:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 512)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 256)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.GetCurCartoonEntitySID(skill) == 1039:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 1024)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetCurCartoonEntitySID(skill) == 1040:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 512)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillCustomDataInt(skill, 'NowElementType', 256)
            cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'NowElementType', defaultValue = 0))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_INT])
            cl_action.SetSkillVarCache(skill, 'NowElementType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgTargetPos(skill, notContainDying = True), 0.3, 0, 180, 18, 25, 0.6, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetSkillVarCache(skill, 'Index')], forceDel = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 33311, 0, 1, { })

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
        if not cl_action.GetSkillVarCache(skill, 'NoKeepOn') == 1:
            if cl_action.CheckHasState(skill, 8123) or not cl_action.CheckTargetAlive(skill, cl_action.GetSkillAID(skill)):
                cl_action.SetSkillVarCache(skill, 'NoKeepOn', 1)
                cl_action.AttackerRemoveState(skill, 33311, bSameItem = False)
            else:
                cl_action.SetSkillVarCache(skill, 'lstHero', cl_action.GetLiveHeroID(skill, True, fMaxDis = 0))
                cl_action.ClearSkillSummonCreateCollect(skill)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CreateBoxPosList(skill, cl_math.Vec3Add(cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, cl_action.GetPointTargetModelHeight(skill, cl_action.GetSkillAID(skill)), 0)), (0, 2.3, 0)), (len(cl_action.GetSkillVarCache(skill, 'lstHero')) * 0.8, 1, 1), len(cl_action.GetSkillVarCache(skill, 'lstHero')), 0.3, 0), WARRIOR_SUMMON, {
                    1039: 10,
                    1041: 10,
                    1040: 10 }, {
                    'Radius': 0.3 })
                cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
                for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'lstHero')), 1):
                    cl_action.SetSkillVarCache(skill, 'Index', i1)
                    cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'lstHero')[i1])
                    cartoon = { }
                    CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
                

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 4)

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
        cl_action.SetSkillVarCache(skill, 'NoKeepOn', 0)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

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
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1929
    m_Name = '#NT#妖化怪随机元素球*1'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'Radius': 12 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

