# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_sectorrotate.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_sectorrotate.pyc
# Source Generated with Decompyle++
# File: crt_sectorrotate.pyc (Python 3.6)

from cl_only import GAME_FRAME, CeilDivide
from cl_commondefines import CRT_CHECK_SERVER, HITPART_DIRECTPOS, OBJ_ALL, VICTIM_STATE_VALID, ATT_SHAPE_RECTANGLE
from cl_pxlayer import PXMASK_LIVEOBJ
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class SectorRotateCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, *args, **kwargs):
        pass

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return False

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, Dir, EffectOffset, Angle, AngleSpeed, Height, Radius, targettype = OBJ_ALL, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['TargetType'] = targettype
        dCartoon['Angle'] = Angle
        dCartoon['Dir'] = (Dir[0], 0, Dir[2])
        dCartoon['AngleSpeed'] = abs(AngleSpeed) / GAME_FRAME
        dCartoon['Height'] = Height
        dCartoon['Radius'] = Radius
        dCartoon['ClockWise'] = AngleSpeed / abs(AngleSpeed)
        dCartoon['CurAngle'] = 0
        dCartoon['AllVLST'] = []
        dCartoon['InnerRadius'] = kwargs['innerRadius'] if 'innerRadius' in kwargs else 0
        dNet = {
            'Start': StartPos,
            'Direction': Dir }
        oSkill.Send(dCartoon['ID'], dNet)
        oGame = oSkill.m_Game
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_TILE)
            debug.ClearDebugLine(oGame, debug.LINE_BOX)
            debug.DebugSector(oGame, StartPos, Radius, Dir, Angle * dCartoon['ClockWise'], debug.LINE_TILE)
            debug.DebugSector(oGame, (StartPos[0], StartPos[1] + Height, StartPos[2]), Radius, Dir, Angle * dCartoon['ClockWise'], debug.LINE_TILE)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        lstVictim = cls.GetAllTarget(oSkill, dCartoon)
        if not lstVictim:
            return 0
        lstHitInfo = []
        for iVictim in lstVictim:
            dHitInfo = {
                'Victim': iVictim,
                'HitArea': HITPART_DIRECTPOS }
            lstHitInfo.append(dHitInfo)
        
        oSkill.m_Update['LastVLST'] = lstVictim
        oSkill.m_Update['HitInfo'] = lstHitInfo
        dNet = {
            'LastVLST': lstVictim }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def GetAllTarget(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        iCurAngle = dCartoon['CurAngle']
        iClockWise = dCartoon['ClockWise']
        iAngle = min(dCartoon['AngleSpeed'], dCartoon['Angle'] - iCurAngle)
        vDir = cl_math.RotateAroundVector(dCartoon['Dir'], (0, 1, 0), int(iCurAngle + CeilDivide(iAngle, 2)) * iClockWise)
        if cl_math.IsZero(vDir):
            return []
        fRadius = dCartoon['Radius']
        fHeight = dCartoon['Height']
        dCartoon['CurAngle'] += iAngle
        vStart = dCartoon['Start']
        fInnerRadius = dCartoon['InnerRadius']
        fWidth = fRadius * cl_math.SinAngle(iAngle)
        if fInnerRadius:
            vSectorStart = cl_math.Vec3DisplaceDir(vStart, vDir, fInnerRadius)
            fLength = fRadius - fInnerRadius
        else:
            vSectorStart = vStart
            fLength = fRadius
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_BOX)
            debug.DebugBox(oGame, vSectorStart, vDir, fLength, fWidth, fHeight)
        lstArgs = [
            vSectorStart,
            vDir,
            fLength,
            fWidth,
            fHeight]
        lstHit = cl_math.GetAttackTargetList(oGame, oSkill.m_Base['Scene'], ATT_SHAPE_RECTANGLE, lstArgs, {
            'Mask': PXMASK_LIVEOBJ,
            'BlockMask': 0 })
        lstTarget = []
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                dCartoon['AllVLST'].append(iVictim)
                lstTarget.append(iVictim)
        
        return lstTarget

    GetAllTarget = classmethod(GetAllTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon or dCartoon['CurAngle'] >= dCartoon['Angle']:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)

