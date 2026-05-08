# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_spiralray.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_spiralray.pyc
# Source Generated with Decompyle++
# File: crt_spiralray.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, Second2Frame
from cl_commondefines import OBJ_ALL, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, VICTIM_STATE_HIT
from cl_object.logging import SkillLog
import cl_math
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class SpiralRayCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, fRadius, fSpeed, fStartAngle, fAngleSpeed, fDistance, iPierce, targettype = OBJ_ALL, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['Radius'] = fRadius
        dCartoon['TargetType'] = targettype
        dCartoon['StartAngle'] = fStartAngle
        dCartoon['AnglePerFrame'] = fAngleSpeed * GAME_FRAME_SECOND
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = Second2Frame(fDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        if cl_math.IsZero(dCartoon['Start']) and cl_math.IsZero(dCartoon['End']):
            oAttack = oSkill.GetAttack()
            SkillLog.Error('%s skillposzero %s %s' % (oSkill.m_Game.m_ID, oAttack.m_PlayerID, oSkill.m_Base['PFKey']))
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Start' in dClient:
            dCartoon['CurPos'] = dClient['Start']
        dNet = { }
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
                    dCartoon['Pierce'] = 0
                elif not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT and cls.CheckValidDamage(dCartoon, iVictim, iHitPart):
                        dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                        dCartoon['AllVLST'].append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart }
                        lstHitInfo.append(dHitInfo)
                        dCartoon['AllHitInfo'].append(dHitInfo)
                        lstVLST.append(iVictim)
                        lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                        dCartoon['CurPos'] = vHitPos
                    
                if dCartoon['Pierce'] <= 0:
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'Ray': lstSend,
                'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
            oSkill.Send(dCartoon['ID'], dNet)
            cls.CollectSkillInfo(oSkill, dCartoon)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vEnd, fRadius, fSpeed, fStartAngle, fAngleSpeed, fDistance, iPierce, targettype = OBJ_ALL, **kwargs):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            dClient = oSkill.m_NetReceive[iNodeID]
            dCartoon['Final'] = cl_math.Vec3DisplacePos(dCartoon['Start'], dCartoon['End'], dCartoon['Distance'])
            if 'End' in dClient and cl_math.CheckDistance3D(dClient['End'], dCartoon['Final'], dCartoon['SpeedPerFrame'] + dCartoon['Radius']):
                dCartoon['Final'] = dClient['End']
            iOver = 1
        elif cl_math.VectorDot3D(cl_math.Vec3Minus(dCartoon['CurPos'], dCartoon['Start']), cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))) > dCartoon['Distance']:
            dCartoon['Final'] = dCartoon['CurPos']
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

