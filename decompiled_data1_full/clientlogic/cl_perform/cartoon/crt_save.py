# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_save.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_save.pyc
# Source Generated with Decompyle++
# File: crt_save.pyc (Python 3.6)

from cl_only import Time2Frame
from .mobject import CBaseCartoon

class SaveCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, iIntervalTime, iMaxChargeLevel, effect = 0, lessSpeed = 100, showui = True):
        dCartoon['IntervalFrame'] = Time2Frame(int(iIntervalTime))
        dCartoon['MaxChargeLevel'] = iMaxChargeLevel

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            oSkill.Send(iNodeID, dClient)
            return 1
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dCartoon['Trigger'] = 1
            oSkill.Send(iNodeID, dClient)
            return 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, iIntervalTime, iMaxchargeLevel, effect = 0, lessSpeed = 100, showui = True):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)

