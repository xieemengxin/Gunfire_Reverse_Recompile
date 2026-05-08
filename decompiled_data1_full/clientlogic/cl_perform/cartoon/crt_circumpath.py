# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_circumpath.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_circumpath.pyc
# Source Generated with Decompyle++
# File: crt_circumpath.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import VICTIM_STATE_HIT, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, WARRIOR_BUILD
import cl_math
from .mobject import CBaseCartoon

class CircumPathCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if 'Over' in dCartoon:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            UpdateBuildInfo(oSkill, dCartoon)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Trace(cls, oSkill, dCartoon):
        PreGetFinalPos(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState in (VICTIM_STATE_VALID, VICTIM_STATE_HIT):
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                elif iVictimState == VICTIM_STATE_BLOCK and dCartoon['HitStatic'] == 0:
                    dCartoon['HitStatic'] = 1
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        if 'Trigger' in dClient and 'Trigger' not in dCartoon:
            dCartoon['Trigger'] = 1
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStartPos, fAngle, vCenterPos, fInitAngleSpeed, fAccpSpeed, fMaxAngleSpeed, iEntityID):
        dNet = {
            'Start': vStartPos,
            'EntityID': iEntityID,
            'Frame': oSkill.m_Game.GetFrameNum() }
        dCartoon['AllVLST'] = []
        dCartoon['HitStatic'] = 0
        dCartoon['Start'] = vStartPos
        dCartoon['Angle'] = fAngle
        dCartoon['CenterPos'] = vCenterPos
        dCartoon['EntityID'] = iEntityID
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)


def UpdateBuildInfo(oSkill, dCartoon):
    oGame = oSkill.m_Game
    iEntityID = dCartoon['EntityID']
    oEntity = oGame.GetObject(iEntityID)
    if not oEntity:
        return None
    iAngle = int(dCartoon['Angle'])
    iClockWise = iAngle / abs(iAngle)
    vFace = cl_math.RotateAroundVector(cl_math.Vec3Minus(dCartoon['Start'], dCartoon['CenterPos']), (0, 1, 0), iAngle)
    vFinalPos = oEntity.Query('CircumPathFinalPos')
    if vFinalPos:
        oGame.Scene_Walk(iEntityID, vFinalPos)
        oEntity.RefreshPos()
    if oEntity.m_FightType & WARRIOR_BUILD == WARRIOR_BUILD:
        fAngle = cl_math.CalRotate2D(cl_math.RotateAroundVector(vFace, (0, iClockWise, 0), 90))
        tAngle = (0, fAngle, 0)
        tEuler = cl_math.Angle2Radians(tAngle)
        oGame.SetEuler(oEntity.m_ID, tEuler)
        oEntity.m_ModelData.SetModelAngle(tAngle)


def PreGetFinalPos(oSkill, dCartoon):
    oGame = oSkill.m_Game
    iEntityID = dCartoon['EntityID']
    oEntity = oGame.GetObject(iEntityID)
    if not oEntity:
        return None
    iAngle = int(dCartoon['Angle'])
    vFace = cl_math.RotateAroundVector(cl_math.Vec3Minus(dCartoon['Start'], dCartoon['CenterPos']), (0, 1, 0), iAngle)
    vFinalPos = cl_math.Vec3DisplaceDir(dCartoon['CenterPos'], vFace, cl_math.CalDistance3D(dCartoon['Start'], dCartoon['CenterPos']))
    oEntity.Set('CircumPathFinalPos', vFinalPos)

