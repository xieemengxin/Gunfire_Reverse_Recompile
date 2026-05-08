# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatewhirling.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatewhirling.pyc
# Source Generated with Decompyle++
# File: crt_delegatewhirling.pyc (Python 3.6)

from cl_only import GAME_FRAME, GAME_FRAME_SECOND
from cl_commondefines import OBJ_ALL, VICTIM_STATE_VALID, VICTIM_STATE_HIT, WARRIOR_HERO, WARRIOR_BOSS
from cl_object.logging import WandLog
import cl_math
from .mobject import CBaseCartoon

class DelegateWhirlingCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 5 * GAME_FRAME
    
    def InitTraceServer(cls, oSkill, dCartoon, iCount, fOuntRadius, fInRadius, fHeight, iMaxCircle, vStartDir, *args, targettype = OBJ_ALL, **kwargs):
        dCartoon['TargetType'] = targettype
        dCartoon['Height'] = fHeight
        dCartoon['Radius'] = fOuntRadius
        dCartoon['Count'] = iCount
        oAttack = oSkill.GetAttack()
        dCartoon['CurPos'] = oAttack.GetPos()
        fSpeed = cls.GetAngleSpeed(oSkill)
        dCartoon['LeftAngle'] = iMaxCircle * 360 if fSpeed > 0 else -iMaxCircle * 360
        dCartoon['ClientSource'] = oAttack.m_ID if oAttack.m_FightType & WARRIOR_HERO else 0
        dCartoon['AngleSpeed'] = fSpeed
        iCurFrame = oSkill.m_Game.GetFrameNum()
        dCartoon['LastFrame'] = iCurFrame
        dCartoon['DealFrame'] = iCurFrame + (dCartoon['LeftAngle'] // dCartoon['AngleSpeed']) * GAME_FRAME + cls.m_WorldLineOutFrame
        dNet = {
            'Count': dCartoon['Count'],
            'Angle': dCartoon['AngleSpeed'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        elif oSkill.m_Game.GetFrameNum() >= dCartoon['DealFrame']:
            iOver = 1
        oAttack = oSkill.GetAttack()
        if not oAttack:
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        iCurSpeed = cls.GetAngleSpeed(oSkill)
        iCurFrame = oSkill.m_Game.GetFrameNum()
        iNodeID = dCartoon['ID']
        if dCartoon['AngleSpeed'] != iCurSpeed:
            dCartoon['LeftAngle'] -= dCartoon['AngleSpeed'] * (iCurFrame - dCartoon['LastFrame']) * GAME_FRAME_SECOND
            dCartoon['LastFrame'] = iCurFrame
            dCartoon['AngleSpeed'] = iCurSpeed
            dCartoon['DealFrame'] = iCurFrame + (dCartoon['LeftAngle'] // dCartoon['AngleSpeed']) * GAME_FRAME + cls.m_WorldLineOutFrame
            oSkill.Send(iNodeID, {
                'Angle': dCartoon['AngleSpeed'] })
        if iCurFrame + 1 not in oSkill.m_CallOut or iNodeID not in oSkill.m_CallOut[iCurFrame + 1]:
            oSkill.Call_Out(1, iNodeID)

    Restart = classmethod(Restart)
    
    def GetAngleSpeed(cls, oSkill):
        oAttack = oSkill.GetAttack()
        pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
        if not pfobj:
            return -1
        return pfobj.GetArgValue('AngleSpeed', -1)

    GetAngleSpeed = classmethod(GetAngleSpeed)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if dCartoon['ClientSource'] and dClient['Source'] != dCartoon['ClientSource']:
            return 0
        oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'])
        if not oAttack:
            return 0
        dNet = { }
        iHit = 0
        dCartoon['CurPos'] = oAttack.GetPos()
        if 'Ray' in dClient:
            iHit = 1
            lstRay = dClient['Ray']
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            oGame = oSkill.m_Game
            tCurPos = oAttack.GetPos()
            fCheckDis = dCartoon['Radius'] + 0.5
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if not iVictimState == VICTIM_STATE_VALID:
                    if (iVictimState == VICTIM_STATE_HIT or not dCartoon['ClientSource']) and dClient['Source'] != iVictim:
                        continue
                oVictim = oGame.GetObject(iVictim)
                if oVictim.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS and not cl_math.CheckDistance(tCurPos, oVictim.GetPos(), fCheckDis + oVictim.m_ModelRadius + oAttack.m_ModelRadius):
                    continue
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitPart }
                lstHitInfo.append(dHitInfo)
                lstVLST.append(iVictim)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

