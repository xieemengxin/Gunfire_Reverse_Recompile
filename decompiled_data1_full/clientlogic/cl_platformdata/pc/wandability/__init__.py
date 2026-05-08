# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import ReadOnly
g_AllWandAbility = { }
g_WandAbilityByType = { }
g_WandAbilityByQuality = { }
g_GWandPointAbility = { }
g_PWandPointAbility = { }
g_WandExcludeAbility = { }
from cl_commondefines import ABILITY_QUALITY_FOUR, ABILITY_QUALITY_NEGATIVE, ABILITY_QUALITY_ONE, ABILITY_QUALITY_THREE, ABILITY_QUALITY_TWO, ABILITY_TYPE_EXCLUSIVE, ABILITY_TYPE_NEGATIVE, ABILITY_TYPE_POSITIVE
g_AllWandAbility = ReadOnly({
    51251: 1,
    51252: 1,
    51254: 1,
    51255: 1,
    51256: 1,
    51257: 1,
    51258: 1,
    51259: 1,
    51260: 1,
    51261: 1,
    51262: 1,
    51263: 1,
    51265: 1,
    51266: 1,
    51267: 1,
    51268: 1,
    51269: 1,
    51270: 1,
    51271: 1,
    51272: 1,
    51273: 1,
    51274: 1,
    51275: 1,
    51276: 1,
    51277: 1,
    51278: 1,
    51279: 1,
    51280: 1,
    51281: 1,
    51282: 1,
    51283: 1,
    51284: 1,
    51285: 1,
    51286: 1,
    51287: 1,
    51288: 1,
    51289: 1,
    51290: 1,
    51291: 1,
    51292: 1,
    51293: 1,
    51294: 1,
    51295: 1,
    51296: 1,
    51297: 1,
    51298: 1,
    51299: 1,
    51300: 1 })
g_WandAbilityByType = ReadOnly({
    ABILITY_TYPE_NEGATIVE: [
        51277,
        51281,
        51282,
        51283,
        51284,
        51285,
        51286],
    ABILITY_TYPE_EXCLUSIVE: [
        51258,
        51259,
        51260,
        51261,
        51262,
        51265,
        51266,
        51267,
        51268,
        51269,
        51270,
        51271,
        51272,
        51273,
        51274,
        51278,
        51279,
        51280,
        51287,
        51288,
        51289,
        51290,
        51291,
        51292,
        51293,
        51294,
        51295,
        51296,
        51297,
        51298,
        51299,
        51300],
    ABILITY_TYPE_POSITIVE: [
        51251,
        51252,
        51254,
        51255,
        51256,
        51257,
        51263,
        51275,
        51276] })
g_WandAbilityByQuality = ReadOnly({
    ABILITY_QUALITY_FOUR: {
        51251: 1,
        51252: 1,
        51254: 1,
        51255: 1,
        51256: 1,
        51257: 1,
        51263: 1,
        51275: 1,
        51276: 1 },
    ABILITY_QUALITY_THREE: {
        51251: 1,
        51252: 1,
        51254: 1,
        51255: 1,
        51256: 1,
        51257: 1,
        51263: 1,
        51275: 1 },
    ABILITY_QUALITY_TWO: {
        51251: 1,
        51252: 1,
        51254: 1,
        51256: 1,
        51257: 1,
        51263: 1 },
    ABILITY_QUALITY_ONE: {
        51251: 1,
        51252: 1,
        51254: 1,
        51256: 1,
        51263: 1 },
    ABILITY_QUALITY_NEGATIVE: {
        51277: 1,
        51281: 1,
        51282: 1,
        51283: 1,
        51284: 1,
        51285: 1,
        51286: 1 } })
g_GWandPointAbility = ReadOnly({
    1005: 51258,
    1006: 51259,
    1011: 51260,
    1007: 51261,
    1003: 51262,
    1010: 51265,
    1013: 51266,
    1016: 51267,
    1018: 51268,
    1015: 51269,
    1020: 51270,
    1002: 51271,
    1012: 51272,
    1019: 51273,
    1022: 51274,
    1021: 51280 })
g_PWandPointAbility = ReadOnly({
    1005: 51278,
    1006: 51279,
    1011: 51287,
    1007: 51288,
    1003: 51289,
    1013: 51290,
    1018: 51291,
    1010: 51292,
    1016: 51293,
    1015: 51294,
    1020: 51295,
    1002: 51296,
    1012: 51297,
    1019: 51298,
    1021: 51299,
    1022: 51300 })
g_WandExcludeAbility = ReadOnly({
    1005: [
        51251],
    1019: [
        51251,
        51254,
        51282],
    1016: [
        51254,
        51282],
    1013: [
        51254,
        51282] })

def GetAllWandAbility():
    return g_AllWandAbility


def GetWandAbilityByType(iType):
    if iType in g_WandAbilityByType:
        return g_WandAbilityByType[iType]
    return []


def GetWandAbilityByQuality(iQuality):
    if iQuality in g_WandAbilityByQuality:
        return g_WandAbilityByQuality[iQuality]
    return { }


def GetGWandPointAbility(iWandSID):
    if iWandSID in g_GWandPointAbility:
        return g_GWandPointAbility[iWandSID]
    return 0


def GetPWandPointAbility(iWandSID):
    if iWandSID in g_PWandPointAbility:
        return g_PWandPointAbility[iWandSID]
    return 0


def GetWandPointAbility(iWandSID):
    lstPointAbility = []
    if iWandSID in g_GWandPointAbility:
        lstPointAbility.append(g_GWandPointAbility[iWandSID])
    if iWandSID in g_PWandPointAbility:
        lstPointAbility.append(g_PWandPointAbility[iWandSID])
    return lstPointAbility


def GetWandExcludeAbility(iWandSID):
    if iWandSID in g_WandExcludeAbility:
        return g_WandExcludeAbility[iWandSID]
    return []

