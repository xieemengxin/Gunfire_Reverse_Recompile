# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_talent.pyc
# RelativePath: clientlogic/cl_minigame/mg_talent.pyc
# Source Generated with Decompyle++
# File: mg_talent.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy, ShufferList
from cl_commondefines import TALENTTYPE_COMMON, MG_TALENT, NPC_CB_VALUE, NPC_CB_DICT, NPC_CB_VALUELIST, VIRTUAL_ITEM_TALENT, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NPC_CB_CHOOSEALL, TALENT_CHOOSE_NOMAL, TALENT_CHOOSE_RARE, TALENT_CHOOSE_PHASE
from cl_commondefines import PF_TYPE_TALENT
from cl_object.logging import WartalentLog
from cs_propdata import PROP_TALENT
from .mobject import CRewardChooseGame, CBaseGameData
import cl_npc.net as npcnet
import cl_perform
import cl_reward
import cl_msgcenter
import cl_minigame
import cl_formula

class CRewardChooseTalentGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_TALENT
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def CheckShiftGameClass(cls, oGame, iOwner):
        oNpc = oGame.GetObject(iOwner)
        if oNpc and oNpc.m_FightType == NWARRIOR_NPC_EXCHANGEGOLDENCUP:
            return CExchangeRewardChooseTalentGame
        return cls.GetGameClass()

    CheckShiftGameClass = classmethod(CheckShiftGameClass)
    
    def GetGameClass(cls):
        return CRewardChooseTalentGame

    GetGameClass = classmethod(GetGameClass)


