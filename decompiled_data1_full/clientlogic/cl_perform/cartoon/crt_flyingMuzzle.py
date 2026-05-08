# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_flyingMuzzle.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_flyingMuzzle.pyc
# Source Generated with Decompyle++
# File: crt_flyingMuzzle.pyc (Python 3.6)

from cl_only import Time2Frame
from .mobject import CBaseCartoon

class FlyingMuzzleCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['StartFireFrame'], dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, iTime, vDir, iEndDelayTime, iStartFireTime, iFiringTimes, iFiringInterval, fAngle, fDistance, iTarget, sType, tDefRotate, vTargetPos, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Time'] = iTime
        dCartoon['StartFireFrame'] = Time2Frame(iStartFireTime)
        dCartoon['FiringTimes'] = iFiringTimes
        dCartoon['IntervalFrame'] = Time2Frame(iFiringInterval)
        dCartoon['Final'] = EndPos
        dCartoon['Target'] = [
            iTarget]
        dCartoon['vTargetPos'] = vTargetPos
        dCartoon['Direction'] = vDir
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'Time': dCartoon['Time'],
            'LockTarget': dCartoon['Target'],
            'CheckStart': dCartoon['vTargetPos'],
            'Count': iStartFireTime,
            'Direction': dCartoon['Direction'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def OnArrive(cls, oSkill, dCartoon):
        cls.Trigger(oSkill)
        dNet = {
            'Trigger': 1 }
        oSkill.Send(dCartoon['ID'], dNet)

    OnArrive = classmethod(OnArrive)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['StartFrame'] + dCartoon['StartFireFrame'] + dCartoon['IntervalFrame'] * dCartoon['FiringTimes'] <= oSkill.m_Game.GetFrameNum():
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)

