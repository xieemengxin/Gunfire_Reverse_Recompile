# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_splitarrow.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_splitarrow.pyc
# Source Generated with Decompyle++
# File: crt_splitarrow.pyc (Python 3.6)

from cl_only import Second2Frame, GAME_FRAME_SECOND
from cl_commondefines import OBJ_ALL
from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from .crt_raycast import RayCastCartoon
import cllib.lib_cartoon as cartooncheck

class SplitArrowCartoon(RayCastCartoon):
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, iSplitNum, fSpeed, lstOffset, fmaxAngle, fLockAngle, fLockDis, fLineDis, fDistance, fCloseDis, fNoTarMaxAngle1, fNoTarMaxAngle2, targettype = OBJ_ALL, **kwargs):
        dCartoon['Pierce'] = iPierce * iSplitNum
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Start'] = dClient['Start']
        dCartoon['End'] = dClient['End']
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'Direction': dClient['Direction'],
            'Count': dClient['Count'] }
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = Second2Frame(fDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dCartoon['PierceStatic'] = True

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iHit = 0
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
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
                    dCartoon['Pierce'] -= 1
                elif iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstVLST.append(iVictim)
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                
                dCartoon['CurPos'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'Ray': lstSend }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)

