# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/shopnpc.pyc
# RelativePath: clientlogic/cl_npc/shopnpc.pyc
# Source Generated with Decompyle++
# File: shopnpc.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_SHOPREFRESH, VIRTUAL_ITEM_ATTR, VIRTUAL_ITEM_RELIFETEAM, NPC_CB_LIST, NPC_ACTION_SHOP, NWARRIOR_NPC, VIRTUAL_ITEM_RAREITEM, VIRTUAL_ITEM_RANDOM
from cl_only import ChooseKey, Functor
from cl_object.logging import WarshopLog
import cl_formula
import cllib.lib_flag
import cl_msgcenter
from . import mobject
from . import net

class CShopNpc(mobject.CNPC):
    m_Type = 'NPC'
    m_Delete = 1
    m_FightType = NWARRIOR_NPC
    m_InteractDis = 5
    m_CheckInteractDistance = False
    m_AddtionalRelicGoodsPos = (4, 5, 7, 8)
    m_DefaultRelicGoodsPos = (5, 8)
    m_ExtraRelicGoodsPos = (12,)
    m_MaxRelicGoods = 2
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_ActionType = NPC_ACTION_SHOP
        self.m_GoodsData = { }
        self.m_LockGoods = { }
        self.m_GoodsCache = { }
        self.m_GoodsSelloff = { }
        self.m_ExHeroRefreshInfo = { }
        self.m_ExFristRefreshCost = { }
        self.m_RareItemRecord = { }
        self.m_HeroMaxRelicGoods = { }

    
    def Release(self):
        super().Release()
        for dGoodsMenu in self.m_GoodsData.values():
            for oGoods in dGoodsMenu.values():
                oGoods.Disable()
            
        
        self.m_GoodsData = { }
        self.m_LockGoods = { }
        self.m_RareItemRecord = { }

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREINTERACTSHOP, oHero, {
            'InteractStatus': self.m_PlayerInteractStatus[pid],
            'ShopNpc': self.m_ID })
        self.SetHeroInteractStatus(pid)
        if oHero.m_ID not in self.m_GoodsData:
            self.m_GoodsCache = { }
            self.m_GoodsSelloff = { }
            if self.m_ActionFunc:
                self.m_ActionFunc(self, oHero)
            self.CalGoodsData(oHero)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INITGOODS, oHero, {
                'ShopNpc': self.m_ID,
                'GoodsMenu': self.m_GoodsData[oHero.m_ID] })
            self.CalSelloff(oHero)
        oHero.m_BuyMgr.SetInteractShopNpc(self.m_ID)
        net.GS2CNpcRefreshInfo(self, oHero)
        self.RefreshShopUI(oHero)
        self.SetNpcRefreshCallBackFunction(oHero)

    
    def StopInteract(self, oHero):
        oHero.m_BuyMgr.SetInteractShopNpc(0)

    
    def RefreshShopUI(self, oHero):
        lstMenu = oHero.m_BuyMgr.GetGoodsShowList(self.m_ID, self.m_GoodsData[oHero.m_ID])
        net.GS2CNpcShop(oHero, self.m_ID, lstMenu)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, Functor(BuyGoods, self.m_ID), self)

    
    def GetGoodsCacheData(self, iType, iHero = None):
        lstSID = []
        for dGoodsWeight in self.m_GoodsCache.values():
            for oGoods in dGoodsWeight:
                if oGoods.m_GoodsType != iType:
                    continue
                self._AddGoodsToLst(oGoods, lstSID)
            
        
        return lstSID

    
    def _AddGoodsToLst(self, oGoods, lstSID):
        if oGoods.m_Items:
            lstGoods = oGoods.m_Items
            for dGoods in lstGoods:
                if 'info' in dGoods and 'sid' in dGoods['info']:
                    lstSID.append(dGoods['info']['sid'])
            
        else:
            lstSID.append(oGoods.m_SID)

    
    def GetGoods(self, iType = 0):
        lstGoods = []
        for dGoodsWeight in self.m_GoodsCache.values():
            for oGoods in dGoodsWeight:
                if not iType:
                    lstGoods.append(oGoods)
                    continue
                if oGoods.m_GoodsType == iType:
                    lstGoods.append(oGoods)
            
        
        return lstGoods

    
    def SetGoods(self, iPos, iWeight, oGoods):
        if iPos not in self.m_GoodsCache:
            self.m_GoodsCache[iPos] = { }
        self.m_GoodsCache[iPos][oGoods] = iWeight
        oGoods.m_Pos = iPos

    
    def CalGoodsData(self, oHero):
        dGoodsMenu = { }
        for iPos, dPosData in self.m_GoodsCache.items():
            self.ChooseGoods(oHero, iPos, dGoodsMenu, dPosData)
        
        self.m_GoodsCache = { }
        self.m_GoodsData[oHero.m_ID] = dGoodsMenu

    
    def ShopRefresh(self, oHero):
        self.UpdateRefreshTimes(oHero, 1)
        self.m_GoodsCache = { }
        self.m_GoodsSelloff = { }
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        if oHero.m_ID in self.m_GoodsData:
            dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        else:
            dGoodsMenu = { }
            self.m_GoodsData[oHero.m_ID] = dGoodsMenu
        for iPos, oGoods in dGoodsMenu.items():
            if iPos not in self.m_GoodsCache:
                continue
            dPosData = self.m_GoodsCache.pop(iPos)
            if self.CanReplace(oHero, iPos, oGoods):
                oOldGoods = dGoodsMenu[iPos]
                oOldGoods.Disable()
                self.ChooseGoods(oHero, iPos, dGoodsMenu, dPosData)
                continue
            if oGoods.m_GoodsType == VIRTUAL_ITEM_RELIFETEAM:
                oOldGoods = dGoodsMenu[iPos]
                dGoodsMenu[iPos] = oOldGoods
        
        for iPos, dPosData in self.m_GoodsCache.items():
            self.ChooseGoods(oHero, iPos, dGoodsMenu, dPosData)
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHOPREFRESH, oHero, {
            'ShopNpc': self.m_ID,
            'GoodsMenu': dGoodsMenu })
        lstMenu = oHero.m_BuyMgr.GetGoodsShowList(self.m_ID, dGoodsMenu)
        self.m_GoodsCache = { }
        self.CalSelloff(oHero)
        net.GS2CNpcShop(oHero, self.m_ID, lstMenu)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, Functor(BuyGoods, self.m_ID), self)

    
    def ShopRefreshAllGoods(self, oHero):
        self.UpdateRefreshTimes(oHero, 1)
        self.m_GoodsCache = { }
        self.m_GoodsSelloff = { }
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        iHeroID = oHero.m_ID
        dGoodsMenu = self.m_GoodsData[iHeroID] if iHeroID in self.m_GoodsData else { }
        for iPos, oOldGoods in dGoodsMenu.items():
            if oOldGoods.m_GoodsType in (VIRTUAL_ITEM_SHOPREFRESH, VIRTUAL_ITEM_RELIFETEAM):
                self.m_GoodsCache.pop(iPos)
                continue
            oOldGoods.Disable()
        
        for iPos, dPosData in self.m_GoodsCache.items():
            self.ChooseGoods(oHero, iPos, dGoodsMenu, dPosData)
        
        lstMenu = oHero.m_BuyMgr.GetGoodsShowList(self.m_ID, dGoodsMenu)
        self.m_GoodsCache = { }
        self.CalSelloff(oHero)
        net.GS2CNpcShop(oHero, self.m_ID, lstMenu)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, Functor(BuyGoods, self.m_ID), self)

    
    def ChooseGoods(self, oHero, iPos, dGoodsMenu, dPosData):
        dWeight = oHero.Query('AddtionalGoodsWeight', { })
        if dWeight:
            if iPos not in self.m_ExtraRelicGoodsPos:
                lstForceRelicGoodsPos = oHero.Query('ForceRelicGoodsPos', [])
                bHasMaxRelicGoods = self.CheckHasMaxRelicGoods(oHero.m_ID, iPos, dGoodsMenu)
                bCanReplace = self.CheckCanReplaceRelicGoodsByPos(oHero, iPos, dGoodsMenu)
                dNewPosData = { }
                for oGoods in dPosData:
                    if bHasMaxRelicGoods or oGoods.m_GoodsType == VIRTUAL_ITEM_RELIC:
                        continue
                    if lstForceRelicGoodsPos:
                        if (iPos in lstForceRelicGoodsPos or bCanReplace) and oGoods.m_GoodsType != VIRTUAL_ITEM_RELIC:
                            continue
                    elif oGoods.m_GoodsType == VIRTUAL_ITEM_RELIC:
                        continue
                    if oGoods.m_GoodsType == VIRTUAL_ITEM_RELIC and iPos not in self.m_DefaultRelicGoodsPos:
                        continue
                    dNewPosData[oGoods] = dPosData[oGoods]
                    if oGoods.m_GoodsType in dWeight:
                        dNewPosData[oGoods] += dWeight[oGoods.m_GoodsType]
                
                if not dNewPosData:
                    WarshopLog.Alert('%s %s %s %s %s all goods was filter %s %s %s' % (self.m_Game.m_ID, self.m_SID, iPos, oHero.m_PlayerID, dPosData, lstForceRelicGoodsPos, bHasMaxRelicGoods, bCanReplace))
                    return None
                dPosData = dNewPosData
            else:
                for oGoods in dPosData:
                    if oGoods.m_GoodsType in dWeight:
                        dPosData[oGoods] += dWeight[oGoods.m_GoodsType]
                
        oChosonGoods = ChooseKey(self.m_Game, dPosData)
        if not oChosonGoods:
            WarshopLog.Alert('%s %s %s %s %s nogoods' % (self.m_Game.m_ID, self.m_SID, iPos, oHero.m_PlayerID, dPosData))
            return None
        self.OnChooseGoods(oHero, iPos, oChosonGoods)
        dGoodsMenu[iPos] = oChosonGoods
        for oGoods in dPosData:
            if oGoods != dGoodsMenu[iPos]:
                oGoods.Disable()
        

    
    def OnChooseGoods(self, oHero, iPos, oChosonGoods):
        pass

    
    def CanReplace(self, oHero, iPos, oGoods):
        if oGoods.m_CanBuy <= 0:
            return False
        if oGoods.m_GoodsType in (VIRTUAL_ITEM_ATTR, VIRTUAL_ITEM_SHOPREFRESH, VIRTUAL_ITEM_RELIFETEAM, VIRTUAL_ITEM_RANDOM):
            return False
        if oGoods.m_GoodsType in (VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_RAREITEM) and oHero.m_BuyMgr.IsGoodsSellOut(iPos, oGoods, self.m_ID):
            return False
        return True

    
    def SetSelloff(self, oHero, iPos, iDiscount):
        self.m_GoodsSelloff[iPos] = iDiscount

    
    def CalSelloff(self, oHero):
        dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        for iPos, iDiscount in self.m_GoodsSelloff.items():
            oGoods = dGoodsMenu[iPos]
            oGoods.SetDiscount(iDiscount)
        
        self.m_GoodsSelloff = { }

    
    def GetRefreshCost(self, oHero):
        dShopNpcRefreshInfo = oHero.Query('ShopNpcRefreshInfo', { })
        if not dShopNpcRefreshInfo:
            return -1
        iHero = oHero.m_ID
        sKey = dShopNpcRefreshInfo['Key']
        if iHero in self.m_ExFristRefreshCost and sKey in self.m_ExFristRefreshCost[iHero]:
            iFristValue = self.m_ExFristRefreshCost[iHero][sKey]
        else:
            iFristValue = cl_formula.GetFormulaResult(self, dShopNpcRefreshInfo['FristValue'], { })
            if iHero not in self.m_ExFristRefreshCost:
                self.m_ExFristRefreshCost[iHero] = { }
            self.m_ExFristRefreshCost[iHero][sKey] = iFristValue
        iMul = dShopNpcRefreshInfo['Mul']
        if iHero in self.m_ExHeroRefreshInfo:
            return iFristValue * iMul ** self.m_ExHeroRefreshInfo[iHero]
        return iFristValue

    
    def CheckCanReplaceRelicGoodsByPos(self, oHero, iCheckPos, dGoodsMenu):
        iCanReplaceNum = oHero.Query('CanReplaceRelicGoodsNum', 0)
        if not iCanReplaceNum:
            return False
        iNum = 0
        for iPos in self.m_AddtionalRelicGoodsPos:
            if iPos >= iCheckPos:
                break
            if iPos not in dGoodsMenu:
                continue
            oGoods = dGoodsMenu[iPos]
            if oGoods.m_GoodsType == VIRTUAL_ITEM_RELIC:
                iNum += 1
        
        return iCanReplaceNum > iNum

    
    def CheckHasMaxRelicGoods(self, iHero, iCheckPos, dGoodsMenu):
        iNum = 0
        for iPos in self.m_AddtionalRelicGoodsPos:
            if iPos == iCheckPos:
                continue
            if iPos not in dGoodsMenu:
                continue
            oGoods = dGoodsMenu[iPos]
            if oGoods.m_GoodsType == VIRTUAL_ITEM_RELIC:
                iNum += 1
        
        iMaxRelicNum = self.m_HeroMaxRelicGoods[iHero] if iHero in self.m_HeroMaxRelicGoods else self.m_MaxRelicGoods
        return iNum >= iMaxRelicNum

    
    def Refresh(self, oHero):
        iCost = self.GetRefreshCost(oHero)
        if iCost < 0:
            return None
        if iCost > oHero.m_WarCash:
            return None
        oHero.AddCash(-iCost, 'ShopRefreshCost')
        iHero = oHero.m_ID
        if iHero in self.m_ExHeroRefreshInfo:
            self.m_ExHeroRefreshInfo[iHero] += 1
        else:
            self.m_ExHeroRefreshInfo[iHero] = 1
        net.GS2CNpcRefreshInfo(self, oHero)
        self.ShopRefreshAllGoods(oHero)
        self.SetNpcRefreshCallBackFunction(oHero)

    
    def UpdateRefreshTimes(self, oHero, iCount):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        dTimes[oHero.m_ID] = iTimes + iCount
        self.Set('HeroRefreshTimes', dTimes)

    
    def LockGoods(self, oHero, iPos, iLock):
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iPos not in self.m_GoodsData[iHero]:
            return None
        oGoods = self.m_GoodsData[iHero][iPos]
        if oGoods.m_HasBuy >= oGoods.m_CanBuy:
            WarshopLog.Debug('%s %s locksoldgoods %s %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, oGoods.m_SID, iPos, iLock))
            return None
        WarshopLog.Debug('%s %s lockgoods %s %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, oGoods.m_SID, iPos, iLock))
        oGoods.SetLock(iLock)
        dLockGoods = self.m_LockGoods.setdefault(iHero, { })
        if iLock:
            dLockGoods[iPos] = oGoods
        else:
            dLockGoods.pop(iPos, None)
        net.GS2CNpcShopSingleChange(oHero, self.m_ID, oGoods, iPos)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, Functor(BuyGoods, self.m_ID), self)
        self.SetNpcRefreshCallBackFunction(oHero)

    
    def SetMaxRelicGoodsNum(self, iHero, iNum):
        self.m_HeroMaxRelicGoods[iHero] = iNum

    
    def ClearMaxRelicGoodsNum(self, iHero):
        self.m_HeroMaxRelicGoods.pop(iHero, 0)



class CGSCashShopNpc(CShopNpc):
    
    def ChooseGoods(self, oHero, iPos, dGoodsMenu, dPosData):
        dWeight = oHero.Query('AddtionalGoodsWeight', { })
        if dWeight:
            for oGoods in dPosData:
                if oGoods.m_GoodsType in dWeight:
                    dPosData[oGoods] += dWeight[oGoods.m_GoodsType]
            
        oChosonGoods = ChooseKey(self.m_Game, dPosData)
        if not oChosonGoods:
            WarshopLog.Alert('%s %s %s %s nogoods' % (self.m_Game.m_ID, self.m_SID, iPos, oHero.m_PlayerID))
            return None
        self.OnChooseGoods(oHero, iPos, oChosonGoods)
        dGoodsMenu[iPos] = oChosonGoods
        for oGoods in dPosData:
            if oGoods != dGoodsMenu[iPos]:
                oGoods.Disable()
        



def BuyGoods(iNpc, oHero, iPos, iReplacePos = 0):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    if not oNpc.ValidInteract(oHero):
        return None
    if oHero.m_ID not in oNpc.m_GoodsData or iPos not in oNpc.m_GoodsData[oHero.m_ID]:
        return None
    oGoods = oNpc.m_GoodsData[oHero.m_ID][iPos]
    oHero.m_BuyMgr.Buy(oGoods, iNpc, iPos, iReplacePos, Functor(BuyGoods2, iPos, iNpc))


def BuyGoods2(iPos, iNpc, oHero, bBuy):
    oNpc = oHero.m_Game.GetObject(iNpc)
    oGoods = oNpc.m_GoodsData[oHero.m_ID][iPos]
    if oNpc and bBuy:
        net.GS2CNpcShopSingleChange(oHero, iNpc, oGoods, iPos)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, Functor(BuyGoods, iNpc), oNpc)
        oNpc.SetNpcRefreshCallBackFunction(oHero)
    net.GS2CNpcShopInteractResult(oHero, oGoods, iPos, bBuy)


