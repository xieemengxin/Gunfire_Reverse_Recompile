# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/dsi1014.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/dsi1014.pyc
# Source Generated with Decompyle++
# File: dsi1014.pyc (Python 3.6)

import cl_action
from cl_dice.dicespecialitem import CDiceSpecialItem as CCustomDiceSpecialItem

def DiceSpecialItem(oOwner, lstDice, dInfo):
    cl_action.SpecialItemAddDicePacketPointsShowCnt(oOwner, lstDice, dInfo, 1)


class CDiceSpecialItem(CCustomDiceSpecialItem):
    m_SID = 1014
    m_Name = '观星'
    m_EnableActionInfo = DiceSpecialItem

