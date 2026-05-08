# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6642.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6642.pyc
# Source Generated with Decompyle++
# File: s6642.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6642
    m_Name = '雷落-天赋异禀'
    m_LimitHero = 207
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 35,
            'Depend': {
                6641: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 207,
                        'max': 2 } }],
            'WarReward': [] } }

