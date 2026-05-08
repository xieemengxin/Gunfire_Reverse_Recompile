# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6682.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6682.pyc
# Source Generated with Decompyle++
# File: s6682.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6682
    m_Name = '妖星-2'
    m_LimitHero = 211
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 60,
            'Depend': {
                6681: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 211,
                        'max': 2 } }],
            'WarReward': [] } }

