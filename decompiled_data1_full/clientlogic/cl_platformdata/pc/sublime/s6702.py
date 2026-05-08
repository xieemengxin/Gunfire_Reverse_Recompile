# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6702.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6702.pyc
# Source Generated with Decompyle++
# File: s6702.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6702
    m_Name = '千岁-游身若水'
    m_LimitHero = 213
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 35,
            'Depend': {
                6701: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 213,
                        'max': 2 } }],
            'WarReward': [] } }

