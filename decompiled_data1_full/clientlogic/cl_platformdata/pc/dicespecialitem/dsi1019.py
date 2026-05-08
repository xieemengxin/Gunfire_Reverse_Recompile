# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1019.pyc
# Source Generated with Decompyle++
# File: dsi1019.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33892, 0, {
        'SpecialItemSID': 1019 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1019
    m_Name = '商店会员'
    m_EnableActionInfo = DiceSpecialItem

