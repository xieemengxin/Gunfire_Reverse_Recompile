# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6570.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6570.pyc
# Source Generated with Decompyle++
# File: s6570.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_WEAPONUPGRADE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6570
    m_Name = '能工巧匠'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 25,
            'Depend': {
                6551: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_WEAPONUPGRADE,
                    'info': {
                        'add': 1 } }] } }

