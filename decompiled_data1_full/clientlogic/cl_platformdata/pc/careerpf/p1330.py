# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1330.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1330.pyc
# Source Generated with Decompyle++
# File: p1330.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon, WinkPosCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_POS, WARRIOR_NORMAL, WATER_BUBBLE_DAMAGE

class CCartoon24(TimerCartoon):
    m_SID = 24
    
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
            cls.EnableShow(skill, 4, 9)
        else:
            cls.EnableCtrl(skill, 4, 9)

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(TimerCartoon):
    m_SID = 12
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon24.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 44 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 44 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, cl_action.ToInt(skill, 16 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1, cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)))
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * 1 })
        if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 25, 1, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0)):
                return None
            cls.EnableShow(skill, [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0), [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 36 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 36 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(WinkPosCartoon):
    m_SID = 14
    
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
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                            pass
                        
                    
                
            
            skill(4, 4, 0, [
                3,
                1,
                90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] > 0 and cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        cl_action.CrtArgDestPosDirPlane(skill(cl_action.CrtArgSelfPos(skill), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 1, 1, 0), 4, 4, 0, [
            3,
            1,
            90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon18(TimerCartoon):
    m_SID = 18
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon14.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon25(TimerCartoon):
    m_SID = 25
    
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
            cls.EnableShow(skill, 4, 9)
        else:
            cls.EnableCtrl(skill, 4, 9)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon25.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, cl_action.ToInt(skill, 16 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1, cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)))
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * 1 })
        if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 25, 1, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0)):
                return None
            cls.EnableShow(skill, [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0), [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 24 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 24 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(WinkPosCartoon):
    m_SID = 15
    
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
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                            pass
                        
                    
                
            
            skill(4, 4, 0, [
                3,
                1,
                90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] > 0 and cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        cl_action.CrtArgDestPosDirPlane(skill(cl_action.CrtArgSelfPos(skill), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 1, 1, 0), 4, 4, 0, [
            3,
            1,
            90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon19(TimerCartoon):
    m_SID = 19
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon26(TimerCartoon):
    m_SID = 26
    
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
            cls.EnableShow(skill, 4, 6)
        else:
            cls.EnableCtrl(skill, 4, 6)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon26.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 68 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 68 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, cl_action.ToInt(skill, 20 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1, cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)))
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * cl_action.GetPerformArgValue(skill, 'L3Mul', iDefault = 3) })
        if cl_action.GetSkillVarCache(skill, 'OnlyHit') == 0:
            cl_action.ChangeAttackerEnergy(skill, cl_action.GetPerformArgValue(skill, 'EnergyRecoverL3', iDefault = 1000) * (cl_action.GetPerformArgValue(skill, 'RecoverMul', iDefault = 100) + cl_action.GetSkillCustomData(skill, 'TempAddRecoveryMul', defaultValue = 0)) / 100, iReason = 0)
            cl_action.SetSkillVarCache(skill, 'OnlyHit', 1)
            if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
                cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 50, 2, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)
            elif cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
                cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 50, 2, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0)):
                return None
            cls.EnableShow(skill, [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0), [
                5,
                5,
                140], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(WinkPosCartoon):
    m_SID = 16
    
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
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                            pass
                        
                    
                
            
            skill(4, 4, 0, [
                3,
                1,
                90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] > 0 and cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 1:
                if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 2:
                    if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 3:
                        pass
                    
                
            
        
        cl_action.CrtArgDestPosDirPlane(skill(cl_action.CrtArgSelfPos(skill), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 1, 1, 0), 4, 4, 0, [
            3,
            1,
            90], [], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon20(TimerCartoon):
    m_SID = 20
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'OnlyHit', 0)
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon16.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon23(TimerCartoon):
    m_SID = 23
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon20.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 28, 1)
        else:
            cls.EnableCtrl(skill, 28, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon21(TimerCartoon):
    m_SID = 21
    
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
            cls.EnableShow(skill, 20, 0)
        else:
            cls.EnableCtrl(skill, 20, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SkillHaltSelf(skill)

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
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            WATER_BUBBLE_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1330, 'Att') * cl_action.GetPerformArgValue(skill, 'L4Mul', iDefault = 1) })
        if not cl_action.CheckHasSkillCollect(skill, 'L4NotAddEnergy'):
            if cl_action.GetSkillVarCache(skill, 'OnlyHit') == 0:
                cl_action.ChangeAttackerEnergy(skill, cl_action.GetPerformArgValue(skill, 'EnergyRecoverL4', iDefault = 0) * (cl_action.GetPerformArgValue(skill, 'RecoverMul', iDefault = 100) + cl_action.GetSkillCustomData(skill, 'TempAddRecoveryMul', defaultValue = 0)) / 100, iReason = 0)
                cl_action.SetSkillVarCache(skill, 'OnlyHit', 1)
                if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
                    cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 10, 0.5, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)
                elif cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
                    cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 10, 0.5, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.ToInt(skill, ((cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[0] + 100) / 100) * 10),
                9,
                cl_action.ToInt(skill, ((cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[1] + 100) / 100) * 100)], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetAttackerFacing(skill), 5, 0), [
                cl_action.ToInt(skill, ((cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[0] + 100) / 100) * 10),
                9,
                cl_action.ToInt(skill, ((cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL)[1] + 100) / 100) * 100)], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon17(TimerCartoon):
    m_SID = 17
    
    def Active(cls, skill):
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
        cartoon = { }
        CCartoon21.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
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
        cl_action.SetSkillVarCache(skill, 'OnlyHit', 0)
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetSkillVarCache(skill, 'WaitTime'), cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] / cl_action.GetSkillVarCache(skill, 'WaitTime')))
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'WaitTime'), cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] / cl_action.GetSkillVarCache(skill, 'WaitTime')))

    InitSuccess = classmethod(InitSuccess)


