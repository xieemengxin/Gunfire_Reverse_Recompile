# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/module/m16043.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/module/m16043.pyc
# Source Generated with Decompyle++
# File: m16043.pyc (Python 3.6)

from cl_anima.mobject import CModuleData as CCustom
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, VIRTUAL_ITEM_EXCLUSINSCRIPTION, VIRTUAL_ITEM_INSCRIPTIONPROP

class CAnimaModule(CCustom):
    m_SID = 16043
    m_Name = '专属铭刻'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_Shape = 1003
    m_LevelInfo = {
        1: {
            'CashCost': 0,
            'WarReward': [
                {
                    'item': VIRTUAL_ITEM_EXCLUSINSCRIPTION,
                    'info': {
                        'new': 3 } },
                {
                    'item': VIRTUAL_ITEM_INSCRIPTIONPROP,
                    'info': {
                        'type': INSCRIPTION_TYPE_EXCLUSIVE,
                        'new': 30 } }] } }

