# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1016.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1016.pyc
# Source Generated with Decompyle++
# File: dsi1016.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemPassiveAddState(oOwner, dInfo, 33853, 0, {
        'RewardPer': 5,
        'Reward': 1,
        'SpecialItemSID': 1016,
        'MaxReward': 5 })


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1016
    m_Name = '储存利息'
    m_EnableActionInfo = DiceSpecialItem

