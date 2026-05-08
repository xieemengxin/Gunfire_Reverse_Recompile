# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/deviceactive/p50361.pyc
# RelativePath: clientlogic/cl_platformdata/pc/deviceactive/p50361.pyc
# Source Generated with Decompyle++
# File: p50361.pyc (Python 3.6)

from cl_pxlayer import PXMASK_BLOCK
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_ONE_DISTANCE, OBJ_ENEMY

class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CustomPerformAction(skill, 50361, 'CalcArrangePosAndFacing', {
            'Pos': cl_action.GetEndPositionInCrt(skill, 0) })
        cl_action.ArrangeDevice(skill, cl_action.GetSkillVarCache(skill, 'ArrangePos'), cl_action.GetSkillVarCache(skill, 'ArrangeFacing'), { }, 0)
        cl_action.SetDeciveAcitveStatus(skill, True)

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
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 1, 5, 40, targettype = OBJ_ENEMY, liveTime = 0, radius = 1.5, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_ONE_DISTANCE)

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
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.RecycleDevice(skill)
    cl_action.SetDeciveAcitveStatus(skill, False)
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CPerform as CCustomPerform
from cl_commondefines import DEVICE_PERFORM_POS_ARRANGE

class CPerform(CCustomPerform):
    m_SID = 50361
    m_Name = '屏障部署'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = { }
    m_Pos = DEVICE_PERFORM_POS_ARRANGE
    m_ForbidRule = 1091


def CalcArrangePosAndFacing(oSkill, dInfo):
    
    def ProjectOnPlane(vVector, vPlaneNormal):
        fDot = cl_math.VectorDot3D(vVector, vPlaneNormal)
        vProject = cl_math.Vec3MulF(vPlaneNormal, fDot)
        return cl_math.Vec3Minus(vVector, vProject)

    oAttack = oSkill.GetAttack()
    vPos = dInfo['Pos']
    vFacing = oAttack.GetFacing()
    if oAttack:
        oDevice = oAttack.GetDevice()
        if oDevice:
            fHalfHeight = oDevice.m_ModelHeight / 2
            fDis = oSkill.m_Game.Scene_GroundDistance(oAttack.m_Scene, vPos, fHalfHeight, PXMASK_BLOCK)
            if fDis < fHalfHeight and vFacing[1] < 0:
                vFacing = (vFacing[0], 0, vFacing[2])
            vProject = ProjectOnPlane((0, 1, 0), vFacing)
            vProject = cl_math.Vec3Normalize(vProject)
            vOffset = cl_math.Vec3MulF(vProject, -fDis)
            vPos = cl_math.Vec3Add(vPos, vOffset)
    oSkill.m_VarCache['ArrangePos'] = vPos
    oSkill.m_VarCache['ArrangeFacing'] = vFacing

