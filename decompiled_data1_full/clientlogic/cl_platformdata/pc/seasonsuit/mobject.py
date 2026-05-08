# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/mobject.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)


class CBaseSeasonSuitData(object):
    m_SID = 0
    m_Name = ''
    m_Condition = { }
    m_CondSID = { }
    m_CondFunc = { }
    m_Action = { }
    m_RemoveAction = { }
    m_ForeverCondition = { }
    m_MaxGrade = 1
    m_GradeInfo = { }
    m_CoreRelic = 0
    
    def GetCondFunc(cls, iSuitLevel):
        return cls.m_CondFunc[iSuitLevel]

    GetCondFunc = classmethod(GetCondFunc)
    
    def GetAction(cls, iSuitLevel):
        return cls.m_Action[iSuitLevel]

    GetAction = classmethod(GetAction)
    
    def GetRemoveAction(cls, iSuitLevel):
        return cls.m_RemoveAction[iSuitLevel]

    GetRemoveAction = classmethod(GetRemoveAction)
    
    def GetMaxGrade(cls):
        return cls.m_MaxGrade

    GetMaxGrade = classmethod(GetMaxGrade)

