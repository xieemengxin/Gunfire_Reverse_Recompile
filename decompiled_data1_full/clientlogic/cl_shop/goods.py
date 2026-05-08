# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_shop/goods.pyc
# RelativePath: clientlogic/cl_shop/goods.pyc
# Source Generated with Decompyle++
# File: goods.pyc (Python 3.6)

from cl_commondefines import TYPE_RELIFE_BUY, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIFETEAM, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_RAREITEM, VIRTUAL_ITEM_RANDOM, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_AUTOPERFORM
from cl_commondefines import SHOPITEM_BULLET, SHOPITEM_THROW, SHOPITEM_RECOVER, SHOPITEM_WEAPON, SHOPITEM_RELIC, SHOPITEM_SUPER, SHOPITEMSID_BULLET, SHOPITEMSID_THROW, SHOPITEMSID_RECOVER, SHOPITEM_CURSERELIC
from cl_cscommondef.cs_other import PF_RS_WARSHOPBUY
from cl_only import ChooseKey, SendAlert
import math
import cl_math
import cl_reward
import cl_netattr
import cl_notify
import cl_msgcenter
import cl_perform
import cl_formula
import cl_shop.goodsdata
g_GoodsToProp = {
    VIRTUAL_ITEM_RAREITEM: cl_netattr.PROP_ITEM,
    VIRTUAL_ITEM_EQUIP: cl_netattr.PROP_DROPITEM_MAINWEAPON }

