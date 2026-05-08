# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6615.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6615.pyc
# Source Generated with Decompyle++
# File: s6615.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6615
    m_Name = '太子-绝地护盾'
    m_LimitHero = 205
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6614: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 205,
                        'max': 5 } }],
            'WarReward': [] } }

