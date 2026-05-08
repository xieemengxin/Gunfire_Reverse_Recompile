# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_flylinepath.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_flylinepath.pyc
# Source Generated with Decompyle++
# File: crt_flylinepath.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import OBJ_ALL_NOSELF, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from .mobject import CBaseCartoon

class FlyLinePathCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def Disable(cls, oSkill, dCartoon):
        cls.End(oSkill)

    Disable = classmethod(Disable)
    
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
        iCurFrame = oSkill.m_Game.GetFrameNum()
        if dCartoon['StartFrame'] + GAME_FRAME * 15 <= iCurFrame:
            iOver = 1
        if 'Over' in dCartoon or dCartoon['Over'] <= iCurFrame:
            cls.AllOver(oSkill, dCartoon)
        elif iOver:
            dCartoon['Over'] = iCurFrame + cls.m_WorldLineOutFrame
            oSkill.Call_Out(cls.m_WorldLineOutFrame, iNodeID)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

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
                elif iVictimState == VICTIM_STATE_BLOCK and dCartoon['HitStatic'] == 0:
                    dCartoon['HitStatic'] = 1
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Over' in dClient:
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
            if 'End' in dClient:
                if len(dDelegateOver) == 1 or dClient['Source'] == oSkill.m_Base['VID']:
                    dCartoon['Final'] = dClient['End']
        if 'Trigger' in dClient and 'Trigger' not in dCartoon:
            dCartoon['Trigger'] = 1
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, iLinePathID, iStartFrame, targettype = OBJ_ALL_NOSELF, *args, **kwargs):
        dCartoon['TargetType'] = targettype
        dCartoon['AllVLST'] = []
        dCartoon['HitStatic'] = 0
        dNet = {
            'Frame': dCartoon['StartFrame'] }
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(GAME_FRAME * 15, dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)

