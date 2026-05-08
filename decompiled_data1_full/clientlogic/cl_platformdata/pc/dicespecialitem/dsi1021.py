# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1021.pyc
# Source Generated with Decompyle++
# File: dsi1021.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemAddDiceMaxAssembly(oOwner, lstDice, dInfo, 1, {
        6: {
            6: -90 },
        12: {
            12: -90 },
        18: {
            18: -90 } })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1021
    m_Name = '额外槽位'
    m_EnableActionInfo = DiceSpecialItem

