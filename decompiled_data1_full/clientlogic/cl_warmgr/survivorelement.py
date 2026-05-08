# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivorelement.pyc
# RelativePath: clientlogic/cl_warmgr/survivorelement.pyc
# Source Generated with Decompyle++
# File: survivorelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_only import Time2Frame, ChooseKey, PY_FLAG_DEAD, SendAlert, GAME_FRAME, DeepCopy, Frame2Time, Functor
from cl_object.logging import SurvivorLog
from cl_commondefines import NWARRIOR_NPC_RAREGOLDENCUP, WARRIOR_HERO, WARRIOR_ELITE, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, DAM_TYPE_TRUE, DAM_USE_HP, WARRIOR_MONSTER, MONSTER_TYPE_MASK, SETTLE_FINISHWAR, VIRTUAL_ITEM_WARCASH, WARRIOR_NORMAL, WARRIOR_BOSS, LEVEL_STATE_PREPARE, LEVEL_STATE_FIGHT, LEVEL_STATE_FINISH, PLAY_TYPE_SINGLE
from cl_commondefines import STATE_CHOOSEREWARD, STATE_TIME_FOREVER, VOTE_TYPE_SURVIVOR, STATE_UNDER_ATTACK, STATE_CLS_ABNORMAL, SURVIVOR_PLAY, NPCMGR_SURVIVOR
from cl_warmgr.survivor import fighttimemgr
from cl_warmgr.survivor import connecttransfernpcctrl
from cl_warmgr.survivor import survivorbornctrl
from cl_warmgr.survivor import survivorupgrademgr
from cl_warmgr.survivor import npcrefreshmgr
from cl_warmgr.survivor import survivormonstersupermgr
from cl_warmgr.survivor import survivorchallenge
from cl_warmgr.survivor import survivorrareitemmgr
from cl_warmgr.survivor import sparemonstermgr
from cl_warmgr.survivor import survivortrapmgr
from cl_warmgr.bigdataanalyse import CPhaseClgAnalyseCom, CRareItemAnalyseCom
from cl_npc.net import GS2CVoteStat
import cl_msgcenter
import cl_notify
import cl_formula
import cl_object
import math
import cl_snetwar
import cl_state
import cl_phasechallenge
import cllib.lib_flag as lib_flag
import types
IDX_GSCASH = 1
IDX_CNT = 0
STATE_ADD_FRAME = GAME_FRAME * 3600
g_MonsterType = {
    WARRIOR_BOSS: 'Boss',
    WARRIOR_ELITE: 'Elite',
    WARRIOR_NORMAL: 'Normal' }

class CSurvivorElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CSurvivorElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'SurvivorElement'
        self.m_PhaseConfig = oData.m_PhaseConfig
        self.m_LevelMap = oData.m_LevelMap
        self.m_NpcConfigMap = oData.m_NpcConfigMap
        self.m_MonsterPower = oData.m_MonsterPower
        self.m_DropSurvivalTime = oData.m_DropSurvivalTime
        self.m_PreSecondGSCash = oData.m_PreSecondGSCash
        self.m_MaxGSCashSecond = oData.m_MaxGSCashSecond
        self.m_RefreshGroupMap = oData.m_RefreshGroupMap
        self.m_RareItemConfigMap = oData.m_RareItemConfigMap
        self.m_TrapConfigMap = oData.m_TrapConfigMap
        self.m_SectorSpawn = oData.m_SectorSpawn
        self.m_ConfigSID = 0
        self.m_MonsterRange = (0, 0, 0, 0)
        self.m_Phase = 0
        self.m_MaxPhase = 0
        self.m_PhaseStartFrame = 0
        self.m_SuspendableCallOut = { }
        self.m_CallCout = { }
        self.m_CallCoutRemoveFlag = { }
        self.m_MonsterBornPos = []
        self.m_CurLine = None
        self.m_LevelState = 0
        self.m_WeaponGrade = oData.m_WeaponGrade
        self.m_InscriptionNum = oData.m_InscriptionNum
        self.m_RareTalentInfo = oData.m_Config.get('m_RareTalentInfo', { })
        self.m_RareCupDropPhase = oData.m_Config.get('m_RareCupDropPhase', [])
        self.m_InitPerform = oData.m_Config.get('m_InitPerform', { })
        self.m_InscriptionConfig = oData.m_Config.get('InscriptionConfig', { })
        self.m_PhaseNotifyInfo = oData.m_PhaseNotifyInfo
        self.m_HeroRareCupRefresh = { }
        self.m_TransferCtrl = connecttransfernpcctrl.NewConnectTransferNpcCtrl(self.m_Game)
        self.m_BornCtrl = survivorbornctrl.NewSurvivorBornManager(self, oData)
        self.m_UpgradeMgr = survivorupgrademgr.NewSurvivorUpgradeMgr(self, oData)
        self.m_FightTimerMgr = fighttimemgr.NewFightTimeManager(self)
        self.m_NpcRefreshMgr = npcrefreshmgr.NewNpcRefreshMgr(self, oData, NPCMGR_SURVIVOR)
        self.m_SuperMonsterMgr = survivormonstersupermgr.NewSurvivorMonsterSuperMgr(self, oData)
        self.m_PhaseChallengeMgr = cl_phasechallenge.NewPhaseChallengeMgr(self)
        self.m_RareItemMgr = survivorrareitemmgr.NewSurvivorRareItemMgr(self, oData)
        self.m_SpareMonsterMgr = sparemonstermgr.NewSpareMonsterMgr(self)
        self.m_TrapMgr = survivortrapmgr.NewSurvivorTrapMgr(self)
        self.m_ExtGSCashInfo = { }
        self.m_RareCupInteractRecord = {
            'Finish': 0,
            'Record': { } }
        self.m_EliteChallenge = None
        self.m_ChooseRewardUpdateFrame = { }
        self.m_ChooseRewardWudiState = { }
        self.m_StateTime = { }
        self.m_RestFlag = False
        self.m_PrepareOverFrame = 0
        for sType in g_MonsterType.values():
            self.m_ExtGSCashInfo[sType] = [
                0,
                0]
        
        self.m_CurTokenCost = { }
        self.m_Pause = False
        self.m_ExecFunc = []

    
    def Init(self):
        self.m_UpgradeMgr.Init()
        oGame = self.m_Game
        oGame.m_WarMgr.Set('AdditionalGemini', self.m_InscriptionConfig.get('AdditionalGemini', 0))
        oGame.m_WarMgr.Set('ExclusiveInscription', self.m_InscriptionConfig.get('ExclusiveInscription', 0))
        cl_msgcenter.AddFunction(oGame.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInitPlayer, self.m_CallFlag, -1, 0)
        cl_msgcenter.AddAttentionFunc(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.OnGetWeaponGrade, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_INSCRIPTIONNUM, self.OnGetInscriptionNum, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOK, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GREATEWEAPON, self.OnCreateWeapon, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_SURVIVOR_HANDLE_RELIC, self.OnHandleRelic, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROP, self.OnDrop, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREDROPCASH, self.OnBeforeDropCash, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, self.OnTalentChoose, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATERAREGOLDENCUP, self.OnCreateRareGoldenCup, self.m_CallFlag)

    
    def InitAfter(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.OnLevelCtrlInit, self.m_CallFlag)
        oBigdataMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oPhaseClgCom = CPhaseClgAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('PhaseClg', oPhaseClgCom)
            oRareItemCom = CRareItemAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('RareItem', oRareItemCom)

    
    def Release(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oGame.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oGame.m_WarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'SurvivorPrepareVote')
        cl_msgcenter.DoneAttention(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_INSCRIPTIONNUM, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GREATEWEAPON, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_SURVIVOR_HANDLE_RELIC, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROP, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREDROPCASH, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATERAREGOLDENCUP, self.m_CallFlag)
        for iHero in oGame.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIEDIST, 'SurvivorPrepareVote')
        
        self.m_PhaseChallengeMgr.Release()
        self.m_TransferCtrl.Release()
        self.m_BornCtrl.Release()
        self.m_UpgradeMgr.Release()
        self.m_FightTimerMgr.Release()
        self.m_NpcRefreshMgr.Release()
        self.m_SuperMonsterMgr.Release()
        self.m_RareItemMgr.Release()
        self.m_TrapMgr.Release()
        if self.m_EliteChallenge:
            self.m_EliteChallenge.Release()
            self.m_EliteChallenge = None
        self.m_SpareMonsterMgr.Release()
        super(CSurvivorElement, self).Release()
        self.m_SuspendableCallOut = { }
        self.m_CallCout = { }
        self.m_CallCoutRemoveFlag = { }
        self.m_RareCupInteractRecord = { }
        self.m_ChooseRewardUpdateFrame = { }
        self.m_ChooseRewardWudiState = { }
        self.m_ExecFunc = []
        self.m_CurLine = None
        self.m_TransferCtrl = None
        self.m_BornCtrl = None
        self.m_UpgradeMgr = None
        self.m_FightTimerMgr = None
        self.m_NpcRefreshMgr = None
        self.m_SuperMonsterMgr = None
        self.m_PhaseChallengeMgr = None
        self.m_RareItemMgr = None
        self.m_TrapMgr = None

    
    def Save(self):
        dData = { }
        dData['FT'] = self.m_FightTimerMgr.Save()
        dData['GSC'] = self.m_ExtGSCashInfo
        dData['PHA'] = self.m_Phase
        dData['RCIR'] = self.m_RareCupInteractRecord
        dData['PCM'] = self.m_PhaseChallengeMgr.Save()
        dData['Hinder'] = self.m_Game.m_WarMgr.Query('SurvivorHinder', [])
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_FightTimerMgr.Load(dData['FT'])
        self.m_ExtGSCashInfo = dData['GSC']
        self.m_Phase = dData['PHA']
        self.m_RareCupInteractRecord = dData['RCIR']
        if 'PCM' in dData:
            self.m_PhaseChallengeMgr.Load(dData['PCM'])
        if not dData['Hinder']:
            return None
        self.m_Game.m_WarMgr.Set('SurvivorHinder', dData['Hinder'])

    
    def OnAddAllPlayer(self, oTarget, oWarMgr, dInfo):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetRoomHero():
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_CallFlag)
        

    
    def OnPlayerMapLoadOK(self, oWarMgr, oTarget, dInfo):
        iCurFrame = self.m_Game.GetFrameNum()
        self.CloseChooseReward(oTarget, iCurFrame)
        self.RefreshClientPhaseInfo(oWarMgr, oTarget)
        self.RefreshPrepareInfo(oWarMgr, oTarget, iCurFrame)
        self.InitPerform(dInfo)

    
    def RefreshPrepareInfo(self, oWarMgr, oTarget, iCurFrame):
        if iCurFrame < self.m_PrepareOverFrame and self.m_Phase in self.m_PhaseConfig[self.m_ConfigSID]:
            iFrame = self.GetPhaseFrameByIndex(1)
            if not iFrame:
                return None
            iTime = Frame2Time(iFrame)
            dPlayer = {
                oTarget.m_PlayerID: 1 }
            iRemainTime = Frame2Time(self.m_PrepareOverFrame - iCurFrame)
            cl_snetwar.GS2CPrepareTimeInfo(dPlayer, iRemainTime, iTime)
            GS2CVoteStat(self.m_Game, oWarMgr.Query('VoteStatus', { }), VOTE_TYPE_SURVIVOR)

    
    def RefreshClientPhaseInfo(self, oWarMgr, oTarget):
        if not self.m_Phase:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
            return None
        iIsFinish = 0
        if not self.m_Phase > self.m_MaxPhase:
            iFrame = self.GetPhaseFrameByIndex(0)
            if iFrame == 0 and not (self.m_EliteChallenge):
                iIsFinish = 1
        cl_snetwar.GS2CPhaseInfo({
            oTarget.m_PlayerID: 1 }, self.m_Phase, iIsFinish)

    
    def OnCreateRareGoldenCup(self, oWarMgr, oTarget, dInfo):
        iNpcID = dInfo['NPC']
        self.m_RareCupInteractRecord['Record'][iNpcID] = { }
        oNpc = self.m_Game.GetObject(iNpcID)
        for iPlayer in self.m_Game.m_WarMgr.GetRoomPlayer():
            if not oNpc.IsVisibleTo(iPlayer):
                self.m_RareCupInteractRecord['Record'][iNpcID][iPlayer] = 1
        

    
    def OnTalentChoose(self, oWarMgr, oTarget, dInfo):
        iNpcID = dInfo['NpcID']
        oGame = self.m_Game
        oNpc = oGame.GetObject(iNpcID)
        if oNpc and oNpc.m_FightType == NWARRIOR_NPC_RAREGOLDENCUP:
            self.m_RareCupInteractRecord['Record'][iNpcID][oTarget.m_PlayerID] = 1

    
    def OnLevelNodeInit(self, oWarMgr, oTarget, dInfo):
        if dInfo['LevelType'] == LEVEL_TYPE_FIGHT:
            iLevel = dInfo['LevelID']
            if iLevel not in self.m_LevelMap:
                SendAlert('err', f'''game:{self.m_Game.m_ID} survivor not exist {iLevel}''')
                return None
            self.m_ConfigSID = self.m_LevelMap[iLevel]
            self.m_MaxPhase = len(self.m_PhaseConfig[self.m_ConfigSID])
            oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
            self.m_CurLine = oLevelCtrl.m_CurNode.m_RoomList[0][0]
            self.m_NpcRefreshMgr.InitNpcPos()
            self.m_NpcRefreshMgr.m_SID = self.m_NpcConfigMap[self.m_ConfigSID]
            self.m_BornCtrl.InitHeroBorn()
            self.m_RareItemMgr.m_CurRareItemConfig = self.m_RareItemConfigMap[self.m_ConfigSID]
            self.m_TrapMgr.m_TrapCongfig = self.m_TrapConfigMap[self.m_ConfigSID]
        else:
            self.m_FightTimerMgr.ResumeCounting('SurvivorOver')
            self.m_BornCtrl.m_HeroBorn = []
        self.m_LevelState = LEVEL_STATE_PREPARE

    
    def OnLevelNodeGoalOK(self, oWarMgr, oTarget, dInfo):
        self.m_SuspendableCallOut = { }
        self.m_CallCout = { }
        self.m_LevelState = LEVEL_STATE_FINISH
        if dInfo['LevelType'] == LEVEL_TYPE_BOSS:
            self.m_FightTimerMgr.PauseCounting('BossOver')

    
    def Start(self, oTarget):
        self.m_LevelState = LEVEL_STATE_FIGHT
        oGame = self.m_Game
        if self.m_Phase > self.m_MaxPhase:
            self.DoSurvivorOver()
            return None
        if not (self.m_Phase) or not oGame.m_WarMgr.IsTransferGame():
            self.m_Phase = 1
            dPlayer = self.m_Game.GetRealPlayers()
            cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 0)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASESTART, self, {
                'Phase': self.m_Phase })
        self.m_FightTimerMgr.StartSummary()
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        self.m_MonsterRange = dPhaseInfo[self.m_Phase]['SpawnMonsterRange']
        self.m_MonsterBornPos = self.m_CurLine.m_MonsterCtrl.GetAllMonsterBornPos()
        self.m_CurLine.m_MonsterCtrl.InitAdditionMonsterInfo()
        self.m_CurLine.m_MonsterCtrl.RefreshPreSpawnDir()
        if oGame.m_WarMgr.IsTransferGame():
            self.AddPhase(0)
            return None
        self.m_NpcRefreshMgr.TryNpcRefresh(0)
        self.m_CurLine.m_MonsterCtrl.CreateExpectedNumberMonsters()
        iFrame = self.GetPhaseFrameByIndex(0)
        self.Call_Out_Suspendable(self.PreAddPhase, iFrame, 'PreAddPhase' + self.m_CallFlag)
        iCheckIntervalFrame = self.GetCheckIntervalFrame()
        self.Call_Out_Suspendable(self.CheckMonsterPower, iCheckIntervalFrame, 'CheckMonsterPower' + self.m_CallFlag)

    
    def OnLevelCtrlInit(self, oTarget, oLevelCtrl, dMsgInfo):
        iLayerNum = 1
        iLevelNum = 1
        if lib_flag.g_IsLogicLayer and g_DebugLevel:
            iLevel = g_DebugLevel
        else:
            dExtraInfo = self.m_Game.m_WarMgr.m_ExtraInfo
            iLevel = 0
            if SURVIVOR_PLAY in dExtraInfo:
                iLevel = dExtraInfo[SURVIVOR_PLAY]
            dLayerData = oLevelCtrl.m_LevelCtrlConf[iLayerNum]
            dLevelInfo = dLayerData['CtrlInfo'][iLevelNum]
            tNormal = dLevelInfo['NormalStore']
            if iLevel not in tNormal:
                SurvivorLog.Debug('game:%d error level:%d' % (self.m_Game.m_ID, iLevel))
                iIndex = self.m_Game.Random(len(tNormal))
                iLevel = tNormal[iIndex]
        oLevelCtrl.m_LayerNum = iLayerNum
        oLevelCtrl.m_LevelNum = iLevelNum
        oLevelCtrl.m_DirectLevel = iLevel

    
    def OnDie(self, oWarMgr, oTarget, dInfo):
        self.m_SuperMonsterMgr.OnDie(oTarget)
        if self.m_Phase > self.m_MaxPhase or self.m_Phase == 0:
            return None
        oReason = dInfo['RS'] if 'RS' in dInfo else None
        if oReason and oReason.GetStrReason() == 'SurvivorGoalOK':
            return None
        if oTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            fGSCash = oTarget.m_SurvivorGSCash
            iMonsterType = oTarget.m_FightType & MONSTER_TYPE_MASK
            if iMonsterType in g_MonsterType:
                sType = g_MonsterType[iMonsterType]
                self.m_ExtGSCashInfo[sType][IDX_CNT] += 1
                self.m_ExtGSCashInfo[sType][IDX_GSCASH] += fGSCash
        if oTarget.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            self.CheckAllDiePause()

    
    def OnInitPlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        if iHero not in self.m_CurTokenCost:
            self.m_CurTokenCost[iHero] = 0

    
    def InitPerform(self, dInfo):
        if self.m_ConfigSID not in self.m_InitPerform:
            return None
        iHero = dInfo['Hero']
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        for iPerform in self.m_InitPerform[self.m_ConfigSID]:
            oHero.AddPerform(iPerform, 1)
        

    
    def OnRemovePlayer(self, oWarMgr, oTarget, dInfo):
        oWarMgr.RefreshPlayerCnt()
        self.CheckAllDiePause()

    
    def ValidSetInfo(self, oNpc, oHero):
        if not oNpc:
            return False
        if oNpc.m_FightType != NWARRIOR_NPC_RAREGOLDENCUP:
            return False
        if oNpc.GetMaxRefreshTimes(oHero):
            return False
        return True

    
    def OnInteract(self, oWarMgr, oTarget, dInfo):
        iNpc = dInfo['NPC']
        oGame = self.m_Game
        oNpc = oGame.GetObject(iNpc)
        oHero = oGame.GetObject(dInfo['Hero'])
        if self.ValidSetInfo(oNpc, oHero):
            oNpc.SetRefreshCost(self.m_RareTalentInfo['RefreshCost'])
            oNpc.SetMaxRefreshTimes(self.m_RareTalentInfo['RefreshMaxTimes'], dInfo['Hero'])

    
    def OnRelife(self, oSurvivor, oTarget, dInfo):
        oWarMgr = self.m_Game.m_WarMgr
        self.m_Pause = False
        iCurFrame = self.m_Game.GetFrameNum()
        self.RefreshPrepareInfo(oWarMgr, oTarget, iCurFrame)
        self.m_FightTimerMgr.ResumeCounting('Alldie')
        if self.m_CallCout:
            self.RestoreCallOut(self.m_CallCout)
            self.m_CallCout = { }
        self.ExecFunc()

    
    def OnCreateWeapon(self, oWarMgr, oTarget, dInfo):
        oWeapon = dInfo['Weapon']
        oWeapon.Set('SurvivorPhase', self.m_Phase)

    
    def OnHandleRelic(self, oWarMgr, oTarget, dInfo):
        if 'Operate' not in dInfo:
            return None
        sOperate = dInfo['Operate']
        if sOperate == 'DropRelic':
            if 'Hero' not in dInfo or 'Relic' not in dInfo or 'StaticInfo' not in dInfo:
                return None
            oHero = self.m_Game.GetObject(dInfo['Hero'])
            if not oHero:
                return None
            oRelic = oHero.m_RelicCon.GetPerform(dInfo['Relic'])
            iSurvivorPhase = oRelic.GetArgValue('SurvivorPhase')
            if iSurvivorPhase:
                dStaticInfo = dInfo['StaticInfo']
                dStaticInfo['SurvivorPhase'] = iSurvivorPhase
            return None
        if sOperate == 'SetDropData':
            if 'Drop' not in dInfo or 'StaticInfo' not in dInfo:
                return None
            oDrop = self.m_Game.GetObject(dInfo['Drop'])
            if not oDrop:
                return None
            dStaticInfo = dInfo['StaticInfo']
            if 'SurvivorPhase' in dStaticInfo:
                oDrop.Set('SurvivorPhase', dStaticInfo['SurvivorPhase'])
            return None
        if sOperate == 'PickRelic':
            if 'Relic' not in dInfo or 'Drop' not in dInfo:
                return None
            oHero = self.m_Game.GetObject(dInfo['Hero'])
            oDrop = self.m_Game.GetObject(dInfo['Drop'])
            if not oHero or not oDrop:
                return None
            iPhase = oDrop.Query('SurvivorPhase', 0)
            if not iPhase:
                return None
            oRelic = oHero.m_RelicCon.GetPerform(dInfo['Relic'])
            if not oRelic:
                return None
            oRelic.SetArgValue('SurvivorPhase', iPhase)

    
    def OnDrop(self, oWarMgr, oTarget, dInfo):
        if 'Drop' not in dInfo or 'Type' not in dInfo:
            return None
        iFightType = dInfo['Type']
        if iFightType not in self.m_DropSurvivalTime:
            return None
        oDrop = self.m_Game.GetObject(dInfo['Drop'])
        if not oDrop:
            return None
        iTime = self.m_DropSurvivalTime[iFightType]
        oDrop.ResetDisappearTime(iTime)

    
    def OnBeforeDropCash(self, oWarMgr, oTarget, dInfo):
        if not oTarget or oTarget.IsDeadNoDying():
            dInfo['Reward'] = []
            return None
        iCash = sum(dInfo['CashList'])
        dInfo['Reward'] = [
            {
                'item': VIRTUAL_ITEM_WARCASH,
                'info': {
                    'amount': iCash,
                    'sendmsg': 1 } }]

    
    def OnEliteChallengeOver(self):
        if not self.m_EliteChallenge:
            return None
        self.m_EliteChallenge.Release()
        self.m_EliteChallenge = None
        dPlayer = self.m_Game.GetRealPlayers()
        cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 1)

    
    def GetPhaseInfo(self):
        return self.m_PhaseConfig[self.m_ConfigSID]

    
    def PreAddPhase(self):
        self.Remove_Call_Out_Suspendable('PreAddPhase' + self.m_CallFlag)
        self.Remove_Call_Out_Suspendable('CheckMonsterPower' + self.m_CallFlag)
        
        try:
            iFrame = self.GetPhaseFrameByIndex(1)
        except:
            SurvivorLog.Debug('game:%d phase%s error' % (self.m_Game.m_ID, self.m_Phase))
            return None

        if iFrame or self.m_Phase == self.m_MaxPhase:
            self.IntervalPhaseBigData()
            self.m_TrapMgr.StopAllTrap()
        if iFrame:
            self.m_RestFlag = True
            self.m_FightTimerMgr.PauseCounting('RestTime')
            self.m_NpcRefreshMgr.TryNpcRefresh(1)
            self.Call_Out_Suspendable(self.AddPhase, iFrame, 'AddPhase' + self.m_CallFlag)
            self.m_PrepareOverFrame = self.m_Game.GetFrameNum() + iFrame
            dPlayer = self.m_Game.GetRealPlayers()
            if not self.IsEliteChallengePhase():
                cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 1)
            self.StartPrepareVote()
        else:
            self.AddPhase()

    
    def IntervalPhaseBigData(self):
        oBigDataAnaMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        oMonsterCom = oBigDataAnaMgr.GetCom('Monster')
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            dIntervalPhaseBigData = { }
            dPhsaeMonsterInfo = oMonsterCom.GetPhaseStatistics(oHero.m_PlayerID, self.m_Phase)
            dIntervalPhaseBigData['Phase'] = self.m_Phase
            dIntervalPhaseBigData['MonsterIntervalPhase'] = dPhsaeMonsterInfo
            self.m_Game.m_WarMgr.SendIntervalPhaseBigData(oHero.m_PlayerID, self.m_Phase, dIntervalPhaseBigData)
        

    
    def AddPhase(self, iPhase = 1):
        self.Remove_Call_Out_Suspendable('AddPhase' + self.m_CallFlag)
        self.m_RestFlag = False
        iRestFrame = self.GetPhaseFrameByIndex(1)
        if iRestFrame:
            self.StopPrepareVote()
            self.m_FightTimerMgr.ResumeCounting('RestTime')
        if self.IsEliteChallengePhase():
            self.m_FightTimerMgr.ResumeCounting('ElitePhase')
        self.m_Phase += iPhase
        if iPhase == 0:
            iPlayFrame = self.m_FightTimerMgr.GetPlayFrame()
            iTotalFrame = 0
            dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
            for iTempPhase in range(1, self.m_Phase):
                iPhaseTime = cl_formula.GetFormulaResult(self, dPhaseInfo[iTempPhase]['PhaseTime'][0])
                iFrame = Time2Frame(iPhaseTime)
                iTotalFrame += iFrame
            
            self.m_PhaseStartFrame = self.m_Game.GetFrameNum() - iPlayFrame - iTotalFrame
        else:
            self.m_PhaseStartFrame = self.m_Game.GetFrameNum()
        dInfo = {
            'Phase': self.m_Phase }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASESTART, self, dInfo)
        dPlayer = self.m_Game.GetRealPlayers()
        cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 0)
        SurvivorLog.Debug('game:%d addphase:%d' % (self.m_Game.m_ID, self.m_Phase))
        if self.m_Phase > self.m_MaxPhase:
            self.DoSurvivorOver()
            return None
        DebugMsg(self)
        self.m_NpcRefreshMgr.TryNpcRefresh(0)
        self.CheckPhaseNotify()
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        self.m_MonsterRange = dPhaseInfo[self.m_Phase]['SpawnMonsterRange']
        iFrame = self.GetPhaseFrameByIndex(0)
        if iFrame == 0:
            self.PhaseEndBigData()
            self.Remove_Call_Out_Suspendable('CheckMonsterPower' + self.m_CallFlag)
            self.m_EliteChallenge = survivorchallenge.NewEliteChallenge(self)
            self.m_EliteChallenge.StartChallenge()
            return None
        self.Call_Out_Suspendable(self.PreAddPhase, iFrame, 'PreAddPhase' + self.m_CallFlag)
        iCheckIntervalFrame = self.GetCheckIntervalFrame()
        self.Call_Out_Suspendable(self.CheckMonsterPower, iCheckIntervalFrame, 'CheckMonsterPower' + self.m_CallFlag)

    
    def PhaseEndBigData(self):
        oUpGradeMgr = self.m_UpgradeMgr
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            (iExperience, iGrade, _, _, _, _) = oUpGradeMgr.m_HeroUpgradeInfo[oHero.m_ID]
            self.m_Game.m_WarMgr.HandlePhaseEndReport(oHero.m_PlayerID, self.m_Phase - 1, iGrade, iExperience)
        

    
    def CheckPhaseNotify(self):
        if self.m_Phase not in self.m_PhaseNotifyInfo:
            return None
        (iNotify, iNotifyTime) = self.m_PhaseNotifyInfo[self.m_Phase]
        if iNotifyTime < 0:
            return None
        cl_notify.SendCommonNotify(self.m_Game, self.m_Game.GetRealPlayers(), iNotify, {
            '$time': str(iNotifyTime) })

    
    def CheckMonsterPower(self):
        if self.m_Phase > self.m_MaxPhase:
            return None
        if self.IsEliteChallengePhase():
            SurvivorLog.Debug('game:%d elitechallenge error %s' % (self.m_Game.m_ID, self.m_SuspendableCallOut))
            return None
        DebugMsg(self)
        self.Remove_Call_Out_Suspendable('CheckMonsterPower' + self.m_CallFlag)
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        iCheckIntervalFrame = self.GetCheckIntervalFrame()
        self.Call_Out_Suspendable(self.CheckMonsterPower, iCheckIntervalFrame, 'CheckMonsterPower' + self.m_CallFlag)
        iTriggerNumber = cl_formula.GetFormulaResult(self, dPhaseInfo[self.m_Phase]['TriggerNumber'])
        self.m_CurLine.m_MonsterCtrl.CheckMonsterPower(iTriggerNumber, self.m_MonsterPower, dPhaseInfo[self.m_Phase]['MonsterWeight'])

    
    def Call_Out_Suspendable(self, func, iDelay, sFlag):
        if iDelay < 1:
            SurvivorLog.Error('%s delay is %d' % (sFlag, iDelay))
            iDelay = 1
        if self.m_Pause:
            if iDelay in self.m_CallCout:
                lstFunc = self.m_CallCout[iDelay].setdefault(sFlag, [])
                lstFunc.append(func)
            else:
                self.m_CallCout[iDelay] = {
                    sFlag: [
                        func] }
            return None
        iCallFrame = self.m_Game.GetFrameNum() + iDelay
        if iCallFrame in self.m_SuspendableCallOut:
            if sFlag in self.m_SuspendableCallOut[iCallFrame]:
                oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
                SendAlert('err', 'game:%d %d %d 定时器标记已存在 %s %s' % (self.m_Game.m_ID, oLevelCtrl.m_CurNode.m_Level, self.m_Phase, iCallFrame, sFlag))
            lstFunc = self.m_SuspendableCallOut[iCallFrame].setdefault(sFlag, [])
            lstFunc.append(func)
        else:
            self.m_SuspendableCallOut[iCallFrame] = {
                sFlag: [
                    func] }
            self.m_Game.TimerCall(self.m_ID, self.SuspendableCallBack, iDelay, 'survivor%d' % iCallFrame)

    
    def Remove_Call_Out_Suspendable(self, sFlag):
        lstRemove = []
        self.m_CallCoutRemoveFlag[sFlag] = 1
        for iCallFrame, dCallOut in self.m_SuspendableCallOut.items():
            if sFlag in dCallOut:
                dCallOut.pop(sFlag)
                if not dCallOut:
                    lstRemove.append(iCallFrame)
        
        for iCallFrame in lstRemove:
            self.m_SuspendableCallOut.pop(iCallFrame)
        

    
    def SuspendableCallBack(self):
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame not in self.m_SuspendableCallOut:
            return None
        dCallOut = self.m_SuspendableCallOut.pop(iCurFrame)
        self.m_CallCoutRemoveFlag = { }
        for sFlag, lstFunc in dCallOut.items():
            if sFlag in self.m_CallCoutRemoveFlag:
                continue
            for func in lstFunc:
                func()
                if self.m_LevelState == LEVEL_STATE_FINISH:
                    return None
            
        

    
    def SuspendCallOut(self):
        if self.m_CallCout:
            return None
        dAllCallOut = { }
        iCurFrame = self.m_Game.GetFrameNum()
        for iCallFrame, dCall in self.m_SuspendableCallOut.items():
            dAllCallOut[iCallFrame - iCurFrame] = dCall
        
        self.m_SuspendableCallOut = { }
        self.m_CallCout = dAllCallOut
        SurvivorLog.Debug('game:%d callout %s %s' % (self.m_Game.m_ID, self.m_CallCout, iCurFrame))

    
    def RestoreCallOut(self, dAllCallOut):
        self.m_SuspendableCallOut = { }
        iCurFrame = self.m_Game.GetFrameNum()
        SurvivorLog.Debug('game:%d restorecallout %s %s' % (self.m_Game.m_ID, dAllCallOut, iCurFrame))
        for iFrame, dCall in dAllCallOut.items():
            iCallFrame = iCurFrame + iFrame
            self.m_SuspendableCallOut[iCallFrame] = dCall
            if iFrame == 0:
                self.SuspendableCallBack()
                continue
            self.m_Game.TimerCall(self.m_ID, self.SuspendableCallBack, iFrame, 'survivor%d' % iCallFrame)
        

    
    def Exec_Suspendable(self, func):
        if self.m_Pause:
            self.m_ExecFunc.append(func)
        else:
            func()

    
    def ExecFunc(self):
        if not self.m_ExecFunc:
            return None
        lstExecFunc = self.m_ExecFunc
        self.m_ExecFunc = []
        for func in lstExecFunc:
            func()
        

    
    def GetPhaseFrameByIndex(self, iIndex):
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        iPhaseTime = cl_formula.GetFormulaResult(self, dPhaseInfo[self.m_Phase]['PhaseTime'][iIndex])
        iFrame = Time2Frame(iPhaseTime)
        return iFrame

    
    def GetMaxDamageTarget(self):
        oGame = self.m_Game
        oReport = oGame.m_WarMgr.GetComponent('Warreport')
        lstDamage = oReport.GetTotalDamage()
        dHeroDamage = { }
        iMaxDamage = 1
        for _, iDamage in lstDamage:
            if iMaxDamage < iDamage:
                iMaxDamage = iDamage
        
        for iHero, iDamage in lstDamage:
            oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
            if not oHero:
                continue
            dHeroDamage[iHero] = int((iDamage / iMaxDamage) * 10000)
        
        iTargetHero = 0
        if dHeroDamage:
            iTargetHero = ChooseKey(self.m_Game, dHeroDamage)
        if not iTargetHero:
            lstHero = oGame.m_WarMgr.GetLiveHero()
            if not lstHero:
                return None
            iLen = len(lstHero)
            idx = oGame.Random(iLen)
            iTargetHero = lstHero[idx]
        oTarget = oGame.GetObject(iTargetHero)
        return oTarget

    
    def OnGetWeaponGrade(self, oWarMgr, oTarget, dInfo):
        dInfo['Grade'] = self.GetWeaponGrade()

    
    def OnGetInscriptionNum(self, oWarMgr, oTarget, dInfo):
        dInfo['InscriptionNum'] = self.GetInscriptionNum()

    
    def GetWeaponGrade(self, dData = None):
        iGrade = cl_formula.GetFormulaResult(self, self.m_WeaponGrade, dData)
        if iGrade < 0:
            iGrade = 0
        return iGrade

    
    def GetInscriptionNum(self, iPhase = 0):
        iCurPhase = iPhase if iPhase else self.m_Phase
        iResult = 0
        for iPhase in sorted(self.m_InscriptionNum):
            if iPhase > iCurPhase:
                break
            iResult = self.m_InscriptionNum[iPhase]
        
        return iResult

    
    def GetMonsterAttrAdjust(self, iType):
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        if self.m_Phase not in dPhaseInfo:
            return []
        if iType & WARRIOR_ELITE == WARRIOR_ELITE:
            return dPhaseInfo[self.m_Phase]['EliteAttr']
        return dPhaseInfo[self.m_Phase]['NormalAttr']

    
    def SceneMonsterAllDie(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        iScene = oLevelCtrl.m_CurNode.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oReason = cl_object.reason.CStrReason('SurvivorGoalOK', None, {
            'DamType': DAM_TYPE_TRUE | DAM_USE_HP })
        for iMonsterSID in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonsterSID, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oMonster.HPModifyDam(0, [
                [
                    oMonster.HP(),
                    oReason]])
        
        self.EndUnderAttack(oScene)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMGOAL, oLevelCtrl, {
            'Room': 0,
            'Level': oLevelCtrl.m_CurNode.m_Level,
            'oScene': oScene })

    
    def EndUnderAttack(self, oScene):
        for iHero in oScene.GetHeros():
            oHero = self.m_Game.GetObject(iHero)
            cl_state.RemoveState(oHero, STATE_UNDER_ATTACK)
        

    
    def GetCheckIntervalFrame(self):
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        iCnt = self.m_Game.m_WarMgr.GetAllPlayerCnt()
        return Time2Frame(dPhaseInfo[self.m_Phase]['CheckInterval'][iCnt])

    
    def IsEliteChallengePhase(self):
        iFrame = self.GetPhaseFrameByIndex(0)
        return iFrame == 0

    
    def GetExtGSCashInfo(self):
        dReportInfo = { }
        for sType, lstInfo in self.m_ExtGSCashInfo.items():
            dReportInfo[sType] = (lstInfo[IDX_CNT], math.ceil(lstInfo[IDX_GSCASH]))
        
        iPlaySecond = self.m_FightTimerMgr.GetPlayFrame() // GAME_FRAME
        iRewardSecond = iPlaySecond if iPlaySecond <= self.m_MaxGSCashSecond else self.m_MaxGSCashSecond
        dReportInfo['PlayTime'] = (iPlaySecond, math.ceil(self.m_PreSecondGSCash * iRewardSecond))
        return dReportInfo

    
    def GetExtGSCash(self, iType):
        if iType == SETTLE_FINISHWAR:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl and not oLevelCtrl.CheckFinishWar():
                return 0
        dReportInfo = self.GetExtGSCashInfo()
        iExtGSCach = 0
        for lstInfo in dReportInfo.values():
            iExtGSCach += lstInfo[IDX_GSCASH]
        
        return iExtGSCach

    
    def CheckAllDiePause(self):
        bSuspend = True
        for iHeroID in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHeroID)
            if not oHero:
                continue
            if oHero.IsDead():
                continue
            bSuspend = False
        
        if bSuspend:
            self.m_Pause = True
            self.m_FightTimerMgr.PauseCounting('Alldie')
            self.SuspendCallOut()

    
    def DoSurvivorOver(self):
        self.InitGoalPos()
        self.m_FightTimerMgr.PauseCounting('SurvivorOver')
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelCtrl.m_CurNode.LevelGoal({ })
        self.SceneMonsterAllDie()
        self.m_PhaseChallengeMgr.OnSurvivorOver()

    
    def InitGoalPos(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iLevel = oLevelCtrl.m_CurNode.m_Level
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        oMiniMap.m_LevelGoalPos.Init()

    
    def OpenChooseReward(self, oHero, iFrame):
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        SurvivorLog.Debug('game:%d openchoose %s %s %s' % (oGame.m_ID, iFrame, oHero.m_PlayerID, iCurFrame))
        self.m_ChooseRewardUpdateFrame[oHero.m_ID] = iCurFrame
        func = Functor(self.CheckChooseRewardStatus, oHero.m_ID)
        sCallFlag = 'CheckStatus' + str(oHero.m_ID)
        self.Call_Out(func, GAME_FRAME * 15, sCallFlag)
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason('ChooseReward'),
            'arg': { } }
        oState = cl_state.AddState(oHero, STATE_CHOOSEREWARD, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(oHero)
            self.m_ChooseRewardWudiState[oHero.m_ID] = oState.m_ID
        pfobj = oHero.GetCareerPerform()
        iPerform = pfobj.m_SID
        oHero.m_Perform.PauseColdDown(iPerform, 0)
        oHero.StopShieldRecover('SurvivorChooseReward')
        oHero.StopEnergyRecover('SurvivorChooseReward')
        self.m_StateTime[oHero.m_ID] = { }
        for oState in oHero.m_State.Values():
            if oState.m_TimeType == STATE_TIME_FOREVER:
                continue
            if oState.m_Type != STATE_CLS_ABNORMAL:
                continue
            iStateRemainFrame = oState.GetRemainTime()
            if iStateRemainFrame <= 0:
                continue
            oState.SetTime(oHero, STATE_ADD_FRAME, 0, iRefresh = 0)
            self.m_StateTime[oHero.m_ID][oState.m_ID] = iStateRemainFrame
        
        oHero.IsNeglectAttack = types.MethodType(ReplaceIsNeglectAttack, oHero)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnClearFuncBinding, 'ReplaceIsNeglectAttack')
        oRescueElement = oGame.m_WarMgr.GetComponent('RescueElement')
        if not oRescueElement:
            return None
        oRescueElement.HaltRescue(oHero, { })

    
    def CloseChooseReward(self, oHero, iFrame):
        SurvivorLog.Debug('game:%d closechoose %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iFrame))
        sCallFlag = 'CheckStatus' + str(oHero.m_ID)
        self.Remove_Call_Out(sCallFlag)
        if oHero.m_ID not in self.m_ChooseRewardWudiState:
            return None
        oState = oHero.m_State.GetItem(self.m_ChooseRewardWudiState[oHero.m_ID])
        self.m_ChooseRewardWudiState.pop(oHero.m_ID)
        if oState:
            oHero.m_State.RemoveItem(oState.m_ID)
        pfobj = oHero.GetCareerPerform()
        iPerform = pfobj.m_SID
        oHero.m_Perform.ReStartColdDown(iPerform, 0)
        oHero.StartShieldRecover('SurvivorChooseReward')
        oHero.StartEnergyRecover('SurvivorChooseReward')
        if 'IsNeglectAttack' in oHero.__dict__:
            del oHero.IsNeglectAttack
        if oHero.m_ID not in self.m_StateTime:
            return None
        for iStateID, iStateRemainFrame in self.m_StateTime[oHero.m_ID].items():
            oState = oHero.m_State.GetItem(iStateID)
            if not oState:
                continue
            oState.SetTime(oHero, iStateRemainFrame, 0, iRefresh = 0)
        

    
    def CheckChooseRewardStatus(self, iHeroID):
        oHero = self.m_Game.GetObject(iHeroID)
        if not oHero:
            return None
        if iHeroID not in self.m_ChooseRewardUpdateFrame:
            return None
        iCurFrame = self.m_Game.GetFrameNum()
        sCallFlag = 'CheckStatus' + str(iHeroID)
        if iCurFrame - self.m_ChooseRewardUpdateFrame[iHeroID] >= GAME_FRAME * 15:
            SurvivorLog.Debug('game:%d closeovertime %s' % (self.m_Game.m_ID, oHero.m_PlayerID))
            self.CloseChooseReward(oHero, iCurFrame)
            self.Remove_Call_Out(sCallFlag)
        else:
            func = Functor(self.CheckChooseRewardStatus, iHeroID)
            self.Call_Out(func, GAME_FRAME * 15, sCallFlag)

    
    def OnClearFuncBinding(self, oWarMgr, oTarget, dInfo):
        iHeroID = dInfo['Hero']
        if iHeroID not in self.m_ChooseRewardUpdateFrame:
            return None
        oHero = self.m_Game.GetObject(iHeroID)
        if not oHero:
            return None
        if 'IsNeglectAttack' in oHero.__dict__:
            del oHero.IsNeglectAttack
        sCallFlag = 'CheckStatus' + str(iHeroID)
        self.Remove_Call_Out(sCallFlag)

    
    def StartPrepareVote(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oWarMgr.Set('VoteStatus', { })
        dPlayer = oGame.GetRealPlayers()
        iFrame = self.GetPhaseFrameByIndex(1)
        iTime = Frame2Time(iFrame)
        cl_snetwar.GS2CPrepareTimeInfo(dPlayer, iTime, iTime)
        self.Call_Out(self.TimedRefreshPrepareInfo, GAME_FRAME * 10, 'TimedRefreshPrepareInfo')
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemoveVotePlayer, 'SurvivorPrepareVote', iOnce = 0)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnHeroDiedist, 'SurvivorPrepareVote')
        

    
    def StopPrepareVote(self):
        oWarMgr = self.m_Game.m_WarMgr
        self.Remove_Call_Out('TimedRefreshPrepareInfo')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'SurvivorPrepareVote')
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIEDIST, 'SurvivorPrepareVote')
        

    
    def TimedRefreshPrepareInfo(self):
        self.Remove_Call_Out('TimedRefreshPrepareInfo')
        self.Call_Out(self.TimedRefreshPrepareInfo, GAME_FRAME * 10, 'TimedRefreshPrepareInfo')
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        oWarMgr = oGame.m_WarMgr
        for iHero in oWarMgr.GetRoomHero():
            oTarget = oGame.GetObject(iHero)
            if not oTarget:
                continue
            self.RefreshPrepareInfo(oWarMgr, oTarget, iCurFrame)
        

    
    def UpdateVoteStatus(self, oHero, iStatus):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        if not self.m_RestFlag:
            return None
        dStat = oWarMgr.SetDefault('VoteStatus', { })
        dStat[oHero.m_PlayerID] = iStatus
        GS2CVoteStat(oGame, dStat, VOTE_TYPE_SURVIVOR)
        lstPlayer = oGame.m_WarMgr.GetLivePlayer()
        SurvivorLog.Debug('game:%s votestatus %s %s %s %s' % (oGame, oHero.m_PlayerID, iStatus, dStat, lstPlayer))
        self.TrySkipRestPhase()

    
    def TrySkipRestPhase(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dStat = oWarMgr.Query('VoteStatus', { })
        lstPlayer = oWarMgr.GetLivePlayer()
        for iPlayer in lstPlayer:
            if not iPlayer not in dStat:
                if not dStat[iPlayer]:
                    return None
        
        if self.m_Phase > 0 and self.m_Phase <= self.m_MaxPhase and self.GetPhaseFrameByIndex(1):
            self.AddPhase()
            iFrame = self.GetPhaseFrameByIndex(1)
            iTime = Frame2Time(iFrame)
            cl_snetwar.GS2CPrepareTimeInfo(lstPlayer, 0, iTime)

    
    def OnRemoveVotePlayer(self, oWarMgr, dInfo):
        pid = dInfo['pid']
        self.RemoveVotePlayer(pid)

    
    def OnHeroDiedist(self, oSurvivor, oHero, dInfo):
        self.RemoveVotePlayer(oHero.m_PlayerID)

    
    def RemoveVotePlayer(self, pid):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dStat = oWarMgr.Query('VoteStatus', { })
        dStat.pop(pid, 0)
        SurvivorLog.Debug('game:%d removevoteplayer %s %s %s' % (oGame.m_ID, pid, dStat, oWarMgr.GetLivePlayer()))
        if dStat:
            self.TrySkipRestPhase()

    
    def GetRemainTokenNumber(self, oTarget):
        dPhaseInfo = self.m_PhaseConfig[self.m_ConfigSID]
        if self.m_Phase not in dPhaseInfo:
            return 0
        iTokenNumber = cl_formula.GetFormulaResult(oTarget, dPhaseInfo[self.m_Phase]['TokenNumber'])
        if iTokenNumber <= self.m_CurTokenCost[oTarget.m_ID]:
            return 0
        return iTokenNumber - self.m_CurTokenCost[oTarget.m_ID]

    
    def AddTokenCost(self, iTarget, iValue):
        if self.m_CurTokenCost[iTarget] + iValue < 0:
            self.m_CurTokenCost[iTarget] = 0
        else:
            self.m_CurTokenCost[iTarget] += iValue
        dDebug = self.m_Game.m_WarMgr.Query('DebugToken')
        if dDebug:
            DebugToken(self, iTarget, dDebug)

    
    def GetPassPhase(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS and oLevelNode.HasGoaledCurNode():
            return self.m_MaxPhase + 1
        if self.m_Phase > 0:
            return self.m_Phase - 1
        return 0



def DebugToken(oSurvivorElement, iTarget, dDebug):
    oSurvivorElement.Remove_Call_Out('DebugToken' + str(iTarget))
    dDebug['cnt'] += 1
    dInfo = { }
    dInfo[oSurvivorElement.m_Game.GetFrameNum()] = dDebug['cnt']
    func = Functor(ShowToken, oSurvivorElement, iTarget, dInfo)
    oSurvivorElement.Call_Out(func, 1, 'DebugToken' + str(iTarget))


def ShowToken(oSurvivorElement, iTarget, dInfo):
    oGame = oSurvivorElement.m_Game
    oTarget = oGame.GetObject(iTarget)
    oGame.m_WarMgr.Set('DebugToken', {
        'cnt': 0 })
    if not oTarget:
        return None
    dPhaseInfo = oSurvivorElement.m_PhaseConfig[oSurvivorElement.m_ConfigSID]
    if oSurvivorElement.m_Phase not in dPhaseInfo:
        return None
    iPlayer = oGame.m_WarMgr.GetPlayerIDByHeroID(iTarget)
    iTokenNumber = cl_formula.GetFormulaResult(oTarget, dPhaseInfo[oSurvivorElement.m_Phase]['TokenNumber'])
    sMsg = '玩家: %s 标识: %s/%s 更新次数 %s' % (iPlayer, oSurvivorElement.m_CurTokenCost[iTarget], iTokenNumber, dInfo)
    lstPlayer = oGame.GetRealPlayers()
    cl_notify.GS2CChat(oGame, lstPlayer, sMsg, 0)


def DebugMsg(oSurvivorElement):
    oGame = oSurvivorElement.m_Game
    if oGame.GetWarMgr().Query('DebugSurvivorAddition'):
        DebugAdditionMonsterMsg(oSurvivorElement)
        return None
    if not oGame.GetWarMgr().Query('DebugSurvivor'):
        return None
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iScene = oLevelCtrl.m_CurNode.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    dPhaseInfo = oSurvivorElement.m_PhaseConfig[oSurvivorElement.m_ConfigSID]
    iExpectedNumber = dPhaseInfo[oSurvivorElement.m_Phase]['ExpectedMonsterNumber']
    iEXtraNumber = cl_formula.GetFormulaResult(oSurvivorElement, dPhaseInfo[oSurvivorElement.m_Phase]['ExtraMonster'])
    iExtraMonsterLimit = dPhaseInfo[oSurvivorElement.m_Phase]['ExtraMonsterLimit']
    iExpectedNumber = min(iExpectedNumber + iEXtraNumber, iExpectedNumber + iExtraMonsterLimit)
    iTriggerNumber = cl_formula.GetFormulaResult(oSurvivorElement, dPhaseInfo[oSurvivorElement.m_Phase]['TriggerNumber'])
    iSuperNumber = len(oSurvivorElement.m_SuperMonsterMgr.m_SuperInfo)
    lstMonster = oScene.GetObjectsByType('Monster')
    dMonster = { }
    iMonsterPower = 0
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.Query('AdditionMonster'):
            continue
        if oMonster.m_SID not in oSurvivorElement.m_MonsterPower:
            continue
        iMonsterPower += oSurvivorElement.m_MonsterPower[oMonster.m_SID]
        if oMonster.m_Name in dMonster:
            dMonster[oMonster.m_Name] += 1
            continue
        dMonster[oMonster.m_Name] = 1
    
    sMsg = '当前阶段%d, 怪物数量%d, 期望数量%d, 触发数量%d, 强化怪数量%d\n' % (oSurvivorElement.m_Phase, iMonsterPower // 100, iExpectedNumber, iTriggerNumber, iSuperNumber)
    sMsg += '怪物具体数据:%s' % dMonster
    lstPlayer = oGame.GetRealPlayers()
    if len(sMsg.encode('utf-8')) > 250:
        iLen = len(sMsg) % 50
        for i in range(1, iLen):
            sRes = sMsg[(i - 1) * 50:i * 50]
            cl_notify.GS2CChat(oGame, lstPlayer, sRes, 0)
        
    else:
        cl_notify.GS2CChat(oGame, lstPlayer, sMsg, 0)


def DebugAdditionMonsterMsg(oSurvivorElement):
    oGame = oSurvivorElement.m_Game
    iPhase = oSurvivorElement.m_Phase
    sMsg = '当前阶段%d ' % (iPhase,)
    oMonsterCtrl = oSurvivorElement.m_CurLine.m_MonsterCtrl
    if iPhase in oMonsterCtrl.m_AdditionMonsterDebug:
        dDebug = oMonsterCtrl.m_AdditionMonsterDebug[iPhase]
        for iChoose, dInfo in dDebug.items():
            iTime = dInfo['TriggerTime']
            sMsg += '抽取%d附属刷怪 触发时间%d \n' % (iChoose, iTime)
            dCreate = dInfo['Create']
            for iGroup, iCount in dCreate.items():
                sMsg += '组数%d,数量%d\n' % (iGroup, iCount)
            
        
    lstPlayer = oGame.GetRealPlayers()
    if len(sMsg.encode('utf-8')) > 250:
        iLen = len(sMsg) % 50
        for i in range(1, iLen):
            sRes = sMsg[(i - 1) * 50:i * 50]
            cl_notify.GS2CChat(oGame, lstPlayer, sRes, 0)
        
    else:
        cl_notify.GS2CChat(oGame, lstPlayer, sMsg, 0)


def ReplaceIsNeglectAttack(oHero, oSkill):
    if not oHero.m_State.GetItemBySID(STATE_CHOOSEREWARD):
        if 'IsNeglectAttack' in oHero.__dict__:
            del oHero.IsNeglectAttack
        return False
    return True


def GetComponentClass(oMgrManager):
    return CSurvivorElement


def SetDebugLevel(iLevel):
    global g_DebugLevel
    if not lib_flag.g_IsLogicLayer:
        return None
    g_DebugLevel = iLevel

if 'g_DebugLevel' not in globals():
    g_DebugLevel = 0
