# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1010.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1010.pyc
# Source Generated with Decompyle++
# File: dsi1010.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemExtractThrowExcludePoints(oOwner, lstDice, dInfo, {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1 }, {
        3: 1,
        6: 1 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1010
    m_Name = '数字黑洞'
    m_EnableActionInfo = DiceSpecialItem

