# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/dicespecialitem/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/pc/dicespecialitem/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import ReadOnly
from cl_commondefines import DICESPECIAL_ACTIVE_TAKEEFFECT, DICESPECIAL_PASSIVE_INIT_TAKEEFFECT, DICESPECIAL_PASSIVE_TAKEEFFECT, DICE_QUALITY_HIGH, DICE_QUALITY_LOW
g_AllDiceSpecialItem = ReadOnly({
    1001: 1,
    1003: 1,
    1005: 1,
    1006: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1014: 1,
    1015: 1,
    1016: 1,
    1017: 1,
    1019: 1,
    1020: 1,
    1021: 1,
    1022: 1,
    1023: 1,
    1024: 1 })

def GetDiceSpecialItemTriggerEnergy(iDiceSpecialItem):
    dDiceSpecialItemTriggerEnergyInfo = {
        1001: 45,
        1003: 40,
        1005: 60,
        1009: 40,
        1011: 25,
        1014: 80,
        1022: 60 }
    if iDiceSpecialItem not in dDiceSpecialItemTriggerEnergyInfo:
        return 0
    return dDiceSpecialItemTriggerEnergyInfo[iDiceSpecialItem]

g_DiceSpecialTypeInfo = ReadOnly({
    DICESPECIAL_PASSIVE_INIT_TAKEEFFECT: [
        1006,
        1012,
        1015,
        1016,
        1019,
        1020,
        1021,
        1023,
        1024],
    DICESPECIAL_PASSIVE_TAKEEFFECT: [
        1006,
        1010,
        1012,
        1013,
        1015,
        1016,
        1017,
        1019,
        1020,
        1021,
        1023,
        1024],
    DICESPECIAL_ACTIVE_TAKEEFFECT: [
        1001,
        1003,
        1005,
        1009,
        1011,
        1014,
        1022] })
g_DiceSpecialItemCanBuyInfo = ReadOnly({
    1001: 99,
    1003: 1,
    1004: 99,
    1005: 1,
    1006: 99,
    1009: 1,
    1010: 99,
    1011: 99,
    1012: 99,
    1013: 99,
    1014: 99,
    1015: 99,
    1016: 99,
    1017: 99,
    1018: 99,
    1019: 99,
    1020: 99,
    1021: 99,
    1022: 99,
    1023: 99,
    1024: 99 })
g_SpecialItemQuality = ReadOnly({
    DICE_QUALITY_HIGH: {
        1003: 1,
        1009: 1 },
    DICE_QUALITY_LOW: {
        1001: 1,
        1005: 1,
        1006: 1,
        1010: 1,
        1011: 1,
        1012: 1,
        1013: 1,
        1014: 1,
        1015: 1,
        1016: 1,
        1017: 1,
        1019: 1,
        1020: 1,
        1021: 1,
        1022: 1,
        1023: 1,
        1024: 1 } })
g_SpItemBanBenedicList = ReadOnly({ })

def GetAllDiceSpecialItem():
    return g_AllDiceSpecialItem


def GetDiceSpecialTypeList(iType):
    if iType not in g_DiceSpecialTypeInfo:
        return []
    return g_DiceSpecialTypeInfo[iType]


def GetSpItemBanBenedicList():
    return g_SpItemBanBenedicList


def GetDiceSpecialItemCanBuy(iDiceSpecialItem):
    if iDiceSpecialItem not in g_DiceSpecialItemCanBuyInfo:
        return 0
    return g_DiceSpecialItemCanBuyInfo[iDiceSpecialItem]


def GetDiceSpecialItemByQuality(iQuality):
    if iQuality not in g_SpecialItemQuality:
        return { }
    return g_SpecialItemQuality[iQuality]

