# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_sectordiffuse.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_sectordiffuse.pyc
# Source Generated with Decompyle++
# File: crt_sectordiffuse.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import CRT_CHECK_SERVER, HITPART_DIRECTPOS, OBJ_ALL, VICTIM_STATE_VALID, ATT_SHAPE_SECTOR
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_BOX
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class SectorDiffuseCartoon(CBaseCartoon):
    
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
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, MinRadius, MaxRadius, Span, Speed, Height, iAngle, targettype = OBJ_ALL, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['Dir'] = cl_math.Vec3Minus(EndPos, StartPos)
        dCartoon['TargetType'] = targettype
        dCartoon['MaxRadius'] = MaxRadius
        dCartoon['MinRadius'] = MinRadius
        dCartoon['Span'] = Span
        dCartoon['Radius'] = MaxRadius - MinRadius - Span
        dCartoon['Speed'] = Speed / GAME_FRAME
        dCartoon['Height'] = Height
        dCartoon['Angle'] = iAngle
        dCartoon['CurRadius'] = 0
        dCartoon['AllVLST'] = []
        dCartoon['IsOverByFightType'] = kwargs['isOverByFightType'] if 'isOverByFightType' in kwargs else False
        dCartoon['FightType'] = kwargs['fightType'] if 'fightType' in kwargs else 0
        dCartoon['IsUseSector'] = kwargs['isUseSector'] if 'isUseSector' in kwargs else False
        dNet = {
            'Start': StartPos,
            'End': EndPos }
        oSkill.Send(dCartoon['ID'], dNet)

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
        if dCartoon['IsUseSector']:
            return cls.GetAllTargetBySector(oSkill, dCartoon)
        return cls.GetAllTargetByRectangle(oSkill, dCartoon)

    GetAllTarget = classmethod(GetAllTarget)
    
    def GetAllTargetBySector(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        fInterval = min(abs(dCartoon['Speed']), dCartoon['Radius'] - dCartoon['CurRadius'])
        fMinRadius = dCartoon['CurRadius'] + dCartoon['MinRadius']
        fMaxRadius = fMinRadius + dCartoon['Span']
        dCartoon['CurRadius'] += fInterval
        fHeight = dCartoon['Height']
        vStart = dCartoon['Start']
        vDir = dCartoon['Dir']
        fAngle = dCartoon['Angle']
        lstArgs = [
            vStart,
            dCartoon['Dir'],
            fMaxRadius,
            fHeight,
            fAngle]
        dQArgs = {
            'Mask': PXMASK_LIVEOBJ,
            'BlockMask': PXMASK_BOX }
        lstHit = cl_math.GetAttackTargetList(oGame, oSkill.m_Base['Scene'], ATT_SHAPE_SECTOR, lstArgs, dQArgs)
        lstTarget = []
        iAttack = oSkill.m_Base['AID']
        iSide = oSkill.m_Cache['Side']
        iTargetType = dCartoon['TargetType']
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                oVictim = oGame.GetObject(iVictim)
                vVictimPos = oVictim.GetPos()
                fDistance = cl_math.CalDistance(vVictimPos, dCartoon['Start'])
                if fDistance <= fMinRadius or fDistance >= fMaxRadius:
                    continue
                if not cl_math.CheckTargetType(oGame, oVictim, iAttack, iSide, iTargetType):
                    continue
                if dCartoon['IsOverByFightType'] and oVictim.m_FightType == dCartoon['FightType']:
                    dCartoon['Over'] = 1
                dCartoon['AllVLST'].append(iVictim)
                lstTarget.append(iVictim)
        
        if oGame.m_WarMgr.Query('DebugRay'):
            SectorDebug(oGame, vStart, vDir, fAngle, fHeight, fMinRadius, fMaxRadius)
        return lstTarget

    GetAllTargetBySector = classmethod(GetAllTargetBySector)
    
    def GetAllTargetByRectangle(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        fInterval = min(abs(dCartoon['Speed']), dCartoon['Radius'] - dCartoon['CurRadius'])
        fMinRadius = dCartoon['CurRadius'] + dCartoon['MinRadius']
        fMaxRadius = fMinRadius + dCartoon['Span']
        dCartoon['CurRadius'] += fInterval
        fHalfHeight = dCartoon['Height'] * 0.5
        fHalfAngle = dCartoon['Angle'] * 0.5
        vStart = dCartoon['Start']
        vDir = dCartoon['Dir']
        vHalfExtent = (fMaxRadius, fHalfHeight, fMaxRadius)
        lstHit = oGame.Scene_GetRectangleObjects(oSkill.m_Base['Scene'], vStart, (0, 0, -1), vHalfExtent, PXMASK_LIVEOBJ, {
            'BlockMask': PXMASK_BOX,
            'StartCenter': 1 })
        lstTarget = []
        iAttack = oSkill.m_Base['AID']
        iSide = oSkill.m_Cache['Side']
        iTargetType = dCartoon['TargetType']
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                oVictim = oGame.GetObject(iVictim)
                vVictimPos = oVictim.GetPos()
                fDistance = cl_math.CalDistance(vVictimPos, dCartoon['Start'])
                if fDistance <= fMinRadius or fDistance >= fMaxRadius:
                    continue
                if not cl_math.CheckTargetType(oGame, oVictim, iAttack, iSide, iTargetType):
                    continue
                iAngle = cl_math.CalAngle2D(vDir, cl_math.Vec3Minus(vVictimPos, vStart))
                if iAngle > fHalfAngle:
                    continue
                if dCartoon['IsOverByFightType'] and oVictim.m_FightType == dCartoon['FightType']:
                    dCartoon['Over'] = 1
                dCartoon['AllVLST'].append(iVictim)
                lstTarget.append(iVictim)
        
        if oGame.m_WarMgr.Query('DebugRay'):
            SectorDebug(oGame, vStart, vDir, dCartoon['Angle'], dCartoon['Height'], fMinRadius, fMaxRadius)
        return lstTarget

    GetAllTargetByRectangle = classmethod(GetAllTargetByRectangle)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon or dCartoon['CurRadius'] >= dCartoon['Radius']:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)


def SectorDebug(oGame, vStart, vDir, fAngle, fHeight, fMinRadius, fMaxRadius):
    if not oGame.m_WarMgr.Query('RetainRay'):
        debug.ClearDebugLine(oGame, debug.LINE_TILE)
    fHalfAngle = fAngle * 0.5
    fHalfHeight = fHeight * 0.5
    iAngle = int(fHalfAngle)
    vCenter = cl_math.Vec3DisplaceDir(vStart, (0, 1, 0), fHalfHeight)
    (ox, oy, oz) = vCenter
    (x1, y1, z1) = cl_math.Vec3DisplaceDir(vCenter, vDir, fMinRadius)
    (x2, y2, z2) = cl_math.Vec3DisplaceDir(vCenter, vDir, fMaxRadius)
    debug.DebugLine(oGame, ox, oy, oz, x2, y2, z2, 65280, debug.LINE_TILE)
    (tx2, ty2, tz2) = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fMinRadius, iAngle)
    debug.DebugLine(oGame, ox, oy, oz, tx2, ty2, tz2, 65280, debug.LINE_TILE)
    debug.DebugLine(oGame, x1, y1, z1, tx2, ty2, tz2, 65280, debug.LINE_TILE)
    (tx2, ty2, tz2) = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fMaxRadius, iAngle)
    debug.DebugLine(oGame, ox, oy, oz, tx2, ty2, tz2, 65280, debug.LINE_TILE)
    debug.DebugLine(oGame, x2, y2, z2, tx2, ty2, tz2, 65280, debug.LINE_TILE)
    (tx3, ty3, tz3) = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fMinRadius, -iAngle)
    debug.DebugLine(oGame, ox, oy, oz, tx3, ty3, tz3, 65280, debug.LINE_TILE)
    debug.DebugLine(oGame, x1, y1, z1, tx3, ty3, tz3, 65280, debug.LINE_TILE)
    (tx3, ty3, tz3) = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fMaxRadius, -iAngle)
    debug.DebugLine(oGame, ox, oy, oz, tx3, ty3, tz3, 65280, debug.LINE_TILE)
    debug.DebugLine(oGame, x2, y2, z2, tx3, ty3, tz3, 65280, debug.LINE_TILE)

