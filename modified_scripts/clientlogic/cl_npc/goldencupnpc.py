# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/goldencupnpc.pyc
# RelativePath: clientlogic/cl_npc/goldencupnpc.pyc
# Source Generated with Decompyle++
# File: goldencupnpc.pyc (Python 3.6)

# 每个金爵默认一次刷新机会

from cl_commondefines import INTERACT_TYPE_FORBID, INTERACT_RULE_MULCHOOSE, PF_TYPE_TALENT
import cl_notify
import cl_minigame
import cl_msgcenter
import cl_formula
import cl_scene
import cl_test as cl_customconfig
from . import mobject
from . import net
from cl_object.logging import WarnpcLog
MIN_GOLDENCUP_REFRESH_TIMES = 1

class CGoldenCupNpc(mobject.CNPC):
    m_CheckInteractDistance = False
    m_EnableChooseAll = True
    
    def __init__(self, *args):
        super(CGoldenCupNpc, self).__init__(*args)
        self.m_Discoverd = False
        self.m_InteractDis = 999
        self.m_ExRefresh = { }
        self.m_RefreshCost = { }
        self.m_MaxRefreshTimes = { }
        self.m_IsExtraInteractRule = 0
        self.m_TalentReward = { }
        self.m_AutoRecycle = 1
        self.m_DropSource = -1

    
    def SetTimes(self, iTimes):
        self.AddExtraInteractRule(INTERACT_RULE_MULCHOOSE, {
            'Times': iTimes,
            'PFType': PF_TYPE_TALENT })
        self.m_IsExtraInteractRule = 1

    
    def IsAutoRecycle(self):
        return self.m_AutoRecycle

    
    def SetAutoRecycle(self, iAutoRecycle):
        self.m_AutoRecycle = iAutoRecycle

    
    def Abandoner(self):
        return self.Query('Abandoner', 0)

    
    def InitCustomAttr(self, clsData, dAddData):
        super().InitCustomAttr(clsData, dAddData)
        self.m_DropSource = dAddData.get('DropSource', -1)
        self.SendMsgToPlayer(cl_msgcenter.MSG_WAR_CREATEGOLDENCUP, { }, iCalAI = 1)

    
    def OnFirstInteract(self, oHero):
        self.m_Discoverd = True
        oGame = self.m_Game
        lstPlayer = [ iPlayer for iPlayer in oGame.GetRealPlayers() if self.IsVisibleTo(iPlayer) ]
        if len(lstPlayer) > 1:
            cl_notify.SendCommonNotify(oGame, lstPlayer, 2209, {
                '$$name': oHero.m_OwnerName })

    
    def OnInteract(self, oHero):
        if not self.m_Discoverd:
            self.OnFirstInteract(oHero)

    
    def PlayerChose(self, oHero):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE_END, oHero, {
            'NpcID': self.m_ID })
        self.ClearCommonShowTalent(oHero)
        if not self.m_ExtraInteractRule:
            self.ClearInteraction(oHero)
        elif self.GetPlayerInteractType(oHero.m_PlayerID) == INTERACT_TYPE_FORBID or self.CheckAllPlayerChose():
            self.Remove('AllChooseRemove')
        else:
            oTalentCon = oHero.m_TalentCon
            if oTalentCon.CheckHasAllTalent():
                self.Recycle(oHero.m_PlayerID)

    
    def ClearInteraction(self, oHero):
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
            oHero.m_PlayerID])
        if self.CheckAllPlayerChose():
            self.Remove('AllChooseRemove')

    
    def Release(self):
        self.DealTalentDate()
        super().Release()

    
    def DealTalentDate(self):
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.ClearCommonShowTalent(oHero)
        

    
    def CheckAllPlayerChose(self):
        lstTarget = self.m_Game.m_WarMgr.GetAllPlayer()
        for iTarget in lstTarget:
            if self.GetPlayerInteractType(iTarget) & INTERACT_TYPE_FORBID != INTERACT_TYPE_FORBID:
                return False
        
        return True

    
    def Refresh(self, oHero):
        if oHero.m_ID not in self.m_ExRefresh:
            self.GetRefreshInfo(oHero)
        if oHero.m_ID not in self.m_ExRefresh or not self.m_ExRefresh[oHero.m_ID]:
            return None
        if self.m_ReleaseFlag:
            return None
        iCost = self.GetRefreshCost(oHero)
        if iCost and iCost > oHero.m_WarCash:
            return None
        self.CostRefreshTimes(oHero)
        if iCost:
            oHero.AddCash(-iCost, 'GoldencupRefreshCost')
        net.GS2CNpcRefreshInfo(self, oHero)
        oMiniGame = self.m_Game.m_MiniGameMgr.GetPlayerMiniGameByOwner(self.m_ID, oHero.m_ID)
        dOldRewardInfo = { }
        if oMiniGame:
            dOldRewardInfo = oMiniGame.Query('Reward', { })
            oMiniGame.End()
        dExtInfo = self.Query('dExtInfo')
        dExtInfo['OldReward'] = dOldRewardInfo
        self.ResetTalentReward(oHero.m_PlayerID)
        self.ClearCommonShowTalent(oHero)
        oNewMiniGame = cl_minigame.NewMiniGame(self.m_Game, self.Query('iMiniGame'), self.m_ID, oHero.m_ID, dExtInfo)
        if oNewMiniGame:
            oNewMiniGame.Start()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REFRESHGOLDENCUP, oHero, { })

    
    def ClearCommonShowTalent(self, oHero):
        dCommonShowTalent = oHero.SetDefault('CommonShowTalent', { })
        if self.m_ID in dCommonShowTalent:
            dCommonShowTalent.pop(self.m_ID)

    
    def GetRefreshInfo(self, oHero):
        iMaxPerRefreshTimes = oHero.Query('TalentChooseRefresh', 0)
        iMaxTempRefreshTimes = oHero.QuerySavedData('TalentChooseRefreshTemp', 0)
        iCurMaxRefreshTimes = max(MIN_GOLDENCUP_REFRESH_TIMES, iMaxPerRefreshTimes + iMaxTempRefreshTimes)
        if oHero.m_ID not in self.m_MaxRefreshTimes:
            self.m_MaxRefreshTimes[oHero.m_ID] = iCurMaxRefreshTimes
            self.m_ExRefresh[oHero.m_ID] = iCurMaxRefreshTimes
        else:
            iMaxRefreshTimes = self.m_MaxRefreshTimes[oHero.m_ID]
            if iMaxRefreshTimes != iCurMaxRefreshTimes:
                if self.m_ExRefresh[oHero.m_ID] <= iMaxRefreshTimes - iMaxPerRefreshTimes:
                    self.m_ExRefresh[oHero.m_ID] = iMaxTempRefreshTimes
                else:
                    self.m_ExRefresh[oHero.m_ID] = iCurMaxRefreshTimes
                self.m_MaxRefreshTimes[oHero.m_ID] = iCurMaxRefreshTimes
        return (iCurMaxRefreshTimes, self.m_ExRefresh[oHero.m_ID])

    
    def GetChooseAllInfo(self, oHero):
        if not self.m_EnableChooseAll:
            return (0, 0)
        iMaxChooseAllTimes = oHero.Query('TalentChooseAll', 0)
        iUseChooseAllTimes = oHero.QuerySavedData('save.UseTalentChooseAll', 0)
        if iMaxChooseAllTimes > iUseChooseAllTimes:
            iCanUseChooseAllTimes = iMaxChooseAllTimes - iUseChooseAllTimes
        else:
            iCanUseChooseAllTimes = 0
        return (iMaxChooseAllTimes, iCanUseChooseAllTimes)

    
    def UseChooseAllTimes(self, oHero):
        if not self.m_EnableChooseAll:
            return None
        iUseTalentChooseAllTimes = oHero.QuerySavedData('save.UseTalentChooseAll')
        oHero.SetSavedData('save.UseTalentChooseAll', iUseTalentChooseAllTimes + 1)
        net.GS2CNpcRefreshInfo(self, oHero)

    
    def CostRefreshTimes(self, oHero):
        iExRefresh = self.m_ExRefresh[oHero.m_ID]
        self.m_ExRefresh[oHero.m_ID] -= 1
        iRefreshTempTimes = oHero.QuerySavedData('TalentChooseRefreshTemp', 0)
        if iExRefresh == iRefreshTempTimes:
            oHero.SetSavedData('TalentChooseRefreshTemp', self.m_ExRefresh[oHero.m_ID])

    
    def SetRefreshCost(self, iCost, iHero):
        self.m_RefreshCost[iHero] = iCost

    
    def SetMaxRefreshTimes(self, iTimes, iHero):
        self.m_MaxRefreshTimes[iHero] = max(MIN_GOLDENCUP_REFRESH_TIMES, iTimes)

    
    def GetMaxRefreshTimes(self, oHero):
        if oHero.m_ID in self.m_MaxRefreshTimes:
            return self.m_MaxRefreshTimes[oHero.m_ID]
        return 0

    
    def GetRefreshCost(self, oHero):
        if oHero.m_ID in self.m_RefreshCost:
            return self.m_RefreshCost[oHero.m_ID]
        return oHero.Query('GoldNpcRefreshCost', 0)

    
    def Save(self):
        dRefreshTime = { }
        for iHero, iRefreshTimes in self.m_ExRefresh.items():
            oHero = self.m_Game.GetObject(iHero)
            dRefreshTime[oHero.m_PlayerID] = iRefreshTimes
        
        dInfo = {
            'SID': self.m_SID,
            'TalentReward': self.m_TalentReward,
            'RefreshTime': dRefreshTime }
        return dInfo

    
    def Load(self, dInfo):
        self.m_TalentReward = dInfo['TalentReward']
        dRefreshTime = dInfo['RefreshTime']
        for pid, iRefreshTime in dRefreshTime.items():
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
            if oHero:
                self.m_ExRefresh[oHero.m_ID] = iRefreshTime
        

    
    def SetTalentReward(self, pid, dReward):
        self.m_TalentReward[pid] = dReward

    
    def ResetTalentReward(self, pid):
        self.m_TalentReward.pop(pid, None)

    
    def GetTalentReward(self, pid):
        if pid not in self.m_TalentReward:
            return { }
        return self.m_TalentReward[pid]

    
    def GetHeroInteractTimes(self, oHero):
        pid = oHero.m_PlayerID
        if not self.IsVisibleTo(pid) or self.GetPlayerInteractType(pid) == INTERACT_TYPE_FORBID:
            return 0
        oRule = self.GetExtraInteractRule(INTERACT_RULE_MULCHOOSE)
        if oRule:
            return oRule.GetHeroInteractTimes(oHero.m_ID)
        return 1

    
    def GetCreateSource(self):
        return self.m_DropSource

    
    def Recycle(self, pid):
        oGame = self.m_Game
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        if not self.ValidRecycle(oHero):
            return None
        WarnpcLog.Info('%s %s recyclegoldencup %s' % (oGame.m_ID, pid, self.m_SID))
        iTimes = self.GetHeroInteractTimes(oHero)
        self.SetInVisiblePlayer(pid)
        cl_scene.GS2CMapDel(self, {
            pid: 1 })
        oMiniGame = self.m_Game.m_MiniGameMgr.GetPlayerMiniGameByOwner(self.m_ID, oHero.m_ID)
        if oMiniGame:
            oMiniGame.RemoveReward()
            oMiniGame.End()
        self.ClearCommonShowTalent(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, oHero, {
            'InteractTimes': iTimes,
            'NpcID': self.m_ID })
        self.ClearInteraction(oHero)

    
    def ValidRecycle(self, oHero):
        oGame = self.m_Game
        oTalentCon = oHero.m_TalentCon
        if not oGame.m_WarMgr.GetEndlessMode() and not oTalentCon.CheckHasAllTalent():
            return False
        pid = oHero.m_PlayerID
        if not self.IsVisibleTo(pid) or self.GetPlayerInteractType(pid) == INTERACT_TYPE_FORBID:
            return False
        return True



