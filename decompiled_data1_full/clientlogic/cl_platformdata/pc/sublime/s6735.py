# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6735.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6735.pyc
# Source Generated with Decompyle++
# File: s6735.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6735
    m_Name = '紫鸮-运势流转'
    m_LimitHero = 216
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6734: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 216,
                        'max': 5 } }],
            'WarReward': [] } }

