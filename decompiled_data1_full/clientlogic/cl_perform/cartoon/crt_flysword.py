# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_flysword.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_flysword.pyc
# Source Generated with Decompyle++
# File: crt_flysword.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, VICTIM_STATE_HIT
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class FlySwordCartoon(CBaseCartoon):
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Over' not in dClient:
            return 0
        dNet['Over'] = 1
        oSkill.Send(iNodeID, dNet)
        return 1

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, *args, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['TargetType'] = kwargs['targettype'] if 'targettype' in kwargs else OBJ_ALL
        vStart = dClient['Start']
        dCartoon['Start'] = vStart
        dCartoon['CurPos'] = vStart
        dNet = { }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != vStart:
            dNet['Start'] = vStart
        oSkill.Send(dCartoon['ID'], dNet)
        dCartoon['PierceStatic'] = True
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        if 'Over' in dClient:
            cls.Disable(oSkill, dCartoon)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Start' in dClient:
            dCartoon['CurPos'] = dClient['Start']
            dNet['Start'] = dClient['Start']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                elif not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT:
                        dCartoon['AllVLST'].append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart }
                        lstVLST.append(iVictim)
                        lstHitInfo.append(dHitInfo)
                        dCartoon['AllHitInfo'].append(dHitInfo)
                        lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

