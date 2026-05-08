# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_shop/herobuy.pyc
# RelativePath: clientlogic/cl_shop/herobuy.pyc
# Source Generated with Decompyle++
# File: herobuy.pyc (Python 3.6)

from cl_cscommondef import BUYRULE_SHOPCASHFREE, BUYRULE_REFRESHFREE, BUYRULE_PRICECHANGE, OBTAIN_GOLD, VIRTUAL_ITEM_AUTOPERFORM, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC, OBTAIN_CASH, OBTAIN_WARCASH, BUYRULE_RANDOMCASHFREE, VIRTUAL_ITEM_RELIFETEAM, VIRTUAL_ITEM_SHOPREFRESH, BUYRULE_RANDOMFREE, BUYRULE_CASHREFRESHFREE, NWARRIOR_NPC_GSCASHSHOP, NWARRIOR_NPC_SHOP, VIRTUAL_ITEM_RAREITEM, VIRTUAL_ITEM_GOLDENCUP, NWARRIOR_NPC_PHASESHOP, PLAYMODE_DAYLY_TRIAL, LINK_DISCONNECT
from cl_only import Functor, ChooseKey
from cl_object.logging import WarshopLog
import cl_notify
import cl_msgcenter

class CHeroBuyMgr(object):
    
    def __init__(self, oGame, iOwner):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_BuyRule = { }
        self.m_InteractShopNpc = 0
        self.m_ShowHidden = { }
        self.InitAttention()

    
    def Release(self):
        self.DoneAttention()
        self.m_Game = None
        self.m_BuyRule = { }

    
    def InitAttention(self):
        oHero = self.GetOwner()
        if not oHero:
            return None
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnLinkStatusChange, 'HeroBuyMgr', iOnce = 0)

    
    def DoneAttention(self):
        oHero = self.GetOwner()
        if not oHero:
            return None
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, 'HeroBuyMgr')

    
    def OnLinkStatusChange(self, oHero, dMsgInfo):
        if 'LinkStatus' not in dMsgInfo:
            return None
        if dMsgInfo['LinkStatus'] != LINK_DISCONNECT:
            return None
        self.m_InteractShopNpc = 0

    
    def SetInteractShopNpc(self, iShopNpc):
        self.m_InteractShopNpc = iShopNpc

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def ShowHiddenGoods(self, iPos):
        self.m_ShowHidden[iPos] = 1

    
    def IsHidden(self, iPos, oGoods):
        if oGoods.IsHidden() and iPos not in self.m_ShowHidden:
            return 1
        return 0

    
    def RefreshShopUI(self):
        if self.m_InteractShopNpc:
            oShopNpc = self.m_Game.GetObject(self.m_InteractShopNpc)
            if not oShopNpc:
                self.m_InteractShopNpc = 0
                return None
            oShopNpc.RefreshShopUI(self.GetOwner())

    
    def _RuleChange(self):
        self.RefreshShopUI()

    
    def _GetRuleInfo(self, iPos, oGoods, iShopNpc):
        dData = {
            'GoodsType': oGoods.m_GoodsType,
            'CashType': oGoods.m_CashType,
            'Cash': oGoods.GetCash(),
            'CanBuy': oGoods.m_CanBuy,
            'ShopNpc': iShopNpc,
            'Hero': self.m_Owner,
            'Pos': iPos }
        return dData

    
    def AddRule(self, iRule, sKey, iValue):
        if iRule not in self.m_BuyRule:
            if iRule in g_BuyRuleClass:
                clsRule = g_BuyRuleClass[iRule]
                self.m_BuyRule[iRule] = clsRule(self.m_Game)
            else:
                return None
        oRule = self.m_BuyRule[iRule]
        oRule.Add(sKey, iValue)
        self._RuleChange()

    
    def RemoveRule(self, iRule, sKey):
        if iRule not in self.m_BuyRule:
            return None
        oRule = self.m_BuyRule[iRule]
        oRule.Remove(sKey)
        self._RuleChange()

    
    def GetGoodsShowList(self, iShopNpc, dGoods):
        lstGoodsInfo = []
        for iPos, oGoods in dGoods.items():
            if self.IsHidden(iPos, oGoods):
                continue
            lstGoodsInfo.append(self.GetGoodsShow(iPos, oGoods, iShopNpc))
        
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GETGOODSLIST, oOwner, {
            'ShopNpc': iShopNpc,
            'GoodsList': lstGoodsInfo })
        return lstGoodsInfo

    
    def GetGoodsShow(self, iPos, oGoods, iShopNpc):
        iAmount = 1
        dRuleInfo = self._GetRuleInfo(iPos, oGoods, iShopNpc)
        dRuleInfo['Amount'] = iAmount
        dRuleInfo['TotalCash'] = oGoods.GetCash()
        for _iRule, oRule in sorted(self.m_BuyRule.items()):
            if oRule.ValidEffect(dRuleInfo):
                oRule.TryEffect(dRuleInfo)
        
        iTotalCash = dRuleInfo['TotalCash']
        iCanBuy = dRuleInfo['CanBuy']
        return [
            iPos,
            oGoods.m_SID,
            oGoods.m_GoodsType,
            iCanBuy,
            oGoods.m_HasBuy,
            oGoods.m_CashType,
            iTotalCash,
            oGoods.m_Lock,
            oGoods.GetAttr(self.m_Game)]

    
    def IsGoodsSellOut(self, iPos, oGoods, iShopNpc):
        iAmount = 1
        dRuleInfo = self._GetRuleInfo(iPos, oGoods, iShopNpc)
        dRuleInfo['Amount'] = iAmount
        dRuleInfo['TotalCash'] = oGoods.GetCash()
        for oRule in self.m_BuyRule.values():
            if oRule.ValidEffect(dRuleInfo):
                oRule.TryEffect(dRuleInfo)
        
        iCanBuy = dRuleInfo['CanBuy']
        return oGoods.m_HasBuy >= iCanBuy

    
    def CanBuy(self, iPos, oGoods, iAmount, dRuleInfo):
        if not oGoods.CanBuy():
            return False
        if self.IsHidden(iPos, oGoods):
            return False
        iCanBuy = dRuleInfo['CanBuy']
        if iCanBuy != -1 and iCanBuy - oGoods.m_HasBuy < iAmount:
            cl_notify.SendCommonNotify(self.m_Game, [
                self.m_Owner], 7001, { })
            return False
        return True

    
    def Buy(self, oGoods, iShopNpc, iPos, iReplacePos, cbFunc):
        iAmount = 1
        dRuleInfo = self._GetRuleInfo(iPos, oGoods, iShopNpc)
        dRuleInfo['Amount'] = iAmount
        iOldCash = iAmount * oGoods.GetCash()
        dRuleInfo['TotalCash'] = iOldCash
        for _iRule, oRule in sorted(self.m_BuyRule.items()):
            if oRule.ValidEffect(dRuleInfo):
                oRule.TryEffect(dRuleInfo)
        
        oOwner = self.GetOwner()
        if not self.CanBuy(iPos, oGoods, iAmount, dRuleInfo):
            cbFunc(oOwner, False)
            return None
        if oGoods.m_GoodsType == VIRTUAL_ITEM_GOLDENCUP:
            oGoods.m_Items[0]['info']['VisiblePlayer'] = {
                oOwner.m_PlayerID: 1 }
        if oGoods.m_CashType == OBTAIN_WARCASH:
            ret = self.BuyByCash(oGoods, iShopNpc, iAmount, dRuleInfo, iReplacePos)
            cbFunc(oOwner, ret)
        elif oGoods.m_CashType == OBTAIN_GOLD:
            self.BuyByGold(oGoods, iShopNpc, iPos, iAmount, cbFunc, dRuleInfo)
        elif oGoods.m_CashType == OBTAIN_CASH:
            ret = self.BuyByGSCash(oGoods, iShopNpc, iAmount, dRuleInfo, iReplacePos)
            cbFunc(oOwner, ret)

    
    def GetActionKey(self, oGoods, iShopNpc):
        oShopNpc = self.m_Game.GetObject(iShopNpc)
        iNpc = oShopNpc.m_SID if oShopNpc else 0
        sAction = g_ItemsToActionMapping[oGoods.m_GoodsType] if oGoods.m_GoodsType in g_ItemsToActionMapping else 'unknown'
        iTarget = oGoods.m_SID if sAction != 'buyback' else 0
        sKey = 'NPC-%d-%s-%s-%d' % (iNpc, 'purchase', sAction, iTarget)
        return sKey

    
    def BuyByCash(self, oGoods, iShopNpc, iAmount, dRuleInfo, iReplacePos = 0):
        oOwner = self.GetOwner()
        oShopNpc = oOwner.m_Game.GetObject(iShopNpc)
        iCash = dRuleInfo['TotalCash']
        if oOwner.m_WarCash < iCash:
            return False
        WarshopLog.Info('%d %d cash %d buy %d_%d' % (self.m_Game.m_ID, self.m_Owner, iCash, oGoods.m_GoodsType, oGoods.m_SID))
        if iCash:
            oOwner.AddCash(-iCash, self.GetActionKey(oGoods, iShopNpc))
        for oRule in self.m_BuyRule.values():
            if oRule.ValidCostEffect(dRuleInfo):
                oRule.CostEffect(oGoods)
        
        oGoods.BuySuccess(oOwner, oGoods.m_Items, iAmount, iReplacePos)
        oGoods.OnBuy(oOwner, oShopNpc)
        self._RuleChange()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BUYGOODS, oOwner, {
            'ShopNpc': iShopNpc,
            'Cost': iCash,
            'Pos': oGoods.m_Pos,
            'Amount': iAmount,
            'Type': oGoods.m_GoodsType,
            'SID': oGoods.m_SID })
        return True

    
    def BuyByGold(self, oGoods, iShopNpc, iPos, iAmount, cbFunc, dRuleInfo):
        iCash = dRuleInfo['TotalCash']
        sReason = 'buy%s_%s' % (oGoods.m_GoodsType, oGoods.m_SID)
        dCostInfo = { }
        for iRule, oRule in self.m_BuyRule.items():
            if oRule.ValidCostEffect(dRuleInfo):
                dCostInfo[iRule] = oRule.CostEffect(oGoods)
        
        self._RuleChange()
        resFunc = Functor(self.BuyByGold2, dCostInfo, iShopNpc, iPos, iCash, iAmount, oGoods.m_Items, cbFunc)
        oOwner = self.GetOwner()
        self.m_Game.m_WarPayMgr.PayGold(oOwner.m_PlayerID, iCash, sReason, resFunc)

    
    def BuyByGold2(self, dCostInfo, iShopNpc, iPos, iCash, iAmount, lstItems, cbFunc, oGame, iPlayer):
        oShopNpc = oGame.GetObject(iShopNpc)
        if not oShopNpc:
            self._BuyByGoldFail(dCostInfo, cbFunc, oGame, iPlayer)
            return False
        if iPlayer not in oShopNpc.m_GoodsData or iPos not in oShopNpc.m_GoodsData[iPlayer]:
            self._BuyByGoldFail(dCostInfo, cbFunc, oGame, iPlayer)
            return False
        oGoods = oShopNpc.m_GoodsData[iPlayer][iPos]
        oHero = oGame.GetObject(iPlayer)
        if not oHero or not oGoods.CanBuy() or lstItems != oGoods.m_Items:
            self._BuyByGoldFail(dCostInfo, cbFunc, oGame, iPlayer)
            return False
        WarshopLog.Info('%d %d gold %d success buy %d_%d' % (self.m_Game.m_ID, self.m_Owner, iCash, oGoods.m_GoodsType, oGoods.m_SID))
        oGoods.BuySuccess(oHero, oGoods.m_Items, iAmount)
        oGoods.OnBuy(oHero, oShopNpc)
        cbFunc(oHero, True)
        return True

    
    def _BuyByGoldFail(self, dCostInfo, cbFunc, oGame, iPlayer):
        for iRule in dCostInfo:
            if iRule in self.m_BuyRule:
                oRule = self.m_BuyRule[iRule]
                oRule.UnCostEffect(dCostInfo[iRule])
        
        self._RuleChange()
        oHero = oGame.GetObject(iPlayer)
        cbFunc(oHero, False)

    
    def BuyByGSCash(self, oGoods, iShopNpc, iAmount, dRuleInfo, iReplacePos = 0):
        oShopNpc = self.m_Game.GetObject(iShopNpc)
        oOwner = self.GetOwner()
        iCash = dRuleInfo['TotalCash']
        if oOwner.m_WarGSCash < iCash:
            cl_notify.GS2CDebugNotify(self.m_Game, self.m_Owner, '刀币不够')
            return False
        sReason = 'buy %d_%d' % (oGoods.m_GoodsType, oGoods.m_SID)
        WarshopLog.Info('%d %d gscash %d %s' % (self.m_Game.m_ID, self.m_Owner, iCash, sReason))
        if iCash:
            oOwner.ConsumeGSCash(iCash, sReason)
        for oRule in self.m_BuyRule.values():
            if oRule.ValidCostEffect(dRuleInfo):
                oRule.CostEffect(oGoods)
        
        oGoods.BuySuccess(oOwner, oGoods.m_Items, iAmount, iReplacePos)
        oGoods.OnBuy(oOwner, oShopNpc)
        if dRuleInfo['GoodsType'] not in (VIRTUAL_ITEM_SHOPREFRESH,):
            self.RefreshShopUI()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BUYGSGOOD, oOwner, {
            'ShopNpc': iShopNpc,
            'Type': oGoods.m_GoodsType })
        return True



