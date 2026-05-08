# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/diceshopnpc.pyc
# RelativePath: clientlogic/cl_npc/diceshopnpc.pyc
# Source Generated with Decompyle++
# File: diceshopnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, DICETAG_WEAPON, DICETAG_PERFORM, DICETAG_OTHER, DICE_QUALITY_NORMAL, DICE_QUALITY_RARE, DICE_QUALITY_TALE, LEVEL_TYPE_FIGHT
from cl_commondefines import VIRTUAL_ITEM_DICE, OBTAIN_WARCASH, MAX_LAYER, LEVEL_TYPE_BOSS, DICESHOP_INITGOODS, DICESHOP_REFRESHGOODS, VIRTUAL_ITEM_DICEPACKET
from cl_commondefines import DICESHOP_BUY_DICEPACKET, DICESHOP_BUY_POINTDICE
from cl_object.logging import DiceLog
from cl_only import ChooseKey, DeepCopy
from cl_platformdata import GetDiceTagInfo, GetDiceTagListInfo, GetExcludeDiceQuality
from cl_container.dicecon import MAX_DICE_ENERGY
import cl_shop
import cl_dice
import cl_msgcenter
import cl_dice.net as dicenet
from . import mobject
from . import net
ENERGY_MAX = 200
SPECIALITEM_UNLIMITED_BUY = 99
DEFAULT_CANROLLTIMES = 1
DEFAULT_ROLLPOINT = 0
MIN_SPECIALITEM_CHOOSE = 2

