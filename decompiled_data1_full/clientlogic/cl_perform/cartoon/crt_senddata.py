# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_senddata.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_senddata.pyc
# Source Generated with Decompyle++
# File: crt_senddata.pyc (Python 3.6)

from .mobject import CBaseCartoon

class SendDataCartoon(CBaseCartoon):
    m_NeedCtrlNet = 1
    m_CutClient = 0
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        oSkill.Send(dCartoon['ID'], {
            'Over': 1 })
        return 1

    IsOver = classmethod(IsOver)

