# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_sublimation/mobject.pyc
# RelativePath: clientlogic/cl_sublimation/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)


class CSublimation(object):
    m_SID = 0
    m_Name = '升华A'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 1,
            'CashCost': 10,
            'Depend': {
                1001: 1,
                1002: 1,
                1003: 1 },
            'TotalDependLevel': 4,
            'Reward': [],
            'WarReward': [] } }
    
    def GetLevelInfo(cls, iTargerLevel):
        return cls.m_LevelInfo.get(iTargerLevel, { })

    GetLevelInfo = classmethod(GetLevelInfo)

