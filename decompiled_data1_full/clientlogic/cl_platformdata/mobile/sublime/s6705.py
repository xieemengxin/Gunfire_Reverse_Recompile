# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6705.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6705.pyc
# Source Generated with Decompyle++
# File: s6705.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6705
    m_Name = '千岁-横冲直撞'
    m_LimitHero = 213
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6704: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 213,
                        'max': 5 } }],
            'WarReward': [] } }

