# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/relictalentelement.pyc
# RelativePath: clientlogic/cl_warmgr/relictalentelement.pyc
# Source Generated with Decompyle++
# File: relictalentelement.pyc (Python 3.6)

from cl_warmgr.mobject import CSeasonElement
from cl_only import ChooseMulKeys, Functor, ChooseKey
from cl_platformdata import GetReliceTalentWeight
from cl_commondefines import NWARRIOR_DROP_MAGIC_POWER, LEVEL_TYPE_BOSS, WARRIOR_BOSS, SUIT_RELIC, VIRTUAL_ITEM_MAGICPOWER, PLAYER_CHOOSE_GENERAL
from cl_commondefines import ENDLESS_REAL, FAKEMG_RELICTALENT, NWARRIOR_NPC_EVENT, LAYER_CHOOSE_EVENTNPC, BOSS_DONOT_COUNT
from cl_reward import GetDropBasePos, GetDropFixPos
from cl_object.logging import RelictalentLog
from cl_drop import GetCommondrop
from cl_minigame import MiniGameAttrInfo
from cl_warmgr.bigdataanalyse import CRelicTalentAnalyseCom
import cl_msgcenter
import cl_netattr

class CRelicTalentElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'RelicTalentElement'
        self.m_RelicPool = GetReliceTalentWeight()
        self.m_EnableRound = self.m_Data.m_Config.get('EnableRound', [])
        self.m_RelicOptionCnt = self.m_Data.m_Config.get('RelicOptionCnt', 3)
        self.m_ForbidRelic = self.m_Data.m_Config.get('ForbidRelic', [])
        self.m_ForbidSuit = self.m_Data.m_Config.get('ForbidSuit', [])
        self.m_MagicNpc = self.m_Data.m_Config.get('MagicNpc', { })
        self.m_ExcludeBossDropLayer = self.m_Data.m_Config.get('ExcludeBossDropLayer', [])
        self.m_MagicRoomCLG = self.m_Data.m_Config.get('MagicRoomCLG', [])
        self.m_MagicRoomCLGCertain = self.m_Data.m_Config.get('MagicRoomCLGCertain', { })
        self.m_MagicBossWeight = self.m_Data.m_Config.get('MagicBossWeight', { })
        self.m_MagicNpcWeight = self.m_Data.m_Config.get('MagicNpcWeight', { })
        self.m_MagicRoomCLGWeight = self.m_Data.m_Config.get('MagicRoomCLGWeight', { })
        self.m_MagicDrop = self.m_Data.m_Config.get('MagicDrop', { })
        self.m_MagicNotify = self.m_Data.m_Config.get('MagicNotify', 0)
        self.m_EventNpc = self.m_Data.m_Config.get('EventNpc', { })
        self.m_MinimumMagic = self.m_Data.m_Config.get('MinimumMagic', 0)
        self.m_NpcReward = { }
        self.m_BossReward = { }
        self.m_RoomCLGReward = { }
        self.m_Enable = 0
        self.m_CurLayer = 0
        self.m_LayerReward = { }
        self.m_ReplaceNpc = -1

    
    def Save(self):
        dData = {
            'RR': self.m_RoomCLGReward,
            'LR': self.m_LayerReward,
            'RN': self.m_ReplaceNpc }
        return dData

    
    def Load(self, dData):
        self.m_RoomCLGReward = dData.get('RR', { })
        self.m_LayerReward = dData.get('LR', { })
        self.m_ReplaceNpc = dData.get('RN', -1)

    
    def Init(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.m_Enable = 1
        oWarMgr.AddForbidRelic(self.m_ForbidRelic)
        oSuitElement = oWarMgr.GetComponent('SuitElement')
        if oSuitElement:
            self.ForbidSuit()
        else:
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_INITELEMENT, self.OnInitElement, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if self.m_MagicRoomCLG and self.m_MagicRoomCLGWeight:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, self.OnRoomChallengeCreateDemon, self.m_CallFlag)
        if self.m_MagicNpc and self.m_MagicNpcWeight:
            oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_CallFlag)
            oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_GENERATE_RELIC, self.OnGenerateRelic, self.m_CallFlag)
        if self.m_EventNpc:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.OnPreChooseNpc, self.m_CallFlag)

    
    def InitAfter(self):
        if not self.m_Enable:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oBigdataMgr = oWarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CRelicTalentAnalyseCom(oGame)
            oBigdataMgr.SetCom('RelicTalent', oAnalyseCom)

    
    def CheckEnable(self):
        return self.m_Enable

    
    def ForbidSuit(self):
        oSuitElement = self.m_Game.m_WarMgr.GetComponent('SuitElement')
        for iSuit in self.m_ForbidSuit:
            oSuitElement.AddForbidSuit(iSuit)
        
        for iRelic in self.m_ForbidRelic:
            oSuitElement.AddForbidSuitCon(SUIT_RELIC, iRelic)
        

    
    def OnInitElement(self, oRelicTalentElement, oWarMgr, dMsgInfo):
        if dMsgInfo['element'] == 'SuitElement':
            self.ForbidSuit()
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_INITELEMENT, self.m_CallFlag)

    
    def Release(self):
        if self.m_Enable:
            oGame = self.m_Game
            oWarMgr = oGame.m_WarMgr
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_INITELEMENT, self.m_CallFlag)
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.m_CallFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_CallFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_GENERATE_RELIC, self.m_CallFlag)
        super().Release()

    
    def RecordReward(self, iCount = 1):
        if self.m_CurLayer not in self.m_LayerReward:
            self.m_LayerReward[self.m_CurLayer] = 0
        self.m_LayerReward[self.m_CurLayer] += iCount

    
    def OnAddPlayer(self, oRelicTalentElement, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        self.EnableCon(oHero)

    
    def EnableAllPleyerCon(self):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetRoomHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            self.EnableCon(oHero)
            oHero.m_RelicTalentCon.SendChooseRelic(iNextCB = 0)
        

    
    def EnableCon(self, oHero):
        lstRelicOption = ChooseMulKeys(self.m_Game, self.m_RelicPool, self.m_RelicOptionCnt)
        oHero.m_RelicTalentCon.Init(lstRelicOption, self.m_MagicNotify)

    
    def OnLevelNodeInit(self, oRelicTalentElement, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oWarMgr.IsEndless():
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CallFlag)
            if oWarMgr.GetEndlessMode() != ENDLESS_REAL:
                cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
                cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
                return None
        iLayer = dMsgInfo['Layer']
        if dMsgInfo['LevelType'] == LEVEL_TYPE_BOSS and iLayer not in self.m_ExcludeBossDropLayer:
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag)
        else:
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
        if self.m_CurLayer and self.m_CurLayer != iLayer and iLayer in self.m_EventNpc:
            iLastLayerReward = self.m_LayerReward.get(self.m_CurLayer, 0)
            if iLastLayerReward < self.m_MinimumMagic:
                iLayerCnt = oLevelCtrl.m_LayerChoose.GetMainLevelLayerCnt(LAYER_CHOOSE_EVENTNPC)
                iReplace = self.m_Game.Random(iLayerCnt)
                self.m_ReplaceNpc = iReplace
            else:
                self.m_ReplaceNpc = -1
        if self.m_ReplaceNpc >= 0:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnPreCreateNpc, self.m_CallFlag)
        else:
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CallFlag)
        self.m_CurLayer = iLayer

    
    def OnCreateMonster(self, oRelicTalentElement, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        if not self.m_MagicBossWeight:
            return None
        iMonster = dMsgInfo['Monster']
        oMonster = oGame.GetObject(iMonster)
        if not oMonster:
            return None
        iFightType = oMonster.m_FightType
        if iFightType & WARRIOR_BOSS != WARRIOR_BOSS or iFightType in BOSS_DONOT_COUNT:
            return None
        RelictalentLog.Debug(f'''{oGame.m_ID} boss reward {oMonster.m_SID} {iMonster}''')
        self.RecordReward()
        self.m_BossReward[iMonster] = { }
        cl_msgcenter.AddAttentionFunc(self, iMonster, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, Functor(self.OnMonsterDie), self.m_CallFlag)

    
    def OnMonsterDie(self, oRelicTalentElement, oMonster, dMsgInfo):
        iMonster = oMonster.m_ID
        cl_msgcenter.DoneAttention(self, iMonster, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.m_CallFlag)
        if not self.m_MagicBossWeight:
            return None
        if iMonster not in self.m_BossReward:
            return None
        dReward = self.m_BossReward[iMonster]
        oGame = self.m_Game
        vBasePos = GetDropBasePos(oMonster)
        (iOption, iMagicPower) = ChooseKey(oGame, self.m_MagicBossWeight)
        iGroup = oGame.m_WarMgr.AddDropGroup()
        dDrop = {
            'Option': iOption,
            'MagicPower': iMagicPower,
            'Group': iGroup }
        if iOption in self.m_MagicDrop:
            dDrop['SID'] = self.m_MagicDrop[iOption]
        dExtraInfo = {
            'Abandoner': iMonster }
        lstHero = oGame.m_WarMgr.GetLiveHero()
        oResMgr = oGame.m_ResMgr
        iScene = oMonster.m_Scene
        for iHero in lstHero:
            if iHero in dReward:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            vPos = GetDropFixPos(oGame, oHero, iScene, vBasePos, iMonster)
            RelictalentLog.Debug(f'''{self.m_Game.m_ID} boss {iMonster} reward {iHero} {iOption} {iMagicPower} {vPos}''')
            dReward[iHero] = 1
            oResMgr.CreateDrop(oMonster.m_Scene, NWARRIOR_DROP_MAGIC_POWER, vPos, [
                dDrop], dExtraInfo, { }, iHero, iSplit = 1)
        

    
    def OnCreateNpc(self, oWarMgr, oNpc, dInfo):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        if oWarMgr.IsEndless():
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_CallFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_GENERATE_RELIC, self.m_CallFlag)
            return None
        iSID = oNpc.m_SID
        if iSID in self.m_MagicNpc:
            (iOption, iMagicPower) = ChooseKey(oGame, self.m_MagicNpcWeight)
            if iOption not in self.m_MagicDrop:
                return None
            RelictalentLog.Debug(f'''{self.m_Game.m_ID} npc replace reward magic {iSID} {oNpc.m_ID} {oNpc.m_LineIdx} {iOption} {iMagicPower}''')
            self.RecordReward()
            self.m_NpcReward[oNpc.m_ID] = {
                'Reward': (iOption, iMagicPower, self.m_MagicNpc[iSID]),
                'Hero': { } }
        if iSID in self.m_EventNpc:
            self.RecordReward()
            if self.m_ReplaceNpc >= 0:
                self.m_ReplaceNpc = -1
                oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
                cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CallFlag)

    
    def OnGenerateRelic(self, oWarMgr, oHero, dInfo):
        if 'MGOwner' not in dInfo:
            return None
        iNpc = dInfo['MGOwner']
        if iNpc not in self.m_NpcReward:
            return None
        iHero = oHero.m_ID
        if iHero in self.m_NpcReward[iNpc]['Hero']:
            return None
        self.m_NpcReward[iNpc]['Hero'][iHero] = 1
        lstReward = dInfo['Reward']
        if not lstReward:
            return None
        (iOption, iMagicPower, idx) = self.m_NpcReward[iNpc]['Reward']
        if idx >= len(lstReward):
            return None
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} npc {iNpc} reward magic {iHero} {iOption} {iMagicPower}''')
        iSID = self.m_MagicDrop[iOption]
        iShape = GetCommondrop(iSID)
        (_, dOldReward) = lstReward[idx]
        dAttrInfo = {
            'SID': iSID,
            'Shape': iShape }
        lstAttr = MiniGameAttrInfo(None, cl_netattr.PROP_DROPITEM_MAGICPOWER, dAttrInfo)
        dReward = {
            'Pos': dOldReward['Pos'],
            'Type': VIRTUAL_ITEM_MAGICPOWER,
            'Attr': lstAttr,
            'Option': iOption,
            'MagicPower': iMagicPower,
            'Notify': self.m_MagicNotify }
        lstReward[idx] = [
            iSID,
            dReward]
        dInfo['SubOp'] = PLAYER_CHOOSE_GENERAL

    
    def OnRoomChallengeCreateDemon(self, oRelicTalentElement, oLevelCtrl, dMsgInfo):
        dMGInfo = dMsgInfo['MGInfo']
        if not dMGInfo:
            return None
        oGame = self.m_Game
        iChangeSID = dMsgInfo['ChallengeSID']
        if iChangeSID in self.m_MagicRoomCLGCertain:
            dMagicRoomCLGWeight = self.m_MagicRoomCLGCertain[iChangeSID]
            (iOption, iMagicPower) = ChooseKey(oGame, dMagicRoomCLGWeight)
            if not iOption:
                return None
            iGroup = oGame.m_WarMgr.AddDropGroup()
            self.AddRewardMagicpower(iOption, iMagicPower, iGroup, dMsgInfo, iCalLimit = 0)
        else:
            (iProb, iLimit) = self.m_MagicRoomCLG
            if len(self.m_RoomCLGReward) >= iLimit:
                return None
            if oGame.Random(100) > iProb:
                return None
            (iOption, iMagicPower) = ChooseKey(oGame, self.m_MagicRoomCLGWeight)
            if not iOption:
                return None
            iGroup = oGame.m_WarMgr.AddDropGroup()
            self.AddRewardMagicpower(iOption, iMagicPower, iGroup, dMsgInfo, iCalLimit = 1)

    
    def AddRewardMagicpower(self, iOption, iMagicPower, iGroup, dMsgInfo, iCalLimit):
        sKey = dMsgInfo['Key']
        if iCalLimit:
            dRoomReward = self.m_RoomCLGReward.setdefault(sKey, { })
        else:
            dRoomReward = { }
        dReward = {
            'item': VIRTUAL_ITEM_MAGICPOWER,
            'info': {
                'Option': iOption,
                'MagicPower': iMagicPower,
                'DropPos': (0, 0, 0),
                'Scene': dMsgInfo['Scene'],
                'Group': iGroup } }
        self.RecordReward()
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} challenge reward {sKey} {iOption} {iMagicPower} {iCalLimit}''')
        dMGInfo = dMsgInfo['MGInfo']
        for iHero, dInfo in dMGInfo.items():
            if iHero in dRoomReward:
                continue
            dRoomReward[iHero] = 1
            dInfo[FAKEMG_RELICTALENT] = (0, [
                dict(dReward)], { })
        

    
    def OnPreChooseNpc(self, oRelicTalentElement, oLevelCtrl, dMsgInfo):
        if dMsgInfo['Type'] != 'event' or not dMsgInfo['NpcWeight']:
            return None
        iLayer = oLevelCtrl.m_LayerNum
        if iLayer not in self.m_EventNpc:
            return None
        dNpcWeight = self.m_EventNpc[iLayer]
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} extendnpc {iLayer} {oLevelCtrl.m_LayerNum} {dNpcWeight}''')
        dMsgInfo['NpcWeight'].update(dNpcWeight)

    
    def OnPreCreateNpc(self, oRelicTalentElement, oLevelCtrl, dMsgInfo):
        if self.m_ReplaceNpc < 0:
            return None
        oGame = self.m_Game
        iNpcSID = dMsgInfo['NPC']
        clsNpcData = oGame.m_WarData.GetNpcData(iNpcSID)
        if not clsNpcData or clsNpcData.m_FightType != NWARRIOR_NPC_EVENT:
            return None
        if self.m_CurLayer not in self.m_EventNpc:
            return None
        if self.m_ReplaceNpc == 0:
            iMagicNpc = ChooseKey(oGame, self.m_EventNpc[self.m_CurLayer])
            RelictalentLog.Debug(f'''{self.m_Game.m_ID} replacenpc {iNpcSID} {iMagicNpc}''')
            dMsgInfo['NPC'] = iMagicNpc
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CallFlag)
        self.m_ReplaceNpc = -1



def GetComponentClass(oWarManager):
    return CRelicTalentElement