class CBaseBuyRule(object):
    m_Type = 0
    
    def __init__(self, oGame):
        pass

    
    def Add(self, sKey, iValue):
        pass

    
    def Remove(self, sKey):
        pass

    
    def ValidEffect(self, dRuleInfo):
        pass

    
    def ValidCostEffect(self, dRuleInfo):
        return self.ValidEffect(dRuleInfo)

    
    def TryEffect(self, dRuleInfo):
        pass

    
    def CostEffect(self, oGoods):
        return { }

    
    def UnCostEffect(self, dTryInfo):
        pass



class CShopCashFreeRule(CBaseBuyRule):
    m_Type = BUYRULE_SHOPCASHFREE
    
    def __init__(self, oGame):
        self.m_PlayMode = oGame.m_WarMgr.m_PlayMode
        self.m_AddKey = { }
        self.m_FreeTimes = 0
        self.m_ShopHasFree = { }
        self.m_TryInfo = { }

    
    def Add(self, sKey, iValue):
        if sKey not in self.m_AddKey:
            self.m_AddKey[sKey] = iValue
            self.m_FreeTimes += iValue

    
    def Remove(self, sKey):
        if sKey in self.m_AddKey:
            self.m_FreeTimes -= self.m_AddKey[sKey]
            self.m_AddKey.pop(sKey)

    
    def ValidEffect(self, dRuleInfo):
        if dRuleInfo['GoodsType'] in [
            VIRTUAL_ITEM_RELIFETEAM,
            VIRTUAL_ITEM_SHOPREFRESH]:
            return False
        if dRuleInfo['CashType'] != OBTAIN_WARCASH:
            return False
        if dRuleInfo['Cash'] < 0 and self.m_PlayMode != PLAYMODE_DAYLY_TRIAL:
            return False
        iShopNpc = dRuleInfo['ShopNpc']
        iFreeTime = self.m_ShopHasFree.get(iShopNpc, 0)
        if iFreeTime >= self.m_FreeTimes:
            return False
        return True

    
    def TryEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        iHasFreeTime = self.m_ShopHasFree.get(iShopNpc, 0)
        iAmount = dRuleInfo['Amount']
        iPerCash = dRuleInfo['Cash']
        iFreeAmount = min(iAmount, self.m_FreeTimes - iHasFreeTime)
        iNewTotalCash = dRuleInfo['TotalCash'] - iPerCash * iFreeAmount
        dRuleInfo['TotalCash'] = iNewTotalCash
        self.m_TryInfo = {
            'FreeAmount': iFreeAmount,
            'ShopNpc': iShopNpc }

    
    def CostEffect(self, oGoods):
        iShopNpc = self.m_TryInfo['ShopNpc']
        iFreeAmount = self.m_TryInfo['FreeAmount']
        if iShopNpc not in self.m_ShopHasFree:
            self.m_ShopHasFree[iShopNpc] = iFreeAmount
        else:
            self.m_ShopHasFree[iShopNpc] += iFreeAmount
        return self.m_TryInfo



