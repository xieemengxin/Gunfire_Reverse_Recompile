# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6652.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6652.pyc
# Source Generated with Decompyle++
# File: s6652.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6652
    m_Name = '狂狼-怒发冲冠'
    m_LimitHero = 208
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 60,
            'Depend': {
                6651: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 208,
                        'max': 2 } }],
            'WarReward': [] } }

