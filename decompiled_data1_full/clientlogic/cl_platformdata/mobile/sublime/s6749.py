# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6749.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6749.pyc
# Source Generated with Decompyle++
# File: s6749.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6749
    m_Name = '#NT#小玖-急救模块'
    m_LimitHero = 222
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 45,
            'CashCost': 125,
            'Depend': {
                6748: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 222,
                        'max': 4 } }],
            'WarReward': [] } }

