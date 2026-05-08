# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6568.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6568.pyc
# Source Generated with Decompyle++
# File: s6568.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_HIDESHOPGOODS
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6568
    m_Name = '琳琅满目'
    m_LimitHero = 0
    m_MaxLevel = 2
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 60,
            'CashCost': 90,
            'Depend': {
                6565: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_HIDESHOPGOODS,
                    'info': {
                        'pos': 7 } }] },
        2: {
            'NeedPlayerGrade': 60,
            'CashCost': 120,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_HIDESHOPGOODS,
                    'info': {
                        'pos': 7 } },
                {
                    'item': VIRTUAL_ITEM_HIDESHOPGOODS,
                    'info': {
                        'pos': 8 } }] } }

