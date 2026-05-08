# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/s8shopnpc.pyc
# RelativePath: clientlogic/cl_npc/s8shopnpc.pyc
# Source Generated with Decompyle++
# File: s8shopnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUELIST, NPC_CB_LIST, NPC_CB_VALUE, VIRTUAL_ITEM_S8GEMITEM, VIRTUAL_ITEM_S8THIRDPERFORM, OBTAIN_WARCASH, MAX_LAYER
from cl_only import ChooseKey
from . import seasonshopnpc
from . import net
from cl_object.logging import SeasoneightLog
from cl_seasonplay.season8.s8goodsdata import GetS8GoodsData
import cl_formula
import cl_shop
DEFAULT_PACKETCOST = 125
S8GOODS_CANBUYTIME = 1
S8GOODS_EXTRA_REFRESHTIMES_KEY = 'S8GoodsExtraRefreshTimes'

class CS8ShopNpc(seasonshopnpc.CSeasonShopNPC):
    m_Season = 8
    m_TPFRefreshTimes = 'ThirdPFPacketRefreshTimes'
    m_GemRefreshTimes = 'GemPacketRefreshTimes'
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_ShowInfo = { }
        self.m_RefreshTimes = { }
        self.m_ThirdPFPacketCost = 0
        self.m_GemPacketCost = 0
        self.m_ThirdPFPacketWeightInfo = { }
        self.m_ThirdPFPacketPlayerWeightInfo = { }
        self.m_GemPacketWeightInfo = { }
        self.m_GemPacketPlayerWeightInfo = { }
        self.m_ThirdPFPacketNum = 0
        self.m_GemPacketNum = 0
        self.m_ChooseLayer = 0
        self.m_ChooseLevel = 0
        self.m_HeroAbandonBuy = { }

    
    def SetInitData(self, iPFPacketCost, iGemPacketCost, dPFPacketConfigInfo, dGemPacketConfigInfo):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            SeasoneightLog.Alert('%s not levelctrl' % oGame.m_ID)
            return None
        self.m_ThirdPFPacketCost = iPFPacketCost
        self.m_GemPacketCost = iGemPacketCost
        iMaxLayer = self.m_FormulaLimit['MaxLayer'] if 'MaxLayer' in self.m_FormulaLimit else MAX_LAYER
        iLayer = min(iMaxLayer, oLevelCtrl.m_LayerNum)
        iMaxLevel = self.m_FormulaLimit['MaxLevel'] if 'MaxLevel' in self.m_FormulaLimit else 99
        iLevel = oLevelCtrl.m_LevelNum
        if iMaxLayer == iLayer and iLevel > iMaxLevel:
            iLevel = iMaxLevel
        self.m_ChooseLevel = iLevel
        self.m_ChooseLayer = iLayer
        if iLayer in dPFPacketConfigInfo:
            for (iConfigLevel, iPacketNum), dPFPacketWeightInfo in dPFPacketConfigInfo[iLayer].items():
                if iLevel == iConfigLevel:
                    self.m_ThirdPFPacketNum = iPacketNum
                    self.m_ThirdPFPacketWeightInfo = dPFPacketWeightInfo
            
        if iLayer in dGemPacketConfigInfo:
            for (iConfigLevel, iPacketNum), dGemPacketWeightInfo in dGemPacketConfigInfo[iLayer].items():
                if iLevel == iConfigLevel:
                    self.m_GemPacketNum = iPacketNum
                    self.m_GemPacketWeightInfo = dGemPacketWeightInfo
            

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        oGame = self.m_Game
        if oGame and oGame.m_WarMgr:
            oWarMgr = oGame.m_WarMgr
            for iHero in oWarMgr.GetRoomHero():
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                if iHero not in self.m_GoodsData:
                    iRewardRefreshTimes = self.m_ThirdPFPacketNum + self.m_GemPacketNum
                    oHero.Set(S8GOODS_EXTRA_REFRESHTIMES_KEY, oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0) + iRewardRefreshTimes)
                    continue
                dGoodsInfo = self.m_GoodsData[iHero]
                for iPos, oGoods in dGoodsInfo.items():
                    if CheckGoodsSellOut(self, oHero, oGoods):
                        continue
                    oHero.Set(S8GOODS_EXTRA_REFRESHTIMES_KEY, oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0) + 1)
                
            
        return super().Release()

    
    def InitGoodsInfo(self, oHero):
        self.InitThirdPFPacket(oHero)
        self.InitGemPacket(oHero)

    
    def RefreshShopUI(self, oHero):
        (lstThirdPFPacket, lstGemPacket) = self.GetShowInfo(oHero.m_ID)
        net.GS2CS8Shop(oHero, self, lstThirdPFPacket, lstGemPacket, iFullUpdate = 1)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, self.BuyPacket, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.PlayerAbandonBuyGoods, self)
        self.SetRefreshTimesCallBack(oHero)

    
    def GetShowInfo(self, iHero):
        if iHero not in self.m_ShowInfo:
            return ([], [])
        lstThirdPFPacket = list(self.m_ShowInfo[iHero]['ThirdPFPacket'].values())
        lstGemPacket = list(self.m_ShowInfo[iHero]['GemPacket'].values())
        return (lstThirdPFPacket, lstGemPacket)

    
    def GetCurMaxPos(self, iHero):
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if not dGoodsMenu:
            return 0
        return max(dGoodsMenu)

    
    def BuyPacket(self, oHero, iGoodPos, iPacketKey):
        SeasoneightLog.Debug('%s %s buy packet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodPos, iPacketKey))
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iGoodPos not in self.m_GoodsData[iHero]:
            SeasoneightLog.Alert('%s %s not hero in gooddata' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGoods = self.m_GoodsData[iHero][iGoodPos]
        if not self.CanBuy(oHero, oGoods):
            SeasoneightLog.Debug('%s %s can not buy packet %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_WarCash, oGoods.GetCash()))
            return None
        lstGoods = oGoods.m_Items
        lstSelectGoods = []
        for dGoodsInfo in lstGoods:
            if 'PacketKey' not in dGoodsInfo:
                SeasoneightLog.Alert('%s %s not packet %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dGoodsInfo))
                continue
            if dGoodsInfo['PacketKey'] == iPacketKey:
                lstSelectGoods = [
                    dGoodsInfo]
                break
        
        if not lstSelectGoods:
            SeasoneightLog.Alert('%s %s not selectgoods' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oHero.AddCash(-oGoods.GetCash(), 'S8ShopBuy')
        oGoods.BuySuccess(oHero, lstSelectGoods, iAmount = 1)
        sKey = 'ThirdPFPacket' if oGoods.m_GoodsType == VIRTUAL_ITEM_S8THIRDPERFORM else 'GemPacket'
        self.UpdateShowInfo(oHero, oGoods, sKey)
        self.RefreshGoodsShow(oHero, oGoods, sKey)

    
    def CheckAllGoodsSellOut(self, oHero):
        if oHero.m_ID not in self.m_GoodsData:
            return 0
        dGoodsData = self.m_GoodsData[oHero.m_ID]
        if not dGoodsData:
            return 0
        for oGoods in dGoodsData.values():
            if oGoods.m_HasBuy < oGoods.m_CanBuy:
                lstAbandonPos = self.m_HeroAbandonBuy.get(oHero.m_ID, [])
                if oGoods.m_Pos not in lstAbandonPos:
                    return 0
        
        return 1

    
    def RefreshGoodsShow(self, oHero, oGoods, sKey):
        (iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes) = self.GetRefreshTimes(oHero, oGoods.m_Pos)
        lstShowInfo = GetGoodsShowInfoByKey(sKey, self, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes)
        iFullUpdate = 0
        if sKey == 'ThirdPFPacket':
            net.GS2CS8Shop(oHero, self, [
                lstShowInfo], [], iFullUpdate)
        elif sKey == 'GemPacket':
            net.GS2CS8Shop(oHero, self, [], [
                lstShowInfo], iFullUpdate)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, self.BuyPacket, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.PlayerAbandonBuyGoods, self)
        self.SetRefreshTimesCallBack(oHero)

    
    def RefreshHeroAllGoodsShow(self, oHero):
        iHero = oHero.m_ID
        dGoodInfo = self.m_GoodsData.get(iHero, { })
        for oGoods in dGoodInfo.values():
            sKey = 'ThirdPFPacket' if oGoods.m_GoodsType == VIRTUAL_ITEM_S8THIRDPERFORM else 'GemPacket'
            self.UpdateShowInfo(oHero, oGoods, sKey)
            self.RefreshGoodsShow(oHero, oGoods, sKey)
        

    
    def SetRefreshTimesCallBack(self, oHero):
        if oHero.Query(self.m_TPFRefreshTimes, 0) or oHero.Query(self.m_GemRefreshTimes, 0) or oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0):
            net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, self.RefreshPacketByType, self)

    
    def RefreshPacketByType(self, oHero, lstAnswer):
        oGame = self.m_Game
        iHero = oHero.m_ID
        iPlayerID = oHero.m_PlayerID
        if not lstAnswer:
            SeasoneightLog.Alert('%s %s %s refresh not answer' % (oGame.m_ID, iHero, iPlayerID))
            return None
        iUseTime = 1 if not oHero.Query('NotUseRefreshTime') else 0
        iPos = lstAnswer[0]
        lstLockPos = lstAnswer[1:]
        if not self.UpdateRefreshTimes(oHero, iPos, -iUseTime):
            SeasoneightLog.Alert('%s %s %s not refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, self.m_RefreshTimes))
            return None
        if iHero not in self.m_GoodsData:
            SeasoneightLog.Alert('%s %s %s not hero id refresh %s %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, iHero, self.m_GoodsData))
            return None
        dGoodsMenu = self.m_GoodsData[oHero.m_ID]
        if iPos not in dGoodsMenu:
            SeasoneightLog.Alert('%s %s %s not pos refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, dGoodsMenu))
            return None
        oGoods = dGoodsMenu[iPos]
        if not self.CanReplace(oGoods):
            SeasoneightLog.Alert('%s %s %s not can replace refresh %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer))
            return None
        iGoodsType = oGoods.m_GoodsType
        if iGoodsType == VIRTUAL_ITEM_S8THIRDPERFORM:
            self.SetThirdPFPacket(oHero, iPos, iRefresh = 1, lstLockPos = lstLockPos)
        elif iGoodsType == VIRTUAL_ITEM_S8GEMITEM:
            self.SetGemPacket(oHero, iPos, iRefresh = 1, lstLockPos = lstLockPos)
        SeasoneightLog.Debug('%s %s %s s8 goods refresh %s %s' % (oGame.m_ID, iHero, iPlayerID, lstAnswer, iGoodsType))
        self.RefreshHeroAllGoodsShow(oHero)
        self.RefreshShopUI(oHero)

    
    def InitThirdPFPacket(self, oHero):
        iCurPos = self.GetCurMaxPos(oHero.m_ID) + 1
        for iPos in range(iCurPos, iCurPos + self.m_ThirdPFPacketNum):
            self.SetThirdPFPacket(oHero, iPos)
        

    
    def SetThirdPFPacket(self, oHero, iPos, iRefresh = 0, lstLockPos = None):
        dThirdPFWeightInfo = self.m_ThirdPFPacketPlayerWeightInfo.get(oHero.m_ID, self.m_ThirdPFPacketWeightInfo)
        if not dThirdPFWeightInfo:
            SeasoneightLog.Alert('%s %s not thirdpf packet goods weight' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGame = self.m_Game
        iGoodSID = ChooseKey(oGame, dThirdPFWeightInfo)
        clsGoodData = GetS8GoodsData(iGoodSID)
        if not clsGoodData:
            SeasoneightLog.Alert('%s %s not thirdpacket good %s ' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID))
            return None
        if clsGoodData.m_GoodsDataType != VIRTUAL_ITEM_S8THIRDPERFORM:
            SeasoneightLog.Alert('%s %s thirdpf packet config err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID))
            return None
        dLockGoodInfo = self.GetLockGoodInfo(oHero, iPos, lstLockPos) if lstLockPos and iRefresh else { }
        lstGoods = self.GetPacketGoodsInfo(oGame, oHero, iGoodSID, clsGoodData, dLockGoodInfo)
        if not lstGoods:
            return None
        iCash = cl_formula.GetResultByData(self, self.m_ThirdPFPacketCost, self.m_FormulaLimit)
        if iCash < 0:
            SeasoneightLog.Alert('%s %s thirdpf packet cost err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iCash))
            iCash = DEFAULT_PACKETCOST
        oGoods = cl_shop.CreateGoodsByData(iGoodSID, VIRTUAL_ITEM_S8THIRDPERFORM, iCash, OBTAIN_WARCASH, S8GOODS_CANBUYTIME, lstGoods, iHide = 0)
        if not iRefresh:
            self.SetRefreshTime(oHero, iPos, oHero.Query(self.m_TPFRefreshTimes, 0))
        self.SetGoods(oHero, iPos, oGoods, 'ThirdPFPacket', iRefresh)

    
    def InitGemPacket(self, oHero):
        iCurPos = self.GetCurMaxPos(oHero.m_ID) + 1
        for iPos in range(iCurPos, iCurPos + self.m_GemPacketNum):
            self.SetGemPacket(oHero, iPos)
        

    
    def SetGemPacket(self, oHero, iPos, iRefresh = 0, lstLockPos = None):
        dGemPacketWeightInfo = self.m_GemPacketPlayerWeightInfo.get(oHero.m_ID, self.m_GemPacketWeightInfo)
        if not dGemPacketWeightInfo:
            SeasoneightLog.Alert('%s %s not gem packet goods weight' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGame = self.m_Game
        iGoodSID = ChooseKey(oGame, dGemPacketWeightInfo)
        clsGoodData = GetS8GoodsData(iGoodSID)
        if not clsGoodData:
            SeasoneightLog.Alert('%s %s not gem good %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID))
            return None
        if clsGoodData.m_GoodsDataType != VIRTUAL_ITEM_S8GEMITEM:
            SeasoneightLog.Alert('%s %s gempacket config err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID))
            return None
        dLockGoodInfo = self.GetLockGoodInfo(oHero, iPos, lstLockPos) if lstLockPos and iRefresh else { }
        lstGoods = self.GetPacketGoodsInfo(oGame, oHero, iGoodSID, clsGoodData, dLockGoodInfo)
        if not lstGoods:
            return None
        iCash = cl_formula.GetResultByData(self, self.m_GemPacketCost, self.m_FormulaLimit)
        if iCash < 0:
            SeasoneightLog.Alert('%s %s gem packet cost err %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iCash))
            iCash = DEFAULT_PACKETCOST
        oGoods = cl_shop.CreateGoodsByData(iGoodSID, VIRTUAL_ITEM_S8GEMITEM, iCash, OBTAIN_WARCASH, S8GOODS_CANBUYTIME, lstGoods, iHide = 0)
        if not iRefresh:
            self.SetRefreshTime(oHero, iPos, oHero.Query(self.m_GemRefreshTimes, 0))
        self.SetGoods(oHero, iPos, oGoods, 'GemPacket', iRefresh)

    
    def GetLockGoodInfo(self, oHero, iPos, lstLockPos):
        iHero = oHero.m_ID
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if iPos not in dGoodsMenu:
            SeasoneightLog.Alert('%s %s get lockgood pos err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
            return { }
        oGoods = dGoodsMenu[iPos]
        lstGoodsInfo = oGoods.m_Items
        dLockGood = { }
        if oGoods.m_GoodsType in (VIRTUAL_ITEM_S8GEMITEM, VIRTUAL_ITEM_S8THIRDPERFORM):
            if len(lstLockPos) >= len(lstGoodsInfo):
                SeasoneightLog.Alert('%s %s get lockgood num err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
                return { }
            for dGoodsInfo in lstGoodsInfo:
                iPacketKey = dGoodsInfo['PacketKey']
                if iPacketKey not in lstLockPos:
                    continue
                iPos = dGoodsInfo.get('Pos', -1)
                if iPos == -1:
                    continue
                dLockGood[iPos] = dGoodsInfo
            
        else:
            SeasoneightLog.Alert('%s %s get lockgood type err %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu), lstLockPos))
        return dLockGood

    
    def GetPacketGoodsInfo(self, oGame, oHero, iGoodSID, clsGoodData, dLockGoodInfo = None):
        dHasChooseInfo = { }
        if dLockGoodInfo:
            for dGoods in dLockGoodInfo.values():
                iPacketKey = dGoods['info']['SID']
                iQuality = dGoods['info']['QL']
                dHasChooseInfo[(iPacketKey, iQuality)] = 1
            
        lstRule = list(clsGoodData.m_InternalGoodRule)
        lstGoods = []
        for iPos, oChooseFunc in enumerate(lstRule):
            if iPos in dLockGoodInfo:
                dGoods = dLockGoodInfo[iPos]
            else:
                tResult = oChooseFunc(oGame, oHero, dHasChooseInfo)
                if not tResult:
                    SeasoneightLog.Alert('%s %s choose packet good fail %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iGoodSID, dHasChooseInfo, dLockGoodInfo))
                    return None
                (iPacketKey, iQuality) = tResult
                dHasChooseInfo[(iPacketKey, iQuality)] = 1
                dGoods = {
                    'item': clsGoodData.m_GoodsDataType,
                    'info': {
                        'SID': iPacketKey,
                        'QL': iQuality },
                    'PacketKey': iPacketKey,
                    'Pos': iPos }
            lstGoods.append(dGoods)
        
        return lstGoods

    
    def SetRefreshTime(self, oHero, iPos, iCount):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            self.m_RefreshTimes[iHero] = { }
        if iPos in self.m_RefreshTimes[iHero]:
            return None
        self.m_RefreshTimes[iHero][iPos] = {
            'MaxCount': iCount,
            'BaseCount': iCount }

    
    def SetGoods(self, oHero, iPos, oGoods, sKey, iRefresh = 0):
        iHero = oHero.m_ID
        dGoodsMenu = self.m_GoodsData.setdefault(iHero, { })
        if iPos in dGoodsMenu:
            if not iRefresh:
                SeasoneightLog.Alert('%s %s shop setrepeat %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, list(dGoodsMenu)))
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
                'ThirdPFPacket': { },
                'GemPacket': { } }
        (iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes) = self.GetRefreshTimes(oHero, oGoods.m_Pos)
        lstShowInfo = GetGoodsShowInfoByKey(sKey, self, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes)
        self.m_ShowInfo[iHero][sKey][oGoods.m_Pos] = lstShowInfo

    
    def UpdateRefreshTimes(self, oHero, iPos, iNum):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            return False
        if iPos not in self.m_RefreshTimes[iHero]:
            return False
        dPosInfo = self.m_RefreshTimes[iHero][iPos]
        iMaxCount = dPosInfo['MaxCount']
        iBaseCount = dPosInfo['BaseCount']
        iResult = iBaseCount + iNum
        if iResult < 0:
            iExtraCount = oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0)
            iFinalExtra = iResult + iExtraCount
            if iFinalExtra < 0:
                return False
            oHero.Set(S8GOODS_EXTRA_REFRESHTIMES_KEY, iFinalExtra)
            iResult = 0
        elif iResult > iMaxCount:
            return False
        dPosInfo['BaseCount'] = iResult
        return True

    
    def GetRefreshTimes(self, oHero, iPos):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            return (0, 0, 0)
        if iPos not in self.m_RefreshTimes[iHero]:
            return (0, 0, 0)
        dPosInfo = self.m_RefreshTimes[iHero][iPos]
        iBaseCount = dPosInfo['BaseCount']
        iExtraCount = oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0)
        return (iBaseCount, iExtraCount, dPosInfo['MaxCount'])

    
    def PlayerAbandonBuyGoods(self, oHero, iPos):
        iHero = oHero.m_ID
        if iHero not in self.m_GoodsData or iPos not in self.m_GoodsData[iHero]:
            SeasoneightLog.Alert('%s %s not hero in gooddata' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        oGoods = self.m_GoodsData[iHero][iPos]
        if not CheckGoodsSellOut(self, oHero, oGoods):
            lstAbandon = self.m_HeroAbandonBuy.setdefault(oHero.m_ID, [])
            if iPos not in lstAbandon:
                lstAbandon.append(iPos)
                iExtraRefreshTimes = oHero.Query(S8GOODS_EXTRA_REFRESHTIMES_KEY, 0)
                oHero.Set(S8GOODS_EXTRA_REFRESHTIMES_KEY, iExtraRefreshTimes + 1)
        self.RefreshHeroAllGoodsShow(oHero)



def CheckGoodsSellOut(oNpc, oHero, oGoods):
    if oGoods.m_HasBuy < oGoods.m_CanBuy:
        lstAbandomPos = oNpc.m_HeroAbandonBuy.get(oHero.m_ID, [])
        if oGoods.m_Pos not in lstAbandomPos:
            return 0
    return 1


def GetThirdPFPacketShowInfo(oNpc, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes):
    lstGoodsInfo = oGoods.m_Items
    if not lstGoodsInfo:
        return []
    lstInternalInfo = []
    for dGoodsInfo in lstGoodsInfo:
        lstInternalInfo.append([
            dGoodsInfo['info']['SID'],
            dGoodsInfo['info']['QL'],
            { }])
    
    iSellOut = CheckGoodsSellOut(oNpc, oHero, oGoods)
    return [
        oGoods.m_Pos,
        iSellOut,
        oGoods.GetCash(),
        iBaseRefreshTimes,
        iExtraRefreshTimes,
        iMaxRefreshTimes,
        lstInternalInfo]


def GetGemPacketShowInfo(oNpc, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes):
    lstGoodsInfo = oGoods.m_Items
    if not lstGoodsInfo:
        return []
    lstInternalInfo = []
    for dGoodsInfo in lstGoodsInfo:
        lstInternalInfo.append([
            dGoodsInfo['info']['SID'],
            dGoodsInfo['info']['QL']])
    
    iSellOut = CheckGoodsSellOut(oNpc, oHero, oGoods)
    return [
        oGoods.m_Pos,
        iSellOut,
        oGoods.GetCash(),
        iBaseRefreshTimes,
        iExtraRefreshTimes,
        iMaxRefreshTimes,
        lstInternalInfo]


def GetGoodsShowInfoByKey(sKey, oNpc, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes):
    if sKey not in GETGOODINFO_FUNC:
        return []
    return GETGOODINFO_FUNC[sKey](oNpc, oHero, oGoods, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes)

GETGOODINFO_FUNC = {
    'ThirdPFPacket': GetThirdPFPacketShowInfo,
    'GemPacket': GetGemPacketShowInfo }
