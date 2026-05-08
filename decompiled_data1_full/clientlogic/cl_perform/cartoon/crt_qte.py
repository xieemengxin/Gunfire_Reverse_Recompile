# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_qte.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_qte.pyc
# Source Generated with Decompyle++
# File: crt_qte.pyc (Python 3.6)

from cl_only import GAME_FRAME_TIME
from .mobject import CBaseCartoon
CHECK_FRAME = 2

class QTECartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, iFrontTime, iTriggerTime, iRearTime):
        iNodeID = dCartoon['ID']
        dCartoon['FrontTime'] = iFrontTime
        dCartoon['TriggerTime'] = iTriggerTime
        dCartoon['RearTime'] = iRearTime
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['StartFrame'] = dClient['Frame']
        dNet = {
            'Frame': dClient['Frame'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID] if iNodeID in oSkill.m_NetReceive else { }
        if 'Frame' in dClient and 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dCartoon['Over'] = 1
        else:
            iCurFrame = oSkill.m_Game.GetFrameNum()
            iFinishFrame = dCartoon['StartFrame'] + (dCartoon['FrontTime'] + dCartoon['TriggerTime'] + dCartoon['RearTime']) / GAME_FRAME_TIME
            if iCurFrame >= iFinishFrame:
                dCartoon['Over'] = 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            iOver = 1
        elif 'Over' in dCartoon:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)

