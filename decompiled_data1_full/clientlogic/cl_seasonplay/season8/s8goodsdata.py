# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season8/s8goodsdata.pyc
# RelativePath: clientlogic/cl_seasonplay/season8/s8goodsdata.pyc
# Source Generated with Decompyle++
# File: s8goodsdata.pyc (Python 3.6)

from cl_platformdata import GetS8GemItem, GetS8ThirdItem
from cl_only import ChooseKey, Functor
from cl_commondefines import S8_GOODS_QUALITY_BLUE, S8_GOODS_QUALITY_PURPLE, S8_GOODS_QUALITY_ORANGE

class CS8GoodsData(object):
    m_SID = 0
    m_Name = ''
    m_InternalGoodRule = ()


def RandomChooseItem(oGame, dChooseInfo, dExcludeInfo):
    dResultInfo = { }
    for tGoodsKey in dChooseInfo:
        if tGoodsKey in dExcludeInfo:
            continue
        dResultInfo[tGoodsKey] = dChooseInfo[tGoodsKey]
    
    return ChooseKey(oGame, dResultInfo)


def RandomChooseS8ThirdPFItem(dQualityInfo, oGame, oHero, dHasChooseInfo):
    dAllThirdItem = GetS8ThirdItem()
    if not dAllThirdItem:
        return ()
    dChooseInfo = { }
    if not dQualityInfo:
        dQualityInfo = {
            S8_GOODS_QUALITY_ORANGE: 100,
            S8_GOODS_QUALITY_PURPLE: 100,
            S8_GOODS_QUALITY_BLUE: 100 }
    for iSID in dAllThirdItem:
        for iQuality, iWeight in dQualityInfo.items():
            dChooseInfo[(iSID, iQuality)] = iWeight
        
    
    tResult = RandomChooseItem(oGame, dChooseInfo, dHasChooseInfo)
    if not tResult:
        tResult = RandomChooseItem(oGame, dChooseInfo, { })
        if not tResult:
            return ()
    return tResult


def RandomChooseS8GemItem(dQualityInfo, oGame, oHero, dHasChooseInfo):
    dAllThirdItem = GetS8GemItem()
    if not dAllThirdItem:
        return ()
    dChooseInfo = { }
    if not dQualityInfo:
        dQualityInfo = {
            S8_GOODS_QUALITY_ORANGE: 100,
            S8_GOODS_QUALITY_PURPLE: 100,
            S8_GOODS_QUALITY_BLUE: 100 }
    for iSID in dAllThirdItem:
        for iQuality, iWeight in dQualityInfo.items():
            dChooseInfo[(iSID, iQuality)] = iWeight
        
    
    tResult = RandomChooseItem(oGame, dChooseInfo, dHasChooseInfo)
    if not tResult:
        tResult = RandomChooseItem(oGame, dChooseInfo, { })
        if not tResult:
            return ()
    return tResult

from cl_commondefines import S8_GOODS_QUALITY_BLUE, S8_GOODS_QUALITY_ORANGE, S8_GOODS_QUALITY_PURPLE, VIRTUAL_ITEM_S8GEMITEM, VIRTUAL_ITEM_S8THIRDPERFORM

class CS8GoodsData1001(CS8GoodsData):
    m_SID = 1001
    m_Name = '技能投放-全蓝'
    m_GoodsDataType = VIRTUAL_ITEM_S8THIRDPERFORM
    m_InternalGoodRule = (Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_BLUE: 100 }), Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_BLUE: 100 }))


class CS8GoodsData1002(CS8GoodsData):
    m_SID = 1002
    m_Name = '技能投放-全紫'
    m_GoodsDataType = VIRTUAL_ITEM_S8THIRDPERFORM
    m_InternalGoodRule = (Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_PURPLE: 100 }), Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_PURPLE: 100 }))


class CS8GoodsData1003(CS8GoodsData):
    m_SID = 1003
    m_Name = '技能投放-全橙'
    m_GoodsDataType = VIRTUAL_ITEM_S8THIRDPERFORM
    m_InternalGoodRule = (Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_ORANGE: 100 }), Functor(RandomChooseS8ThirdPFItem, {
        S8_GOODS_QUALITY_ORANGE: 100 }))


class CS8GoodsData1051(CS8GoodsData):
    m_SID = 1051
    m_Name = '宝石投放-常规'
    m_GoodsDataType = VIRTUAL_ITEM_S8GEMITEM
    m_InternalGoodRule = (Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }))


class CS8GoodsData1052(CS8GoodsData):
    m_SID = 1052
    m_Name = '宝石投放-BOSS'
    m_GoodsDataType = VIRTUAL_ITEM_S8GEMITEM
    m_InternalGoodRule = (Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }), Functor(RandomChooseS8GemItem, {
        S8_GOODS_QUALITY_ORANGE: 1,
        S8_GOODS_QUALITY_PURPLE: 9,
        S8_GOODS_QUALITY_BLUE: 90 }))

g_AllGoodsData = {
    1001: CS8GoodsData1001,
    1002: CS8GoodsData1002,
    1003: CS8GoodsData1003,
    1051: CS8GoodsData1051,
    1052: CS8GoodsData1052 }

def GetS8GoodsData(iSID):
    if iSID not in g_AllGoodsData:
        return None
    return g_AllGoodsData[iSID]