class CPriceChangeRule(CBaseBuyRule):
    m_Type = BUYRULE_PRICECHANGE
    
    def __init__(self, oGame):
        self.m_AddKey = { }

    
    def GetTotalChangePercent(self):
        iTotalChange = 0
        for iChange in self.m_AddKey.values():
            iTotalChange += iChange
        
        return iTotalChange

    
    def Add(self, sKey, iValue):
        self.m_AddKey[sKey] = iValue

    
    def Remove(self, sKey):
        if sKey in self.m_AddKey:
            self.m_AddKey.pop(sKey)

    
    def ValidEffect(self, dRuleInfo):
        if dRuleInfo['GoodsType'] == VIRTUAL_ITEM_RELIFETEAM:
            return False
        if dRuleInfo['CashType'] != OBTAIN_WARCASH:
            return False
        return True

    
    def TryEffect(self, dRuleInfo):
        iPerCash = dRuleInfo['Cash']
        iTotalCash = dRuleInfo['TotalCash']
        iValidAmount = iTotalCash // iPerCash
        iPrecent = self.GetTotalChangePercent()
        dRuleInfo['Cash'] = iPerCash * (100 + iPrecent) // 100
        dRuleInfo['TotalCash'] = iValidAmount * dRuleInfo['Cash']
        return { }



