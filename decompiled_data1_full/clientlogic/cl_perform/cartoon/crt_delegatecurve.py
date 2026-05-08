# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatecurve.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatecurve.pyc
# Source Generated with Decompyle++
# File: crt_delegatecurve.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, GAME_FRAME
from cl_commondefines import OBJ_ALL, MONSTER_PART_UNTAGGED, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from cl_pxlayer import PXMASK_SKILLBLK
from .mobject import CBaseCartoon

class DelegateCurveCartoon(CBaseCartoon):
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
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif (oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame']) * dCartoon['SpeedPerFrame'] > dCartoon['Distance']:
            iOver = 1
        if 'Over' in dCartoon or dCartoon['Over'] <= oSkill.m_Game.GetFrameNum():
            cls.AllOver(oSkill, dCartoon)
        elif iOver:
            dCartoon['Over'] = oSkill.m_Game.GetFrameNum() + cls.m_WorldLineOutFrame
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
            cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Over' in dClient:
            dDelegateOver = dCartoon.setdefault('DelegateOver', { })
            dDelegateOver[dClient['Source']] = 1
            if 'End' in dClient:
                if len(dDelegateOver) == 1 or dClient['Source'] == oSkill.m_Base['VID']:
                    dCartoon['Final'] = dClient['End']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, iPierce, fDistance, fSpeed, iAnglePerSecond, fHeightRatio, targettype = OBJ_ALL, defLockPos = (0, 0, 0), *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['AnglePerFrame'] = iAnglePerSecond // GAME_FRAME
        dCartoon['HeightRatio'] = fHeightRatio
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['AllVLST'] = []
        dCartoon['DefLockPos'] = defLockPos
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'LockTarget': [
                oSkill.m_Base['VID']],
            'Offset': dCartoon['DefLockPos'] }
        oAttack = oSkill.GetAttack()
        vAttack = oAttack.GetPos()
        if vAttack != StartPos:
            vCheckStart = (vAttack[0], StartPos[1], vAttack[2])
            r = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vCheckStart, StartPos, PXMASK_SKILLBLK, {
                'Normal': 1,
                'PassID': oAttack.m_ID })
        else:
            r = [
                -1]
        if r[0] != -1:
            vHitPos = r[1]
            dCartoon['Final'] = vHitPos
            dNet['Ray'] = [
                (vHitPos, r[2], 0, MONSTER_PART_UNTAGGED)]
            dNet['Over'] = 1
            cls.HitStatic(oSkill)
            cls.Disable(oSkill, dCartoon)
            cls.AllOver(oSkill, dCartoon)
        else:
            iFlyFrame = int(fDistance // dCartoon['SpeedPerFrame'] + 1)
            oSkill.Call_Out(iFlyFrame, dCartoon['ID'])
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

