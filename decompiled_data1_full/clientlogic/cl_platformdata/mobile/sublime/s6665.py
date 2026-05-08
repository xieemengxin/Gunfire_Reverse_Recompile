# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6665.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6665.pyc
# Source Generated with Decompyle++
# File: s6665.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6665
    m_Name = '卫士-一心二用'
    m_LimitHero = 209
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 410,
            'Depend': {
                6664: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 209,
                        'max': 5 } }],
            'WarReward': [] } }

