# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6778.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6778.pyc
# Source Generated with Decompyle++
# File: s6778.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6778
    m_Name = '#NT#园丁升华3'
    m_LimitHero = 221
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 221,
                        'max': 3 } }],
            'WarReward': [] } }