class CRefreshFreeRule(CBaseBuyRule):
    m_Type = BUYRULE_REFRESHFREE
    
    def __init__(self, oGame):
        self.m_AddKey = { }
        self.m_FreeTimes = 0
        self.m_ShopHasFree = { }
        self.m_Game = oGame

    
    def Add(self, sKey, iValue):
        if sKey not in self.m_AddKey:
            self.m_AddKey[sKey] = iValue
            self.m_FreeTimes += iValue

    
    def Remove(self, sKey):
        if sKey in self.m_AddKey:
            self.m_FreeTimes -= self.m_AddKey[sKey]
            self.m_AddKey.pop(sKey)

    
    def ValidEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        oShopNpc = self.m_Game.GetObject(iShopNpc)
        if not oShopNpc or oShopNpc.m_FightType not in [
            NWARRIOR_NPC_SHOP,
            NWARRIOR_NPC_PHASESHOP]:
            return False
        if dRuleInfo['GoodsType'] != VIRTUAL_ITEM_SHOPREFRESH:
            return False
        if dRuleInfo['CanBuy'] == -1:
            iHasFreeTime = self.m_ShopHasFree.get(iShopNpc, 0)
            if iHasFreeTime >= self.m_FreeTimes:
                return False
        return True

    
    def TryEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        iHasFreeTime = self.m_ShopHasFree.get(iShopNpc, 0)
        iAmount = dRuleInfo['Amount']
        iPerCash = dRuleInfo['Cash']
        iFreeAmount = min(iAmount, self.m_FreeTimes - iHasFreeTime)
        iNewTotalCash = dRuleInfo['TotalCash'] - iPerCash * iFreeAmount
        dRuleInfo['TotalCash'] = iNewTotalCash
        if dRuleInfo['CanBuy'] != -1:
            dRuleInfo['CanBuy'] += self.m_FreeTimes
        self.m_TryInfo = {
            'FreeAmount': iFreeAmount,
            'ShopNpc': iShopNpc,
            'Hero': dRuleInfo['Hero'] }

    
    def CostEffect(self, oGoods):
        iShopNpc = self.m_TryInfo['ShopNpc']
        iFreeAmount = self.m_TryInfo['FreeAmount']
        if iShopNpc not in self.m_ShopHasFree:
            self.m_ShopHasFree[iShopNpc] = iFreeAmount
        else:
            self.m_ShopHasFree[iShopNpc] += iFreeAmount
        oNpc = self.m_Game.GetObject(iShopNpc)
        if oNpc:
            oHero = self.m_Game.GetObject(self.m_TryInfo['Hero'])
            if oHero:
                oNpc.UpdateRefreshTimes(oHero, -1)
        return self.m_TryInfo

    
    def UnCostEffect(self, dTryInfo):
        iShopNpc = self.m_TryInfo['ShopNpc']
        iFreeAmount = dTryInfo['FreeAmount']
        self.m_ShopHasFree[iShopNpc] -= iFreeAmount
        oNpc = self.m_Game.GetObject(iShopNpc)
        if oNpc:
            oHero = self.m_Game.GetObject(self.m_TryInfo['Hero'])
            if oHero:
                oNpc.UpdateRefreshTimes(oHero, 1)



