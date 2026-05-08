# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1001.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1001.pyc
# Source Generated with Decompyle++
# File: dsi1001.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemReThrowDicePoints(oOwner, lstDice, dInfo)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1001
    m_Name = '重掷'
    m_EnableActionInfo = DiceSpecialItem

