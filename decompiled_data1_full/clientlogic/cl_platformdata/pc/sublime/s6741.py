# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6741.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6741.pyc
# Source Generated with Decompyle++
# File: s6741.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6741
    m_Name = '小玖-加固装甲'
    m_LimitHero = 217
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
                        'sid': 217,
                        'max': 1 } }],
            'WarReward': [] } }