class CRewardChooseTalentGame(CRewardChooseGame):
    m_RewardReason = 'RewardChooseTalentGame'
    m_SubMsg = TALENT_CHOOSE_NOMAL
    
    def OnInit(self):
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if 'Num' not in self.m_Data:
            self.m_Data['Num'] = 3
        super(CRewardChooseTalentGame, self).OnInit()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_GEN, oPlayer, {
            'NPC': self.m_Owner,
            'Talent': self.Query('Reward', { }),
            'Reason': self.m_RewardReason })

    
    def GetRewardInfo(self):
        dReward = { }
        lstReward = []
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if not oPlayer:
            return { }
        dAssignReward = self.GetAssignReward(oPlayer.m_PlayerID)
        if dAssignReward:
            self.PreChooseAction(oPlayer, dAssignReward)
            return dAssignReward
        iCareer = oPlayer.m_Career
        if iCareer not in self.m_ChooseWeight:
            return { }
        dCareerChooseWeight = self.m_ChooseWeight[iCareer] if iCareer in self.m_ChooseWeight else { }
        dFilterChooseWeight = { }
        for iType, dChooseWeight in dCareerChooseWeight.items():
            dFilterChooseWeight[iType] = { }
            dFilterChooseWeight[iType].update(dChooseWeight)
        
        dBanTalent = oPlayer.m_TalentCon.GetAllBanTalent()
        dModifyTalentWeight = oPlayer.Query('ModifyTalentWeight', { })
        for iType, dChooseWeight in dFilterChooseWeight.items():
            lstTalent = list(dChooseWeight)
            for iTalent in lstTalent:
                if iTalent in dBanTalent:
                    dChooseWeight.pop(iTalent)
                    continue
                oTalent = oPlayer.m_TalentCon.GetPerform(iTalent)
                if oTalent and oTalent.m_Level == oTalent.GetMaxUpgradeLevel():
                    dChooseWeight.pop(iTalent)
                    continue
                if iTalent in dModifyTalentWeight:
                    iNowWeight = dChooseWeight[iTalent]
                    iModify = sum(dModifyTalentWeight[iTalent].values())
                    iNowWeight = int(iNowWeight + iNowWeight * iModify / 100)
                    if iNowWeight < 0:
                        iNowWeight = 0
                    dChooseWeight[iTalent] = iNowWeight
            
        
        iChooseNum = self.Query('ChooseTalentNum', 0)
        iChooseNum = iChooseNum if iChooseNum else 3
        oNpc = self.m_Game.GetObject(self.m_Owner)
        if oNpc and oNpc.Query('SelectedTalent'):
            bSelectedTalent = oNpc.Query('SelectedTalent')
            if bSelectedTalent:
                oNpc.Delete('SelectedTalent')
                lstTalent = []
                for oPerform in oPlayer.m_TalentCon.m_Perform.values():
                    if oPerform.m_PFType != PF_TYPE_TALENT:
                        continue
                    if oPerform.Level() >= oPerform.m_MaxLevel:
                        continue
                    if oPerform.m_SID in dBanTalent:
                        continue
                    lstTalent.append(oPerform.m_SID)
                
                lstTalent = ShufferList(oPlayer.m_Game, lstTalent, iChooseNum)
                lstReward.extend(lstTalent)
                iChooseNum -= len(lstTalent)
        if iChooseNum > 0:
            dAllChooseWeight = { }
            for dChooseWeight in dFilterChooseWeight.values():
                dAllChooseWeight.update(dChooseWeight)
            
            dCommonTalentWeight = oPlayer.m_TalentCon.GetCommonTalentWeight()
            dAllChooseWeight.update(dCommonTalentWeight)
            dOldReward = self.Query('OldReward', { })
            if iChooseNum <= len(dAllChooseWeight) - len(dOldReward):
                for iTalent in dOldReward:
                    if iTalent in dAllChooseWeight:
                        dAllChooseWeight.pop(iTalent)
                
            dCommonShowTalent = oPlayer.Query('CommonShowTalent', { })
            iCommonShowTalentNum = 0
            for lstCommonShowTalent in dCommonShowTalent.values():
                iCommonShowTalentNum += len(lstCommonShowTalent)
            
            if iChooseNum <= len(dAllChooseWeight) - iCommonShowTalentNum:
                for lstTalent in dCommonShowTalent.values():
                    for iShowTalent in lstTalent:
                        if iShowTalent not in dAllChooseWeight:
                            continue
                        dAllChooseWeight.pop(iShowTalent)
                    
                
            for _ in range(iChooseNum):
                iTalent = ChooseKey(self.m_Game, dAllChooseWeight)
                if not iTalent:
                    WartalentLog.Warn('player%d 天赋无可抽取' % self.m_Player)
                    break
                lstReward.append(iTalent)
                dAllChooseWeight.pop(iTalent)
            
        for iTalent in lstReward:
            oTalent = oPlayer.m_TalentCon.GetPerform(iTalent)
            dReward[iTalent] = self.GetRewardTalentLevel(oTalent)
        
        self.PreChooseAction(oPlayer, dReward)
        return dReward

    
    def PreChooseAction(self, oPlayer, dReward):
        iOwner = self.m_Owner
        oNpc = self.m_Game.GetObject(iOwner)
        dAllGenTalent = oNpc.SetDefault('AllGenTalent', { })
        if self.m_Player not in dAllGenTalent:
            dAllGenTalent[self.m_Player] = []
        dAllGenTalent[self.m_Player].extend(list(dReward))
        for iSID in dReward:
            clsPerform = cl_perform.GetPerformModule(iSID)
            clsPerform.PreChooseAction(oPlayer)
        

    
    def SendChoose(self):
        oGame = self.m_Game
        oPlayer = oGame.GetObject(self.m_Player)
        oNpc = oGame.GetObject(self.m_Owner)
        if not oPlayer or not oNpc:
            self.Leave()
            return None
        lstTalent = self.SetRealReward(oPlayer, oNpc)
        self.SetNpcInfo(oPlayer, oNpc, lstTalent)
        self.Leave()

    
    def SetNpcInfo(self, oPlayer, oNpc, lstTalent):
        npcnet.GS2CNpcChooseTalent(oPlayer, lstTalent, self.m_Owner)
        self.SetNpcUI(oPlayer, oNpc)
        oNpc.SetNpcRefreshCallBackFunction(oPlayer)

    
    def SetRealReward(self, oPlayer, oNpc):
        dReward = self.RefreshRewardTalentLevel(oPlayer)
        lstTalent = []
        lstReward = list(dReward)
        dCommonShowTalent = oPlayer.SetDefault('CommonShowTalent', { })
        dCommonShowTalent[oNpc.m_ID] = lstReward
        dData = {
            'Num': oNpc.Query('ForceNum', self.m_Data['Num']) }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE_BEFORE, oPlayer, dData, iSub = self.m_SubMsg)
        iNum = dData['Num']
        dRealReward = { }
        for iSID in lstReward[:iNum]:
            iLevel = dReward[iSID]
            clsPerform = cl_perform.GetPerformModule(iSID)
            sSubDesc = clsPerform.SubDesc(oPlayer)
            lstTalent.append((iSID, iLevel, sSubDesc))
            dRealReward[iSID] = iLevel
        
        dOldReward = self.Query('RealReward', { })
        lstAdd = list(set(dRealReward) - set(dOldReward))
        if lstAdd:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_GEN_CHANGE, oPlayer, {
                'Talents': lstAdd })
        self.Set('RealReward', dRealReward)
        return lstTalent

    
    def RefreshRewardTalentLevel(self, oPlayer):
        dReward = self.Query('Reward', { })
        for iSID in dReward:
            oTalent = oPlayer.m_TalentCon.GetPerform(iSID)
            dReward[iSID] = self.GetRewardTalentLevel(oTalent)
        
        return dReward

    
    def GetRewardTalentLevel(self, oTalent):
        if oTalent:
            return oTalent.m_Level + 1
        return 1

    
    def RemoveReward(self):
        self.Set('Reward', { })
        self.Set('RealReward', { })

    
    def PlayerChooseTalent(self, who, iAnswer):
        dReward = self.Query('RealReward', { })
        lstTalent = list(dReward)
        oGame = self.m_Game
        iOwner = self.m_Owner
        iMGID = self.m_ID
        if not iAnswer == 0 or not dReward or iAnswer not in dReward:
            self.RemoveReward()
            dReward = {
                'item': VIRTUAL_ITEM_TALENT,
                'info': {
                    'sid': iAnswer,
                    'amount': 1 } }
            dExtInfo = {
                'NpcID': iOwner }
            cl_reward.RewardItem(oGame, who, [
                dReward], 'RewardChooseTalentGame%d-%d' % (self.m_SID, self.m_ID), dExtInfo)
        else:
            WartalentLog.Alert('%s %s %s no reward' % (who.m_PlayerID, iAnswer, dReward))
        self.End()
        oNpc = oGame.GetObject(iOwner)
        if oNpc:
            dAllGenTalent = oNpc.Query('AllGenTalent', { })
            dInfo = {
                'Talents': dAllGenTalent[who.m_ID] if who.m_ID in dAllGenTalent else lstTalent,
                'NpcID': oNpc.m_ID,
                'Reason': self.m_RewardReason,
                'Choose': iAnswer,
                'MGID': iMGID }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE, who, dInfo)
            oNpc.PlayerChose(who)

    
    def PlayerChooseAllTalent(self, who):
        oGame = self.m_Game
        iOwner = self.m_Owner
        oNpc = oGame.GetObject(iOwner)
        if not oNpc or not (oNpc.m_EnableChooseAll):
            return None
        dReward = self.FilterOverMaxLevelTalent(who)
        sReason = 'RewardChooseAllTalentGame%d-%d' % (self.m_SID, self.m_ID)
        (iMaxTalentChooseAllTimes, iCanTalentChooseAllTimes) = oNpc.GetChooseAllInfo(who)
        if iCanTalentChooseAllTimes <= 0:
            WartalentLog.Alert('%s %s %s %s no reward all %s' % (who.m_PlayerID, dReward, iMaxTalentChooseAllTimes, iCanTalentChooseAllTimes, sReason))
            return None
        if dReward:
            lstTalent = list(dReward)
            self.RemoveReward()
            oNpc.UseChooseAllTimes(who)
            dAllGenTalent = oNpc.Query('AllGenTalent', { })
            dInfo = {
                'Talents': dAllGenTalent[who.m_ID] if who.m_ID in dAllGenTalent else lstTalent,
                'NpcID': oNpc.m_ID,
                'Reason': self.m_RewardReason,
                'ChooseAll': 1,
                'MGID': self.m_ID }
            dExtInfo = {
                'NpcID': iOwner }
            for iTalent in lstTalent:
                dRealReward = {
                    'item': VIRTUAL_ITEM_TALENT,
                    'info': {
                        'sid': iTalent,
                        'amount': 1 } }
                cl_reward.RewardItem(oGame, who, [
                    dRealReward], sReason, dExtInfo)
                dInfo['Choose'] = iTalent
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE, who, dInfo)
            
        else:
            WartalentLog.Alert('%s %s %s reward empty %s' % (who.m_PlayerID, oNpc.m_SID, dReward, sReason))
        self.End()
        oNpc.PlayerChose(who)

    
    def GetAssignReward(self, pid):
        oNpc = self.m_Game.GetObject(self.m_Owner)
        if not oNpc:
            return { }
        if oNpc.m_FightType not in (NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP):
            return { }
        return oNpc.GetTalentReward(pid)

    
    def SetNpcUI(self, oPlayer, oNpc):
        npcnet.SetNpcUICallBackFunction(oPlayer, NPC_CB_VALUE, self.PlayerChooseTalent, oNpc)
        if oNpc.m_EnableChooseAll:
            npcnet.SetNpcUICallBackFunction(oPlayer, NPC_CB_CHOOSEALL, self.PlayerChooseAllTalent, oNpc)

    
    def FilterOverMaxLevelTalent(self, oHero):
        dRealReward = self.Query('RealReward', { })
        if not dRealReward:
            return { }
        dPerform = oHero.m_TalentCon.m_Perform
        dReward = { }
        for iTalent, iLevel in dRealReward.items():
            if iTalent in dPerform and dPerform[iTalent].m_MaxLevel < iLevel:
                continue
            dReward[iTalent] = iLevel
        
        return dReward



