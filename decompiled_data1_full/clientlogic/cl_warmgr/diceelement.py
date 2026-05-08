# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/diceelement.pyc
# RelativePath: clientlogic/cl_warmgr/diceelement.pyc
# Source Generated with Decompyle++
# File: diceelement.pyc (Python 3.6)

from cl_warmgr.mobject import CSeasonElement
from cl_cscommondef import WARRIOR_BOSS, BOSS_DONOT_COUNT, NWARRIOR_NPC_PASSBOX, LEVEL_TYPE_FIGHT, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_DICE, DROP_REASON_NPCREWARD, DICEPUT_MAX_LAYER, LEVEL_TYPE_BOSS, DICE_QUALITY_ALL, RECYCLE_DROP, CURRENCY_CASH, NWARRIOR_DROP_DICESPECIALITEM, DICE_QUALITY_LOW, DICE_QUALITY_HIGH, MODE_SNOWMOUNTAINS, TYPE_ASSEMBLE, CHALLENGE_DICESEASON_APPENDSKILL, MG_DICE, DICETAG_AI
from cl_only import ChooseKey, Time2Frame, Functor, DeepCopy, ShufferList
from cl_platformdata import GetExcludeDiceQuality, GetDiceSpecialItemByQuality, GetAIDice, GetDiceAIMapping, GetDiceTagListInfo
from cl_object.logging import SeasonLog
from cl_object.reason import REASON_TYPE_PERFORM
import cl_msgcenter
import cl_reward
import cl_dice
import cl_formula
import cl_snetwar
import cl_dice.net as dicenet
POINTWEIGHT_MAX = 10000
GUARANTE_ROOMPOS = 2
IGNORE_LAYER = 1
IGNORE_LEVEL = 1
AI_NEED_SEASONTALENTPF = [
    6623]
ROLL_POINT_DEFAULT_WEIGHT = {
    6: 10,
    12: 10,
    18: 10 }
DEFAULT_ROLLPOINT_RANGE = 6
DEFAULT_ROLL_POINT_MAX_WEIGHT = 40

class CDiceElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'DiceElement'
        self.m_Enable = 0
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_TempPointRange = dConfig.get('TempPointRange', { })
        self.m_MaxDicePoint = self.InitMaxDicePoint()
        self.m_DiceRewardNum = dConfig.get('DiceRewardNum', 0)
        self.m_DiceRewardDelay = dConfig.get('DiceRewardDelay', 0)
        self.m_DropDiceConfig = dConfig.get('DropDiceConfig', { })
        self.m_DiceRewardConfig = dConfig.get('DiceRewardConfig', { })
        self.m_NpcSID = dConfig.get('DiceShopNpc', 0)
        self.m_ExtraDiceShop = dConfig.get('ExtraDiceShop', { })
        self.m_UseExtraDiceShop = 0
        self.m_ChallengeLvWeightInfo = dConfig.get('ChallengeLvWeightInfo', { })
        self.m_ChallengeLvToPoint = dConfig.get('ChallengeLvToPoint', { })
        self.m_ChallengePutInfo = dConfig.get('ChallengePutInfo', [])
        self.m_ChallengeIgnoreInfo = dConfig.get('ChallengeIgnoreInfo', [])
        self.m_ChallengePutWeight = dConfig.get('ChallengePutWeight', 1)
        self.m_SelectionPacketDropInfo = dConfig.get('SelectionPacketDropInfo', { })
        self.m_PacketChallengeDropInfo = dConfig.get('PacketChallengeDropInfo', { })
        self.m_SelectionPacketQualityInfo = dConfig.get('SelectionPacketQualityInfo', { })
        self.m_DiceEnergyInfo = dConfig.get('DiceEnergyInfo', { })
        self.m_DiceQualityAddEnergy = dConfig.get('DiceQualityAddEnergy', { })
        self.m_DropDiceShape = dConfig.get('DropDiceShape', { })
        self.m_DiceDamagePerform = dConfig.get('DiceDamagePerform', { })
        self.m_WarInitDiceEnergy = dConfig.get('WarInitDiceEnergy', 0)
        self.m_PacketDropTimes = { }
        self.m_AccumulatedChallengePoint = 0
        self.m_UnLockDiceInfo = { }
        self.m_UnlockSpecailItemInfo = { }
        self.m_BaseRollPointWeight = self.InitRollPointWeight(dConfig.get('BaseRollPointWeight', ROLL_POINT_DEFAULT_WEIGHT))
        self.m_HeroRollPointWeight = { }

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.m_Enable = 1
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, self.m_CallFlag)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeEnd, self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, self.m_CallFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, self.m_CallFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnAddPlayerInfo, self.m_CallFlag, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE_BEFORE, self.ChooseChallengeBefore, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.OnChooseChallenge, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.OnChooseNpcPre, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        oWarMgr.Set('PutDiceNpc', 1)
        self.InitDiceSeasonAnalyseCom()

    
    def Release(self):
        self.m_Enable = 0
        oWarMgr = self.m_WarMgr
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.m_CallFlag)
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE_BEFORE, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        self.m_WarMgr = None
        super().Release()

    
    def FilterAndFixAISeasonInfo(self, dDelegateAI):
        if 'UnLockAbilityDesc' in dDelegateAI:
            dDelegateAI.pop('UnLockAbilityDesc')
        if 'SignInfo' in dDelegateAI:
            dDelegateAI.pop('SignInfo')

    
    def DisableHeroSeasonEffect(self, oHero):
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return { }
        oDiceCon.AllPerformDisable()
        sReason = 'AIMapping'
        dDisAssembleDice = { }
        dDiceAIMapping = GetDiceAIMapping()
        dAssembledDice = oDiceCon.GetAssembleDice()
        for iPos, iDice in dAssembledDice.items():
            oDice = oDiceCon.GetDiceByID(iDice)
            if not oDice:
                continue
            iDiceSID = oDice.m_SID
            iDiceQuality = oDice.m_Quality
            if iDiceSID in dDiceAIMapping:
                iAIDiceSID = dDiceAIMapping[iDiceSID]
                if DICETAG_AI not in GetDiceTagListInfo(iAIDiceSID):
                    continue
                oAIDice = self.CreateSimpleDice(oHero, iAIDiceSID, iDiceQuality, sReason = sReason)
                if not oAIDice:
                    continue
                oDiceCon.AddDiceToContainer(oAIDice, sReason = sReason)
                oAIDice.SetPoint(oDice.m_RollPoint, sReason = sReason)
                dDisAssembleDice[iPos] = oDice.m_ID
                oDiceCon.AssembleDice(oAIDice.m_ID, iPos, TYPE_ASSEMBLE, sReason = 'AITakeOver')
        
        dNextThrowItemCache = oDiceCon.m_NextThrowItemCache
        if dNextThrowItemCache:
            dNextThrowItemCache.clear()
        dicenet.GS2CDiceSpecialItemInfo(oHero.m_PlayerID, oDiceCon.m_NextThrowItemCache)
        oPerformCom = oHero.m_Perform
        for iAIPerform in AI_NEED_SEASONTALENTPF:
            if iAIPerform in oPerformCom.m_Perform:
                oPerform = oPerformCom.m_Perform[iAIPerform]
                oPerform.Enable(oHero, iNotify = 0)
        
        return dDisAssembleDice

    
    def EnableHeroSeasonEffect(self, oHero, _dSeasonEffect):
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return None
        for iPos, iDice in _dSeasonEffect.items():
            oDiceCon.AssembleDice(iDice, iPos, TYPE_ASSEMBLE, sReason = 'AIHandOver')
        
        oDiceCon.RemoveAIDice()
        oDiceCon.AllPerformEnable()
        oDiceCon.EffectSpecialItem()

    
    def CreateSimpleDice(self, oHero, iDiceSID, iDiceQuality, sReason = ''):
        oGame = self.m_Game
        dDiceInfo = {
            'SID': iDiceSID,
            'QL': iDiceQuality,
            'PR': self.GetTempPointRangeByQuality(iDiceQuality) }
        oDice = cl_dice.CreateDice(oGame, oDiceCon = None, dDiceInfo = dDiceInfo)
        if not oDice:
            SeasonLog.Debug('%d createsimpledice err %d %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dDiceInfo, sReason))
            return None
        SeasonLog.Debug('%d createsimpledice %d %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dDiceInfo, sReason))
        return oDice

    
    def CheckEnable(self):
        return self.m_Enable

    
    def Save(self):
        dData = {
            'PDT': self.m_PacketDropTimes,
            'ACP': self.m_AccumulatedChallengePoint,
            'ULD': self.m_UnLockDiceInfo,
            'ULSI': self.m_UnlockSpecailItemInfo }
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_PacketDropTimes = dData.get('PDT', { })
        self.m_AccumulatedChallengePoint = dData.get('ACP', 0)
        self.m_UnLockDiceInfo = dData.get('ULD', { })
        self.m_UnlockSpecailItemInfo = dData.get('ULSI', { })

    
    def InitDiceSeasonAnalyseCom(self):
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oBigdataMgr.InitDiceSeasonAnalyseCom()

    
    def OnAddPlayer(self, oElement, oWarMgr, dInfo):
        if oWarMgr.m_IsUseRecord:
            return None
        oHero = dInfo['oCtrlHero']
        self.AddSeasonDropRecyclePrice(oHero, {
            NWARRIOR_DROP_DICE: 0 }, self.m_CallFlag)
        dPlayerInfo = dInfo.get('CreateInfo', { })
        oDiceCon = oHero.m_DiceCon
        pid = oHero.m_PlayerID
        if 'UnLockDice' in dPlayerInfo:
            self.m_UnLockDiceInfo[pid] = dict.fromkeys(set(dPlayerInfo['UnLockDice']) - set(GetAIDice()), 1)
        if 'UnLockSpecailItem' in dPlayerInfo:
            self.m_UnlockSpecailItemInfo[pid] = dPlayerInfo['UnLockSpecailItem']
        if 'UnLockAbilityDesc' in dPlayerInfo:
            oDiceCon.m_UnLockAbilityDesc = dPlayerInfo['UnLockAbilityDesc']
        if 'SpecialItemInfo' in dPlayerInfo:
            oDiceCon.AddCarrySpecItem(dPlayerInfo['SpecialItemInfo'], iIsAI = dPlayerInfo.get('IsAI', 0))
        if 'SignInfo' in dPlayerInfo:
            oDiceCon.UpdateSignInfo(dPlayerInfo['SignInfo'])
        oDiceCon.ChangeDiceEnergy(self.m_WarInitDiceEnergy, 'AddPlayer')

    
    def OnAddPlayerInfo(self, oWarMgr, dInfo):
        oHero = dInfo['Hero']
        if not oHero:
            return None
        pid = oHero.m_PlayerID
        self.InitHeroRollPointWeight(pid)

    
    def InitRollPointWeight(self, dWeightInfo):
        dBaseWeight = { }
        for iMaxPointRange, iWeight in dWeightInfo.items():
            dBaseWeight[iMaxPointRange] = { iWeight: iPoint for iPoint in range(1, iMaxPointRange + 1) }
        
        return dBaseWeight

    
    def InitHeroRollPointWeight(self, pid):
        self.m_HeroRollPointWeight[pid] = DeepCopy(self.m_BaseRollPointWeight)

    
    def OnAddAllPlayer(self, oWarMgr, oHero, dMsgInfo):
        oGame = self.m_Game
        oRecycleDropElement = oWarMgr.GetComponent('RecycleDropElement')
        if oRecycleDropElement:
            oRecycleDropElement.AddCustomRecycleRule(NWARRIOR_DROP_DICE, RecycleDiceDrop)
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.Query('UseExtraDiceShop'):
                self.m_UseExtraDiceShop = 1
                break
        

    
    def InitMaxDicePoint(self):
        iMaxDicePoint = 0
        for dPointRange in self.m_TempPointRange.values():
            lstPointRange = []
            for lstRange in dPointRange.values():
                lstPointRange.extend(lstRange)
            
            iQualityMaxPoint = max(lstPointRange)
            if iQualityMaxPoint > iMaxDicePoint:
                iMaxDicePoint = iQualityMaxPoint
        
        return iMaxDicePoint

    
    def GetTempPointRangeByQuality(self, Quality):
        if Quality not in self.m_TempPointRange:
            return { }
        return self.m_TempPointRange[Quality]

    
    def GetMaxDicePoint(self):
        return self.m_MaxDicePoint

    
    def GetSceneLayer(self, oLevelCtrl, iScene):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return 0
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if not oLevelNode:
            return 0
        return min(DICEPUT_MAX_LAYER, oLevelNode.m_LayerNum)

    
    def GetIncreaseEnergy(self, oHero, iEnergy):
        return iEnergy * (100 + oHero.Query('S6GetEnergyIncrease', 0)) // 100

    
    def OnDie(self, oWarMgr, oTarget, dMsgInfo):
        if oTarget.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS or oTarget.m_FightType in BOSS_DONOT_COUNT:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFinishWar():
            return None
        oGame = self.m_Game
        iScene = oTarget.m_Scene
        iLayer = self.GetSceneLayer(oLevelCtrl, iScene)
        iEnergy = self.m_DiceEnergyInfo['KillBoss'].get(iLayer, 0)
        if not iEnergy:
            return None
        setHero = set(oWarMgr.GetLiveHero()) | set(oWarMgr.GetAllAIHero())
        for iHero in setHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oDiceCon = oHero.m_DiceCon
            if not oDiceCon:
                continue
            oDiceCon.AddMaxAssemblyNum(iAdd = 1)
            self.DropDice(oTarget, oHero, iScene, iLayer)
            iTrueEnergy = self.GetIncreaseEnergy(oHero, iEnergy)
            oDiceCon.ChangeDiceEnergy(iTrueEnergy, 'KillBoss')
        

    
    def OnChallengeEnd(self, oWarMgr, oLevelCtrl, dMsgInfo):
        if dMsgInfo['SID'] not in self.m_ChallengePutInfo:
            return None
        dEnergy = { }
        iEnergy = 0
        iDiceSeasonChallengeFlag = 0
        iLayer = self.GetSceneLayer(oLevelCtrl, dMsgInfo['Scene'])
        tLineIdx = (dMsgInfo['LevelID'], dMsgInfo['Room'], 0)
        oChallenge = oLevelCtrl.m_RoomChallenge.GetChallenge(tLineIdx)
        if oChallenge.m_Type == CHALLENGE_DICESEASON_APPENDSKILL:
            dEnergy = oChallenge.m_DiceEnergy
            iDiceSeasonChallengeFlag = 1
        else:
            iEnergy = self.m_DiceEnergyInfo['SeasonChallenge'].get(iLayer, 0)
            if not iEnergy:
                return None
        setHero = set(oWarMgr.GetLiveHero()) | set(oWarMgr.GetAllAIHero())
        for iHero in setHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oDiceCon = oHero.m_DiceCon
            if not oDiceCon:
                continue
            if iDiceSeasonChallengeFlag:
                iTrueEnergy = dEnergy[oHero.m_PlayerID] if oHero.m_PlayerID in dEnergy else 0
            else:
                iTrueEnergy = self.GetIncreaseEnergy(oHero, iEnergy)
            oDiceCon.ChangeDiceEnergy(iTrueEnergy, 'SeasonChallenge')
            if oWarMgr.IsAIHero(iHero):
                self.AddAIRandomDice(oLevelCtrl, oHero, oDiceCon, iLayer, tLineIdx)
        

    
    def AddAIRandomDice(self, oLevelCtrl, oHero, oDiceCon, iLayer, tLineIdx):
        oGame = self.m_Game
        oChallenge = oLevelCtrl.m_RoomChallenge.GetChallenge(tLineIdx)
        if oChallenge.m_Type == CHALLENGE_DICESEASON_APPENDSKILL:
            dChooseQualityWeight = { }
            dReward = oChallenge.m_RecordReward
            iRound = self.m_WarMgr.m_Round
            dMiniGame = dReward[iRound] if iRound in dReward else { }
            for iRewardSID in dMiniGame:
                clsData = oGame.m_WarData.GetMiniGameData(iRewardSID)
                if clsData and clsData.m_Type == MG_DICE:
                    dChooseQualityWeight = clsData.m_ChooseQualityWeight
                    break
            
            if not dChooseQualityWeight or iLayer not in dChooseQualityWeight:
                return None
            iQuality = ChooseKey(oGame, dChooseQualityWeight[iLayer])
            if not iQuality:
                return None
            dDiceAIMapping = GetDiceAIMapping()
            sReason = 'AIRandomDice'
            dChooseWeight = self.GetAbilityFilterExcludeQuality(oHero.m_PlayerID, iQuality)
            iChooseDice = ChooseKey(oGame, dChooseWeight)
            oDice = self.CreateSimpleDice(oHero, iChooseDice, iQuality, sReason = sReason)
            if not oDice:
                return None
            oDiceCon.AddDiceToContainer(oDice, sReason = sReason)
            oDiceCon.RollDice(oDice.m_ID, sReason = sReason)
            if iChooseDice in dDiceAIMapping:
                iAIDice = dDiceAIMapping[iChooseDice]
                oAIDice = self.CreateSimpleDice(oHero, iAIDice, iQuality, sReason = sReason)
                if not oAIDice:
                    return None
                oDiceCon.AddDiceToContainer(oAIDice, sReason = sReason)
                iBaseRollPoint = oDice.m_RollPoint
                if iBaseRollPoint:
                    oAIDice.SetPoint(iBaseRollPoint, sReason = sReason)
                else:
                    oDiceCon.RollDice(oAIDice.m_ID, sReason = sReason)
                self.AIPickUpDice(oDiceCon, oAIDice)
            else:
                self.AIPickUpDice(oDiceCon, oDice)

    
    def AIPickUpDice(self, oDiceCon, oDice):
        if not oDice.GetRollType():
            return None
        sReason = 'AIPickUpDice'
        dAssembleDice = oDiceCon.GetAssembleDice()
        iAssembleDiceNum = len(dAssembleDice)
        iDiceSID = oDice.m_SID
        iDice = oDice.m_ID
        iAssembleNum = oDiceCon.m_AssembleNum.setdefault(iDiceSID, 0)
        if iAssembleNum or iAssembleDiceNum < oDiceCon.GetMaxAssemblyNum():
            iAssemblePos = oDiceCon.GetNextCanAssemblePos()
            oDiceCon.AssembleDice(iDice, iAssemblePos, TYPE_ASSEMBLE, sReason = sReason)
        else:
            iSameNameDice = oDiceCon.GetDiceBySID(iDiceSID, bAssemble = True)
            oSameNameDice = oDiceCon.GetDiceByID(iSameNameDice)
            if oSameNameDice and oSameNameDice.m_RollPoint < oDice.m_RollPoint:
                oDiceCon.AssembleDice(iDice, oSameNameDice.m_AssemblePos, TYPE_ASSEMBLE, sReason = sReason)

    
    def OnChooseNpcPre(self, oWarMgr, oLevelCtrl, dMsgInfo):
        sType = dMsgInfo['Type']
        if sType != 'diceshop':
            return None
        iLevelNum = dMsgInfo['LevelNum']
        iLayerNum = dMsgInfo['LayerNum']
        dExtraDiceShop = self.m_ExtraDiceShop.get(iLayerNum, { })
        if not (self.m_UseExtraDiceShop) and iLevelNum in dExtraDiceShop:
            dMsgInfo['NpcWeight'] = { }

    
    def GetSelectionPacketDrop(self, iQuality):
        if iQuality not in self.m_SelectionPacketQualityInfo:
            return 0
        return self.m_SelectionPacketQualityInfo[iQuality]

    
    def DropDice(self, oTarget, oHero, iScene, iLayer):
        iLayer = min(DICEPUT_MAX_LAYER, iLayer)
        if iLayer not in self.m_DropDiceConfig:
            return None
        oGame = self.m_Game
        dDropDiceConfig = self.m_DropDiceConfig[iLayer]
        if not dDropDiceConfig:
            return None
        vBasePos = cl_reward.GetDropBasePos(oTarget)
        iTarget = oTarget.m_ID
        vPos = cl_reward.GetDropFixPos(oGame, oHero, iScene, vBasePos, iTarget)
        dDropDice = { }
        for iQuality, iNum in dDropDiceConfig.items():
            dChooseWeight = self.GetAbilityFilterExcludeQuality(oHero.m_PlayerID, iQuality)
            for _ in range(iNum):
                iChooseDiceAbility = ChooseKey(oGame, dChooseWeight)
                oDice = self.CreateSimpleDice(oHero, iChooseDiceAbility, iQuality, sReason = 'DropDice')
                if not oDice:
                    continue
                if iQuality not in dDropDice:
                    dDropDice[iQuality] = {
                        iChooseDiceAbility: 1 }
                elif iChooseDiceAbility not in dDropDice[iQuality]:
                    dDropDice[iQuality][iChooseDiceAbility] = 1
                else:
                    dDropDice[iQuality][iChooseDiceAbility] += 1
                oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_DICE, vPos, [
                    oDice], {
                    'Abandoner': iTarget }, { }, oHero.m_ID, iSplit = 1)
            
        
        SeasonLog.Debug('%s %s %s %s drop dice %s' % (oGame.m_ID, iScene, iLayer, oHero.m_PlayerID, dDropDice))

    
    def DropDiceSpecialItem(self, oTarget, oHero, sReason):
        oGame = self.m_Game
        dLowSpecialItem = GetDiceSpecialItemByQuality(DICE_QUALITY_LOW)
        dHighSpecialItem = GetDiceSpecialItemByQuality(DICE_QUALITY_HIGH)
        iLowSpecialItem = ChooseKey(oGame, dLowSpecialItem)
        iHighSpecialItem = ChooseKey(oGame, dHighSpecialItem)
        if not iLowSpecialItem or not iHighSpecialItem:
            SeasonLog.Alert('%s %s drop dicespecialitem qualityerr %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, dLowSpecialItem, dHighSpecialItem, sReason))
            return None
        lstSpecialItem = [
            iLowSpecialItem,
            iHighSpecialItem]
        iScene = oTarget.m_Scene
        SeasonLog.Debug('%s %s %s drop dicespecialitem %s %s' % (oGame.m_ID, oHero.m_PlayerID, iScene, lstSpecialItem, sReason))
        for iSpecialItem in lstSpecialItem:
            dDrop = {
                'SID': iSpecialItem }
            vBasePos = cl_reward.GetDropBasePos(oTarget)
            iTarget = oTarget.m_ID
            vPos = cl_reward.GetDropFixPos(self.m_Game, oHero, iScene, vBasePos, iTarget)
            oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_DICESPECIALITEM, vPos, [
                dDrop], {
                'Abandoner': iTarget }, { }, oHero.m_ID, iSplit = 1)
        

    
    def OnNpcInteract(self, oListener, oHero, dMsgInfo):
        if 'NpcType' not in dMsgInfo or dMsgInfo['NpcType'] != NWARRIOR_NPC_PASSBOX:
            return None
        oGame = self.m_Game
        iNpc = dMsgInfo['NPC']
        oNpc = oGame.GetObject(iNpc)
        if not oNpc:
            return None
        tLineIdx = oNpc.m_LineIdx
        if not tLineIdx:
            return None
        iLevel = tLineIdx[0]
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode or oLevelNode.m_LevelType not in (LEVEL_TYPE_FIGHT,):
            return None
        vPos = oNpc.GetPos()
        iScene = oNpc.m_Scene
        iLayer = oLevelNode.m_LayerNum
        iDelay = self.m_DiceRewardDelay
        if iDelay:
            oNpc.Call_Out(Functor(self.RewardDiceByPassBox, iNpc, iLayer, iScene, vPos), Time2Frame(iDelay), 'PassBoxReward')
        else:
            self.RewardDiceByPassBox(iNpc, iLayer, iScene, vPos)

    
    def RewardDiceByPassBox(self, iNpc, iLayer, iScene, vPos):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        sReason = 'PassBoxReward'
        iLayer = min(DICEPUT_MAX_LAYER, iLayer)
        for iHero in self.m_WarMgr.GetLiveHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstReward = []
            for _ in range(self.m_DiceRewardNum):
                dRewardDiceInfo = self.GetRewardDiceInfo(oHero, iLayer)
                if not dRewardDiceInfo:
                    continue
                oDice = cl_dice.CreateDice(oGame, None, dRewardDiceInfo)
                if oDice:
                    dReward = {
                        'item': VIRTUAL_ITEM_DROP,
                        'info': {
                            'DropType': NWARRIOR_DROP_DICE,
                            'DropInfo': [
                                oDice],
                            'DropPos': vPos } }
                    lstReward.append(dReward)
            
            SeasonLog.Debug('%s %s %s reward dice %s %s' % (oGame.m_ID, iScene, oHero.m_PlayerID, lstReward, sReason))
            cl_reward.RewardItem(oGame, oHero, lstReward, sReason, {
                'Player': iHero,
                'Abandoner': iNpc,
                'DropReason': DROP_REASON_NPCREWARD,
                'Scene': iScene })
        

    
    def GetRewardDiceInfo(self, oHero, iLayer):
        if iLayer not in self.m_DiceRewardConfig:
            return { }
        oGame = self.m_Game
        dLayerRewardConfig = self.m_DiceRewardConfig[iLayer]
        if not dLayerRewardConfig:
            return { }
        iChooseQuality = ChooseKey(oGame, self.GetDiceRewardResult(dLayerRewardConfig))
        dChooseWeight = self.GetAbilityFilterExcludeQuality(oHero.m_PlayerID, iChooseQuality)
        iChooseDiceAbility = ChooseKey(oGame, dChooseWeight)
        if not iChooseQuality or not iChooseDiceAbility:
            SeasonLog.Debug('%s %s choose diceinfo fail %s %s' % (oGame.m_ID, oHero.m_PlayerID, iChooseQuality, iChooseDiceAbility))
            return { }
        dDiceInfo = {
            'SID': iChooseDiceAbility,
            'QL': iChooseQuality,
            'PR': self.GetTempPointRangeByQuality(iChooseQuality) }
        return dDiceInfo

    
    def GetCurDiceData(self, oHero):
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return { }
        return oDiceCon.GetDiceData()

    
    def GetDiceRewardResult(self, dConfig):
        dResult = { }
        for iQuality, iValue in dConfig.items():
            dResult[iQuality] = cl_formula.GetResultByData(self, iValue, { })
        
        return dResult

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFinishWar() or dInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        iLevelID = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'regrouprelicpos')
        if not dAddInfo:
            return None
        dAddInfo = DeepCopy(dAddInfo)
        iScene = dInfo['Scene']
        self.CreateDiceNpc(iScene, oLevelNode, dAddInfo)

    
    def OnLevelStart(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelID = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        if not oLevelCtrl.CheckFirstHall():
            return None
        iLevelID = dInfo['LevelID']
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'seasonnpcpos')
        if not dAddInfo:
            return None
        dAddInfo = DeepCopy(dAddInfo)
        iScene = oLevelNode.m_Scene
        self.CreateDiceNpc(iScene, oLevelNode, dAddInfo)

    
    def CreateDiceNpc(self, iScene, oLevelNode, dAddInfo):
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

    
    def GetAbilityFilterExcludeQuality(self, pid, iQuality):
        if iQuality not in DICE_QUALITY_ALL:
            return { }
        return dict.fromkeys(set(self.GetAllUnLockDice(pid)) - set(GetExcludeDiceQuality(iQuality)), 1)

    
    def GetAIAbilityFilterExcludeQuality(self, pid, iQuality):
        if iQuality not in DICE_QUALITY_ALL:
            return { }
        return dict.fromkeys(set(GetAIDice()) - set(GetExcludeDiceQuality(iQuality)), 1)

    
    def ValidRecycleDrop(self, oHero, oDrop):
        if oDrop.m_ReleaseFlag:
            SeasonLog.Debug('%d recycle failed release %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_ID, oDrop.m_Owner))
            return 0
        if oDrop.m_Source and oDrop.m_Source != oHero.m_PlayerID:
            SeasonLog.Debug('%d recycle failed owner %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_ID, oDrop.m_Source))
            return 0
        if oHero.IsDead():
            SeasonLog.Debug('%d recycle failed dead %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, oHero.m_ID, oDrop.m_Owner))
            return 0
        return 1

    
    def RecycleDrop(self, oHero, oDrop, sReason, iSync = 1):
        iCanRecycle = self.ValidRecycleDrop(oHero, oDrop)
        if not iCanRecycle:
            return None
        oDiceCon = oHero.m_DiceCon
        if not oDiceCon:
            return None
        oDice = oDrop.m_DropInfo[0]
        dInfo = {
            'Dice': oDice.m_ID,
            'QL': oDice.m_Quality,
            'RecycleDropType': oDrop.m_FightType,
            'CurPoint': oDice.m_RollPoint,
            'Reward': oDiceCon.GetDiceRecyclePrice(oDice),
            'DiceSID': oDice.m_SID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, dInfo, iSub = RECYCLE_DROP)
        oDrop.Remove(sReason)
        iReward = dInfo['Reward']
        if iReward <= 0:
            return None
        oHero.AddCash(iReward, 'RecycleDiceDrop')
        if iSync:
            cl_snetwar.GS2CRecycleDropResult(self.m_Game, oDrop.m_ID, oHero.m_ID, iCanRecycle, CURRENCY_CASH, iReward, self.m_Game.GetRealPlayers())

    
    def OnChooseChallenge(self, _oDiceElement, oWarMgr, dMsgInfo):
        if dMsgInfo['Layer'] == IGNORE_LAYER and dMsgInfo['Level'] == IGNORE_LEVEL:
            return None
        iLevelID = dMsgInfo['LevelID']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iType = oLevelCtrl.GetLevelType(iLevelID)
        if iType != LEVEL_TYPE_FIGHT:
            return None
        oChallengeMgr = oLevelCtrl.m_RoomChallenge
        if not oChallengeMgr.ValidChooseChallenge(dMsgInfo):
            return None
        dChooseChallenge = dMsgInfo['ChooseChallenge']
        if set(dChooseChallenge.values()) & set(self.m_ChallengePutInfo):
            for (_, iRoomPos), iChallenge in dChooseChallenge.items():
                if iChallenge in self.m_ChallengePutInfo:
                    dMsgInfo['IgnoreAppearPos'] = iRoomPos
                    break
            
            return None
        dChallengeWeight = dict.fromkeys(self.m_ChallengePutInfo, self.m_ChallengePutWeight)
        oGame = self.m_Game
        iGuaranteChallenge = ChooseKey(oGame, dChallengeWeight)
        if iGuaranteChallenge:
            iAllRoom = oChallengeMgr.GetLevelRoomTotal(iLevelID)
            iGuaranteRoomPos = iAllRoom - GUARANTE_ROOMPOS
            if iGuaranteRoomPos < 0:
                iGuaranteRoomPos = 0
            SeasonLog.Debug('%d %d %s set guarante challenge %s' % (oGame.m_ID, iLevelID, iGuaranteRoomPos, iGuaranteChallenge))
            dMsgInfo['IgnoreAppearPos'] = iGuaranteRoomPos
            dChooseChallenge[(iLevelID, iGuaranteRoomPos)] = iGuaranteChallenge

    
    def ChooseChallengeBefore(self, _oDiceElement, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum == IGNORE_LAYER and oLevelCtrl.m_LevelNum == IGNORE_LEVEL:
            return None
        iLevel = dMsgInfo['Level']
        iType = oLevelCtrl.GetLevelType(iLevel)
        if iType == LEVEL_TYPE_BOSS:
            return None
        if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and oLevelCtrl.m_LevelNum == oLevelCtrl.GetFightMaxLevel():
            oChallengeMgr = oLevelCtrl.m_RoomChallenge
            iAllRoom = oChallengeMgr.GetLevelRoomTotal(iLevel)
            dMsgInfo['Info']['SeasonIgnore'] = {
                iLevel: iAllRoom - 1 }
        dChallengeWeight = dMsgInfo['ChallengeWeight']
        dOldChallengeWeight = dict(dChallengeWeight)
        for iChallenge in list(dChallengeWeight):
            if iChallenge not in self.m_ChallengeIgnoreInfo:
                continue
            dChallengeWeight.pop(iChallenge)
        
        for iChallenge in self.m_ChallengePutInfo:
            dChallengeWeight[iChallenge] = self.m_ChallengePutWeight
        
        SeasonLog.Debug('%d %d dice change challenge %s %s' % (self.m_Game.m_ID, dMsgInfo['Level'], dOldChallengeWeight, dChallengeWeight))

    
    def ChooseChallengePointAndLv(self):
        oGame = self.m_Game
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return (0, 0)
        (iLayer, _) = oLevelCtrl.GetLayerAndLevelMap(oLevelCtrl.m_LayerNum, oLevelCtrl.m_LevelNum)
        iLayer = min(4, iLayer)
        dPointInfo = self.m_ChallengeLvToPoint.get(iLayer, { })
        dLvWeight = self.m_ChallengeLvWeightInfo[iLayer]
        iLv = ChooseKey(oGame, dLvWeight)
        if not iLv:
            return (0, 0)
        lstPoint = dPointInfo.get(iLv, [])
        if not lstPoint:
            return (0, 0)
        if len(lstPoint) > 1:
            iMin = lstPoint[0]
            iMax = lstPoint[-1]
            if iMin != iMax - 1:
                lstPoint = list(range(iMin, iMax + 1))
            lstPoint = ShufferList(oGame, lstPoint, iNum = 1)
        iChallengePoint = lstPoint[0]
        self.AddAccumulatedChallengePoint(iChallengePoint)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_AFTER_SETSEASONCHALLENGEPOINT, oLevelCtrl, { })
        return (iChallengePoint, iLv)

    
    def GetLevelEndInfo(self, pid):
        oWarMgr = self.m_WarMgr
        oHero = oWarMgr.GetHeroByPlayer(pid)
        oDiceCon = oHero.m_DiceCon
        return {
            'UnLockAbilityDesc': oDiceCon.m_UnLockAbilityDesc }

    
    def GetPacketChallengeDropInfo(self):
        return self.m_PacketChallengeDropInfo

    
    def AddPacketDropTimes(self, iLayer, iTimes = 1):
        if not iTimes:
            return None
        if iLayer in self.m_PacketDropTimes:
            self.m_PacketDropTimes[iLayer] += iTimes
        else:
            self.m_PacketDropTimes[iLayer] = iTimes

    
    def CheckPacketValidDrop(self, iLayer, iLimit):
        if iLayer in self.m_PacketDropTimes and iLimit <= self.m_PacketDropTimes[iLayer]:
            return 0
        return 1

    
    def GetDiceEnergyInfo(self, sKey):
        if sKey not in self.m_DiceEnergyInfo:
            return { }
        return self.m_DiceEnergyInfo[sKey]

    
    def GetAllUnLockDice(self, pid):
        if pid not in self.m_UnLockDiceInfo:
            return { }
        return self.m_UnLockDiceInfo[pid]

    
    def GetAllUnLockSpecItem(self, pid):
        if pid not in self.m_UnlockSpecailItemInfo:
            return { }
        return self.m_UnlockSpecailItemInfo[pid]

    
    def AddAccumulatedChallengePoint(self, iPoint):
        self.m_AccumulatedChallengePoint += iPoint

    
    def GetAccumulatedChallengePoint(self):
        return self.m_AccumulatedChallengePoint

    
    def GetDropDiceShape(self):
        return self.m_DropDiceShape

    
    def GetDiceDamageInfo(self, iTotalDam, dInfo):
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in self.m_DiceDamagePerform:
                return {
                    self.m_DiceDamagePerform[iPerform]: iTotalDam }
        if 'RS' in dInfo and dInfo['RS'].m_Type == REASON_TYPE_PERFORM:
            iPerform = dInfo['RS'].m_Perform
            if iPerform in self.m_DiceDamagePerform:
                return {
                    self.m_DiceDamagePerform[iPerform]: iTotalDam }
        return { }

    
    def GetAddEnergyByDiceQuality(self, iQuality):
        if iQuality in self.m_DiceQualityAddEnergy:
            return self.m_DiceQualityAddEnergy[iQuality]
        return 0

    
    def GetBaseRollPointWeight(self, iMaxPointRange):
        if iMaxPointRange not in self.m_BaseRollPointWeight:
            return self.m_BaseRollPointWeight[DEFAULT_ROLLPOINT_RANGE]
        return self.m_BaseRollPointWeight[iMaxPointRange]

    
    def GetHeroRollPointWeight(self, pid, iMaxPointRange):
        if pid not in self.m_HeroRollPointWeight or iMaxPointRange not in self.m_HeroRollPointWeight[pid]:
            SeasonLog.Debug('%s %s not exist roll point weight %s %s' % (self.m_Game.m_ID, pid, self.m_HeroRollPointWeight, iMaxPointRange))
            if iMaxPointRange in self.m_BaseRollPointWeight:
                return self.m_BaseRollPointWeight[iMaxPointRange]
            return self.m_BaseRollPointWeight[DEFAULT_ROLLPOINT_RANGE]
        return self.m_HeroRollPointWeight[pid][iMaxPointRange]

    
    def ChangeHeroRollPointWeight(self, pid, iMaxPointRange, dChangeInfo):
        dRollPointWeight = self.m_HeroRollPointWeight.setdefault(pid, { })
        dRangeRollWeight = dRollPointWeight.setdefault(iMaxPointRange, { })
        SeasonLog.Debug('%s %s roll point weight change %s %s %s' % (self.m_Game.m_ID, pid, dRangeRollWeight, iMaxPointRange, dChangeInfo))
        for iPoint, iMul in dChangeInfo.items():
            if iPoint in dRangeRollWeight:
                iNewWeight = dRangeRollWeight[iPoint] * (100 + iMul) // 100
                if iNewWeight < 1:
                    iNewWeight = 1
                elif iNewWeight > DEFAULT_ROLL_POINT_MAX_WEIGHT:
                    iNewWeight = DEFAULT_ROLL_POINT_MAX_WEIGHT
                dRangeRollWeight[iPoint] = iNewWeight
        



def GetComponentClass(oWarManager):
    return CDiceElement


def RecycleDiceDrop(oWarMgr, oHero, oDrop, sReason):
    if not oWarMgr:
        return None
    if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_DICE:
        return None
    oDiceElement = oWarMgr.GetDiceElement()
    if not oDiceElement:
        return None
    oDiceElement.RecycleDrop(oHero, oDrop, sReason, iSync = 0)

