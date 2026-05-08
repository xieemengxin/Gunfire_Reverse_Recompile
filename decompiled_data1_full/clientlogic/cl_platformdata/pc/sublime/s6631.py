# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6631.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6631.pyc
# Source Generated with Decompyle++
# File: s6631.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6631
    m_Name = '青燕-连续跃击'
    m_LimitHero = 206
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 0,
            'CashCost': 25,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 206,
                        'max': 1 } }],
            'WarReward': [] } }