class CUpgradeChooseTalentGameData(CRewardChooseTalentGameData):
    
    def GetGameClass(cls):
        return CUpgradeChooseTalentGame

    GetGameClass = classmethod(GetGameClass)


class CUpgradeChooseTalentGame(CRewardChooseTalentGame):
    m_RewardReason = 'UpgradeChooseTalentGame'
    
    def OnInit(self):
        super(CUpgradeChooseTalentGame, self).OnInit()

    
    def GetRewardInfo(self):
        dReward = { }
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if not oPlayer:
            return { }
        iCareer = oPlayer.m_Career
        if iCareer not in self.m_ChooseWeight:
            return { }
        dCareerChooseWeight = self.m_ChooseWeight[iCareer] if iCareer in self.m_ChooseWeight else { }
        dFilterChooseWeight = { }
        for iType, dChooseWeight in dCareerChooseWeight.items():
            dFilterChooseWeight[iType] = { }
            dFilterChooseWeight[iType].update(dChooseWeight)
        
        dBanTalent = oPlayer.m_TalentCon.GetAllBanTalent()
        dAddtionalTalentWeight = oPlayer.Query('AddtionalTalentWeight', { })
        for iType, dChooseWeight in dFilterChooseWeight.items():
            lstTalent = list(dChooseWeight)
            for iTalent in lstTalent:
                if iTalent in dBanTalent:
                    dChooseWeight.pop(iTalent)
                    continue
                oTalent = oPlayer.m_TalentCon.GetPerform(iTalent)
                if oTalent and oTalent.m_Level == oTalent.GetMaxUpgradeLevel():
                    dChooseWeight.pop(iTalent)
                    continue
                if iTalent in dAddtionalTalentWeight:
                    iNowWeight = dChooseWeight[iTalent]
                    iNowWeight = int(iNowWeight + iNowWeight * dAddtionalTalentWeight[iTalent] / 100)
                    if iNowWeight < 0:
                        iNowWeight = 0
                    dChooseWeight[iTalent] = iNowWeight
            
        
        iChooseCnt = self.Query('ChooseCnt', 0)
        if not iChooseCnt:
            return { }
        dAllChooseWeight = { }
        for dChooseWeight in dFilterChooseWeight.values():
            dAllChooseWeight.update(dChooseWeight)
        
        for _ in range(iChooseCnt):
            iTalent = ChooseKey(self.m_Game, dAllChooseWeight)
            if not iTalent:
                WartalentLog.Warn('player%d 天赋无可抽取' % self.m_Player)
                break
            clsTalent = cl_perform.GetPerformModule(iTalent)
            lstAttr = cl_minigame.MiniGameAttrInfo(clsTalent, PROP_TALENT)
            dReward[iTalent] = {
                'Attr': lstAttr }
            dAllChooseWeight.pop(iTalent)
        
        self.PreChooseAction(oPlayer, dReward)
        return dReward

    
    def SendChoose(self):
        oHero = self.m_Game.GetObject(self.m_Player)
        if oHero:
            dReward = self.Query('Reward')
            oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
            if oSurvivorElement:
                dExtInfo = self.Query('ExtInfo', { })
                oSurvivorElement.m_UpgradeMgr.AddRewardInfo(oHero, VIRTUAL_ITEM_TALENT, dReward, 'UpGradeMiniGame', dExtInfo)
        self.End()



