# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/reliclotterynpc.pyc
# RelativePath: clientlogic/cl_npc/reliclotterynpc.pyc
# Source Generated with Decompyle++
# File: reliclotterynpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, RELIC_SUBMSG_GENERATE_LOTTERY, PERFORMCHOOSE_TYPE_LOTTERYRD1, PERFORMCHOOSE_TYPE_LOTTERYRD2, SOURCE_REASON_MODE_RELICLOTTERT, INTERACT_STATUS_DONE, RELIC_TYPE_MYSTERY
from cl_cscommondef.cs_itemdef import QUALITY_TYPE_HIGH, QUALITY_TYPE_CURSE
from cl_cscommondef.cs_other import RELICBAG_TYPE_EXTEND
from cl_cscommondef.cs_fight import BLANKRELIC
from cl_object.logging import WarnpcLog
from cl_only import ChooseKey, ChooseMulKeys, Functor, SendAlert
from cl_platformdata import GetRelicQualityMap, GetRelicByType
from . import mobject
from . import net
import cl_formula
import cl_msgcenter
import cl_notify
import cl_perform
LOTTERY_REWARD_CORERELIC = 1
LOTTERY_REWARD_SUITRELIC = 2
LOTTERY_REWARD_RAMDONRELIC = 3
LOTTERY_RELICBACK_CHAT_BLACKRELIC = 9693
LOTTERY_RELICBACK_CHAT_NORMALRELIC = 9682
LOTTERY_REWARD_LIST = [
    LOTTERY_REWARD_CORERELIC,
    LOTTERY_REWARD_SUITRELIC,
    LOTTERY_REWARD_RAMDONRELIC]

def ValidRewardChooseSuitRelic(oNpc, oHero, iCostRelic):
    oElement = oNpc.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oElement:
        return 0
    dRelic = oElement.GetAllLackRelic(oHero)
    dRelic.pop(iCostRelic, 0)
    for iRelic in GetRelicByType(RELIC_TYPE_MYSTERY):
        dRelic.pop(iRelic, 0)
    
    dRelic = oHero.m_RelicCon.GetRelicAfterFilter(dRelic)
    if not dRelic:
        return 0
    return 1


def ValidRewardRamdonRelic(oNpc, oHero, iCostRelic):
    oRelicCon = oHero.m_RelicCon
    clsMiniGame = oNpc.m_Game.m_WarData.GetMiniGameData(oNpc.m_RewardMG)
    if clsMiniGame:
        dAvailableRelic = oRelicCon.GetRelicAfterFilter(clsMiniGame.m_ChooseWeight)
        dAvailableRelic.pop(iCostRelic, None)
        for iRelic in GetRelicByType(RELIC_TYPE_MYSTERY):
            dAvailableRelic.pop(iRelic, 0)
        
        dQualityWeight = clsMiniGame.m_ChooseQuality
        dQualityMap = GetRelicQualityMap()
        for iRelic in dAvailableRelic:
            if iRelic not in dQualityMap:
                continue
            iQuality = dQualityMap[iRelic]
            if iQuality not in dQualityWeight:
                continue
            return 1
        
    return 0

LOTTERY_VALID_FUNC = {
    LOTTERY_REWARD_RAMDONRELIC: ValidRewardRamdonRelic,
    LOTTERY_REWARD_SUITRELIC: ValidRewardChooseSuitRelic,
    LOTTERY_REWARD_CORERELIC: ValidRewardChooseSuitRelic }

def GetFinalRewardRelic(oHero, lstRelic):
    lstFinal = []
    for iSID in lstRelic:
        iRelic = iSID
        dMsgInfo = {
            'Relic': iRelic,
            'Level': 1 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_LOTTERY)
        iLevel = dMsgInfo['RelicDropLevel'] if 'RelicDropLevel' in dMsgInfo else 1
        if 'ReplaceRelicInfo' in dMsgInfo:
            iCanRepeat = dMsgInfo['RelicCanRepeat']
            for iReplaceRelic, iReplaceLevel in dMsgInfo['ReplaceRelicInfo']:
                if not iCanRepeat and iReplaceRelic in lstRelic:
                    continue
                iRelic = iReplaceRelic
                if 'RelicUseOldLevel' in dMsgInfo and not dMsgInfo['RelicUseOldLevel']:
                    iLevel = iReplaceLevel
            
        lstFinal.append((iRelic, iLevel))
    
    return lstFinal


