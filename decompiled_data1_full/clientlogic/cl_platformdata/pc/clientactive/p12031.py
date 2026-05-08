# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12031.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12031.pyc
# Source Generated with Decompyle++
# File: p12031.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object
from cl_commondefines import GARDENER_THROW_TYPE_NORMAL, WARRIOR_PLANT, WARRIOR_BUILD, OBSTACLE_JAR, WARRIOR_MONSTER, PLANT_PHASE_NORMAL, GARDENER_PARASITIC_STATE, CHECKAIM_STATE_CANAIM, CHECKAIM_STATE_NOTAIMOBJ, OBSTACLE_EXPLODE
from cl_object.logging import GardenerLog
from cl_platformdata import GetGardenerAimThrowType
from cl_perform.cartoon.defines import AimTriggerCartoon, DoubleClickUseCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
            cls.EnableShow(skill, 12, 0)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 33, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DoubleClickUseCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CustomPerformAction(skill, 12031, 'StartThrowPF', { })
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 3000)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(AimTriggerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.CustomPerformAction(skill, 12031, 'CollectAimInfo', { })
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'ThrowType': cl_action.GetSkillCustomData(skill, 'ThrowType', defaultValue = 0) })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 1, 25)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 12, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.CustomPerformAction(skill, 12031, 'RemoveAimJar', { })


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12031
    m_Name = '#园丁Q前置'
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
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    
    def CanUse(self, oWarrior, dInfo):
        self.m_CanUseCount = 1
        return super().CanUse(oWarrior, dInfo)



def StartThrowPF(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iAimTarget = oSkill.m_Custom['AimTarget'] if 'AimTarget' in oSkill.m_Custom else 0
    iThrowType = oSkill.m_Custom['ThrowType'] if 'ThrowType' in oSkill.m_Custom else GARDENER_THROW_TYPE_NORMAL
    dInfo = {
        'BuffInfo': oSkill.m_Custom['BuffInfo'] if 'BuffInfo' in oSkill.m_Custom else { },
        'PlantPhase': oSkill.m_Custom['PlantPhase'] if 'PlantPhase' in oSkill.m_Custom else PLANT_PHASE_NORMAL,
        'Shape': oSkill.m_Custom['AimTargetShape'] if 'AimTargetShape' in oSkill.m_Custom else 0,
        'AimJar': oSkill.m_Custom['AimJar'] if 'AimJar' in oSkill.m_Custom else 0,
        'ExtraAddParasiticCount': oSkill.m_Custom['ExtraAddParasiticCount'] if 'ExtraAddParasiticCount' in oSkill.m_Custom else 0,
        'ExplodeJarInfo': oSkill.m_Custom['ExplodeJarInfo'] if 'ExplodeJarInfo' in oSkill.m_Custom else { } }
    oAttack.m_GardenerCon.StartThrowPF(iAimTarget, iThrowType, dInfo)


def CollectAimInfo(oSkill, *args):
    dCustom = oSkill.m_Custom
    if 'LockTarget' not in dCustom:
        return None
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGardenerCon = oAttack.m_GardenerCon
    for iTarget in dCustom['LockTarget']:
        iCheckAimState = oGardenerCon.CheckValidGardenerAim(iTarget)
        oTarget = oGame.GetObject(iTarget)
        if iCheckAimState != CHECKAIM_STATE_CANAIM:
            if iCheckAimState != CHECKAIM_STATE_NOTAIMOBJ:
                GardenerLog.Alert('%s %s gardener aim err %s %s %s' % (oGame.m_ID, oAttack.m_PlayerID, iCheckAimState, oTarget.m_Shape, oTarget.m_SID))
            else:
                GardenerLog.Debug('%s %s gardener not aim target' % (oGame.m_ID, oAttack.m_PlayerID))
            return None
        iShape = oTarget.m_Shape
        iThrowType = GetGardenerAimThrowType(iShape)
        oSkill.m_Custom['ThrowType'] = iThrowType
        oSkill.m_Custom['AimTargetShape'] = iShape
        oSkill.m_Custom['AimTarget'] = iTarget
        if iThrowType != GARDENER_THROW_TYPE_NORMAL:
            iFightType = oTarget.m_FightType
            if iFightType & WARRIOR_MONSTER:
                oParasiticState = oTarget.m_State.GetItemBySource(GARDENER_PARASITIC_STATE, oAttack.m_ID)
                if oParasiticState:
                    oSkill.m_Custom['ExtraAddParasiticCount'] = oParasiticState.GetCount()
                cl_action.SetDirectHitInfo(oSkill, iTarget)
                cl_action.KillTarget(oSkill, iTarget, iClearRelife = 1)
                return None
            if iFightType & WARRIOR_PLANT == WARRIOR_PLANT:
                dBuffInfo = oTarget.GetTransferState()
                oSkill.m_Custom['BuffInfo'] = dBuffInfo
                oSkill.m_Custom['PlantPhase'] = oTarget.Phase()
                oGardenerCon.ClearTargetPlant(iTarget, 'AimPlant')
                return None
            if iFightType & WARRIOR_BUILD and OBSTACLE_JAR in oTarget.m_ClassifyList:
                oGardenerCon.SetAimJar(iTarget)
                if oTarget.m_Scene:
                    oTarget.RemoveFromScene()
                oSkill.m_Custom['AimJar'] = iTarget
                oTarget.Set('Aiming', 1)
                dParam = oTarget.m_ModelData.GetServerData()
                oSkill.m_Custom['ExplodeJarInfo'] = {
                    'SID': oTarget.m_SID,
                    'Prefab': oTarget.m_Prefab,
                    'Line': oTarget.m_LineIdx,
                    'Scale': dParam['Scale'] if 'Scale' in dParam else (1, 1, 1),
                    'Angle': dParam['Angle'] if 'Angle' in dParam else (0, 0, 0),
                    'Center': dParam['Center'] if 'Center' in dParam else (0, 0, 0),
                    'Shape': oTarget.m_ModelData.m_ModelShape,
                    'Size': oTarget.m_ModelData.m_ModelSize,
                    'GlobalArea': oTarget.m_ClientGlobalArea }
                return None
            oTarget.Remove('AimPlant')
    


def RemoveAimJar(oSkill, *args):
    if 'AimJar' not in oSkill.m_Custom:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iJar = oSkill.m_Custom['AimJar']
    oGardenerCon = oAttack.m_GardenerCon
    if not oGardenerCon.CheckAimJar(iJar):
        return None
    oJar = oSkill.m_Game.GetObject(iJar)
    if not oJar:
        return None
    oJar.Remove('AimJar')
    oGardenerCon.ClearAimJar(iJar)

