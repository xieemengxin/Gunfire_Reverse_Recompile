# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1017.pyc
# Source Generated with Decompyle++
# File: dsi1017.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemAddDiceRandomPoints(oOwner, lstDice, dInfo, 4, {
        2: 6,
        7: 12,
        14: 18 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1017
    m_Name = '幸运数字'
    m_EnableActionInfo = DiceSpecialItem

