# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_raycast.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_raycast.pyc
# Source Generated with Decompyle++
# File: crt_raycast.pyc (Python 3.6)

from cl_only import Second2Frame, PY_FLAG_DEAD, GAME_FRAME_SECOND, GAME_FRAME
from cl_commondefines import MONSTER_PART_UNTAGGED, CRT_CHECK_SERVER, OBJ_ALL, VICTIM_STATE_HIT, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, CRT_EXTCHECK_SERVANT, WARRIOR_MECH, CRT_EXTCHECK_LASERWEAPON, SIDE_TYPE_HERO
from cl_pxlayer import PXMASK_SKILLBLK, PXMASK_LIVEOBJ, PXMASK_SIDEBLK
import cl_math
import cl_gamedebug as debug
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon
DEFAULT_ENDFRAME = GAME_FRAME * 20

class RayCastCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
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
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, effect = 0, radius = 0, flyover = 0, passid = 0, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        dCartoon['Radius'] = radius
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dNet = {
            'End': dCartoon['End'] }
        if 'extCheck' in kwargs:
            if kwargs['extCheck'] == CRT_EXTCHECK_SERVANT:
                dCartoon['NoCostServant'] = 1
            elif kwargs['extCheck'] == CRT_EXTCHECK_LASERWEAPON:
                dCartoon['PierceStatic'] = 1
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = Second2Frame(fDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        if 'End' in dClient:
            dCartoon['Final'] = dClient['End']
        if 'FlyOverDis' in dClient:
            dCartoon['FlyOverDis'] = 1
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                    dCartoon['CurPos'] = vHitPos
                elif not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT and cls.CheckValidDamage(dCartoon, iVictim, iHitPart):
                        dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim, dCartoon)
                        dCartoon['AllVLST'].append(iVictim)
                        lstVLST.append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart }
                        lstHitInfo.append(dHitInfo)
                        dCartoon['AllHitInfo'].append(dHitInfo)
                        lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                        dCartoon['CurPos'] = vHitPos
                    
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['CurPos'] = dCartoon['CurPos']
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
            cls.CollectSkillInfo(oSkill, dCartoon)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOverClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' not in dClient:
            return 0
        return 1

    IsOverClient = classmethod(IsOverClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, ShowStartPos, EndPos, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, effect = 0, radius = 0, flyover = 0, passid = 0, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        if dCartoon['Distance'] and dCartoon['SpeedPerFrame']:
            dCartoon['EndFrame'] = dCartoon['StartFrame'] + dCartoon['Distance'] // dCartoon['SpeedPerFrame']
        else:
            dCartoon['EndFrame'] = dCartoon['StartFrame'] + DEFAULT_ENDFRAME
        dCartoon['TargetType'] = targettype
        dCartoon['Radius'] = radius
        dCartoon['CurPos'] = StartPos
        dCartoon['PassID'] = passid
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        if 'IgnoreLayer' in oSkill.m_Custom and PXMASK_SKILLBLK in oSkill.m_Custom['IgnoreLayer']:
            bIgnoreStatic = True
        else:
            bIgnoreStatic = False
        dCartoon['IgnoreStatic'] = bIgnoreStatic
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != ShowStartPos:
            dNet['Start'] = ShowStartPos
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            dNet['CheckStart'] = StartPos
        if bIgnoreStatic:
            dNet['IgnoreStatic'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        if oSkill.m_Game.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = StartPos
            (tx, ty, tz) = EndPos
            debug.ClearDebugLine(oSkill.m_Game, debug.LINE_TILE)
            debug.DebugLine(oSkill.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
        dCartoon['AllVLST'] = []
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        vAttack = oAttack.GetPos()
        if vAttack != StartPos and not bIgnoreStatic:
            vCheckStart = (vAttack[0], StartPos[1], vAttack[2])
            r = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vCheckStart, StartPos, PXMASK_SKILLBLK, {
                'Normal': 1,
                'PassID': oAttack.m_ID if not dCartoon['PassID'] else dCartoon['PassID'] })
            if r[0] != -1:
                vHitPos = r[1]
                dCartoon['Over'] = 1
                dCartoon['Final'] = vHitPos
                dNet['Ray'] = [
                    (vHitPos, r[2], 0, MONSTER_PART_UNTAGGED)]
                dNet['Over'] = 1
                cls.HitStatic(oSkill)
                cls.Disable(oSkill, dCartoon)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        vCur = dCartoon['CurPos']
        fDisPerFrame = dCartoon['SpeedPerFrame']
        fRadius = dCartoon['Radius']
        oGame = oSkill.m_Game
        vTar = cl_math.Vec3Mad(vCur, dCartoon['Dir'], fDisPerFrame)
        dCartoon['CurPos'] = vTar
        iPassID = oSkill.m_Base['AID'] if not dCartoon['PassID'] else dCartoon['PassID']
        if dCartoon['IgnoreStatic']:
            iMask = PXMASK_LIVEOBJ
        else:
            iMask = PXMASK_SKILLBLK | PXMASK_LIVEOBJ
        if oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            iBlockMask = PXMASK_SIDEBLK
        else:
            iBlockMask = PXMASK_SKILLBLK
        if fRadius == 0:
            lstVictim = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vCur, vTar, iMask, {
                'PassID': iPassID,
                'BlockMask': iBlockMask,
                'ExcludeFlag': PY_FLAG_DEAD,
                'Normal': 1 })
        else:
            lstVictim = oGame.Scene_SweepMultiple(oSkill.m_Base['Scene'], vCur, fRadius, dCartoon['Dir'], fDisPerFrame, iMask, {
                'PassID': iPassID,
                'BlockMask': iBlockMask,
                'ExcludeFlag': PY_FLAG_DEAD,
                'Normal': 1,
                'Distance': 1 })
        if not lstVictim:
            return 0
        if oSkill.m_Base['pid']:
            lstVictim = cls.PreProcessVictimList(oSkill, dCartoon, lstVictim)
        lstVLST = []
        lstSend = []
        for iVictim, dHit in lstVictim:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                dCartoon['Pierce'] = 0
                lstSend.append((dHit['Pos'], dHit['Normal'], 0, MONSTER_PART_UNTAGGED))
            elif iVictimState == VICTIM_STATE_VALID:
                fDistance = dHit['Distance'] if 'Distance' in dHit else 1
                if not fDistance:
                    dHit['Pos'] = cl_math.Vec3Mad(vCur, dCartoon['Dir'], fDisPerFrame * 0.5)
                dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim, dCartoon)
                lstVLST.append(iVictim)
                lstSend.append((dHit['Pos'], dCartoon['Dir'], iVictim, MONSTER_PART_UNTAGGED))
                dCartoon['AllVLST'] = lstVLST
            if dCartoon['Pierce'] <= 0:
                dCartoon['Final'] = dHit['Pos']
                dCartoon['CurPos'] = dHit['Pos']
                break
        
        oSkill.m_Update['LastVLST'] = lstVLST
        oSkill.m_Update['CurPos'] = dCartoon['CurPos']
        dNet = {
            'Ray': lstSend,
            'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
        oSkill.Send(dCartoon['ID'], dNet)
        cls.CollectSkillInfo(oSkill, dCartoon)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOverServer(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif not cl_math.CheckDistance3D(dCartoon['Start'], dCartoon['CurPos'], dCartoon['Distance'] - dCartoon['Radius']):
            fRadius = dCartoon['Radius']
            dCartoon['Final'] = dCartoon['CurPos'] if fRadius == 0 else cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fRadius)
            iOver = 1
        elif oSkill.m_Game.GetFrameNum() > dCartoon['EndFrame']:
            iOver = 1
        if iOver:
            return 1
        return 0

    IsOverServer = classmethod(IsOverServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        if 'Final' in dCartoon:
            vEnd = dCartoon['Final']
        else:
            fRadius = dCartoon['Radius']
            vEnd = dCartoon['CurPos'] if fRadius == 0 else cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fRadius)
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)
    
    def GetVictimPierceCost(cls, oSkill, iVictim, dCartoon = None):
        iCost = CBaseCartoon.GetVictimPierceCost(oSkill, iVictim)
        if iCost and dCartoon and 'NoCostServant' in dCartoon:
            oVictim = oSkill.m_Game.GetObject(iVictim)
            if oVictim and oVictim.m_FightType == WARRIOR_MECH:
                iCost = 0
        return iCost

    GetVictimPierceCost = classmethod(GetVictimPierceCost)