class CRandomFreeRule(CBaseBuyRule):
    m_Type = BUYRULE_RANDOMFREE
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_AddKey = { }
        self.m_TotalFree = 0
        self.m_ShopHasFree = { }
        self.m_ShopFreePos = { }
        self.m_TryInfo = { }

    
    def Add(self, sKey, iValue):
        if sKey not in self.m_AddKey:
            self.m_AddKey[sKey] = iValue
            self.m_TotalFree += iValue

    
    def Remove(self, sKey):
        if sKey in self.m_AddKey:
            iValue = self.m_AddKey.pop(sKey)
            self.m_TotalFree -= iValue

    
    def ValidEffect(self, dRuleInfo):
        if dRuleInfo['CashType'] != OBTAIN_WARCASH:
            return False
        if dRuleInfo['GoodsType'] in (VIRTUAL_ITEM_SHOPREFRESH, VIRTUAL_ITEM_RELIFETEAM):
            return False
        return True

    
    def TryEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        iHasFreeNum = self.m_ShopHasFree.get(iShopNpc, 0)
        iRestFreeNum = self.m_TotalFree - iHasFreeNum
        if iRestFreeNum <= 0:
            return None
        iTotal = dRuleInfo['TotalCash']
        if iTotal == 0:
            return None
        iCurPos = dRuleInfo['Pos']
        dFreePos = self.m_ShopFreePos.setdefault(iShopNpc, { })
        if not dFreePos:
            oNpc = self.m_Game.GetObject(iShopNpc)
            if not oNpc:
                return None
            dValidPos = { }
            iHero = dRuleInfo['Hero']
            oHero = self.m_Game.GetObject(iHero)
            for iPos, oGoods in oNpc.m_GoodsData[iHero].items():
                if oGoods.m_CashType != OBTAIN_WARCASH:
                    continue
                if oGoods.m_GoodsType == VIRTUAL_ITEM_SHOPREFRESH:
                    continue
                if oGoods.m_HasBuy >= oGoods.m_CanBuy:
                    continue
                if oHero.m_BuyMgr.IsHidden(iPos, oGoods):
                    continue
                dValidPos[iPos] = 1
            
            for _ in range(min(iRestFreeNum, len(dValidPos))):
                iFreePos = ChooseKey(self.m_Game, dValidPos)
                dValidPos.pop(iFreePos)
                dFreePos[iFreePos] = 1
            
        if iCurPos in dFreePos:
            dRuleInfo['TotalCash'] = 0
            self.m_TryInfo['ShopNpc'] = iShopNpc

    
    def ValidCostEffect(self, dRuleInfo):
        if 'ShopNpc' not in self.m_TryInfo:
            return False
        return self.ValidEffect(dRuleInfo)

    
    def CostEffect(self, oGoods):
        iShopNpc = self.m_TryInfo.pop('ShopNpc')
        if oGoods.m_GoodsType == VIRTUAL_ITEM_SHOPREFRESH:
            self.m_ShopFreePos[iShopNpc] = { }
        else:
            dFreePos = self.m_ShopFreePos.setdefault(iShopNpc, { })
            if not dFreePos or oGoods.m_Pos not in dFreePos:
                return None
            self.m_ShopFreePos[iShopNpc] = { }
            iFreeAmount = 1
            if iShopNpc not in self.m_ShopHasFree:
                self.m_ShopHasFree[iShopNpc] = iFreeAmount
            else:
                self.m_ShopHasFree[iShopNpc] += iFreeAmount
        return { }



