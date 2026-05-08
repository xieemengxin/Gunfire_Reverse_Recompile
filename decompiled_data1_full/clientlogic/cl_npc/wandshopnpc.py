# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/wandshopnpc.pyc
# RelativePath: clientlogic/cl_npc/wandshopnpc.pyc
# Source Generated with Decompyle++
# File: wandshopnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, VIRTUAL_ITEM_WANDCARDPACK, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, WAND_CARDPACK, WANDPUT_SHOPBUY, LEVEL_TYPE_BOSS, WANDPUT_MAX_LAYER, WANDTAG_PERFORM, WANDTAG_WEAPON, WANDTAG_OTHER, WANDSHOP_REFRESHGOODS, WANDSHOP_INITGOODS, NPC_CB_VALUELIST, WAND_QUALITY_TALE, ROLLABILITY_OPTION, UNLOCK_WANDABILITY_SEASONTALENT
from cl_object.logging import WandLog
from cl_platformdata import GetWandCardPack, GetAllWandCompRarity, GetWandCompByTag
from cl_only import ChooseKey, DeepCopy
from cl_cscommondef import SHOP_ITEM_CHANGE_REASON_NONE
import cl_shop
import cl_wand
import cl_msgcenter
import cl_notify
from . import mobject
from . import net
REFRESH_SUC_NOTIFY = 2108

