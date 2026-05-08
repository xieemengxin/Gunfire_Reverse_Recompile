# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8007.pyc
# Source Generated with Decompyle++
# File: p8007.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_POS

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.CheckSightCentrePosDis(skill, cl_action.GetStartPositionInCrt(skill, 1), 30)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.UseExtraThrowPerform(skill, {
            'vEnd': cl_action.GetStartPositionInCrt(skill, 1),
            'DirectPos': 1 }, 30, 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 1), 20, 3, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })
        if not cl_action.CheckHasState(skill, 32661):
            cl_action.ChangeAttackerEnergy(skill, 200, iReason = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1 else cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1423, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 46, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 80, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'DirectPos', defaultValue = 0))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT,
        SKILLCACHE_POS])
    if cl_action.GetSkillCustomData(skill, 'ThrowMsg', defaultValue = 0) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 8007
    m_Name = '被动火陨'
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
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 60,
        'DebuffProb': 5000,
        'ExplodeDelay': 0,
        'Radius': 20,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_PassRule = {
        1062: 1 }
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        if 'StartTimes' in oSkill.m_Custom:
            oSkill.m_Collect['StartTimes'] = oSkill.m_Custom['StartTimes'] + 1
        if 'Att' in oSkill.m_Custom:
            oSkill.m_Cache['Att'] = oSkill.m_Custom['Att']
        super().UsePerform(oWarrior, oSkill)


