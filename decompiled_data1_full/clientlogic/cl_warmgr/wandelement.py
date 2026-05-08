# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/wandelement.pyc
# RelativePath: clientlogic/cl_warmgr/wandelement.pyc
# Source Generated with Decompyle++
# File: wandelement.pyc (Python 3.6)

from cl_warmgr.mobject import CSeasonElement
from cl_commondefines import LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE, WANDPUT_INITIAL, WANDCOMPPUT_INITIAL, MAGIC_WAND_DAMAGE, PF_SUBMSG_COMMON, CURRENCY_CASH, LEVEL_TYPE_BOSS, WAND_CARDPACK, NPC_CB_VALUE, WAND_COMP_TYPE_CONDITION, NWARRIOR_DROP_WANDCOMP, NWARRIOR_DROP_MAGIC_WAND, WARRIOR_NORMAL, LEVEL_TYPE_FIGHT, ELITEINTRUDE_CHALLENGE, RECYCLE_DROP, WARRIOR_MONSTER, WARRIOR_HERO, MG_SOURCE_KILLMONSTER, S5_ITEM_TYPE_WAND, S5_ITEM_TYPE_COMP, WARRIOR_ELITE, WANDCOMPPUT_SHOPBUY, WAND_SUBMSG_ADDABILITY, WANDABILITY_ADDEXTCONCOMP, WAND_SUBMSG_ADD, PF_TYPE_WANDABILITY, ABILITY_TYPE_EXCLUSIVE, CARRY_WAND_ABILITY_MAX_NUM, PAIR_WAND
from cl_platformdata import GetWandPut, GetWandCompPut, GetWandCompRecycleInfo, GetWandRecycleInfo, GetWandPointAbility, GetWandExcludeAbility
from cl_object.logging import SeasonLog
from cl_only import Functor, DeepCopy, PY_FLAG_DEAD, ChooseKey
from cl_object.reason import REASON_TYPE_PERFORM
import cl_msgcenter
import cl_wand
import cl_npc.net as npcnet
import cl_snetwar
import cl_reward
import cl_object
import cl_state
import cl_perform
WANDSHOP_MAX_REFRESHTIMES = 2
INITWAND = 1001

class CWandElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'WandElement'
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_NpcSID = dConfig.get('WandShopNpc', 0)
        self.m_ReplaceAFPF = dConfig.get('ReplaceAFPF', { })
        self.m_RoomChallengeInfo = dConfig.get('RoomChallengeInfo', { })
        self.m_WandMGReward = dConfig.get('WandMG', { })
        self.m_WandDropLayerLimit = dConfig.get('WandDropLayerLimit', 2)
        self.m_CurLayerDropNum = 0
        self.m_GuaranteedDropNum = dConfig.get('GuaranteedDropCount', 10)
        self.m_CurKillNum = 0
        self.m_HeroTruePut = { }
        self.m_ShopCompExcludePut = { }
        self.m_Enable = 0
        self.m_WandCntChange = { }
        self.m_WandCardPackCache = { }
        self.m_ShopBuyWandRecord = { }
        self.m_RewardedLevel = { }
        self.m_WandPerform = dConfig.get('WandDamageStatistics', { })
        self.m_AbilityFloatingRange = dConfig.get('AbilityQualityFloatingRange', { })
        self.m_ReverseAbilityFloatingRange = dConfig.get('ReverseAbilityFloatingRange', { })
        self.m_AbilityChooseRatio = dConfig.get('AbilityChooseRatio', { })

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.m_Enable = 1
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnLoadPlayerInfo, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, self.m_CallFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelInit, self.m_CallFlag, iOnce = 0, iPriority = -1)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER_BEFORE, self.OnMonsterSuperBefore, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WANDCHANGE, self.OnAddWand, self.m_CallFlag, iSub = WAND_SUBMSG_ADD)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WAND, self.OnAddExtCompAbility, self.m_CallFlag, iSub = WAND_SUBMSG_ADDABILITY)
        oWarMgr.Set('PutWandNpc', 1)
        self.InitWandSeasonAnalyseCom()

    
    def InitWandSeasonAnalyseCom(self):
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oBigdataMgr.InitWandSeasonAnalyseCom()

    
    def Release(self):
        self.m_Enable = 0
        oWarMgr = self.m_WarMgr
        self.ClearWandCntChange()
        self.m_WandCardPackCache = { }
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER_BEFORE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WANDCHANGE, self.m_CallFlag, iSub = WAND_SUBMSG_ADD)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WAND, self.m_CallFlag, iSub = WAND_SUBMSG_ADDABILITY)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)
        
        self.m_WarMgr = None
        super().Release()

    
    def FilterAndFixAISeasonInfo(self, dDelegateAI):
        dDelegateAI['CurWand'] = INITWAND
        if 'CurWandComp' in dDelegateAI:
            dDelegateAI.pop('CurWandComp')
        if 'CarryAbility' in dDelegateAI:
            dDelegateAI.pop('CarryAbility')

    
    def DisableHeroSeasonEffect(self, oHero):
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return { }
        oWand = oWandCon.GetCurWand()
        if not oWand:
            return { }
        oWand.Disable()
        return { }

    
    def EnableHeroSeasonEffect(self, oHero, _dSeasonEffect):
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        oWand = oWandCon.GetCurWand()
        if not oWand:
            return None
        oWand.Enable()

    
    def CheckEnable(self):
        return self.m_Enable

    
    def Save(self):
        dData = {
            'SBWR': self.m_ShopBuyWandRecord }
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ShopBuyWandRecord = dData.get('SBWR', { })

    
    def OnLoadPlayerInfo(self, oElement, oWarMgr, dInfo):
        oHero = dInfo['Hero']
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        iPlayerID = oHero.m_PlayerID
        dPlayerInfo = dInfo['Info']
        if 'ShopCompExcludePut' in dPlayerInfo:
            self.m_ShopCompExcludePut[iPlayerID] = dPlayerInfo['ShopCompExcludePut']
        if 'UnlockInfo' in dPlayerInfo:
            self.m_HeroTruePut[iPlayerID] = dPlayerInfo['UnlockInfo']
        SeasonLog.Debug('%s %s s5loadinfo %s %s' % (self.m_Game.m_ID, iPlayerID, self.m_ShopCompExcludePut.get(iPlayerID, { }), self.m_HeroTruePut.get(iPlayerID, { })))

    
    def OnAddPlayer(self, oElement, oWarMgr, dInfo):
        oHero = dInfo['oCtrlHero']
        iPlayerID = oHero.m_PlayerID
        dPrice = oHero.SetDefault('RecycleDropPrice', { })
        for iType in (NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_WANDCOMP):
            dPrice[iType] = (0, self.m_CallFlag)
        
        oRecycleDropElement = oWarMgr.GetComponent('RecycleDropElement')
        if oRecycleDropElement:
            oRecycleDropElement.RefreshRecycleDropInfo(oHero)
        cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerformStart, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)
        if oWarMgr.m_IsUseRecord:
            return None
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        oGame = self.m_Game
        dInitialWandComp = self.GetWandCompPutWithFilter(iPlayerID, WANDCOMPPUT_INITIAL)
        for iInitWandComp in dInitialWandComp:
            oWandCon.AddBagComp(iInitWandComp, 1, 1, 'initial', iNotify = 0)
        
        SeasonLog.Debug('%s %s init initcomp: %s' % (oGame.m_ID, iPlayerID, dInitialWandComp))
        self.AddCarryWand(oHero, dInfo.get('CreateInfo', { }))

    
    def AddCarryWand(self, oHero, dPlayerInfo):
        oWarMgr = oHero.m_Game.m_WarMgr
        if oWarMgr.m_IsUseRecord:
            return None
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        oGame = self.m_Game
        iPlayerID = oHero.m_PlayerID
        iCurWand = dPlayerInfo.get('CurWand', 0)
        if not iCurWand:
            return None
        oCarryWand = oWandCon.RewardWand(iCurWand, 1, 'carrywand', iNotify = 0)
        if not oCarryWand:
            return None
        oWandCon.SetCurWand(oCarryWand.m_ID)
        lstCurWandComp = dPlayerInfo.get('CurWandComp', [])
        lstTrueRplComp = []
        if lstCurWandComp:
            oCarryWand.RemoveAllCustomComp()
            for iPos, iCompSID in lstCurWandComp:
                oWandCon.AddWandComp(oCarryWand.m_ID, iPos, iCompSID, 1)
                lstTrueRplComp.append((iPos, iCompSID))
            
        lstCarryAbility = dPlayerInfo.get('CarryAbility', [])
        lstTrueCarryAbility = self.CheckAndFixCarryAbility(oHero, iCurWand, lstCarryAbility)
        oCarryWand.SetCarryAbility(lstTrueCarryAbility)
        SeasonLog.Debug('%s %s carrywand: %d %s %s %s' % (oGame.m_ID, iPlayerID, iCurWand, lstCurWandComp, lstTrueRplComp, lstTrueCarryAbility))

    
    def CheckAndFixCarryAbility(self, oHero, iWandSID, lstAbility):
        iAbilityNum = len(lstAbility)
        if iAbilityNum > CARRY_WAND_ABILITY_MAX_NUM:
            lstAbility = lstAbility[:CARRY_WAND_ABILITY_MAX_NUM]
        clsWand = cl_wand.GetWandDataCls(iWandSID)
        lstPointAbility = GetWandPointAbility(iWandSID)
        lstEvolutionPointAbility = GetWandPointAbility(clsWand.m_EvolutionTarget)
        lstPointAbility.extend(lstEvolutionPointAbility)
        lstExcludeAbility = GetWandExcludeAbility(iWandSID)
        lstTrueAbility = []
        oGame = self.m_Game
        iPlayer = oHero.m_PlayerID
        for iAbilitySID, iQuality, iFloatingRange in lstAbility:
            if iAbilitySID in lstExcludeAbility:
                SeasonLog.Alert('%s %s checkcarryability inexclude %d %d %d %d' % (oGame.m_ID, iPlayer, iWandSID, iAbilitySID, iQuality, iFloatingRange))
                continue
            clsAbility = cl_perform.GetPerformModule(iAbilitySID)
            if not clsAbility or clsAbility.m_PFType != PF_TYPE_WANDABILITY:
                continue
            if clsAbility.m_AbilityType == ABILITY_TYPE_EXCLUSIVE and iAbilitySID not in lstPointAbility:
                SeasonLog.Alert('%s %s checkcarryability errtype %d %d %d %d' % (oGame.m_ID, iPlayer, iWandSID, iAbilitySID, iQuality, iFloatingRange))
                continue
            if clsAbility.m_QualityValue and iQuality not in clsAbility.m_QualityValue:
                SeasonLog.Alert('%s %s checkcarryability errquality %d %d %d %d' % (oGame.m_ID, iPlayer, iWandSID, iAbilitySID, iQuality, iFloatingRange))
                continue
            bIsAbilityValid = False
            if clsAbility.CheckCanFloating():
                dFloatingRange = self.GetFloatingRangeByType(clsAbility.m_IsReverseFloting).get(iQuality, (0, 0))
                if dFloatingRange[0] <= iFloatingRange and iFloatingRange <= dFloatingRange[1]:
                    bIsAbilityValid = True
                elif not iFloatingRange:
                    bIsAbilityValid = True
            if None:
                lstTrueAbility.append((iAbilitySID, iQuality, iFloatingRange))
                continue
            SeasonLog.Alert('%s %s checkcarryability errfloating %d %d %d %d' % (oGame.m_ID, iPlayer, iWandSID, iAbilitySID, iQuality, iFloatingRange))
        
        return lstTrueAbility

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFinishWar():
            return None
        if dInfo['LevelType'] != LEVEL_TYPE_BOSS or not (self.m_NpcSID):
            return None
        iLevelID = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'regrouprelicpos')
        dAddInfo = DeepCopy(dAddInfo)
        if not dAddInfo:
            return None
        iScene = dInfo['Scene']
        dMsgInfo = {
            'NPC': self.m_NpcSID,
            'LevelNode': oLevelNode,
            'NPCInfo': dAddInfo,
            'Scene': iScene }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
        if not dMsgInfo['NPC']:
            return None
        self.m_Game.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)

    
    def OnMonsterSuperBefore(self, oWarMgr, oTarget, dMsgInfo):
        if oTarget.m_FightType & WARRIOR_NORMAL == WARRIOR_NORMAL or oTarget.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            iAfPF = dMsgInfo['AfPF']
            if iAfPF not in self.m_ReplaceAFPF:
                return None
            oTarget.Set(f'''{self.m_CallFlag}-{oTarget.m_ID}''', 1)
            dMsgInfo['AfPF'] = self.m_ReplaceAFPF[iAfPF]

    
    def OnDie(self, oWarMgr, oTarget, dMsgInfo):
        if not (oTarget.m_FightType & WARRIOR_MONSTER) or not oTarget.Query(f'''{self.m_CallFlag}-{oTarget.m_ID}''', 0):
            return None
        self.m_CurKillNum += 1
        if self.m_CurLayerDropNum >= self.m_WandDropLayerLimit:
            return None
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl or not (oLevelCtrl.m_CurNode):
            return None
        iLevel = oLevelCtrl.m_CurNode.m_Level
        if iLevel in self.m_RewardedLevel:
            return None
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        iAttack = dMsgInfo['AID']
        oAttack = oGame.GetObject(iAttack)
        if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
            dHero = oScene.GetHeros()
            if not dHero:
                return None
            iAttack = ChooseKey(oGame, dHero)
        (iMiniGame, iRatio) = self.m_WandMGReward
        if self.m_CurKillNum < self.m_GuaranteedDropNum and oGame.Random(10000) >= iRatio:
            return None
        SeasonLog.Debug('%s dierewardwand %s %s' % (oGame.m_ID, iLevel, oScene.m_ID))
        self.m_CurKillNum = 0
        self.m_RewardedLevel[iLevel] = 1
        self.m_CurLayerDropNum += 1
        iTarget = oTarget.m_ID
        dExtInfo = {
            'CalOffset': 0,
            'Abandoner': iTarget,
            'AutoReward': 0,
            'CanReward': 0 }
        dMGInfo = cl_reward.RewardItemByMiniGame(oTarget, iAttack, {
            iMiniGame: (10000, 1) }, 'WandMGReward%s' % iTarget, MG_SOURCE_KILLMONSTER, dExtInfo)
        cl_reward.CreateDemon(oGame, iTarget, dMGInfo)

    
    def OnAddExtCompAbility(self, oWarMgr, oTarget, dMsgInfo):
        if 'Wand' not in dMsgInfo:
            return None
        iWand = dMsgInfo['Wand']
        oWancon = oTarget.m_WandCon
        oWand = oWancon.GetWandByID(iWand)
        if not oWand:
            return None
        if oWand.HasWandAbility(WANDABILITY_ADDEXTCONCOMP):
            oWancon.AddExtConCompMgrState({
                'WandInfo': {
                    iWand: 1 } })

    
    def OnAddWand(self, oWarMgr, oTarget, dMsgInfo):
        if 'WandSID' not in dMsgInfo or dMsgInfo['WandSID'] != PAIR_WAND:
            return None
        oTarget.m_WandCon.AddPairWandMgrState()
        self.OnAddExtCompAbility(oWarMgr, oTarget, dMsgInfo)

    
    def CheckWandDamage(self, iPerform):
        return iPerform in self.m_WandPerform

    
    def GetWandDamageInfo(self, iTotalDam, dInfo):
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in self.m_WandPerform:
                return {
                    self.m_WandPerform[iPerform]: iTotalDam }
        if 'RS' in dInfo and dInfo['RS'].m_Type == REASON_TYPE_PERFORM:
            iPerform = dInfo['RS'].m_Perform
            if iPerform in self.m_WandPerform:
                return {
                    self.m_WandPerform[iPerform]: iTotalDam }
        return { }

    
    def OnPerformStart(self, _oListener, _oHero, dMsgInfo):
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if not self.CheckWandDamage(iPerform):
            return None
        oSkill.m_Collect['ExShowTips'] = MAGIC_WAND_DAMAGE

    
    def GetCurWandData(self, oHero):
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return { }
        return oWandCon.GetCurWandData()

    
    def CacheCompCnt(self, iHero, iWand, iComp):
        if iHero not in self.m_WandCntChange or self.m_WandCntChange[iHero]['Wand'] != iWand:
            self.m_WandCntChange[iHero] = {
                'Wand': iWand,
                'Comp': [
                    iComp] }
        if 'Comp' in self.m_WandCntChange[iHero] or iComp not in self.m_WandCntChange[iHero]['Comp']:
            self.m_WandCntChange[iHero]['Comp'].append(iComp)
        else:
            self.m_WandCntChange[iHero]['Comp'] = [
                iComp]
        if self.Find_Call_Out('CacheCnt'):
            return None
        self.Call_Out(self.ProcessCntCache, 1, 'CacheCnt')

    
    def CacheWandCnt(self, iHero, iWand):
        if iHero not in self.m_WandCntChange or self.m_WandCntChange[iHero]['Wand'] != iWand:
            self.m_WandCntChange[iHero] = {
                'Wand': iWand,
                'WandCnt': 1 }
        else:
            self.m_WandCntChange[iHero]['WandCnt'] = 1
        if self.Find_Call_Out('CacheCnt'):
            return None
        self.Call_Out(self.ProcessCntCache, 1, 'CacheCnt')

    
    def ProcessCntCache(self):
        self.Remove_Call_Out('CacheCnt')
        dAllWandCntChange = self.m_WandCntChange
        self.m_WandCntChange = { }
        for iHero in dAllWandCntChange:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or not (oHero.m_WandCon):
                continue
            dWandCntChange = dAllWandCntChange[iHero]
            lstComp = dWandCntChange['Comp'] if 'Comp' in dWandCntChange else []
            bWandCnt = True if 'WandCnt' in dWandCntChange else False
            oHero.m_WandCon.ProcessCntCache(dWandCntChange['Wand'], lstComp, bWandCnt)
        

    
    def ClearWandCntChange(self):
        self.Remove_Call_Out('CacheWandCnt')
        self.m_WandCntChange = { }

    
    def AddShopBuyWandRecord(self, oHero, iWandSID):
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in self.m_ShopBuyWandRecord:
            self.m_ShopBuyWandRecord[iPlayerID] = {
                iWandSID: 1 }
        else:
            self.m_ShopBuyWandRecord[iPlayerID][iWandSID] = 1

    
    def GetShopBuyWandRecord(self, iPlayerID):
        if iPlayerID in self.m_ShopBuyWandRecord:
            return self.m_ShopBuyWandRecord[iPlayerID]
        return { }

    
    def RewardWandCardPack(self, oHero, iNpc, sReason, lstWand):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_WandCardPackCache:
            self.m_WandCardPackCache[iPlayer] = { }
        self.m_WandCardPackCache[iPlayer][iNpc] = lstWand
        self.SendWandCardPack(oHero, iNpc)

    
    def VaildRewardWand(self, iPlayer, iNpc):
        if iPlayer not in self.m_WandCardPackCache:
            return 0
        if iNpc not in self.m_WandCardPackCache[iPlayer]:
            return 0
        return 1

    
    def SendWandCardPack(self, oHero, iNpc):
        iPlayer = oHero.m_PlayerID
        if not self.VaildRewardWand(oHero.m_PlayerID, iNpc):
            return None
        lstWand = self.m_WandCardPackCache[iPlayer][iNpc]
        cbFun = Functor(self.TryRewardWand, iNpc, lstWand)
        npcnet.GS2CWandShopCardPackInfo(oHero, WAND_CARDPACK, lstWand)
        npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, cbFun)

    
    def TryRewardWand(self, iNpc, lstWand, oHero, iRewardPos):
        iPlayer = oHero.m_PlayerID
        if not self.VaildRewardWand(iPlayer, iNpc):
            return None
        self.m_WandCardPackCache[iPlayer].pop(iNpc)
        if not self.m_WandCardPackCache[iPlayer]:
            self.m_WandCardPackCache.pop(iPlayer)
        if iRewardPos + 1 > len(lstWand):
            return None
        (_, iWand, iLevel) = lstWand[iRewardPos]
        self.AddShopBuyWandRecord(oHero, iWand)
        self.TrueRewardWand(oHero, iWand, iLevel, sReason = 'wandcardpack')
        oHero.m_BuyMgr.RefreshShopUI()

    
    def TrueRewardWand(self, oHero, iWand, iLevel, sReason = ''):
        oGame = oHero.m_Game
        iPlayer = oHero.m_PlayerID
        SeasonLog.Debug('%s %s rewardwand %s-%s %s' % (oGame.m_ID, iPlayer, iWand, iLevel, sReason))
        iScene = oHero.m_Scene
        oWandCon = oHero.m_WandCon
        if not oWandCon.ValidAddWand():
            iHero = oHero.m_ID
            dExtraInfo = {
                'Abandoner': iHero }
            oWand = cl_wand.CreateWand(oGame, oWandCon, iWand, iLevel, { }, dTmp = {
                'NoInitComp': 1 })
            if not oWand:
                SeasonLog.Alert('%s %s %s wand %s reward fail %s' % (oGame.m_ID, iPlayer, iScene, iWand, sReason))
                return None
            dLevelInfo = oWand.GetWandLevelInfo()
            if oWand.m_Grade not in dLevelInfo:
                SeasonLog.Alert('%s %s %s wand %s-%s reward gradeerr %s' % (oGame.m_ID, iPlayer, iScene, iWand, oWand.m_Grade, sReason))
                return None
            (_, lstInitCondComp, _, lstInitActionComp, _, _) = dLevelInfo[oWand.m_Grade]
            for iType, dCompStatus in oWand.m_CompDismantleStatus.items():
                if iType == WAND_COMP_TYPE_CONDITION:
                    lstInitComp = lstInitCondComp
                else:
                    lstInitComp = lstInitActionComp
                for iPos, iStatus in dCompStatus.items():
                    if not iStatus:
                        continue
                    for iCompPos, (iCompSID, iCompLevel, _) in enumerate(lstInitComp):
                        if iCompPos != iPos:
                            continue
                        oWand.RemoveComp(iType, iPos, sReason)
                        if not iCompSID:
                            continue
                        oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_WANDCOMP, oHero.GetPos(), [
                            {
                                'WandCompSID': iCompSID,
                                'WandCompLevel': iCompLevel }], dExtraInfo, { }, iHero)
                    
                
            
            oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_MAGIC_WAND, oHero.GetPos(), [
                oWand], dExtraInfo, { }, iHero)
        else:
            oWandCon.RewardWand(iWand, iLevel, sReason)

    
    def CalRecycleWandPrice(self, oWand):
        return oWand.m_Grade * 50

    
    def CalRecycleWandCompPrice(self, iComp, iLevel):
        clsWandComp = cl_wand.GetWandCompCls(iComp)
        if not clsWandComp:
            return 0
        return iLevel * 10

    
    def OnLevelStart(self, _oElement, oWarMgr, dInfo):
        if dInfo['LevelType'] == LEVEL_TYPE_HIDE:
            return None
        dWandCardPackCache = self.m_WandCardPackCache
        self.m_WandCardPackCache = { }
        for iPlayer, dWandInfo in dWandCardPackCache.items():
            oHero = oWarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            for lstWand in dWandInfo.values():
                iPos = self.m_Game.Random(len(lstWand))
                (_, iWand, iLevel) = lstWand[iPos]
                self.TrueRewardWand(oHero, iWand, iLevel, sReason = 'levelpass')
            
        

    
    def ValidRecycleDrop(self, oHero, oDrop):
        if oDrop.m_ReleaseFlag:
            SeasonLog.Debug('%d recycle failed release %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_ID, oDrop.m_Owner))
            return 0
        if oDrop.m_Source and oDrop.m_Source != oHero.m_PlayerID:
            SeasonLog.Debug('%d recycle failed owner %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_ID, oDrop.m_Source))
            return 0
        iFightType = oDrop.m_FightType
        if iFightType == NWARRIOR_DROP_MAGIC_WAND:
            oWand = oDrop.m_DropInfo[0]
            if not GetWandRecycleInfo(oWand.m_SID):
                return 0
        if not iFightType == NWARRIOR_DROP_WANDCOMP or GetWandCompRecycleInfo(oDrop.m_WandCompSID):
            return 0
        return 0

    
    def RecycleDrop(self, oHero, oDrop, sReason, iNotify = 1):
        iPrice = 0
        iCanRecycle = self.ValidRecycleDrop(oHero, oDrop)
        if iCanRecycle:
            dMsgInfo = { }
            if oDrop.m_FightType == NWARRIOR_DROP_MAGIC_WAND:
                oWand = oDrop.m_DropInfo[0]
                iPrice = self.CalRecycleWandPrice(oWand)
            else:
                iCompSID = oDrop.m_WandCompSID
                iLevel = oDrop.m_WandCompLevel
                iPrice = self.CalRecycleWandCompPrice(iCompSID, iLevel)
            dMsgInfo['RecycleDropType'] = oDrop.m_FightType
            oDrop.Remove(sReason)
            iPrice = oHero.AddCash(iPrice, sReason)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, dMsgInfo, iSub = RECYCLE_DROP)
        if iNotify:
            cl_snetwar.GS2CRecycleDropResult(self.m_Game, oDrop.m_ID, oHero.m_ID, iCanRecycle, CURRENCY_CASH, iPrice, self.m_Game.GetRealPlayers())

    
    def OnLevelNodeFinish(self, _oElement, oWarMgr, dInfo):
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        dHero = { }
        for iHero in oWarMgr.GetAllHero():
            oHero = self.m_Game.GetObject(iHero, PY_FLAG_DEAD)
            if not oHero:
                continue
            dHero[oHero.m_ID] = oHero
        
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            oScene = oGame.m_SceneMgr.GetScene(oNode.m_Scene)
            if not oScene:
                continue
            lstDrop = oScene.GetObjectsByType('Drop')
            for iDrop in lstDrop:
                oDrop = self.m_Game.GetObject(iDrop)
                if not oDrop:
                    continue
                iHero = oDrop.m_Owner
                iAbandoner = oDrop.Abandoner()
                if iHero in dHero:
                    oHero = dHero[iHero]
                elif iAbandoner in dHero:
                    oHero = dHero[iAbandoner]
                
                iCanPick = self.ValidRecycleDrop(oHero, oDrop)
                if not iCanPick:
                    continue
                oDrop.Pick(oHero.m_ID)
            
        

    
    def OnLayerStart(self, oListener, oLevelCtrl, dMsgInfo):
        self.m_RewardedLevel = { }
        self.m_CurLayerDropNum = 0

    
    def OnLevelInit(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType != LEVEL_TYPE_FIGHT:
            return None
        iLevel = dInfo['LevelID']
        iLevelNum = dInfo['Level']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayerNum = oLevelCtrl.m_LayerNum
        iBaseLayerNum = oWarMgr.GetBaseLayer(iLayerNum)
        iNewVerLayer = oWarMgr.GetNewVerLayer()
        tLevelInfo = (iBaseLayerNum, iLevelNum, iNewVerLayer)
        if tLevelInfo not in self.m_RoomChallengeInfo:
            return None
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        dChooseChallenge = oLevelCtrl.m_RoomChallenge.GetChooseChallengeInfo()
        iLastRoomPos = len(oLevelNode.m_RoomList) - 1
        iSeasonChallenge = self.m_RoomChallengeInfo[tLevelInfo]
        SeasonLog.Debug('%d wand challenge %d %d %s %d' % (self.m_Game.m_ID, iLevel, iLastRoomPos, tLevelInfo, iSeasonChallenge))
        for iRoomPos in range(len(oLevelNode.m_RoomList)):
            tLevel = (iLevel, iRoomPos)
            if tLevel not in dChooseChallenge:
                continue
            iChallenge = dChooseChallenge[tLevel]
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallenge)
            if not clsChallengeData:
                continue
            if clsChallengeData.m_Type in ELITEINTRUDE_CHALLENGE:
                dChooseChallenge.pop(tLevel)
        
        dChooseChallenge[(iLevel, iLastRoomPos)] = iSeasonChallenge

    
    def GetTruePutByType(self, iPlayerID, iType):
        if iType not in (S5_ITEM_TYPE_WAND, S5_ITEM_TYPE_COMP):
            return { }
        if iPlayerID not in self.m_HeroTruePut or iType not in self.m_HeroTruePut[iPlayerID]:
            return { }
        return self.m_HeroTruePut[iPlayerID][iType]

    
    def GetWandPutWithFilter(self, iPlayerID, iSource):
        setWandPutFilter = set(GetWandPut(iSource)) & set(self.GetTruePutByType(iPlayerID, S5_ITEM_TYPE_WAND))
        if not setWandPutFilter:
            SeasonLog.Alert('%s %s %s wandputfilter err %s %s' % (self.m_Game.m_ID, iPlayerID, iSource, GetWandPut(iSource), self.GetTruePutByType(iPlayerID, S5_ITEM_TYPE_WAND)))
            return { }
        return dict.fromkeys(setWandPutFilter, 1)

    
    def GetWandCompPutWithFilter(self, iPlayerID, iSource):
        setWandCompPutFilter = set(GetWandCompPut(iSource)) & set(self.GetTruePutByType(iPlayerID, S5_ITEM_TYPE_COMP))
        if not setWandCompPutFilter:
            SeasonLog.Alert('%s %s %s wandcompputfilter err %s %s' % (self.m_Game.m_ID, iPlayerID, iSource, GetWandCompPut(iSource), self.GetTruePutByType(iPlayerID, S5_ITEM_TYPE_COMP)))
            return { }
        return dict.fromkeys(setWandCompPutFilter, 1)

    
    def GetShopWandCompPut(self, iPlayerID):
        if iPlayerID not in self.m_ShopCompExcludePut:
            return { }
        setShopCompPut = set(GetWandCompPut(WANDCOMPPUT_SHOPBUY)) - set(self.m_ShopCompExcludePut[iPlayerID])
        if not setShopCompPut:
            SeasonLog.Alert('%s %s shopcompput err %s %s' % (self.m_Game.m_ID, iPlayerID, GetWandCompPut(WANDCOMPPUT_SHOPBUY), self.m_ShopCompExcludePut[iPlayerID]))
            return { }
        return dict.fromkeys(setShopCompPut, 1)

    
    def GetRandomAbilityFloatingRange(self, iQuality, iReverse = 0):
        dRange = self.GetFloatingRangeByType(iReverse)
        if iQuality not in dRange:
            return 0
        oGame = self.m_Game
        tRange = dRange[iQuality]
        if not tRange or len(tRange) != 2:
            SeasonLog.Debug('%s get range fail %s %s' % (oGame.m_ID, iQuality, tRange))
            return 0
        (iMin, iMax) = tRange
        iCount = (iMax - iMin) // 10 + 1
        dRangeWeight = { }
        for i in range(iCount):
            dRangeWeight[iMin + i * 10] = 1
        
        return ChooseKey(oGame, dRangeWeight)

    
    def GetFloatingRangeByType(self, iReverse = 0):
        if iReverse:
            return self.m_ReverseAbilityFloatingRange
        return self.m_AbilityFloatingRange

    
    def GetNegativeRatio(self):
        if 'NegativeRatio' not in self.m_AbilityChooseRatio:
            return 0
        return self.m_AbilityChooseRatio['NegativeRatio']

    
    def GetAbilityQualityWeight(self, iHasNegative):
        if iHasNegative:
            return self.m_AbilityChooseRatio.get('HasNegative', { })
        return self.m_AbilityChooseRatio.get('NotNegative', { })



def GetComponentClass(oWarManager):
    return CWandElement

