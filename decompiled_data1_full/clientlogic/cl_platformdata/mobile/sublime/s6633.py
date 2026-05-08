# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6633.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6633.pyc
# Source Generated with Decompyle++
# File: s6633.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6633
    m_Name = '青燕-充能射击'
    m_LimitHero = 206
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6632: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 206,
                        'max': 3 } }],
            'WarReward': [] } }

