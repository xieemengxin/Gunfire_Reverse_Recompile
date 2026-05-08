# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/s7shopnpc.pyc
# RelativePath: clientlogic/cl_npc/s7shopnpc.pyc
# Source Generated with Decompyle++
# File: s7shopnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUELIST, NPC_CB_LIST, NPC_CB_VALUE, VIRTUAL_ITEM_S7CRYSTAL, OBTAIN_WARCASH, MAX_LAYER, VIRTUAL_ITEM_S7MODULE, VIRTUAL_ITEM_S7CRYSTALPACKET, S7SHOP_ADD_CRYSTALGOODS, S7GOODS_ALL_DEPOLY, S7GOODS_SINGLE_DEPOLY, SEASONSHOP_INITS7GOODS, SEASONSHOP_BUYS7CRYSTAL, SEASONSHOP_BUYS7PACKET, LEVEL_TYPE_BOSS
from cl_cscommondef import NPC_CB_DICT
from cl_object.logging import BackpackLog
from cl_only import ChooseKey
from cl_seasonplay.season7.s7goodsdata import GetS7GoodsData
from cl_seasonplay.season7.crystal import CALPOINT_CNTMAX
from . import seasonshopnpc
from . import net
import cl_shop
import cl_seasonplay.season7 as clseason7
import cl_formula
import cl_msgcenter
S7GOODS_CANBUYTIME = 1

