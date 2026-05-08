# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6685.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6685.pyc
# Source Generated with Decompyle++
# File: s6685.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6685
    m_Name = '妖星-5'
    m_LimitHero = 211
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 410,
            'Depend': {
                6684: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 211,
                        'max': 5 } }],
            'WarReward': [] } }

