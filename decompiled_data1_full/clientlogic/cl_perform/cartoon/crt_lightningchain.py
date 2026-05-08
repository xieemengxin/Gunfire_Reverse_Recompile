# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_lightningchain.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_lightningchain.pyc
# Source Generated with Decompyle++
# File: crt_lightningchain.pyc (Python 3.6)

from cl_commondefines import VICTIM_STATE_VALID, OBJ_ENEMY, VICTIM_STATE_BLOCK, CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED
from cl_pxlayer import PXMASK_MONSTER, PXMASK_SKILLBLK, PXMASK_ENEMYBLK
from cl_only import Second2Frame
from .mobject import CBaseCartoon
import cl_math

class LightningChainCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDiffDistance, fAttDistance, iPlayerID, sModeNode, fLiveTime, bKeepStart = False):
        dCartoon['TargetType'] = OBJ_ENEMY
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Start' not in dClient:
            dCartoon['Over'] = 1
            oSkill.Halt('nostart')
            return None
        dCartoon['Start'] = dClient['Start']
        dCartoon['Pierce'] = iPierce
        dCartoon['InitPierce'] = dCartoon['Pierce']
        dCartoon['DiffDistance'] = fDiffDistance
        dCartoon['AttDistance'] = fAttDistance
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['KeepStart'] = bKeepStart
        dCartoon['AllVLST'] = []
        dNet = { }
        if 'End' in dClient:
            dCartoon['End'] = dClient['End']
            dNet['End'] = dCartoon['End']
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstSend = []
            lstVLST = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                dCartoon['LastPos'] = dCartoon['CurPos']
                dCartoon['CurPos'] = vHitPos
                if not CheckDistance(oSkill, dCartoon):
                    continue
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    lstVLST.append(iVictim)
                    dCartoon['AllVLST'].append(iVictim)
                    cls.CollectSkillInfo(oSkill, dCartoon)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                elif iVictimState == VICTIM_STATE_BLOCK:
                    dCartoon['Pierce'] = 0
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
                
                if dCartoon['Pierce'] <= 0:
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['LastVLST'] = lstVLST
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceServer(cls, oSkill, dCartoon, iInitiative, vStart, iPierce, fDiffDistance, fAttDistance, iAttAngle, iNearDistance, iNearAngle, fDelayTime, bInitiativeFirestOpen, lstlockPosition, iPlayerID, sModeNode, iLiveTime, bKeepStart):
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['Start'] = vStart
        dCartoon['Pierce'] = iPierce
        dCartoon['InitPierce'] = iPierce
        dCartoon['DiffDistance'] = fDiffDistance
        dCartoon['AttDistance'] = fAttDistance
        dCartoon['KeepStart'] = bKeepStart
        dCartoon['IntervalFrame'] = Second2Frame(fDelayTime)
        dCartoon['CurTarget'] = 0
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['AllVLST'] = []

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        iPierce = dCartoon['Pierce']
        if iPierce <= 0:
            return 0
        iScene = oSkill.m_Base['Scene']
        if dCartoon['InitPierce'] == iPierce:
            lstVictim = [
                oSkill.m_Base['VID']]
        else:
            lstVictim = oGame.Scene_GetSphereObjects(iScene, dCartoon['LastPos'], dCartoon['DiffDistance'], PXMASK_MONSTER, {
                'BlockMask': PXMASK_SKILLBLK })
        lstVLST = []
        lstHitInfo = []
        dNet = { }
        lstSend = []
        dCartoon['LastPos'] = dCartoon['CurPos']
        iHitArea = MONSTER_PART_UNTAGGED
        for iVictim in lstVictim:
            if iVictim in dCartoon['AllVLST']:
                continue
            oVictim = oSkill.m_Game.GetObject(iVictim)
            if not oVictim:
                continue
            vPos = oVictim.GetPos()
            vCheckEnd = (vPos[0], vPos[1] + oVictim.m_ModelHeight * 0.6, vPos[2])
            (iVictim, vHitPos, vNormal) = oSkill.m_Game.Scene_RaycastSingle(iScene, dCartoon['LastPos'], vCheckEnd, PXMASK_ENEMYBLK, {
                'Normal': 1,
                'PassID': dCartoon['CurTarget'] })
            if iVictim == -1:
                continue
            dCartoon['CurPos'] = vHitPos
            if not CheckDistance(oSkill, dCartoon):
                continue
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                lstVLST.append(iVictim)
                dCartoon['AllVLST'].append(iVictim)
                cls.CollectSkillInfo(oSkill, dCartoon)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitArea }
                lstHitInfo.append(dHitInfo)
                dCartoon['CurTarget'] = iVictim
            elif iVictimState == VICTIM_STATE_BLOCK:
                dCartoon['Pierce'] = 0
                oSkill.m_Update['HitStatic'] = 1
                dNet['HitStatic'] = 1
            lstSend.append((vHitPos, vNormal, iVictim, iHitArea))
            if dCartoon['Pierce'] <= 0:
                dCartoon['Final'] = vHitPos
                break
        
        oSkill.m_Update['HitInfo'] = lstHitInfo
        oSkill.m_Update['LastVLST'] = lstVLST
        dNet['Ray'] = lstSend
        oSkill.Send(dCartoon['ID'], dNet)
        if lstHitInfo:
            return 1
        dCartoon['Pierce'] = 0
        dCartoon['Over'] = 1
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if oSkill.m_CheckType & CRT_CHECK_SERVER or dCartoon['Pierce'] <= 0:
            iOver = 1
        else:
            dClient = oSkill.m_NetReceive[iNodeID]
            if 'Over' in dClient and dClient['Over'] == 1:
                iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['LastPos']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos
        oSkill.m_Collect['lstVLST'] = dCartoon['AllVLST']

    CollectSkillInfo = classmethod(CollectSkillInfo)


def CheckDistance(oSkill, dCartoon):
    iCheck = 0
    if dCartoon['KeepStart']:
        fCheckDistance = dCartoon['DiffDistance']
        vStart = dCartoon['Start']
    elif dCartoon['Pierce'] == dCartoon['InitPierce']:
        fCheckDistance = dCartoon['AttDistance']
    else:
        fCheckDistance = dCartoon['DiffDistance']
    vStart = dCartoon['CurPos']
    if cl_math.CheckDistance3D(dCartoon['LastPos'], vStart, fCheckDistance):
        iCheck = 1
    return iCheck

