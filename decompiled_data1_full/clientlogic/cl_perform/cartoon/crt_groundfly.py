# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_groundfly.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_groundfly.pyc
# Source Generated with Decompyle++
# File: crt_groundfly.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, Time2Frame, GAME_FRAME
from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
import cl_math
from .mobject import CBaseCartoon

class GroundFlyCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def AllOver(cls, oSkill, dCartoon):
        oSkill.PopStack(dCartoon)

    AllOver = classmethod(AllOver)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'DelegateOver' in dCartoon:
            iOver = 1
            dSendOverPlayer = dCartoon['DelegateOver']
            lstLiveOnlinePlayer = oSkill.m_Game.m_WarMgr.GetLiveOnlinePlayer()
            if set(dSendOverPlayer.keys()) == set(lstLiveOnlinePlayer):
                cls.AllOver(oSkill, dCartoon)
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame'] > dCartoon['FlyFrame']:
            iOver = 1
        if 'Over' in dCartoon or dCartoon['Over'] <= oSkill.m_Game.GetFrameNum():
            cls.AllOver(oSkill, dCartoon)
        elif iOver:
            dCartoon['Over'] = oSkill.m_Game.GetFrameNum() + cls.m_WorldLineOutFrame
            oSkill.Call_Out(cls.m_WorldLineOutFrame, iNodeID)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return iOver

    IsOver = classmethod(IsOver)
    
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
                if 'TriggerStop' not in dCartoon or dCartoon['TriggerStop']:
                    dCartoon['Pierce'] -= 1
                dCartoon['CurPos'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Over' in dClient:
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
            if 'End' in dClient:
                if len(dDelegateOver) == 1 or dClient['Source'] == oSkill.m_Base['VID']:
                    dCartoon['Final'] = dClient['End']
        if 'Trigger' in dClient and 'Trigger' not in dCartoon:
            dCartoon['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, vDir, fSpeed, fFlyTime, fRadius, fMaxAngle, tolerateRadius = 0.5, targettype = OBJ_ALL, triggerStop = True, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['Dir'] = (vDir,)
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['FlyFrame'] = Time2Frame(fFlyTime)
        dCartoon['Radius'] = fRadius
        dCartoon['MaxAngle'] = fMaxAngle
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['AllVLST'] = []
        dCartoon['TriggerStop'] = triggerStop
        dCartoon['Pierce'] = 1
        dNet = {
            'Start': dCartoon['Start'],
            'SpeedVector': cl_math.Vec3MulF(vDir, fSpeed) }
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(dCartoon['FlyFrame'], dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

