# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivorrewardmgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivorrewardmgr.pyc
# Source Generated with Decompyle++
# File: survivorrewardmgr.pyc (Python 3.6)

from cl_only import DeepCopy, WeakProxy, Time2Frame
from cl_object.logging import SurvivorLog
from cl_commondefines import VIRTUAL_ITEM_EQUIP
from cl_commondecorator import ChooseRewardEnd
from cl_npc.net import GS2CPhaseGoldenCount
import cl_msgcenter
import cl_formula
import cl_minigame
import cl_snetwar
import cl_reward
import cl_notify
NOTIFY_WEAPON = 2375

class CSurvivorRewardMgr(object):
    
    def __init__(self, oSurvivorElement, oData):
        self.m_Survivor = WeakProxy(oSurvivorElement)
        self.m_Game = self.m_Survivor.m_Game
        self.m_CallFlag = 'SurvivorRewardMgr'
        self.m_RemainTimes = { }
        self.m_NextTimes = { }
        self.m_NextMGRecord = []
        self.m_MiniGame = oData.m_Config.get('REWARD', { })
        self.m_InitWeapon = { }
        self.m_CountDown = oData.m_Config.get('CountDown', 1500)
        self.m_ChooseWeaponHero = []

    
    def Init(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnInitHeroInfo, self.m_CallFlag, -1, 0)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMSG_RESTPHASE, self.OnRestPhase, self.m_CallFlag)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, self.OnHeroChooseTalent, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        oGame.DoneGlobalAttention(oWarMgr, cl_msgcenter.MSG_WARMSG_RESTPHASE, self.m_CallFlag)
        oGame.DoneGlobalAttention(oWarMgr, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, self.m_CallFlag)
        self.m_Survivor = None
        self.m_Game = None
        self.m_RemainTimes = { }
        self.m_NextTimes = { }

    
    def Save(self):
        dData = { }
        dData['RT'] = self.m_RemainTimes
        dData['NT'] = self.m_NextTimes
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_RemainTimes = dData['RT']
        self.m_NextTimes = dData['NT']

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        oGame = self.m_Game
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.OnMapLoadOK, iPriority = 1, iOnce = 1)
        

    
    def OnInitHeroInfo(self, oWarMgr, dInfo):
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        if self.m_RemainTimes:
            return None
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.m_RemainTimes[oHero.m_PlayerID] = 0
            self.m_NextTimes[oHero.m_PlayerID] = 0
        

    
    def OnMapLoadOK(self, oHero, dMsgInfo):
        iHero = oHero.m_ID
        if iHero not in self.m_InitWeapon:
            oMiniGame = cl_minigame.NewMiniGame(self.m_Game, self.m_MiniGame['WeaponMG'], oHero.m_ID, oHero.m_ID, {
                'ChooseCnt': 3 })
            if oMiniGame:
                oMiniGame.Start()
            elif not self.m_InitWeapon[iHero]:
                return 1
        None.GS2CChooseItem(oHero)
        return 0

    
    def GS2CChooseItem(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_InitWeapon or not self.m_InitWeapon[iHero]:
            return None
        (iMenuIdx, dReward) = self.m_InitWeapon[iHero]
        lstItem = []
        for dOption in dReward.values():
            lstAtt = dOption['Attr']
            lstItem.append({
                'Attr': lstAtt })
        
        cl_snetwar.GS2CChooseRewardItem(oHero.m_PlayerID, iMenuIdx, VIRTUAL_ITEM_EQUIP, lstItem, { })

    
    def AddInitWeapon(self, oHero, dReward):
        oHero.IncMenuIdx()
        iMenuIdx = oHero.m_NpcUIMenuIdx
        self.m_InitWeapon[oHero.m_ID] = [
            iMenuIdx,
            dReward]

    
    def ValidChooseReward(self, oHero):
        iHero = oHero.m_ID
        if iHero in self.m_InitWeapon and self.m_InitWeapon[iHero]:
            return True
        return False

    
    def ChooseReward(self, oHero, iMenuIdx, iAnswer):
        iHero = oHero.m_ID
        if iHero not in self.m_InitWeapon or not self.m_InitWeapon[iHero]:
            return 1
        if iAnswer:
            (_, dReward) = self.m_InitWeapon[iHero]
            self.m_InitWeapon[iHero] = []
            SurvivorLog.Info('%d %d choose initweapon %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iAnswer))
            dTrueReward = {
                'item': VIRTUAL_ITEM_EQUIP,
                'info': {
                    'sid': iAnswer,
                    'item': dReward[iAnswer]['Item'],
                    'data': { } } }
            sReason = 'initweapon-%d' % iAnswer
            cl_reward.RewardItem(self.m_Game, oHero, [
                dTrueReward], sReason, {
                'NoSendCreateRelicMsg': True })
        else:
            self.m_InitWeapon[iHero] = []
        iPlayerID = oHero.m_PlayerID
        if iPlayerID in self.m_ChooseWeaponHero:
            self.m_ChooseWeaponHero.remove(iPlayerID)
            cl_notify.SendCommonNotify(self.m_Game, [
                iPlayerID], NOTIFY_WEAPON, { }, {
                'iTime': 0 })
            self.m_Survivor.ResumeFightNotify([
                iPlayerID])
        return 1

    ChooseReward = ChooseRewardEnd(ChooseReward)
    
    def InitWeaponCountDown(self):
        oGame = self.m_Game
        lstPlayer = []
        for iHero, lstReward in self.m_InitWeapon.items():
            if not lstReward:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstPlayer.append(oHero.m_PlayerID)
        
        self.m_ChooseWeaponHero = lstPlayer
        self.m_Survivor.RemoveFightNotify(lstPlayer)
        cl_notify.SendCommonNotify(oGame, lstPlayer, NOTIFY_WEAPON, {
            '$time': str(self.m_CountDown) }, {
            'iTime': self.m_CountDown })
        self.m_Survivor.Call_Out(self.CountDownOver, Time2Frame(self.m_CountDown), 'CountDownOver')

    
    def CountDownOver(self):
        oGame = self.m_Game
        lstPlayer = []
        for iHero, lstReward in self.m_InitWeapon.items():
            if not lstReward:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstPlayer.append(oHero.m_PlayerID)
            (iMenuIdx, dReward) = lstReward
            (iAnswer, lstAtt) = list(dReward.items())[0]
            self.ChooseReward(oHero, iMenuIdx, iAnswer)
            cl_snetwar.GS2CChooseRewardItem(oHero.m_PlayerID, iMenuIdx, VIRTUAL_ITEM_EQUIP, [], { })
        
        if lstPlayer:
            cl_notify.SendCommonNotify(self.m_Game, lstPlayer, NOTIFY_WEAPON, { }, {
                'iTime': 0 })
            self.m_Survivor.ResumeFightNotify(lstPlayer)

    
    def OnRestPhase(self, oTarget, oSurvivor, dMsgInfo):
        oGame = self.m_Game
        for iHeroID in oGame.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHeroID)
            if not oHero:
                continue
            self.m_RemainTimes[oHero.m_PlayerID] += self.m_NextTimes[oHero.m_PlayerID] + 1
            self.m_NextTimes[oHero.m_PlayerID] = 0
            self.RewardWarCash(oHero, dMsgInfo)
            self.GS2CPhaseGoldenCount(oHero.m_PlayerID)
        

    
    def GS2CPhaseGoldenCount(self, iPlayerID):
        GS2CPhaseGoldenCount(iPlayerID, self.m_RemainTimes[iPlayerID])

    
    def OnHeroChooseTalent(self, oWarMgr, oHero, dMsgInfo):
        if 'Choose' in dMsgInfo and dMsgInfo['Choose'] == 0 and dMsgInfo['Reason'] == 'PhaseChooseTalentGame' and dMsgInfo['MGID'] not in self.m_NextMGRecord:
            self.m_NextMGRecord.append(dMsgInfo['MGID'])
            self.m_NextTimes[oHero.m_PlayerID] += 1

    
    def RewardWarCash(self, oHero, dMsgInfo):
        oSurvivor = self.m_Survivor
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iWarGSCash = cl_formula.GetFormulaResult(self, dPhaseInfo[oSurvivor.m_Phase]['WarGSCash'])
        oHero.AddGSCash(iWarGSCash, 'phasereward%s' % oSurvivor.m_Phase)
        if 'NoReWard' in dMsgInfo:
            return None
        (sBaseCash, sExtraCash) = dPhaseInfo[oSurvivor.m_Phase]['WarCash']
        iBaseCash = cl_formula.GetFormulaResult(self, sBaseCash)
        iExtraCash = cl_formula.GetFormulaResult(self, sExtraCash) if oSurvivor.IsPreKillAllMonster() else 0
        iWarCash = iBaseCash + iExtraCash
        oHero.AddCash(iWarCash, 'phasereward%s' % oSurvivor.m_Phase)

    
    def GetTalentMG(self):
        return self.m_MiniGame['TalentMG']

    
    def ValidReward(self, iPlayerID):
        iRemainTimes = self.m_RemainTimes[iPlayerID] if iPlayerID in self.m_RemainTimes else 0
        if iRemainTimes <= 0:
            return 0
        return 1

    
    def ConsumeTimes(self, iPlayerID, iCount):
        self.m_RemainTimes[iPlayerID] -= iCount
        self.GS2CPhaseGoldenCount(iPlayerID)



def NewSurvivorRewardMgr(oSurvivorElement, oData):
    oSurvivorRewardMgr = CSurvivorRewardMgr(oSurvivorElement, oData)
    oSurvivorRewardMgr.Init()
    return oSurvivorRewardMgr

