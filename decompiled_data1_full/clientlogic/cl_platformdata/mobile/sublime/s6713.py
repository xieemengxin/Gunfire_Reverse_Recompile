# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6713.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6713.pyc
# Source Generated with Decompyle++
# File: s6713.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6713
    m_Name = '行者-强效法器'
    m_LimitHero = 214
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6712: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 214,
                        'max': 3 } }],
            'WarReward': [] } }

