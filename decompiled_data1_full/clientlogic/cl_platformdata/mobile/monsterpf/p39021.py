# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39021.pyc
# Source Generated with Decompyle++
# File: p39021.pyc (Python 3.6)

from cl_only import SendAlert
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import SectorRotateCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_USE_HP, OBJ_ALL, OBJ_ENEMY, WARRIOR_BUILD

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 280, 0)

    InitSuccess = classmethod(InitSuccess)


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
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 0)

    InitSuccess = classmethod(InitSuccess)


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
            cls.EnableCtrl(skill, 50 if cl_action.GetMonsterPhase(skill) >= 3 else 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 50, 1)

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
            cls.EnableCtrl(skill, 250, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(SectorRotateCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ALL):
            if cl_action.CheckVictimSID(skill, 1184):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            elif cl_action.CheckVictimSID(skill, 1185):
                cl_action.ChangeVictimDefValue(skill, cl_action.GetSkillVictimAttr(skill, 'HPMax') * -1, DAM_USE_HP)
            else:
                cl_action.WeaponDamage(skill, {
                    'Att': 150 }, { }, sendPFMsg = False)
                cl_action.PushHeroVictim(skill, (0, 0, 0), 5, 5, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetSkillVarCache(skill, 'WaveDir'), (0, 8, 0), 90, (60 if cl_action.GetMonsterPhase(skill) >= 3 else 45) * ((cl_action.GetAttackerStateCount(skill, 8111, dState = { }) + 100) / 100), 11, 50, targettype = OBJ_ENEMY, effect = None, antiEffect = None, innerRadius = 30)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.FloatToIntFloor(skill, 160 if cl_action.GetMonsterPhase(skill) >= 2 else 240), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.CustomPerformAction(skill, 39021, 'TryAdjustWaveDir', [
        90,
        -1,
        20])
    cl_action.MonsterAttackerFacePos(skill, cl_action.GetSkillServerCache(skill, 'FacePos'), 20)
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39021
    m_Name = '罗睺左挥掌'
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
        'DebuffProb': 10000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']


def TryAdjustWaveDir(oSkill, *args):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    iAngle = args[0][0]
    iFlag = args[0][1]
    iOffsetAngle = (iAngle // 2) * iFlag
    iExtOffsetAngle = args[0][2]
    iHalfAngle = iAngle // 2
    oVictim = oGame.GetObject(oSkill.m_Base['VID'])
    vVictimPos = oVictim.GetPos()
    lstSealWallID = oAttack.Query('SealWallID')
    if lstSealWallID:
        lstSealWallAngle = []
        for iSealWall in lstSealWallID:
            oSealWall = oGame.GetObject(iSealWall)
            lstSealWallAngle.append(cl_math.CalAngle2D(oSealWall.GetPos(), vVictimPos))
        
        iAngleC1 = lstSealWallAngle[0] - iHalfAngle
        iAngleC2 = lstSealWallAngle[1] - iHalfAngle
        if iAngleC1 < 0 and iAngleC2 < 0:
            SendAlert('err', f'''罗睺挥掌所需角度不够,请检查 {iAngle} {iOffsetAngle} {iAngleC1} {iAngleC2}''')
        elif iAngleC1 < 0:
            iOffsetAngle = iOffsetAngle + abs(iAngleC1) + iExtOffsetAngle
        elif iAngleC2 < 0:
            iOffsetAngle = iOffsetAngle - (abs(iAngleC2) + iExtOffsetAngle)
        vDir = cl_math.RotateAroundVector(cl_math.Vec3Minus(vVictimPos, oAttack.GetPos()), (0, 1, 0), iOffsetAngle)
        oSkill.m_VarCache['WaveDir'] = vDir
    else:
        vDir = cl_math.RotateAroundVector(cl_math.Vec3Minus(vVictimPos, oAttack.GetPos()), (0, 1, 0), iOffsetAngle)
        oSkill.m_VarCache['WaveDir'] = vDir
    vMidDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), -iFlag * iHalfAngle)
    vFacePos = cl_math.Vec3DisplacePos(oAttack.GetPos(), vMidDir, 30)
    oSkill.m_Collect['FacePos'] = vFacePos

