# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1020.pyc
# Source Generated with Decompyle++
# File: dsi1020.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33890, 0, {
        'AssemblyNum': 1,
        'DiceEnergy': 15,
        'SpecialItemSID': 1020 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1020
    m_Name = '快速启动'
    m_EnableActionInfo = DiceSpecialItem

