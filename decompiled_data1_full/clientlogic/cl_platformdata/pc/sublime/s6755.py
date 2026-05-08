# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6755.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6755.pyc
# Source Generated with Decompyle++
# File: s6755.pyc (Python 3.6)

from cl_commondefines import REWARD_HEROUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6755
    m_Name = '凛-寒气外溢'
    m_LimitHero = 218
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 255,
            'Depend': {
                6754: 1 },
            'TotalDependLevel': 0,
            'Reward': [
                {
                    'item': REWARD_HEROUPGRADE,
                    'info': {
                        'sid': 218,
                        'max': 5 } }],
            'WarReward': [] } }