class CWarGoods(object):
    
    def __init__(self, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
        self.m_SID = iSID
        self.m_GoodsType = iGoodsType
        self.m_Cash = iCash
        self.m_CashType = iCashType
        self.m_Discount = 100
        self.m_CanBuy = iCanBuy
        self.m_HasBuy = 0
        self.m_Items = lstGoods
        self.m_Enable = True
        self.m_Hidden = iHide
        self.m_Pos = -1
        self.m_CanRewardRelic = False
        self.m_GoodsAttr = []
        self.m_Lock = 0
        self.m_ShowInfo = { }

    
    def Enable(self):
        self.m_Enable = True

    
    def Disable(self):
        self.m_Enable = False

    
    def IsHidden(self):
        return self.m_Hidden

    
    def GetCash(self):
        return self.m_Cash * self.m_Discount // 100

    
    def SetDiscount(self, iDiscount):
        self.m_Discount = iDiscount

    
    def CanBuy(self):
        if not self.m_Enable:
            return False
        return True

    
    def SetLock(self, iLock):
        self.m_Lock = iLock

    
    def IsLock(self):
        return self.m_Lock

    
    def BuySuccess(self, oHero, lstItems, iAmount, iReplacePos = 0):
        self.m_HasBuy += iAmount
        self.m_Lock = 0
        dExtInfo = {
            'iReplacePos': iReplacePos }
        cl_reward.RewardItem(oHero.m_Game, oHero, lstItems, PF_RS_WARSHOPBUY, dExtInfo)

    
    def GetAttr(self, oGame = None):
        if self.m_GoodsAttr:
            return self.m_GoodsAttr
        lstAllAttr = []
        if self.m_GoodsType in (VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RAREITEM):
            iProp = g_GoodsToProp[self.m_GoodsType]
            for dGoods in self.m_Items:
                lstAttr = []
                oItem = dGoods['info']['item']
                for sAttr in cl_netattr.INFO_OBJECT_INIT[iProp]:
                    (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
                    iValue = cl_netattr.GetPropValue(oItem, sAttr, iMode)
                    if iValue is None:
                        continue
                    lstAttr.append((iIdx, iType, iLen, iValue))
                
                dItem = {
                    'Attr': lstAttr }
                lstAllAttr.append(dItem)
            
        elif self.m_GoodsType == VIRTUAL_ITEM_RELIC:
            for dGoods in self.m_Items:
                lstAttr = []
                iSID = dGoods['info']['sid']
                clsPerform = cl_perform.GetPerformModule(iSID)
                for sAttr in cl_netattr.INFO_OBJECT_INIT[cl_netattr.PROP_RELIC]:
                    (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
                    if sAttr == 'Level':
                        iValue = dGoods['info']['level']
                    else:
                        iValue = cl_netattr.GetPropValue(clsPerform, sAttr, iMode, oGame)
                    if iValue is None:
                        continue
                    lstAttr.append((iIdx, iType, iLen, iValue))
                
                dItem = {
                    'Attr': lstAttr }
                lstAllAttr.append(dItem)
            
        self.m_GoodsAttr = lstAllAttr
        return lstAllAttr

    
    def SetRewardRelic(self, iRewardCnt):
        self.m_CanRewardRelic = True
        self.m_RewardRelicCnt = iRewardCnt

    
    def OnBuy(self, oHero, oNpc):
        if self.m_CanRewardRelic:
            lstReward = self.GetRelicReward(oHero, oNpc)
            if not lstReward:
                return None
            for iRelic in lstReward:
                dReward = {
                    'item': VIRTUAL_ITEM_RELIC,
                    'info': {
                        'sid': iRelic } }
                cl_reward.RewardItem(oHero.m_Game, oHero, [
                    dReward], 'shopbuyext')
                oHero.m_RelicCon.GS2CAddExtraRelic(iRelic)
            

    
    def GetRelicReward(self, oHero, oNpc):
        oGame = oHero.m_Game
        setAllUnlockRelic = oHero.Query('Illus')['Relic']
        lstAllCanSellRelic = cl_perform.GetAllCanSellRelic(oGame)
        lstAllRelic = list((setAllUnlockRelic & set(lstAllCanSellRelic)) - set(oHero.m_RelicCon.GetFilterRelic()))
        for iRelic in oNpc.GetGoodsCacheData(VIRTUAL_ITEM_RELIC):
            if iRelic in lstAllRelic:
                lstAllRelic.remove(iRelic)
        
        oScene = oGame.m_SceneMgr.GetScene(oNpc.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(oHero.m_ID)
        if oChoosePool:
            dRelic = oChoosePool.m_PreLoadData['Relic']
            for iRelic in dRelic:
                if iRelic in lstAllRelic:
                    lstAllRelic.remove(iRelic)
            
        if not lstAllRelic:
            return None
        lstReward = []
        for i in range(self.m_RewardRelicCnt):
            iReward = oGame.m_RandomMgr.ChooseKey('relic%d' % oHero.m_ID, {
                'Select': lstAllRelic })
            lstAllRelic = lstAllRelic.remove(iReward) if iReward in lstAllRelic else lstAllRelic
            lstReward.append(iReward)
        
        return lstReward

    
    def GetExtraInfo(self):
        return { }

    
    def SetShowInfo(self, dShowInfo):
        self.m_ShowInfo = dShowInfo

    
    def GetShowInfo(self):
        return self.m_ShowInfo



class CRelifeGoods(CWarGoods):
    
    def __init__(self, oGame, iNpc, iHero, iCash, iCashType, iCanBuy, iTarget):
        self.m_Game = oGame
        self.m_Npc = iNpc
        self.m_SID = 0
        self.m_Owner = iHero
        self.m_GoodsType = VIRTUAL_ITEM_RELIFETEAM
        self.m_Cash = iCash
        self.m_CashType = iCashType
        self.m_Discount = 100
        self.m_CanBuy = iCanBuy
        self.m_HasBuy = 0
        self.m_Items = []
        self.m_Enable = True
        self.m_Hidden = True
        self.m_Pos = -1
        self.m_RelifeTarget = iTarget
        self.m_AttentionKey = 'RelifeGoods%s%s' % (self.m_Owner, self.m_RelifeTarget)
        self.m_CanRewardRelic = False
        self.m_Lock = 0
        oTarget = oGame.GetObject(iTarget)
        if oTarget:
            lstHero = oGame.m_WarMgr.GetRoomHero()
            if iTarget not in lstHero:
                return None
            oNpc = oGame.GetObject(iNpc)
            if oNpc.Query(self.m_AttentionKey, 0):
                return None
            oNpc.Set(self.m_AttentionKey, 1)
            if oTarget.IsRealDied():
                self.m_Hidden = False
            oGame.AddGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_DIEDIST, self.OnDieDist, self.m_AttentionKey)
            oGame.AddGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_AttentionKey)
            oGame.AddGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, self.OnPlayerLeave, self.m_AttentionKey)

    
    def Disable(self):
        self.m_Enable = False
        if self.m_Game:
            self.m_Game.DoneGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_DIEDIST, self.m_AttentionKey)
            self.m_Game.DoneGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_RELIFE, self.m_AttentionKey)
            self.m_Game.DoneGlobalAttention(self.m_Npc, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, self.m_AttentionKey)
            self.m_Game = None

    
    def GetCash(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero:
            return 0
        return cl_formula.GetFormulaResult(oHero, self.m_Cash)

    
    def CanBuy(self):
        if not self.m_Enable:
            return False
        oTarget = self.m_Game.GetObject(self.m_RelifeTarget)
        if not oTarget:
            return False
        if not oTarget.IsRealDied():
            cl_notify.SendCommonNotify(self.m_Game, [
                self.m_Owner], 2128, {
                '$$playername': oTarget.Name() })
            return False
        return True

    
    def OnDieDist(self, oNpc, oTarget, dInfo):
        if oTarget.m_ID != self.m_RelifeTarget:
            return None
        self.m_Hidden = False
        self.RefreshNpcShop(oNpc)

    
    def OnPlayerLeave(self, oNpc, oTarget, dInfo):
        if oTarget.m_ID != self.m_RelifeTarget:
            return None
        self.Disable()
        self.m_Hidden = True
        self.RefreshNpcShop(oNpc)

    
    def OnRelife(self, oNpc, oTarget, dInfo):
        if oTarget.m_ID != self.m_RelifeTarget:
            return None
        if self.m_HasBuy >= self.m_CanBuy:
            return None
        self.m_Hidden = True
        self.RefreshNpcShop(oNpc)

    
    def RefreshNpcShop(self, oNpc):
        oGame = oNpc.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return None
        oOwner.m_BuyMgr.RefreshShopUI()

    
    def BuySuccess(self, oHero, lstItems, iAmount, iReplacePos = 0):
        self.m_HasBuy += iAmount
        oWarMgr = self.m_Game.m_WarMgr
        oTarget = self.m_Game.GetObject(self.m_RelifeTarget)
        if not oTarget:
            return None
        oWatch = oWarMgr.GetComponent('WatchElement')
        oPVEDie = oWarMgr.GetComponent('PVEDieElement')
        if not oPVEDie:
            return None
        iBuyRelifeItemTimes = oHero.QuerySavedData('BuyRelifeItemTimes', 0)
        oHero.SetSavedData('BuyRelifeItemTimes', iBuyRelifeItemTimes + 1)
        oGame = oHero.m_Game
        vEnd = oHero.GetPos()
        oNpc = oGame.GetObject(self.m_Npc)
        if oNpc:
            vFace = cl_math.Vec3Minus(oNpc.GetPos(), vEnd)
        else:
            vFace = oTarget.GetFacing()
        if oWatch:
            oWatch.RelifeWatch(oTarget)
        oPVEDie.WatcherRelife(oTarget, TYPE_RELIFE_BUY, oHero.m_ID)
        if oTarget.m_Scene == oHero.m_Scene:
            oTarget.WalkTo(vEnd)
            oTarget.Stop()
        else:
            oTarget.Goto(oHero.m_Scene, vEnd, vFace)

    
    def GetAttr(self, oGame = None):
        lstAttr = []
        (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME['Target']
        lstAttr.append((iIdx, iType, iLen, self.m_RelifeTarget))
        return [
            {
                'Attr': lstAttr }]



class CPetGoods(CWarGoods):
    
    def __init__(self, oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
        super().__init__(iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)
        self.m_Game = oGame
        self.m_Owner = iHero
        self.m_ShowInfo = { }

    
    def Disable(self):
        super().Disable()
        if not self.m_HasBuy:
            oPet = self.GetPet()
            if oPet:
                oPet.Remove('GoodsDisable')
        self.m_Game = None

    
    def OnBuy(self, oHero, oNpc):
        pass

    
    def GetPet(self):
        iPet = self.m_Items[0]['info']['item']
        oPet = self.m_Game.GetObject(iPet)
        return oPet

    
    def GetCash(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            iForceCash = oHero.Query('ForcePetGoodCash', None)
            if iForceCash is not None:
                return iForceCash
        return self.m_Cash * self.m_Discount // 100

    
    def GetShowInfo(self):
        if self.m_ShowInfo:
            return self.m_ShowInfo
        oPet = self.GetPet()
        dShowInfo = {
            'Offset': oPet.GetAttrOffsetPacketInfo(),
            'AllAttr': cl_netattr.MakePetShowAddPacket(oPet),
            'Ability': oPet.Ability() }
        self.m_ShowInfo = dShowInfo
        return dShowInfo

    
    def CanBuy(self):
        if not self.m_Enable:
            return False
        if not (self.m_CanBuy) or self.m_HasBuy >= self.m_CanBuy:
            return False
        oPet = self.GetPet()
        if not oPet:
            return False
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero or not oHero.m_PetCon.ValidAdd(oPet):
            return False
        return True



class CWandGoods(CWarGoods):
    
    def __init__(self, oGame, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
        super().__init__(iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)
        self.m_Game = oGame
        self.m_Owner = iHero

    
    def OnBuy(self, oHero, oNpc):
        pass



class CDiceGoods(CWarGoods):
    
    def __init__(self, oGame, iNpc, iHero, iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide):
        super().__init__(iSID, iGoodsType, iCash, iCashType, iCanBuy, lstGoods, iHide)
        self.m_Game = oGame
        self.m_Npc = iNpc
        self.m_Owner = iHero

    
    def GetCash(self):
        oNpc = self.m_Game.GetObject(self.m_Npc)
        if not oNpc:
            return 0
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero:
            return 0
        dGoodInfo = self.m_Items[0].get('info', { })
        if not dGoodInfo:
            return 0
        iQuality = dGoodInfo.get('QL', 0)
        iGoodsType = self.m_Items[0].get('item', 0)
        return oNpc.GetGoodsCash(oHero, iQuality, iGoodsType)



class CRandGoods(CWarGoods):
    m_RewardTypeToGoods = {
        SHOPITEM_THROW: SHOPITEMSID_THROW,
        SHOPITEM_RECOVER: SHOPITEMSID_RECOVER,
        SHOPITEM_BULLET: SHOPITEMSID_BULLET }
    
    def __init__(self, iSID, iCash, iCashType, iCanBuy, lstGoods, iHide):
        self.m_SID = iSID
        self.m_GoodsType = VIRTUAL_ITEM_RANDOM
        self.m_Cash = iCash
        self.m_CashType = iCashType
        self.m_Discount = 100
        self.m_CanBuy = iCanBuy
        self.m_HasBuy = 0
        self.m_Items = lstGoods
        self.m_Enable = True
        self.m_Hidden = iHide
        self.m_Lock = 0
        self.m_RandResult = { }

    
    def BuySuccess(self, oHero, lstItems, iAmount, iReplacePos = 0):
        self.m_HasBuy += iAmount
        self.m_Lock = 0
        dExtInfo = {
            'iReplacePos': iReplacePos }
        dArgs = lstItems[0]['info']
        dReward = self.RandomChooseReward(oHero, dArgs)
        cl_reward.RewardItem(oHero.m_Game, oHero, [
            dReward], PF_RS_WARSHOPBUY, dExtInfo)

    
    def OnBuy(self, oHero, oNpc):
        pass

    
    def GetAttr(self, oGame = None):
        return []

    
    def RandomChooseReward(self, oHero, dArg):
        from cl_wardata.npcaction import ChooseWeapon, ChooseRelic
        from cl_npc.eventnpcaction import ChooseCurseRelic
        dChooseWeight = dArg['ChooseWeight']
        dExtraInfo = dArg['ExtraInfo']
        dWeaponChooseMG = dArg['WeaponChooseMG']
        dRelicChooseMG = dArg['RelicChooseMG']
        oGame = oHero.m_Game
        iRound = oGame.m_WarMgr.m_Round
        (iWeaponEnhance, iRelicLevel) = (0, 1)
        dGoods = { }
        iChoose = ChooseKey(oGame, dChooseWeight)
        if iChoose == SHOPITEM_SUPER:
            dTypeWeight = {
                SHOPITEM_RELIC: dExtraInfo['SuperRelicWeight'],
                SHOPITEM_WEAPON: dExtraInfo['SuperWeaponWeight'] }
            iChoose = ChooseKey(oGame, dTypeWeight)
            if iChoose == SHOPITEM_WEAPON:
                iWeaponEnhance = dExtraInfo['SuperWeaponEnhance']
            elif iChoose == SHOPITEM_RELIC:
                iRelicLevel = dExtraInfo['SuperRelicLevel']
        if iChoose in self.m_RewardTypeToGoods:
            clsGoods = cl_shop.goodsdata.GetGoodsData(self.m_RewardTypeToGoods[iChoose])
            if clsGoods:
                dGoods = clsGoods.m_Items[0]
                self.m_RandResult.update({
                    'RandItem': clsGoods.m_SID,
                    'RandType': clsGoods.m_GoodsType })
            elif iChoose == SHOPITEM_WEAPON:
                iWeaponMG = dWeaponChooseMG[iRound]
                oEquip = ChooseWeapon(oHero, iWeaponMG, iWeaponEnhance, [])
                if oEquip:
                    dGoods = {
                        'item': VIRTUAL_ITEM_EQUIP,
                        'info': {
                            'sid': oEquip.m_SID,
                            'item': oEquip,
                            'data': { } } }
                    self.m_RandResult.update({
                        'RandItem': oEquip.m_SID,
                        'RandLevel': iWeaponEnhance,
                        'RandType': VIRTUAL_ITEM_EQUIP })
                elif iChoose == SHOPITEM_RELIC:
                    iRelicMG = dRelicChooseMG[iRound]
                    iRelic = ChooseRelic(oHero, iRelicMG, iRelicLevel, 0)
                    if iRelic:
                        dGoods = {
                            'item': VIRTUAL_ITEM_RELIC,
                            'info': {
                                'sid': iRelic,
                                'data': { },
                                'level': iRelicLevel } }
                        self.m_RandResult.update({
                            'RandItem': iRelic,
                            'RandLevel': iRelicLevel,
                            'RandType': VIRTUAL_ITEM_RELIC })
                    elif iChoose == SHOPITEM_CURSERELIC:
                        iCurseRelic = ChooseCurseRelic(oHero)
                        if iCurseRelic:
                            dGoods = {
                                'item': VIRTUAL_ITEM_RELIC,
                                'info': {
                                    'sid': iCurseRelic,
                                    'data': { } } }
                            self.m_RandResult.update({
                                'RandItem': iCurseRelic,
                                'RandType': VIRTUAL_ITEM_RELIC })
        if not None:
            SendAlert('err', '随机商品未抽取到物品 %d %d %d %d' % (self.m_SID, iChoose, iWeaponEnhance, iRelicLevel))
        return dGoods

    
    def GetExtraInfo(self):
        return self.m_RandResult


