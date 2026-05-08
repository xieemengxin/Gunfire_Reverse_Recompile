# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatethrow.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatethrow.pyc
# Source Generated with Decompyle++
# File: crt_delegatethrow.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL_NOSELF, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, WARRIOR_STONEPILLAR
import cl_math
from .mobject import CBaseCartoon

class DelegateThrowCartoon(CBaseCartoon):
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
                if dCartoon['HitOver'] and not dCartoon['Pierce']:
                    break
                if dCartoon['HitStaticOver'] and dCartoon['HitStatic']:
                    break
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
                    if dCartoon['HitOver']:
                        dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                        if dCartoon['Pierce'] <= 0:
                            dClient['Over'] = 1
                            break
                dCartoon['CurPos'] = None
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Over' in dClient:
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
            if 'End' in dClient or len(dDelegateOver) == 1 or dClient['Source'] == oSkill.m_Base['VID']:
                dCartoon['Final'] = cl_math.Vec3Add(dClient['End'], (0, 0.02, 0))
        if 'Trigger' in dClient and 'Trigger' not in dCartoon:
            dCartoon['Trigger'] = 1
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vDir, fSpeed, fRadius, vUpForce, vBounciness, iDelayTrigger, iHitStaticOver, pierce, targettype = OBJ_ALL_NOSELF, *args, **kwargs):
        dCartoon['Start'] = vStart
        dCartoon['CurPos'] = dCartoon['Start']
        if 'SpeedVector' not in dCartoon:
            vDir = cl_math.Vec3Normalize(vDir)
            dCartoon['SpeedVector'] = cl_math.Vec3MulF(vDir, fSpeed)
        dCartoon['Radius'] = fRadius
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['Pierce'] = pierce
        dCartoon['HitOver'] = 1 if pierce > 0 else 0
        dCartoon['TargetType'] = targettype
        dCartoon['AllVLST'] = []
        dCartoon['HitStatic'] = 0
        dCartoon['Final'] = vStart
        dNet = {
            'Start': dCartoon['Start'],
            'SpeedVector': dCartoon['SpeedVector'] }
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(GAME_FRAME * 15, dCartoon['ID'])

    InitTraceServer = classmethod(InitTraceServer)
    
    def GetVictimPierceCost(cls, oSkill, iVictim):
        iCost = CBaseCartoon.GetVictimPierceCost(oSkill, iVictim)
        if iCost and oSkill.m_CheckType & CRT_CHECK_SERVER:
            oVictim = oSkill.m_Game.GetObject(iVictim)
            if oVictim and oVictim.m_FightType == WARRIOR_STONEPILLAR:
                iCost = 0
        return iCost

    GetVictimPierceCost = classmethod(GetVictimPierceCost)