class CLimitGoldenCupNpc(CGoldenCupNpc):
    
    def __init__(self, *args):
        super(CLimitGoldenCupNpc, self).__init__(*args)



class CRareGoldenCupNpc(CGoldenCupNpc):
    m_EnableChooseAll = False
    
    def __init__(self, *args):
        super(CRareGoldenCupNpc, self).__init__(*args)
        self.m_RefreshCost = 0
        self.m_CurRefreshCost = { }
        self.SendRareGoldenMsg(cl_msgcenter.MSG_WAR_ADDRAREGOLDENCUP)

    
    def Refresh(self, oHero):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        (_, iRefreshTimes) = self.GetRefreshInfo(oHero)
        if iRefreshTimes <= 0:
            return None
        if self.m_ReleaseFlag:
            return None
        iCost = self.GetRefreshCost(oHero)
        WarnpcLog.Info('%d %d refresh raregoldencup %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_WarGSCash, iCost))
        if iCost and iCost > oHero.m_WarGSCash:
            WarnpcLog.Alert('%d %d refresh no enough gscash %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_WarGSCash, iCost))
            return None
        oHero.ConsumeGSCash(iCost, 'GoldencupRefreshCost')
        self.SetElementRefreshInfo(oHero.m_ID)
        dTimes[oHero.m_ID] = iTimes + 1
        self.Set('HeroRefreshTimes', dTimes)
        net.GS2CNpcRefreshInfo(self, oHero)
        oMiniGame = self.m_Game.m_MiniGameMgr.GetPlayerMiniGameByOwner(self.m_ID, oHero.m_ID)
        dOldRewardInfo = { }
        if oMiniGame:
            dOldRewardInfo = oMiniGame.Query('Reward', { })
            oMiniGame.End()
        dExtInfo = self.Query('dExtInfo')
        dExtInfo['OldReward'] = dOldRewardInfo
        self.ResetTalentReward(oHero.m_PlayerID)
        oNewMiniGame = cl_minigame.NewMiniGame(self.m_Game, self.Query('iMiniGame'), self.m_ID, oHero.m_ID, dExtInfo)
        if oNewMiniGame:
            oNewMiniGame.Start()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REFRESHGOLDENCUP, oHero, { })

    
    def GetRefreshInfo(self, oHero):
        oSurvivorElement = self.m_Game.m_WarMgr.GetSurvivorElement()
        if not oSurvivorElement:
            return (MIN_GOLDENCUP_REFRESH_TIMES, MIN_GOLDENCUP_REFRESH_TIMES)
        iMaxRefreshTimes = max(MIN_GOLDENCUP_REFRESH_TIMES, self.m_MaxRefreshTimes[oHero.m_ID] if oHero.m_ID in self.m_MaxRefreshTimes else 0)
        dTimes = oSurvivorElement.m_HeroRareCupRefresh
        if oHero.m_ID not in dTimes:
            dTimes[oHero.m_ID] = 0
        self.Set('HeroRefreshTimes', dTimes)
        iRefreshTimes = iMaxRefreshTimes - dTimes[oHero.m_ID]
        return (iMaxRefreshTimes, iRefreshTimes)

    
    def SetRefreshCost(self, tCost):
        self.m_RefreshCost = tCost

    
    def GetRefreshCost(self, oHero):
        dInfo = {
            cl_formula.FML_ARG_VID: oHero.m_ID }
        iCost = cl_formula.GetFormulaResult(self, self.m_RefreshCost, dInfo)
        return iCost

    
    def SetElementRefreshInfo(self, iHero):
        oSurvivorElement = self.m_Game.m_WarMgr.GetSurvivorElement()
        if not oSurvivorElement:
            return None
        if iHero not in oSurvivorElement.m_HeroRareCupRefresh:
            oSurvivorElement.m_HeroRareCupRefresh[iHero] = 1
        else:
            oSurvivorElement.m_HeroRareCupRefresh[iHero] += 1

    
    def OnFirstInteract(self, oHero):
        self.m_Discoverd = True
        oGame = self.m_Game
        lstPlayer = [ iPlayer for iPlayer in oGame.GetRealPlayers() if self.IsVisibleTo(iPlayer) ]
        if len(lstPlayer) > 1:
            cl_notify.SendCommonNotify(oGame, lstPlayer, 9357, {
                '$$name': oHero.m_OwnerName })

    
    def InitCustomAttr(self, clsData, dAddData):
        super().InitCustomAttr(clsData, dAddData)
        self.SendRareGoldenMsg(cl_msgcenter.MSG_WAR_CREATERAREGOLDENCUP)

    
    def SendRareGoldenMsg(self, iMsg):
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            cl_msgcenter.SendMsg(iMsg, oHero, {
                'NPC': self.m_ID })
        



class CPhaseGoldenCupNpc(CGoldenCupNpc):
    m_CheckInteractDistance = False
    
    def __init__(self, *args):
        super(CPhaseGoldenCupNpc, self).__init__(*args)
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivorElement:
            self.m_MiniGame = oSurvivorElement.m_RewardMgr.GetTalentMG()
            self.InitPhaseTalentGenInfo()
        else:
            self.m_MiniGame = 0

    
    def OnChooseOne(self, oHero, iAnswer):
        self.ConsumeTimes(oHero.m_PlayerID, 1)

    
    def OnChooseAll(self, oHero):
        self.ConsumeTimes(oHero.m_PlayerID, 1)

    
    def ConsumeTimes(self, iPlayer, iTimes):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if not oSurvivorElement:
            return None
        oSurvivorElement.m_RewardMgr.ConsumeTimes(iPlayer, iTimes)

    
    def PlayerChose(self, oHero):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if not oSurvivorElement:
            super().PlayerChose(oHero)
            return None
        dAllGenTalent = self.Query('AllGenTalent', { })
        if oHero.m_ID in dAllGenTalent:
            dAllGenTalent.pop(oHero.m_ID)
        oRewardMgr = oSurvivorElement.m_RewardMgr
        if oRewardMgr.ValidReward(oHero.m_PlayerID):
            net.GS2CNpcRefreshInfo(self, oHero)
            oMiniGame = cl_minigame.NewMiniGame(self.m_Game, self.m_MiniGame, self.m_ID, oHero.m_ID, self.Query('dExtInfo'))
            if oMiniGame:
                oMiniGame.SendChoose()
            else:
                super().PlayerChose(oHero)

    
    def ValidInteract(self, oHero):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if not oSurvivorElement:
            return False
        if not oSurvivorElement.m_RewardMgr.ValidReward(oHero.m_PlayerID):
            return False
        return super().ValidInteract(oHero)

    
    def OnInteract(self, oHero):
        pass

    
    def Release(self):
        self.SetPhaseTalentGenInfo()
        super().Release()

    
    def SetPhaseTalentGenInfo(self):
        oBigDataAnaMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        oNewSurvivorCom = oBigDataAnaMgr.GetCom('NewSurvivor')
        if not oNewSurvivorCom:
            return None
        dAllGenTalent = self.Query('AllGenTalent', { })
        if not dAllGenTalent:
            return None
        oNewSurvivorCom.m_PhaseTalentGenInfo = dAllGenTalent

    
    def InitPhaseTalentGenInfo(self):
        oBigDataAnaMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        oNewSurvivorCom = oBigDataAnaMgr.GetCom('NewSurvivor')
        if oNewSurvivorCom:
            dPhaseInfo = oNewSurvivorCom.m_PhaseTalentGenInfo
            self.Set('AllGenTalent', dPhaseInfo)
            oNewSurvivorCom.m_PhaseTalentGenInfo = { }
