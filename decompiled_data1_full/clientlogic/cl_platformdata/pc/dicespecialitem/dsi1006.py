# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1006.pyc
# Source Generated with Decompyle++
# File: dsi1006.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemChangeRollWeightByMul(oOwner, lstDice, dInfo, {
        6: {
            3: 300 },
        12: {
            3: 300 },
        18: {
            3: 300 } })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1006
    m_Name = '数三'
    m_EnableActionInfo = DiceSpecialItem

