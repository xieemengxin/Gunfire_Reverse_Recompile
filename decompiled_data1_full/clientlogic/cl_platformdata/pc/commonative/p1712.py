# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1712.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1712.pyc
# Source Generated with Decompyle++
# File: p1712.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'Random', cl_action.CrtArgRandomNum(skill, 1, 100) < 25)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillCache(skill, 'DebuffProb', 0)
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * (2 if cl_action.GetSkillVarCache(skill, 'EnergyCost') >= 30 else 1) * 1 * (2 if cl_action.GetSkillVarCache(skill, 'EnergyCost') >= 60 and cl_action.GetTalentLevel(skill, 3115) >= 2 else 1)) })
        if cl_action.CheckHasTalent(skill, 3115):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * (2 if cl_action.GetSkillVarCache(skill, 'EnergyCost') >= 30 else 1) * 1 * (2 if cl_action.GetSkillVarCache(skill, 'EnergyCost') >= 60 and cl_action.GetTalentLevel(skill, 3115) >= 2 else 1) * (cl_action.GetTalentLevel(skill, 3115) * 0.25 + 0.25)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), (0, 0, 0), [
                20 if cl_action.CheckCurLevel(skill, 1101007) else 10], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

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
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_pxlayer import PXMASK_BOX
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1712
    m_Name = '心灵之火'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_IgnoreLayer = (PXMASK_BOX,)
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 0 }
    
    def UsePerform(self, oWarrior, oSkill):
        pfobj = oWarrior.GetCareerPerform()
        if not pfobj:
            return None
        oSkill.m_Cache['Att'] = pfobj.CalAttr('Att')
        iEnergyCost = oWarrior.QueryAttr('EnergyMax') // 2
        cl_action.SetSkillServerCache(oSkill, 'EnergyCost', iEnergyCost)
        cl_action.SetSkillVarCache(oSkill, 'EnergyCost', iEnergyCost)
        super().UsePerform(oWarrior, oSkill)