class CS7ShopNpc(seasonshopnpc.CSeasonShopNPC):
    m_Season = 0
    m_MPRefreshTimes = 'ModulePacketRefreshTimes'
    m_CPRefreshTimes = 'CrystalPacketRefreshTimes'
    m_RefreshKeyInfo = {
        VIRTUAL_ITEM_S7CRYSTALPACKET: m_CPRefreshTimes,
        VIRTUAL_ITEM_S7MODULE: m_MPRefreshTimes }
    m_DefaultCrystal = (1002, 3)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_ShowInfo = { }
        self.m_ChooseLayer = 0
        self.m_ChooseLevel = 0
        self.m_CrystalGoodNum = 0
        self.m_CrystalGoodCost = None
        self.m_CrystalGoodInfo = { }
        self.m_CrystalPacketNum = 0
        self.m_CrystalPacketCost = None
        self.m_CrystalPacketSize = 0
        self.m_CrystalPacketDiff = 0
        self.m_CrystalPacketInfo = { }
        self.m_CrystalPacketPlayerInfo = { }
        self.m_ModulePacketNum = 0
        self.m_ModulePacketCost = None
        self.m_ModulePacketChoose = { }
        self.m_ModulePacketHasChoose = { }
        self.m_CacheModuleGoods = { }

    
    def Release(self):
        self.m_CrystalGoodCost = None
        self.m_CrystalPacketCost = None
        self.m_ModulePacketCost = None
        super().Release()

    
    def SetInitData(self, iCrystalGoodNum, iCrystalGoodCost, iCrystalPacketNum, iCrystalPacketCost, iCrystalPacketSize, iCrystalPacketDiff, iModulePacketNum, iModulePacketCost, dCrystalGoodInfo, dCrystalPacketInfo, dModulePacketChoose):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            BackpackLog.Alert('%s not levelctrl' % oGame.m_ID)
            return None
        iMaxLayer = self.m_FormulaLimit['MaxLayer'] if 'MaxLayer' in self.m_FormulaLimit else MAX_LAYER
        iLayer = min(iMaxLayer, oLevelCtrl.m_LayerNum)
        iMaxLevel = self.m_FormulaLimit['MaxLevel'] if 'MaxLevel' in self.m_FormulaLimit else 99
        iLevel = oLevelCtrl.m_LevelNum
        if iMaxLayer == iLayer and iLevel > iMaxLevel:
            iLevel = iMaxLevel
        self.m_ChooseLayer = iLayer
        self.m_ChooseLevel = iLevel
        if iLayer in dCrystalGoodInfo:
            self.m_CrystalGoodNum = iCrystalGoodNum
            self.m_CrystalGoodCost = iCrystalGoodCost
            self.m_CrystalGoodInfo = cl_formula.CalArgsFormula(self, dCrystalGoodInfo[iLayer], self.m_FormulaLimit)
        if iLayer in dCrystalPacketInfo:
            self.m_CrystalPacketNum = iCrystalPacketNum
            self.m_CrystalPacketCost = iCrystalPacketCost
            self.m_CrystalPacketSize = iCrystalPacketSize
            self.m_CrystalPacketDiff = iCrystalPacketDiff
            if iLevel in dCrystalPacketInfo[iLayer]:
                self.m_CrystalPacketInfo = dCrystalPacketInfo[iLayer][iLevel]
        self.m_ModulePacketNum = iModulePacketNum
        self.m_ModulePacketCost = iModulePacketCost
        if iLayer in dModulePacketChoose and iLevel in dModulePacketChoose[iLayer]:
            self.m_ModulePacketChoose = dModulePacketChoose[iLayer][iLevel]

    
    def SetCrystalPacketPlayerInfo(self, oHero, dCrystalPacketInfo):
        if self.m_ChooseLayer in dCrystalPacketInfo and self.m_ChooseLevel in dCrystalPacketInfo[self.m_ChooseLayer]:
            self.m_CrystalPacketPlayerInfo[oHero.m_ID] = dCrystalPacketInfo[self.m_ChooseLayer][self.m_ChooseLevel]

    
    def ComCrystal(self, oHero, lstAnswer):
        if not oHero.m_BackpackCon:
            return None
        if len(lstAnswer) != 3:
            BackpackLog.Alert('%s %s npc comcrystal err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, lstAnswer))
            return None
        (iMainCrystalID, iCostCrystalID, iCostCrystalID2) = lstAnswer
        lCostCrystal = [
            iCostCrystalID,
            iCostCrystalID2]
        oHero.m_BackpackCon.ComCrystal(iMainCrystalID, lCostCrystal)

    
    def GetGoodsMinCashAndTotalCach(self, oHero):
        if oHero.m_ID not in self.m_GoodsData:
            return (-1, -1)
        dGoodsData = self.m_GoodsData[oHero.m_ID]
        if not dGoodsData:
            return (-1, -1)
        lstGoodsCash = [ oGood.GetCash() for oGood in dGoodsData.values() if oGood ]
        iMinCash = min(lstGoodsCash)
        iTotalCash = sum(lstGoodsCash)
        return (iMinCash, iTotalCash)

    
    def InitGoodsInfo(self, oHero):
        self.InitCrystalGood(oHero)
        self.InitCrystalPacket(oHero)
        self.InitModulePacket(oHero)
        (iMinCash, iTotalCash) = self.GetGoodsMinCashAndTotalCach(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONSHOP, oHero, {
            'MinCash': iMinCash,
            'TotalCash': iTotalCash }, iSub = SEASONSHOP_INITS7GOODS)

    
    def GetShowInfo(self, iHero):
        if iHero not in self.m_ShowInfo:
            return ([], [], [])
        lstModulePacket = list(self.m_ShowInfo[iHero]['ModulePacket'].values())
        lstCrystalGoods = list(self.m_ShowInfo[iHero]['CrystalGoods'].values())
        lstCrystalPacket = list(self.m_ShowInfo[iHero]['CrystalPacket'].values())
        return (lstModulePacket, lstCrystalGoods, lstCrystalPacket)

    
    def RefreshShopUI(self, oHero):
        (lstModulePacket, lstCrystalGoods, lstCrystalPacket) = self.GetShowInfo(oHero.m_ID)
        net.GS2CS7Shop(oHero, self, lstModulePacket, lstCrystalGoods, lstCrystalPacket, iFullUpdate = 1)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.BuyCrystal, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, self.BuyPacket, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_DICT, self.RotateCrystalInCrystalPacket, self)
        self.SetRefreshTimesCallBack(oHero)

    
    def SetRefreshTimesCallBack(self, oHero):
        if oHero.Query(self.m_MPRefreshTimes, 0) or oHero.Query(self.m_CPRefreshTimes, 0):
            net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, self.RefreshPacketByType, self)

    
    def RefreshGoodsShow(self, oHero, oGoods, sKey):
        (iRefreshTimes, iMaxRefreshTimes) = self.GetRefreshTimes(oHero, oGoods.m_Pos)
        lstShowInfo = GETGOODINFO_FUNC[sKey](oGoods, iRefreshTimes, iMaxRefreshTimes)
        iFullUpdate = 0
        if sKey == 'ModulePacket':
            net.GS2CS7Shop(oHero, self, [
                lstShowInfo], [], [], iFullUpdate)
        elif sKey == 'CrystalGoods':
            net.GS2CS7Shop(oHero, self, [], [
                lstShowInfo], [], iFullUpdate)
        elif sKey == 'CrystalPacket':
            net.GS2CS7Shop(oHero, self, [], [], [
                lstShowInfo], iFullUpdate)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.BuyCrystal, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, self.BuyPacket, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_DICT, self.RotateCrystalInCrystalPacket, self)
        self.SetRefreshTimesCallBack(oHero)

    
    def CheckAllGoodsSellOut(self, oHero):
        if oHero.m_ID not in self.m_GoodsData:
            return 0
        dGoodsData = self.m_GoodsData[oHero.m_ID]
        if not dGoodsData:
            return 0
        for oGoods in dGoodsData.values():
            if oGoods.m_HasBuy < oGoods.m_CanBuy:
                return 0
        
        return 1

    
    def BuyCrystal(self, oHero, iGoodPos):
        BackpackLog.Debug('%s %s buy crystal %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos))
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iGoodPos not in self.m_GoodsData[iHero]:
            BackpackLog.Alert('%s %s not hero in gooddata' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGoods = self.m_GoodsData[iHero][iGoodPos]
        if not self.CanBuy(oHero, oGoods):
            BackpackLog.Alert('%s %s can not buy crystal' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oHero.AddCash(-oGoods.GetCash(), 'S7ShopBuy')
        oGoods.BuySuccess(oHero, oGoods.m_Items, iAmount = 1)
        iSellOutAll = self.CheckAllGoodsSellOut(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONSHOP, oHero, {
            'SellOutAll': iSellOutAll }, iSub = SEASONSHOP_BUYS7CRYSTAL)
        self.UpdateShowInfo(oHero, oGoods, 'CrystalGoods')
        self.RefreshGoodsShow(oHero, oGoods, 'CrystalGoods')

    
    def BuyPacket(self, oHero, iGoodPos, iPacketKey):
        BackpackLog.Debug('%s %s buy packet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iPacketKey))
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iGoodPos not in self.m_GoodsData[iHero]:
            BackpackLog.Alert('%s %s not hero in gooddata' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGoods = self.m_GoodsData[iHero][iGoodPos]
        if not self.CanBuy(oHero, oGoods):
            BackpackLog.Debug('%s %s can not buy packet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_WarCash, oGoods.GetCash()))
            return None
        lstGoods = oGoods.m_Items
        lstSelectGoods = []
        for dGoodsInfo in lstGoods:
            if 'PacketKey' not in dGoodsInfo:
                BackpackLog.Alert('%s %s not packet %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dGoodsInfo))
                continue
            if dGoodsInfo['PacketKey'] == iPacketKey:
                lstSelectGoods = [
                    dGoodsInfo]
                break
        
        if not lstSelectGoods:
            BackpackLog.Alert('%s %s not selectgoods' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oHero.AddCash(-oGoods.GetCash(), 'S7ShopBuy')
        oGoods.BuySuccess(oHero, lstSelectGoods, iAmount = 1)
        iSellOutAll = self.CheckAllGoodsSellOut(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONSHOP, oHero, {
            'SellOutAll': iSellOutAll }, iSub = SEASONSHOP_BUYS7PACKET)
        sKey = 'CrystalPacket' if oGoods.m_GoodsType == VIRTUAL_ITEM_S7CRYSTALPACKET else 'ModulePacket'
        self.UpdateShowInfo(oHero, oGoods, sKey)
        self.RefreshGoodsShow(oHero, oGoods, sKey)

    
    def GetCurMaxPos(self, iHero):
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if not dGoodsMenu:
            return 0
        return max(dGoodsMenu)

    
    def SetGoods(self, oHero, iPos, oGoods, sKey, iRefresh = 0):
        iHero = oHero.m_ID
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if iPos in dGoodsMenu:
            if not iRefresh:
                BackpackLog.Alert('%s %s shop setrepeat %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu)))
                return None
            if dGoodsMenu[iPos]:
                dGoodsMenu[iPos].Disable()
        dGoodsMenu[iPos] = oGoods
        oGoods.m_Pos = iPos
        self.UpdateShowInfo(oHero, oGoods, sKey)

    
    def UpdateShowInfo(self, oHero, oGoods, sKey):
        iHero = oHero.m_ID
        if iHero not in self.m_ShowInfo:
            self.m_ShowInfo[iHero] = {
                'ModulePacket': { },
                'CrystalGoods': { },
                'CrystalPacket': { } }
        (iRefreshTimes, iMaxRefreshTimes) = self.GetRefreshTimes(oHero, oGoods.m_Pos)
        lstShowInfo = GETGOODINFO_FUNC[sKey](oGoods, iRefreshTimes, iMaxRefreshTimes)
        self.m_ShowInfo[iHero][sKey][oGoods.m_Pos] = lstShowInfo

    
    def InitCrystalGood(self, oHero):
        iCurPos = self.GetCurMaxPos(oHero.m_ID) + 1
        for iPos in range(iCurPos, iCurPos + self.m_CrystalGoodNum):
            self.SetCrystalGood(oHero, iPos)
        

    
    def SetCrystalGood(self, oHero, iPos, iRefresh = 0):
        dRandomInfo = self.m_CrystalGoodInfo
        (iCrystal, dGoods) = self.GetRandomCrystalInfo(oHero, dRandomInfo, { }, VIRTUAL_ITEM_S7CRYSTAL)
        if not iCrystal:
            BackpackLog.Alert('%s %s not crystal packet cost' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        iCash = cl_formula.GetResultByData(self, self.m_CrystalGoodCost, self.m_FormulaLimit)
        if not iCash:
            BackpackLog.Alert('%s %s not crystal goods cost' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGoods = cl_shop.CreateGoodsByData(iCrystal, VIRTUAL_ITEM_S7CRYSTAL, iCash, OBTAIN_WARCASH, S7GOODS_CANBUYTIME, [
            dGoods], iHide = 0)
        self.SetGoods(oHero, iPos, oGoods, 'CrystalGoods', iRefresh)

    
    def GetRandomCrystalInfo(self, oHero, dRandomInfo, dHasChooseCrystal, iType):
        oGame = self.m_Game
        iGoodSID = ChooseKey(oGame, dRandomInfo)
        clsData = GetS7GoodsData(iGoodSID)
        if not clsData:
            BackpackLog.Alert('%s %s not crystalgood %s %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID, dRandomInfo))
            return (0, { })
        tInternalGoodRule = clsData.m_InternalGoodRule
        if not tInternalGoodRule:
            BackpackLog.Alert('%s %s not crystalrule %s %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID, dRandomInfo))
            return (0, { })
        oChooseFunc = tInternalGoodRule[0]
        tResult = oChooseFunc(oGame, oHero, dHasChooseCrystal)
        if not tResult:
            BackpackLog.Alert('%s %s not crystal choose %s %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID, dRandomInfo))
            tResult = self.m_DefaultCrystal
        (iCrystal, iTotalPoint) = tResult
        dCrystal = {
            'SID': iCrystal,
            'TP': iTotalPoint,
            'PI': clseason7.CalInitPointInfo(oGame, iCrystal, iTotalPoint) }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7CRYSTALSHOPINIT, oHero, {
            'CrystalInfo': dCrystal })
        dGoods = {
            'item': iType,
            'info': dCrystal }
        return (iCrystal, dGoods)

    
    def InitCrystalPacket(self, oHero):
        iCurPos = self.GetCurMaxPos(oHero.m_ID) + 1
        for iPos in range(iCurPos, iCurPos + self.m_CrystalPacketNum):
            self.SetCrystalPacket(oHero, iPos)
        

    
    def SetCrystalPacket(self, oHero, iPos, iRefresh = 0, lstLockPos = None):
        dRandomInfo = self.m_CrystalPacketPlayerInfo.get(oHero.m_ID, self.m_CrystalPacketInfo)
        if not dRandomInfo:
            BackpackLog.Alert('%s %s not module crystal packet choose' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGame = self.m_Game
        iGoodSID = ChooseKey(oGame, dRandomInfo)
        clsData = GetS7GoodsData(iGoodSID)
        if not clsData:
            BackpackLog.Alert('%s %s not crystalpacket %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID, dRandomInfo))
            return None
        dLockGoodInfo = self.GetLockGoodInfo(oHero, iPos, lstLockPos) if lstLockPos and iRefresh else { }
        lstGoods = self.GetCrystalGoodsInfo(oHero, iGoodSID, clsData, dLockGoodInfo)
        if not lstGoods:
            return None
        iCash = cl_formula.GetResultByData(self, self.m_CrystalPacketCost, self.m_FormulaLimit)
        if iCash < 0:
            BackpackLog.Alert('%s %s set err crystal packet cash %s' % (oGame.m_ID, oHero.m_PlayerID, iCash))
            return None
        oGoods = cl_shop.CreateGoodsByData(0, VIRTUAL_ITEM_S7CRYSTALPACKET, iCash, OBTAIN_WARCASH, S7GOODS_CANBUYTIME, lstGoods, iHide = 0)
        dMsgInfo = {
            'MaxPoint': clsData.m_ShowMaxPoint }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7SHOP, oHero, dMsgInfo, iSub = S7SHOP_ADD_CRYSTALGOODS)
        iMaxPoint = dMsgInfo['MaxPoint']
        oGoods.SetShowInfo({
            'MaxPoint': iMaxPoint })
        if not iRefresh and clsData.m_CanRefresh:
            self.SetRefreshTime(oHero, iPos, oHero.Query(self.m_CPRefreshTimes, 0))
        self.SetGoods(oHero, iPos, oGoods, 'CrystalPacket', iRefresh)

    
    def GetCrystalGoodsInfo(self, oHero, iGoodSID, clsData, dLockPos):
        oGame = self.m_Game
        lstGoods = []
        dHasChooseCrystal = { }
        for dGoods in dLockPos.values():
            dHasChooseCrystal[(dGoods['info']['SID'], dGoods['info']['TP'])] = 1
        
        for iPacketKey, oChooseFunc in enumerate(clsData.m_InternalGoodRule):
            if iPacketKey in dLockPos:
                dGoods = dLockPos[iPacketKey]
            else:
                tResult = oChooseFunc(oGame, oHero, dHasChooseCrystal)
                if not tResult:
                    BackpackLog.Alert('%s %s not crystal choose %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID, dHasChooseCrystal))
                    tResult = self.m_DefaultCrystal
                (iCrystal, iTotalPoint) = tResult
                if self.m_CrystalPacketDiff:
                    dHasChooseCrystal[tResult] = 1
                dCrystalInfo = {
                    'SID': iCrystal,
                    'TP': iTotalPoint,
                    'PI': clseason7.CalInitPointInfo(oGame, iCrystal, iTotalPoint),
                    'R': 0 }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7CRYSTALSHOPINIT, oHero, {
                    'CrystalInfo': dCrystalInfo })
                dGoods = {
                    'item': VIRTUAL_ITEM_S7CRYSTALPACKET,
                    'info': dCrystalInfo,
                    'PacketKey': iPacketKey }
            lstGoods.append(dGoods)
        
        return lstGoods

    
    def RotateCrystalInCrystalPacket(self, oHero, dData):
        iGoodPos = dData.get(0, -1)
        iPacketKey = dData.get(1, -1)
        BackpackLog.Debug('%s %s rotate in packet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iPacketKey))
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iGoodPos not in self.m_GoodsData[iHero]:
            BackpackLog.Alert('%s %s rotate not hero in gooddata %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos))
            return None
        oGoods = self.m_GoodsData[iHero][iGoodPos]
        lstGoods = oGoods.m_Items
        dCrystalInfo = { }
        for dGoodsInfo in lstGoods:
            if 'PacketKey' not in dGoodsInfo:
                BackpackLog.Alert('%s %s rotate not packet %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dGoodsInfo))
                continue
            dCrystalInfo = dGoodsInfo['info'] if dGoodsInfo['PacketKey'] == iPacketKey or 'info' in dGoodsInfo else { }
        
        if not dCrystalInfo:
            BackpackLog.Alert('%s %s not rotate info %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dGoodsInfo, iPacketKey))
            return None
        dCrystalPointInfo = dCrystalInfo.get('PI', { })
        iCrystalRotate = dCrystalInfo.get('R', 0)
        if not dCrystalInfo:
            return None
        dNewCrystalPointInfo = { }
        for tOldPos, iPoint in dCrystalPointInfo.items():
            (x, y) = tOldPos
            tNewPos = (-y, x)
            dNewCrystalPointInfo[tNewPos] = iPoint
        
        dCrystalInfo['PI'] = dNewCrystalPointInfo
        dCrystalInfo['R'] = (iCrystalRotate + 1) % CALPOINT_CNTMAX
        self.RefreshGoodsShow(oHero, oGoods, 'CrystalPacket')

    
    def GetLockGoodInfo(self, oHero, iPos, lstLockPos):
        iHero = oHero.m_ID
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if iPos not in dGoodsMenu:
            BackpackLog.Alert('%s %s get lockgood pos err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
            return { }
        oGoods = dGoodsMenu[iPos]
        lstGoodsInfo = oGoods.m_Items
        if len(lstLockPos) >= len(lstGoodsInfo):
            BackpackLog.Alert('%s %s get lockgood num err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
            return { }
        dLockGood = { }
        iGoodType = oGoods.m_GoodsType
        if iGoodType == VIRTUAL_ITEM_S7MODULE:
            for iSubPos, dGoodsInfo in enumerate(lstGoodsInfo):
                iPacketKey = dGoodsInfo['PacketKey']
                if iPacketKey not in lstLockPos:
                    continue
                dLockGood[iSubPos] = dGoodsInfo
            
        elif iGoodType == VIRTUAL_ITEM_S7CRYSTALPACKET:
            for dGoodsInfo in lstGoodsInfo:
                iPacketKey = dGoodsInfo['PacketKey']
                if iPacketKey not in lstLockPos:
                    continue
                dLockGood[iPacketKey] = dGoodsInfo
            
        else:
            BackpackLog.Alert('%s %s get lockgood type err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
        return dLockGood

    
    def InitModulePacket(self, oHero):
        dModulePacketChoose = self.m_ModulePacketChoose
        if not dModulePacketChoose:
            BackpackLog.Alert('%s %s not module packet choose' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        iCurPos = self.GetCurMaxPos(oHero.m_ID) + 1
        for iPos in range(iCurPos, iCurPos + self.m_ModulePacketNum):
            self.SetModulePacket(oHero, iPos, dModulePacketChoose)
        

    
    def SetModulePacket(self, oHero, iPos, dModulePacketChoose, iRefresh = 0, lstLockPos = None):
        oGame = self.m_Game
        iGoodSID = ChooseKey(oGame, dModulePacketChoose)
        clsData = GetS7GoodsData(iGoodSID)
        if not clsData:
            BackpackLog.Alert('%s %s not module packet goods %s %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID, dModulePacketChoose))
            return None
        dPlayerCacheModuleInfo = self.m_CacheModuleGoods.setdefault(oHero.m_PlayerID, { })
        dCacheModuleInfo = dPlayerCacheModuleInfo.setdefault(iPos, { })
        dLockGoodInfo = self.GetLockGoodInfo(oHero, iPos, lstLockPos) if lstLockPos and iRefresh else { }
        lstGoods = self.GetModuleGoodsInfo(oGame, oHero, clsData, iGoodSID, dCacheModuleInfo, dLockGoodInfo)
        if not lstGoods:
            return None
        iCash = cl_formula.GetResultByData(self, self.m_ModulePacketCost, self.m_FormulaLimit)
        if iCash < 0:
            BackpackLog.Alert('%s %s set err module packet cash %s' % (oGame.m_ID, oHero.m_PlayerID, iCash))
            return None
        if iRefresh:
            self.m_CacheModuleGoods[oHero.m_PlayerID][iPos] = self.BuildLastModuleCache(oHero, iPos)
        oGoods = cl_shop.CreateGoodsByData(iGoodSID, VIRTUAL_ITEM_S7MODULE, iCash, OBTAIN_WARCASH, S7GOODS_CANBUYTIME, lstGoods, iHide = 0)
        if not iRefresh and clsData.m_CanRefresh:
            self.SetRefreshTime(oHero, iPos, oHero.Query(self.m_MPRefreshTimes, 0))
        self.SetGoods(oHero, iPos, oGoods, 'ModulePacket', iRefresh)

    
    def BuildLastModuleCache(self, oHero, iPos):
        dCacheModuleInfo = { }
        if oHero.m_ID not in self.m_GoodsData:
            return dCacheModuleInfo
        dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        if iPos not in dGoodsMenu:
            return dCacheModuleInfo
        oLastGoods = dGoodsMenu[iPos]
        for dModuleInfo in oLastGoods.m_Items:
            if 'PacketKey' not in dModuleInfo or 'info' not in dModuleInfo or 'QL' not in dModuleInfo['info']:
                continue
            tKey = (dModuleInfo['PacketKey'], dModuleInfo['info']['QL'])
            dCacheModuleInfo[tKey] = 1
        
        return dCacheModuleInfo

    
    def GetExtraGoodNum(self, oHero):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return 0
        iLevel = oScene.m_Level
        iLevelType = oLevelCtrl.GetLevelType(iLevel)
        if iLevelType == LEVEL_TYPE_BOSS:
            return oHero.Query('S7BossLevelExtraGoodNum', 0)
        return oHero.Query('S7ExtraGoodNum', 0)

    
    def GetModuleGoodsInfo(self, oGame, oHero, clsData, iGoodSID, dCacheModuleInfo = None, dLockGoodInfo = None):
        lstGoods = []
        if clsData.m_GoodsDataType == S7GOODS_SINGLE_DEPOLY:
            dHistoryChooseModule = self.m_ModulePacketHasChoose.setdefault(oHero.m_PlayerID, { })
            dChooseModule = { }
            if dLockGoodInfo:
                for dGoods in dLockGoodInfo.values():
                    iPacketKey = dGoods['info']['SID']
                    iQuality = dGoods['info']['QL']
                    dChooseModule[(iPacketKey, iQuality)] = 1
                
            if dCacheModuleInfo is None:
                dCacheModuleInfo = { }
            iExtraGoodNum = self.GetExtraGoodNum(oHero)
            lstGoodRule = list(clsData.m_InternalGoodRule) + list(clsData.m_ExtraGoodRule)[:iExtraGoodNum]
            for iSubPos, oChooseFunc in enumerate(lstGoodRule):
                if dLockGoodInfo and iSubPos in dLockGoodInfo:
                    dGoods = dLockGoodInfo[iSubPos]
                else:
                    tResult = oChooseFunc(oGame, oHero, dChooseModule, dHistoryChooseModule, dCacheModuleInfo)
                    if not tResult:
                        BackpackLog.Alert('%s %s not module can choose %s %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID, dChooseModule))
                        continue
                    (iPacketKey, iQuality) = tResult
                    dChooseModule[(iPacketKey, iQuality)] = 1
                    if not clsData.m_RefreshCanRepeat:
                        dHistoryChooseModule[(iPacketKey, iQuality)] = 1
                    dGoods = {
                        'item': VIRTUAL_ITEM_S7MODULE,
                        'info': {
                            'SID': iPacketKey,
                            'QL': iQuality },
                        'PacketKey': iPacketKey }
                lstGoods.append(dGoods)
            
        elif clsData.m_GoodsDataType == S7GOODS_ALL_DEPOLY:
            if not clsData.m_InternalGoodRule:
                BackpackLog.Alert('%s %s not modulerule %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID))
                return []
            oChooseFunc = clsData.m_InternalGoodRule[0]
            lstResult = oChooseFunc(oGame, oHero)
            if not lstResult:
                BackpackLog.Alert('%s %s not module can get %s' % (oGame.m_ID, oHero.m_PlayerID, iGoodSID))
                return []
            for tResult in lstResult:
                (iPacketKey, iQuality) = tResult
                dGoods = {
                    'item': VIRTUAL_ITEM_S7MODULE,
                    'info': {
                        'SID': iPacketKey,
                        'QL': iQuality },
                    'PacketKey': iPacketKey }
                lstGoods.append(dGoods)
            
        return lstGoods

    
    def RefreshPacketByType(self, oHero, lstAnswer):
        oGame = self.m_Game
        iHero = oHero.m_ID
        iPlayerID = oHero.m_PlayerID
        if not lstAnswer:
            BackpackLog.Alert('%s %s %s refresh not answer' % (oGame.m_ID, iHero, iPlayerID))
            return None
        iUseTime = 1 if not oHero.Query('NotUseRefreshTime') else 0
        iPos = lstAnswer[0]
        lstLockPos = lstAnswer[1:]
        if not self.UpdateRefreshTimes(oHero, iPos, -iUseTime):
            BackpackLog.Alert('%s %s %s not refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, self.m_RefreshTimes))
            return None
        if iHero not in self.m_GoodsData:
            BackpackLog.Alert('%s %s %s not hero id refresh %s %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, iHero, self.m_GoodsData))
            return None
        dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        if iPos not in dGoodsMenu:
            BackpackLog.Alert('%s %s %s not pos refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, dGoodsMenu))
            return None
        oGoods = dGoodsMenu[iPos]
        if not self.CanReplace(oGoods):
            BackpackLog.Alert('%s %s %s not can replace refresh %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer))
            return None
        iGoodsType = oGoods.m_GoodsType
        if iGoodsType == VIRTUAL_ITEM_S7CRYSTALPACKET:
            self.SetCrystalPacket(oHero, iPos, iRefresh = 1, lstLockPos = lstLockPos)
        elif iGoodsType == VIRTUAL_ITEM_S7MODULE and self.m_ModulePacketChoose:
            self.SetModulePacket(oHero, iPos, self.m_ModulePacketChoose, iRefresh = 1, lstLockPos = lstLockPos)
        BackpackLog.Debug('%s %s %s s7 goods refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, iGoodsType))
        self.RefreshShopUI(oHero)



def GetCrystalGoodShowInfo(oGoods, iRefreshTimes, iMaxRefreshTimes):
    lstGoodsInfo = oGoods.m_Items
    if not lstGoodsInfo:
        return []
    dGoodsInfo = lstGoodsInfo[0]['info']
    iSellOut = 1 if oGoods.m_HasBuy >= oGoods.m_CanBuy else 0
    lstPointInfo = [ [
x,
y,
iPoint] for (x, y), iPoint in dGoodsInfo['PI'].items() ]
    return [
        oGoods.m_Pos,
        dGoodsInfo['SID'],
        lstPointInfo,
        iSellOut,
        oGoods.GetCash()]


def GetCrystalPacketShowInfo(oGoods, iRefreshTimes, iMaxRefreshTimes):
    lstGoodsInfo = oGoods.m_Items
    if not lstGoodsInfo:
        return []
    lstInternalInfo = []
    for dGoodsInfo in lstGoodsInfo:
        iPacketKey = dGoodsInfo['PacketKey']
        lstPointInfo = [ [
x,
y,
iPoint] for (x, y), iPoint in dGoodsInfo['info']['PI'].items() ]
        lstInternalInfo.append([
            iPacketKey,
            dGoodsInfo['info']['SID'],
            lstPointInfo])
    
    iSellOut = 1 if oGoods.m_HasBuy >= oGoods.m_CanBuy else 0
    return [
        oGoods.m_Pos,
        iSellOut,
        oGoods.GetCash(),
        iRefreshTimes,
        iMaxRefreshTimes,
        oGoods.GetShowInfo()['MaxPoint'],
        lstInternalInfo]


def GetModulePacketShowInfo(oGoods, iRefreshTimes, iMaxRefreshTimes):
    lstGoodsInfo = oGoods.m_Items
    if not lstGoodsInfo:
        return []
    lstInternalInfo = []
    for dGoodsInfo in lstGoodsInfo:
        iPacketKey = dGoodsInfo['info']['SID']
        lstInternalInfo.append([
            iPacketKey,
            dGoodsInfo['info']['QL']])
    
    iSellOut = 1 if oGoods.m_HasBuy >= oGoods.m_CanBuy else 0
    return [
        oGoods.m_Pos,
        iSellOut,
        oGoods.GetCash(),
        iRefreshTimes,
        iMaxRefreshTimes,
        lstInternalInfo]

GETGOODINFO_FUNC = {
    'CrystalGoods': GetCrystalGoodShowInfo,
    'CrystalPacket': GetCrystalPacketShowInfo,
    'ModulePacket': GetModulePacketShowInfo }
