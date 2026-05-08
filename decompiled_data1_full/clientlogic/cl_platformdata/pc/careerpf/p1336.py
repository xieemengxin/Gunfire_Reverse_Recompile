# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1336.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1336.pyc
# Source Generated with Decompyle++
# File: p1336.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon, WinkPosCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, WARRIOR_NORMAL, WATER_BUBBLE_DAMAGE

class CCartoon25(TimerCartoon):
    m_SID = 25
    
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
            cls.EnableShow(skill, 4, cl_action.ToInt(skill, 13 / (skill.m_Cache['ExplodeDelay'] + 100) / 100 / 4))
        else:
            cls.EnableCtrl(skill, 4, cl_action.ToInt(skill, 13 / (skill.m_Cache['ExplodeDelay'] + 100) / 100 / 4))

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon25.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 92 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 92 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, 16, 1, cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)))
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * cl_action.GetPerformArgValue(skill, 'H2AttMultiple', iDefault = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 6, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                3,
                75], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 6, 0), [
                skill.m_Cache['Radius'],
                3,
                75], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if 0 == cl_action.GetSkillVarCache(skill, 'EnergyCostH2'):
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.ChangeAttackerEnergy(skill, cl_action.GetSkillVarCache(skill, 'EnergyCostH2'), iReason = 0)
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 64 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 64 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, cl_action.ToInt(skill, 24 / (skill.m_Cache['ExplodeDelay'] + 100) / 100 / 4))
        else:
            cls.EnableCtrl(skill, 4, cl_action.ToInt(skill, 24 / (skill.m_Cache['ExplodeDelay'] + 100) / 100 / 4))

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        pass

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 92 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 92 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, 16, 1, False)
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * cl_action.GetPerformArgValue(skill, 'H3AttMultiple', iDefault = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgSelfFace(skill), 2, 0)):
                return None
            cls.EnableShow(skill, [
                10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgSelfFace(skill), 2, 0), [
                10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon14.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if 0 == cl_action.GetSkillVarCache(skill, 'EnergyCostH3'):
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.ChangeAttackerEnergy(skill, cl_action.GetSkillVarCache(skill, 'EnergyCostH3'), iReason = 0)
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 68 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 68 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(WinkPosCartoon):
    m_SID = 15
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 64, 0, [
                1,
                1,
                45], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSceneObjPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0]), cl_math.Vec3Minus(cl_action.CrtArgSelfPos(skill), cl_action.GetSceneObjPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])), 1, 0) if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] > 0 else cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), 5, 0), 64, 0, [
                1,
                1,
                45], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0, needHitQingYanLayer = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 4, 0)
        else:
            cls.EnableCtrl(skill, 4, 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 120 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 120 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(DirectPosCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, 16, 1, cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)))
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * cl_action.GetPerformArgValue(skill, 'H4AttMultiple', iDefault = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgSelfFace(skill), 3, 0), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgSelfFace(skill), 3, 0), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if 0 == cl_action.GetSkillVarCache(skill, 'EnergyCostH4'):
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.ChangeAttackerEnergy(skill, cl_action.GetSkillVarCache(skill, 'EnergyCostH4'), iReason = 0 if cl_action.GetAttackerStateCount(skill, 33827) >= 30 else cl_action.GetSkillVarCache(skill, 'EnergyCostH4'))
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 44 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 44 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'PFSkillCount') == 0:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetSkillVarCache(skill, 'PFSkillCount') == 1:
            cartoon = { }
            CCartoon11.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetSkillVarCache(skill, 'PFSkillCount') == 2:
            cl_action.SetSkillServerCache(skill, 'Heavy4', 1)
            cartoon = { }
            CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

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
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
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
            cls.EnableShow(skill, 44, 1)
        else:
            cls.EnableCtrl(skill, 44, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'EnergyCostH2', cl_action.GetPerformArgValue(skill, 'EnergyCostH2', iDefault = -3000))
    cl_action.SetSkillVarCache(skill, 'EnergyCostH3', cl_action.GetPerformArgValue(skill, 'EnergyCostH3', iDefault = -3000))
    cl_action.SetSkillVarCache(skill, 'EnergyCostH4', cl_action.GetPerformArgValue(skill, 'EnergyCostH4', iDefault = -3000))
    cl_action.ApplyStateTransDamFactor(skill, 33604)
    cl_action.SkillForbid(skill, True, 1106)
    cl_action.SetSkillVarCache(skill, 'ChainTimes', 3 if skill.m_Cache['AttDistance'] > 0 else 2)
    if cl_action.CheckClientCtrl(skill):
        cl_action.SetSkillVarCache(skill, 'PFSkillCount', cl_action.ToInt(skill, cl_action.GetSkillRunTimes(skill) % cl_action.GetSkillVarCache(skill, 'ChainTimes')))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, 'SkillCount', iDefault = 0))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
            cl_action.GetSkillVID(skill)])
        cl_action.SetSkillVarCache(skill, 'PFSkillCount', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1106)


def End(skill):
    if not cl_action.CheckIsHalt(skill):
        cl_action.SkillForbid(skill, False, 1106)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPFEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1336
    m_Name = '#NT#进阶式'
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
        'ColdTime': 4,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 15,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 1013
    m_BaseArgData = {
        'EnergyCostH3': -3000,
        'EnergyCostH4': -3000,
        'H2AttMultiple': 9,
        'H3AttMultiple': 12,
        'H4AttMultiple': 24,
        'EnergyCostH2': -3000 }
    m_AIPerformDam = 1200

