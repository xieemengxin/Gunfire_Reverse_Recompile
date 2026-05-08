# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_timerbreak.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_timerbreak.pyc
# Source Generated with Decompyle++
# File: crt_timerbreak.pyc (Python 3.6)

from cl_only import Time2Frame
import cl_action
from .mobject import CBaseCartoon

class TimerWithBreakCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    m_CurClient = 0
    
    def InitTraceClient(cls, oSkill, dCartoon, waitTime, triggerTime):
        dCartoon['WaitFrame'] = Time2Frame(waitTime)
        dCartoon['CurTimes'] = 0
        dCartoon['TriggerTimes'] = max(triggerTime, 1)

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, waitTime, triggerTime):
        dCartoon['WaitFrame'] = Time2Frame
        dCartoon['CurTimes'] = 0
        dCartoon['TriggerTimes'] = max(triggerTime, 1)

    InitTraceServer = classmethod(InitTraceServer)
    
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
        oBreakCondition = cl_action.CheckReloadFullBullet
        if not oBreakCondition(oSkill):
            cls.Trigger(oSkill)
            oSkill.Send(dCartoon['ID'], {
                'Count': dCartoon['CurTimes'] })

    OnArrive = classmethod(OnArrive)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        oBreakCondition = cl_action.CheckReloadFullBullet
        if iNodeID in oSkill.m_NetReceive and 'Over' in oSkill.m_NetReceive[iNodeID]:
            iOver = 1
        elif oBreakCondition(oSkill):
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return iOver
        return iOver

    IsOver = classmethod(IsOver)

