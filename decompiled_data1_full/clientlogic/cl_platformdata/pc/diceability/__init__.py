# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import ReadOnly
g_AllDiceAbility = { }
g_ExcludeDiceQuality = { }
g_DiceTagInfo = { }
g_DiceTagListInfo = { }
g_DiceMaxSameAssemblyNum = { }
g_DiceAIMapping = { }
g_AIDice = []
from cl_commondefines import DICETAG_AI, DICETAG_OTHER, DICETAG_PERFORM, DICETAG_SEASONOUTPUT, DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE, DICE_PUTOUT_POLL_THREE, DICE_PUTOUT_POLL_TWO, DICE_QUALITY_NORMAL, DICE_QUALITY_RARE
g_AllDiceAbility = ReadOnly({
    51301: 1,
    51302: 1,
    51303: 1,
    51305: 1,
    51306: 1,
    51307: 1,
    51308: 1,
    51309: 1,
    51311: 1,
    51312: 1,
    51313: 1,
    51314: 1,
    51315: 1,
    51316: 1,
    51317: 1,
    51318: 1,
    51319: 1,
    51322: 1,
    51323: 1,
    51325: 1,
    51326: 1,
    51327: 1,
    51328: 1,
    51330: 1,
    51331: 1,
    51332: 1,
    51333: 1,
    51334: 1,
    51335: 1,
    51336: 1,
    51338: 1,
    51339: 1,
    51340: 1,
    51341: 1,
    51344: 1,
    51345: 1,
    51346: 1,
    51347: 1,
    51348: 1,
    51349: 1,
    51350: 1,
    51351: 1,
    51352: 1,
    51353: 1,
    51355: 1,
    51359: 1,
    51361: 1,
    51362: 1,
    51363: 1,
    51364: 1,
    51366: 1,
    51367: 1,
    51368: 1,
    51369: 1,
    51370: 1,
    51371: 1,
    51372: 1,
    51373: 1,
    51374: 1,
    51375: 1,
    51376: 1,
    51377: 1,
    51378: 1,
    51379: 1,
    51380: 1,
    51381: 1,
    51382: 1,
    51383: 1,
    51384: 1,
    51385: 1,
    51386: 1,
    51387: 1,
    51388: 1,
    51389: 1,
    51390: 1,
    51391: 1,
    51392: 1,
    51393: 1,
    51394: 1,
    51395: 1,
    51396: 1,
    51398: 1,
    51399: 1,
    51400: 1,
    51401: 1,
    51402: 1,
    51403: 1,
    51404: 1 })
g_DiceTagInfo = ReadOnly({
    DICETAG_AI: [
        51383,
        51384,
        51385,
        51386],
    DICETAG_SEASONOUTPUT: [
        51336,
        51338,
        51340,
        51341,
        51351,
        51352,
        51363,
        51370,
        51383,
        51384,
        51385,
        51386,
        51393,
        51394],
    DICETAG_OTHER: [
        51313,
        51314,
        51315,
        51316,
        51317,
        51318,
        51319,
        51325,
        51327,
        51328,
        51332,
        51334,
        51350,
        51359,
        51364,
        51372,
        51373,
        51377,
        51378,
        51379,
        51392,
        51396,
        51400],
    DICETAG_PERFORM: [
        51308,
        51309,
        51311,
        51312,
        51323,
        51330,
        51353,
        51355,
        51361,
        51362,
        51366,
        51367,
        51368,
        51369,
        51371,
        51375,
        51380,
        51381,
        51382,
        51387,
        51388,
        51389,
        51390,
        51391,
        51395,
        51399],
    DICETAG_WEAPON: [
        51301,
        51302,
        51303,
        51305,
        51306,
        51307,
        51322,
        51326,
        51331,
        51333,
        51335,
        51339,
        51344,
        51345,
        51346,
        51347,
        51348,
        51349,
        51374,
        51376,
        51398,
        51401,
        51402,
        51403,
        51404] })
g_ExcludeDiceQuality = ReadOnly({
    DICE_QUALITY_RARE: {
        51346: 1,
        51349: 1,
        51366: 1,
        51379: 1,
        51382: 1,
        51398: 1,
        51400: 1,
        51401: 1 },
    DICE_QUALITY_NORMAL: {
        51303: 1,
        51305: 1,
        51306: 1,
        51309: 1,
        51313: 1,
        51314: 1,
        51315: 1,
        51317: 1,
        51322: 1,
        51323: 1,
        51325: 1,
        51326: 1,
        51327: 1,
        51330: 1,
        51331: 1,
        51333: 1,
        51334: 1,
        51335: 1,
        51336: 1,
        51339: 1,
        51344: 1,
        51346: 1,
        51347: 1,
        51348: 1,
        51349: 1,
        51350: 1,
        51352: 1,
        51355: 1,
        51359: 1,
        51361: 1,
        51362: 1,
        51363: 1,
        51366: 1,
        51368: 1,
        51369: 1,
        51372: 1,
        51373: 1,
        51374: 1,
        51377: 1,
        51379: 1,
        51381: 1,
        51382: 1,
        51383: 1,
        51384: 1,
        51386: 1,
        51387: 1,
        51388: 1,
        51391: 1,
        51394: 1,
        51395: 1,
        51396: 1,
        51398: 1,
        51399: 1,
        51400: 1,
        51401: 1,
        51404: 1 } })
