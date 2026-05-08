# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s8thirditem/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s8thirditem/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import ReadOnly
g_AllS8ThirdItem = ReadOnly({
    1001: 1,
    1002: 1,
    1003: 1,
    1004: 1,
    1005: 1 })
from cl_commondefines import S8_GOODS_QUALITY_BLUE, S8_GOODS_QUALITY_ORANGE, S8_GOODS_QUALITY_PURPLE
g_ThirdAbilityChooseRule = ReadOnly({
    S8_GOODS_QUALITY_ORANGE: {
        (3, 1): 1,
        (2, 3): 9,
        (1, 3): 90 },
    S8_GOODS_QUALITY_PURPLE: {
        (3, 1): 1,
        (2, 3): 9,
        (1, 3): 90 },
    S8_GOODS_QUALITY_BLUE: {
        (3, 1): 1,
        (2, 3): 9,
        (1, 3): 90 } })
g_ThirdQuality2AbilityNum = ReadOnly({
    S8_GOODS_QUALITY_ORANGE: 3,
    S8_GOODS_QUALITY_PURPLE: 2,
    S8_GOODS_QUALITY_BLUE: 1 })

def GetS8ThirdItem():
    return g_AllS8ThirdItem


def GetThirdAbilityChooseRule(iQuality):
    if iQuality in g_ThirdAbilityChooseRule:
        return g_ThirdAbilityChooseRule[iQuality]
    return { }


def GetThirdAbilityNum(iQuality):
    if iQuality in g_ThirdQuality2AbilityNum:
        return g_ThirdQuality2AbilityNum[iQuality]
    return 0

