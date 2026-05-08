# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6773.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6773.pyc
# Source Generated with Decompyle++
# File: s6773.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6773
    m_Name = '苍玦-劫印传灯'
    m_LimitHero = 220
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6772: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 220,
                        'max': 3 } }],
            'WarReward': [] } }

