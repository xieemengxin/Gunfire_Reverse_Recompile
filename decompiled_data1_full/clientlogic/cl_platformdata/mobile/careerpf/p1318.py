# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1318.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1318.pyc
# Source Generated with Decompyle++
# File: p1318.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastingPosCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon3(RayCastingPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EnergyCost', 3000)
        if cl_action.CheckHasTalent(skill, 3110):
            cl_action.AttackerAddState(skill, 32660, 600, 0, { })
            cl_action.SetAttackerStateCount(skill, 32660, cl_action.GetAttackerAttr(skill, 'EnergyMax'))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetTalentLevel(skill, 3113) == 3:
            if cl_action.CountDistance(skill, cl_action.GetCartoonStart(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 < 1:
                pass
            
        
        skill('Att', {
            cl_action.ToInt: skill(skill.m_Cache['Att'] * 2, 1 * (0 + 1)) })
        if cl_action.CheckHasTalent(skill, 3115):
            if cl_action.GetTalentLevel(skill, 3113) == 3:
                if cl_action.CountDistance(skill, cl_action.GetCartoonStart(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 < 1:
                    pass
                
            
            skill('Att', {
                cl_action.ToInt: skill(skill.m_Cache['Att'] * 2, 1 * (0 + 1) * (cl_action.GetTalentLevel(skill, 3115) * 0.25 + 0.25)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0, 0, 1.5))):
                return None
            cls.EnableShow(skill, 99, 50, 30, 1, [
                6,
                4,
                3], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 0.8)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1318
    m_Name = '炽炎有灵触发'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 35000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 3000
    
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


