# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/sublime/s6714.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/sublime/s6714.pyc
# Source Generated with Decompyle++
# File: s6714.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6714
    m_Name = '行者-技艺精熟'
    m_LimitHero = 214
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 45,
            'CashCost': 125,
            'Depend': {
                6713: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 214,
                        'max': 4 } }],
            'WarReward': [] } }

