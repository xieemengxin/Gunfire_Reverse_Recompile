# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1012.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1012.pyc
# Source Generated with Decompyle++
# File: dsi1012.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33764, 0, {
        'SpecialItemSID': 1012,
        'Reward': 4 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1012
    m_Name = '强化分解'
    m_EnableActionInfo = DiceSpecialItem

