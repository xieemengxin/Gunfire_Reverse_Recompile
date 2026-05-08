# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1003.pyc
# Source Generated with Decompyle++
# File: dsi1003.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemProcessDice(oOwner, lstDice, dInfo, 4)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1003
    m_Name = '加工'
    m_EnableActionInfo = DiceSpecialItem

