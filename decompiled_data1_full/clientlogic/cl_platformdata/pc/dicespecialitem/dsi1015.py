# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1015.pyc
# Source Generated with Decompyle++
# File: dsi1015.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33850, 0, {
        'EnergyMul': 50,
        'SpecialItemSID': 1015 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1015
    m_Name = '充能增幅'
    m_EnableActionInfo = DiceSpecialItem

