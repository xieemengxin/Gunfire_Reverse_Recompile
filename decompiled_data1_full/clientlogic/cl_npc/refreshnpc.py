# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/refreshnpc.pyc
# RelativePath: clientlogic/cl_npc/refreshnpc.pyc
# Source Generated with Decompyle++
# File: refreshnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, NWARRIOR_DROP_RELIC, INTERACT_STATUS_DONE, VIRTUAL_ITEM_DROP, VIRTUAL_ITEM_RELIC, INTERACT_TYPE_ALLOW, DROP_REASON_NPCREWARD, NPC_REFRESH_COST_WARCASH, NPC_REFRESH_COST_GSCASH, RELIC_SUBMSG_GENERATE_DROP
from cl_only import Functor, Time2Frame
import cl_minigame
import cl_notify
import cl_formula
import cl_msgcenter
from . import magicbox
from . import net
from . import eventnpcaction
from .mobject import SendNpcRefreshMsg, SendNpcChooseMsg

class CRefreshNPC(magicbox.CBoxNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.SetInitInteract(INTERACT_TYPE_ALLOW)
        self.m_ChooseGame = 0
        self.m_InitRefreshCost = 0
        self.m_RefreshCost = 0
        self.m_Reward = { }
        self.m_ExtraReward = { }
        self.m_HeroRefreshInfo = { }
        self.m_CostType = NPC_REFRESH_COST_WARCASH

    
    def SetChooseGame(self, iMiniGame):
        self.m_ChooseGame = iMiniGame

    
    def SetInitRefreshCost(self, func, iCostType):
        self.m_InitRefreshCost = func
        self.m_CostType = iCostType
        self.Delete('InitRandCache')

    
    def SetRefreshCost(self, func):
        self.m_RefreshCost = func

    
    def RefreshOption(self, oHero):
        iRewardSID = 0
        iRewardType = 0
        iLevel = 1
        lstReward = []
        if oHero.m_ID in self.m_Reward:
            lstReward = self.m_Reward[oHero.m_ID].Query('Reward', [])
        if lstReward:
            dReward = lstReward[0]
            iRewardType = dReward['item']
            dInfo = dReward['info']
            if iRewardType == VIRTUAL_ITEM_RELIC:
                iRewardSID = dInfo['sid']
                dInfo['level'] = self.GetArgValue('RelicLevel', 1)
            elif iRewardType == VIRTUAL_ITEM_DROP:
                lstDropData = dInfo['DropInfo']
                if dInfo['DropType'] == NWARRIOR_DROP_RELIC and lstDropData:
                    iRewardType = VIRTUAL_ITEM_RELIC
                    iRewardSID = lstDropData[0]
                    dMsgInfo = {
                        'Relic': iRewardSID,
                        'NPC': self.m_ID,
                        'Level': iLevel }
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_DROP)
                    if 'DropLevel' in dInfo:
                        iLevel = dInfo['DropLevel']
                    else:
                        iFlag = 0
                        if 'RelicDropLevel' in dMsgInfo:
                            iLevel = dMsgInfo['RelicDropLevel']
                            iFlag += 1
                        if 'ReplaceRelicInfo' in dMsgInfo and dMsgInfo['ReplaceRelicInfo']:
                            if 'RelicUseOldLevel' in dMsgInfo and not dMsgInfo['RelicUseOldLevel']:
                                (lstDropData[0], iLevel) = dMsgInfo['ReplaceRelicInfo'][0]
                                iFlag += 1
                            else:
                                (lstDropData[0], _) = dMsgInfo['ReplaceRelicInfo'][0]
                            iRewardSID = lstDropData[0]
                        if not iFlag:
                            iLevel = self.GetArgValue('RelicLevel', 1)
                        dInfo['DropLevel'] = iLevel
            dInfo['ShowedBeforDrop'] = 1
        (iCost, iCostType) = self.GetCost(oHero.m_ID)
        iRefreshCnt = self.GetArgValue('RefreshCnt', 0)
        if iRefreshCnt:
            iLimit = 1
            iHero = oHero.m_ID
            dTimes = self.Query('HeroRefreshTimes', { })
            iTimes = dTimes[iHero] if iHero in dTimes else 0
            iCount = iRefreshCnt - iTimes
        else:
            iLimit = 0
            iCount = 0
        net.GS2CRefreshNPC(oHero, iRewardType, iRewardSID, iCost, iLevel, iCostType, iLimit, iCount)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(OptionInteract, self.m_ID, iRewardSID), self)
        if oHero.m_ID in self.m_Reward:
            lstAllOption = []
            if self.ValidRefresh(oHero):
                lstAllOption.append([
                    -1,
                    1])
            if iRewardSID:
                lstAllOption.append([
                    0,
                    1])
            SendNpcRefreshMsg(oHero, self, 1, lstAllOption)

    
    def NewMiniGame(self, oHero):
        iChooseCnt = 1 if oHero.m_ID in self.m_ExtraReward else 0
        vPos = eventnpcaction.CalOffsetCoodinates2(self, iChooseCnt)
        return cl_minigame.NewMiniGame(self.m_Game, self.m_ChooseGame, self.m_ID, oHero.m_ID, {
            'AutoRefresh': 0,
            'AutoReward': 1,
            'Scene': self.m_Scene,
            'DropReason': DROP_REASON_NPCREWARD,
            'DropPos': vPos })

    
    def OnInteract(self, oHero):
        if self.GetHeroInteractStatus(oHero.m_PlayerID) != INTERACT_STATUS_DONE:
            oMiniGame = self.NewMiniGame(oHero)
            if not oMiniGame:
                cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, '失效的MG-%d' % self.m_ChooseGame)
                return None
            self.m_Reward[oHero.m_ID] = oMiniGame
        self.RefreshOption(oHero)

    
    def GetCost(self, iHero):
        iCostType = self.m_CostType
        if iHero not in self.m_Reward:
            return (-1, iCostType)
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes[iHero] if iHero in dTimes else 0
        dInfo = {
            cl_formula.FML_ARG_VID: iHero }
        if self.m_FormulaLimit:
            dInfo.update(self.m_FormulaLimit)
        (iNowTimes, iCost) = self.m_HeroRefreshInfo[iHero] if iHero in self.m_HeroRefreshInfo else (-1, 0)
        if iNowTimes != iTimes:
            if iTimes < 1:
                fRandCache = self.Query('InitRandCache', None)
                if fRandCache is not None:
                    dInfo['RandCache'] = fRandCache
                iCost = cl_formula.GetFormulaResult(self, self.m_InitRefreshCost, dInfo)
                if 'RandCache' in dInfo:
                    self.Set('InitRandCache', dInfo['RandCache'])
                else:
                    iCost = cl_formula.GetFormulaResult(self, self.m_RefreshCost, dInfo)
            self.m_HeroRefreshInfo[iHero] = (None, iCost)
        return (iCost, iCostType)

    
    def GetReward(self, oHero, iReward):
        if oHero.m_ID not in self.m_Reward:
            return None
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        if iTimes < 1:
            return None
        self.BoxModelOpen(oHero.m_PlayerID)
        oMiniGame = self.m_Reward.pop(oHero.m_ID)
        iExtra = oHero.Query('NpcInteractExtraChoose', 0)
        if iExtra and oHero.m_ID not in self.m_ExtraReward:
            self.m_ExtraReward[oHero.m_ID] = 1
            self.m_Reward[oHero.m_ID] = self.NewMiniGame(oHero)
            dTimes.pop(oHero.m_ID)
        iDelayTime = self.GetArgValue('RewardDelay')
        if not iDelayTime:
            self.GetReward2(oMiniGame)
        else:
            self.Call_Out(Functor(self.GetReward2, oMiniGame), Time2Frame(iDelayTime), 'DelayReward')
        SendNpcChooseMsg(oHero, self, 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROP_RELIC_REWARD, oHero, {
            'Relic': iReward })

    
    def GetReward2(self, oMiniGame):
        oMiniGame.Start()

    
    def ValidRefresh(self, oHero):
        iRefreshCnt = self.GetArgValue('RefreshCnt', 0)
        if iRefreshCnt:
            iHero = oHero.m_ID
            dTimes = self.Query('HeroRefreshTimes', { })
            iTimes = dTimes[iHero] if iHero in dTimes else 0
            if iTimes >= iRefreshCnt:
                return False
        (iCost, iCostType) = self.GetCost(oHero.m_ID)
        if iCostType == NPC_REFRESH_COST_WARCASH or oHero.m_WarCash < iCost:
            return False
        if iCostType == NPC_REFRESH_COST_GSCASH and oHero.m_WarGSCash < iCost:
            return False
        return True

    
    def RefreshReward(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_Reward:
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, '奖励已获取')
            return 0
        (iCost, iCostType) = self.GetCost(iHero)
        if not self.ValidRefresh(oHero):
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, '铜币或精魄或刷新次数不够')
            return 0
        sActionKey = self.ActionKey()
        if iCostType == NPC_REFRESH_COST_WARCASH:
            oHero.AddCash(-iCost, sActionKey)
        elif iCostType == NPC_REFRESH_COST_GSCASH:
            oHero.ConsumeGSCash(iCost, sActionKey)
        oMiniGame = self.m_Reward[iHero]
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(iHero, 0)
        dTimes[iHero] = iTimes + 1
        self.Set('HeroRefreshTimes', dTimes)
        oMiniGame.RefreshReward()
        self.RefreshOption(oHero)
        SendNpcChooseMsg(oHero, self, -1)

    
    def ActionKey(self):
        return 'Npc-%d-refresh-event-0' % self.m_SID

    
    def OptionInteract(self, oHero, iOption, iReward):
        if iOption == 1:
            self.GetReward(oHero, iReward)
        elif iOption == 2:
            self.RefreshReward(oHero)



def OptionInteract(iNpc, iReward, oHero, iOption):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.OptionInteract(oHero, iOption, iReward)

