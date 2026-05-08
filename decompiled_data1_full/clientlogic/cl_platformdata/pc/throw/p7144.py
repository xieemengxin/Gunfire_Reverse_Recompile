# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p7144.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p7144.pyc
# Source Generated with Decompyle++
# File: p7144.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE, SKILLCACHE_SIGNSPEED

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
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 0), (0, 0.1, 0)), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DelegateThrowCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cl_action.StartBackSwing(skill, 4 if int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
        cl_action.UnlockMonsterAttackerFace(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgDestPosDir(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgSelfFace(skill), 5, 0), (60, 0, 0), baseHorizontal = False), cl_action.CalParabolaSpeed(cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgTargetPos(skill, notContainDying = False), -30, 60), 0, (0, -30, 0), (0, 0), 0, True, liveTime = 0, innerRadius = 0, pierce = 0, need3DWarning = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 6), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(RayCastCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cl_action.StartBackSwing(skill, 4 if int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
        cl_action.UnlockMonsterAttackerFace(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.25, -2)), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), skill.m_Cache['Pierce'], 90, 80, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.25, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.LockMonsterAttackerFace(skill)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 1:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetCustomPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False))
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(4000 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendOwnerUseThrowPFMsg(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.GetSkillCustomData(skill, 'BigCannon', defaultValue = 0))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_SIGNSPEED, skill.m_Cache['Radius'])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAttackerAttr(skill, 'AttSpeed'))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7144
    m_Name = '木机甲飞弹'
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
        'ColdTime': 75,
        'AttDistance': 40,
        'MaxCover': 1,
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
        'Pierce': 1,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1038
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

