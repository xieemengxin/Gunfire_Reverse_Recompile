# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6774.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6774.pyc
# Source Generated with Decompyle++
# File: s6774.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6774
    m_Name = '苍玦-贯影之力'
    m_LimitHero = 220
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 45,
            'CashCost': 125,
            'Depend': {
                6773: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 220,
                        'max': 4 } }],
            'WarReward': [] } }