class CCartoon22(TimerCartoon):
    m_SID = 22
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon17.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1500)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 40 / (skill.m_Cache['ExplodeDelay'] + 100) / 100), 1500)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon22.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'WaitTime', cl_action.ToInt(skill, 24 / (skill.m_Cache['ExplodeDelay'] + 100) / 100))
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
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
            cartoon = { }
            CCartoon18.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon19.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 2:
            cartoon = { }
            CCartoon23.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
            cartoon = { }
            CCartoon13.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33604)
    if cl_action.CheckClientCtrl(skill):
        cl_action.SetSkillVarCache(skill, 'ChainTimes', 4 if skill.m_Cache['AttDistance'] > 0 else 3)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, 'SkillCount', iDefault = 0))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
            cl_action.GetSkillVID(skill)])
        cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgTargetPos(skill, notContainDying = False))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINTSPECIAL, [
            skill.m_Cache['DamInterval'],
            skill.m_Cache['Pierce']])
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
            cl_action.SetSkillCustomDataInt(skill, 'AIDamFactor', 3000)
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
                cartoon = { }
                CCartoon18.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
                cartoon = { }
                CCartoon19.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 2:
                cartoon = { }
                CCartoon23.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
                cartoon = { }
                CCartoon13.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SetSkillCustomDataInt(skill, 'AIDamFactor', 1000)
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
                cartoon = { }
                CCartoon18.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
                cartoon = { }
                CCartoon19.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 2:
                cartoon = { }
                CCartoon23.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
                cartoon = { }
                CCartoon13.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPFEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1330
    m_Name = '#NT#基础式'
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
        'ColdTime': 4,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1098
    m_CheckForbid = 1013
    m_BaseArgData = {
        'EnergyCost3': -1000,
        'EnergyCost4': -1000,
        'EnergyRecoverL3': 1000,
        'L3Mul': 3,
        'RecoverMul': 100 }
    m_AIPerformDam = 1200