def OnChooseRewardRelic(iNpc, oHero, idx, iAuto = 0):
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        WarnpcLog.Debug(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery nonpc {iNpc} {idx}''')
        return None
    (iReward, dInfo) = oNpc.GetProcessInfo(oHero.m_ID)
    if not dInfo or 'Option' not in dInfo:
        WarnpcLog.Alert(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery operr {iNpc} {idx} {dInfo}''')
        return None
    lstOption = dInfo['Option']
    if idx >= len(lstOption):
        WarnpcLog.Error(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery ans illegal {idx} {lstOption}''')
        return None
    (iRelic, iLevel) = lstOption[idx]
    WarnpcLog.Debug(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery rd{iReward} {iRelic} {iLevel} {iAuto}''')
    oHero.m_RelicCon.AddRelic(iRelic, oNpc.m_Flag, iLevel, {
        'SourceReason': SOURCE_REASON_MODE_RELICLOTTERT }, iSource = oHero.m_PlayerID)
    oNpc.DoneReward(oHero, iRelic, iLevel, iAuto)


def RewardSuitCoreRelic(oNpc, oHero, iCostRelic):
    oGame = oNpc.m_Game
    oElement = oGame.m_WarMgr.GetSeasonSuitElement()
    dLackRelic = oElement.GetCoreSuitLackRelic(oHero)
    dLackRelic.pop(iCostRelic, None)
    dLackRelic = oHero.m_RelicCon.GetRelicAfterFilter(dLackRelic)
    iCoreRelic = ChooseKey(oGame, dLackRelic)
    dRelic = oElement.GetAllLackRelic(oHero)
    for iRelic in GetRelicByType(RELIC_TYPE_MYSTERY):
        dRelic.pop(iRelic, 0)
    
    dRelic = oHero.m_RelicCon.GetRelicAfterFilter(dRelic)
    dRelic.pop(iCostRelic, 0)
    if iCoreRelic:
        dRelic.pop(iCoreRelic, 0)
        lstRelic = ChooseMulKeys(oGame, dRelic, 2)
        if lstRelic:
            lstRelic.insert(1, iCoreRelic)
        else:
            lstRelic = [
                iCoreRelic]
    else:
        lstRelic = ChooseMulKeys(oGame, dRelic, 3)
    lstRelic = GetFinalRewardRelic(oHero, lstRelic)
    oNpc.SetProcessInfo(oHero.m_ID, 'Option', lstRelic)
    WarnpcLog.Debug(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery rd1 op {lstRelic}''')
    net.GS2CChoosePerform(oHero, lstRelic, PERFORMCHOOSE_TYPE_LOTTERYRD1)
    net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(OnChooseRewardRelic, oNpc.m_ID))
    LotteryRelicBack(oNpc, oHero)


def RewardChooseSuitRelic(oNpc, oHero, iCostRelic):
    oGame = oNpc.m_Game
    oElement = oGame.m_WarMgr.GetSeasonSuitElement()
    dRelic = oElement.GetAllLackRelic(oHero)
    dRelic.pop(iCostRelic, 0)
    dRelic = oHero.m_RelicCon.GetChooseRelicWeight(dRelic)
    for iRelic in GetRelicByType(RELIC_TYPE_MYSTERY):
        dRelic.pop(iRelic, 0)
    
    lstRelic = ChooseMulKeys(oGame, dRelic, 2)
    lstRelic = GetFinalRewardRelic(oHero, lstRelic)
    oNpc.SetProcessInfo(oHero.m_ID, 'Option', lstRelic)
    WarnpcLog.Debug(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery rd2 op {lstRelic}''')
    net.GS2CChoosePerform(oHero, lstRelic, PERFORMCHOOSE_TYPE_LOTTERYRD2)
    net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(OnChooseRewardRelic, oNpc.m_ID))
    LotteryRelicBack(oNpc, oHero)


