# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_doubleclickuse.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_doubleclickuse.pyc
# Source Generated with Decompyle++
# File: crt_doubleclickuse.pyc (Python 3.6)

from cl_only import Time2Frame
from .mobject import CBaseCartoon

class DoubleClickUseCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame'] >= dCartoon['MaxWaitFrame']:
            dCartoon['Over'] = 1
        if 'Over' in dCartoon:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, maxWaitTime, *args, **kwargs):
        iMaxWaitFrame = Time2Frame(maxWaitTime)
        dCartoon['MaxWaitFrame'] = iMaxWaitFrame
        oSkill.Call_Out(iMaxWaitFrame, dCartoon['ID'])

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            oSkill.m_Collect['End'] = dClient['End'] if 'End' in dClient else dCartoon['Start']
            oSkill.m_Collect['TargetID'] = dClient['LastVLST'][0] if 'LastVLST' in dClient and dClient['LastVLST'] else 0
            oSkill.Send(dCartoon['ID'], dClient)
            return 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)

