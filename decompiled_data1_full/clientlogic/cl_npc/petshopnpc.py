# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/petshopnpc.pyc
# RelativePath: clientlogic/cl_npc/petshopnpc.pyc
# Source Generated with Decompyle++
# File: petshopnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUELIST, PET_HANDLE_BUY, PET_HANDLE_SELL, PET_PUT_WAY_BUY, VIRTUAL_ITEM_PET
from cl_only import Functor, ChooseKey
from cl_object.logging import PetLog
import cl_formula
import cl_msgcenter
import cl_shop
import cl_pet
import cl_platformdata
from . import mobject
from . import net

class CPetShopNpc(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_SellPrice = 0
        self.m_GoodsData = { }
        self.m_SellQualityCoff = { }
        self.m_PetSellPriceCache = { }
        self.m_AttentionKey = 'PetShop%s' % self.m_ID
        self.m_Options = {
            PET_HANDLE_SELL: (self.SellPet, 2),
            PET_HANDLE_BUY: (self.BuyPet, 2) }
        self.m_GoodsNum = 0
        self.m_GoodsCashType = 0
        self.m_GoodsCash = 0
        self.m_GoodsQualityCoff = { }

    
    def InitGoodsInfo(self, oHero, iNum, iCashType, iCash, dQualityCoff):
        self.m_GoodsCashType = iCashType
        self.m_GoodsCash = iCash
        self.m_GoodsQualityCoff = dQualityCoff
        for iPos in range(iNum):
            self.ChooseGoods(oHero, iPos, False)
        

    
    def ChooseGoods(self, oHero, iPos, bReplace):
        oGame = self.m_Game
        dGoodsTypeWeight = cl_pet.GetPetTypeWeight(PET_PUT_WAY_BUY)
        oPetCon = oHero.m_PetCon
        if not oPetCon:
            return None
        if oPetCon.m_EggPriorType in dGoodsTypeWeight:
            dGoodsTypeWeight[oPetCon.m_EggPriorType] = oPetCon.GetPetShopTypeWeight()
        if not dGoodsTypeWeight:
            PetLog.Alert('%s petgoods no typeweight' % self.m_Game.m_ID)
            return None
        iType = ChooseKey(oGame, dGoodsTypeWeight)
        dGoodsPetPutWeight = cl_platformdata.GetPetBuyPutWeight()
        dPet = dGoodsPetPutWeight[iType]
        iSID = ChooseKey(oGame, dPet)
        oPet = cl_pet.CreatePet(oGame, oHero, iSID, PET_PUT_WAY_BUY, { })
        if not oPet:
            return None
        iQualityCoff = self.m_GoodsQualityCoff[oPet.m_Quality]
        iTrueCash = cl_formula.GetFormulaResult(oHero, self.m_GoodsCash, {
            'Npc': self.m_ID,
            'QualityCoff': iQualityCoff })
        dGoods = {
            'item': VIRTUAL_ITEM_PET,
            'info': {
                'sid': iSID,
                'item': oPet.m_ID,
                'data': { } } }
        oGoods = cl_shop.CreatePetGoods(oGame, oHero.m_ID, iSID, VIRTUAL_ITEM_PET, iTrueCash, self.m_GoodsCashType, 1, [
            dGoods], iHide = 0)
        self.SetGoods(oHero, iPos, oGoods, bReplace)

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        for iHero in self.m_PetSellPriceCache:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_ADD_PET, self.m_AttentionKey)
        
        for dGoodsMenu in self.m_GoodsData.values():
            for oGoods in dGoodsMenu.values():
                oGoods.Disable()
            
        
        self.m_FuseResult = { }
        self.m_GoodsData = { }
        self.m_Options = { }
        super().Release()

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.SetHeroInteractStatus(pid)
        if oHero.m_ID not in self.m_GoodsData and self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        self.RefreshShopUI(oHero)

    
    def ValidInteract(self, oHero):
        if not oHero.m_PetCon:
            return False
        if not super().ValidInteract(oHero):
            return False
        return True

    
    def SetGoods(self, oHero, iPos, oGoods, bReplace = False):
        dGoodsMenu = self.m_GoodsData.setdefault(oHero.m_ID, { })
        if not bReplace and iPos in dGoodsMenu:
            PetLog.Alert('%s %s shop setrepeat %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu)))
            return None
        dGoodsMenu[iPos] = oGoods
        oGoods.m_Pos = iPos

    
    def Refresh(self, oHero):
        if not self.CheckRefreshTimes(oHero):
            return None
        self.UpdateRefreshTimes(oHero, 1)
        if oHero.m_ID in self.m_GoodsData:
            dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        else:
            dGoodsMenu = { }
            self.m_GoodsData[oHero.m_ID] = dGoodsMenu
        for iPos, oGoods in dict(dGoodsMenu).items():
            if self.CanReplace(oHero, iPos, oGoods):
                oOldGoods = dGoodsMenu[iPos]
                oOldGoods.Disable()
                self.ChooseGoods(oHero, iPos, True)
        
        self.RefreshShopUI(oHero)

    
    def CheckRefreshTimes(self, oHero):
        iMaxRefreshTimes = oHero.Query('PetShopRefreshTimes', 0)
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

    
    def CanReplace(self, oHero, iPos, oGoods):
        iCanBuy = oGoods.m_CanBuy
        if iCanBuy <= 0 or oGoods.m_HasBuy >= iCanBuy:
            return False
        return True

    
    def RefreshShopUI(self, oHero):
        lstPetGoods = self.GetPetGoodsShowInfo(self.m_GoodsData[oHero.m_ID])
        iMaxRefreshTimes = oHero.Query('PetShopRefreshTimes', 0)
        if iMaxRefreshTimes > 0:
            dTimes = self.SetDefault('HeroRefreshTimes', { })
            iTimes = dTimes.setdefault(oHero.m_ID, 0)
            iCanRefreshTimes = iMaxRefreshTimes - iTimes
        else:
            iCanRefreshTimes = 0
        net.GS2CPetShop(oHero, self.m_ID, lstPetGoods, iMaxRefreshTimes, iCanRefreshTimes)
        net.GS2CPetSellPrice(oHero, self.m_ID, self.GetAllPetSellPrice(oHero))
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, Functor(PetShopInteractChooseOption, self.m_ID), self)
        if self.CheckRefreshTimes(oHero):
            self.SetNpcRefreshCallBackFunction(oHero)

    
    def GetPetGoodsShowInfo(self, dGoods):
        lstPetGoods = []
        for iPos, oGoods in dGoods.items():
            if oGoods.IsHidden():
                continue
            iTotalCash = oGoods.GetCash()
            iCanBuy = oGoods.m_CanBuy
            dShowInfo = oGoods.GetShowInfo()
            dOffset = dShowInfo['Offset']
            lstAllAttr = dShowInfo['AllAttr']
            lstAbility = dShowInfo['Ability']
            lstGoodsInfo = [
                iPos,
                oGoods.m_SID,
                iCanBuy,
                oGoods.m_HasBuy,
                oGoods.m_GoodsType,
                iTotalCash,
                dOffset,
                lstAllAttr,
                lstAbility]
            lstPetGoods.append(lstGoodsInfo)
        
        return lstPetGoods

    
    def SetSellPrice(self, iPrice, dQualityCoff):
        self.m_SellPrice = iPrice
        self.m_SellQualityCoff = dQualityCoff

    
    def GetAllPetSellPrice(self, oHero):
        dPrice = { }
        iHero = oHero.m_ID
        if iHero not in self.m_PetSellPriceCache:
            dCache = { }
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_ADD_PET, self.OnHeroAddPet, self.m_AttentionKey)
        else:
            dCache = self.m_PetSellPriceCache[iHero]
        for oPet in oHero.m_PetCon.GetAllPet():
            iPetID = oPet.m_ID
            if iPetID in dCache:
                dPrice[iPetID] = dCache[iPetID]
                continue
            dPrice[iPetID] = cl_formula.GetFormulaResult(oHero, self.m_SellPrice, {
                'QualityCoff': self.m_SellQualityCoff.get(oPet.m_Quality, 0) })
        
        self.m_PetSellPriceCache[iHero] = dPrice
        return dPrice

    
    def OnHeroAddPet(self, oListener, oHero, dMsgInfo):
        iPetID = dMsgInfo['TargetPet']
        oPet = self.m_Game.GetObject(iPetID)
        if oPet:
            dCache = self.m_PetSellPriceCache[oHero.m_ID]
            dCache[iPetID] = cl_formula.GetFormulaResult(oHero, self.m_SellPrice, {
                'QualityCoff': self.m_SellQualityCoff.get(oPet.m_Quality, 0) })
            net.GS2CPetSellPrice(oHero, self.m_ID, dCache)

    
    def ChooseOption(self, oHero, lstAnswer):
        if not self.ValidInteract(oHero):
            return None
        iOption = lstAnswer[0]
        if iOption not in self.m_Options:
            PetLog.Alert('%s %s petshop op err %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        (func, iMinLen) = self.m_Options[iOption]
        if len(lstAnswer) < iMinLen:
            PetLog.Alert('%s %s petshop res err %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        func(oHero, lstAnswer[1:])

    
    def BuyPet(self, oHero, lstAnswer):
        iHero = oHero.m_ID
        iPos = lstAnswer[0]
        if iHero not in self.m_GoodsData or iPos not in self.m_GoodsData[iHero]:
            return None
        oGoods = self.m_GoodsData[iHero][iPos]
        PetLog.Debug('%s %s buypet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, oGoods.m_SID))
        if self.CanBuy(oHero, oGoods):
            oHero.AddCash(-oGoods.GetCash(), 'BuyPet')
            oGoods.BuySuccess(oHero, oGoods.m_Items, 1)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, { }, iSub = PET_HANDLE_BUY)
        self.RefreshShopUI(oHero)

    
    def CanBuy(self, oHero, oGoods):
        if not oGoods.CanBuy():
            return False
        if oGoods.IsHidden():
            return False
        if oHero.m_WarCash < oGoods.GetCash():
            return False
        return True

    
    def SellPet(self, oHero, lstPet):
        iHero = oHero.m_ID
        if iHero not in self.m_PetSellPriceCache:
            return None
        oGame = self.m_Game
        oPetCon = oHero.m_PetCon
        dCachePrice = self.m_PetSellPriceCache[iHero]
        oCurPet = oPetCon.GetCurPet()
        iCurPet = oCurPet.m_ID if oCurPet else 0
        iCompanionPet = oPetCon.m_CompanionPet
        dTrueSell = { }
        for iPetID in lstPet:
            if iPetID not in oPetCon.m_Pet:
                PetLog.Alert('%s %s sell %d err %s %s' % (oGame.m_ID, oHero.m_PlayerID, iPetID, lstPet, list(oPetCon.m_Pet)))
                continue
            oSellPet = oPetCon.GetPetByID(iPetID)
            if oSellPet.GetLock():
                PetLog.Alert('%s %s sellLockPet %s' % (oGame.m_ID, oHero.m_PlayerID, iPetID))
                continue
            if iPetID == iCurPet or iPetID == iCompanionPet:
                PetLog.Alert('%s %s sellcurpet %d' % (oGame.m_ID, oHero.m_PlayerID, iPetID))
                continue
            if iPetID not in dCachePrice:
                PetLog.Alert('%s %s sell %d nocache %s' % (oGame.m_ID, oHero.m_PlayerID, iPetID, dCachePrice))
                continue
            dTrueSell[iPetID] = dCachePrice[iPetID]
        
        PetLog.Debug('%s %s sell %s' % (oGame.m_ID, oHero.m_PlayerID, dTrueSell))
        for iPetID in dTrueSell:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_PET, oHero, {
                'TargetPet': iPetID }, iSub = PET_HANDLE_SELL)
            oPetCon.RemovePet(iPetID, 'Sell')
        
        iTotalPrice = sum(dTrueSell.values())
        oHero.AddCash(iTotalPrice, 'SellPet')



def PetShopInteractChooseOption(iNpc, oHero, lstAnswer):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.ChooseOption(oHero, lstAnswer)