def LotteryRelicBack(oNpc, oHero):
    dRelicBackProbFactor = oHero.Query('LotteryRelicBackFactor', { })
    if not dRelicBackProbFactor:
        return None
    iRelicBackProb = sum(dRelicBackProbFactor.values())
    if iRelicBackProb < 100:
        iOriginPerform = ChooseKey(oHero.m_Game, dRelicBackProbFactor, iTotal = 100)
    else:
        iOriginPerform = ChooseKey(oHero.m_Game, dRelicBackProbFactor)
    if iOriginPerform:
        (_, dInfo) = oNpc.GetProcessInfo(oHero.m_ID)
        iCostRelic = dInfo['CostRelic']
        iRelicLevel = dInfo['RelicLevel']
        iIsExtendRelic = dInfo['IsExtendRelic']
        if iIsExtendRelic:
            oHero.m_RelicCon.AddExtendRelic(iCostRelic, 'RefundLotteryCost', iRelicLevel, iSource = oHero.m_PlayerID)
        else:
            oHero.m_RelicCon.AddRelic(iCostRelic, 'RefundLotteryCost', iRelicLevel, iSource = oHero.m_PlayerID)
        oPerform = oHero.GetPerform(iOriginPerform)
        if not oPerform:
            return None
        dReplaceInfo = {
            '$name': oPerform.m_Name }
        iChat = LOTTERY_RELICBACK_CHAT_BLACKRELIC
        if iCostRelic != BLANKRELIC:
            iChat = LOTTERY_RELICBACK_CHAT_NORMALRELIC
            clsRelic = cl_perform.GetPerformModule(iCostRelic)
            dReplaceInfo['$relic'] = clsRelic.m_Name
        cl_notify.SendCommonNotify(oHero.m_Game, {
            oHero.m_PlayerID}, iChat, dReplaceInfo)


def RewardRamdonRelic(oNpc, oHero, iCostRelic):
    oGame = oNpc.m_Game
    oRelicCon = oHero.m_RelicCon
    clsMiniGame = oGame.m_WarData.GetMiniGameData(oNpc.m_RewardMG)
    dRelic = { }
    if clsMiniGame:
        dAvailableRelic = oRelicCon.GetRelicAfterFilter(clsMiniGame.m_ChooseWeight)
        dAvailableRelic.pop(iCostRelic, None)
        for iRelic in GetRelicByType(RELIC_TYPE_MYSTERY):
            dAvailableRelic.pop(iRelic, 0)
        
        dQualityWeight = clsMiniGame.m_ChooseQuality
        dQualityMap = GetRelicQualityMap()
        for iRelic in dAvailableRelic:
            if iRelic not in dQualityMap:
                continue
            iQuality = dQualityMap[iRelic]
            if iQuality not in dQualityWeight:
                continue
            dRelic[iRelic] = dQualityWeight[iQuality]
        
    iRelic = ChooseKey(oGame, dRelic)
    (iRelic, iLevel) = GetFinalRewardRelic(oHero, [
        iRelic])[0]
    WarnpcLog.Debug(f'''{oGame.m_ID} {oHero.m_PlayerID} lottery rd3 {iRelic} {iLevel}''')
    LotteryRelicBack(oNpc, oHero)
    oRelicCon.AddRelic(iRelic, oNpc.m_Flag, iLevel, {
        'SourceReason': SOURCE_REASON_MODE_RELICLOTTERT }, iSource = oHero.m_PlayerID)
    oNpc.DoneReward(oHero, iRelic, iLevel)

LOTTERY_REWARD_FUNC = {
    LOTTERY_REWARD_RAMDONRELIC: RewardRamdonRelic,
    LOTTERY_REWARD_SUITRELIC: RewardChooseSuitRelic,
    LOTTERY_REWARD_CORERELIC: RewardSuitCoreRelic }

def ProcessChooseSuitRelic(iType, oNpc, oHero):
    (_, dInfo) = oNpc.GetProcessInfo(oHero.m_ID)
    if not dInfo or 'Option' not in dInfo:
        WarnpcLog.Alert(f'''{oNpc.m_Game.m_ID} {oHero.m_PlayerID} lottery operr {oNpc.m_ID} {dInfo}''')
        return None
    lstOption = dInfo['Option']
    oNpc.RefreshRecord(oHero)
    net.GS2CChoosePerform(oHero, lstOption, iType)
    net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(OnChooseRewardRelic, oNpc.m_ID))

LOTTERY_PROCESS_FUNC = {
    LOTTERY_REWARD_SUITRELIC: Functor(ProcessChooseSuitRelic, PERFORMCHOOSE_TYPE_LOTTERYRD2),
    LOTTERY_REWARD_CORERELIC: Functor(ProcessChooseSuitRelic, PERFORMCHOOSE_TYPE_LOTTERYRD1) }

def AutoRewardCoreRelic(oNpc, oHero):
    (_, dInfo) = oNpc.GetProcessInfo(oHero.m_ID)
    if not dInfo or 'Option' not in dInfo:
        WarnpcLog.Alert(f'''{oNpc.m_Game.m_ID} {oHero.m_PlayerID} lottery operr {oNpc.m_ID} {dInfo}''')
        return None
    lstOption = dInfo['Option']
    idx = 1 if len(lstOption) > 1 else 0
    OnChooseRewardRelic(oNpc.m_ID, oHero, idx, iAuto = 1)


