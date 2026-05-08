# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1431.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1431.pyc
# Source Generated with Decompyle++
# File: p1431.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, WallSummonCartoon
from cl_commondefines import CRT_CHECK_SERVER, INK_DAMAGE, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_NORMAL

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
        if cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.StartAndEndAtSameHeight(skill, cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.GetEndPositionInCrt(skill, 0))) > 0.1:
            cl_action.SetSkillVarCache(skill, 'bulletdis', cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.GetEndPositionInCrt(skill, 0)))
            cl_action.SetSkillVarCache(skill, 'bulletcenterpos', cl_math.Vec3MulV(cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.GetEndPositionInCrt(skill, 0)), (0.5, 0.5, 0.5)))
            cl_action.SetSkillVarCache(skill, 'bulletpos', cl_action.GetEndPositionInCrt(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 1500 / (60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30) / 3), 3)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            pass
        
        skill(cl_action.ToInt, skill(1500, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / (60 if 0 >= 80 else 30) / 3), 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'forward', cl_action.CrtArgSelfFace(skill))
        cl_action.SetSkillVarCache(skill, 'bulletpos', cl_action.GetEndPositionInCrt(skill, 0))
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 35, 1)
        else:
            cls.EnableCtrl(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(WallSummonCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'HorizontalDir', cl_action.GetCartoonHorizontalDir(skill, 0))
        cl_action.SetSkillServerCache(skill, 'InkAreaCheckLength', cl_action.GetInkAreaCheckLength(skill, 0, 15))
        cl_action.SetSkillServerCache(skill, 'InkAreaCheckHeight', cl_action.GetInkAreaCheckHeight(skill, 0))
        cl_action.SetSkillServerCache(skill, 'CartoonFlag', 0)
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { }, sSubMsgKey = '')
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
                'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 1) })
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
        cl_action.SetSkillServerCache(skill, 'CartoonFlag', 1)
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { }, sSubMsgKey = '')

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, (cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius')), 1000, 1064, 45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15, 60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30, cl_action.ToInt(skill, (45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15) * 100 / (60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30)), targettype = OBJ_ENEMY)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_math.Vec3Minus(cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 0)), cl_action.CrtArgToCameraRotation(skill, (0, cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius') * 0.5, 0))), cl_action.CrtArgSelfCenterPos(skill), cl_math.Vec3Minus(cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 0)), cl_action.CrtArgToCameraRotation(skill, (0, cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius') * 0.5, 0))) if cl_action.CheckClientCtrl(skill) else cl_action.CrtArgSelfCenterPos(skill), cl_math.Vec3Minus(cl_action.GetSceneCenterPosition(skill, cartoon), cl_action.CrtArgToCameraRotation(skill, (0, cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius') * 0.5, 0))), (cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius'), cl_action.GetAttackerPerformAttr(skill, 1431, 'Radius')), 1000, 1064, 45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15, 60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30, cl_action.ToInt(skill, (45 if cl_action.GetAttackerPerformAttr(skill, 1431, 'ExplodeDelay') >= 1 else 15) * 100 / (60 if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0 else 0) >= 80 else 30)), targettype = OBJ_ENEMY, ignoreStatic = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
            cls.EnableShow(skill, 20, skill.m_Cache['TriggerTimes'] - 1)
        else:
            cls.EnableCtrl(skill, 20, skill.m_Cache['TriggerTimes'] - 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            if 1 == skill.m_Cache['TriggerTimes']:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 5, 1)
        else:
            cls.EnableCtrl(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 5, 1)
        else:
            cls.EnableCtrl(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1431
    m_Name = '挥墨成卷'
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
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 60,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 1000,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1062
    m_CheckForbid = 1010
    m_BaseArgData = {
        'MoveSpeed_Buff': 3000 }
    m_AIPerformDam = 2000

