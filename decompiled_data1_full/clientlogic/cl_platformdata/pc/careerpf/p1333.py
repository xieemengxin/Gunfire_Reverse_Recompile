# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1333.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1333.pyc
# Source Generated with Decompyle++
# File: p1333.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import PLANT_PHASE_NORMAL, PLANT_PHASE_TREE, PLANT_TRANSDAM_STATE, STATE_TIME_FOREVER, WARRIOR_SUMMON_SEED
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_CYLINDER, CRT_CHECK_SERVER, CRT_EXTCHECK_SEEDPLANT, OBJ_ALL, SKILLCACHE_LSTPOS, SKILLCACHE_POS, WARRIOR_MONSTER, WARRIOR_PLANT, WARRIOR_SUMMON_SEED

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CustomPerformAction(skill, 1333, 'DisposeCreate', { })
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'HitMonster': cl_action.GetSkillCustomData(skill, 'HitMonster', defaultValue = 0),
            'CreatePlant': cl_action.GetSkillCustomData(skill, 'CreatePlant', defaultValue = 0) }, sSubMsgKey = '')
        cl_action.CustomPerformAction(skill, 1333, 'AddPlantTransDamFactor', { })

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckMonsterType(skill, WARRIOR_SUMMON_SEED, cl_action.GetCurVID(skill)):
            cl_action.UpdateFieldSeedInfo(skill)
        if cl_action.CheckMonsterType(skill, WARRIOR_PLANT, cl_action.GetCurVID(skill)) and cl_action.GetTargetOwnerID(skill, cl_action.GetCurVID(skill)) == cl_action.GetSkillAID(skill):
            cl_action.UpdateDictSkillCustomData(skill, 'HitPlant', cl_action.GetCurVID(skill), cl_action.GetTargetPhase(skill, cl_action.GetCurVID(skill)))
        if cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)):
            cl_action.SetSkillCustomDataInt(skill, 'HitMonster', 1)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), end = cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                5], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ALL, pierceStatic = True, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0)), [
                skill.m_Cache['Radius'],
                5], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ALL, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_SEEDPLANT, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.SetSkillServerCache(skill, 'CatalyzeNum', 0)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    if cl_math.CalDistance3D(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, -10000, 0)) > 0.1:
        if cl_action.CheckClientCtrl(skill):
            cl_action.SkillHaltTargetPerform(skill, cl_action.GetSkillAID(skill), 8506)
            cl_action.CreateGardenerArea(skill, 2041, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetScaleByOriginSize(10, cl_action.GetAttackerPerformAttr(skill, 1333, 'Radius')))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
            if cl_action.GetSpecificPerformArgValue(skill, 1333, 'DomainBarrierSummon', iDefault = 0) >= 1:
                cl_action.CreateSummonBarrier(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetScaleByOriginSize(cl_action.GetSkillBaseAttr(skill, 'Radius'), skill.m_Cache['Radius']), cl_action.GetSpecificPerformArgValue(skill, 1333, 'DomainBarrierSummon', iDefault = 0))
            else:
                cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetPosWithinCircle(skill, skill.m_Cache['Radius'], skill.m_Cache['AddStateTime'], True))
                cl_action.SkillHaltTargetPerform(skill, cl_action.GetSkillAID(skill), 8506)
                cl_action.CreateGardenerArea(skill, 2041, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetScaleByOriginSize(10, cl_action.GetAttackerPerformAttr(skill, 1333, 'Radius')))
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
                if cl_action.GetSpecificPerformArgValue(skill, 1333, 'DomainBarrierSummon', iDefault = 0) >= 1:
                    cl_action.CreateSummonBarrier(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetScaleByOriginSize(cl_action.GetSkillBaseAttr(skill, 'Radius'), skill.m_Cache['Radius']), cl_action.GetSpecificPerformArgValue(skill, 1333, 'DomainBarrierSummon', iDefault = 0))


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1333
    m_Name = '木灵召唤'
    m_ExtPerform = (12032, 8506)
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
        'ColdTime': 800,
        'AttDistance': 0,
        'MaxCover': 2,
        'UseInterval': 0,
        'AddStateTime': 1,
        'Att': 4000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 500,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'EvolveNum': 0,
        'CatalyzeNum': 1 }
    m_AIPerformDam = 1600


