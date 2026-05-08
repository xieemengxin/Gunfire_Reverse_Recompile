# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6783.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6783.pyc
# Source Generated with Decompyle++
# File: s6783.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6783
    m_Name = '呦呦-光合作用'
    m_LimitHero = 221
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6782: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 221,
                        'max': 3 } }],
            'WarReward': [] } }

