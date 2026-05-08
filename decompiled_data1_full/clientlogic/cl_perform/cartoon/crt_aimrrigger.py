# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_aimrrigger.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_aimrrigger.pyc
# Source Generated with Decompyle++
# File: crt_aimrrigger.pyc (Python 3.6)

from .mobject import CBaseCartoon
from cl_object.logging import OtherLog
import cl_math

class AimTriggerCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    m_TimeoutTime = 750
    m_Mistake = 1
    
    def IsOver(cls, oSkill, dCartoon):
        if oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame'] >= cls.m_TimeoutTime:
            oAttack = oSkill.GetAttack()
            iPlayerID = oAttack.m_PlayerID if oAttack else 0
            OtherLog.Debug('%s %s aimtrigger timeout' % (oSkill.m_Game.m_ID, iPlayerID))
            dCartoon['Over'] = 1
        if 'Over' in dCartoon:
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iTriggerAimTime, iCheckDis, *args, **kwargs):
        dCartoon['TriggerAimTime'] = iTriggerAimTime
        dCartoon['CheckDis'] = iCheckDis
        dCartoon['NowAim'] = 0
        oSkill.Call_Out(cls.m_TimeoutTime, dCartoon['ID'])

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        lstVLST = []
        vAttack = oAttack.GetPos()
        if 'LockTarget' in dClient:
            lstLockTarget = dClient['LockTarget']
            if not lstLockTarget:
                return -1
            iTriggerAimTime = dCartoon['TriggerAimTime']
            oGame = oSkill.m_Game
            for iTargetID in lstLockTarget:
                oTarget = oGame.GetObject(iTargetID)
                if not oTarget:
                    continue
                vTarget = oTarget.GetPos()
                if cl_math.CalDistance3D(vTarget, vAttack) > dCartoon['CheckDis'] + cls.m_Mistake:
                    OtherLog.Debug('%s %s aimtrigger check dis fail %s %s' % (oGame.m_ID, oTarget.m_SID, vTarget, vAttack))
                    continue
                if oGame.GetObject(iTargetID):
                    dCartoon['NowAim'] += 1
                    lstVLST.append(iTargetID)
                if dCartoon['NowAim'] >= iTriggerAimTime:
                    dCartoon['Over'] = 1
                    break
            
            if lstVLST:
                oSkill.m_Custom['LockTarget'] = lstVLST
                cls.Trigger(oSkill)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)

