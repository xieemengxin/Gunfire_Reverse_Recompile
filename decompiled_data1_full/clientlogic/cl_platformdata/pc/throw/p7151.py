# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p7151.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p7151.pyc
# Source Generated with Decompyle++
# File: p7151.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, DelegateThrowCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE, SKILLCACHE_POS, SKILLCACHE_SIGNSPEED

class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 4(int / (5000 if int(5000 / (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 5000)) < 4 else cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 5000)))

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
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 7), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DelegateThrowCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.CrtArgSelfFace(skill), 5, 0), (60, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), -30, 60), 0, (0, -30, 0), (0, 0), 0, True, liveTime = 0, innerRadius = 0, pierce = 0, need3DWarning = False, end = (0, 0, 0), initDir = (0, 0, 0))

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCartoonCurPos(skill, 4), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(CurveCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-1.53022, 2.82024, 0.381198)) if cl_action.GetTimerCartoonCurTimes(skill, 3) % 2 == 0 else cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (1.53452, 2.76842, 0.386077)), cl_action.CrtArgSelfFace(skill), 5, 0), 1, 90, 60, 2000, 0.7, targettype = OBJ_ENEMY, pierceblock = True, liveTime = 0, hittarger = False, iVictim = 0, lockPos = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), bLockDeadPos = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSkillVarCache(skill, 'monster', cl_action.GetNearestMonsterInRange(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0], 0 if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else 1, 1, 0 if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else 1, 0.9, 0.85, iUseVictim = 0, iExcludeState = 0, iExcludeStateCountMin = 0, iExcludeStateFromAttack = 0))
        if cl_action.GetSkillVarCache(skill, 'monster') == 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1:
                cartoon = { }
                CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SetSkillVictim(skill, cl_action.GetSkillVarCache(skill, 'monster'))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgWarriorPos(skill, cl_action.GetNearestMonsterInRange(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0], 0 if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else 1, 1, 0 if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else 1, 0.9, 0.85, iUseVictim = 0, iExcludeState = 0, iExcludeStateCountMin = 0, iExcludeStateFromAttack = 0)))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_POS])
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1:
                cartoon = { }
                CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4(int / (int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if 125 + cl_action.GetSummonOwnerTalentLevel(skill, 3310) * 25(((int((int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1) / 2) if int((125 + cl_action.GetSummonOwnerTalentLevel(skill, 3310) * 25) / (int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if int((int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1) / 2)(((int if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1)) < 4 else int if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1)), int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if int((int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) if int(((cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1) / 2)(((int if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1 else cl_action.GetSummonOwnerTalentLevel(skill, 3310) if cl_action.GetSummonOwnerTalentLevel(skill, 3310) > 0 else 1) * 4 + 4) * (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100)) > 0 else 1)

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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4(int / (5000 if int(5000 / (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 5000)) < 4 else cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 5000)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendOwnerUseThrowPFMsg(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.GetSkillCustomData(skill, 'BigCannon', defaultValue = 0))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_SIGNSPEED, skill.m_Cache['Radius'])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetAttackerPerformAttr(skill, 7151, 'AttDistance')])
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAttackerAttr(skill, 'AttSpeed'))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_POS,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7151
    m_Name = '木机甲副炮飞弹'
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
        'ColdTime': 2000,
        'AttDistance': 40,
        'MaxCover': 0,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 0,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1038
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