class CRewardChooseRareTalentGameData(CRewardChooseTalentGameData):
    
    def GetGameClass(cls):
        return CRewardChooseRareTalentGame

    GetGameClass = classmethod(GetGameClass)


class CRewardChooseRareTalentGame(CRewardChooseTalentGame):
    m_RewardReason = 'RewardChooseRareTalentGame'
    m_SubMsg = TALENT_CHOOSE_RARE
    
    def OnInit(self):
        super(CRewardChooseRareTalentGame, self).OnInit()

    
    def GetRewardInfo(self):
        dOldReward = self.Query('OldReward', { })
        dReward = { }
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if not oPlayer:
            return { }
        iCareer = oPlayer.m_Career
        if iCareer not in self.m_ChooseWeight:
            return { }
        dCareerChooseWeight = self.m_ChooseWeight[iCareer] if iCareer in self.m_ChooseWeight else { }
        dFilterChooseWeight = { }
        for iType, dChooseWeight in dCareerChooseWeight.items():
            dFilterChooseWeight[iType] = { }
            dFilterChooseWeight[iType].update(dChooseWeight)
        
        dBanTalent = oPlayer.m_TalentCon.GetAllBanTalent()
        for iType, dChooseWeight in dFilterChooseWeight.items():
            lstTalent = list(dChooseWeight)
            for iTalent in lstTalent:
                if iTalent in dBanTalent:
                    dChooseWeight.pop(iTalent)
                    continue
                oTalent = oPlayer.m_TalentCon.GetPerform(iTalent)
                if oTalent and oTalent.m_Level == oTalent.GetMaxUpgradeLevel():
                    dChooseWeight.pop(iTalent)
            
        
        for iType, dChooseWeight in dFilterChooseWeight.items():
            if not dChooseWeight:
                continue
            if iType == TALENTTYPE_COMMON:
                continue
            iWeight = self.GetRareTalentWeight(oPlayer, iType)
            lstTalent = list(dChooseWeight)
            for iTalent in lstTalent:
                dChooseWeight[iTalent] = iWeight
            
        
        dAllChooseWeight = { }
        for dChooseWeight in dFilterChooseWeight.values():
            for iTalent, iWeight in dChooseWeight.items():
                if iTalent in dOldReward:
                    continue
                if iTalent not in dAllChooseWeight:
                    dAllChooseWeight[iTalent] = iWeight
                    continue
                dAllChooseWeight[iTalent] += iWeight
            
        
        iChooseNum = self.m_Data['Num']
        for _ in range(iChooseNum):
            iTalent = ChooseKey(self.m_Game, dAllChooseWeight)
            if not iTalent:
                WartalentLog.Warn('player%d 稀有天赋无可抽取' % self.m_Player)
                break
            oTalent = oPlayer.m_TalentCon.GetPerform(iTalent)
            dReward[iTalent] = self.GetRewardTalentLevel(oTalent)
            dAllChooseWeight.pop(iTalent)
        
        return dReward

    
    def GetRareTalentWeight(self, oPlayer, iTalentType):
        oSurvivorElement = oPlayer.m_Game.m_WarMgr.GetSurvivorElement()
        if not oSurvivorElement:
            return 0
        iWeight = oSurvivorElement.m_RareTalentInfo['TypeNum']
        return cl_formula.GetResultByData(oPlayer, iWeight, { }, {
            'TalentType': iTalentType })



