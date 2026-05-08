# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_raycasttimer.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_raycasttimer.pyc
# Source Generated with Decompyle++
# File: crt_raycasttimer.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND
from cl_commondefines import VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, VICTIM_STATE_HIT
from .mobject import CBaseCartoon

class RaycastTimerCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iWaittime, iTriggertimes, lstShape, iAttShape, iTargetType, fdistance, fSpeed, *args, **kwargs):
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['TargetType'] = iTargetType
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        if 'End' in dClient:
            dCartoon['Final'] = dClient['End']
        if 'FlyOverDis' in dClient:
            dCartoon['FlyOverDis'] = 1
            dNet['FlyOverDis'] = 1
        if 'Count' in dClient:
            dNet['Count'] = 1
        if 'Direction' in dClient:
            dNet['Direction'] = dClient['Direction']
        if 'Ray' in dClient:
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
                elif 'FlyOverDis' not in dCartoon:
                    if (iVictimState == VICTIM_STATE_VALID or iVictimState == VICTIM_STATE_HIT) and cls.CheckValidDamage(dCartoon, iVictim, iHitPart):
                        dCartoon['AllVLST'].append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart }
                        lstVLST.append(iVictim)
                        lstHitInfo.append(dHitInfo)
                        dCartoon['AllHitInfo'].append(dHitInfo)
                        lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    elif 'FlyOverDis' in dCartoon and dCartoon['FlyOverDis'] == 1 or iVictimState == VICTIM_STATE_VALID or iVictimState == VICTIM_STATE_HIT:
                        dCartoon['AllVLST'].append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart }
                        lstVLST.append(iVictim)
                        lstHitInfo.append(dHitInfo)
                        lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dCartoon['AllVLST'] = []
            dNet['Trigger'] = 1
        oSkill.Send(iNodeID, dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' not in dClient:
            return 0
        oSkill.Send(iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)

