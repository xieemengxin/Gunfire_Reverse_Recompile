# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1926.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1926.pyc
# Source Generated with Decompyle++
# File: p1926.pyc (Python 3.6)

from cl_only import ShufferList, ChooseKey
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTPOS

class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
            cls.EnableCtrl(skill, 20, 4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': 7000 })
        cl_action.VictimAddState(skill, 1011, 300, 0, {
            'MoveSpeedMul': -4000 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 2)], cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4))), (0, 25, 0)), cl_math.Vec3Add(cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 2)], cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4))), (0, 25, 0)), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[cl_action.GetCartoonLoopID(skill, 2)], cl_math.Vec3MulV(cl_action.GetSkillVarCache(skill, 'Dir'), (cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4, cl_action.GetTimerCartoonCurTimes(skill, 2) * 4))), 1, 200, 25, targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 4)

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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = cl_action.GetTimerCartoonCurTimes(skill, 3) + -1)
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = cl_action.GetTimerCartoonCurTimes(skill, 3) + -1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTPOS)
    cl_action.CustomPerformAction(skill, 1926, 'SetThunderPos', { })
    cl_action.SetSkillVarCache(skill, 'Dir', cl_action.CrtArgSelfFace(skill))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1926
    m_Name = '#NT# 雷雨天气预警落雷'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0


def SetThunderPos(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        cl_action.SetSkillCacheData(oSkill, SKILLCACHE_LSTPOS, [])
        return None
    dThunderPosInfo = oAttack.Query('ThunderPosInfo', { })
    if not dThunderPosInfo:
        lstThunderCernterPos = oAttack.Query('ThunderCernterPos', [])
        if 'TrapPerformInfo' in oSkill.m_Cache:
            dPerformInfo = oSkill.m_Cache['TrapPerformInfo']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in dPerformInfo and dPerformInfo[iPerform]['CustomParam']:
                dPerform = dPerformInfo[iPerform]
                lstParam = dPerform['CustomParam']
                iCurTimes = dPerform['CurTimes']
                dParam = lstParam[iCurTimes % len(lstParam)]
                if 'NumWeight' in dParam:
                    dNumWeight = { }
                    for sKey, iValues in dParam['NumWeight'].items():
                        dNumWeight[int(sKey)] = iValues
                    
                    if 'Random' in dParam and dParam['Random']:
                        dThunderPosInfo['Random'] = 1
                        dThunderPosInfo['NumWeight'] = dNumWeight
                    else:
                        iNum = ChooseKey(oSkill.m_Game, dNumWeight)
                        lstThunderCernterPos = ShufferList(oSkill.m_Game, lstThunderCernterPos, iNum)
        dThunderPosInfo['ThunderPos'] = lstThunderCernterPos
        oAttack.Set('ThunderPosInfo', dThunderPosInfo)
    if 'Random' in dThunderPosInfo:
        iNum = ChooseKey(oSkill.m_Game, dThunderPosInfo['NumWeight'])
        lstTureThunderPos = ShufferList(oSkill.m_Game, dThunderPosInfo['ThunderPos'], iNum)
    else:
        lstTureThunderPos = dThunderPosInfo['ThunderPos']
    cl_action.SetSkillCacheData(oSkill, SKILLCACHE_LSTPOS, lstTureThunderPos)

