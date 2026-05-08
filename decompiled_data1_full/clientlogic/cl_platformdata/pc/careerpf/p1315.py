# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1315.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1315.pyc
# Source Generated with Decompyle++
# File: p1315.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RangeSpreadCartoon, TimerCartoon, TraceCartoon
from cl_item.defines import EQUIP_HANDGUN, EQUIP_LASER, EQUIP_RIFLE, EQUIP_ROCKET_LAUNCHER, EQUIP_SHOTGUN, EQUIP_SMG, EQUIP_TYPE_CLOSEWEAPON, EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_BARRIAR, NWARRIOR_NPC_SHOP, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, WARRIOR_OBSTACLE_NORMAL

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetCrtValue(skill, 0, 'launcher_mark', iDefault = 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.CustomPerformAction(skill, 1315, 'CustomSetLastExplosionTrigger', [])
        for i1 in range(0, cl_action.GetSkillVarCache(skill, 'sk1315_trajectory'), 1):
            if cl_action.GetSkillVarCache(skill, 'sk1315_trajectory') - 1 == i1:
                if cl_action.ListHasWeaponType(skill, EQUIP_ROCKET_LAUNCHER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or 1 == cl_action.GetSkillServerCache(skill, 'LastExplosionTrigger'):
                    cl_action.SetSkillServerCache(skill, 'LastTrigger', 1)
            cl_action.SetSkillServerCache(skill, 'LastTrigger', 1)
            if i1 == 0:
                if cl_action.ListHasWeaponType(skill, EQUIP_SMG, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_RIFLE, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_LASER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
                    cl_action.ModifySkillCache(skill, 'Att', (cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) if cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) > 0 else cl_action.GetCurWeaponAttr(skill, 'Att')) + 50000)
                elif cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) > 0:
                    pass
                
            skill('Att', cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0), cl_action.GetCurWeaponAttr(skill, 'Att'))
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillVarCache(skill, 'sk1315_damageratio') }, { }, sendPFMsg = False)
            cl_action.SetSkillServerCache(skill, 'LastTrigger', 0)
        
        cl_action.SetAttackerCustomIntData(skill, 'StrengthWeaponAtt', 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                6 if skill.m_Cache['MultipleExplodeCnt'] == 0 else skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        elif skill.m_Cache['MultipleExplodeCnt'] == 0:
            pass
        
        skill(cl_action.CrtArgHitPos(skill), (0, 0, 0), 6, [
            skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RangeSpreadCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.ListHasWeaponType(skill, EQUIP_TYPE_CLOSEWEAPON, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cl_action.AttackerAddState(skill, 32655, 0, 0, { })
        if cl_action.CheckHasTalent(skill, 3006) and cl_action.GetCartoonHitTargetInOrder(skill, 2) != 0:
            cl_action.AttackerAddState(skill, 32721, 0, 1, { })
        cl_action.SetSkillVarCache(skill, 'sk1315_damageratio', int((cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) * 100 / 10) if (cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) > 10 else 100)
        cl_action.SetSkillVarCache(skill, 'sk1315_trajectory', 10(int if (cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) > 10 else cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { })
        cl_action.SetSkillServerCache(skill, 'mengji_hitidx', int(cl_action.GetSkillServerCache(skill, 'mengji_hitidx') + 1))
        if cl_action.GetAttackerStateCount(skill, 32666, dState = { }) > cl_action.CrtArgRandomNum(skill, 0, 100):
            cl_action.SetSkillServerCache(skill, 'Smash_IsCrazy', 1)
        else:
            cl_action.SetSkillServerCache(skill, 'Smash_IsCrazy', 0)
        cl_action.ModifySkillCache(skill, 'Att', cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) if cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) > 0 else cl_action.GetCurWeaponAttr(skill, 'Att'))
        if cl_action.ListHasWeaponType(skill, EQUIP_ROCKET_LAUNCHER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        else:
            for i2 in range(0, cl_action.GetSkillVarCache(skill, 'sk1315_trajectory'), 1):
                if cl_action.GetSkillVarCache(skill, 'sk1315_trajectory') - 1 == i2:
                    if cl_action.ListHasWeaponType(skill, EQUIP_ROCKET_LAUNCHER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or 1 == cl_action.GetSkillServerCache(skill, 'LastExplosionTrigger'):
                        cl_action.SetSkillServerCache(skill, 'LastTrigger', 1)
                cl_action.SetSkillServerCache(skill, 'LastTrigger', 1)
                if i2 == 0:
                    if cl_action.ListHasWeaponType(skill, EQUIP_SMG, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_RIFLE, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_LASER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
                        cl_action.ModifySkillCache(skill, 'Att', (cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) if cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) > 0 else cl_action.GetCurWeaponAttr(skill, 'Att')) + 50000)
                elif cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0) > 0:
                    pass
                
                skill('Att', cl_action.GetAttackerCustomData(skill, 'StrengthWeaponAtt', iDefault = 0), cl_action.GetCurWeaponAttr(skill, 'Att'))
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.GetSkillVarCache(skill, 'sk1315_damageratio') }, { }, sendPFMsg = False)
                cl_action.SetSkillServerCache(skill, 'LastTrigger', 0)
            
            cl_action.SetAttackerCustomIntData(skill, 'StrengthWeaponAtt', 0)
        if cl_action.CheckHasState(skill, 32655):
            cl_action.AttackerRemoveState(skill, 32655, bSameItem = False)
        cl_action.SetSkillVarCache(skill, 'hitindex', int(cl_action.GetSkillVarCache(skill, 'hitindex') + 1))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetEndPositionInCrt(skill, 2), cl_action.GetCartoonHitTargetInOrder(skill, 2), int(cl_action.GetSmashTimes(skill) + 0) if cl_action.ListHasWeaponType(skill, EQUIP_HANDGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_TYPE_FUNDAMENTALWEAPON, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetSmashTimes(skill), skill.m_Cache['AddStateTime'], 0, 1.2, 0.2, 0.9, 1.7)
        elif cl_action.ListHasWeaponType(skill, EQUIP_HANDGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_TYPE_FUNDAMENTALWEAPON, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            pass
        
        skill(cl_action.GetEndPositionInCrt(skill, 2), cl_action.GetCartoonHitTargetInOrder(skill, 2), int(cl_action.GetSmashTimes(skill) + 0), cl_action.GetSmashTimes(skill), skill.m_Cache['AddStateTime'], 0, 1.2, 0.2, 0.9, 1.7)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_OBSTACLE_NORMAL, OBJ_ENEMY):
            cl_action.PerformDamage(skill, {
                'Att': 1000 })
        elif cl_action.CheckHitPointArea(skill, MONSTER_PART_BARRIAR):
            cl_action.IgnoreCurVictimOnceAfterHit(skill)
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if cl_action.CheckHasTalent(skill, 5019):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0.1, -0.2, 0.4))):
                return None
            cls.EnableShow(skill, 1, 50, 100, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = cl_action.CalLockDistance(skill, 20), angle = 90, lockDis = 0, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = False, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, traceTimes = 1, maskFightType = NWARRIOR_NPC_SHOP, noTargetOver = False, searchByDistance = False)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0.1, -0.2, 0.4)), cl_action.GetSceneCenterPosition(skill, cartoon), 1, 50, 100, showstart = (0, 0, 0), targettype = OBJ_ENEMY, targetID = 0, liveTime = 0, lineDistance = cl_action.CalLockDistance(skill, 20), angle = 90, lockWeakness = False, lockAngle = 0, canDesAngle = 0, lockDis = 0, IgnoreDefalutDis = 0, IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = False, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, lockSumm = False, lockCanDestroy = False, lockHideDoor = False, isBlocked = False, isMonsterFirst = False, lockExplode = False, traceTimes = 1, maskFightType = NWARRIOR_NPC_SHOP, noTargetOver = False, searchByDistance = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
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
        cl_action.SetSkillVarCache(skill, 'index', 1)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 75, 1)
        else:
            cls.EnableCtrl(skill, 75, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)
    cl_action.SetSkillServerCache(skill, 'mengji_hitidx', 0)
    cl_action.SetSkillVarCache(skill, 'hitindex', 0)
    cl_action.SetSkillServerCache(skill, 'LastExplosionTrigger', 0)
    cl_action.ModifySkillCacheValue(skill, 'MultipleExplodeCnt', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[0])
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CWeaponPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1315
    m_Name = '破魂'
    m_ExtPerform = (8505, 1319)
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
        'ColdTime': 1600,
        'AttDistance': 25,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 1,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 50,
        'DebuffProb': 4000,
        'ExplodeDelay': 200,
        'Radius': 6,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 4,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 3200
    
    def UsePerform(self, oWarrior, oSkill):
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            oWeapon = oWarrior.m_WieldCon.GetCurWeapon()
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_LSTINT, [
                oWeapon.m_Type])
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_LSTINTSPECIAL, [
                0])
        super().UsePerform(oWarrior, oSkill)



def CustomSetLastExplosionTrigger(oSkill, *args):
    oSkill.m_Collect['LastExplosionTrigger'] = 0
    if 'LastVLST' not in oSkill.m_Update:
        return None
    lstVictim = oSkill.m_Update['LastVLST']
    if not lstVictim:
        return None
    if lstVictim[-1] == oSkill.m_Update['CurVID']:
        oSkill.m_Collect['LastExplosionTrigger'] = 1

