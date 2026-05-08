# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_waitdata.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_waitdata.pyc
# Source Generated with Decompyle++
# File: crt_waitdata.pyc (Python 3.6)

from .mobject import CBaseCartoon
import cl_perform.net as pfnet

class WaitDataCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iEndTime, iSendTrigger, dClientArg):
        dCartoon['CanSendTrigger'] = iSendTrigger

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 1

    HitTargetClient = classmethod(HitTargetClient)
    
    def OnArrive(cls, oSkill, dCartoon):
        if not dCartoon['CanSendTrigger']:
            return None
        iNodeID = dCartoon['ID']
        Send(oSkill, iNodeID, {
            'Trigger': 1 })
        cls.Trigger(oSkill)

    OnArrive = classmethod(OnArrive)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        Send(oSkill, iNodeID, {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)


def Send(oSkill, iNodeID, dNet):
    pfnet.GS2CClientSkillTrigger(oSkill, {
        iNodeID: dNet }, [
        oSkill.m_Base['netexclude']])
    oSkill.Send(iNodeID, dNet)

