# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39246.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39246.pyc
# Source Generated with Decompyle++
# File: p39246.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, SKILLCACHE_POS

class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 15)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 0, 7992)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7989, bSameItem = False)
        cl_action.AttackerRemoveState(skill, 7994, bSameItem = False)
        cl_action.AttackerRemoveState(skill, 7993, bSameItem = False)
        cl_action.SkillHaltOther(skill, 39249)
        cl_action.StartBackSwing(skill, 165)

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
            cls.EnableCtrl(skill, 4, 7500)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 7989, 0, 1, { })
        if cl_action.GetAttackSID(skill) == 39251:
            cl_action.AttackerAddState(skill, 8078, 0, 1, { })
            cl_action.AttackerAddState(skill, 7992, 0, 1, { })
            cl_action.SetSkillVarCache(skill, 'live', cl_action.GetLiveHeroID(skill, True, fMaxDis = 0))
            if cl_action.GetMonsterPerformRecord(skill, 39246) == 2:
                if len(cl_action.GetSkillVarCache(skill, 'live')) > 0:
                    if len(cl_action.GetSkillVarCache(skill, 'live')) > 1:
                        if len(cl_action.GetSkillVarCache(skill, 'live')) > 2:
                            if len(cl_action.GetSkillVarCache(skill, 'live')) > 3:
                                cl_action.AttackerUsePerform(skill, 39249, {
                                    'time': 50,
                                    'number': 4,
                                    'change': 0 }, 0, 0)
                                cartoon = { }
                                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                            else:
                                cl_action.AttackerUsePerform(skill, 39249, {
                                    'time': 50,
                                    'number': 3,
                                    'change': 0 }, 0, 0)
                                cartoon = { }
                                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                        else:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 50,
                                'number': 2,
                                'change': 0 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                    else:
                        cl_action.AttackerUsePerform(skill, 39249, {
                            'time': 50,
                            'number': 1,
                            'change': 0 }, 0, 0)
                        cartoon = { }
                        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
            elif len(cl_action.GetSkillVarCache(skill, 'live')) > 0:
                if len(cl_action.GetSkillVarCache(skill, 'live')) > 1:
                    if len(cl_action.GetSkillVarCache(skill, 'live')) > 2:
                        if len(cl_action.GetSkillVarCache(skill, 'live')) > 3:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 70,
                                'number': 2,
                                'change': 1 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                        else:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 80,
                                'number': 2,
                                'change': 1 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                    else:
                        cl_action.AttackerUsePerform(skill, 39249, {
                            'time': 80,
                            'number': 1,
                            'change': 1 }, 0, 0)
                        cartoon = { }
                        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cl_action.AttackerUsePerform(skill, 39249, {
                        'time': 100,
                        'number': 1,
                        'change': 1 }, 0, 0)
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.AttackerAddState(skill, 7992, 0, 1, { })
            cl_action.SetSkillVarCache(skill, 'live', cl_action.GetLiveHeroID(skill, True, fMaxDis = 0))
            if cl_action.GetMonsterPerformRecord(skill, 39246) == 2:
                if len(cl_action.GetSkillVarCache(skill, 'live')) > 0:
                    if len(cl_action.GetSkillVarCache(skill, 'live')) > 1:
                        if len(cl_action.GetSkillVarCache(skill, 'live')) > 2:
                            if len(cl_action.GetSkillVarCache(skill, 'live')) > 3:
                                cl_action.AttackerUsePerform(skill, 39249, {
                                    'time': 50,
                                    'number': 4,
                                    'change': 0 }, 0, 0)
                                cartoon = { }
                                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                            else:
                                cl_action.AttackerUsePerform(skill, 39249, {
                                    'time': 50,
                                    'number': 3,
                                    'change': 0 }, 0, 0)
                                cartoon = { }
                                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                        else:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 50,
                                'number': 2,
                                'change': 0 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                    else:
                        cl_action.AttackerUsePerform(skill, 39249, {
                            'time': 50,
                            'number': 1,
                            'change': 0 }, 0, 0)
                        cartoon = { }
                        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
            elif len(cl_action.GetSkillVarCache(skill, 'live')) > 0:
                if len(cl_action.GetSkillVarCache(skill, 'live')) > 1:
                    if len(cl_action.GetSkillVarCache(skill, 'live')) > 2:
                        if len(cl_action.GetSkillVarCache(skill, 'live')) > 3:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 70,
                                'number': 2,
                                'change': 1 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                        else:
                            cl_action.AttackerUsePerform(skill, 39249, {
                                'time': 80,
                                'number': 2,
                                'change': 1 }, 0, 0)
                            cartoon = { }
                            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                    else:
                        cl_action.AttackerUsePerform(skill, 39249, {
                            'time': 80,
                            'number': 1,
                            'change': 1 }, 0, 0)
                        cartoon = { }
                        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cl_action.AttackerUsePerform(skill, 39249, {
                        'time': 100,
                        'number': 1,
                        'change': 1 }, 0, 0)
                    cartoon = { }
                    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 60, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 6, 1)

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
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
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
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 15)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, (1610.38, 500.31, 1263.58), 360)

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
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 35) * 100 if (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 35) * 100 >= 4 else 4), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        cl_action.MonsterTeleportToPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.AttackerUsePerform(skill, 39250, {
            'vPos': cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_math.Vec3Minus(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetSkillVarCache(skill, 'start')), (cl_action.GetTimerCartoonCurTimes(skill, 4) - 1) * 2, 0),
            'end': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) }, 10, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 35) * 100 / (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1)) if cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 35) * 100 / (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1)) > 4 else 4, cl_action.ToInt(skill, cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_math.Vec3Minus(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)), 99, 0), 180)
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
        if cl_action.GetAttackSID(skill) == 39251:
            if cl_action.GetMonsterPerformRecord(skill, 39246) == 2:
                if len(cl_action.GetLiveHeroID(skill, True, fMaxDis = 0)) > 2:
                    cl_action.CreateMonsterAtPos(skill, 39261, cl_action.CrtArgSelfPos(skill), 0, False, 'demonking')
                    if cl_action.CheckHasState(skill, 7998):
                        cartoon = { }
                        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
                    else:
                        cartoon = { }
                        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
                elif cl_action.CheckHasState(skill, 7998):
                    cartoon = { }
                    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
            elif len(cl_action.GetLiveHeroID(skill, True, fMaxDis = 0)) > 1:
                cl_action.CreateMonsterAtPos(skill, 39261, cl_action.CrtArgSelfPos(skill), 0, False, 'demonking')
                if cl_action.CheckHasState(skill, 7998):
                    cartoon = { }
                    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.CheckHasState(skill, 7998):
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.CheckHasState(skill, 7998):
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 61, 1)

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
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_POS])
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'start', cl_action.CrtArgSelfPos(skill))
    cl_action.SetSkillVarCache(skill, 'end', cl_action.DemonKingCondensedSiteSelection(skill, 1169, [
        (1591.92, 500.16, 1279.66),
        (1637.55, 500.03, 1271.01)]))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'end'))
    cartoon = { }
    CCartoon8.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39246
    m_Name = '妖王-妖气凝聚'
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
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']

