# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p7170.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p7170.pyc
# Source Generated with Decompyle++
# File: p7170.pyc (Python 3.6)

from cl_only import GAME_FRAME_TIME
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_SIGNSPEED

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        for i1 in range(0, cl_action.GetSkillCustomData(skill, 'ExtraTrajectory', defaultValue = 0) + 1, 1):
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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(CurveCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cl_action.StartBackSwing(skill, 4 if int(6700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(6700 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))
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
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0.9, -0.5)), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 1, cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED), 25, 330, 0.7, targettype = OBJ_ENEMY, pierceblock = True, liveTime = 0, hittarger = False, iVictim = 0, lockPos = (0, 0, 0), bLockDeadPos = False)

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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4 if int(3300 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 4 else int(3300 / cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33733)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetSkillCustomData(skill, 'ExtraTrajectory', defaultValue = 0),
        cl_action.GetAttackerBaseAttr(skill, 'AttSpeed')])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, skill.m_Cache['AttSpeed'])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_SIGNSPEED, cl_action.GetAttackerAttr(skill, 'HitRange'))
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 7170
    m_Name = '#NT#园丁巨树普攻'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 80,
        'AttDistance': 99,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1038
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0
    
    def GetCDTime(self, oWarrior):
        return 10000 // oWarrior.QueryAttr('AttSpeed') * GAME_FRAME_TIME


