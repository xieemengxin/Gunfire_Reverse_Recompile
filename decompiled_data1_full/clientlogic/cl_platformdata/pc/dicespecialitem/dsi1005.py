# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1005.pyc
# Source Generated with Decompyle++
# File: dsi1005.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemCopyDice(oOwner, lstDice, dInfo, 1)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1005
    m_Name = '复制'
    m_EnableActionInfo = DiceSpecialItem

