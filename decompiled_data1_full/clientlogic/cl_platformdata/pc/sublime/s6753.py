# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6753.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6753.pyc
# Source Generated with Decompyle++
# File: s6753.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6753
    m_Name = '凛-化雪凝冰'
    m_LimitHero = 218
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 30,
            'CashCost': 60,
            'Depend': {
                6752: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 218,
                        'max': 3 } }],
            'WarReward': [] } }

