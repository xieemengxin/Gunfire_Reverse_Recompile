# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1909.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1909.pyc
# Source Generated with Decompyle++
# File: p1909.pyc (Python 3.6)

from cl_platformdata.custom.commonative.customaction import CommonAddToxicCount
from cl_object import elementtype
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ALL, OBJ_ENEMY, OBJ_FRIEND, SKILLCACHE_LSTINT, SKILLCACHE_POS

class CCartoon6(DelegateDirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'IsFirst', defaultValue = 0) == 1:
            cl_action.SetSkillCustomDataInt(skill, 'IsFirst', 0)
            cl_action.SendCurCartoonTriggerMsg(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY):
            if cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0) > 0:
                cl_action.VictimAddState(skill, 33075, 50, 0, {
                    'PF50105LV': cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0),
                    'Decelerate': cl_action.GetSpecificPerformArgValue(skill, 50105, 'Decelerate', iDefault = -1000) })
                if cl_action.GetSkillCustomData(skill, 'HasPF50101', defaultValue = 0) > 0:
                    cl_action.VictimAddState(skill, 33077, 50, 0, {
                        'ToxicCount': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True),
                        'Decelerate': cl_action.GetSpecificPerformArgValue(skill, 50101, 'Decelerate', iDefault = -500) })
                    if not cl_action.GetDictValueFromSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                        cl_action.CustomPerformAction(skill, 1909, 'AddToxicCount', {
                            'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                        cl_action.UpdateDictSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxinCD', iDefault = 1))
                        cl_action.PerformDamage(skill, {
                            'Att': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True) * skill.m_Cache['Att'] })
                elif not cl_action.GetDictValueFromSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                    cl_action.CustomPerformAction(skill, 1909, 'AddToxicCount', {
                        'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                    cl_action.UpdateDictSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxinCD', iDefault = 1))
                    cl_action.PerformDamage(skill, {
                        'Att': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True) * skill.m_Cache['Att'] })
                elif cl_action.GetSkillCustomData(skill, 'HasPF50101', defaultValue = 0) > 0:
                    cl_action.VictimAddState(skill, 33077, 50, 0, {
                        'ToxicCount': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True),
                        'Decelerate': cl_action.GetSpecificPerformArgValue(skill, 50101, 'Decelerate', iDefault = -500) })
                    if not cl_action.GetDictValueFromSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                        cl_action.CustomPerformAction(skill, 1909, 'AddToxicCount', {
                            'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                        cl_action.UpdateDictSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxinCD', iDefault = 1))
                        cl_action.PerformDamage(skill, {
                            'Att': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True) * skill.m_Cache['Att'] })
                    elif not cl_action.GetDictValueFromSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), iDefault = 0) >= cl_action.GetNowFrame(skill):
                        cl_action.CustomPerformAction(skill, 1909, 'AddToxicCount', {
                            'EasilyInjureState': cl_action.GetSpecificPerformArgValue(skill, 50108, 'EasilyInjureState', iDefault = 0) })
                        cl_action.UpdateDictSkillCustomData(skill, 'skill1909HitInfo', cl_action.GetCurVID(skill), cl_action.GetNowFrame(skill) + 25 * cl_action.GetPerformArgValue(skill, 'ToxinCD', iDefault = 1))
                        cl_action.PerformDamage(skill, {
                            'Att': cl_action.GetTargetStateCount(skill, 33062, cl_action.GetCurVID(skill), False, True) * skill.m_Cache['Att'] })
                    elif cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
                        if cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0) > 0:
                            cl_action.VictimAddState(skill, 33076, 50, 0, {
                                'PF50101LV': cl_action.GetSkillCustomData(skill, 'PF50105LV', defaultValue = 0),
                                'Accelerate': cl_action.GetSpecificPerformArgValue(skill, 50105, 'Accelerate', iDefault = 1000) })
                            if cl_action.GetSkillCustomData(skill, 'HasPF50101', defaultValue = 0) > 0:
                                cl_action.VictimAddState(skill, 33078, 500, 0, { })
                            elif cl_action.GetSkillCustomData(skill, 'HasPF50101', defaultValue = 0) > 0:
                                cl_action.VictimAddState(skill, 33078, 500, 0, { })

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
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = True, explosion = False, useclientpos = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] < 2)

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
        cl_action.GetPerformArgValue(skill, 'Duration', iDefault = 200) if cl_action.GetSkillCustomData(skill, 'KeepTime', defaultValue = 0) == 0 else cl_action.GetSkillCustomData(skill, 'KeepTime', defaultValue = 0)])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT,
        SKILLCACHE_POS])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1909
    m_Name = '#NT致命装置-毒气装置释放毒气'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'Radius': 4,
        'EnergyCost': 1000 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000,
        'ToxicStateSID': 33062,
        'MaxCount': 5,
        'AddCount': 1,
        'ToxicTime': 500,
        'NeedAddEasilyInjure': 0,
        'Duration': 200 }
    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def CanUse(self, oWarrior, dInfo):
        dCustom = dInfo['Custom'] if 'Custom' in dInfo else { }
        iPosType = dCustom['PosType'] if 'PosType' in dCustom else 0
        oOwner = oWarrior.GetOwner()
        if not iPosType and oOwner.DeviceEnergy() < self.CostEnergy():
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oOwner = oWarrior.GetOwner()
        iPosType = oSkill.m_Custom['PosType'] if 'PosType' in oSkill.m_Custom else 0
        if not iPosType:
            oOwner.DeviceEnergyModify(-self.CostEnergy())
        super().UsePerform(oWarrior, oSkill)

    
    def CostEnergy(self):
        return self.CalAttr('EnergyCost')



def AddToxicCount(oSkill, *args):
    iTarget = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    iAttack = oSkill.m_Base['AID']
    dArgDataCache = oSkill.m_Cache['ArgData']
    dCustomData = {
        'ToxicTime': dArgDataCache['ToxicTime'],
        'MaxCount': dArgDataCache['MaxCount'],
        'AddCount': dArgDataCache['AddCount'],
        'NeedAddEasilyInjure': dArgDataCache['NeedAddEasilyInjure'] }
    CommonAddToxicCount(oTarget, iAttack, dCustomData)

