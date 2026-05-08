# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_liquidthrowcartoon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_liquidthrowcartoon.pyc
# Source Generated with Decompyle++
# File: crt_liquidthrowcartoon.pyc (Python 3.6)

from cl_commondefines import VICTIM_STATE_HIT, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, MONSTER_PART_SHIELD
from .mobject import CBaseCartoon
from cl_object.logging import SkillLog
from . import ContinuousCostBullet
import cl_msgcenter
MAX_COUNT_CHANGE = 2

class LiquidThrowCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return 1
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Disable(cls, oSkill, dCartoon):
        super().Disable(oSkill, dCartoon)
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTINUESHOOT_END, oAttack, { }, iSub = -1)

    Disable = classmethod(Disable)
    
    def InitTraceClient(cls, oSkill, dCartoon, targettype, *args, **kwargs):
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dCartoon['Count'] = 0
        dCartoon['TargetType'] = targettype
        dCartoon['Frame'] = oSkill.m_Game.GetFrameNum()

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            dCartoon['Over'] = 1
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        iHit = 0
        dNet = { }
        if 'Count' in dClient:
            iLastCount = dCartoon['Count']
            if dClient['Count'] <= iLastCount:
                return 0
            iNowFrame = oSkill.m_Game.GetFrameNum()
            iCountChange = dClient['Count'] - iLastCount
            iChangeFrame = iNowFrame - dCartoon['Frame'] if iLastCount != 0 else 1
            if iChangeFrame == 0:
                return 0
            iMaxCountChange = MAX_COUNT_CHANGE * iChangeFrame
            oAttack = oSkill.GetAttack()
            if iCountChange > iMaxCountChange:
                SkillLog.Debug('%s, %s liquidthrowcartoon count err: %s' % (oAttack.m_Game.m_ID, oAttack.m_PlayerID, dClient['Count']))
                iCountChange = iMaxCountChange
            dCartoon['Count'] = iLastCount + iCountChange
            dCartoon['Frame'] = iNowFrame
            pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
            if not pfobj:
                SkillLog.Debug('%s, %s liquidthrowcartoon not pfobj: %s; %s' % (oAttack.m_Game.m_ID, oAttack.m_PlayerID, oSkill.m_Base['Weapon'], oAttack.m_WieldCon.m_ItemSID))
                return 0
            for _ in range(iCountChange):
                ContinuousCostBullet(oSkill, iNodeID)
            
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['CurPos'] = vHitPos
                    continue
                if not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT:
                        dCartoon['AllVLST'].append(iVictim)
                        lstVLST.append(iVictim)
                        dHitInfo = {
                            'Victim': iVictim,
                            'HitPos': vHitPos,
                            'HitArea': iHitPart,
                            'Normal': vNormal }
                        lstHitInfo.append(dHitInfo)
                        dCartoon['AllHitInfo'].append(dHitInfo)
                        dCartoon['CurPos'] = vHitPos
                        continue
            
            if 'CurPos' in dCartoon:
                oSkill.m_Update['LastVLST'] = lstVLST
                oSkill.m_Update['HitInfo'] = lstHitInfo
                oSkill.m_Update['CurPos'] = dCartoon['CurPos']
                dNet['Ray'] = dClient['Ray']
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dNet['Trigger'] = 1
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        if dNet:
            oSkill.Send(iNodeID, dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

