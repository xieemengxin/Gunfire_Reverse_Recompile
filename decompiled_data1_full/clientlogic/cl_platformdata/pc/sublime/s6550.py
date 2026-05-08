# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6550.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6550.pyc
# Source Generated with Decompyle++
# File: s6550.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_PASSIVE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6550
    m_Name = '返老还童'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 120,
            'Depend': {
                6549: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_PASSIVE,
                    'info': {
                        'sid': 6555,
                        'data': { } } }] } }

