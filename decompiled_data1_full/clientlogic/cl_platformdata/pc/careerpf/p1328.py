# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1328.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1328.pyc
# Source Generated with Decompyle++
# File: p1328.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import AnnulusDiffuseCartoon, DirectPosCartoon, SendDataCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_FLAW, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE, SKILLCACHE_POS, WARRIOR_BOSS, WARRIOR_ELITE

class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetCurVictim(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            '1324Start': 1 })

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
        cl_action.SetCurVictim(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            '1324ExtTarget': 1 })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(SendDataCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) > 0:
            cl_action.SetSkillVarCache(skill, 'Diffuse', 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0]):
            cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0]))
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2:
                cl_action.KillCurVictim(skill, True)
            else:
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') }, dArgs = {
                    'Single': 1 })

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
            cls.EnableShow(skill)
        else:
            cls.EnableCtrl(skill)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(AnnulusDiffuseCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasTalent(skill, 3502) and cl_action.GetTargetFlawCount(skill, cl_action.GetCurVID(skill)) > 0:
            cl_action.SetHitVictimAllFlaw(skill, 1)
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) * 1 / cl_action.CalAttenuationByDis(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) + 100) / 100, cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) + 100) / 100 / 20, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4 + 12, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4)) }, dArgs = {
                'FlawDam': 1 })
        cl_action.PerformDamage(skill, {
            'Att': cl_action.CalAttenuationByDis(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) + 100) / 100, cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) + 100) / 100 / 20, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4 + 12, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4 + 12, 5, 1.5, targettype = OBJ_ENEMY, liveTime = 0, pierceStatic = True)
        else:
            cls.EnableCtrl(skill, cl_action.GetStartPositionInCrt(skill, 1), cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4, cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4 + 12, 5, 1.5, targettype = OBJ_ENEMY, liveTime = 0, pierceStatic = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckHasSkillVarCache(skill, 'Diffuse'):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasTalent(skill, 3502) and cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) > 0 and cl_action.GetTargetFlawCount(skill, cl_action.GetCurVID(skill)) > 0:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
            cl_action.SetHitVictimAllFlaw(skill, 1)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetPerformArgValue(skill, 'ExtFlawDam', iDefault = 0) * (cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtExplodeDam', iDefault = 0) + 100) / 100) / 100) }, dArgs = {
                'FlawDam': 1 })
        cl_action.IgnoreCurVictimOnceAfterHit(skill)
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1324, 'Att') * (cl_action.GetPerformArgValue(skill, 'ExtExplodeDam', iDefault = 0) + 100) / 100) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4 if cl_action.GetSkillCustomArg(skill, 'Slay') == 1 else cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 0)
        elif cl_action.GetSkillCustomArg(skill, 'Slay') == 1:
            pass
        
        skill(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 0, 0), cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius') + 4, [
            cl_action.GetAttackerPerformAttr(skill, 1324, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 0)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 22, 0)
        else:
            cls.EnableCtrl(skill, 22, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetCurVictim(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 1854):
            cl_action.SetSkillServerCache(skill, 'Super', True)
            if cl_action.TargetGetStateRemainTime(skill, cl_action.GetCurVID(skill), 1854) < (17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95):
                cl_action.TargetSetStateTime(skill, cl_action.GetCurVID(skill), 1854, (17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95) + 10)
                if cl_action.TargetGetStateRemainTime(skill, cl_action.GetCurVID(skill), 1864) < (17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95):
                    if not cl_action.CheckMonsterType(skill, WARRIOR_ELITE, cl_action.GetCurVID(skill)) or cl_action.CheckMonsterType(skill, WARRIOR_BOSS, cl_action.GetCurVID(skill)):
                        cl_action.TargetSetStateTime(skill, cl_action.GetCurVID(skill), 1864, (17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95) + 10)
                    else:
                        cl_action.SetSkillServerCache(skill, 'Super', False)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95, 1)
        else:
            cls.EnableCtrl(skill, 17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyPFTransDamFactor(skill)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2:
        cl_action.TargetAddState(skill, 32949, (17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95) + 10, 1, { }, cl_action.GetCurVID(skill))
    elif not cl_action.CheckMonsterType(skill, WARRIOR_BOSS, cl_action.GetCurVID(skill)):
        cl_action.TargetAddState(skill, 32958, 17 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) == 360 else 55 if cl_action.CheckHasState(skill, 33007) and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) >= 180 and cl_action.GetAttackerStateCount(skill, 33007, dState = { }) < 360 else 95, 1, { }, cl_action.GetCurVID(skill))
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1328
    m_Name = '#NT#处决（灵佑触发）'
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
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 70000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 7000,
        'ExplodeDelay': 200,
        'Radius': 2,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 3000
    
    def SendUseMsg(self, oWarrior, oSkill):
        iCurVID = cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTINT)[0]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_START, oWarrior, {
            'Skill': oSkill,
            'UnCrtByOwnerSign': self.m_UnCrtByOwnerSign,
            'CurVID': iCurVID }, iSub = self.m_SubMsg)

    
    def CalBulletUse(self, oSkill):
        return 0

    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_CanUseCount = 0

    
    def AddCanUseCount(self, iAdd = 1):
        self.m_CanUseCount += iAdd

    
    def CanUse(self, oWarrior, dInfo):
        if self.m_CanUseCount < 1:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        self.m_CanUseCount -= 1
        super().UsePerform(oWarrior, oSkill)