def AutoRewardSuitRelic(oNpc, oHero):
    (_, dInfo) = oNpc.GetProcessInfo(oHero.m_ID)
    if not dInfo or 'Option' not in dInfo:
        WarnpcLog.Alert(f'''{oNpc.m_Game.m_ID} {oHero.m_PlayerID} lottery operr {oNpc.m_ID} {dInfo}''')
        return None
    lstOption = dInfo['Option']
    idx = oNpc.m_Game.Random(len(lstOption))
    OnChooseRewardRelic(oNpc.m_ID, oHero, idx, iAuto = 1)

LOTTERY_LEVEL_FINISH_FUNC = {
    LOTTERY_REWARD_SUITRELIC: AutoRewardSuitRelic,
    LOTTERY_REWARD_CORERELIC: AutoRewardCoreRelic }

class CRelicLotteryNpc(mobject.CNPC):
    
    def __init__(self, *args):
        super(CRelicLotteryNpc, self).__init__(*args)
        self.m_Record = { }
        self.m_ExtraLotteryCnt = { }
        self.m_Process = { }
        self.m_Weight = { }
        self.m_CloseProb = 0
        self.m_NextCloseProb = { }
        self.m_RewardMG = 0
        self.m_CloseToHero = { }
        self.m_Flag = 'RelicLottery-%s' % self.m_ID
        self.InitLinsten()

    
    def Release(self):
        self.DoneLinsten()
        super(CRelicLotteryNpc, self).Release()

    
    def InitLinsten(self):
        cl_msgcenter.AddAttentionFunc(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, self.m_Flag)

    
    def DoneLinsten(self):
        cl_msgcenter.DoneAttention(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)

    
    def SetInitData(self, dWeight, iCloseProb, iMiniGame):
        self.m_Weight = dWeight
        self.m_CloseProb = iCloseProb
        self.m_RewardMG = iMiniGame

    
    def ValidInteract(self, oHero):
        oElement = self.m_Game.m_WarMgr.GetSeasonSuitElement()
        if not oElement:
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, '赛季套装玩法未激活，请检查战场难度')
            return 0
        return super().ValidInteract(oHero)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_Record:
            self.m_Record[iHero] = []
            self.m_ExtraLotteryCnt[iHero] = 0
            self.RefreshNextCloseProb(oHero)
        (iProcess, _) = self.m_Process.get(iHero, (0, { }))
        if iProcess in LOTTERY_PROCESS_FUNC:
            LOTTERY_PROCESS_FUNC[iProcess](self, oHero)
            return None
        self.RefreshRecord(oHero)

    
    def OnInteract(self, oHero):
        pass

    
    def RefreshRecord(self, oHero):
        iHero = oHero.m_ID
        iReInteractProb = min(100 - self.m_NextCloseProb.get(iHero, 0), 100)
        net.GS2CRelicLotteryNpcData(oHero, self.m_Record.get(iHero, []), iReInteractProb)
        if not self.m_Process.get(iHero, None):
            net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnChooseCostRelic, self)

    
    def OnChooseCostRelic(self, oHero, iMixRelic):
        if self.m_PlayerInteractStatus[oHero.m_PlayerID] == INTERACT_STATUS_DONE:
            WarnpcLog.Error(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} lottery done ans {iMixRelic}''')
            return None
        oRelicCon = oHero.m_RelicCon
        iCostRelic = oRelicCon.GetRelicSIDByMixSID(iMixRelic)
        if not oRelicCon.CheckHasRelic(iCostRelic):
            WarnpcLog.Error(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} lottery {iMixRelic} {iCostRelic} ans err''')
            return None
        iHero = oHero.m_ID
        iQuality = oRelicCon.GetRelicQuality(iMixRelic)
        dMsgInfo = {
            'Quality': iQuality }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREREWARD_RELICLOTTERY, oHero, dMsgInfo)
        iQuality = dMsgInfo['Quality']
        if iQuality == QUALITY_TYPE_CURSE:
            WarnpcLog.Error(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} lottery costcurse{iMixRelic} {iCostRelic}''')
            return None
        iSuper = oRelicCon.IsSuperRelic(iMixRelic)
        if iSuper:
            if iQuality == QUALITY_TYPE_HIGH:
                iQuality = -1
            else:
                iQuality = iQuality << 1
        iPreReward = self.PreGetReward(oHero, iCostRelic, iQuality)
        if iPreReward not in LOTTERY_REWARD_LIST:
            WarnpcLog.Alert(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} lottery {iMixRelic} {iCostRelic} {iSuper} rd err {iPreReward}''')
            return None
        WarnpcLog.Debug(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} lottery {iMixRelic} {iCostRelic} {iSuper} rd {iPreReward}''')
        iRelicLevel = oRelicCon.GetRelicLevelByMixSID(iMixRelic)
        iIsExtendRelic = 1 if iMixRelic & RELICBAG_TYPE_EXTEND else 0
        self.m_Process[iHero] = (iPreReward, {
            'CostRelic': iCostRelic,
            'RelicLevel': iRelicLevel,
            'IsExtendRelic': iIsExtendRelic })
        oRelicCon.RemoveRelicByMixSID(iMixRelic, self.m_Flag, iForce = 1)
        self.TrueReward(oHero, iPreReward, iCostRelic)

    
    def SetProcessInfo(self, iHero, key, value):
        dInfo = self.m_Process[iHero][1]
        dInfo[key] = value

    
    def GetProcessInfo(self, iHero):
        if iHero not in self.m_Process:
            return (0, { })
        return self.m_Process[iHero]

    
    def PreGetReward(self, oHero, iCostRelic, iQuality):
        iPreReward = 0
        dReward = { }
        if iQuality not in self.m_Weight:
            SendAlert('err', f'''{self.m_Game.m_ID} 抽奖NPC未配置品质 {iQuality} 的奖励权重''')
            return 0
        dWeight = self.m_Weight[iQuality]
        for iReward in LOTTERY_REWARD_LIST:
            if iReward not in LOTTERY_VALID_FUNC or not LOTTERY_VALID_FUNC[iReward](self, oHero, iCostRelic):
                continue
            if iReward not in dWeight:
                SendAlert('err', f'''{self.m_Game.m_ID} 抽奖NPC未配置品质 {iQuality} 的 {iReward} 等奖权重''')
                continue
            dReward[iReward] = dWeight[iReward]
        
        iPreReward = ChooseKey(self.m_Game, dReward)
        return iPreReward

    
    def TrueReward(self, oHero, iPreReward, iCostRelic):
        LOTTERY_REWARD_FUNC[iPreReward](self, oHero, iCostRelic)

    
    def DoneReward(self, oHero, iRelic, iLevel, iAuto = 0):
        iHero = oHero.m_ID
        (iReward, dInfo) = self.m_Process.pop(iHero)
        self.m_Record[iHero].append((iReward, iRelic, iLevel))
        if self.CheckClose(oHero):
            self.m_CloseToHero[iHero] = 1
            self.SetHeroInteractStatus(oHero.m_PlayerID)
        dMsgInfo = {
            'Npc': self.m_ID,
            'PreReward': iReward,
            'Relic': iRelic,
            'CostRelic': dInfo['CostRelic'],
            'HeroRecord': self.m_Record[iHero],
            'IsClose': self.m_CloseToHero[iHero] if iHero in self.m_CloseToHero else 0,
            'LotteryCnt': len(self.m_Record[iHero]) }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DONEREWARD_RELICLOTTERY, oHero, dMsgInfo)
        self.RefreshNextCloseProb(oHero)
        if not iAuto:
            self.RefreshRecord(oHero)

    
    def CheckClose(self, oHero):
        iProb = self.m_NextCloseProb.get(oHero.m_ID, 0)
        return self.m_Game.Random(100) < iProb

    
    def RefreshNextCloseProb(self, oHero):
        iHero = oHero.m_ID
        dData = {
            'LotteryCnt': len(self.m_Record[iHero]) + 1,
            'ExtraLotteryCnt': self.m_ExtraLotteryCnt[iHero] }
        self.m_NextCloseProb[iHero] = cl_formula.GetResultByData(oHero, self.m_CloseProb, dData)

    
    def OnLevelFinish(self, _oListener, _oWarMgr, _dMsgInfo):
        oGame = self.m_Game
        for iHero, dReward in dict(self.m_Process).items():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            (iProcess, _) = dReward
            if iProcess in LOTTERY_LEVEL_FINISH_FUNC:
                LOTTERY_LEVEL_FINISH_FUNC[iProcess](self, oHero)
        

    
    def ModifyExtraLotteryCnt(self, oHero, iCnt):
        iHeroID = oHero.m_ID
        if iHeroID not in self.m_ExtraLotteryCnt:
            self.m_ExtraLotteryCnt[iHeroID] = iCnt
        else:
            self.m_ExtraLotteryCnt[iHeroID] += iCnt


