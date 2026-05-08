# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6634.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6634.pyc
# Source Generated with Decompyle++
# File: s6634.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6634
    m_Name = '青燕-技能强化'
    m_LimitHero = 206
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 45,
            'CashCost': 125,
            'Depend': {
                6633: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 206,
                        'max': 4 } }],
            'WarReward': [] } }

