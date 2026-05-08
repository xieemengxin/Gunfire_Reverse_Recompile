# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6777.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6777.pyc
# Source Generated with Decompyle++
# File: s6777.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6777
    m_Name = '#NT#园丁升华2'
    m_LimitHero = 221
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 35,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 221,
                        'max': 2 } }],
            'WarReward': [] } }

