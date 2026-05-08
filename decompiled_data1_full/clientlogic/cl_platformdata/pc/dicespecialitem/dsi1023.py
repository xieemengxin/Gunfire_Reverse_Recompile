# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1023.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1023.pyc
# Source Generated with Decompyle++
# File: dsi1023.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33911, 0, {
        'SpecialItemSID': 1023 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1023
    m_Name = '双生灵宝（主动）'
    m_EnableActionInfo = DiceSpecialItem

