# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_convolution.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_convolution.pyc
# Source Generated with Decompyle++
# File: crt_convolution.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND
from cl_commondefines import VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, VICTIM_STATE_HIT, OBJ_ALL
from .mobject import CBaseCartoon
MAX_CONTINUE_FRAME = 100

class ConvolutionCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            cls.Disable(oSkill, dCartoon)
            return None
        oSkill.Call_Out(MAX_CONTINUE_FRAME, dCartoon['ID'])
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iGatherTime, lstgatherinterval, iTargetID, fSpeed, targettype = OBJ_ALL, *args, **kwargs):
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['TargetID'] = iTargetID
        dCartoon['Offset'] = dClient['Offset']
        dCartoon['TargetType'] = targettype
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'Offset': dCartoon['Offset'] }
        if 'FlyOverDis' in dClient:
            dNet['FlyOverDis'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        dCartoon['AllVLST'] = []

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        if 'FlyOverDis' in dClient:
            dNet['FlyOverDis'] = 1
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
                elif not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT:
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
            dNet['Trigger'] = dClient['Trigger']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if oSkill.m_Game.GetFrameNum() < dCartoon['StartFrame'] + MAX_CONTINUE_FRAME:
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

