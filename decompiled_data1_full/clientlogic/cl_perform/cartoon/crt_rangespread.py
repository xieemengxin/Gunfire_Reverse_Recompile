# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_rangespread.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_rangespread.pyc
# Source Generated with Decompyle++
# File: crt_rangespread.pyc (Python 3.6)

from cl_commondefines import VICTIM_STATE_VALID, VICTIM_STATE_HIT, OBJ_ENEMY, MONSTER_PART_UNTAGGED, CRT_CHECK_SERVER, ATT_SHAPE_SPHERE, HITPART_DIRECTPOS
from cl_only import Second2Frame
from cl_pxlayer import PXMASK_MONSTER
import cllib.lib_cartoon as cartooncheck
import cl_math
from .mobject import CBaseCartoon

class RangeSpreadCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
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
            cls.CollectSkillInfo(oSkill, dCartoon)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, vStart, playerID, iPierce, iTargetRepeat, fRadius, *args):
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['Start'] = vStart
        dCartoon['Center'] = vStart
        dCartoon['Pierce'] = iPierce
        dCartoon['Radius'] = fRadius
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Direction' in dClient:
            dNet['Direction'] = dClient['Direction']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = dClient['LockTarget']
        iHit = 0
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            for vHitPos, _, iVictim, _ in dClient['Ray']:
                oVictim = oSkill.m_Game.GetObject(iVictim)
                if not oVictim:
                    continue
                dCartoon['CurPos'] = vHitPos
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= 1
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': MONSTER_PART_UNTAGGED }
                    lstHitInfo.append(dHitInfo)
                    dCartoon['Final'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['LastVLST'] = lstVLST
            oSkill.m_Update['LastVLST'] = lstVLST
        oSkill.Send(iNodeID, dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, playerID, iPierce, iTargetRepeat, fRadius, fTotalTime, *args):
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['Start'] = vStart
        dCartoon['FirstTarget'] = playerID
        dCartoon['Center'] = vStart
        dCartoon['Pierce'] = iPierce
        dCartoon['TargetRepeat'] = iTargetRepeat
        dCartoon['Radius'] = 10
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True
        dCartoon['IntervalFrame'] = Second2Frame(fTotalTime / iPierce)
        dCartoon['TotalFrame'] = iPierce * dCartoon['IntervalFrame']
        dCartoon['AllVLST'] = []

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        dCartoon['Pierce'] -= 1
        iTarget = 0
        iFirstTarget = dCartoon['FirstTarget']
        if iFirstTarget:
            iTarget = iFirstTarget
            dCartoon['FirstTarget'] = 0
        else:
            vStart = dCartoon['CurPos']
            lstArgs = [
                vStart,
                dCartoon['Radius']]
            dQArgs = {
                'Mask': PXMASK_MONSTER,
                'BlockMask': 0 }
            lstHit = cl_math.GetAttackTargetList(oGame, oSkill.m_Base['Scene'], ATT_SHAPE_SPHERE, lstArgs, dQArgs)
            lstValid = []
            for iVictim in lstHit:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT and dCartoon['TargetRepeat']:
                        lstValid.append(iVictim)
                        continue
            
            if lstValid:
                iTarget = lstValid[oGame.Random(len(lstValid))]
        if iTarget:
            oTarget = oGame.GetObject(iTarget)
            vTarget = oTarget.GetPos() if oTarget else dCartoon['CurPos']
            dCartoon['AllVLST'].append(iTarget)
            lstVictim = [
                iTarget]
            dHitInfo = {
                'Victim': iTarget,
                'HitArea': HITPART_DIRECTPOS }
            oSkill.m_Update['LastVLST'] = lstVictim
            oSkill.m_Update['HitInfo'] = [
                dHitInfo]
            dNet = {
                'LockTarget': [
                    iTarget],
                'LastVLST': lstVictim,
                'Direction': cl_math.Vec3Minus(vTarget, dCartoon['CurPos']) }
            dCartoon['CurPos'] = vTarget
            oSkill.Send(dCartoon['ID'], dNet)
            return 1
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        iRemainTimes = max(0, dCartoon['Pierce'])
        oSkill.m_Collect['RemainTimes'] = iRemainTimes

    CollectSkillInfo = classmethod(CollectSkillInfo)

