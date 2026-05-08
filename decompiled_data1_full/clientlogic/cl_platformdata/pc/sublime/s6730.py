# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6730.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6730.pyc
# Source Generated with Decompyle++
# File: s6730.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6730
    m_Name = '虞火-炽炎追击'
    m_LimitHero = 217
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 410,
            'Depend': {
                6724: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 217,
                        'max': 5 } }],
            'WarReward': [] } }

