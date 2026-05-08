# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6644.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6644.pyc
# Source Generated with Decompyle++
# File: s6644.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6644
    m_Name = '雷落-电能回流'
    m_LimitHero = 207
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 45,
            'CashCost': 125,
            'Depend': {
                6643: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 207,
                        'max': 4 } }],
            'WarReward': [] } }

