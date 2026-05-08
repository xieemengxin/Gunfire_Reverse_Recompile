# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6621.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6621.pyc
# Source Generated with Decompyle++
# File: s6621.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6621
    m_Name = '獒乌-携弹强化'
    m_LimitHero = 201
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
                        'sid': 201,
                        'max': 1 } }],
            'WarReward': [] } }