class CPhaseShopNpc(CShopNpc):
    m_CheckInteractDistance = False
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_Refreshing = 0
        oSurvivor = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivor:
            dLockGoods = oSurvivor.m_NpcRefreshMgr.PopNpcCustomData('ShopLockGoods', { })
            for dGoods in dLockGoods.values():
                for oGoods in dGoods.values():
                    oGoods.Enable()
                
            
            self.m_LockGoods.update(dLockGoods)

    
    def OnChooseGoods(self, oHero, iPos, oChosonGoods):
        if oChosonGoods.m_GoodsType == VIRTUAL_ITEM_RAREITEM:
            dRareItems = self.m_RareItemRecord.setdefault(oHero.m_ID, { })
            dRareItems[iPos] = oChosonGoods

    
    def CalGoodsData(self, oHero):
        dGoodsMenu = { }
        iHero = oHero.m_ID
        if iHero in self.m_LockGoods:
            dGoodsMenu.update(self.m_LockGoods[iHero])
        for iPos, dPosData in self.m_GoodsCache.items():
            if iPos in dGoodsMenu:
                continue
            self.ChooseGoods(oHero, iPos, dGoodsMenu, dPosData)
        
        self.m_GoodsCache = { }
        self.m_GoodsData[oHero.m_ID] = dGoodsMenu

    
    def ValidAction(self, oHero, dInfo):
        iRefresh = 0
        if dInfo and 'Refresh' in dInfo:
            iRefresh = dInfo['Refresh']
        return self.m_Refreshing == iRefresh

    
    def ShopRefresh(self, oHero):
        self.m_Refreshing = 1
        super().ShopRefresh(oHero)
        self.m_Refreshing = 0

    
    def CanReplace(self, oHero, iPos, oGoods):
        if oGoods.IsLock():
            return False
        if not (cllib.lib_flag.g_IsMobile) and oGoods.m_GoodsType == VIRTUAL_ITEM_RAREITEM and oHero.m_BuyMgr.IsGoodsSellOut(iPos, oGoods, self.m_ID):
            return False
        return True

    
    def GetGoodsCacheData(self, iType, iHero = None):
        lstSID = super().GetGoodsCacheData(iType)
        if iHero and iHero in self.m_LockGoods:
            for oGoods in self.m_LockGoods[iHero].values():
                if oGoods.m_GoodsType != iType:
                    continue
                self._AddGoodsToLst(oGoods, lstSID)
            
        if iType == VIRTUAL_ITEM_RAREITEM and iHero in self.m_RareItemRecord:
            for oGoods in self.m_RareItemRecord[iHero].values():
                self._AddGoodsToLst(oGoods, lstSID)
            
        return lstSID

    
    def Remove(self, sReason):
        oSurvivor = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivor:
            dLockGoods = { }
            for iHero, dGoods in self.m_LockGoods.items():
                dHeroGoods = { }
                for iPos, oGoods in dGoods.items():
                    if oGoods.IsLock():
                        dHeroGoods[iPos] = oGoods
                
                if dHeroGoods:
                    dLockGoods[iHero] = dHeroGoods
            
            if dLockGoods:
                oSurvivor.m_NpcRefreshMgr.SetNpcCustomData('ShopLockGoods', dLockGoods)
        super().Remove(sReason)


