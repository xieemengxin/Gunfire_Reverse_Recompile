# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_traceline.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_traceline.pyc
# Source Generated with Decompyle++
# File: crt_traceline.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, VICTIM_STATE_VALID
import cl_math
import cllib.lib_cartoon as cartooncheck
import cl_msgcenter
from . import ContinuousCostBullet
from .mobject import CBaseCartoon

class TraceLineCartoon(CBaseCartoon):
    m_ContinueShoot = 1
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Disable(cls, oSkill, dCartoon):
        super().Disable(oSkill, dCartoon)
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTINUESHOOT_END, oAttack, { }, iSub = -1)

    Disable = classmethod(Disable)
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDistance, targettype = OBJ_ALL, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['TargetType'] = targettype
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
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
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iAttack = oSkill.m_Base['AID']
        if 'Start' in dClient:
            vStart = dClient['Start']
            dCartoon['Start'] = vStart
            dCartoon['CurPos'] = vStart
        else:
            oAttack = oSkill.m_Game.GetObject(iAttack)
            vPos = oAttack.GetPos()
            vUpdate = (vPos[0], vPos[1] + oAttack.m_ModelHeight * 0.85, vPos[2])
            dCartoon['Start'] = vUpdate
            dCartoon['CurPos'] = vUpdate
        if 'End' in dClient:
            dNet['End'] = dClient['End']
        if 'Ray' in dClient and 'Trigger' in dClient:
            iHit = 1
            lstRay = dClient['Ray']
            iPierce = dCartoon['Pierce']
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    iPierce -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    lstVLST.append(iVictim)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                if iPierce <= 0:
                    dCartoon['CurPos'] = vHitPos
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            cls.CollectSkillInfo(oSkill, dCartoon)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vEnd, iPierce, fDistance, targettype = OBJ_ALL, **kwargs):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            dClient = oSkill.m_NetReceive[iNodeID]
            if 'End' in dClient and cl_math.CalDistance3D(dClient['End'], dCartoon['Start']) < dCartoon['Distance']:
                dCartoon['Final'] = dClient['End']
            else:
                dCartoon['Final'] = dCartoon['Start']
                if cl_math.IsEqual(dCartoon['Start'], dCartoon['End']):
                    oSkill.LogCheckErr('start equal end %s' % (dCartoon['Start'],))
            iOver = 1
        else:
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            if not cl_math.CheckDistance3D(oAttack.GetPos(), dCartoon['CurPos'], dCartoon['Distance'] + 2):
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

