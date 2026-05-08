# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6623.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6623.pyc
# Source Generated with Decompyle++
# File: s6623.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6623
    m_Name = '獒乌-手雷强化'
    m_LimitHero = 201
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6622: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 201,
                        'max': 3 } }],
            'WarReward': [] } }

