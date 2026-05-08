# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_mortarcharge.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_mortarcharge.pyc
# Source Generated with Decompyle++
# File: crt_mortarcharge.pyc (Python 3.6)

from cl_only import Time2Frame
from .crt_charge import ChargeCartoon, GetMaxChargeLevel

class MortarChargeCartoon(ChargeCartoon):
    m_NeedCtrlNet = 0
    
    def InitTraceClient(cls, oSkill, dCartoon, iIntervalTime, iMaxChargeLevel, iPerBulletCost, iAutoEnd, iAdvanceEnd, minChargeLevel = 0, effect = 0, halfEnd = 0, offsetTime = 0):
        dCartoon['IntervalFrame'] = Time2Frame(int(iIntervalTime))
        dCartoon['MaxChargeLevel'] = iMaxChargeLevel
        dCartoon['PerBulletCost'] = iPerBulletCost
        dCartoon['AutoEnd'] = iAutoEnd
        dCartoon['AdvanceEnd'] = iAdvanceEnd
        dCartoon['MinChargeLevel'] = minChargeLevel
        if iAutoEnd:
            iMaxFrame = dCartoon['IntervalFrame'] * iMaxChargeLevel
            dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iMaxFrame)

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, iIntervalTime, iMaxChargeLevel, iPerBulletCost, iAutoEnd, iAdvanceEnd, minChargeLevel = 0, effect = 0, halfEnd = 0, offsetTime = 0):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        iMaxChargeLevel = GetMaxChargeLevel(oSkill, dCartoon)
        iChargeLevel = min(dClient['Count'], iMaxChargeLevel)
        if 'Over' in dClient:
            if dCartoon['AdvanceEnd'] and iChargeLevel < dCartoon['MinChargeLevel']:
                oSkill.Halt('chargelevelless client:%d cur:%d min:%d' % (dClient['Count'], iChargeLevel, dCartoon['MinChargeLevel']))
                return -1
            dCartoon['Over'] = 1
            dCartoon['ChargeLevel'] = iChargeLevel
            oSkill.Send(dCartoon['ID'], dClient)
            return 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)

