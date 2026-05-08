# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_dice/__init__.pyc
# RelativePath: clientlogic/cl_dice/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_dice.mobject import CDiceData
from cl_platformdata import IsRunPCData, ImportdMod, GetAllDiceSpecialItem, GetAllDiceAbility

def GetDiceDataCls():
    return CDiceData


def CreateDice(oGame, oDiceCon, dDiceInfo, iPointID = 0, dTmp = None):
    if dDiceInfo['SID'] not in GetAllDiceAbility():
        return None
    clsDiceData = GetDiceDataCls()
    if not clsDiceData:
        return None
    return clsDiceData.Create(oGame, oDiceCon, dDiceInfo, iPointID, dTmp)

if 'g_DiceSpecialItem' not in globals():
    g_DiceSpecialItem = { }

def GetDiceSpecialCls(iSID):
    if iSID not in GetAllDiceSpecialItem():
        return None
    if iSID not in g_DiceSpecialItem:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'dicespecialitem', 'dsi%4d' % iSID)
        if not mod:
            return None
        g_DiceSpecialItem[iSID] = mod.CDiceSpecialItem
    return g_DiceSpecialItem[iSID]

