# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_jumpcrash.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_jumpcrash.pyc
# Source Generated with Decompyle++
# File: crt_jumpcrash.pyc (Python 3.6)

from .crt_winkpos import ExitDashCheck
from .mobject import CBaseCartoon

class JumpCrashCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def IsOver(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, horizontalSpeed, upSpeed, *args, **kwargs):
        dCartoon['HorizontalSpeed'] = horizontalSpeed
        dCartoon['UpSpeed'] = upSpeed
        oAttack = oSkill.GetAttack()
        dCtrlCheck = {
            'ActNum': oSkill.m_Base['ActNum'],
            'CartoonID': dCartoon['ID'],
            'ExitCB': ExitDashCheck,
            'UpSpeed': dCartoon['UpSpeed'],
            'Second': 1 }
        oAttack.m_MoveCtrl.AddDashCtrlCheck(oAttack, dCtrlCheck)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iHit = 0
        if iNodeID not in oSkill.m_NetReceive:
            return iHit
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Trigger' in dClient:
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)