class CRandomCashFreeRule(CRandomFreeRule):
    m_Type = BUYRULE_RANDOMCASHFREE
    
    def ValidEffect(self, dRuleInfo):
        if dRuleInfo['CashType'] != OBTAIN_CASH:
            return False
        if dRuleInfo['GoodsType'] in (VIRTUAL_ITEM_SHOPREFRESH,):
            return False
        return True

    
    def TryEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        iHasFreeNum = self.m_ShopHasFree.get(iShopNpc, 0)
        iRestFreeNum = self.m_TotalFree - iHasFreeNum
        if iRestFreeNum <= 0:
            return None
        iTotal = dRuleInfo['TotalCash']
        if iTotal == 0:
            return None
        iCurPos = dRuleInfo['Pos']
        dFreePos = self.m_ShopFreePos.setdefault(iShopNpc, { })
        if not dFreePos:
            oNpc = self.m_Game.GetObject(iShopNpc)
            if not oNpc:
                return None
            dValidPos = { }
            iHero = dRuleInfo['Hero']
            oHero = self.m_Game.GetObject(iHero)
            for iPos, oGoods in oNpc.m_GoodsData[iHero].items():
                if oGoods.m_CashType != OBTAIN_CASH:
                    continue
                if oGoods.m_GoodsType == VIRTUAL_ITEM_SHOPREFRESH:
                    continue
                if oGoods.m_HasBuy >= oGoods.m_CanBuy:
                    continue
                if oHero.m_BuyMgr.IsHidden(iPos, oGoods):
                    continue
                dValidPos[iPos] = 1
            
            for _ in range(min(iRestFreeNum, len(dValidPos))):
                iFreePos = ChooseKey(self.m_Game, dValidPos)
                dValidPos.pop(iFreePos)
                dFreePos[iFreePos] = 1
            
        if iCurPos in dFreePos:
            dRuleInfo['TotalCash'] = 0
            self.m_TryInfo['ShopNpc'] = iShopNpc



