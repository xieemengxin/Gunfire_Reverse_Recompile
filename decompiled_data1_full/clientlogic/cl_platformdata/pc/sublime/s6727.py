# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6727.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6727.pyc
# Source Generated with Decompyle++
# File: s6727.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6727
    m_Name = '虞火-灵火神兵'
    m_LimitHero = 217
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 60,
            'Depend': {
                6721: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 217,
                        'max': 2 } }],
            'WarReward': [] } }

