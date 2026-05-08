# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_powerjump.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_powerjump.pyc
# Source Generated with Decompyle++
# File: crt_powerjump.pyc (Python 3.6)

import cl_math
from .crt_winkpos import ExitDashCheck
from .mobject import CBaseCartoon
from cl_commondefines import CRT_CHECK_CLIENT

class PowerJumpCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, horizontalSpeed, maxDistance, *args, **kwargs):
        dCartoon['HorizontalSpeed'] = horizontalSpeed
        dCartoon['MaxDistance'] = maxDistance
        fSecond = maxDistance / horizontalSpeed
        oAttack = oSkill.GetAttack()
        dCtrlCheck = {
            'ActNum': oSkill.m_Base['ActNum'],
            'CartoonID': dCartoon['ID'],
            'ExitCB': ExitDashCheck,
            'UpSpeed': 1,
            'Second': fSecond }
        oAttack.m_MoveCtrl.AddDashCtrlCheck(oAttack, dCtrlCheck)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iHit = 0
        if iNodeID not in oSkill.m_NetReceive:
            return iHit
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        dCartoon['Over'] = 1
        dNet = {
            'Over': 1 }
        oSkill.Send(dCartoon['ID'], dNet)
        return 0

    HitTargetServer = classmethod(HitTargetServer)

