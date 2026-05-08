# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1420.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1420.pyc
# Source Generated with Decompyle++
# File: p1420.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_PERFORMMODE

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetAttackerStateCount(skill, 32564) < 16:
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        elif cl_action.GetAttackerStateCount(skill, 32564) < 32:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 64)
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        else:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 80)
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
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon), end = cl_action.CrtArgSightCentrePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                2,
                45], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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

    InitSuccess = classmethod(InitSuccess)


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
            cls.EnableShow(skill, 7, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon17(TimerCartoon):
    m_SID = 17
    
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
        CCartoon24.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 7, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(TimerCartoon):
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
        cartoon = { }
        CCartoon17.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon16.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 7, 1)

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
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 7, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)

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
        if cl_action.GetAttackerStateCount(skill, 32564) < 16:
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * 0.4 })
        elif cl_action.GetAttackerStateCount(skill, 32564) < 32:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 64)
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * 0.4 })
        else:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 80)
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] * 0.4 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon), end = cl_action.CrtArgSightCentrePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                2,
                45], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon20(TimerCartoon):
    m_SID = 20
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 9 if (12 if (4 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 6), cl_action.ToInt(skill, (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) - 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon18(TimerCartoon):
    m_SID = 18
    
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
        if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1:
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon20.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 14 if (17 if (20 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 10), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(TimerCartoon):
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
            cls.EnableShow(skill, cl_action.ToInt(skill, 9 if (12 if (4 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 6), cl_action.ToInt(skill, (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) - 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon19(TimerCartoon):
    m_SID = 19
    
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
        if not (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1:
            cartoon = { }
            CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 14 if (17 if (20 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 1 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 10), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon18.Init(skill, cartoon, casting = 1, index = 0)
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
        cartoon = { }
        CCartoon19.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon21(TimerCartoon):
    m_SID = 21
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 30 if (35 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 22), cl_action.ToInt(skill, (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) - 2))

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
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
        if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2:
            cartoon = { }
            CCartoon8.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon21.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 10 if (15 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 5), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon22(TimerCartoon):
    m_SID = 22
    
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
            cls.EnableShow(skill, cl_action.ToInt(skill, 12 if (16 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 8), cl_action.ToInt(skill, (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) * 2 - 3))

    InitSuccess = classmethod(InitSuccess)


class CCartoon23(TimerCartoon):
    m_SID = 23
    
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
        CCartoon22.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 10 if (15 if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 2 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 3 else 5), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        if not (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) < 2:
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 1, index = 0)
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)
        if not (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) < 2:
            cartoon = { }
            CCartoon23.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, ((cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) * -3 + 68) / 2), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon25(TimerCartoon):
    m_SID = 25
    
    def Active(cls, skill):
        if cl_action.CheckHasTalent(skill, 2911):
            if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 0:
                if cl_action.CheckHasState(skill, 32563):
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.CheckHasState(skill, 32563):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.CheckHasState(skill, 32563):
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
        else:
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
            cls.EnableShow(skill, 55(cl_action.ToInt, (skill if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 0 else cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) * -3 + 68), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if cl_action.CheckHasTalent(skill, 2911):
            if (cl_action.GetPerformMode(skill) // 8 if cl_action.GetPerformMode(skill) // 8 < 5 else 4) == 0:
                if cl_action.CheckHasState(skill, 32563):
                    cartoon = { }
                    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
            elif cl_action.CheckHasState(skill, 32563):
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 1, index = 0)
        elif cl_action.CheckHasState(skill, 32563):
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 1, index = 0)
        else:
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
            cls.EnableShow(skill, 55, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasTalent(skill, 2911):
        cartoon = { }
        CCartoon25.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_PERFORMMODE]

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1420
    m_Name = '冲拳'
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
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 70000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 7,
        'BulletVerticalAcc': 0,
        'AddStateTime': 200,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