class CCashRefreshFreeRule(CRefreshFreeRule):
    m_Type = BUYRULE_CASHREFRESHFREE
    
    def ValidEffect(self, dRuleInfo):
        iShopNpc = dRuleInfo['ShopNpc']
        oShopNpc = self.m_Game.GetObject(iShopNpc)
        if not oShopNpc or oShopNpc.m_FightType != NWARRIOR_NPC_GSCASHSHOP:
            return False
        if dRuleInfo['GoodsType'] != VIRTUAL_ITEM_SHOPREFRESH:
            return False
        return True


g_BuyRuleClass = {
    BUYRULE_CASHREFRESHFREE: CCashRefreshFreeRule,
    BUYRULE_RANDOMCASHFREE: CRandomCashFreeRule,
    BUYRULE_RANDOMFREE: CRandomFreeRule,
    BUYRULE_REFRESHFREE: CRefreshFreeRule,
    BUYRULE_PRICECHANGE: CPriceChangeRule,
    BUYRULE_SHOPCASHFREE: CShopCashFreeRule }
g_ItemsToActionMapping = {
    VIRTUAL_ITEM_SHOPREFRESH: 'refreshgoods',
    VIRTUAL_ITEM_RAREITEM: 'rareitem',
    VIRTUAL_ITEM_AUTOPERFORM: 'autoperform',
    VIRTUAL_ITEM_BULLET: 'bullet',
    VIRTUAL_ITEM_EQUIP: 'weapon',
    VIRTUAL_ITEM_RELIC: 'relic',
    VIRTUAL_ITEM_RELIFETEAM: 'buyback' }
