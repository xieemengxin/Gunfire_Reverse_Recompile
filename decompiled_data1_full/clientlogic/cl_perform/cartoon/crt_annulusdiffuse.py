# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_annulusdiffuse.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_annulusdiffuse.pyc
# Source Generated with Decompyle++
# File: crt_annulusdiffuse.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import CRT_CHECK_SERVER, HITPART_DIRECTPOS, OBJ_ALL
from cl_commondefines import VICTIM_STATE_VALID, MONSTER_PART_BARRIAR
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_BOX
import cl_math
import cl_gamedebug as debug
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class AnnulusDiffuseCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, MinRadius, MaxRadius, Speed, Height, targettype = OBJ_ALL, pierceStatic = False, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        StartPos = dClient['Start']
        dCartoon['Start'] = StartPos
        dCartoon['TargetType'] = targettype
        dCartoon['MaxRadius'] = MaxRadius
        dCartoon['MinRadius'] = MinRadius
        dCartoon['HalfHeight'] = Height * 0.5
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['AllVLST'] = []
        dNet = {
            'Start': StartPos }
        oSkill.Send(dCartoon['ID'], dNet)
        oGame = oSkill.m_Game
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_TILE)
            debug.DebugCircle(oGame, StartPos, MaxRadius, debug.LINE_TILE)
            debug.DebugCircle(oGame, (StartPos[0], StartPos[1] + Height, StartPos[2]), MaxRadius, debug.LINE_TILE)
            if MinRadius != 0:
                debug.DebugCircle(oGame, StartPos, MinRadius, debug.LINE_TILE)
                debug.DebugCircle(oGame, (StartPos[0], StartPos[1] + Height, StartPos[2]), MinRadius, debug.LINE_TILE)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        cartooncheck.CheckDataDiffuseRay(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        iHit = 0
        fMinRadius = dCartoon['MinRadius']
        fMaxRadius = dCartoon['MaxRadius']
        vStart = dCartoon['Start']
        oGame = oSkill.m_Game
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            lstRay = dClient['Ray']
            for vHitPos, _, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    oVictim = oGame.GetObject(iVictim)
                    fModelRadius = oVictim.m_ModelRadius
                    fDistance = cl_math.CalDistance(vHitPos, vStart)
                    if fDistance < fMinRadius - fModelRadius or fDistance > fMaxRadius + fModelRadius:
                        continue
                    lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': HITPART_DIRECTPOS if iHitPart != MONSTER_PART_BARRIAR else iHitPart }
                lstHitInfo.append(dHitInfo)
                dCartoon['AllVLST'].append(iVictim)
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'LastVLST': lstVLST }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, MinRadius, MaxRadius, Speed, Height, targettype = OBJ_ALL, pierceStatic = False, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['TargetType'] = targettype
        dCartoon['MaxRadius'] = MaxRadius
        dCartoon['MinRadius'] = MinRadius
        dCartoon['Radius'] = MaxRadius - MinRadius
        dCartoon['Speed'] = Speed / GAME_FRAME
        dCartoon['HalfHeight'] = Height * 0.5
        dCartoon['CurRadius'] = 0
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['AllVLST'] = []
        dNet = {
            'Start': StartPos }
        oSkill.Send(dCartoon['ID'], dNet)
        oGame = oSkill.m_Game
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_TILE)
            debug.DebugCircle(oGame, StartPos, MaxRadius, debug.LINE_TILE)
            debug.DebugCircle(oGame, (StartPos[0], StartPos[1] + Height, StartPos[2]), MaxRadius, debug.LINE_TILE)
            if MinRadius != 0:
                debug.DebugCircle(oGame, StartPos, MinRadius, debug.LINE_TILE)
                debug.DebugCircle(oGame, (StartPos[0], StartPos[1] + Height, StartPos[2]), MinRadius, debug.LINE_TILE)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        lstVictim = cls.GetAllTarget(oSkill, dCartoon)
        if not lstVictim:
            return 0
        lstHitInfo = []
        for iVictim in lstVictim:
            dHitInfo = { }
            dHitInfo['Victim'] = iVictim
            dHitInfo['HitArea'] = HITPART_DIRECTPOS
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
        fInterval = min(abs(dCartoon['Speed']), dCartoon['Radius'] - dCartoon['CurRadius'])
        if dCartoon['Speed'] < 0:
            fMinRadius = dCartoon['MaxRadius'] - dCartoon['CurRadius'] - fInterval
        else:
            fMinRadius = dCartoon['CurRadius'] + dCartoon['MinRadius']
        fMaxRadius = fMinRadius + fInterval
        dCartoon['CurRadius'] += fInterval
        fHalfHeight = dCartoon['HalfHeight']
        vStart = dCartoon['Start']
        vHalfExtent = (fMaxRadius, fHalfHeight, fMaxRadius)
        lstHit = oGame.Scene_GetRectangleObjects(oSkill.m_Base['Scene'], vStart, (0, 0, -1), vHalfExtent, PXMASK_LIVEOBJ, {
            'BlockMask': PXMASK_BOX,
            'StartCenter': 1 })
        lstTarget = []
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                oVictim = oGame.GetObject(iVictim)
                fDistance = cl_math.CalDistance(oVictim.GetPos(), dCartoon['Start'])
                if fDistance < fMinRadius or fDistance > fMaxRadius:
                    continue
                dCartoon['AllVLST'].append(iVictim)
                lstTarget.append(iVictim)
        
        return lstTarget

    GetAllTarget = classmethod(GetAllTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            iOver = cls.IsOverServer(oSkill, dCartoon)
        else:
            iOver = cls.IsOverClient(oSkill, dCartoon)
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def IsOverServer(cls, oSkill, dCartoon):
        if 'Over' in dCartoon or dCartoon['CurRadius'] >= dCartoon['Radius']:
            return 1
        return 0

    IsOverServer = classmethod(IsOverServer)
    
    def IsOverClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' not in dClient:
            return 0
        return 1

    IsOverClient = classmethod(IsOverClient)

