# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1325.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1325.pyc
# Source Generated with Decompyle++
# File: p1325.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
from cl_only import Functor, GAME_FRAME
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTPOS

class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 33044, bSameItem = False)

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
            cls.EnableShow(skill, 15, 1)
        else:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 25, 1)
        else:
            cls.EnableCtrl(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetAttackerStateCount(skill, 33068, 0)

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
            cls.EnableShow(skill, 60, 1)
        else:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 1, 33044)

    Active = classmethod(Active)
    
    def End(cls, skill):
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
            cls.EnableShow(skill, 200, 45)
        else:
            cls.EnableCtrl(skill, 200, 45)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.PerformCreateInkBead(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS), 40)
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSpherePointByRay(skill, 0.01, 1, 20), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSpherePointByRay(skill, 0.01, 1, 20), (0, 0, 0), [
                6], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetAttackerStateCount(skill, 33068, 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 57, 1)
        else:
            cls.EnableCtrl(skill, 57, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.AttackerAddState(skill, 33058, 0, 1, {
        'TransDamFactor': cl_action.GetTransDamFactor(skill),
        'TransDam': 1 })
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerRemoveState(skill, 33044, bSameItem = False)
    cl_action.SetAttackerStateCount(skill, 33068, 0)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1325
    m_Name = '灵墨化形'
    m_ExtPerform = (1326, 1918, 1920, 1921)
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
        'ColdTime': 1500,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 1600,
        'Att': 60000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3300,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_BaseArgData = {
        'DamReduceRatio': 6000,
        'ShieldRecoverAdd': 1000,
        'AddStateThresholdValue': 15 }
    m_AIPerformDam = 600
    
    def UsePerform(self, oWarrior, oSkill):
        cl_action.AttackerAddState(oSkill, 33044, oSkill.m_Cache.get('AddStateTime', 1600), 0, {
            'TransDamFactor': cl_action.GetTransDamFactor(oSkill) })
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            oPerform = oWarrior.GetPerform(SUB_PERFORM)
            if not oPerform:
                return None
            oPerform.AttrChange('PFBulletUse', 'ai', -10000, 0)
            iTotal = 5
            oSkill.AddEndFunc(ClearFunc)
            oWarrior.m_Agent.Call_Out(Functor(DelayUseSubPF, oSkill, 0, iTotal), GAME_FRAME, 'AICareerPF')


SUB_PERFORM = 1326

def DelayUseSubPF(oSkill, iCur, iTotal):
    oWarrior = oSkill.GetAttack()
    if not oWarrior or not (oWarrior.m_Agent):
        return None
    oPerform = oWarrior.GetPerform(SUB_PERFORM)
    if not oPerform:
        return None
    if not oWarrior.m_Game.m_SkillMgr.GetSkillBySource(SUB_PERFORM, oWarrior.m_ID, iItem = 0):
        oTarget = oWarrior.m_Agent.GetLockTarget()
        if oTarget and cl_math.CheckDistance(oTarget.GetPos(), oWarrior.GetPos(), oPerform.CalAttr('Radius') + oTarget.m_ModelRadius):
            iCur += 1
            cl_war.UsePerform(oWarrior, oPerform, { })
    if iCur <= iTotal:
        oWarrior.m_Agent.Call_Out(Functor(DelayUseSubPF, oSkill, iCur, iTotal), GAME_FRAME, 'AICareerPF')
    else:
        oWarrior.m_Agent.Call_Out(oSkill.Halt, GAME_FRAME, 'AICareerPF')


def ClearFunc(oSkill):
    oWarrior = oSkill.GetAttack()
    if not oWarrior:
        return None
    oPerform = oWarrior.GetPerform(SUB_PERFORM)
    if not oPerform:
        return None
    oPerform.AttrClear('PFBulletUse', 'ai')
    if oWarrior.m_Agent:
        oWarrior.m_Agent.Remove_Call_Out('AICareerPF')

