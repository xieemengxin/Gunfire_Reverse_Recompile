# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1313.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1313.pyc
# Source Generated with Decompyle++
# File: p1313.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetPosInCustomData(skill) if cl_action.IsHeroCtrl(skill) else cl_math.Vec3Add(cl_action.GetPosInCustomData(skill), (0, 0, -3))):
                return None
            cls.EnableShow(skill, 1, 50, 100, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 5 if skill.m_Cache['BulletSpeed'] == 1 else 0, angle = 90 if cl_action.IsHeroCtrl(skill) else 180, lockDis = 0, IgnoreDefalutDis = cl_action.CrtArgSightDefaultDis(skill, 10), iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)
        elif cl_action.IsHeroCtrl(skill):
            pass
        
        skill(cl_action.GetPosInCustomData(skill), cl_math.Vec3Add(cl_action.GetPosInCustomData(skill), (0, 0, -3)), cl_action.VectorShiftForAttDir(skill, cl_action.GetSceneCenterPosition(skill, cartoon), (cl_action.RandomFloat(-0.3, 0.3), 0, 0)), 1, 50, 100, showstart = (0, 0, 0), targettype = OBJ_ENEMY, targetID = 0, liveTime = 0, lineDistance = 5 if skill.m_Cache['BulletSpeed'] == 1 else 0, angle = 90 if cl_action.IsHeroCtrl(skill) else 180, lockWeakness = False, lockAngle = 0, canDesAngle = 0, lockDis = 0, IgnoreDefalutDis = cl_action.CrtArgSightDefaultDis(skill, 10), IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0, lockSumm = False, lockCanDestroy = False, lockHideDoor = False, isBlocked = False, isMonsterFirst = False, lockExplode = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyPFTransDamFactor(skill)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1313
    m_Name = '#剑雨飞弹'
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
        'ColdTime': 10,
        'AttDistance': 100,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 20000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 1000,
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
    m_AIPerformDam = 160
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_CanUseCount = 0

    
    def GetCanUseCount(self):
        return self.m_CanUseCount

    
    def AddCanUseCount(self, iAdd = 1):
        self.m_CanUseCount += iAdd

    
    def CanUse(self, oWarrior, dInfo):
        if self.m_CanUseCount < 1:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        self.m_CanUseCount -= 1
        (iEachCount, iExtCount) = oWarrior.Query('1312ExtSwordCount', (0, 0))
        itimes = iEachCount
        if iExtCount:
            iExtCount -= 1
            oWarrior.Set('1312ExtSwordCount', (iEachCount, iExtCount))
            itimes += 1
        oSkill.m_Collect['1313-Curtimes'] = itimes
        super().UsePerform(oWarrior, oSkill)