class CWandShopNpc(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_GoodsData = { }
        self.m_WandCash = 0
        self.m_ExtraWandCash = 0
        self.m_ExtraCompCash = 0
        self.m_WandQualityWeight = { }
        self.m_CompQualityWeight = { }
        self.m_QualityRatio = { }
        self.m_WandCompByRarity = { }
        self.m_GuaranteeCompTag = { }
        self.m_GuaranteeCount = 0
        self.m_WandShopPut = { }
        self.m_WandCompShopPut = { }
        self.m_InitRollInfo = { }
        self.m_RollInfo = { }

    
    def SetHeroGuaranteeCompTag(self, iPlayer):
        self.m_GuaranteeCompTag[iPlayer] = dict.fromkeys([
            WANDTAG_PERFORM,
            WANDTAG_WEAPON,
            WANDTAG_OTHER], self.m_GuaranteeCount)

    
    def InitGoodsInfo(self, oHero, dLevel, iWandCash, dWandQualityWeight, dCompQualityWeight, iExtraWandNum, iExtraWandCash, iExtraWandCompNum, iExtraCompCash, dQuality, iGuarantee):
        self.m_WandCash = iWandCash
        self.m_ExtraWandCash = iExtraWandCash
        self.m_ExtraCompCash = iExtraCompCash
        self.m_WandQualityWeight = dWandQualityWeight
        self.m_CompQualityWeight = dCompQualityWeight
        self.m_QualityRatio = dQuality
        self.m_GuaranteeCount = iGuarantee
        iPlayer = oHero.m_PlayerID
        self.m_WandCompByRarity[iPlayer] = DeepCopy(GetAllWandCompRarity())
        self.SetHeroGuaranteeCompTag(iPlayer)
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oWandElement = oWarMgr.GetWandElement()
        if not oWandElement:
            return None
        self.m_WandShopPut[iPlayer] = oWandElement.GetWandPutWithFilter(iPlayer, WANDPUT_SHOPBUY)
        self.m_WandCompShopPut[iPlayer] = oWandElement.GetShopWandCompPut(iPlayer)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        iLayer = min(WANDPUT_MAX_LAYER, oLevelCtrl.m_LayerNum)
        dExtraShopGoodsNum = oHero.Query('AddWandShopGoodsExtraGoodsNum', { })
        iExtraWandNum = iExtraWandNum + (dExtraShopGoodsNum[VIRTUAL_ITEM_WAND] if VIRTUAL_ITEM_WAND in dExtraShopGoodsNum else 0)
        iExtraWandCompNum = iExtraWandCompNum + (dExtraShopGoodsNum[VIRTUAL_ITEM_WANDCOMP] if VIRTUAL_ITEM_WANDCOMP in dExtraShopGoodsNum else 0)
        iPos = 0
        iBossLevel = 0
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_BOSS:
            iBossLevel = 1
            iLayer = min(WANDPUT_MAX_LAYER, iLayer + 1)
        if iBossLevel or oHero.Query('UnlockWandCardPack'):
            dWandCardPack = GetWandCardPack()
            if WAND_CARDPACK in dWandCardPack:
                iPos = self.OnSetWandCardPack(oHero, dWandCardPack, dLevel, iLayer, iPos)
        for iPos in range(iPos + 1, iExtraWandNum + iPos + 1):
            self.OnSetExtraWandGoods(oHero, iPos, iLayer, bReplace = False)
        
        dChangeWandShopWandComp = oHero.Query('ChangeWandShopWandComp', { })
        dExcludeComp = { }
        for iOffset in range(1, iExtraWandCompNum + 1):
            if iBossLevel and iOffset in dChangeWandShopWandComp:
                tOrderInfo = dChangeWandShopWandComp[iOffset]
            else:
                tOrderInfo = (0, SHOP_ITEM_CHANGE_REASON_NONE)
            (iWandComp, iRarity) = self.OnSetExtraWandCompGoods(oHero, iOffset + iPos, iLayer, bReplace = False, tOrderInfo = tOrderInfo, iBossLevel = iBossLevel, dExclude = dExcludeComp)
            if iRarity not in dExcludeComp:
                dExcludeComp[iRarity] = {
                    iWandComp: 1 }
                continue
            dExcludeComp[iRarity][iWandComp] = 1
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDSHOP, oHero, {
            'WandComp': dExcludeComp }, iSub = WANDSHOP_INITGOODS)
        if dExcludeComp:
            WandLog.Debug('%s %s wandshop initgoods %s' % (oGame.m_ID, iPlayer, dExcludeComp))

    
    def OnSetWandCardPack(self, oHero, dWandCardPack, dLevel, iLayer, iCurPos):
        dCardPack = dWandCardPack[WAND_CARDPACK]
        if dCardPack:
            iGoodsType = VIRTUAL_ITEM_WANDCARDPACK
            iLevel = dLevel[iLayer]
            iRatio = self.m_QualityRatio[iLevel] if iLevel in self.m_QualityRatio else 1
            iCash = self.m_WandCash * iRatio
            dGoods = {
                'item': iGoodsType,
                'info': {
                    'type': WAND_CARDPACK,
                    'level': iLevel,
                    'Npc': self.m_ID,
                    'data': { } } }
            iCurPos += 1
            oGoods = cl_shop.CreateWandGoods(self.m_Game, oHero.m_ID, list(dCardPack.keys())[0], iGoodsType, iCash, 0, 1, [
                dGoods], 0)
            self.SetGoods(oHero, iCurPos, oGoods)
        return iCurPos

    
    def OnSetExtraWandGoods(self, oHero, iCurPos, iLayer, bReplace):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_WandShopPut or not self.m_WandShopPut[iPlayer]:
            return None
        oGame = self.m_Game
        iGoodsType = VIRTUAL_ITEM_WAND
        dWeight = self.m_WandQualityWeight[iLayer]
        iWand = ChooseKey(oGame, self.m_WandShopPut[iPlayer])
        iLevel = ChooseKey(oGame, dWeight)
        iRatio = self.m_QualityRatio[iLevel] if iLevel in self.m_QualityRatio else 1
        dWandGoods = {
            'item': iGoodsType,
            'info': {
                'sid': iWand,
                'level': iLevel,
                'Npc': self.m_ID,
                'data': { },
                'ChangeReason': SHOP_ITEM_CHANGE_REASON_NONE } }
        oGoods = cl_shop.CreateWandGoods(oGame, oHero.m_ID, iWand, iGoodsType, self.m_ExtraWandCash * iRatio, 0, 1, [
            dWandGoods], 0)
        self.SetGoods(oHero, iCurPos, oGoods, bReplace)

    
    def OnSetExtraWandCompGoods(self, oHero, iCurPos, iLayer, bReplace, tOrderInfo, iBossLevel = 0, dExclude = None):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_WandCompShopPut or not self.m_WandCompShopPut[iPlayer]:
            return (0, 0)
        oGame = self.m_Game
        iGoodsType = VIRTUAL_ITEM_WANDCOMP
        (iOrderRarity, iChangeReason) = tOrderInfo
        if not iOrderRarity:
            dWandCompQualityWeight = oHero.Query('ReplaceWandShopWandCompWeight', { })
            if not iBossLevel or not dWandCompQualityWeight or iLayer not in dWandCompQualityWeight:
                dWandCompQualityWeight = self.m_CompQualityWeight
            iOrderRarity = ChooseKey(oGame, dWandCompQualityWeight[iLayer])
            iChangeReason = SHOP_ITEM_CHANGE_REASON_NONE
        iPlayer = oHero.m_PlayerID
        lstRarityComp = self.m_WandCompByRarity.get(iPlayer, { }).get(iOrderRarity, [])
        setRarityChoose = set(self.m_WandCompShopPut[iPlayer]) & set(lstRarityComp)
        setChoose = self.CheckGuaranteeCompTag(oGame, iPlayer, setRarityChoose)
        iHasExclude = 0
        if dExclude and iOrderRarity in dExclude:
            iHasExclude = 1
            setChoose -= set(dExclude[iOrderRarity])
        if not setChoose:
            setChoose = setRarityChoose
            if iHasExclude:
                setExcludeChoose = setChoose - set(dExclude[iOrderRarity])
                if setExcludeChoose:
                    setChoose = setExcludeChoose
            WandLog.Debug('%s %s shop guarantee choose %s %s' % (oGame.m_ID, iPlayer, setChoose, dExclude))
        dWandCompWeight = dict.fromkeys(setChoose, 1)
        if not dWandCompWeight:
            WandLog.Debug('%s %s shop no shopwandcomp %s %s' % (oGame.m_ID, iPlayer, setChoose, iOrderRarity))
            return (0, 0)
        iWandComp = ChooseKey(oGame, dWandCompWeight)
        iCompRatio = self.m_QualityRatio[iOrderRarity] if iOrderRarity in self.m_QualityRatio else 1
        dCompGoods = {
            'item': iGoodsType,
            'info': {
                'sid': iWandComp,
                'level': iOrderRarity,
                'Npc': self.m_ID,
                'data': { },
                'ChangeReason': iChangeReason } }
        oGoods = cl_shop.CreateWandGoods(oGame, oHero.m_ID, iWandComp, iGoodsType, self.m_ExtraCompCash * iCompRatio, 0, 1, [
            dCompGoods], 0)
        self.SetGoods(oHero, iCurPos, oGoods, bReplace)
        return (iWandComp, iOrderRarity)

    
    def CheckGuaranteeCompTag(self, oGame, iPlayer, setChoose):
        setNewChoose = set()
        if iPlayer in self.m_GuaranteeCompTag and self.m_GuaranteeCompTag[iPlayer]:
            dGuaranteeCompTag = self.m_GuaranteeCompTag[iPlayer]
            iTag = ChooseKey(oGame, dGuaranteeCompTag)
            if dGuaranteeCompTag[iTag] <= 1:
                dGuaranteeCompTag.pop(iTag)
            else:
                dGuaranteeCompTag[iTag] -= 1
            setNewChoose = setChoose & set(GetWandCompByTag(iTag))
        return setNewChoose

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        for dGoodsMenu in self.m_GoodsData.values():
            for oGoods in dGoodsMenu.values():
                oGoods.Disable()
            
        
        self.m_GoodsData = { }
        super().Release()

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.SetHeroInteractStatus(pid)
        if oHero.m_ID not in self.m_GoodsData and self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        oHero.m_BuyMgr.SetInteractShopNpc(self.m_ID)
        self.RefreshShopUI(oHero)
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if oWandElement:
            oWandElement.SendWandCardPack(oHero, self.m_ID)
        self.SendWandShopRollInfo(oHero)

    
    def SetGoods(self, oHero, iPos, oGoods, bReplace = False):
        dGoodsMenu = self.m_GoodsData.setdefault(oHero.m_ID, { })
        if not bReplace and iPos in dGoodsMenu:
            WandLog.Alert('%s %s shop setrepeat %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu)))
            return None
        if iPos in dGoodsMenu and dGoodsMenu[iPos]:
            dGoodsMenu[iPos].Disable()
        dGoodsMenu[iPos] = oGoods
        oGoods.m_Pos = iPos

    
    def Refresh(self, oHero):
        if not self.CheckRefreshTimes(oHero):
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        iLayer = min(WANDPUT_MAX_LAYER, oLevelCtrl.m_LayerNum)
        self.UpdateRefreshTimes(oHero, 1)
        if oHero.m_ID in self.m_GoodsData:
            dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        else:
            dGoodsMenu = { }
            self.m_GoodsData[oHero.m_ID] = dGoodsMenu
        iCompPosIndex = 1
        dChangeWandShopWandComp = oHero.Query('ChangeWandShopWandComp', { })
        iBossLevel = 0
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_BOSS:
            iBossLevel = 1
        dExcludeComp = { }
        iPlayer = oHero.m_PlayerID
        self.SetHeroGuaranteeCompTag(iPlayer)
        self.ClearRefreshRecord(oHero, dGoodsMenu)
        for iPos, oGoods in dGoodsMenu.items():
            if not self.CanReplace(oHero, iPos, oGoods):
                continue
            if oGoods.m_GoodsType == VIRTUAL_ITEM_WAND:
                self.OnSetExtraWandGoods(oHero, iPos, iLayer, bReplace = True)
                continue
            if (oGoods.m_GoodsType == VIRTUAL_ITEM_WANDCOMP or iBossLevel) and iCompPosIndex in dChangeWandShopWandComp:
                tOrderInfo = dChangeWandShopWandComp[iCompPosIndex]
            else:
                tOrderInfo = (0, SHOP_ITEM_CHANGE_REASON_NONE)
            iCompPosIndex += 1
            (iWandComp, iRarity) = self.OnSetExtraWandCompGoods(oHero, iPos, iLayer, bReplace = True, tOrderInfo = tOrderInfo, iBossLevel = iBossLevel, dExclude = dExcludeComp)
            if iRarity not in dExcludeComp:
                dExcludeComp[iRarity] = {
                    iWandComp: 1 }
                continue
            dExcludeComp[iRarity][iWandComp] = 1
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDSHOP, oHero, {
            'WandComp': dExcludeComp }, iSub = WANDSHOP_REFRESHGOODS)
        if dExcludeComp:
            WandLog.Debug('%s %s wandshop refreshgoods %s' % (oGame.m_ID, iPlayer, dExcludeComp))
        self.RefreshShopUI(oHero)
        cl_notify.SendCommonNotify(oHero.m_Game, [
            oHero.m_PlayerID], REFRESH_SUC_NOTIFY, { })

    
    def ClearRefreshRecord(self, oHero, dGoodsMenu):
        iPlayer = oHero.m_PlayerID
        for iPos, oGoods in dGoodsMenu.items():
            if not self.CanReplace(oHero, iPos, oGoods):
                continue
            oOldGoods = dGoodsMenu[iPos]
            iRefreshSID = oOldGoods.m_SID
            iRefreshLevel = oOldGoods.m_Items[0].get('info', { }).get('level', 0)
            if iPlayer in self.m_WandCompByRarity and iRefreshLevel in self.m_WandCompByRarity[iPlayer] and iRefreshSID in self.m_WandCompByRarity[iPlayer][iRefreshLevel]:
                self.m_WandCompByRarity[iPlayer][iRefreshLevel].remove(iRefreshSID)
        

    
    def CanReplace(self, oHero, iPos, oGoods):
        if oGoods.m_GoodsType == VIRTUAL_ITEM_WANDCARDPACK:
            return False
        iCanBuy = oGoods.m_CanBuy
        if iCanBuy <= 0 or oGoods.m_HasBuy >= iCanBuy:
            return False
        return True

    
    def CheckRefreshTimes(self, oHero):
        iMaxRefreshTimes = oHero.Query('WandShopRefreshTimes', 0)
        if not iMaxRefreshTimes:
            return False
        dTimes = self.SetDefault('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        if iTimes >= iMaxRefreshTimes:
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
        lstWandGoods = self.GetWandGoodsShowInfo(self.m_GoodsData[iHero])
        iMaxRefreshTimes = oHero.Query('WandShopRefreshTimes', 0)
        if iMaxRefreshTimes > 0:
            dTimes = self.SetDefault('HeroRefreshTimes', { })
            iTimes = dTimes.setdefault(iHero, 0)
            iCanRefreshTimes = iMaxRefreshTimes - iTimes
        else:
            iCanRefreshTimes = 0
        net.GS2CWandShop(oHero, self.m_ID, lstWandGoods, iCanRefreshTimes, iMaxRefreshTimes)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnSelectResult, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, self.RollWandAbility, self)
        if self.CheckRefreshTimes(oHero):
            self.SetNpcRefreshCallBackFunction(oHero)

    
    def GetWandGoodsShowInfo(self, dGoods):
        lstWandGoods = []
        for iPos, oGoods in dGoods.items():
            if oGoods.IsHidden():
                continue
            iTotalCash = oGoods.GetCash()
            iSellOut = 1 if oGoods.m_HasBuy >= oGoods.m_CanBuy else 0
            iLevel = oGoods.m_Items[0].get('info', { }).get('level', 0)
            iChangeReason = oGoods.m_Items[0].get('info', { }).get('ChangeReason', SHOP_ITEM_CHANGE_REASON_NONE)
            lstGoodsInfo = [
                iPos,
                oGoods.m_GoodsType,
                oGoods.m_SID,
                iTotalCash,
                iSellOut,
                iLevel,
                iChangeReason]
            lstWandGoods.append(lstGoodsInfo)
        
        return lstWandGoods

    
    def OnSelectResult(self, oHero, iPos):
        if iPos >= ROLLABILITY_OPTION:
            self.SelectRollResult(oHero, iPos)
        else:
            self.WandShopBuy(oHero, iPos)

    
    def WandShopBuy(self, oHero, iPos):
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iPos not in self.m_GoodsData[iHero]:
            return None
        oGoods = self.m_GoodsData[iHero][iPos]
        if self.CanBuy(oHero, oGoods):
            WandLog.Debug('%s %s wandshopbuy %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, oGoods.m_GoodsType, oGoods.m_SID))
            iGoodPrice = oGoods.GetCash()
            oHero.AddCash(-iGoodPrice, 'WandShopBuy')
            oGoods.BuySuccess(oHero, oGoods.m_Items, 1)
            iLevel = oGoods.m_Items[0].get('info', { }).get('level', 0)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDSHOP_BUY, oHero, {
                'ShopNpc': self.m_ID,
                'ItemType': oGoods.m_GoodsType,
                'ItemSID': oGoods.m_SID,
                'Rarity': iLevel,
                'Cost': iGoodPrice })

    
    def CanBuy(self, oHero, oGoods):
        if not oGoods.CanBuy():
            return False
        if not (oGoods.m_CanBuy) or oGoods.m_HasBuy >= oGoods.m_CanBuy:
            return False
        if oGoods.IsHidden():
            return False
        if oHero.m_WarCash < oGoods.GetCash():
            return False
        return True

    
    def OnStopInteract(self, oHero):
        oHero.m_BuyMgr.SetInteractShopNpc(0)

    
    def InitAbilityRollInfo(self, dInfo):
        self.m_InitRollInfo = dInfo

    
    def RollWandAbility(self, oHero, lstAnswer):
        if not oHero.HasSeasonTalent(UNLOCK_WANDABILITY_SEASONTALENT):
            WandLog.Alert('%s %s roll notalent' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        if len(lstAnswer) != 2:
            WandLog.Alert('%s %s roll numerr %s' % (self.m_Game.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            WandLog.Alert('%s %s roll nowandcon' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        (iRollWand, iConsumeWand) = lstAnswer
        oRollWand = oWandCon.GetWandByID(iRollWand)
        if not oRollWand or oRollWand.GetWandQuality() != WAND_QUALITY_TALE:
            WandLog.Alert('%s %s roll rollwanderr %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iRollWand))
            return None
        oConsumeWand = oWandCon.GetWandByID(iConsumeWand)
        if not oConsumeWand:
            WandLog.Alert('%s %s roll notconsumewand %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iConsumeWand))
            return None
        if oRollWand.m_SID not in (oConsumeWand.m_SID, oConsumeWand.m_EvolutionTarget):
            WandLog.Alert('%s %s roll consumewanderr %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oRollWand.m_SID, oConsumeWand.m_SID, oConsumeWand.m_EvolutionTarget))
            return None
        iConsumeWandQuality = oConsumeWand.GetWandQuality()
        if iConsumeWandQuality not in self.m_InitRollInfo:
            WandLog.Alert('%s %s roll consumewandqualityerr %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oConsumeWand.m_SID, iConsumeWandQuality, self.m_InitRollInfo.keys()))
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDSHOP_BEFORE_ROLL, oHero, {
            'RollWand': oRollWand,
            'ConsumeWandQuality': iConsumeWandQuality })
        oWandCon.RemoveWand(iConsumeWand, sReason = 'RollWandAbility', iDrop = 0)
        dRollInfo = self.m_InitRollInfo[iConsumeWandQuality]
        iOptionNum = dRollInfo['OptionNum']
        iNegativeRatio = dRollInfo['NegativeRatio']
        dCertainlyQuality = dRollInfo['Certainl']
        dHasNegativeyWeight = dRollInfo['HasNegative']
        dNotNegativeyWeight = dRollInfo['NotNegative']
        iPointAbilityWeight = dRollInfo['PointAbilityWeight']
        if iConsumeWandQuality == WAND_QUALITY_TALE and 'LockWeight' in dRollInfo:
            dLockAppointWeight = dRollInfo['LockWeight']
        else:
            dLockAppointWeight = { }
        dRollAbility = oWandCon.GetWandRollAbility(iRollWand, iOptionNum, iNegativeRatio, dHasNegativeyWeight, dNotNegativeyWeight, dCertainlyQuality, iPointAbilityWeight, dLockAppointWeight)
        self.m_RollInfo[oHero.m_ID] = (iRollWand, dRollAbility)
        net.GS2CWandShopRollInfo(oHero, iRollWand, dRollAbility)

    
    def SelectRollResult(self, oHero, iOption):
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_RollInfo:
            return None
        (iRollWand, dRollAbility) = self.m_RollInfo.pop(iHero)
        if iOption == ROLLABILITY_OPTION:
            return None
        if iOption not in dRollAbility:
            return None
        lstAbility = dRollAbility[iOption]
        oWandCon.SetWandAbility(iRollWand, lstAbility, 'RollWandAbility')

    
    def SendWandShopRollInfo(self, oHero):
        if oHero.m_ID not in self.m_RollInfo:
            return None
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        (iRollWand, dRollAbility) = self.m_RollInfo[oHero.m_ID]
        oRollWand = oWandCon.GetWandByID(iRollWand)
        if not oRollWand:
            self.m_RollInfo.pop(oHero.m_ID)
            return None
        net.GS2CWandShopRollInfo(oHero, iRollWand, dRollAbility)


