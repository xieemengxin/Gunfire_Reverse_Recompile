# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6738.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6738.pyc
# Source Generated with Decompyle++
# File: s6738.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6738
    m_Name = '召唤师-3'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 105,
            'Depend': {
                6737: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 214,
                        'max': 3 } }],
            'WarReward': [] } }

