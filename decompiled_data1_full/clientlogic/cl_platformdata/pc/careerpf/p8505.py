# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p8505.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p8505.pyc
# Source Generated with Decompyle++
# File: p8505.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_POS
from cl_item.defines import EQUIP_LASER, EQUIP_RIFLE, EQUIP_ROCKET_LAUNCHER, EQUIP_SHOTGUN, EQUIP_SMG, EQUIP_TYPE_CLOSEWEAPON

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetCrtValue(skill, 0, 'launcher_mark', iDefault = 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        for i1 in range(0, cl_action.GetSkillVarCache(skill, 'sk8505_trajectory'), 1):
            cl_action.WeaponDamage(skill, {
                'Att': int((cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) / 100) * cl_action.GetSkillVarCache(skill, 'sk8505_damageratio')) if cl_action.GetSkillCustomData(skill, 'Att', defaultValue = False) else cl_action.GetSkillVarCache(skill, 'sk8505_damageratio') }, { }, sendPFMsg = False)
            cl_action.ModifySkillCache(skill, 'Att', cl_action.GetSkillVarCache(skill, 'BaseAtt'))
        

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgHitPos(skill), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 8505, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        if cl_action.ListHasWeaponType(skill, EQUIP_TYPE_CLOSEWEAPON, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cl_action.AttackerAddState(skill, 32655, 0, 0, { })
        cl_action.SetSkillVarCache(skill, 'sk8505_damageratio', int((cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) * 100 / 10) if (cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) > 10 else 100)
        cl_action.SetSkillVarCache(skill, 'sk8505_trajectory', 10 if (cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill)) > 10 else cl_action.CalTrajectory(skill, 1.25) if cl_action.ListHasWeaponType(skill, EQUIP_SHOTGUN, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) else cl_action.GetTrajectory(skill))
        if cl_action.ListHasWeaponType(skill, EQUIP_SMG, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_RIFLE, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) or cl_action.ListHasWeaponType(skill, EQUIP_LASER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cl_action.ModifySkillCache(skill, 'Att', cl_action.GetWeaponIntAttr(skill, 'Att') + 50000)

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
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { })
        cl_action.SetSkillServerCache(skill, 'mengji_hitidx', int(cl_action.GetSkillServerCache(skill, 'mengji_hitidx') + 1))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
        cl_action.SetCurCartoonCurPos(skill, 1, cl_action.CrtArgHitPos(skill))
        if cl_action.GetAttackerStateCount(skill, 32666, dState = { }) > cl_action.CrtArgRandomNum(skill, 0, 100):
            cl_action.SetSkillServerCache(skill, 'Smash_IsCrazy', 1)
        else:
            cl_action.SetSkillServerCache(skill, 'Smash_IsCrazy', 0)
        if cl_action.ListHasWeaponType(skill, EQUIP_ROCKET_LAUNCHER, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        for i2 in range(0, cl_action.GetSkillVarCache(skill, 'sk8505_trajectory'), 1):
            cl_action.WeaponDamage(skill, {
                'Att': int((cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) / 100) * cl_action.GetSkillVarCache(skill, 'sk8505_damageratio')) if cl_action.GetSkillCustomData(skill, 'Att', defaultValue = False) else cl_action.GetSkillVarCache(skill, 'sk8505_damageratio') }, { }, sendPFMsg = False)
            cl_action.ModifySkillCache(skill, 'Att', cl_action.GetSkillVarCache(skill, 'BaseAtt'))
        
        if cl_action.CheckHasState(skill, 32655):
            cl_action.AttackerRemoveState(skill, 32655, bSameItem = False)
        cl_action.SetSkillVarCache(skill, 'hitindex', int(cl_action.GetSkillVarCache(skill, 'hitindex') + 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, cl_action.GetSkillCustomData(skill, 'chopsTimes', defaultValue = 0) if cl_action.GetSkillCustomData(skill, 'chopsTimes', defaultValue = 0) > 0 else 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 64, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgTargetPos(skill, notContainDying = False))
    cl_action.AddItemToLstInt(skill, cl_action.GetWeaponIntAttr(skill, 'ItemType'))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL, cl_action.CrtArgRandomIntList(skill, 0, 99, cl_action.GetSkillCustomData(skill, 'chopsTimes', defaultValue = 0) if cl_action.GetSkillCustomData(skill, 'chopsTimes', defaultValue = 0) > 0 else 1))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_POS])
    cl_action.SetSkillVarCache(skill, 'hitindex', 0)
    cl_action.SetSkillServerCache(skill, 'mengji_hitidx', 0)
    cl_action.SetSkillVarCache(skill, 'VictimPos', cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 2, 0)))
    cl_action.SetSkillVarCache(skill, 'BaseAtt', cl_action.GetWeaponIntAttr(skill, 'Att'))
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CWeaponPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8505
    m_Name = '#单体破魂斩'
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
        'ColdTime': 10,
        'AttDistance': 25,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 100,
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
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 3200

