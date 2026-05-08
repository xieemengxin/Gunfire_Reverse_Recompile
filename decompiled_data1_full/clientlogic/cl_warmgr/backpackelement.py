# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/backpackelement.pyc
# RelativePath: clientlogic/cl_warmgr/backpackelement.pyc
# Source Generated with Decompyle++
# File: backpackelement.pyc (Python 3.6)

from cl_only import Functor, Time2Frame, ChooseKey, SendAlert
from cl_commondefines import NWARRIOR_NPC_PASSBOX, LEVEL_TYPE_FIGHT, NWARRIOR_DROP_S7MODULE, NWARRIOR_DROP_S7CRYSTAL, VIRTUAL_ITEM_DROP, DROP_REASON_NPCREWARD, WARRIOR_BOSS, BOSS_DONOT_COUNT, DROP_REASON_NORMAL, MAX_LAYER, QUALITY_NORMAL, CHALLENGE_COUNT_MUTANTMONSTER, WARRIOR_HERO, FAKEMG_S7CRYSTAL, VIRTUAL_ITEM_S7CRYSTAL, NWARRIOR_NPC_S7SHOP, VIRTUAL_ITEM_S7MODULE, VIRTUAL_ITEM_S7CRYSTALPACKET, FAKEMG_S7MOUDLE
from cl_warmgr.mobject import CSeasonElement
from cl_platformdata import GetTotalPoint2Crystal
from cl_object.reason import REASON_TYPE_PERFORM
from cl_object.logging import SeasonLog
from cl_container.backpackcon import CRYSTAL_RAWMATERIAL_SID
from cl_seasonplay.season7.s7goodsdata import GetS7GoodsData
import cl_msgcenter
import cl_reward
import cl_seasonplay.season7 as clseason7
import cl_formula
import cl_newformula
DROP_CRYSTAL_MAX_LAYER = 5
SPECIAL_MODULE_DROP_DEFAULT_POINT = {
    2120: 1 }
DROP_MODULE_DEFAULT_POINT = 2

class CBackpackElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'BackpackElement'
        self.m_Enable = 0
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_PassBoxDropDelay = 150
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_PassBoxDropS7ItemNum = dConfig.get('PassBoxDropS7ItemNum', [
            0,
            0])
        self.m_KillBossDropS7ItemNum = dConfig.get('KillBossDropS7ItemNum', [
            0,
            0])
        self.m_DropCrystalTotalPointWeight = dConfig.get('DropCrystalTotalPointWeight', { })
        self.m_KillLayerBossUnlockConEquipAreaSize = dConfig.get('KillLayerBossUnlockConEquipAreaSize', { })
        self.m_MaxConEquipAreaSize = dConfig.get('MaxConEquipAreaSize', [
            0,
            0])
        self.m_BackpackDamagePerform = dConfig.get('BackpackDamagePerform', { })
        self.m_SeasonChallengeDropCrystalProp = { }
        self.m_SeasonChallengeGuaranteeCount = dConfig.get('SeasonChallengeGuaranteeCount', 5)
        self.m_SeasonChallengeNoRewardCurCount = 0
        self.m_ExtraS7ShopNpc = dConfig.get('ExtraS7ShopNpc', { })
        self.m_UseExtraS7ShopNpc = 0
        self.m_AIEnableWhitePF = dConfig.get('AIEnableWhitePF', [])
        self.m_AIMoudleWhite = dConfig.get('AIMoudleWhite', [])
        self.m_SeasonChallengeLayerRewardLimit = dConfig.get('SeasonChallengeLayerRewardLimit', 2)
        self.m_SeasonChallengeLayerRewardCount = 0
        self.m_SeasonChallengeDropModuleWeight = { }
        self.m_SeasonChallengeDropGoodSID = dConfig.get('SeasonChallengeDropGoodSID', { })
        self.m_SeasonChallengeLayerRewardModuleNum = 0

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        super().Init()
        self.m_Enable = 1
        oWarMgr.Set('PutS7ShopNpc', 1)
        oGame = self.m_Game
        sFlag = self.m_CallFlag
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, sFlag)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, sFlag)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, sFlag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, sFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, self.OnChallengeEndCreateDemon, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnAddPlayer, sFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.OnChooseNpcPre, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.OnLevelGoalBefore, sFlag)
        self.InitSeason7AnalyseCom()

    
    def Release(self):
        self.m_Enable = 0
        oWarMgr = self.m_WarMgr
        oGame = self.m_Game
        sFlag = self.m_CallFlag
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, sFlag)
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, sFlag)
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, sFlag)
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, sFlag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, sFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, sFlag)
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, sFlag)
        super().Release()
        self.m_WarMgr = None
        self.m_Game = None

    
    def FilterAndFixAISeasonInfo(self, dDelegateAI):
        if 'SignModule' in dDelegateAI:
            dDelegateAI.pop('SignModule')
        if 'SpecialPassive' in dDelegateAI:
            dDelegateAI.pop('SpecialPassive')

    
    def OnAddPlayer(self, oElement, oWarMgr, dInfo):
        if oWarMgr.m_IsUseRecord:
            return None
        oHero = dInfo['Hero']
        oBackbackCon = oHero.m_BackpackCon
        if not oBackbackCon:
            return None
        (iMaxRow, iMaxCol) = self.m_MaxConEquipAreaSize
        (iUnlockRow, iUnlockCol) = self.m_KillLayerBossUnlockConEquipAreaSize.get(0, [
            0,
            0])
        oBackbackCon.SetEquipAreaMaxSize(iMaxRow, iMaxCol, sReason = 'init', iSync = 0)
        oBackbackCon.UnlockEquipAreaSize(iUnlockRow, iUnlockCol, sReason = 'init', iSync = 0)
        dPlayerInfo = dInfo['Info']
        if 'UnLockS7Module' in dPlayerInfo:
            oBackbackCon.SetUnLockModule(dPlayerInfo['UnLockS7Module'])
        if 'UnLockS7Crystal' in dPlayerInfo:
            oBackbackCon.SetUnLockCrystal(dPlayerInfo['UnLockS7Crystal'])
        if 'SignModule' in dPlayerInfo:
            oBackbackCon.UpdateSignModuleInfo(dPlayerInfo['SignModule'])
        if 'SpecialPassive' in dPlayerInfo:
            oBackbackCon.SetSpecialPassive(dPlayerInfo['SpecialPassive'])

    
    def OnAddAllPlayer(self, oWarMgr, oHero, dMsgInfo):
        oGame = self.m_Game
        oRecycleDropElement = oWarMgr.GetComponent('RecycleDropElement')
        if oRecycleDropElement:
            oRecycleDropElement.AddCustomRecycleRule(NWARRIOR_DROP_S7CRYSTAL, AutoPickCryStalDrop)
        dSeasonChallengeDropCrystalProp = self.m_SeasonChallengeDropCrystalProp
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.Query('UseExtraS7ShopNpc'):
                self.m_UseExtraS7ShopNpc = 1
            dHeroDropCrystalProp = oHero.Query('S7DropCrystalProp', { })
            for iLayer, iProp in dHeroDropCrystalProp.items():
                if iLayer not in dSeasonChallengeDropCrystalProp:
                    dSeasonChallengeDropCrystalProp[iLayer] = iProp
                    continue
                dSeasonChallengeDropCrystalProp[iLayer] = max(iProp, dSeasonChallengeDropCrystalProp[iLayer])
            
            dSeasonChallengeDropModuleProp = self.m_SeasonChallengeDropModuleWeight
            dHeroDropModuleProp = oHero.Query('S7DropModuleProp', { })
            for iLayer, iProp in dHeroDropModuleProp.items():
                if iLayer not in dSeasonChallengeDropModuleProp:
                    dSeasonChallengeDropModuleProp[iLayer] = iProp
                    continue
                dSeasonChallengeDropModuleProp[iLayer] = max(iProp, dSeasonChallengeDropModuleProp[iLayer])
            
        

    
    def OnLayerStart(self, oBackpackElement, oLevelCtrl, dMsgInfo):
        self.m_SeasonChallengeLayerRewardCount = 0
        self.m_SeasonChallengeLayerRewardModuleNum = 0

    
    def OnChooseNpcPre(self, oWarMgr, oLevelCtrl, dMsgInfo):
        sType = dMsgInfo['Type']
        if sType != 's7shop':
            return None
        iLevelNum = dMsgInfo['LevelNum']
        iLayerNum = dMsgInfo['LayerNum']
        if iLayerNum not in self.m_ExtraS7ShopNpc or iLevelNum not in self.m_ExtraS7ShopNpc[iLayerNum]:
            return None
        if self.m_UseExtraS7ShopNpc:
            return None
        dMsgInfo['NpcWeight'] = { }

    
    def ChooseCrystalTotalPoint(self, oTarget, iLayerNum):
        iLayerNum = min(iLayerNum, MAX_LAYER)
        if iLayerNum not in self.m_DropCrystalTotalPointWeight:
            return 0
        dLayerInfo = self.m_DropCrystalTotalPointWeight[iLayerNum]
        if not dLayerInfo:
            return 0
        oGame = self.m_Game
        dTrueLayerInfo = cl_formula.CalArgsFormula(oTarget, dLayerInfo, { })
        (iMinTotalPoint, iMaxTotalPoint) = ChooseKey(oGame, dTrueLayerInfo)
        iTotalPoint = oGame.Random((iMaxTotalPoint - iMinTotalPoint) + 1) + iMinTotalPoint
        return iTotalPoint

    
    def OnNpcInteract(self, oListener, oHero, dMsgInfo):
        if 'NpcType' not in dMsgInfo or dMsgInfo['NpcType'] != NWARRIOR_NPC_PASSBOX:
            return None
        oGame = self.m_Game
        iNpc = dMsgInfo['NPC']
        oNpc = oGame.GetObject(iNpc)
        if not oNpc:
            return None
        oLevelNode = cl_newformula.GetObjLevelNode(oNpc)
        if not oLevelNode or oLevelNode.m_LevelType not in (LEVEL_TYPE_FIGHT,):
            return None
        (iModuleNum, iCrystalNum) = self.m_PassBoxDropS7ItemNum
        iDelay = self.m_PassBoxDropDelay
        if iDelay:
            oNpc.Call_Out(Functor(self.RewardDropS7Item, iModuleNum, iCrystalNum, oNpc, 'PassBox', DROP_REASON_NPCREWARD), Time2Frame(iDelay), '%s-PassBoxReward' % self.m_CallFlag)
        else:
            self.RewardDropS7Item(iModuleNum, iCrystalNum, oNpc, 'PassBox', DROP_REASON_NPCREWARD)

    
    def OnDie(self, oWarMgr, oTarget, dMsgInfo):
        if oTarget.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS or oTarget.m_FightType in BOSS_DONOT_COUNT:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFinishWar():
            return None
        (iModuleNum, iCrystalNum) = self.m_KillBossDropS7ItemNum
        self.RewardDropS7Item(iModuleNum, iCrystalNum, oTarget, 'BossDie')
        (iLayer, _) = cl_newformula.GetObjLayerAndLevel(oTarget)
        self.UnlockConEquipAreaSize(iLayer)

    
    def GetSceneLayer(self, oLevelCtrl, iScene):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return 0
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if not oLevelNode:
            return 0
        return min(DROP_CRYSTAL_MAX_LAYER, oLevelNode.m_LayerNum)

    
    def CheckSeasonChallengeCanDropCrystal(self, iLayer):
        iProp = self.m_SeasonChallengeDropCrystalProp.get(iLayer, 0)
        if not iProp:
            return 0
        if self.m_SeasonChallengeLayerRewardCount >= self.m_SeasonChallengeLayerRewardLimit:
            SeasonLog.Info('%s layer can reward max %s %s' % (self.m_Game.m_ID, self.m_SeasonChallengeLayerRewardCount, self.m_SeasonChallengeLayerRewardLimit))
            return 0
        if self.m_SeasonChallengeNoRewardCurCount >= self.m_SeasonChallengeGuaranteeCount:
            SeasonLog.Info('%s guarantee reward drop %s %s' % (self.m_Game.m_ID, self.m_SeasonChallengeNoRewardCurCount, self.m_SeasonChallengeGuaranteeCount))
            self.m_SeasonChallengeNoRewardCurCount = 0
            self.m_SeasonChallengeLayerRewardCount += 1
            return 1
        oGame = self.m_Game
        iRandom = oGame.Random(100) + 1
        if iRandom > iProp:
            self.m_SeasonChallengeNoRewardCurCount += 1
            return 0
        self.m_SeasonChallengeNoRewardCurCount = 0
        self.m_SeasonChallengeLayerRewardCount += 1
        return 1

    
    def ChooseSeasonChallengeDropModule(self, oHero):
        clsData = GetS7GoodsData(self.m_SeasonChallengeDropGoodSID)
        if not clsData:
            return []
        oGame = self.m_Game
        dHasChooseInfo = { }
        lstModule = []
        for oChooseFunc in clsData.m_InternalGoodRule:
            tResult = oChooseFunc(oGame, oHero, dHasChooseInfo, { }, { })
            if not tResult:
                continue
            (iSID, iQuality) = tResult
            dModuleData = {
                'SID': iSID,
                'QL': iQuality }
            oModule = clseason7.CreateModule(oGame, oModuleDataCon = None, dData = dModuleData)
            if not oModule:
                continue
            if oModule.m_SID not in SPECIAL_MODULE_DROP_DEFAULT_POINT:
                oModule.m_DefaultPoint = DROP_MODULE_DEFAULT_POINT
            lstModule.append(oModule)
        
        return lstModule

    
    def CheckSeasonChallengeCanDropModule(self, iLayer):
        if self.m_SeasonChallengeLayerRewardModuleNum >= self.m_SeasonChallengeLayerRewardLimit:
            SeasonLog.Info('%s seasonchallenge reward drop module limit: %s %s' % (self.m_Game.m_ID, self.m_SeasonChallengeLayerRewardModuleNum, self.m_SeasonChallengeLayerRewardLimit))
            return 0
        if iLayer in self.m_SeasonChallengeDropModuleWeight:
            iProp = self.m_SeasonChallengeDropModuleWeight[iLayer]
            oGame = self.m_Game
            iRandom = oGame.Random(100)
            if iRandom < iProp:
                self.m_SeasonChallengeLayerRewardModuleNum += 1
                return 1
        return 0

    
    def SeasonChallengeRewardModule(self, oHero, dInfo, iRewardAIHero):
        lstModule = self.ChooseSeasonChallengeDropModule(oHero)
        if lstModule:
            SeasonLog.Info('%s %s seasonchallenge reward drop module rewardaiflag: %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iRewardAIHero))
        if iRewardAIHero:
            for oModule in lstModule:
                oHero.m_BackpackCon.AddS7Item(oModule, 'SeasonChallengDrop')
            
        else:
            for idx, oModule in enumerate(lstModule):
                lstRewardModule = [
                    {
                        'item': VIRTUAL_ITEM_DROP,
                        'info': {
                            'DropType': NWARRIOR_DROP_S7MODULE,
                            'DropInfo': [
                                oModule],
                            'DropPos': (0, 0, 0) } }]
                iFakeMGID = FAKEMG_S7MOUDLE + idx * 1000
                dInfo[iFakeMGID] = (0, lstRewardModule, {
                    'Player': oHero.m_ID })
            

    
    def SeasonChallengeRewardCrystalInfo(self, oHero, dInfo, iRewardAIHero):
        oGame = self.m_Game
        iCrystalSID = CRYSTAL_RAWMATERIAL_SID
        clsCrystalData = clseason7.GetCrystalPerformCls(iCrystalSID)
        if not clsCrystalData:
            return None
        iTotalPoint = ChooseKey(oGame, clsCrystalData.m_CanChoosePoint)
        dCrystalData = {
            'SID': iCrystalSID,
            'TP': iTotalPoint }
        SeasonLog.Info('%s seasonchallenge reward drop crystal hero:%s rewardaiflag:%s' % (self.m_Game.m_ID, oHero.m_PlayerID, iRewardAIHero))
        if iRewardAIHero:
            lstReward = [
                {
                    'item': VIRTUAL_ITEM_S7CRYSTAL,
                    'info': dCrystalData }]
            cl_reward.RewardItem(oGame, oHero, lstReward, 'SeasonChallengeDrop')
        else:
            oCrystal = clseason7.CreateCrystal(oGame, oCrystalCon = None, dData = dCrystalData)
            if not oCrystal:
                return None
            lstReward = [
                {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_S7CRYSTAL,
                        'DropInfo': [
                            oCrystal],
                        'DropPos': (0, 0, 0) } }]
            dInfo[FAKEMG_S7CRYSTAL] = (0, lstReward, {
                'Player': oHero.m_ID })

    
    def OnChallengeEndCreateDemon(self, oWarMgr, oLevelCtrl, dMsgInfo):
        if 'MGInfo' not in dMsgInfo or dMsgInfo['ChallengeSID'] not in self.m_SeasonChallengePutWeight or dMsgInfo['ChallengeType'] != CHALLENGE_COUNT_MUTANTMONSTER:
            return None
        iLayer = self.GetSceneLayer(oLevelCtrl, dMsgInfo['Scene'])
        iCanDropCrystal = self.CheckSeasonChallengeCanDropCrystal(iLayer)
        iCanDropMoudle = self.CheckSeasonChallengeCanDropModule(iLayer)
        if not iCanDropCrystal and not iCanDropMoudle:
            return None
        oGame = self.m_Game
        for iHero, dInfo in dMsgInfo['MGInfo'].items():
            oHero = oGame.GetObject(iHero)
            if not oHero or not (oHero.m_FightType & WARRIOR_HERO):
                continue
            if oWarMgr.IsAIHero(iHero):
                if iCanDropCrystal:
                    self.SeasonChallengeRewardCrystalInfo(oHero, dInfo, iRewardAIHero = 1)
                if iCanDropMoudle:
                    self.SeasonChallengeRewardModule(oHero, dInfo, iRewardAIHero = 1)
                    continue
            if iCanDropCrystal:
                self.SeasonChallengeRewardCrystalInfo(oHero, dInfo, iRewardAIHero = 0)
            if iCanDropMoudle:
                self.SeasonChallengeRewardModule(oHero, dInfo, iRewardAIHero = 0)
        

    
    def RewardDropS7Item(self, iModuleNum, iCrystalNum, oAbandoner, sDropReason, iDropReason = DROP_REASON_NORMAL):
        if not oAbandoner:
            return None
        oGame = self.m_Game
        if not oGame:
            return None
        iScene = oAbandoner.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        vPos = cl_reward.GetDropBasePos(oAbandoner)
        iAbandoner = oAbandoner.m_ID
        (iLayer, iLevel) = cl_newformula.GetObjLayerAndLevel(oAbandoner)
        dTotalPoint2Crystal = GetTotalPoint2Crystal()
        for iHero in self.m_WarMgr.GetRoomHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dAllModule = oHero.m_BackpackCon.GetUnLockModule()
            lstModuleReward = []
            for _ in range(iModuleNum):
                iModuleSID = ChooseKey(oGame, dAllModule)
                dModuleData = {
                    'SID': iModuleSID,
                    'QL': QUALITY_NORMAL }
                oModule = clseason7.CreateModule(oGame, oModuleDataCon = None, dData = dModuleData)
                if not oModule:
                    continue
                lstModuleReward.append({
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_S7MODULE,
                        'DropInfo': [
                            oModule],
                        'DropPos': vPos } })
            
            cl_reward.RewardItem(oGame, oHero, lstModuleReward, 'PassBox', {
                'Player': iHero,
                'Abandoner': iAbandoner,
                'DropReason': iDropReason,
                'Scene': iScene })
            lstCrystalReward = []
            dAllCrystal = oHero.m_BackpackCon.GetUnLockCrystal()
            for _ in range(iCrystalNum):
                iCrystalTotalPoint = self.ChooseCrystalTotalPoint(oAbandoner, iLayer)
                if iCrystalTotalPoint not in dTotalPoint2Crystal:
                    SendAlert('err', '%s %s 抽取s7水晶总点数失败 %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, iCrystalTotalPoint, iLayer, iLevel))
                    continue
                dCrystal = dTotalPoint2Crystal[iCrystalTotalPoint]
                dCanChooseCrystal = { iWeight: iCrystal for iCrystal, iWeight in dCrystal.items() if iCrystal in dAllCrystal }
                iCrystalSID = ChooseKey(oGame, dCanChooseCrystal)
                if not iCrystalSID:
                    SendAlert('err', '%s %s 抽取s7水晶失败 %s' % (oGame.m_ID, oHero.m_PlayerID, iCrystalTotalPoint))
                    continue
                dCrystalData = {
                    'SID': iCrystalSID,
                    'TP': iCrystalTotalPoint }
                oCrystal = clseason7.CreateCrystal(oGame, oCrystalCon = None, dData = dCrystalData)
                if not oCrystal:
                    continue
                lstCrystalReward.append({
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_S7CRYSTAL,
                        'DropInfo': [
                            oCrystal],
                        'DropPos': vPos } })
            
            cl_reward.RewardItem(oGame, oHero, lstCrystalReward, sDropReason, {
                'Player': iHero,
                'Abandoner': iAbandoner,
                'DropReason': iDropReason,
                'Scene': iScene })
        

    
    def UnlockConEquipAreaSize(self, iLayerNum):
        oGame = self.m_Game
        if not oGame:
            return None
        dLayer2Size = self.m_KillLayerBossUnlockConEquipAreaSize
        if iLayerNum not in dLayer2Size:
            return None
        (iUnlockRow, iUnlockCol) = dLayer2Size[iLayerNum]
        for iHero in self.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oBackCon = oHero.m_BackpackCon
            if not oBackCon:
                continue
            oBackCon.UnlockEquipAreaSize(iUnlockRow, iUnlockCol, sReason = 'killboss')
        

    
    def GetCurBackPackData(self, oHero):
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon:
            return { }
        return oBackpackCon.GetBackPackData()

    
    def GetBackpackDamageInfo(self, iTotalDam, dInfo):
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in self.m_BackpackDamagePerform:
                return {
                    self.m_BackpackDamagePerform[iPerform]: iTotalDam }
        if 'RS' in dInfo and dInfo['RS'].m_Type == REASON_TYPE_PERFORM:
            iPerform = dInfo['RS'].m_Perform
            if iPerform in self.m_BackpackDamagePerform:
                return {
                    self.m_BackpackDamagePerform[iPerform]: iTotalDam }
        return { }

    
    def CheckEnable(self):
        return self.m_Enable

    
    def Save(self):
        dData = { }
        dData['CNRC'] = self.m_SeasonChallengeNoRewardCurCount
        dData['CLRC'] = self.m_SeasonChallengeLayerRewardCount
        dData['CLRN'] = self.m_SeasonChallengeLayerRewardModuleNum
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_SeasonChallengeNoRewardCurCount = dData.get('CNRC', 0)
        self.m_SeasonChallengeLayerRewardCount = dData.get('CLRC', 0)
        self.m_SeasonChallengeLayerRewardModuleNum = dData.get('CLRN', 0)

    
    def InitSeason7AnalyseCom(self):
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oBigdataMgr.InitSeason7AnalyseCom()

    
    def OnLevelGoalBefore(self, _oElement, oWarMgr, dInfo):
        oGame = self.m_Game
        iScene = dInfo['Scene']
        lstAIHero = oWarMgr.GetAllAIHero()
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        lstNPC = oScene.GetObjectsByType('NPC')
        for iNpc in lstNPC:
            oNpc = oGame.GetObject(iNpc)
            if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_S7SHOP:
                continue
            for iHero in lstAIHero:
                self.AIHeroAutoBuy(oNpc, iHero)
            
        

    
    def AIHeroAutoBuy(self, oNpc, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon:
            return None
        dGoodsData = oNpc.m_GoodsData
        oNpc.InitHeroGoods(oHero)
        if iHero not in dGoodsData:
            return None
        for iGoodPos, oGoods in oNpc.m_GoodsData[iHero].items():
            if oGoods.m_HasBuy >= oGoods.m_CanBuy:
                continue
            if oGoods.m_GoodsType == VIRTUAL_ITEM_S7CRYSTAL:
                oGoods.m_Cash = 0
                oNpc.BuyCrystal(oHero, iGoodPos)
                continue
            lstItems = oGoods.m_Items
            if not lstItems:
                continue
            iIndex = self.m_Game.Random(len(lstItems))
            if oGoods.m_GoodsType == VIRTUAL_ITEM_S7MODULE:
                iSID = lstItems[iIndex]['info']['SID']
            elif oGoods.m_GoodsType == VIRTUAL_ITEM_S7CRYSTALPACKET:
                iSID = lstItems[iIndex]['PacketKey']
            
            oGoods.m_Cash = 0
            oNpc.BuyPacket(oHero, iGoodPos, iSID)
        

    
    def GetAIMoudleWhite(self):
        return self.m_AIMoudleWhite

    
    def EnableHeroSeasonEffect(self, oHero, _dSeasonEffect):
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon:
            return None
        oBackpackCon.m_NeedEnableModule = 1
        oBackpackCon.AllPerformEnable()

    
    def DisableHeroSeasonEffect(self, oHero):
        oBackpackCon = oHero.m_BackpackCon
        if not oBackpackCon:
            return None
        oBackpackCon.AllPerformDisable()

    
    def EnableAIWhiteList(self, oHero):
        for iPerform in self.m_AIEnableWhitePF:
            oPerform = oHero.GetPerform(iPerform)
            if oPerform:
                oPerform.Enable(oHero, iNotify = 0)
        
        self.EnableHeroSeasonEffect(oHero, { })



def AutoPickCryStalDrop(oWarMgr, oHero, oDrop, sReason):
    if not oWarMgr or not oHero or not (oHero.m_Game):
        return None
    if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_S7CRYSTAL:
        return None
    SeasonLog.Info('%s %s auto pick s7crystal drop %s' % (oHero.m_Game.m_ID, oHero.m_ID, oDrop.m_DropInfo))
    oDrop.Pick(oHero.m_ID)


def GetComponentClass(oWarManager):
    return CBackpackElement