class CPhaseChooseTalentGameData(CRewardChooseTalentGameData):
    
    def GetGameClass(cls):
        return CPhaseChooseTalentGame

    GetGameClass = classmethod(GetGameClass)


class CPhaseChooseTalentGame(CRewardChooseTalentGame):
    m_RewardReason = 'PhaseChooseTalentGame'
    m_SubMsg = TALENT_CHOOSE_PHASE
    
    def OnInit(self):
        super(CPhaseChooseTalentGame, self).OnInit()

    
    def PlayerChooseTalent(self, who, iAnswer):
        oNpc = self.m_Game.GetObject(self.m_Owner)
        if oNpc:
            oNpc.OnChooseOne(who, iAnswer)
        super().PlayerChooseTalent(who, iAnswer)

    
    def PlayerChooseAllTalent(self, who):
        oNpc = self.m_Game.GetObject(self.m_Owner)
        if oNpc:
            oNpc.OnChooseAll(who)
        super().PlayerChooseAllTalent(who)



class CDirectRewardRandomTalentGameData(CRewardChooseTalentGameData):
    
    def GetGameClass(cls):
        return CDirectRewardRandomTalentGame

    GetGameClass = classmethod(GetGameClass)


class CDirectRewardRandomTalentGame(CRewardChooseTalentGame):
    m_RewardReason = 'DirectRewardRandomTalentGame'
    
    def OnInit(self):
        self.Set('ChooseTalentNum', 1)
        super().OnInit()

    
    def SendChoose(self):
        oGame = self.m_Game
        oPlayer = oGame.GetObject(self.m_Player)
        if oPlayer:
            dReward = self.Query('Reward', { })
            if not dReward:
                WartalentLog.Alert('%s %s %s %s %s randomtalent no reward' % (oGame.m_ID, oPlayer.m_PlayerID, self.m_ID, self.m_SID, dReward))
                return None
            lstTalent = list(dReward)
            self.Set('Reward', { })
            self.RewardTalent(oPlayer, lstTalent[0])

    
    def RewardTalent(self, oHero, iTalent):
        dReward = {
            'item': VIRTUAL_ITEM_TALENT,
            'info': {
                'sid': iTalent,
                'amount': 1 } }
        dExtInfo = {
            'NpcID': self.m_Owner }
        cl_reward.RewardItem(self.m_Game, oHero, [
            dReward], '%s-%d-%d' % (self.m_RewardReason, self.m_SID, self.m_ID), dExtInfo)
        self.End()



