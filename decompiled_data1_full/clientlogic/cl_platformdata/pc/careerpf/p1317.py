# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1317.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1317.pyc
# Source Generated with Decompyle++
# File: p1317.pyc (Python 3.6)

from cl_only import ChooseKey
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_CYLINDER, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE, SKILLCACHE_POS, WARRIOR_MONSTER

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1317, 'Att') * 3) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), end = cl_math.Vec3Add(cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), cl_math.Vec3Add(cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), (0, 10, 0)), [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(DirectPosCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1317, 'Att') * 0.3125) })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 5:
            cl_action.AddSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCurVID(skill)), 1)
            if cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCurVID(skill))) < 100 and cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCurVID(skill))) % 3 == 0:
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.GetSkillEffectByKey(skill, 1)), end = cl_math.Vec3Add(cl_action.CrtArgGetTransPos(skill, cl_action.GetSkillEffectByKey(skill, 1)), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                7,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgGetTransPos(skill, cl_action.GetSkillEffectByKey(skill, 1)), cl_math.Vec3Add(cl_action.CrtArgGetTransPos(skill, cl_action.GetSkillEffectByKey(skill, 1)), (0, 10, 0)), [
                7,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 20)
        else:
            cls.EnableCtrl(skill, 25, 20)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 4:
            cl_action.AddSceneEventForState(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 500, 1, {
                'Radius': 7 }, 32635, 500, 1, iFightType = WARRIOR_MONSTER, iLeaveSetTime = -1)
            cartoon = { }
            CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1317, 'Att') * 2) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), end = cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                7,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0)), [
                7,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 35, 1)
        else:
            cls.EnableCtrl(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 3:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1317, 'Att') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), end = cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0)), [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)
        else:
            cls.EnableCtrl(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.CustomPerformAction(skill, 1317, 'SetTargetPos2VarCache', [])

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) >= 2:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1317, 'Att') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), end = cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0))):
                return None
            cls.EnableShow(skill, [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 10, 0)), [
                3.5,
                10], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1] > 0:
        cl_action.AttackerAddState(skill, 32900, 0, 1, {
            'DamFactor': cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1] })
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1317
    m_Name = '星落'
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
        'ColdTime': 1500,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 80000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 3.5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_AIPerformDam = 3000
    
    def UsePerform(self, oWarrior, oSkill):
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            oWarMgr = oWarrior.m_Game.m_WarMgr
            if oWarMgr.IsEndless():
                iLayer = 4
            else:
                oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
                iLayer = oLevelCtrl.m_LayerNum
            dRatio = g_PerfromModeRatio[iLayer]
            iMode = ChooseKey(oWarMgr.m_Game, dRatio)
            iEmptyGroove = 0
            iDamFactor = 0
            oSkill.m_Custom['AIDamFactor'] = g_AIDamFactor[iMode]
            iVictim = oSkill.m_Base['VID']
            oVictim = oWarrior.m_Game.GetObject(iVictim)
            vPos = oVictim.GetPos() if oVictim else oSkill.m_Base['vEnd']
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_LSTINT, [
                iEmptyGroove,
                iDamFactor])
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_POS, vPos)
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_PERFORMMODE, iMode)
        oWarrior.m_GamblerCon.ClearAllQuality(iAssignComb = 0, iSkillClearFlag = 1)
        super().UsePerform(oWarrior, oSkill)


g_PerfromModeRatio = {
    1: {
        2: 45,
        3: 25 },
    2: {
        2: 35,
        3: 55,
        4: 20 },
    3: {
        2: 25,
        3: 40,
        4: 50 },
    4: {
        2: 15,
        3: 25,
        4: 90 } }
g_AIDamFactor = {
    2: 5000,
    3: 3300,
    4: 430 }

def SetTargetPos2VarCache(oSkill, *args):
    dCartoon = oSkill.GetCurCartoon()
    oSkill.m_VarCache['targetPos'] = dCartoon['Start']