def DisposeCreate(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_GardenerCon):
        return None
    oGardenerCon = oAttack.m_GardenerCon
    iPerform = oSkill.m_Base['pfid']
    oPerform = oAttack.GetPerform(iPerform)
    dCustom = oSkill.m_Custom
    iEvolveNum = oPerform.GetArgValue('EvolveNum') if oPerform else 0
    iCreatePlantNum = min(oSkill.m_Cache['AddStateTime'], len(cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTPOS)))
    iHatchSeedNum = min(len(oGardenerCon.GetFieldSeedInfo()), cl_action.GetPerformArgValue(oSkill, 'CatalyzeNum', iDefault = 1))
    sKey = oSkill.m_Base['PFKey']
    if iEvolveNum:
        if iCreatePlantNum >= iEvolveNum:
            iCreatePlantNum -= iEvolveNum
            EvolvePlant(oSkill, oGardenerCon)
        elif iCreatePlantNum + iHatchSeedNum >= iEvolveNum:
            iEvolveNum -= iCreatePlantNum
            iCreatePlantNum = 0
            DeleteSeed(oAttack, iHatchSeedNum, sKey)
            iHatchSeedNum -= iEvolveNum
            EvolvePlant(oSkill, oGardenerCon)
        elif 'HitPlant' in dCustom:
            pass
        
        dPlant = { }
        dRemovePlant = { }
        iRemoveNum = 0
        for iPlant, iPlantPhase in dPlant.items():
            if iPlantPhase != PLANT_PHASE_NORMAL:
                continue
            oPlant = oGardenerCon.GetPlant(iPlant, PLANT_PHASE_NORMAL)
            if not oPlant or oPlant.Query('NotToEvole'):
                continue
            iRemoveNum += 1
            if iRemoveNum + iCreatePlantNum + iHatchSeedNum >= iEvolveNum:
                iCreatePlantNum = 0
                DeleteSeed(oAttack, iHatchSeedNum, sKey)
                iHatchSeedNum = 0
                for iRemovePlant in dRemovePlant:
                    oGardenerCon.ClearTargetPlant(iRemovePlant, sKey)
                
                EvolvePlant(oSkill, oGardenerCon, iTree = oPlant.m_ID)
                break
            dRemovePlant[iPlant] = 1
        
    for i1 in range(iCreatePlantNum):
        cl_action.CreatePlantByPos(oSkill, cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTPOS)[i1], 0, None)
    
    for iSeed in list(oGardenerCon.GetFieldSeedInfo()):
        if not iHatchSeedNum:
            break
        iHatchSeedNum -= 1
        oPlant = oAttack.m_GardenerCon.HatchSeed(iSeed, sKey)
        if not oPlant:
            continue
        cl_action.CollectPlantInfo(oSkill, oPlant.m_ID, PLANT_PHASE_NORMAL)
    


def EvolvePlant(oSkill, oGardenerCon, iTree = 0):
    iPlantPhase = PLANT_PHASE_TREE
    if iTree:
        oGardenerCon.SetPlantPhase(iTree, iPlantPhase)
        oSkill.m_Custom['HitPlant'][iTree] = iPlantPhase
    else:
        vPos = cl_action.GetSkillCacheData(oSkill, SKILLCACHE_POS)
        oTree = oGardenerCon.CreatePlant(vPos, iPlantPhase, iCheckPos = 0, sReason = oSkill.m_Base['PFKey'])
        if oTree:
            cl_action.CollectPlantInfo(oSkill, oTree.m_ID, iPlantPhase)


def DeleteSeed(oAttack, iDeleteSeedNum, sReason):
    oGardenerCon = oAttack.m_GardenerCon
    for iSeed in list(oGardenerCon.GetFieldSeedInfo()):
        if not iDeleteSeedNum:
            break
        iDeleteSeedNum -= 1
        oGardenerCon.RemoveSeed(iSeed, sReason)
    


def AddPlantTransDamFactor(oSkill, *arg):
    dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    dPlant = oSkill.m_Custom['CreatePlant'] if 'CreatePlant' in oSkill.m_Custom else { }
    if not dPlant:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iAttackID = oAttack.m_ID
    oGardenerCon = oAttack.m_GardenerCon
    iTimeType = STATE_TIME_FOREVER
    for iPlant in dPlant:
        oPlant = oGardenerCon.GetPlant(iPlant)
        if not oPlant:
            continue
        oReason = oSkill.m_Base['RS'].ExtInfo({
            'ActNum': oSkill.m_Base['ActNum'] })
        dData = {
            'AID': iAttackID,
            'RS': oReason,
            'arg': {
                'TransDamFactor': dTransFactor } }
        oState = cl_state.AddState(oPlant, PLANT_TRANSDAM_STATE, iTimeType, iTime = 0, dState = dData)
        if not oState:
            continue
        oState.Enable(oPlant)
    

