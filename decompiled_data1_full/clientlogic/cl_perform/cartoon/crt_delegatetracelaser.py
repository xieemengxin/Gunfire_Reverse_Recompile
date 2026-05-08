# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatetracelaser.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatetracelaser.pyc
# Source Generated with Decompyle++
# File: crt_delegatetracelaser.pyc (Python 3.6)

from cl_only import Time2Frame, GAME_FRAME
from cl_commondefines import VICTIM_STATE_VALID, VICTIM_STATE_HIT, VICTIM_STATE_BLOCK, OBJ_ALL
import cl_math
from .mobject import CBaseCartoon

class DelegateTraceLaserCartoon(CBaseCartoon):
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
            if set(dSendOverPlayer) == set(lstLiveOnlinePlayer):
                cls.AllOver(oSkill, dCartoon)
        iCurFrame = oSkill.m_Game.GetFrameNum()
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] <= iCurFrame:
            iOver = 1
        if 'Over' in dCartoon and dCartoon['Over'] <= iCurFrame:
            cls.AllOver(oSkill, dCartoon)
        if iOver:
            dCartoon['Over'] = iCurFrame + cls.m_WorldLineOutFrame
            oSkill.Call_Out(cls.m_WorldLineOutFrame, iNodeID)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, fMaxDis, fRadius, fRadiusInc, fMaxAngle, iTime, iInterval, iTargetType = OBJ_ALL, fEndAngle = 90, **kwargs):
        if not vStart or cl_math.IsZero(vStart):
            dCartoon['Start'] = oSkill.m_Base['vStart']
        else:
            dCartoon['Start'] = vStart
        oAttack = oSkill.GetAttack()
        vDir = oAttack.GetFacing()
        dCartoon['Distance'] = fMaxDis
        dCartoon['Radius'] = fRadius
        dCartoon['RadiusInc'] = fRadius * fRadiusInc / 100
        dCartoon['MaxAngle'] = fMaxAngle
        dCartoon['WaitFrame'] = Time2Frame(iTime)
        dCartoon['IntervalFrame'] = Time2Frame(iInterval)
        dCartoon['TargetType'] = iTargetType
        dCartoon['LockTarget'] = oSkill.m_Base['VID']
        dCartoon['Direction'] = vDir
        dCartoon['CurPos'] = vStart
        dNet = {
            'Start': vStart,
            'Direction': vDir,
            'LockTarget': [
                oSkill.m_Base['VID']] }
        oSkill.Send(dCartoon['ID'], dNet)
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'])

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
        if 'Over' in dClient:
            dCartoon['Final'] = dClient['End']
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

