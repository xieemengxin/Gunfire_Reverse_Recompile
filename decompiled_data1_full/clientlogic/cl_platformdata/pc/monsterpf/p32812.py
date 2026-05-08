# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p32812.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p32812.pyc
# Source Generated with Decompyle++
# File: p32812.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityCurveCartoon, MonsterLiftLandCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_NORMAL, DAM_TYPE_THUNDER, OBJ_ENEMY, SKILLCACHE_ELEMENTTYPE, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTPOS, SKILLCACHE_PERFORMMODE, WARRIOR_SUMMON
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

class CCartoon11(TimerCartoon):
    m_SID = 11
    
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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS) != []:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).pop()], WARRIOR_SUMMON, {
                1042: 10 }, {
                'Radius': cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100,
                'ScaleX': cl_action.GetPerformArgValue(skill, 'ScaleX', iDefault = 1),
                'ScaleY': cl_action.GetPerformArgValue(skill, 'ScaleY', iDefault = 1),
                'ScaleZ': cl_action.GetPerformArgValue(skill, 'ScaleZ', iDefault = 1) }, (0, 0, 0))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_LSTINT])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

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
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'maxNum') - cl_action.GetSkillVarCache(skill, 'minNum')))

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(EntityCurveCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        cl_action.TargetAddState(skill, cl_action.CrtArgRandomNum(skill, 1172, 1174), 0, 0, { }, cl_action.GetCartoonEntityID(skill, 14))
        cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.GetStartPositionInCrt(skill, 14))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 14), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 14), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 14), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 14), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 14) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgMissingPos(skill, 0), cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, 1042, 180, 11, 30, 0.3, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 13)], forceDel = True, iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
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
        if cl_action.GetCartoonLoopID(skill, 13) <= len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 13)], True, 0, (0, 0, 0), parentName = '')
            cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = False, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_EXCLUDEMONSTERHATE, bResetVID = True))
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(TimerCartoon):
    m_SID = 12
    
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
        if cl_action.GetSkillVarCache(skill, 'minNum') + (cl_action.GetTimerCartoonCurTimes(skill, 12) - 1) + 1 == cl_action.GetSkillVarCache(skill, 'maxNum'):
            cl_action.AttackerRemoveState(skill, 7969, bSameItem = False)
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 1, index = cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'minNum') + (cl_action.GetTimerCartoonCurTimes(skill, 12) - 1)))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'maxNum') - cl_action.GetSkillVarCache(skill, 'minNum')))

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(EntityCurveCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.TargetAddState(skill, cl_action.CrtArgRandomNum(skill, 1172, 1174), 0, 0, { }, cl_action.GetCartoonEntityID(skill, 6))
        cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS).append(cl_action.GetStartPositionInCrt(skill, 6))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetCartoonEntityID(skill, 6), 4)
        if cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1172):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_CORRISION)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1173):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_FIRE)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        elif cl_action.CheckWarriorHasState(skill, cl_action.GetCartoonEntityID(skill, 6), 1174):
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_THUNDER)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
        else:
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)
            cl_action.WarriorUsePerform(skill, cl_action.GetSkillAID(skill), 1629, {
                'vEnd': cl_action.GetEndPositionInCrt(skill, 6) }, False, iTargetVID = 0)
            cl_action.SetPerformElementType(skill, 1629, DAM_TYPE_NORMAL)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_action.CrtArgMissingPos(skill, 0), cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100, 1042, 180, 11, 30, 0.3, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 4)], forceDel = True, iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
        if cl_action.GetCartoonLoopID(skill, 4) <= len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)):
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 4)], True, 0, (0, 0, 0), parentName = '')
            cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 360, bNotContainDying = False, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_EXCLUDEMONSTERHATE, bResetVID = True))
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 2) - 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, cl_action.GetSkillVarCache(skill, 'minNum'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(MonsterLiftLandCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetAttackerCustomIntData(skill, 'FixDropPos', 0)

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
            cls.EnableCtrl(skill, 15, False, 5, True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
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
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 70, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 1, 7969)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 100, 40)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True))
        cl_action.SetSkillVarCache(skill, 'minNum', cl_action.ToInt(skill, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) * 2 + 4) / cl_action.GetPerformArgValue(skill, 'Div', iDefault = 1)))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY, cl_action.GetPerformArgValue(skill, 'Radius', iDefault = 30))
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.CrtArgDestPosDirPoint(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1, 0)), cl_action.CrtArgGetCustomDir(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1, 10)), (0, 0, 0), baseHorizontal = False), 10, cl_action.GetSkillVarCache(skill, 'minNum'), 360 / cl_action.GetSkillVarCache(skill, 'minNum'), False), WARRIOR_SUMMON, {
            1042: 10 }, {
            'Radius': cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100,
            'ScaleX': cl_action.GetPerformArgValue(skill, 'ScaleX', iDefault = 1),
            'ScaleY': cl_action.GetPerformArgValue(skill, 'ScaleY', iDefault = 1),
            'ScaleZ': cl_action.GetPerformArgValue(skill, 'ScaleZ', iDefault = 1) }, (0, 0, 0))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillSummonCreate(skill))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, [])
        cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.ToInt(skill, (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 2 + 4) / cl_action.GetPerformArgValue(skill, 'Div', iDefault = 1)))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE, cl_action.ToInt(skill, (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 4 + 8) / cl_action.GetPerformArgValue(skill, 'Div', iDefault = 1)))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT,
            SKILLCACHE_LSTINT,
            SKILLCACHE_LSTPOS,
            SKILLCACHE_EXTRATRAJECTORY,
            SKILLCACHE_PERFORMMODE,
            SKILLCACHE_ELEMENTTYPE])
        cl_action.SetSkillVarCache(skill, 'minNum', cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE))
        cl_action.SetSkillVarCache(skill, 'maxNum', cl_action.GetSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
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
        cl_action.AttackerAddState(skill, 7964, 3000, 0, { })
        cl_action.AttackerAddState(skill, 7969, 0, 1, { })
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(MonsterLiftLandCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'ifHasState', cl_action.CheckHasState(skill, 7964))
        if cl_action.CheckHasState(skill, 7962):
            if cl_action.CheckHasState(skill, 7964):
                cl_action.AttackerAddState(skill, 7969, 0, 1, { })
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon9.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.AttackerAddState(skill, 7962, 0, 0, { })
            if cl_action.CheckHasState(skill, 7964):
                cl_action.AttackerAddState(skill, 7969, 0, 1, { })
                cartoon = { }
                CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 15, True, 5, True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
        cl_action.SetAttackerCustomPos(skill, 'FixDropPos', cl_action.CrtArgSelfPos(skill))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 33, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ResetMonsterPerformRecord(skill)
    cl_action.SetSkillVarCache(skill, 'jump', cl_action.CrtArgSelfPos(skill))
    cartoon = { }
    CCartoon7.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)
    cl_action.AttackerRemoveState(skill, 7969, bSameItem = False)


def End(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetSkillSummonCreate(skill), 0)
    cl_action.AttackerRemoveState(skill, 7969, bSameItem = False)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ELEMENTTYPE,
        SKILLCACHE_EXTRATRAJECTORY,
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 32812
    m_Name = '【第三幕】精英定点法师怪-炮台形态'
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
        'ColdTime': 200,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

