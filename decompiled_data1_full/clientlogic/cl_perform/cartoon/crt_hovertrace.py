# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_hovertrace.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_hovertrace.pyc
# Source Generated with Decompyle++
# File: crt_hovertrace.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, VICTIM_STATE_HIT, WARRIOR_PERFORM, WARRIOR_OBSTACLE_NORMAL, OBSTACLE_JAR
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class HoverTraceCartoon(CBaseCartoon):
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Over' not in dClient:
            return 0
        dNet['Over'] = 1
        oSkill.Send(iNodeID, dNet)
        oSkill.m_Collect['Pierce'] = 0
        return 1

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, vHoverDev, fHoverChangeAngle, iPierce, fRayCastDis, fRayCastAngle, fRayCastHeight, *args, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['ChangeAngle'] = fHoverChangeAngle
        dCartoon['Distance'] = fRayCastDis
        dCartoon['Angle'] = fRayCastAngle
        dCartoon['Height'] = fRayCastHeight
        dCartoon['MaxSpeed'] = kwargs['maxSpeed'] if 'maxSpeed' in kwargs else 0
        dCartoon['MinSpeed'] = kwargs['minSpeed'] if 'minSpeed' in kwargs else 0
        dCartoon['TargetType'] = kwargs['targettype'] if 'targettype' in kwargs else OBJ_ALL
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dNet = { }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)
        dCartoon['PierceStatic'] = True
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        oSkill.m_Collect['MaxDistance'] = kwargs['maxBuffDis'] if 'maxBuffDis' in kwargs else 0
        oSkill.m_Collect['BaseBullet'] = 1

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Start' in dClient:
            dCartoon['CurPos'] = dClient['Start']
            dNet['Start'] = dClient['Start']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            oAttack = oSkill.GetAttack()
            pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                elif not iVictimState == VICTIM_STATE_VALID:
                    pass
                oSkill.m_Cache['Distance'] = dClient['Distance'] if iVictimState == VICTIM_STATE_HIT or 'Distance' in dClient else 0
                dCartoon['AllVLST'].append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitPart }
                lstVLST.append(iVictim)
                lstHitInfo.append(dHitInfo)
                dCartoon['AllHitInfo'].append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                pfobj.CostBullet(oAttack, oSkill)
                dCartoon['CurPos'] = vHitPos
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def GetVictimPierceCost(cls, oSkill, iVictim):
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if not oVictim:
            return 0
        if oVictim.m_FightType == WARRIOR_OBSTACLE_NORMAL and OBSTACLE_JAR in oVictim.m_ClassifyList:
            return 0
        if oVictim.m_FightType == WARRIOR_PERFORM:
            return 0
        return 1

    GetVictimPierceCost = classmethod(GetVictimPierceCost)


def CheckHitSpeed(oSkill, dCartoon, vHitPos):
    pass

