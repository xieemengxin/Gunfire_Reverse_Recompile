# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1013.pyc
# Source Generated with Decompyle++
# File: dsi1013.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemSplitThrowDicePoints(oOwner, lstDice, dInfo, 6)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1013
    m_Name = '拆分'
    m_EnableActionInfo = DiceSpecialItem

