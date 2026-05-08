# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6645.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6645.pyc
# Source Generated with Decompyle++
# File: s6645.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6645
    m_Name = '雷落-雷牵电引'
    m_LimitHero = 207
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6644: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 207,
                        'max': 5 } }],
            'WarReward': [] } }

