# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p24011.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p24011.pyc
# Source Generated with Decompyle++
# File: p24011.pyc (Python 3.6)

from cl_only import Functor
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_snetwar
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon2(RayCastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 30 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtMonsterCustomMuzzlePos(skill, 'CustomMuzzlePos', [
                cl_action.GetCartoonLoopID(skill, 1),
                1.75,
                0.4]), cl_action.CrtMonsterCustomMuzzlePos(skill, 'CustomMuzzlePos', [
                cl_action.GetCartoonLoopID(skill, 1),
                1.75,
                0.4]), cl_action.CrtArgMissingPos(skill, 0.5), 1, 75, 60, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 3, radius = 0, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'waittime'), 1)

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
        cl_action.SetSkillVarCache(skill, 'waittime', 4)
        for i1 in range(0, cl_action.GetRandomInRange(skill, 8, 10), 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = i1)
            cl_action.SetSkillVarCache(skill, 'waittime', cl_action.GetSkillVarCache(skill, 'waittime') + (30 - i1 * 5 if 30 - i1 * 5 > cl_action.GetAttackerAttr(skill, 'AttSpeed') else cl_action.GetAttackerAttr(skill, 'AttSpeed')))
        
        cl_action.StartBackSwing(skill, 180)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.CustomPerformAction(skill, 24011, 'CustomLockTarget', [
            120])

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
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    cl_action.CustomPerformAction(skill, 24011, 'CustomUnlockFace', [
        300,
        50])


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 24011
    m_Name = '【第四幕】召唤怪-连射'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 900,
        'AttDistance': 80,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']


def CustomMuzzlePos(oSkill, *args):
    iIndex = args[0][0]
    fDis = args[0][1]
    fy = args[0][2]
    oAttack = oSkill.GetAttack()
    return GetCannonPos(oAttack, iIndex % 3, fy, fDis)


def CustomLockTarget(oSkill, *args):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    iVictim = oSkill.m_Base['VID']
    oVictim = oGame.GetObject(iVictim)
    iTurnSpeed = args[0][0]
    if not oVictim:
        return None
    dAffiliateMonster = oAttack.Query('AffiliateMonster', { })
    for iMonster in dAffiliateMonster:
        cl_snetwar.GS2CConstantFaceTarget(oGame, oAttack.m_Scene, iMonster, iVictim, iTurnSpeed)
    


def CustomUnlockFace(oSkill, *args):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    iIndex = 0
    (iTime, y) = args[0]
    dAffiliateMonster = oAttack.Query('AffiliateMonster', { })
    for iMonster in dAffiliateMonster:
        cl_snetwar.GS2CConstantFaceTarget(oGame, oAttack.m_Scene, iMonster, 0, 0)
        iAngle = (iIndex % 3) * 120
        vFace = cl_math.RotateAroundVector(oAttack.GetFacing(), (0, 1, 0), iAngle)
        oMonster = oGame.GetObject(iMonster)
        oGame.SetFacing(iMonster, vFace)
        (x, _, z) = oMonster.GetNetFacing()
        cl_snetwar.GS2CFace(oGame, oAttack.m_Scene, iMonster, (x, y, z), iTime)
        iIndex += 1
    


def GetCannonPos(oAttack, iIndex, fy, fDis):
    vOwner = oAttack.GetPos()
    vOwner = (vOwner[0], vOwner[1] + fy, vOwner[2])
    iAngle = (iIndex % 3) * 120
    vFace = cl_math.RotateAroundVector(oAttack.GetFacing(), (0, 1, 0), iAngle)
    if cl_math.IsZero(vFace):
        return vOwner
    vPos = cl_math.Vec3DisplaceDir(vOwner, vFace, fDis)
    return vPos

