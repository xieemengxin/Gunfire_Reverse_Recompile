# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9215.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9215.pyc
# Source Generated with Decompyle++
# File: p9215.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_drop
from cl_commondefines import WARRIOR_OBSTACLE_NORMAL, OBSTACLE_JAR, NWARRIOR_DROP_AXE, STATUS_STOP
from cl_newformula import GetWarriorAttr
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, HIT_OVER_NORMAL, MONSTER_PART_SHIELD, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_POS, WARRIOR_MONSTER, WARRIOR_OBSTACLE_NORMAL

class CCartoon8(TimerCartoon):
    m_SID = 8
    
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
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_OBSTACLE_NORMAL, OBJ_ALL):
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)

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
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ThrowByPowerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'MoveDir', cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if (cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALL) or cl_action.CheckHitPointArea(skill, MONSTER_PART_SHIELD)) and cl_action.GetSkillServerCache(skill, 'DropAxe') >= 1:
            cl_action.CustomPerformAction(skill, 9215, 'DropAxe', {
                'StateSID': 1655,
                'StateTime': 0 if cl_action.CheckHasInscription(skill, 4962) else 300,
                'DistanceParam1': 50,
                'DistanceParam2': 3,
                'MinFlyTime': 120,
                'MaxFlyTime': 150,
                'MinFlyDis': 15,
                'MaxFlyDis': 30,
                'Angle': 45,
                'ExtTime': 600 if cl_action.CheckHasInscription(skill, 4961) else 100,
                'BossStoneSID': 39091,
                'AirWallLen': 17 })
        elif cl_action.CheckVictimType(skill, WARRIOR_OBSTACLE_NORMAL, OBJ_ALL):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgMuzzlePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, 0.7, (0, -10, 0), (1, 1), 500, True, True, 0, 0, None, 0, innerRadius = 0.05, pierce = skill.m_Cache['Pierce'], ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3)

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
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    cl_action.SetSkillServerCache(skill, 'DropAxe', 0)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1066)


def End(skill):
    cl_action.SkillForbid(skill, False, 1066)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9215
    m_Name = '#NT#飞斧'
    m_ExtPerform = (4330,)
    m_HaltInfo = {
        10214: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'MaxPFBullet': 1,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001


def DropAxe(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim)
    if not oVictim or oVictim.IsWudi():
        return None
    vVictimPos = oVictim.GetPos()
    vPosStart = oAttack.GetPos()
    iScene = oSkill.m_Base['Scene']
    dInfo = args[0]
    vDropPos = vPosStart
    if oAttack.m_MoveCtrl.m_CurStatus != STATUS_STOP and oSkill.m_Collect['MoveDir'] and not cl_math.IsZero(oSkill.m_Collect['MoveDir']):
        fDistance = cl_math.CalDistance(vPosStart, vVictimPos)
        fFlyDistance = GetWarriorAttr('MoveSpeed', oAttack) * dInfo['DistanceParam1'] * 0.01 + dInfo['DistanceParam2']
        if fDistance <= fFlyDistance and not cl_math.CheckVector2Angle(cl_math.Vec3Minus(vVictimPos, vPosStart), oSkill.m_Collect['MoveDir'], dInfo['Angle']):
            fFlyDistance = fDistance - 2
        vPosEnd = cl_math.Vec3DisplaceDir(vPosStart, oSkill.m_Collect['MoveDir'], fFlyDistance)
        vPosEnd = oGame.Scene_NavMeshRayCast(iScene, vPosStart, vPosEnd)
        if oVictim.m_SID == dInfo['BossStoneSID'] and abs(vPosEnd[2] - vVictimPos[2]) < dInfo['AirWallLen']:
            vDropPos = vPosStart
        else:
            vDropPos = vPosEnd
    iFlyTime = CalcFlyTime(dInfo['MinFlyTime'], dInfo['MaxFlyTime'], dInfo['MinFlyDis'], dInfo['MaxFlyDis'], vVictimPos, vDropPos)
    dInfo['ExtTime'] += iFlyTime
    dInfo['Item'] = oSkill.m_Base['Weapon']
    dExtraInfo = {
        'Abandoner': iVictim }
    lstDropData = [
        dInfo]
    oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_AXE, vDropPos, lstDropData, dExtraInfo, {
        'DropSource': oAttack.m_PlayerID }, oAttack.m_ID)


def CalcFlyTime(iMinTime, iMaxTime, iMinDis, iMaxDis, vStart, vEnd):
    fDistance = cl_math.CalDistance(vStart, vEnd)
    if fDistance >= iMaxDis:
        return iMaxTime
    if fDistance <= iMinDis:
        return iMinTime
    return int(iMinTime + (iMaxTime - iMinTime) * (fDistance - iMinDis) / (iMaxDis - iMinDis))

