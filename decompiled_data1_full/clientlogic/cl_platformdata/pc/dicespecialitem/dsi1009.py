# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1009.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1009.pyc
# Source Generated with Decompyle++
# File: dsi1009.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemFuseDice(oOwner, lstDice, dInfo)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1009
    m_Name = '合成'
    m_EnableActionInfo = DiceSpecialItem

