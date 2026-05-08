# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegateraycast.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegateraycast.pyc
# Source Generated with Decompyle++
# File: crt_delegateraycast.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, GAME_FRAME
from cl_commondefines import MONSTER_PART_UNTAGGED, OBJ_ALL, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK
from cl_pxlayer import PXMASK_SKILLBLK
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class DelegateRayCastCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif not cl_math.CheckDistance3D(dCartoon['Start'], dCartoon['CurPos'], dCartoon['Distance'] - dCartoon['Radius']):
            fRadius = dCartoon['Radius']
            dCartoon['Final'] = dCartoon['CurPos'] if fRadius == 0 else cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fRadius)
            iOver = 1
        elif oSkill.m_Game.GetFrameNum() >= dCartoon['DealFrame']:
            iOver = 1
            dCartoon['Final'] = dCartoon['CurPos']
        if iOver:
            iNodeID = dCartoon['ID']
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, ShowStartPos, EndPos, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, effect = 0, radius = 0, flyover = 0, passid = 0, iLockTarget = 0, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
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
            'Start': StartPos }
        if iLockTarget:
            dNet['LockTarget'] = [
                iLockTarget]
        else:
            dNet['End'] = EndPos
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != ShowStartPos:
            dNet['Start'] = ShowStartPos
        if bIgnoreStatic:
            dNet['IgnoreStatic'] = 1
        if oSkill.m_Game.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = StartPos
            (tx, ty, tz) = EndPos
            debug.ClearDebugLine(oSkill.m_Game, debug.LINE_TILE)
            debug.DebugLine(oSkill.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
        dCartoon['AllVLST'] = []
        oAttack = oSkill.GetAttack()
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
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = int((fDistance / fSpeed + 5) * GAME_FRAME)
        dCartoon['DealFrame'] = oSkill.m_Game.GetFrameNum() + iFlyFrame
        oSkill.Call_Out(iFlyFrame, dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)
    
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
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                elif iVictimState == VICTIM_STATE_BLOCK and dCartoon['Pierce'] > 0:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Over' in dClient:
            dCartoon['Final'] = dClient['End']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

