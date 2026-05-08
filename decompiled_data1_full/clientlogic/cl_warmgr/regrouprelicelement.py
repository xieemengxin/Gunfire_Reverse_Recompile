# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/regrouprelicelement.pyc
# RelativePath: clientlogic/cl_warmgr/regrouprelicelement.pyc
# Source Generated with Decompyle++
# File: regrouprelicelement.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_BOSS, WARRIOR_BOSS, NWARRIOR_DROP_RELIC_MYSTERY, EXTENDBAG_TYPE_RELIC, BOSS_DONOT_COUNT, NWARRIOR_DROP_RELIC_BLANK, BLANKRELIC, RECYCLE_UNDROP, RECYCLE_DROP, RELIC_TYPE_MYSTERY, FAKEMG_REGROUPRELIC, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_RELIC, DYNAMIC_DEMON_MONSTERRELIC, LEVEL_TYPE_HALL
from cl_cscommondef import QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, QUALITY_TYPE_HIGH, MG_SOURCE_RELIC
from cl_warmgr.mobject import CSeasonElement
from cl_object.logging import SeasonLog
from cl_only import ChooseKey, Functor, Time2Frame, DeepCopy
from cl_platformdata import GetRelicByType
from cl_warmgr.bigdataanalyse import CRelicActivityAnalyseCom
import cl_reward
import cl_perform
import cl_msgcenter
import cl_platformdata
import cl_snetwar
BOSS_RELIC_KEY = 'BossRelic'
MYSTERYRELIC_RECYCLE = {
    QUALITY_TYPE_HIGH: {
        RECYCLE_UNDROP: 2429,
        RECYCLE_DROP: 2426 },
    QUALITY_TYPE_NORMAL: {
        RECYCLE_UNDROP: 2428,
        RECYCLE_DROP: 2425 },
    QUALITY_TYPE_LOW: {
        RECYCLE_UNDROP: 2427,
        RECYCLE_DROP: 2424 } }

class CRegroupRelicElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'RegroupRelicElement'
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_ForceOpenElement = dConfig.get('ForceOpenElement', [])
        self.m_NpcSID = dConfig.get('RegroupRelicNpc', 0)
        self.m_ReplaceNpc = dConfig.get('ReplaceNpc', { })
        self.m_NoRepeatBossRelicLayer = dConfig.get('NoRepeatBossRelicLayer', 5)
        self.m_Enable = 0
        self.m_ChosenBossRelic = { }
        self.m_ForceBossRelic = 0
        self.m_DropMysteryRelicRatio = dConfig.get('DropMysteryRelicRatio', 0)
        self.m_InitBlankRelicNum = dConfig.get('InitBlankRelicNum', 0)
        self.m_ExtLotteryNpc = dConfig.get('ExtLotteryNpc', [])
        self.m_MysteryRelicWeight = GetRelicByType(RELIC_TYPE_MYSTERY)
        self.m_SignRelic = { }
        self.m_GeneralFuseNpc = 0
        self.m_GeneralLotteryNpc = 0

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.InitEvent()
        self.m_Enable = 1
        oWarMgr.Set('PutRegroupRelicNpc', 1)
        oWarMgr.Set('PutRelicLotteryNpc', 1)

    
    def InitAfter(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        for sElement in self.m_ForceOpenElement:
            oWarMgr.OpenElement(sElement, bForce = True)
        
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CRelicActivityAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('RelicActivity', oAnalyseCom)

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, sFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, sFlag, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnCreateNpc, sFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.OnChooseNpcPre, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, sFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEHERO, self.OnCreateHero, sFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, sFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DEMON_DYNAMIC_REWARD, self.OnDemonCreateDynamicReward, sFlag, iSub = DYNAMIC_DEMON_MONSTERRELIC)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerLogin, sFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, self.OnRecycle, sFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, sFlag)

    
    def Save(self):
        dData = {
            'CBR': dict(self.m_ChosenBossRelic),
            'SR': self.m_SignRelic }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ChosenBossRelic = dData['CBR']
        self.m_SignRelic = dData.get('SR', { })

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        if dInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum == oWarMgr.GetMaxLayer():
            return None
        if not self.m_NpcSID:
            SeasonLog.Alert('RegroupRelicElement:NpcSID is null')
            return None
        iLevelID = dInfo['LevelID']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        iScene = oLevelNode.m_Scene
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'regrouprelicpos')
        if not dAddInfo:
            SeasonLog.Alert('RegroupRelicElement:%s regrouprelicpos is null' % iLevelID)
            return None
        dAddInfo = DeepCopy(dAddInfo)
        self.CreateNpc(iScene, oLevelNode, dAddInfo)

    
    def CreateNpc(self, iScene, oLevelNode, dAddInfo):
        if not self.m_NpcSID:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        dMsgInfo = {
            'NPC': self.m_NpcSID,
            'LevelNode': oLevelNode,
            'NPCInfo': dAddInfo,
            'Scene': iScene }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
        if not dMsgInfo['NPC']:
            return None
        self.m_Game.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)

    
    def OnLevelNodeFinish(self, oWarMgr, dInfo):
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            iScene = oNode.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            if not oScene:
                continue
            lstDrop = oScene.GetObjectsByType('Drop')
            for iDrop in lstDrop:
                oDrop = self.m_Game.GetObject(iDrop)
                if not oDrop:
                    continue
                if oDrop.m_FightType != NWARRIOR_DROP_RELIC_BLANK:
                    continue
                if not oDrop.m_Owner:
                    continue
                oHero = self.m_Game.GetObject(oDrop.m_Owner)
                if not oHero:
                    continue
                oDrop.Remove('AutoPick')
                oHero.m_RelicCon.ChangeBlankRelicNum(1, 'AutoPick')
            
        

    
    def OnCreateNpc(self, oWarMgr, oLevelCtrl, dMsgInfo):
        iNpc = dMsgInfo['NPC']
        if iNpc in self.m_ReplaceNpc:
            iNewNpc = self.m_ReplaceNpc[iNpc]
            dMsgInfo['NPC'] = iNewNpc
        if iNpc == self.m_NpcSID and oLevelCtrl.m_CurLType == LEVEL_TYPE_HALL and oWarMgr.IsEndless():
            dMsgInfo['NPC'] = 0

    
    def OnChooseNpcPre(self, oWarMgr, oLevelCtrl, dMsgInfo):
        sType = dMsgInfo['Type']
        if not sType == 'regrouprelic' or self.m_GeneralFuseNpc:
            dMsgInfo['NpcWeight'] = { }
        elif sType == 'reliclottery' and not (self.m_GeneralLotteryNpc) and (dMsgInfo['LayerNum'], dMsgInfo['LevelNum']) in self.m_ExtLotteryNpc:
            dMsgInfo['NpcWeight'] = { }

    
    def OnStartFight(self, _oListener, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if iLevelType == LEVEL_TYPE_BOSS:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag)
        elif oLevelCtrl.CheckFirstHall():
            iLevelID = dMsgInfo['LevelID']
            dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'seasonnpcpos')
            if not dAddInfo:
                SeasonLog.Alert('RegroupRelicElement:%s seasonnpcpos is null' % iLevelID)
                return None
            dAddInfo = DeepCopy(dAddInfo)
            oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
            iScene = oLevelNode.m_Scene
            self.CreateNpc(iScene, oLevelNode, dAddInfo)

    
    def OnCreateMonster(self, _oListener, oLevelCtrl, dMsgInfo):
        oGame = self.m_Game
        iMonster = dMsgInfo['Monster']
        oMonster = oGame.GetObject(iMonster)
        if not oMonster or oMonster.m_Owner or oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            return None
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.m_CallFlag)
        if self.m_ForceBossRelic:
            iChosenRelic = self.m_ForceBossRelic
            self.m_ForceBossRelic = 0
        else:
            dBossRelicPut = cl_platformdata.GetBossRelicPut()
            dChooseRelic = self.BuildChooseBossRelic(oLevelCtrl, oMonster, dBossRelicPut)
            if not dChooseRelic:
                iLevelID = oLevelCtrl.m_CurNode.m_Level
                SeasonLog.Debug('%s %s %s choosebossrelic empty %s %s' % (oGame.m_ID, iLevelID, oMonster.m_SID, dBossRelicPut, self.m_ChosenBossRelic))
                return None
            iChosenRelic = ChooseKey(oGame, dChooseRelic)
        self.AddBossRelic(oLevelCtrl, oMonster, iChosenRelic)

    
    def BuildChooseBossRelic(self, oLevelCtrl, oMonster, dBossRelicPut):
        dChooseRelic = { }
        iDataSID = oMonster.m_DataSID
        iCurLayer = oLevelCtrl.m_LayerNum
        bExcludeChosen = iCurLayer < self.m_NoRepeatBossRelicLayer
        for iRelicSID in dBossRelicPut:
            if bExcludeChosen and iRelicSID in self.m_ChosenBossRelic:
                continue
            clsRelic = cl_perform.GetPerformModule(iRelicSID)
            if not clsRelic:
                continue
            if clsRelic.m_LimitMonster and iDataSID not in clsRelic.m_LimitMonster:
                continue
            if clsRelic.m_ExcludeMonster and iDataSID in clsRelic.m_ExcludeMonster:
                continue
            dChooseRelic[iRelicSID] = 1
        
        return dChooseRelic

    
    def AddBossRelic(self, oLevelCtrl, oMonster, iRelicSID):
        oGame = self.m_Game
        iMonster = oMonster.m_ID
        iLevelID = oLevelCtrl.m_CurNode.m_Level
        iCurBossRelic = oMonster.Query(BOSS_RELIC_KEY, 0)
        if iCurBossRelic:
            SeasonLog.Alert('%s %s %s addbossrelic %s cur:%s' % (oGame.m_ID, iLevelID, oMonster.m_SID, iRelicSID, iCurBossRelic))
            return None
        SeasonLog.Debug('%s %s %s addbossrelic %s' % (oGame.m_ID, iLevelID, oMonster.m_SID, iRelicSID))
        iLayer = oLevelCtrl.m_LayerNum
        if iLayer < self.m_NoRepeatBossRelicLayer:
            self.m_ChosenBossRelic[iRelicSID] = 1
        oPerform = oMonster.AddPerform(iRelicSID, 1)
        if not oPerform:
            SeasonLog.Alert('%s %s %s addbossrelic %s err' % (oGame.m_ID, iLevelID, oMonster.m_SID, iRelicSID))
            return None
        oMonster.Set(BOSS_RELIC_KEY, iRelicSID)
        dMsgInfo = {
            'CurLayer': iLayer,
            'BossSID': oMonster.m_SID,
            'iPerform': iRelicSID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_ADDBOSSRELIC, self.m_WarMgr, dMsgInfo)
        cl_msgcenter.AddAttentionFunc(self, iMonster, cl_msgcenter.MSG_WAR_DIE, self.OnBossDie, self.m_CallFlag)
        oScene = oGame.m_SceneMgr.GetScene(oMonster.m_Scene)
        oGame.AddGlobalAttention(iMonster, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, OnPlayerMapLoadOK, self.m_CallFlag)
        if oScene:
            dPlayer = oScene.GetPlayers()
            if dPlayer:
                cl_snetwar.GS2CMonsterUseRelic(oGame, iMonster, [
                    iRelicSID], dPlayer)

    
    def OnBossDie(self, _oListener, oMonster, dMsgInfo):
        iMonster = oMonster.m_ID
        cl_msgcenter.DoneAttention(self, iMonster, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(iMonster, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)

    
    def SetForceBossRelic(self, iRelicSID):
        self.m_ForceBossRelic = iRelicSID

    
    def Release(self):
        self.DoneEvent()
        self.m_WarMgr = None
        super().Release()

    
    def DoneEvent(self):
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, sFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, sFlag)
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, sFlag)
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, sFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, sFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEHERO, sFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, sFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DEMON_DYNAMIC_REWARD, sFlag, iSub = DYNAMIC_DEMON_MONSTERRELIC)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, sFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, sFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, sFlag)

    
    def OnCreateHero(self, oWarMgr, oTarget, dInfo):
        iHeroID = dInfo['Hero']
        oHero = self.m_Game.GetObject(iHeroID)
        oHero.SwitchExtendBag(EXTENDBAG_TYPE_RELIC, 1)

    
    def OnMonsterDie(self, oWarMgr, oMonster, dMsgInfo):
        iFightType = oMonster.m_FightType
        if iFightType & WARRIOR_BOSS != WARRIOR_BOSS or iFightType in BOSS_DONOT_COUNT:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oWarMgr.GetEndlessMode() and oLevelCtrl.m_LayerNum == 4:
            return None
        oGame = self.m_Game
        vBasePos = cl_reward.GetDropBasePos(oMonster)
        iScene = oMonster.m_Scene
        iMonster = oMonster.m_ID
        dExtraInfo = {
            'Abandoner': iMonster }
        lstHero = oWarMgr.GetLiveHero()
        dRewardBlankRelicHero = { }
        lstRewardMysteryRelicHero = []
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            vPos = cl_reward.GetDropFixPos(oGame, oHero, iScene, vBasePos, iMonster)
            iBossDropBlankRelic = oHero.Query('BossDropBlankRelic', 0)
            for _ in range(0, iBossDropBlankRelic):
                oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_RELIC_BLANK, vPos, [
                    {
                        'SID': BLANKRELIC }], dExtraInfo, { }, iHero, iSplit = 1)
            
            if self.DropMysteryRelic(oHero, iScene, vPos, 'Boss'):
                lstRewardMysteryRelicHero.append(oHero.m_PlayerID)
            dRewardBlankRelicHero[oHero.m_PlayerID] = iBossDropBlankRelic
        
        SeasonLog.Info('%s bossdrop br %s %s' % (oGame.m_ID, dRewardBlankRelicHero, lstRewardMysteryRelicHero))

    
    def GetMysteryRelic(self, oHero):
        oGame = self.m_Game
        if oGame.Random(100) >= self.m_DropMysteryRelicRatio:
            return 0
        dRelicWeight = { }
        for iRelic in self.m_MysteryRelicWeight:
            if oHero.m_RelicCon.GetPerform(iRelic):
                continue
            dRelicWeight[iRelic] = 10
        
        if not dRelicWeight:
            return 0
        return ChooseKey(oGame, dRelicWeight)

    
    def DropMysteryRelic(self, oHero, iScene, vPos, sReason):
        iMysteryRelic = self.GetMysteryRelic(oHero)
        if not iMysteryRelic:
            return 0
        iHero = oHero.m_ID
        pid = self.m_WarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dStaticInfo = {
            'DropLevel': 1,
            'DropSource': pid }
        self.m_Game.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_RELIC_MYSTERY, vPos, [
            iMysteryRelic], { }, dStaticInfo, iHero)
        return 1

    
    def OnDemonCreateDynamicReward(self, oWarMgr, oHero, dMsgInfo):
        iMysteryRelic = self.GetMysteryRelic(oHero)
        if not iMysteryRelic:
            return 0
        lstReward = [
            {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iMysteryRelic] } }]
        dMsgInfo['Reward'][FAKEMG_REGROUPRELIC] = (0, lstReward, {
            'Player': oHero.m_ID })
        SeasonLog.Info('%s monsterrelic mysteryrelic %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iMysteryRelic))

    
    def SignRelic(self, iPlayer, iRelic, iSign):
        if iPlayer not in self.m_SignRelic:
            self.m_SignRelic[iPlayer] = []
        lstSignRelic = self.m_SignRelic[iPlayer]
        if iSign or iRelic not in lstSignRelic:
            lstSignRelic.append(iRelic)
        elif iRelic in lstSignRelic:
            lstSignRelic.remove(iRelic)

    
    def OnPlayerLogin(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_SignRelic:
            return None
        cl_snetwar.GS2CUpdateSignRelic(iPlayer, self.m_SignRelic[iPlayer])

    
    def OnRecycle(self, oWarMgr, oHero, dMsgInfo):
        if 'AutoRecycle' in dMsgInfo:
            return None
        if 'Relic' not in dMsgInfo:
            return None
        clsPerform = cl_perform.GetPerformModule(dMsgInfo['Relic'])
        if not clsPerform or clsPerform.m_RelicType != RELIC_TYPE_MYSTERY:
            return None
        iQuality = clsPerform.m_Quality
        if iQuality not in MYSTERYRELIC_RECYCLE:
            return None
        dType2RelicGame = MYSTERYRELIC_RECYCLE[iQuality]
        iRecycleType = dMsgInfo['RecycleType']
        iRelicGame = dType2RelicGame[iRecycleType]
        dReward = {
            iRelicGame: (10000, 1) }
        dExtInfo = {
            'CheckGoldenCup': 0,
            'OnlyRewardAttack': 1,
            'Abandoner': oHero.m_ID,
            'RepeatReward': 1,
            'Source': MG_SOURCE_RELIC,
            'Level': 1 }
        cl_reward.RewardItemByMiniGame(oHero, oHero.m_ID, dReward, 'RecycleMysteryRelic%d' % oHero.m_ID, MG_SOURCE_RELIC, dExtInfo)

    
    def OnAddAllPlayer(self, oWarMgr, oHero, dMsgInfo):
        oGame = self.m_Game
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if not oHero.QuerySavedData('InitBlankRelicNum'):
                oHero.SetSavedData('InitBlankRelicNum', 1)
                oHero.m_RelicCon.ChangeBlankRelicNum(self.m_InitBlankRelicNum, self.m_CallFlag)
            if oHero.Query('GeneralFuseNpc'):
                self.m_GeneralFuseNpc = 1
            if oHero.Query('GeneralLotteryNpc'):
                self.m_GeneralLotteryNpc = 1
        



def OnPlayerMapLoadOK(oMonster, oHero, dMsgInfo):
    if oHero.m_Scene != oMonster.m_Scene:
        return None
    iBossRelic = oMonster.Query(BOSS_RELIC_KEY, 0)
    if not iBossRelic:
        return None
    cl_snetwar.GS2CMonsterUseRelic(oHero.m_Game, oMonster.m_ID, [
        iBossRelic], {
        oHero.m_PlayerID: 1 })


def GetComponentClass(oWarManager):
    return CRegroupRelicElement

