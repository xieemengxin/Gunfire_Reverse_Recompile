# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9606.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9606.pyc
# Source Generated with Decompyle++
# File: p9606.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MeleeWeaponCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_NORMAL

class CCartoon3(MeleeWeaponCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            if cl_action.CheckHasState(skill, 1849):
                if cl_action.CheckVictimType(skill, WARRIOR_NORMAL, OBJ_ENEMY):
                    if cl_action.CheckPosIsNavMeshArrive(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), cl_math.Vec3Minus(cl_action.GetEndPositionInCrt(skill, 3), cl_action.CrtArgSelfCenterPos(skill)), 0.3, True, iOffset = 0.1):
                        cl_action.PushMoveVictim(skill, (0, 0, 0), cl_action.GetAttackerAttr(skill, 'MoveSpeed') + 0.15, ((cl_action.GetAttackerAttr(skill, 'MoveSpeed') - 6) / 6 + 1) * 1.26, cl_math.Vec3Minus(cl_action.GetEndPositionInCrt(skill, 3), cl_action.CrtArgSelfCenterPos(skill)), iCartoonSID = -1, bKnockBack = True)
                        cl_action.AttackerAddState(skill, 1850, 17, 0, {
                            'IsNormal': 1 if cl_action.CheckVictimType(skill, WARRIOR_NORMAL, OBJ_ENEMY) else 0 })
                        cl_action.WeaponDamage(skill, {
                            'Att': 100 }, { }, sendPFMsg = False)
                    else:
                        cl_action.AttackerAddState(skill, 1850, 17, 0, {
                            'IsNormal': 0 })
                        cl_action.WeaponDamage(skill, {
                            'Att': 100 }, { }, sendPFMsg = False)
                else:
                    cl_action.AttackerAddState(skill, 1850, 17, 0, {
                        'IsNormal': 1 if cl_action.CheckVictimType(skill, WARRIOR_NORMAL, OBJ_ENEMY) else 0 })
                    cl_action.WeaponDamage(skill, {
                        'Att': 100 }, { }, sendPFMsg = False)
            else:
                cl_action.WeaponDamage(skill, {
                    'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                0.5,
                75,
                20], meshCount = 1, totalTime = 10, targettype = OBJ_ENEMY, pierceStatic = False, left2right = False, center2around = True, canCritical = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasState(skill, 1849):
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i1)
        
    else:
        for i2 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i2)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9606
    m_Name = '钻头'
    m_ExtPerform = (5312,)
    m_HaltInfo = { }
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
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

