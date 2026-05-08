# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_curgroundfly.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_curgroundfly.pyc
# Source Generated with Decompyle++
# File: crt_curgroundfly.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from .mobject import CBaseCartoon

class CurGroundFlyCartoon(CBaseCartoon):
    
    def InitTraceClient(cls, oSkill, dCartoon, fSpeed, fFlyTime, fMaxAngle, vEnemyCheckBox, vSeedCheckBox, tolerateRadius = 0.5, targettype = OBJ_ALL, **kwargs):
        dCartoon['TargetType'] = targettype
        dCartoon['AllVLST'] = []
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Start'] = dClient['Start']
        dCartoon['Direction'] = dClient['Direction']
        dCartoon['CurPos'] = dClient['Start']
        dNet = {
            'Start': dCartoon['Start'],
            'Direction': dCartoon['Direction'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if iNodeID in oSkill.m_NetReceive:
            dNetReceive = oSkill.m_NetReceive[iNodeID]
            if 'Over' in dNetReceive:
                iOver = 1
            if 'End' in dNetReceive:
                dCartoon['Final'] = dNetReceive['End']
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Start' in dClient:
            dCartoon['CurPos'] = dClient['Start']
            dNet['Start'] = dClient['Start']
        if 'End' in dClient:
            dNet['End'] = dClient['End']
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                elif iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Trigger' in dClient and 'Trigger' not in dCartoon:
            dCartoon['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, vDir, fSpeed, fFlyTime, fMaxAngle, vEnemyCheckBox, vSeedCheckBox, tolerateRadius = 0.5, targettype = OBJ_ALL, **kwargs):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

