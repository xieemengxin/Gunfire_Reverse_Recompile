# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6545.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6545.pyc
# Source Generated with Decompyle++
# File: s6545.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_SHOPGOODSWEIGHT
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6545
    m_Name = '渠道拓展'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 25,
            'Depend': {
                6555: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_SHOPGOODSWEIGHT,
                    'info': {
                        'type': VIRTUAL_ITEM_RELIC,
                        'weight': 100 } }] } }

