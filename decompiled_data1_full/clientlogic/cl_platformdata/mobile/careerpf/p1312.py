# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1312.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1312.pyc
# Source Generated with Decompyle++
# File: p1312.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_commondefines import SKILLCACHE_PARENTACTNUM
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_INT

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 24, 1)

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
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetTimerCartoonCurTimes(skill, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.CalWaitTimeByTotaltime(cl_action.GetSkillVarCache(skill, 'SwordCount'), 6, 50, 260, 6), cl_action.GetSkillVarCache(skill, 'SwordCount'))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'SwordCount', cl_action.FloatToIntFloor(skill, skill.m_Cache['Radius'] * skill.m_Cache['BulletSpeed'] * 0.7) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) <= 100 or 15 <= skill.m_Cache['Radius'] * skill.m_Cache['BulletSpeed'] or (30) < cl_action.FloatToIntFloor(skill, skill.m_Cache['Radius'] * skill.m_Cache['BulletSpeed']) else cl_action.FloatToIntFloor(skill, skill.m_Cache['Radius'] * skill.m_Cache['BulletSpeed']))
    cl_action.SetSkillServerCache(skill, 'swordnum', cl_action.GetSkillVarCache(skill, 'SwordCount'))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1312
    m_Name = '出鞘'
    m_ExtPerform = (1313, 8503, 4301)
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
        'ColdTime': 520,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 8,
        'AddStateTime': 200,
        'Att': 20000,
        'CrazyEff': 10000,
        'BulletSpeed': 3,
        'DebuffProb': 0,
        'ExplodeDelay': 280,
        'Radius': 0,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1061
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 160
    
    def UsePerform(self, oWarrior, oSkill):
        super().UsePerform(oWarrior, oSkill)
        iPerentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
        oSkill.m_Collect['PerentActNum'] = iPerentActNum
        iSwordCount = int(oSkill.m_Cache['Radius'] * oSkill.m_Cache['BulletSpeed'])
        oSkill.m_Collect['TotalSwordNum'] = iSwordCount
        iCurSwordCount = oSkill.m_VarCache['SwordCount']
        if iCurSwordCount > iSwordCount:
            iCurSwordCount = iSwordCount
        if iCurSwordCount < 1:
            iCurSwordCount = 1
        oPerform = oWarrior.GetPerform(1313)
        iTotalSwordCount = iSwordCount
        iCurTotalSwordCount = iCurSwordCount
        if oPerform:
            iCanUseCount = oPerform.GetCanUseCount()
            if iCanUseCount > 0:
                (iEachCount, iExtCount) = oWarrior.Query('1312ExtSwordCount', (0, 0))
                iTotalSwordCount += iCanUseCount * (iEachCount + 1) + iExtCount
                iCurTotalSwordCount += iCanUseCount
        iEachCount = int(iTotalSwordCount // iCurTotalSwordCount) - 1
        iExtCount = int(iTotalSwordCount % iCurTotalSwordCount)
        oWarrior.Set('1312ExtSwordCount', (iEachCount, iExtCount))
        if oPerform:
            oPerform.AddCanUseCount(iCurSwordCount)


