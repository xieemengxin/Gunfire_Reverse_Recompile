# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_monsterliftland.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_monsterliftland.pyc
# Source Generated with Decompyle++
# File: crt_monsterliftland.pyc (Python 3.6)

from cl_only import Functor
from cl_pxlayer import PXMASK_SKILLBLK
from cl_object.logging import SkillLog
import cl_math
from .mobject import CBaseCartoon

class MonsterLiftLandCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            cls.Disable(oSkill, dCartoon)
            return None
        bLift = dCartoon['Lift']
        fDistance = dCartoon['Distance']
        vAttack = oAttack.GetPos()
        oGame = oAttack.m_Game
        fModelRadius = 0
        if bLift:
            if dCartoon['ForceMove']:
                fUpDistance = fDistance
            else:
                fModelHeight = oAttack.m_ModelHeight
                fModelRadius = oAttack.m_ModelRadius
                vAttackTop = cl_math.Vec3Add(vAttack, (0, fModelHeight, 0))
                lstVictim = oGame.Scene_SweepMultiple(oAttack.m_Scene, vAttackTop, fModelRadius, (0, 1, 0), fDistance, PXMASK_SKILLBLK, {
                    'BlockMask': PXMASK_SKILLBLK })
                fUpDistance = fDistance
                if lstVictim:
                    dCartoon['HitBlock'] = 1
                    for iVictim, dHit in lstVictim:
                        vHitPos = dHit['Pos']
                        if not cl_math.IsEqual(vHitPos, (0, 0, 0)):
                            fUpDistance = vHitPos[1] - vAttackTop[1]
                        else:
                            fUpDistance = 0
                    
            if fUpDistance < 0.1:
                fUpDistance = 0
            if fUpDistance > fDistance + fModelRadius:
                oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
                SkillLog.Debug('%s liftup %s %s %s over %s' % (oSkill.m_Base['pfid'], oScene.m_Level, vAttackTop, fUpDistance, fDistance + fModelRadius))
                fUpDistance = fDistance
            vTar = cl_math.Vec3Add(vAttack, (0, fUpDistance, 0))
        elif dCartoon['ForceMove']:
            fGroundDis = fDistance
        else:
            fModelRadius = oAttack.m_ModelRadius
            fCheckDistance = fDistance + 1
            lstVictim = oGame.Scene_SweepMultiple(oAttack.m_Scene, vAttack, fModelRadius, (0, -1, 0), fCheckDistance, PXMASK_SKILLBLK, {
                'BlockMask': PXMASK_SKILLBLK })
            fGroundDis = fCheckDistance
            if lstVictim:
                for iVictim, dHit in lstVictim:
                    vHitPos = dHit['Pos']
                    if not cl_math.IsEqual(vHitPos, (0, 0, 0)):
                        fGroundDis = vAttack[1] - vHitPos[1]
                    else:
                        fGroundDis = 0
                
        if fGroundDis < 0.1:
            fGroundDis = 0
        if fGroundDis > fDistance + fModelRadius:
            oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
            SkillLog.Debug('%s liftdown %s %s %s over %s' % (oSkill.m_Base['pfid'], oScene.m_Level, vAttack, fGroundDis, fDistance + fModelRadius))
            fGroundDis = fDistance
        vTar = cl_math.Vec3Minus(vAttack, (0, fGroundDis, 0))
        dCartoon['End'] = vTar
        cls.StartMove(oAttack, oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        if 'HitBlock' in dCartoon and dCartoon['HitBlock']:
            oSkill.m_Update['HitStatic'] = 1
        return 1

    HitTarget = classmethod(HitTarget)
    
    def InitTraceServer(cls, oSkill, dCartoon, fSpeed, bLift, fDistance, bForceMove = False):
        dCartoon['Speed'] = max(0, fSpeed)
        dCartoon['Distance'] = fDistance
        dCartoon['Lift'] = bLift
        dCartoon['ForceMove'] = bForceMove

    InitTraceServer = classmethod(InitTraceServer)
    
    def StartMove(cls, oAttack, oSkill, dCartoon):
        iRet = oAttack.m_MoveCtrl.AirMove(oAttack, dCartoon['End'], dCartoon['Speed'], False, Functor(PathMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID']))
        if not iRet:
            oSkill.Halt('monsterliftlandmovefail')
            return None

    StartMove = classmethod(StartMove)
    
    def IsOver(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        dCartoon['Final'] = oAttack.GetPos()
        iNodeID = dCartoon['ID']
        oSkill.Send(iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)


def PathMoveEnd(iActNum, iCartoon, oAttack, tEnd, iFail):
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if iFail:
        oSkill.Send(iCartoon, {
            'Over': 1 })
        dCartoon['cls'].Disable(oSkill, dCartoon)
        return None
    oSkill.Update([
        dCartoon['ID']])