g_DiceTagListInfo = ReadOnly({
    51301: [
        DICETAG_WEAPON],
    51302: [
        DICETAG_WEAPON],
    51303: [
        DICETAG_WEAPON],
    51305: [
        DICETAG_WEAPON],
    51306: [
        DICETAG_WEAPON],
    51307: [
        DICETAG_WEAPON],
    51308: [
        DICETAG_PERFORM],
    51309: [
        DICETAG_PERFORM],
    51311: [
        DICETAG_PERFORM],
    51312: [
        DICETAG_PERFORM],
    51313: [
        DICETAG_OTHER],
    51314: [
        DICETAG_OTHER],
    51315: [
        DICETAG_OTHER],
    51316: [
        DICETAG_OTHER],
    51317: [
        DICETAG_OTHER],
    51318: [
        DICETAG_OTHER],
    51319: [
        DICETAG_OTHER],
    51322: [
        DICETAG_WEAPON],
    51323: [
        DICETAG_PERFORM],
    51325: [
        DICETAG_OTHER],
    51326: [
        DICETAG_WEAPON],
    51327: [
        DICETAG_OTHER],
    51328: [
        DICETAG_OTHER],
    51330: [
        DICETAG_PERFORM],
    51331: [
        DICETAG_WEAPON],
    51332: [
        DICETAG_OTHER],
    51333: [
        DICETAG_WEAPON],
    51334: [
        DICETAG_OTHER],
    51335: [
        DICETAG_WEAPON],
    51336: [
        DICETAG_SEASONOUTPUT],
    51338: [
        DICETAG_SEASONOUTPUT],
    51339: [
        DICETAG_WEAPON],
    51340: [
        DICETAG_SEASONOUTPUT],
    51341: [
        DICETAG_SEASONOUTPUT],
    51344: [
        DICETAG_WEAPON],
    51345: [
        DICETAG_WEAPON],
    51346: [
        DICETAG_WEAPON],
    51347: [
        DICETAG_WEAPON],
    51348: [
        DICETAG_WEAPON],
    51349: [
        DICETAG_WEAPON],
    51350: [
        DICETAG_OTHER],
    51351: [
        DICETAG_SEASONOUTPUT],
    51352: [
        DICETAG_SEASONOUTPUT],
    51353: [
        DICETAG_PERFORM],
    51355: [
        DICETAG_PERFORM],
    51359: [
        DICETAG_OTHER],
    51361: [
        DICETAG_PERFORM],
    51362: [
        DICETAG_PERFORM],
    51363: [
        DICETAG_SEASONOUTPUT],
    51364: [
        DICETAG_OTHER],
    51366: [
        DICETAG_PERFORM],
    51367: [
        DICETAG_PERFORM],
    51368: [
        DICETAG_PERFORM],
    51369: [
        DICETAG_PERFORM],
    51370: [
        DICETAG_SEASONOUTPUT],
    51371: [
        DICETAG_PERFORM],
    51372: [
        DICETAG_OTHER],
    51373: [
        DICETAG_OTHER],
    51374: [
        DICETAG_WEAPON],
    51375: [
        DICETAG_PERFORM],
    51376: [
        DICETAG_WEAPON],
    51377: [
        DICETAG_OTHER],
    51378: [
        DICETAG_OTHER],
    51379: [
        DICETAG_OTHER],
    51380: [
        DICETAG_PERFORM],
    51381: [
        DICETAG_PERFORM],
    51382: [
        DICETAG_PERFORM],
    51383: [
        DICETAG_SEASONOUTPUT,
        DICETAG_AI],
    51384: [
        DICETAG_SEASONOUTPUT,
        DICETAG_AI],
    51385: [
        DICETAG_SEASONOUTPUT,
        DICETAG_AI],
    51386: [
        DICETAG_SEASONOUTPUT,
        DICETAG_AI],
    51387: [
        DICETAG_PERFORM],
    51388: [
        DICETAG_PERFORM],
    51389: [
        DICETAG_PERFORM],
    51390: [
        DICETAG_PERFORM],
    51391: [
        DICETAG_PERFORM],
    51392: [
        DICETAG_OTHER],
    51393: [
        DICETAG_SEASONOUTPUT],
    51394: [
        DICETAG_SEASONOUTPUT],
    51395: [
        DICETAG_PERFORM],
    51396: [
        DICETAG_OTHER],
    51398: [
        DICETAG_WEAPON],
    51399: [
        DICETAG_PERFORM],
    51400: [
        DICETAG_OTHER],
    51401: [
        DICETAG_WEAPON],
    51402: [
        DICETAG_WEAPON],
    51403: [
        DICETAG_WEAPON],
    51404: [
        DICETAG_WEAPON] })
