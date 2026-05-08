# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1022.pyc
# Source Generated with Decompyle++
# File: dsi1022.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemSendLastTimePoint(oOwner, lstDice, dInfo, 3)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1022
    m_Name = '锚定'
    m_EnableActionInfo = DiceSpecialItem

