# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6544.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6544.pyc
# Source Generated with Decompyle++
# File: s6544.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_PASSIVE
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6544
    m_Name = '物品回收'
    m_LimitHero = 0
    m_MaxLevel = 2
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 90,
            'Depend': {
                6543: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_PASSIVE,
                    'info': {
                        'sid': 6544,
                        'data': { } } }] },
        2: {
            'NeedPlayerGrade': 60,
            'CashCost': 120,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_PASSIVE,
                    'info': {
                        'sid': 6544,
                        'data': { } } }] } }

