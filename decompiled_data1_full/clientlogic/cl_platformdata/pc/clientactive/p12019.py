# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12019.pyc
# Source Generated with Decompyle++
# File: p12019.pyc (Python 3.6)

from cl_object.logging import SkillLog
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
POS_CTRL_INDEX = 2
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_LSTINT, SKILLCACHE_POS

class CCartoon6(TraceCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerAttr(skill, 'HPMax') + cl_action.GetAttackerAttr(skill, 'ArmorMax') + cl_action.GetAttackerAttr(skill, 'ShieldMax') + (cl_action.GetAttackerAttr(skill, 'HPMax') + cl_action.GetAttackerAttr(skill, 'ArmorMax') + cl_action.GetAttackerAttr(skill, 'ShieldMax')) * cl_action.GetPerformArgValue(skill, 'AttRatio', iDefault = 0) / 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, 0.8, 0))):
                return None
            cls.EnableShow(skill, 1, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0], 30, showstart = cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), (0, 0.8, 0)), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0.1, angle = 8, lockDis = 0, IgnoreDefalutDis = 100, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    cartoon = { }
    CCartoon6.Init(skill, cartoon, casting = 0, index = 0)


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

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 12019
    m_Name = '荆棘外壳针刺发射'
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
        'UseInterval': 20 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 3000 }
    m_SyncCanUseCount = True
    m_CanUseCountMax = 10
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_TemporaryCount = 0
        self.m_IsServerCtrl = 0

    
    def CanUse(self, oWarrior, dInfo):
        oCtrlCache = dInfo['CtrlCache']
        sAttr = cl_action.GetSkillCacheAttrName(SKILLCACHE_LSTINT)
        lstIntParaList = oCtrlCache.GetSkillCache(sAttr)
        if (self.CheckIntParaList(lstIntParaList, POS_CTRL_INDEX) or lstIntParaList[POS_CTRL_INDEX]) and self.m_TemporaryCount > 0:
            self.m_IsServerCtrl = 1
        else:
            SkillLog.Error('%d %d pf12019 cache %s' % (self.m_Game.m_ID, oWarrior.m_PlayerID, lstIntParaList))
        bCanUse = super().CanUse(oWarrior, dInfo)
        if not bCanUse and self.m_IsServerCtrl:
            self.m_IsServerCtrl = 0
            self.AddTemporaryCount(-1)
        return bCanUse

    
    def InUseInterval(self):
        if self.m_IsServerCtrl:
            return 0
        return super().InUseInterval()

    
    def GetUseInterval(self, oWarrior):
        if self.m_IsServerCtrl:
            return 0
        return super().GetUseInterval(oWarrior)

    
    def UsePerform(self, oWarrior, oSkill):
        super().UsePerform(oWarrior, oSkill, not (self.m_IsServerCtrl))
        if self.m_IsServerCtrl:
            self.m_IsServerCtrl = 0
            self.m_TemporaryCount -= 1
            self.AddCanUseCountMax(-1)

    
    def CheckIntParaList(self, lstIntParaList, iIndex):
        if not lstIntParaList:
            return 0
        if len(lstIntParaList) < iIndex + 1:
            return 0
        return 1

    
    def AddTemporaryCount(self, iAdd = 1):
        self.m_TemporaryCount += iAdd
        self.AddCanUseCountMax(iAdd)
        self.AddCanUseCount(iAdd, False)


