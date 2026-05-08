# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_shop/__init__.pyc
# RelativePath: clientlogic/cl_shop/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import cl_shop.goods
import cl_shop.goodsdata
import cl_test as cl_customconfig


def _ScaleGoodsCash(iCash):
    return cl_customconfig.ScaleInt(iCash, cl_customconfig.GetFloat('economy.goods_price_multiplier', 1.0))


def CreateGoodsByData(iGoodsSID, iGoodsType, iCash, iCashType, iCanBuy, dGoods, iHide):
    iCash = _ScaleGoodsCash(iCash)
    return cl_shop.goods.CWarGoods(iGoodsSID, iGoodsType, iCash, iCashType, iCanBuy, dGoods, iHide)


def CreateGoodsByConfig(iSID, iCash, iCashType, iCanBuy, iHide):
    clsData = cl_shop.goodsdata.GetGoodsData(iSID)
    if not clsData:
        return None
    iCash = _ScaleGoodsCash(iCash)
    oGoods = cl_shop.goods.CWarGoods(iSID, clsData.m_GoodsType, iCash, iCashType, iCanBuy, clsData.m_Items, iHide)
    return oGoods


def CreateRelifeGoods(oGame, iNpc, iHero, iCash, iCashType, iCanBuy, iPlayer):
    iCash = _ScaleGoodsCash(iCash)
    return cl_shop.goods.CRelifeGoods(oGame, iNpc, iHero, iCash, iCashType, iCanBuy, iPlayer)


def CreatePetGoods(oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
    iCash = _ScaleGoodsCash(iCash)
    return cl_shop.goods.CPetGoods(oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)


def CreateWandGoods(oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
    iCash = _ScaleGoodsCash(iCash)
    return cl_shop.goods.CWandGoods(oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)


def CreateCDiceGoods(oGame, iNpc, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
    iCash = _ScaleGoodsCash(iCash)
    return cl_shop.goods.CDiceGoods(oGame, iNpc, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)


def CreateRandGoods(iSID, iCash, iCashType, iCanBuy, iHide):
    clsData = cl_shop.goodsdata.GetGoodsData(iSID)
    if not clsData:
        return None
    iCash = _ScaleGoodsCash(iCash)
    oGoods = cl_shop.goods.CRandGoods(iSID, iCash, iCashType, iCanBuy, clsData.m_Items, iHide)
    return oGoods
