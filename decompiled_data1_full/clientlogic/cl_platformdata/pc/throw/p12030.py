# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p12030.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p12030.pyc
# Source Generated with Decompyle++
# File: p12030.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, WallSummonCartoon
from cl_commondefines import CRT_CHECK_SERVER, INK_DAMAGE, OBJ_ENEMY, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_CHARGELEVEL, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE, WARRIOR_NORMAL

class CCartoon14(TimerCartoon):
    m_SID = 14
    
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
            cls.EnableShow(skill, cl_action.ToInt(skill, 1500 / (60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30) / 3), 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(TimerCartoon):
    m_SID = 15
    
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
            cls.EnableShow(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(WallSummonCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'HorizontalDir', cl_action.GetCartoonHorizontalDir(skill, 0))
        cl_action.SetSkillServerCache(skill, 'InkAreaCheckLength', cl_action.GetInkAreaCheckLength(skill, 0, 15))
        cl_action.SetSkillServerCache(skill, 'InkAreaCheckHeight', cl_action.GetInkAreaCheckHeight(skill, 0))
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        if cl_action.IsHeroCtrl(skill):
            cl_action.SetSkillServerCache(skill, 'ExShowTips', [
                INK_DAMAGE][0])
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1431, 'Att') * 1) })
            if cl_action.GetDistanceByAttackerAndTarget(skill) < 5 and cl_action.CheckVictimType(skill, WARRIOR_NORMAL, OBJ_ENEMY):
                if cl_action.CheckVictimInStruckCD(skill):
                    cl_action.PushMoveVictim(skill, (0, 0, 0), 40, 4, (0, 0, 0), iCartoonSID = -1, bKnockBack = True)
                else:
                    cl_action.PushVictim(skill, (0, 0, 0), 40, 4, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 1)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, (cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius')), 1000, 1064, 45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15, 60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30, cl_action.ToInt(skill, (45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15) * 100 / (60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30)), targettype = OBJ_ENEMY)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, cl_action.GetAttackerPerformAttr(skill, 12030, 'TriggerTimes') - 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_CHARGELEVEL)
    cl_action.SetSkillCustomDataInt(skill, 'TriggerOrigin', cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY))
    cl_action.AddSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS)
    cl_action.SetSkillServerCache(skill, 'Enhance', cl_action.GetSkillCacheData(skill, SKILLCACHE_ATTACKSTATUS))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_CHARGELEVEL) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    if 1 == cl_action.GetAttackerPerformAttr(skill, 12030, 'TriggerTimes'):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ATTACKSTATUS,
        SKILLCACHE_CHARGELEVEL,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12030
    m_Name = '被动挥墨成卷'
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
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'AddStateTime': 0,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'MoveSpeed_Buff': 3000 }
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

