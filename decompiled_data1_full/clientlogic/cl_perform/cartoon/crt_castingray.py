# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_castingray.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_castingray.pyc
# Source Generated with Decompyle++
# File: crt_castingray.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, VICTIM_STATE_VALID
from cl_object.logging import SkillLog
import cl_math
import cl_gamedebug as debug
import cllib.lib_cartoon as cartooncheck
import cl_msgcenter
from . import ContinuousCostBullet
from .mobject import CBaseCartoon

class CastingRayCartoon(CBaseCartoon):
    m_CutClient = 2
    m_ContinueShoot = 1
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Disable(cls, oSkill, dCartoon):
        super().Disable(oSkill, dCartoon)
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTINUESHOOT_END, oAttack, { }, iSub = -1)

    Disable = classmethod(Disable)
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fMaxDistance, targettype = OBJ_ALL, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['MaxDistance'] = fMaxDistance
        dCartoon['Distance'] = fMaxDistance
        dCartoon['TargetType'] = targettype
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'End' not in dClient:
            SkillLog.Alert('%s CastingRayCartoon not key End' % oSkill.m_Base['PFKey'])
            dCartoon['End'] = dClient['Start']
        else:
            dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        if not 'Trigger' in dClient and ContinuousCostBullet(oSkill, iNodeID):
            oSkill.Halt()
            return -1
        dNet = { }
        iHit = 0
        iPierce = dCartoon['Pierce']
        iAttack = oSkill.m_Base['AID']
        if 'Start' in dClient:
            vStart = dClient['Start']
            dCartoon['Start'] = vStart
        else:
            oAttack = oSkill.m_Game.GetObject(iAttack)
            vPos = oAttack.GetPos()
            vStart = (vPos[0], vPos[1] + oAttack.m_ModelHeight * 0.85, vPos[2])
        dNet['Start'] = vStart
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = dClient['LockTarget']
        if 'Distance' in dClient:
            fDistance = dClient['Distance']
            if fDistance < 0:
                fDistance = 0
            elif fDistance > dCartoon['MaxDistance']:
                dCartoon['Distance'] = dCartoon['MaxDistance']
            else:
                dCartoon['Distance'] = fDistance
            dNet['Distance'] = fDistance
        if 'Ray' in dClient and 'Trigger' in dClient:
            iHit = 1
            lstRay = dClient['Ray']
            lstVLST = []
            lstHitInfo = []
            lstSend = []
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID or iVictim in lstVLST:
                    continue
                lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitPart }
                lstHitInfo.append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                dCartoon['CurPos'] = vHitPos
                iPierce -= cls.GetVictimPierceCost(oSkill, iVictim)
                if iPierce <= 0:
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            cls.CollectSkillInfo(oSkill, dCartoon)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, iPierce, fDistance, targettype = OBJ_ALL, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != StartPos:
            dNet['Start'] = StartPos
        oSkill.Send(dCartoon['ID'], dNet)
        if oSkill.m_Game.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = StartPos
            (tx, ty, tz) = EndPos
            debug.ClearDebugLine(oSkill.m_Game, debug.LINE_TILE)
            debug.DebugLine(oSkill.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if not oSkill.m_Base:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        iOver = 0
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            dClient = oSkill.m_NetReceive[iNodeID]
            if 'End' in dClient:
                dCartoon['Final'] = dClient['End']
            elif not cl_math.IsEqual(dCartoon['Start'], dCartoon['End']):
                dCartoon['Final'] = cl_math.Vec3DisplacePos(dCartoon['Start'], dCartoon['End'], dCartoon['Distance'])
            else:
                dCartoon['Final'] = dCartoon['Start']
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

