# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_splittraceray.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_splittraceray.pyc
# Source Generated with Decompyle++
# File: crt_splittraceray.pyc (Python 3.6)

from cl_only import Second2Frame, GAME_FRAME_SECOND
from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
import cllib.lib_cartoon as cartooncheck
import cl_math
from .crt_raycast import RayCastCartoon

class SplitTraceCartoon(RayCastCartoon):
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, effect = 0, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        dCartoon['Radius'] = 0
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = Second2Frame(fDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dCartoon['PierceStatic'] = True

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iHit = 0
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstRay = dClient['Ray']
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                elif iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstVLST.append(iVictim)
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                
                dCartoon['CurPos'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'Ray': lstSend }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)

