# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_monsterjump.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_monsterjump.pyc
# Source Generated with Decompyle++
# File: crt_monsterjump.pyc (Python 3.6)

from cl_only import Functor
from cl_commondefines import PATHMODE_COLLISIONLESS
import cl_math
from .mobject import CBaseCartoon

class MonsterJumpCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack or not dCartoon['PathLine']:
            cls.Disable(oSkill, dCartoon)
            return None
        vStart = dCartoon['PathLine'].pop(0)
        if cl_math.CheckDistance3D(oAttack.GetPos(), vStart, 0.5):
            cls.Restart(oSkill, dCartoon)
        else:
            oAttack.m_MoveCtrl.SeekPath(oAttack, vStart, Functor(PathMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID'], True))
            oAttack.m_MoveCtrl.SetPathMode('CrtJumpMove', PATHMODE_COLLISIONLESS)
            if dCartoon['FacePath'] and oAttack.m_FaceCtrl:
                oAttack.m_FaceCtrl.FacePath(oAttack, 'JumpCrt')

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            cls.Disable(oSkill, dCartoon)
            return None
        vTar = dCartoon['PathLine'].pop(0)
        oAttack.m_MoveCtrl.ClearPathMode('CrtJumpMove')
        oAttack.m_MoveCtrl.JumpMove(oAttack, vTar, dCartoon['Speed'], dCartoon['Height'], dCartoon['JumpTimeConfig'], Functor(PathMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID'], False))

    Restart = classmethod(Restart)
    
    def HitTarget(cls, oSkill, dCartoon):
        return 1

    HitTarget = classmethod(HitTarget)
    
    def Disable(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if oAttack:
            if dCartoon['FacePath'] and oAttack.m_Agent:
                oAttack.m_Agent.ResumeFaceStatus()
            if oAttack.m_MoveCtrl:
                oAttack.m_MoveCtrl.ClearPathMode('CrtJumpMove')
        super(MonsterJumpCartoon, cls).Disable(oSkill, dCartoon)

    Disable = classmethod(Disable)
    
    def InitTraceServer(cls, oSkill, dCartoon, lstPos, fJumpSpeed, fJumpHeight, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime, iFacePath = 1):
        dCartoon['PathLine'] = list(lstPos)
        dCartoon['Speed'] = fJumpSpeed
        dCartoon['Height'] = fJumpHeight
        dCartoon['FacePath'] = iFacePath
        dCartoon['JumpTimeConfig'] = (iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime)

    InitTraceServer = classmethod(InitTraceServer)
    
    def IsOver(cls, oSkill, dCartoon):
        if dCartoon['PathLine']:
            return 0
        iNodeID = dCartoon['ID']
        oSkill.Send(iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)


def PathMoveEnd(iActNum, iCartoon, bFirst, oAttack, tEnd, iFail):
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    if iFail:
        oSkill.Halt('jumpfail')
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if bFirst and dCartoon['PathLine']:
        dCartoon['cls'].Restart(oSkill, dCartoon)
    else:
        oSkill.Update([
            dCartoon['ID']])

