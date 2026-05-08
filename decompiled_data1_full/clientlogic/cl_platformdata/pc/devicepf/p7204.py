# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7204.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7204.pyc
# Source Generated with Decompyle++
# File: p7204.pyc (Python 3.6)

from cl_platformdata.custom.commonative.customaction import CommonAddToxicCount
from cl_commondefines import TOXIC_FOG, TOXIC_DAM
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ALL, OBJ_ENEMY, OBJ_FRIEND, SKILLCACHE_LSTINT, SKILLCACHE_POS, SKILLCACHE_SIGNSPEED

class CCartoon6(DelegateDirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CustomPerformAction(skill, 7204, 'PF50101FirstDam', { })

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY) and cl_action.GetSkillCustomData(skill, 'd50235_flag', defaultValue = '0') == 1:
            cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
                'CurVID': cl_action.GetCurVID(skill) })
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY):
            if cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0) > 0:
                cl_action.VictimAddState(skill, 33075, 50, 0, {
                    'PF50105LV': cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0),
                    'Decelerate': cl_action.GetSkillCustomData(skill, 'PF50105Decelerate', defaultValue = 0) })
                if not cl_action.GetDictValueFromSkillCustomData(skill, 'skill7204HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                    cl_action.CustomPerformAction(skill, 7204, 'AddToxicCount', {
                        'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                    cl_action.UpdateDictSkillCustomData(skill, 'skill7204HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxicCD', iDefault = 1))
                elif not cl_action.GetDictValueFromSkillCustomData(skill, 'skill7204HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                    cl_action.CustomPerformAction(skill, 7204, 'AddToxicCount', {
                        'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                    cl_action.UpdateDictSkillCustomData(skill, 'skill7204HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxicCD', iDefault = 1))
            elif cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
                if cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0) > 0:
                    cl_action.VictimAddState(skill, 33076, 50, 0, {
                        'PF50101LV': cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0),
                        'Accelerate': cl_action.GetSkillCustomData(skill, 'PF50105Accelerate', defaultValue = 0) })
                if cl_action.GetSkillCustomData(skill, 'PF50238', defaultValue = 0) > 0 and cl_action.GetCurVID(skill) == cl_action.GetAttackerOwnerID(skill):
                    cl_action.VictimAddState(skill, 33862, 53, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetMuzzlePos(skill) if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] < 2 else cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_SIGNSPEED)], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = True, explosion = False, useclientpos = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] < 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'IsFirst', 1)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 52, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1] / 50)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        cl_action.SetSkillVarCache(skill, 'DevicePos', cl_action.GetMuzzlePos(skill))
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetSkillCustomData(skill, 'PosType', defaultValue = 0),
        cl_action.GetPerformArgValue(skill, 'Duration', iDefault = 0) if cl_action.GetSkillCustomData(skill, 'KeepTime', defaultValue = 0) == 0 else cl_action.GetSkillCustomData(skill, 'KeepTime', defaultValue = 0)])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_SIGNSPEED, skill.m_Cache['Radius'] * (cl_action.GetSkillCustomData(skill, 'AddRadiusRatio', defaultValue = 0) / 100 + 1))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT,
        SKILLCACHE_POS,
        SKILLCACHE_SIGNSPEED])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_POS,
        SKILLCACHE_SIGNSPEED]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CDeviceActive as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7204
    m_Name = '毒气装置-毒雾技能'
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
        'ColdTime': 0,
        'AttDistance': 10,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'EnergyCost': 1000,
        'Radius': 4,
        'CommonMaxCount': 5 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (1,)
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000,
        'ToxicStateSID': 33137,
        'AddCount': 1,
        'ToxicTime': 300,
        'NeedAddEasilyInjure': 0,
        'Duration': 500,
        'ToxicCD': 1 }


def AddToxicCount(oSkill, *args):
    iTarget = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    iAttack = oSkill.m_Base['AID']
    dArgDataCache = oSkill.m_Cache['ArgData']
    iToxicStateSID = dArgDataCache['ToxicStateSID']
    dCustomData = {
        'ToxicStateSID': iToxicStateSID,
        'ToxicTime': dArgDataCache['ToxicTime'],
        'MaxCount': oSkill.m_Cache['CommonMaxCount'],
        'AddCount': dArgDataCache['AddCount'],
        'NeedAddEasilyInjure': dArgDataCache['NeedAddEasilyInjure'] }
    if 'PF50101' in oSkill.m_Custom and not oTarget.m_State.CheckHasStateFrom(iToxicStateSID, iAttack, 0):
        if 'NeedToBeHurtTarget' not in oSkill.m_Collect:
            oSkill.m_Collect['NeedToBeHurtTarget'] = { }
        oSkill.m_Collect['NeedToBeHurtTarget'][iTarget] = 1
    CommonAddToxicCount(oTarget, iAttack, dCustomData)


def ToxicDam(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    pfobj = oAttack.GetPerform(TOXIC_DAM)
    if not pfobj:
        return None
    ToxicPerfrom = oAttack.GetPerform(TOXIC_FOG)
    if not ToxicPerfrom:
        return None
    dArgDataCache = oSkill.m_Cache['ArgData']
    dCustomData = {
        'ToxicStateSID': dArgDataCache['ToxicStateSID'] if 'ToxicStateSID' in dArgDataCache else ToxicPerfrom.GetArgValue('ToxicStateSID', 0),
        'MaxCount': oSkill.m_Cache['CommonMaxCount'] }
    iVID = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
    dData = {
        'Custom': dCustomData,
        'VID': iVID }
    cl_war.UsePerform(oAttack, pfobj, dData)


def PF50101FirstDam(oSkill, *args):
    if 'PF50101' not in oSkill.m_Custom:
        return None
    dTarget = oSkill.m_Collect['NeedToBeHurtTarget'] if 'NeedToBeHurtTarget' in oSkill.m_Collect else { }
    if not dTarget:
        return None
    oDevice = oSkill.GetAttack()
    if not oDevice:
        return None
    pfobj = oDevice.GetPerform(TOXIC_DAM)
    if not pfobj:
        return None
    oToxicPerform = oDevice.GetPerform(TOXIC_FOG)
    if not oToxicPerform:
        return None
    dCustomData = {
        'MaxCount': oSkill.m_Cache['CommonMaxCount'] }
    dData = {
        'Custom': dCustomData }
    for iTarget in dTarget:
        dData['VID'] = iTarget
        cl_war.UsePerform(oDevice, pfobj, dData)
    
    oSkill.m_Collect['NeedToBeHurtTarget'] = { }