class CExchangeRewardChooseTalentGame(CRewardChooseTalentGame):
    m_RewardReason = 'ExchangeRewardChooseTalentGame'
    
    def OnInit(self):
        self.m_Data['Num'] = 1
        super().OnInit()

    
    def SetNpcInfo(self, oPlayer, oNpc, lstTalent):
        npcnet.GS2CExchangeNpcChooseTalent(oPlayer, lstTalent, self.m_Owner)
        if oNpc.m_EnableChooseAll:
            npcnet.SetNpcUICallBackFunction(oPlayer, NPC_CB_VALUELIST, self.PlayerChooseAllTalent, oNpc)
        npcnet.SetNpcUICallBackFunction(oPlayer, NPC_CB_DICT, self.PlayerChooseTalent, oNpc)
        oNpc.SetNpcRefreshCallBackFunction(oPlayer)

    
    def PlayerChooseTalent(self, who, dQue):
        dReward = self.Query('RealReward', { })
        oGame = self.m_Game
        WartalentLog.Info('%s %s choose receive %s %s' % (oGame.m_ID, who.m_PlayerID, dQue, dReward))
        oNpc = oGame.GetObject(self.m_Owner)
        if not oNpc or not dQue or not dReward or not self.CheckAnswer(who, dQue, dReward, 0):
            return None
        lstTalent = list(dReward)
        dAllGenTalent = oNpc.Query('AllGenTalent', { })
        sReason = '%s-%d-%d' % (self.m_RewardReason, self.m_SID, self.m_ID)
        dInfo = {
            'Talents': dAllGenTalent[who.m_ID] if who.m_ID in dAllGenTalent else lstTalent,
            'NpcID': oNpc.m_ID,
            'Reason': self.m_RewardReason,
            'MGID': self.m_ID }
        self.DeGradeTalents(who, list(dQue.values()), sReason)
        self.RemoveReward()
        dExtInfo = {
            'NpcID': self.m_Owner }
        for iAdd in dQue:
            dRewardInfo = {
                'item': VIRTUAL_ITEM_TALENT,
                'info': {
                    'sid': iAdd,
                    'amount': 1 } }
            cl_reward.RewardItem(oGame, who, [
                dRewardInfo], sReason, dExtInfo)
            dInfo['Choose'] = iAdd
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE, who, dInfo)
        
        self.End()
        oNpc.PlayerChose(who)

    
    def PlayerChooseAllTalent(self, who, lstAnswer):
        dReward = self.FilterOverMaxLevelTalent(who)
        lstTalent = list(dReward)
        dQue = { }
        iLen = len(lstTalent)
        if iLen and len(lstAnswer) == iLen:
            for idx in range(iLen):
                dQue[lstTalent[idx]] = lstAnswer[idx]
            
        oGame = self.m_Game
        WartalentLog.Info('%s %s chooseall receive %s %s' % (oGame.m_ID, who.m_PlayerID, lstAnswer, dReward))
        oNpc = oGame.GetObject(self.m_Owner)
        if not oNpc or not dQue or not dReward or not self.CheckAnswer(who, dQue, dReward, 1):
            return None
        (_, iCanTalentChooseAllTimes) = oNpc.GetChooseAllInfo(who)
        if iCanTalentChooseAllTimes <= 0:
            WartalentLog.Alert('%s %s %s %s lack of all usetimes' % (oGame.m_ID, who.m_PlayerID, dReward, iCanTalentChooseAllTimes))
            return None
        oNpc.UseChooseAllTimes(who)
        sReason = '%s-%d-%d-All' % (self.m_RewardReason, self.m_SID, self.m_ID)
        self.DeGradeTalents(who, lstAnswer, sReason)
        self.RemoveReward()
        dAllGenTalent = oNpc.Query('AllGenTalent', { })
        dInfo = {
            'Talents': dAllGenTalent[who.m_ID] if who.m_ID in dAllGenTalent else lstTalent,
            'NpcID': oNpc.m_ID,
            'Reason': self.m_RewardReason,
            'ChooseAll': 1,
            'MGID': self.m_ID }
        dExtInfo = {
            'NpcID': self.m_Owner }
        for iTalent in lstTalent:
            dRealReward = {
                'item': VIRTUAL_ITEM_TALENT,
                'info': {
                    'sid': iTalent,
                    'amount': 1 } }
            cl_reward.RewardItem(oGame, who, [
                dRealReward], sReason, dExtInfo)
            dInfo['Choose'] = iTalent
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TALENT_CHOOSE, who, dInfo)
        
        self.End()
        oNpc.PlayerChose(who)

    
    def CheckAnswer(self, who, dQue, dReward, iAll):
        if iAll or len(dQue) != len(dReward):
            return False
        if len(dQue) > 1:
            return False
        oTalentCon = who.m_TalentCon
        if not oTalentCon:
            return False
        dTalent = oTalentCon.GetAllTalentLevel()
        oGame = self.m_Game
        dCurLevelCost = { }
        for iAdd, iExchange in dQue.items():
            if not iExchange or iExchange not in dTalent:
                return False
            if iExchange in dQue:
                WartalentLog.Alert('%s %s %s exchange the same' % (oGame.m_ID, who.m_PlayerID, iExchange))
                return False
            if iAdd not in dReward:
                WartalentLog.Alert('%s %s %s %s no reward' % (oGame.m_ID, who.m_PlayerID, iAdd, dReward))
                return False
            iLevel = dCurLevelCost.get(iExchange, 0) + 1
            dCurLevelCost[iExchange] = iLevel
            iCanCost = dTalent[iExchange]
            if iLevel > iCanCost:
                WartalentLog.Alert('%s %s %s %s not enough level' % (oGame.m_ID, who.m_PlayerID, iLevel, iCanCost))
                return False
        
        return True

    
    def DeGradeTalents(self, who, lstTalent, sReason):
        oTalentCon = who.m_TalentCon
        if not oTalentCon:
            return None
        for iTalent in lstTalent:
            oTalentCon.DeGradeTalent(iTalent, 1, sReason)
        


