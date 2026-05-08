# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6635.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6635.pyc
# Source Generated with Decompyle++
# File: s6635.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6635
    m_Name = '青燕-紧急防护'
    m_LimitHero = 206
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6634: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 206,
                        'max': 5 } }],
            'WarReward': [] } }