g_AIDice = ReadOnly([
    51383,
    51384,
    51385,
    51386])
g_DicePutOutPool = ReadOnly({
    DICE_PUTOUT_POLL_THREE: {
        51336: 1,
        51338: 1,
        51340: 1,
        51341: 1,
        51351: 1,
        51352: 1,
        51363: 1,
        51370: 1,
        51393: 1,
        51394: 1 },
    DICE_PUTOUT_POLL_TWO: {
        51309: 1,
        51322: 1,
        51323: 1,
        51325: 1,
        51330: 1,
        51333: 1,
        51334: 1,
        51335: 1,
        51344: 1,
        51346: 1,
        51347: 1,
        51348: 1,
        51349: 1,
        51350: 1,
        51355: 1,
        51361: 1,
        51366: 1,
        51368: 1,
        51369: 1,
        51372: 1,
        51373: 1,
        51374: 1,
        51379: 1,
        51381: 1,
        51382: 1,
        51387: 1,
        51388: 1,
        51389: 1,
        51390: 1,
        51391: 1,
        51392: 1,
        51395: 1,
        51396: 1,
        51398: 1,
        51399: 1,
        51400: 1,
        51401: 1,
        51402: 1,
        51403: 1,
        51404: 1 },
    DICE_PUTOUT_POLL_ONE: {
        51301: 1,
        51302: 1,
        51303: 1,
        51305: 1,
        51306: 1,
        51307: 1,
        51308: 1,
        51311: 1,
        51312: 1,
        51313: 1,
        51314: 1,
        51315: 1,
        51316: 1,
        51317: 1,
        51318: 1,
        51319: 1,
        51326: 1,
        51327: 1,
        51328: 1,
        51331: 1,
        51332: 1,
        51339: 1,
        51345: 1,
        51353: 1,
        51359: 1,
        51362: 1,
        51364: 1,
        51367: 1,
        51371: 1,
        51375: 1,
        51376: 1,
        51377: 1,
        51378: 1,
        51380: 1 } })
g_DiceMaxSameAssemblyNum = ReadOnly({
    51301: 2,
    51302: 2,
    51303: 1,
    51305: 2,
    51306: 2,
    51307: 2,
    51308: 1,
    51309: 2,
    51311: 2,
    51312: 2,
    51313: 2,
    51314: 2,
    51315: 2,
    51316: 2,
    51317: 2,
    51318: 2,
    51319: 2,
    51322: 1,
    51323: 1,
    51325: 1,
    51326: 1,
    51327: 2,
    51328: 2,
    51330: 1,
    51331: 1,
    51332: 1,
    51333: 1,
    51334: 1,
    51335: 1,
    51336: 2,
    51338: 2,
    51339: 1,
    51340: 2,
    51341: 1,
    51344: 1,
    51345: 2,
    51346: 1,
    51347: 1,
    51348: 1,
    51349: 1,
    51350: 1,
    51351: 1,
    51352: 1,
    51353: 2,
    51355: 1,
    51359: 1,
    51361: 1,
    51362: 1,
    51363: 1,
    51364: 1,
    51366: 1,
    51367: 1,
    51368: 1,
    51369: 1,
    51370: 1,
    51371: 1,
    51372: 1,
    51373: 1,
    51374: 1,
    51375: 1,
    51376: 1,
    51377: 1,
    51378: 1,
    51379: 1,
    51380: 1,
    51381: 1,
    51382: 1,
    51383: 2,
    51384: 2,
    51385: 2,
    51386: 1,
    51387: 1,
    51388: 1,
    51389: 1,
    51390: 1,
    51391: 1,
    51392: 1,
    51393: 1,
    51394: 1,
    51395: 1,
    51396: 1,
    51398: 1,
    51399: 1,
    51400: 1,
    51401: 1,
    51402: 1,
    51403: 1,
    51404: 1 })
g_DiceAIMapping = ReadOnly({
    51336: 51383,
    51338: 51384,
    51340: 51385,
    51363: 51386 })

def GetAllDiceAbility():
    return g_AllDiceAbility


def GetExcludeDiceQuality(iQuality):
    if iQuality in g_ExcludeDiceQuality:
        return g_ExcludeDiceQuality[iQuality]
    return { }


def GetDiceTagInfo():
    return g_DiceTagInfo


def GetDiceTagListInfo(iDice):
    if iDice not in g_DiceTagListInfo:
        return []
    return g_DiceTagListInfo[iDice]


def GetAIDice():
    return g_AIDice


def GetDiceByPutOutPoolType(iPoolType):
    if iPoolType not in g_DicePutOutPool:
        return { }
    return g_DicePutOutPool[iPoolType]


def GetDicePointMaxSameAssemblyNum(iSID):
    if iSID not in g_DiceMaxSameAssemblyNum:
        return 0
    return g_DiceMaxSameAssemblyNum[iSID]


def GetDiceAIMapping():
    return g_DiceAIMapping