class CDiceShopNpc(mobject.CNPC):
    m_GuaranteedDiceTag = (DICETAG_WEAPON, DICETAG_PERFORM, DICETAG_OTHER)
    m_DefaultDice = 51301
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_GoodsData = { }
        self.m_BaseDiceGoodsNum = 0
        self.m_BaseRefreshCount = 0
        self.m_NotSellOut = { }
        self.m_DiceProb = { }
        self.m_DefaultItem = { }
        self.m_RandomItem = { }
        self.m_RandomItemNum = 0
        self.m_DicePacketInfo = { }
        self.m_GoodQuality = { }
        self.m_DicePacketCache = { }
        self.m_ExcludePoints = { }
        self.m_DiceCashInfo = { }
        self.m_HeroDiceBuyTimes = { }

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        for dGoodsMenu in self.m_GoodsData.values():
            for oGoods in dGoodsMenu.values():
                oGoods.Disable()
            
        
        self.m_GoodsData = { }
        super().Release()

    
    def SetInitData(self, iBaseDiceGoodsNum, dDiceCashInfo, dGoodQuality, iBaseRefreshCount, dDicePacketInfo, dBossDicePacketInfo, dExcludePoints):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            DiceLog.Alert('%s setdiceinitdata not levelctrl' % oGame.m_ID)
            return None
        iLayer = min(MAX_LAYER, oLevelCtrl.m_LayerNum)
        if iLayer not in dGoodQuality:
            DiceLog.Alert('%s not layer in dicegoodquality %s %s' % (oGame.m_ID, iLayer, oLevelCtrl.m_LayerNum))
            return None
        dQualityInfo = dGoodQuality[iLayer]
        self.m_BaseDiceGoodsNum = iBaseDiceGoodsNum
        self.m_BaseRefreshCount = iBaseRefreshCount
        self.m_ExcludePoints = dExcludePoints
        self.m_DiceCashInfo = dDiceCashInfo
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_BOSS:
            if iLayer in dBossDicePacketInfo:
                self.m_DicePacketInfo = dBossDicePacketInfo[iLayer]
            self.m_GoodQuality = DeepCopy(dQualityInfo[LEVEL_TYPE_BOSS])
        elif iLayer in dDicePacketInfo:
            self.m_DicePacketInfo = dDicePacketInfo[iLayer]
        self.m_GoodQuality = DeepCopy(dQualityInfo[LEVEL_TYPE_FIGHT])
        iSumGoodsNum = 0
        for iQuality, iNum in self.m_GoodQuality.items():
            iTempSum = iSumGoodsNum + iNum
            if iTempSum > self.m_BaseDiceGoodsNum:
                DiceLog.Alert('%s %s setdiceinitdata goods num anomaly %s %s %s' % (oGame.m_ID, iLayer, iSumGoodsNum, iNum, self.m_BaseDiceGoodsNum))
                self.m_GoodQuality[iQuality] = self.m_BaseDiceGoodsNum - iSumGoodsNum
                iSumGoodsNum = self.m_BaseDiceGoodsNum
                continue
            iSumGoodsNum = iTempSum
        

    
    def InitGoodsInfo(self, oHero):
        self.ChooseDiceGoods(oHero)
        self.InitDicePacketGoods(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICESHOP, oHero, {
            'ShopNpc': self.m_ID }, iSub = DICESHOP_INITGOODS)

    
    def ChooseDiceGoods(self, oHero):
        if not oHero.Query('CanChooseDiceGoods', 0):
            return None
        oWarMgr = self.m_Game.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        iNum = oHero.Query('DiceSpecial1019', 0)
        if not iNum:
            iNum = self.m_BaseDiceGoodsNum
        dChooseDice = self.ChooseDice(oHero, iNum)
        for iPos, (iDice, iDiceQuality) in enumerate(dChooseDice):
            self.SetDiceGood(oHero, iPos, iDice, iDiceQuality, oDiceElement.GetTempPointRangeByQuality(iDiceQuality))
        
        iChooseNum = len(dChooseDice)
        if iChooseNum < iNum:
            DiceLog.Alert('%s %s dice num anomaly %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dChooseDice, iNum, iChooseNum))
            for iPos in range(iChooseNum, iNum):
                iGuaranteedQuality = self.GetGuaranteedQuality()
                self.SetDiceGood(oHero, iPos, self.m_DefaultDice, iGuaranteedQuality, oDiceElement.GetTempPointRangeByQuality(iGuaranteedQuality))
            

    
    def SetDiceGood(self, oHero, iPos, iDice, iDiceQuality, dPointRange):
        dGoods = self.GetDiceGoodInfo(iDice, iDiceQuality, dPointRange)
        if not dGoods:
            return None
        iGoodsType = VIRTUAL_ITEM_DICE
        oGoods = cl_shop.CreateCDiceGoods(self.m_Game, self.m_ID, oHero.m_ID, iDice, iGoodsType, self.GetGoodsCash(oHero, iDiceQuality, iGoodsType), OBTAIN_WARCASH, 1, [
            dGoods], iHide = 0)
        self.RollGoodsDice(oHero, oGoods, 'SetDiceGood')
        self.SetGoods(oHero, iPos, oGoods, bReplace = True)

    
    def GetDiceGoodInfo(self, iDice, iDiceQuality, dPointRange):
        dGoods = {
            'item': VIRTUAL_ITEM_DICE,
            'info': {
                'SID': iDice,
                'QL': iDiceQuality,
                'PR': dPointRange,
                'CRT': DEFAULT_CANROLLTIMES,
                'RP': DEFAULT_ROLLPOINT } }
        return dGoods

    
    def InitDicePacketGoods(self, oHero):
        self.SetGoodsData(oHero, 0, self.m_DicePacketInfo)

    
    def UpgradeDiceGood(self, oHero):
        dGoodsData = self.m_GoodsData
        if oHero.m_ID not in dGoodsData:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        iGoodsType = VIRTUAL_ITEM_DICE
        for iPos, oGoodsData in self.m_GoodsData[oHero.m_ID].items():
            dData = oGoodsData.m_Items[0]['info']
            if dData['item'] != iGoodsType:
                continue
            iQuality = dData['QL']
            if oGoodsData.m_HasBuy >= oGoodsData.m_CanBuy or iQuality == DICE_QUALITY_TALE:
                continue
            iSID = dData['SID']
            iQuality = iQuality + 1
            dGoods = self.GetDiceGoodInfo(iSID, iQuality, oDiceElement.GetTempPointRangeByQuality(iQuality))
            oGoods = cl_shop.CreateCDiceGoods(self.m_Game, self.m_ID, oHero.m_ID, iSID, iGoodsType, self.GetGoodsCash(oHero, iQuality, iGoodsType), OBTAIN_WARCASH, 1, [
                dGoods], iHide = 0)
            self.SetGoods(oHero, iPos, oGoods, bReplace = True)
        
        self.RefreshShopUI(oHero)

    
    def AddDicePacketGood(self, oHero, iSellOut, dPackageGoods):
        self.SetGoodsData(oHero, iSellOut, dPackageGoods)

    
    def SetGoodsData(self, oHero, iSellOut, dPackageGoods):
        dGoodsData = self.m_GoodsData.setdefault(oHero.m_ID, { })
        if dGoodsData:
            iCurPosMax = max(dGoodsData)
        else:
            iCurPosMax = 0
        iGoodsType = VIRTUAL_ITEM_DICEPACKET
        for idx, iGoodQuality in enumerate(dPackageGoods.values(), start = 1):
            dGoods = {
                'item': iGoodsType,
                'info': {
                    'QL': iGoodQuality,
                    'SO': iSellOut } }
            oGoods = cl_shop.CreateCDiceGoods(self.m_Game, self.m_ID, oHero.m_ID, 0, iGoodsType, self.GetGoodsCash(oHero, iGoodQuality, iGoodsType), OBTAIN_WARCASH, 1, [
                dGoods], iHide = 0)
            self.SetGoods(oHero, iCurPosMax + idx, oGoods, bReplace = True)
        

    
    def GetGoodsCash(self, oHero, iQuality, iGoodsType):
        iInitPrice = self.GetInitCashByQuality(iQuality)
        if iGoodsType == VIRTUAL_ITEM_DICE:
            return iInitPrice
        iBuyTimes = self.GetHeroDiceBuyTimes(oHero.m_ID, iQuality)
        return self.CalPacketGoodsCash(oHero, iQuality, iInitPrice, iBuyTimes)

    
    def GetNextTimePacketCash(self, oHero, iQuality, iGoodsType):
        if iGoodsType != VIRTUAL_ITEM_DICEPACKET:
            return 0
        iInitPrice = self.GetInitCashByQuality(iQuality)
        iBuyTimes = self.GetHeroDiceBuyTimes(oHero.m_ID, iQuality) + 1
        return self.CalPacketGoodsCash(oHero, iQuality, iInitPrice, iBuyTimes)

    
    def CalPacketGoodsCash(self, oHero, iQuality, iInitPrice, iBuyTimes):
        iInitPrice *= (100 + oHero.Query('S6PacketDicePriceIncrease', 100)) / 100
        iRoundInitPrice = min(round(iInitPrice), MAX_DICE_ENERGY)
        if not iBuyTimes:
            return iRoundInitPrice
        dRatio = self.m_DiceCashInfo.get('Ratio', { })
        if iQuality not in dRatio:
            return iRoundInitPrice
        dRatioTrigger = dRatio[iQuality]
        if not dRatioTrigger:
            return iRoundInitPrice
        dThreshold = self.m_DiceCashInfo.get('Threshold', { })
        if iQuality not in dThreshold:
            return iRoundInitPrice
        iThreshold = dThreshold[iQuality]
        if iBuyTimes <= iThreshold:
            iIncreaseRatio = 100 + iBuyTimes * dRatioTrigger[1]
        else:
            iIncreaseRatio = 100 + iThreshold * dRatioTrigger[1] + (iBuyTimes - iThreshold) * dRatioTrigger[2]
        return min(round(iInitPrice * iIncreaseRatio / 100), MAX_DICE_ENERGY)

    
    def GetInitCashByQuality(self, iQuality):
        dInitCash = self.m_DiceCashInfo.get('Init', { })
        if iQuality not in dInitCash:
            return 0
        return dInitCash[iQuality]

    
    def ChooseDice(self, oHero, iNum):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return { }
        iHero = oHero.m_ID
        iPlayer = oHero.m_PlayerID
        dAllDice = oDiceElement.GetAllUnLockDice(iPlayer)
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = min(MAX_LAYER, oLevelCtrl.m_LayerNum)
        dNotSellOut = DeepCopy(self.m_NotSellOut[iHero]) if iHero in self.m_NotSellOut else { }
        dNotSellOutQuality = { }
        for _, iQuality in dNotSellOut:
            if iQuality not in dNotSellOutQuality:
                dNotSellOutQuality[iQuality] = 1
                continue
            dNotSellOutQuality[iQuality] += 1
        
        dGoodQualityInfo = { }
        lstGoodsQuality = []
        dGoodQuality = self.m_GoodQuality
        iExtendGoodQualityCount = oHero.Query('DiceSpecial1019', 0)
        if iExtendGoodQualityCount:
            dGoodQuality = self.ExtendDiceQuality(oHero, dGoodQuality, iExtendGoodQualityCount)
        for iDiceQuality, iGoodsNum in dGoodQuality.items():
            if dNotSellOutQuality:
                if iDiceQuality not in dNotSellOutQuality:
                    continue
                iGoodsNum = min(iGoodsNum, dNotSellOutQuality[iDiceQuality])
            if not iGoodsNum:
                continue
            (dAllChooseWeight, dChooseWeight, dSoldOutDiceChooseWeight) = self.ChooseDiceByQuality(oHero, dAllDice, iLayer, iDiceQuality, dNotSellOut)
            if not dAllChooseWeight:
                continue
            dGoodQualityInfo[iDiceQuality] = {
                'AllChooseWeight': dAllChooseWeight,
                'ChooseWeight': dChooseWeight,
                'SoldOutDiceChooseWeight': dSoldOutDiceChooseWeight }
            lstCurQuality = [ iDiceQuality for _ in range(iGoodsNum) ]
            lstGoodsQuality.extend(lstCurQuality)
        
        if not lstGoodsQuality:
            return { }
        tGuaranteedDiceTag = self.m_GuaranteedDiceTag
        iGuaranteedDiceTagNum = len(tGuaranteedDiceTag)
        iGuaranteed = 1 if iNum >= iGuaranteedDiceTagNum else 0
        dDiceTagInfo = GetDiceTagInfo()
        setLeftGuaranteedDiceTag = set(tGuaranteedDiceTag)
        dChooseResult = { }
        for index, iDiceQuality in enumerate(lstGoodsQuality):
            if iGuaranteed and iNum - index <= len(setLeftGuaranteedDiceTag):
                iTag = setLeftGuaranteedDiceTag.pop()
                if iTag not in dDiceTagInfo or not dDiceTagInfo[iTag]:
                    DiceLog.Alert('%s %s no guaranteed tag dice %s' % (oGame.m_ID, iPlayer, iTag))
                    tKey = self.GetGuaranteedDice({
                        self.m_DefaultDice: 1 }, iDiceQuality, { })
                else:
                    tKey = self.GetGuaranteedDice(dDiceTagInfo[iTag], iDiceQuality, dNotSellOut)
            else:
                dCurQualityInfo = dGoodQualityInfo[iDiceQuality]
                dAllChooseWeight = dCurQualityInfo.get('AllChooseWeight', { })
                dChooseWeight = dCurQualityInfo.get('ChooseWeight', { })
                dSoldOutDiceChooseWeight = dCurQualityInfo.get('SoldOutDiceChooseWeight', { })
                if not dChooseWeight:
                    if dSoldOutDiceChooseWeight:
                        dChooseWeight = DeepCopy(dSoldOutDiceChooseWeight)
                    else:
                        dChooseWeight = DeepCopy(dAllChooseWeight)
                tKey = ChooseKey(oGame, dChooseWeight)
                dChooseWeight.pop(tKey, None)
            if not tKey:
                DiceLog.Alert('%s %s shop no choose dice %s %s' % (oGame.m_ID, iPlayer, index, iDiceQuality))
                continue
            setDiceTag = set(GetDiceTagListInfo(tKey[0]))
            setLeftGuaranteedDiceTag = setLeftGuaranteedDiceTag - setDiceTag
            dChooseResult[tKey] = 1
        
        return dChooseResult

    
    def ChooseDiceByQuality(self, oHero, dAllDice, iLayer, iDiceQuality, dNotSellOut):
        oGame = self.m_Game
        iPlayer = oHero.m_PlayerID
        dAllChooseWeight = { }
        dChooseWeight = { }
        dSoldOutDiceChooseWeight = { }
        for iDice in dAllDice:
            if iDice in GetExcludeDiceQuality(iDiceQuality):
                continue
            tKey = (iDice, iDiceQuality)
            dAllChooseWeight[tKey] = 1
            if tKey not in dNotSellOut:
                dChooseWeight[tKey] = 1
                continue
            dSoldOutDiceChooseWeight[tKey] = 1
        
        if not dAllChooseWeight:
            DiceLog.Alert('%s %s no info chooseweight %s %s %s' % (oGame.m_ID, iPlayer, iLayer, iDiceQuality, dAllDice))
            return ({ }, { }, { })
        return (dAllChooseWeight, dChooseWeight, dSoldOutDiceChooseWeight)

    
    def GetGuaranteedDice(self, dTagChooseDice, iDiceQuality, dNotSellOut):
        dChooseDice = { }
        dChooseWeight = { }
        for iDice in set(dTagChooseDice):
            if iDice in GetExcludeDiceQuality(iDiceQuality):
                continue
            tKey = (iDice, iDiceQuality)
            dChooseDice[tKey] = 1
            if tKey not in dNotSellOut:
                dChooseWeight[tKey] = 1
        
        if not dChooseDice:
            DiceLog.Alert('%s anomaly guaranteed dice %s %s' % (self.m_Game.m_ID, dTagChooseDice, dNotSellOut))
            return (self.m_DefaultDice, self.GetGuaranteedQuality())
        if not dChooseWeight:
            dChooseWeight = dChooseDice
        return ChooseKey(self.m_Game, dChooseWeight)

    
    def GetGuaranteedQuality(self):
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFirstHall():
            return DICE_QUALITY_NORMAL
        return DICE_QUALITY_RARE

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.SetHeroInteractStatus(pid)
        if oHero.m_ID not in self.m_GoodsData and self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        oHero.m_BuyMgr.SetInteractShopNpc(self.m_ID)
        self.RefreshShopUI(oHero)

    
    def SetGoods(self, oHero, iPos, oGoods, bReplace = False):
        dGoodsMenu = self.m_GoodsData.setdefault(oHero.m_ID, { })
        if not bReplace and iPos in dGoodsMenu:
            DiceLog.Alert('%s %s shop setrepeat %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu)))
            return None
        if iPos in dGoodsMenu and dGoodsMenu[iPos]:
            dGoodsMenu[iPos].Disable()
        dGoodsMenu[iPos] = oGoods
        oGoods.m_Pos = iPos

    
    def Refresh(self, oHero):
        if not self.CheckRefreshTimes(oHero):
            return None
        iRefreshCost = self.GetExtraRefreshCost(oHero)
        if iRefreshCost:
            if not self.CheckExtraRefresh(oHero, iRefreshCost):
                return None
            oDicecon = oHero.m_DiceCon
            oDicecon.ChangeDiceEnergy(-iRefreshCost, 'DiceShopRefresh')
        self.UpdateRefreshTimes(oHero, 1)
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iHeroID = oHero.m_ID
        if iHeroID in self.m_GoodsData:
            dGoodsMenu = self.m_GoodsData[iHeroID]
        else:
            dGoodsMenu = { }
            self.m_GoodsData[iHeroID] = dGoodsMenu
        dNotSellOut = { }
        dRefreshPos = { }
        for iPos, oGoods in dict(dGoodsMenu).items():
            if oGoods.m_GoodsType != VIRTUAL_ITEM_DICE:
                continue
            if oGoods.m_HasBuy < oGoods.m_CanBuy:
                dGoodInfo = oGoods.m_Items[0].get('info', { })
                dNotSellOut[(dGoodInfo.get('SID', 0), dGoodInfo.get('QL', 0))] = 1
                dRefreshPos[iPos] = 1
        
        self.m_NotSellOut[iHeroID] = dNotSellOut
        dNewChooseDice = self.ChooseDice(oHero, len(dRefreshPos))
        oDiceElement = oWarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        for iPos in dRefreshPos:
            tRemoveKey = ()
            for iDice, iDiceQuality in dNewChooseDice:
                tRemoveKey = (iDice, iDiceQuality)
                self.SetDiceGood(oHero, iPos, iDice, iDiceQuality, oDiceElement.GetTempPointRangeByQuality(iDiceQuality))
            
            if tRemoveKey:
                dNewChooseDice.pop(tRemoveKey)
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICESHOP, oHero, {
            'ShopNpc': self.m_ID }, iSub = DICESHOP_REFRESHGOODS)
        self.RefreshShopUI(oHero)

    
    def GetMaxRefreshTimes(self, oHero):
        return self.m_BaseRefreshCount + oHero.Query('DiceShopRefreshTimes', 0)

    
    def CheckRefreshTimes(self, oHero):
        iForceSetDiceShopRefreshUnLimit = oHero.Query('DiceSpecial1019', 0)
        if not iForceSetDiceShopRefreshUnLimit:
            dTimes = self.SetDefault('HeroRefreshTimes', { })
            iTimes = dTimes.setdefault(oHero.m_ID, 0)
            if iTimes >= self.GetMaxRefreshTimes(oHero):
                return False
        return True

    
    def UpdateRefreshTimes(self, oHero, iCount):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        dTimes[oHero.m_ID] = iTimes + iCount
        self.Set('HeroRefreshTimes', dTimes)

    
    def RefreshShopUI(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData:
            return None
        (lstDiceGoods, lstDicePacketGoods) = self.GetGoodsShowInfo(oHero, self.m_GoodsData[iHero])
        iForceSetDiceShopRefreshUnLimit = oHero.Query('DiceSpecial1019', 0)
        if iForceSetDiceShopRefreshUnLimit:
            iCanRefreshTimes = self.GetExtraRefreshCost(oHero)
            iMaxRefreshTimes = -1
        else:
            iMaxRefreshTimes = self.GetMaxRefreshTimes(oHero)
            if iMaxRefreshTimes > 0:
                dTimes = self.SetDefault('HeroRefreshTimes', { })
                iTimes = dTimes.setdefault(iHero, 0)
                iCanRefreshTimes = iMaxRefreshTimes - iTimes
            else:
                iCanRefreshTimes = 0
        net.GS2CDiceShop(oHero, self.m_ID, lstDiceGoods, iCanRefreshTimes, iMaxRefreshTimes, lstDicePacketGoods)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnSelectResult, self)
        self.SetNpcRefreshCallBackFunction(oHero)

    
    def GetGoodsShowInfo(self, oHero, dGoods):
        lstDiceGoods = []
        lstDicePacketGoods = []
        for iPos, oGoods in dGoods.items():
            if oGoods.IsHidden():
                continue
            dGoodInfo = oGoods.m_Items[0].get('info', { })
            iQuality = dGoodInfo.get('QL', 0)
            iCash = oGoods.GetCash()
            iSellOut = 1 if oGoods.m_HasBuy >= oGoods.m_CanBuy else 0
            iGoodsType = oGoods.m_GoodsType
            if iGoodsType == VIRTUAL_ITEM_DICE:
                iAbilitySID = dGoodInfo.get('SID', 0)
                dPointRange = dGoodInfo.get('PR', { })
                iRollPoint = dGoodInfo.get('RP', 0)
                lstGoodsInfo = []
                lstGoodsInfo = [
                    iPos,
                    iAbilitySID,
                    dPointRange,
                    iQuality,
                    iCash,
                    iSellOut,
                    iRollPoint]
                lstDiceGoods.append(lstGoodsInfo)
                continue
            if iGoodsType == VIRTUAL_ITEM_DICEPACKET:
                iNextTimeSellOut = dGoodInfo.get('SO', 0)
            iNextTimePacketCash = 0 if iNextTimeSellOut else self.GetNextTimePacketCash(oHero, iQuality, iGoodsType)
            lstDicePacketGoods.append([
                iPos,
                iQuality,
                iCash,
                iSellOut,
                iNextTimePacketCash])
        
        return (lstDiceGoods, lstDicePacketGoods)

    
    def AddHeroDiceBuyTimes(self, iHero, iQuality, iTimes):
        if iHero in self.m_HeroDiceBuyTimes:
            if iQuality in self.m_HeroDiceBuyTimes[iHero]:
                self.m_HeroDiceBuyTimes[iHero][iQuality] += iTimes
            else:
                self.m_HeroDiceBuyTimes[iHero][iQuality] = iTimes
        else:
            self.m_HeroDiceBuyTimes[iHero] = {
                iQuality: iTimes }

    
    def GetHeroDiceBuyTimes(self, iHero, iQuality):
        if iHero in self.m_HeroDiceBuyTimes and iQuality in self.m_HeroDiceBuyTimes[iHero]:
            return self.m_HeroDiceBuyTimes[iHero][iQuality]
        return 0

    
    def OnSelectResult(self, oHero, iPos):
        iHero = oHero.m_ID
        if iHero in self.m_GoodsData and iPos in self.m_GoodsData[iHero]:
            oGoods = self.m_GoodsData[iHero][iPos]
            if not self.CanBuy(oHero, oGoods):
                return None
            dGoodInfo = oGoods.m_Items[0].get('info', { })
            if oGoods.m_GoodsType == VIRTUAL_ITEM_DICE:
                self.DiceShopBuy(oHero, oGoods, dGoodInfo)
            elif oGoods.m_GoodsType == VIRTUAL_ITEM_DICEPACKET:
                self.DicePacketShopBuy(oHero, oGoods, dGoodInfo)
            elif iHero in self.m_DicePacketCache:
                self.SelectDice(oHero, iPos)
            elif iHero in self.m_GoodsData:
                pass
            
        lstGoodsData = []
        DiceLog.Alert('%s %s diceshop selecterr %s %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iHero, iPos, lstGoodsData, self.m_DicePacketCache))

    
    def DiceShopBuy(self, oHero, oGoods, dGoodInfo):
        DiceLog.Debug('%s %s buydice %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oGoods.m_Pos, oGoods.m_SID, dGoodInfo))
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return None
        iCostCash = oGoods.GetCash()
        oDiceCon.ChangeDiceEnergy(-iCostCash, 'DiceShopBuy')
        iShopRollTimes = dGoodInfo.get('diceshopnpcroll', 0)
        if iShopRollTimes:
            iCurCanRollTimes = dGoodInfo['CRT']
            dGoodInfo['CRT'] = 0 if iShopRollTimes >= iCurCanRollTimes else iCurCanRollTimes - iShopRollTimes
        oGoods.BuySuccess(oHero, oGoods.m_Items, 1)
        self.RefreshShopUI(oHero)
        iGoodsPoint = dGoodInfo.get('RP', 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICESHOP_BUY, oHero, {
            'ShopNpc': self.m_ID,
            'ChoosePoint': iGoodsPoint,
            'Cost': iCostCash }, iSub = DICESHOP_BUY_POINTDICE)

    
    def DicePacketShopBuy(self, oHero, oGoods, dGoodInfo):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        iQuality = dGoodInfo['QL']
        dPointRange = oDiceElement.GetTempPointRangeByQuality(iQuality)
        if 'DPI' in dGoodInfo:
            dDicePointsInfo = dGoodInfo['DPI']
        else:
            dAllDice = oDiceElement.GetAllUnLockDice(oHero.m_PlayerID)
            dExcludeDice = GetExcludeDiceQuality(iQuality)
            lstSelectionDice = list(dAllDice.keys() - dExcludeDice.keys())
            if not lstSelectionDice:
                return None
            oDiceCon = oHero.m_DiceCon
            if oDiceCon and oDiceCon.GetDicePacketPointsShowCnt():
                oDiceCon.ChangeDicePacketPointsShowCnt(-1)
                dDicePointsInfo = { }
                for iDice in lstSelectionDice:
                    iPoints = 0
                    dInfo = {
                        'SID': iDice,
                        'QL': iQuality,
                        'PR': dPointRange,
                        'CRT': DEFAULT_CANROLLTIMES,
                        'RP': DEFAULT_ROLLPOINT }
                    oDice = cl_dice.CreateDice(self.m_Game, None, dInfo)
                    if oDice:
                        lstResult = oDice.RollPoint(oHero, iResultNum = 1, dResultPoint = { }, iUseBaseWeight = 1)
                        if lstResult:
                            iPoints = lstResult[0]
                    if not iPoints:
                        DiceLog.Alert('%s %s dpshow err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iDice))
                        continue
                    dDicePointsInfo[iDice] = iPoints
                
                dGoodInfo['DPI'] = dDicePointsInfo
            else:
                dDicePointsInfo = dict.fromkeys(lstSelectionDice, 0)
        iSellOut = dGoodInfo['SO'] if 'SO' in dGoodInfo else 0
        dicenet.GS2CDiceSelectionPacketInfo(oHero, iQuality, dDicePointsInfo, dPointRange)
        self.m_DicePacketCache[oHero.m_ID] = [
            oGoods.m_Pos,
            iQuality,
            dDicePointsInfo,
            iSellOut]
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnSelectResult, self)

    
    def SelectDice(self, oHero, iDiceSID):
        (iGoodPos, iQuality, dDicePointsInfo, iSellOut) = self.m_DicePacketCache[oHero.m_ID]
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            DiceLog.Debug('%s %s selectdice conerr %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iDiceSID))
            return None
        if iDiceSID not in dDicePointsInfo:
            DiceLog.Debug('%s %s selectdice siderr %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iDiceSID, dDicePointsInfo))
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iGoodPos not in self.m_GoodsData[iHero]:
            DiceLog.Debug('%s %s selectdice gooderr %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iDiceSID, self.m_GoodsData))
            return None
        oGoods = self.m_GoodsData[iHero][iGoodPos]
        if not self.CanBuy(oHero, oGoods):
            DiceLog.Debug('%s %s selectdice notcanbuy %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iDiceSID, oDiceCon.GetDiceEnergy()))
            return None
        self.m_DicePacketCache.pop(oHero.m_ID)
        sReason = 'BuyDicePacket'
        DiceLog.Debug('%s %s dicepacket result %s %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iDiceSID, iQuality, dDicePointsInfo, sReason))
        iCostCash = oGoods.GetCash()
        oDiceCon.ChangeDiceEnergy(-iCostCash, 'SelectDice')
        dDiceInfo = oDiceCon.GetDiceInfo(iDiceSID, iQuality)
        if dDicePointsInfo[iDiceSID]:
            dDiceInfo['RP'] = dDicePointsInfo[iDiceSID]
            dDiceInfo['CRT'] = 0
            dDiceInfo['RewardEnergy'] = 1
        self.AddHeroDiceBuyTimes(iHero, iQuality, iTimes = 1)
        oGoods.BuySuccess(oHero, [], iSellOut)
        self.ClearPacketDicePointInfo(oGoods)
        oDiceCon.RewardDice(dDiceInfo, sReason, bAccumulatedRollPoint = True)
        self.RefreshShopUI(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICESHOP_BUY, oHero, {
            'ShopNpc': self.m_ID,
            'Quality': iQuality,
            'ChooseDice': iDiceSID,
            'Cost': iCostCash }, iSub = DICESHOP_BUY_DICEPACKET)

    
    def ClearPacketDicePointInfo(self, oGoods):
        dInfo = oGoods.m_Items[0].get('info', { })
        dInfo.pop('DPI', None)

    
    def CanBuy(self, oHero, oGoods):
        if not oGoods.CanBuy():
            return False
        if not (oGoods.m_CanBuy) or oGoods.m_HasBuy >= oGoods.m_CanBuy:
            return False
        if oGoods.IsHidden():
            return False
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return False
        if oDiceCon.GetDiceEnergy() < oGoods.GetCash():
            return False
        return True

    
    def OnStopInteract(self, oHero):
        oHero.m_BuyMgr.SetInteractShopNpc(0)

    
    def RollAllGoodsDice(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData:
            return None
        sReason = 'diceshopnpcroll'
        dGoods = self.m_GoodsData[iHero]
        for oGoods in dGoods.values():
            if oGoods.m_GoodsType != VIRTUAL_ITEM_DICE:
                continue
            if oGoods.IsHidden() or oGoods.m_HasBuy >= oGoods.m_CanBuy:
                continue
            self.RollGoodsDice(oHero, oGoods, sReason)
        
        self.RefreshShopUI(oHero)

    
    def RollGoodsDice(self, oHero, oGoods, sReason):
        dGoodInfo = oGoods.m_Items[0].get('info', { })
        oDice = cl_dice.CreateDice(self.m_Game, None, dGoodInfo)
        if not oDice:
            return None
        dExcludePoints = { }
        if 'Exclude' in dGoodInfo:
            iExclude = dGoodInfo['Exclude']
            dExcludePoints[iExclude] = 1
        iQuality = dGoodInfo['QL']
        if iQuality in self.m_ExcludePoints:
            dExcludePoints.update(self.m_ExcludePoints[iQuality])
        lstResult = oDice.RollPoint(oHero, iResultNum = 1, dResultPoint = { }, dExcludePoints = dExcludePoints, iUseBaseWeight = 1)
        if not lstResult:
            return None
        if sReason not in dGoodInfo:
            dGoodInfo[sReason] = 1
        else:
            dGoodInfo[sReason] += 1
        iPoint = oDice.SetPoint(lstResult[0], sReason)
        dGoodInfo['Exclude'] = iPoint
        dGoodInfo['RP'] = iPoint
        dGoodInfo['CRT'] = 0

    
    def CheckExtraRefresh(self, oHero, iRefreshCost):
        if oHero.m_DiceCon.GetDiceEnergy() < iRefreshCost:
            return False
        return True

    
    def GetExtraRefreshCost(self, oHero):
        iTimes = self.GetHeroRefreshTimes(oHero)
        iAddCostPer = oHero.Query('DiceSpecial1019AddPer', 2)
        iAddCost = oHero.Query('DiceSpecial1019AddCost', 1)
        return (iTimes // iAddCostPer) * iAddCost

    
    def GetHeroRefreshTimes(self, oHero):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        return iTimes

    
    def ExtendDiceQuality(self, oHero, dGoodQuality, iExtendGoodQualityCount):
        iCurGoodQualityCount = 0
        for iVal in dGoodQuality.values():
            iCurGoodQualityCount += iVal
        
        iExtraGoodQualityCount = iExtendGoodQualityCount - iCurGoodQualityCount
        iShouldAddGoodQualityCount = iExtraGoodQualityCount
        if iExtraGoodQualityCount <= 0:
            return dGoodQuality
        dResultGoodQuality = DeepCopy(dGoodQuality)
        for sKey in dResultGoodQuality:
            iAddGoodQualityCount = int((dResultGoodQuality[sKey] / iCurGoodQualityCount) * iShouldAddGoodQualityCount)
            if iAddGoodQualityCount:
                iExtraGoodQualityCount -= iAddGoodQualityCount
                dResultGoodQuality[sKey] += iAddGoodQualityCount
        
        if iExtraGoodQualityCount:
            oGame = self.m_Game
            iActualAddGoodQualityCount = iShouldAddGoodQualityCount - iExtraGoodQualityCount
            DiceLog.Alert('%s %s shouldaddgoodquality %s actualadd %s extendcnt %s goodquality %s' % (oGame.m_ID, oHero.m_PlayerID, iShouldAddGoodQualityCount, iActualAddGoodQualityCount, iExtendGoodQualityCount, str(dGoodQuality)))
            dGoodQualityChooseRatio = DeepCopy(dGoodQuality)
            for sKey in dGoodQualityChooseRatio:
                fAddGoodQualityCount = (dGoodQualityChooseRatio[sKey] / iCurGoodQualityCount) * iShouldAddGoodQualityCount
                dGoodQualityChooseRatio[sKey] = int(fAddGoodQualityCount * 100)
            
            for _ in range(iExtraGoodQualityCount):
                sKey = ChooseKey(oGame, dGoodQualityChooseRatio)
                dResultGoodQuality[sKey] += 1
            
        return dResultGoodQuality


