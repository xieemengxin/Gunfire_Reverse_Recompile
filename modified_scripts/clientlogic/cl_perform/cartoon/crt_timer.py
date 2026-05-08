# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_timer.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_timer.pyc
# Source Generated with Decompyle++
# File: crt_timer.pyc (Python 3.6)

from cl_only import Time2Frame
from .mobject import CBaseCartoon
import cl_test as cl_customconfig

def FastTimerFrame(waitTime):
    iFrame = Time2Frame(waitTime)
    if iFrame <= 0:
        return 0
    fMul = cl_customconfig.GetTimerSpeedMultiplier()
    if fMul <= 1.0:
        return iFrame
    iNew = int(round(iFrame / fMul))
    if iNew <= 0:
        iNew = 1
    return iNew


class TimerCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    m_CutClient = 0
    
    def InitTraceClient(cls, oSkill, dCartoon, waitTime, triggerTimes):
        dCartoon['WaitFrame'] = FastTimerFrame(waitTime)
        dCartoon['CurTimes'] = 0
        dCartoon['TriggerTimes'] = max(triggerTimes, 1)

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, waitTime, triggerTimes):
        dCartoon['WaitFrame'] = FastTimerFrame(waitTime)
        dCartoon['CurTimes'] = 0
        dCartoon['TriggerTimes'] = max(triggerTimes, 1)

    InitTraceServer = classmethod(InitTraceServer)
    
    def Trace(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'], dCartoon['Casting'])

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive and 'Count' in oSkill.m_NetReceive[iNodeID] and oSkill.m_NetReceive[iNodeID]['Count'] > dCartoon['CurTimes']:
            return 1
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] * (dCartoon['CurTimes'] + 1) <= oSkill.m_Game.GetFrameNum():
            return 1
        return 0

    HitTarget = classmethod(HitTarget)
    
    def OnArrive(cls, oSkill, dCartoon):
        dCartoon['CurTimes'] += 1
        cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], {
            'Count': dCartoon['CurTimes'] })

    OnArrive = classmethod(OnArrive)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            iOver = 1
        elif dCartoon['TriggerTimes'] <= dCartoon['CurTimes']:
            iOver = 1
        elif 'DependState' in dCartoon:
            oAttack = oSkill.GetAttack()
            iDependState = dCartoon['DependState']
            if not oAttack and oAttack.m_State.GetItemBySID(iDependState):
                iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'], dCartoon['Casting'])

    Restart = classmethod(Restart)
