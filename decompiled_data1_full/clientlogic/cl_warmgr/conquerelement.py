# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/conquerelement.pyc
# RelativePath: clientlogic/cl_warmgr/conquerelement.pyc
# Source Generated with Decompyle++
# File: conquerelement.pyc (Python 3.6)

from cl_warmgr.mobject import CSeasonElement
from cl_warmgr.conquer import conquerchallengemgr
from cl_commondefines import LEVEL_TYPE_FIGHT, WARRIOR_MONSTER, NWARRIOR_DROP_PETEGG, LEVEL_TYPE_HIDE, PET_EGG_NORMAL, LEVEL_TYPE_BOSS, WARRIOR_BOSS, BOSS_DONOT_COUNT
from cl_platformdata import GetPetEggDrop, GetAllPet, GetAIMemberPetAbility
from cl_only import ChooseMulKeys, PY_FLAG_DEAD, SendAlert, ChooseKey
from cl_object.logging import PetLog
from cl_container.petabilitycon import ABILITY_MAX_COUNT
from cl_warmgr.bigdataanalyse import CConquerAnalyseCom, CPetAnalyseCom
import cl_msgcenter
import cl_random
import cl_reward
import cl_notify
import cl_pet
ENDLESS_EGGDROP = (99, 99)
AIMEMBER_GETPET_MINLAYER = 1
AIMEMBER_GETPET_MINLEVEL = 3

class CConquerElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'ConquerElement'
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_HatchNotify = dConfig.get('HatchNotify', 2020)
        self.m_BossHatchLayer = dConfig.get('BossHatchLayer', (3, 4))
        self.m_RarePetEggMinimum = dConfig.get('RarePetEggMinimum', 3)
        self.m_ConquerRewardRareEggProb = dConfig.get('ConquerRewardRareEggProb', 30)
        self.m_ConquerRewardEggSID = dConfig.get('ConquerRewardEggSID', { })
        self.m_FuseCost = dConfig.get('FuseCost', 100)
        self.m_SingleFuseMaxResetTimes = dConfig.get('SingleFuseMaxResetTimes', 2)
        self.m_ActiveAbilityCost = dConfig.get('ActiveAbilityCost', 300)
        self.m_PetGrowth = {
            'HPMax': 10,
            'Att': 32 }
        self.m_PetShopTypeWeight = dConfig.get('PetShopTypeWeight', 10)
        if self.m_WarMgr.m_Cycle > 0:
            self.m_PetGrowthData = dConfig.get('PetGrowthCycle', { })
        else:
            self.m_PetGrowthData = dConfig.get('PetGrowthNormal', { })
        self.m_ConquerchallengeMgr = conquerchallengemgr.NewConquerChallengeMgr(self, oData)
        self.m_Enable = 0
        self.m_PetDropMonster = { }
        self.m_MonsterCnt = { }
        self.m_PetEggDropRatio = { }
        self.m_BossDropPetEggHero = { }
        self.m_DropNormalCnt = 0
        self.m_ConquerExtraReward = { }

    
    def Init(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.m_ConquerchallengeMgr.Init()
        self.m_Enable = 1
        oWarMgr.Set('PutPetShop', 1)
        sFlag = self.m_CallFlag
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_TRANSFERENABLE, self.OnTransferEnable, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerChooseLeaveGame, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.OnLevelNodeFinishBefore, sFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, sFlag)
        self.AddAIMemberAttention()
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, sFlag)

    
    def InitAfter(self):
        if not self.m_Enable:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oBigdataMgr = oWarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CConquerAnalyseCom(oGame)
            oBigdataMgr.SetCom('Conquer', oAnalyseCom)
            oAnalyseCom = CPetAnalyseCom(oGame)
            oBigdataMgr.SetCom('Pet', oAnalyseCom)

    
    def AddAIMemberAttention(self):
        oWarMgr = self.m_Game.m_WarMgr
        if not oWarMgr.CheckHasAIMember():
            return None
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOk, self.m_CallFlag)

    
    def Release(self):
        self.m_ConquerchallengeMgr.Release()
        self.m_Enable = 0
        self.DoneAttention()
        self.m_WarMgr = None
        super().Release()

    
    def CheckEnable(self):
        return self.m_Enable

    
    def Save(self):
        return {
            'ConquerChallenge': self.m_ConquerchallengeMgr.Save(),
            'DropNormalCnt': self.m_DropNormalCnt }

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ConquerchallengeMgr.Load(dData['ConquerChallenge'])
        self.m_DropNormalCnt = dData.get('DropNormalCnt', 0)

    
    def DoneAttention(self):
        if not self.m_Enable:
            return None
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_TRANSFERENABLE, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, sFlag)
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, sFlag)

    
    def OnAddPlayer(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        dConfig = { }
        oHero.m_PetCon.Enable(dConfig)

    
    def OnStartFight(self, oListener, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] != LEVEL_TYPE_FIGHT:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        dPetEggDrop = GetPetEggDrop()
        if oWarMgr.IsEndless():
            tPutKey = ENDLESS_EGGDROP
        else:
            tPutKey = (oLevelCtrl.m_LayerNum, oLevelCtrl.m_LevelNum)
        if tPutKey not in dPetEggDrop:
            return None
        self.m_PetDropMonster = { }
        self.m_MonsterCnt = { }
        oGame = self.m_Game
        oLevelNode = oLevelCtrl.GetLevelNode(dMsgInfo['LevelID'])
        dLineCnt = oLevelNode.GetAllLineMonsterCnt()
        dChoose = { }
        for tLineIdx, iCnt in dLineCnt.items():
            for idx in range(1, iCnt + 1):
                dChoose[(tLineIdx, idx)] = 1
            
        
        if not dChoose:
            return None
        sKey = 'eggpetdrop'
        oRandomMgr = oGame.m_RandomMgr
        if not oRandomMgr.ValidRandom(sKey):
            oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, sKey, dChoose)
        else:
            oRandomMgr.SetChoose(sKey, dChoose)
        (iExcept, iSigma, iMin, iMax) = dPetEggDrop[tPutKey]
        if iExcept <= 0:
            return None
        dPut = oRandomMgr.ChooseKey(sKey, {
            'Expect': iExcept,
            'Sigma': iSigma,
            'Game': oGame,
            'Limit': dChoose,
            'Min': iMin,
            'Max': iMax })
        dPetDropMonster = self.m_PetDropMonster
        dChoose = { }
        setRoomHero = set(oWarMgr.GetRoomHero(iCalAI = 0))
        for tKey, iCnt in dPut.items():
            if iCnt > 0:
                dPetDropMonster[tKey] = setRoomHero
                continue
            dChoose[tKey] = 1
        
        iPutCnt = len(dPetDropMonster)
        for iRatio, setHero in self.m_PetEggDropRatio.items():
            iExtExcept = iPutCnt * iRatio // 100 - iPutCnt
            if iExtExcept > 0:
                dExtPut = oRandomMgr.ChooseKey(sKey, {
                    'Expect': iExtExcept,
                    'Sigma': 0,
                    'Game': oGame,
                    'Limit': dChoose })
                for tKey, iCnt in dExtPut.items():
                    if iCnt > 0:
                        dPetDropMonster[tKey] = setHero
                
            if iExtExcept < 0:
                dChooseKey = dict.fromkeys(dPetDropMonster, 10)
                lstKey = ChooseMulKeys(oGame, dChooseKey, -iExtExcept)
                for tKey in lstKey:
                    dPetDropMonster[tKey] -= setHero
                
        
        PetLog.Debug('%s chooseegg %s' % (oGame.m_ID, self.m_PetDropMonster))

    
    def SetPetEggDropRatio(self, iHero, iNewRatio):
        for iRatio, setHero in self.m_PetEggDropRatio.items():
            if iHero in setHero and iRatio != iNewRatio:
                oGame = self.m_Game
                oHero = oGame.GetObject(iHero)
            iPlayer = oHero.m_PlayerID if oHero else 0
            SendAlert('err', 'game:%s %s %s 设置了多个妖灵蛋投放几率 %s %s' % (oGame.m_ID, iPlayer, iHero, iRatio, iNewRatio))
            return None
        
        setRatio = self.m_PetEggDropRatio.setdefault(iNewRatio, set())
        setRatio.add(iHero)

    
    def RemovePetEggDropRatio(self, iHero):
        iEmptyRatio = 0
        for iRatio, setHero in self.m_PetEggDropRatio.items():
            if iHero in setHero:
                setHero.remove(iHero)
                if not setHero:
                    iEmptyRatio = iRatio
        
        if iEmptyRatio:
            self.m_PetEggDropRatio.pop(iEmptyRatio)

    
    def GetConquerExtraReward(self, iHero):
        if iHero not in self.m_ConquerExtraReward:
            return []
        lstAllReward = []
        for lstReward in self.m_ConquerExtraReward[iHero].values():
            for dReward in lstReward:
                lstAllReward.append(dReward)
            
        
        return lstAllReward

    
    def SetConquerExtraReward(self, iHero, sKey, lstReward):
        if iHero not in self.m_ConquerExtraReward:
            self.m_ConquerExtraReward[iHero] = { }
        self.m_ConquerExtraReward[iHero][sKey] = lstReward

    
    def ClearConquerExtraReward(self, iHero, sKey):
        if iHero not in self.m_ConquerExtraReward:
            return None
        if sKey not in self.m_ConquerExtraReward[iHero]:
            return None
        self.m_ConquerExtraReward[iHero].pop(sKey)

    
    def GetConquerDropNormalCnt(self):
        return self.m_DropNormalCnt

    
    def SetConquerDropNormalCnt(self, iNewCnt):
        self.m_DropNormalCnt = iNewCnt

    
    def OnMonsterDie(self, oWarMgr, oMonster, dMsgInfo):
        if not oMonster.m_FightType & WARRIOR_MONSTER:
            return None
        self.DropEggByKillBoss(oMonster)
        tLineIdx = oMonster.m_LineIdx
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLineNode = oLevelCtrl.GetLineNode(tLineIdx)
        if not oLineNode:
            return None
        (iGroup, iBaseSID) = oLineNode.m_MonsterCtrl.GetMonsterBelong(oMonster)
        if not iGroup or not iBaseSID:
            return None
        dMonsterCnt = self.m_MonsterCnt
        iGroupCnt = dMonsterCnt.setdefault(tLineIdx, 0) + 1
        dMonsterCnt[tLineIdx] = iGroupCnt
        tKey = (tLineIdx, iGroupCnt)
        lstHero = self.m_PetDropMonster.pop(tKey, [])
        if not lstHero:
            return None
        vBasePos = cl_reward.GetDropBasePos(oMonster)
        iMonster = oMonster.m_ID
        iScene = oMonster.m_Scene
        oGame = self.m_Game
        lstReward = []
        lstPass = []
        iGroup = oGame.m_WarMgr.AddDropGroup()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
            if not oHero:
                lstPass.append(iHero)
                continue
            dDrop = {
                'Type': PET_EGG_NORMAL,
                'Group': iGroup }
            lstReward.append(oHero.m_PlayerID)
            vPos = cl_reward.GetDropFixPos(oGame, oHero, iScene, vBasePos, iMonster)
            oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_PETEGG, vPos, [
                dDrop], { }, { }, iHero, iSplit = 1)
        
        PetLog.Debug('%s %s dropegg %s pass %s' % (oGame.m_ID, tKey, lstReward, lstPass))

    
    def SetBossDropEgg(self, iHero):
        self.m_BossDropPetEggHero[iHero] = 1

    
    def ClearBossDropEgg(self, iHero):
        if iHero in self.m_BossDropPetEggHero:
            self.m_BossDropPetEggHero.pop(iHero)

    
    def DropEggByKillBoss(self, oMonster):
        iFightType = oMonster.m_FightType
        if iFightType & WARRIOR_BOSS != WARRIOR_BOSS or iFightType in BOSS_DONOT_COUNT:
            return None
        oGame = self.m_Game
        vBasePos = cl_reward.GetDropBasePos(oMonster)
        iScene = oMonster.m_Scene
        oWarMgr = oGame.m_WarMgr
        iMonster = oMonster.m_ID
        dExtraInfo = {
            'Abandoner': iMonster }
        iGroup = oGame.m_WarMgr.AddDropGroup()
        lstHero = oWarMgr.GetLiveHero()
        lstRewardHero = []
        dBossDropPetEggHero = self.m_BossDropPetEggHero
        for iHero in lstHero:
            if iHero not in dBossDropPetEggHero:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dDrop = {
                'Type': PET_EGG_NORMAL,
                'Group': iGroup }
            vPos = cl_reward.GetDropFixPos(oGame, oHero, iScene, vBasePos, iMonster)
            oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_PETEGG, vPos, [
                dDrop], dExtraInfo, { }, iHero, iSplit = 1)
            lstRewardHero.append(oHero.m_PlayerID)
        
        PetLog.Debug('%s BossDropEgg %s' % (oGame.m_ID, lstRewardHero))

    
    def LiveHeroHatchEgg(self, bNotify):
        oGame = self.m_Game
        dPlayer = { }
        for iHero in oGame.m_WarMgr.GetLiveHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.m_PetCon.ChangeAllEggHatchType():
                dPlayer[oHero.m_PlayerID] = 1
        
        if bNotify and dPlayer:
            cl_notify.SendCommonNotify(self.m_Game, dPlayer, self.m_HatchNotify, { })

    
    def OnTransferEnable(self, oListener, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_HIDE:
            return None
        if not self.m_WarMgr.IsEndless():
            if dMsgInfo['LevelType'] != LEVEL_TYPE_BOSS or dMsgInfo['Layer'] not in self.m_BossHatchLayer:
                return None
        self.LiveHeroHatchEgg(True)

    
    def OnLevelNodeFinish(self, oListener, oWarMgr, dMsgInfo):
        if not self.m_WarMgr.IsEndless():
            return None
        self.LiveHeroHatchEgg(False)

    
    def OnLevelNodeGoalOk(self, oListener, oWarMgr, dMsgInfo):
        self.AIMemberGetPet(oWarMgr, dMsgInfo)

    
    def AIMemberGetPet(self, oWarMgr, dMsgInfo):
        if self.m_WarMgr.IsEndless():
            return None
        oElement = oWarMgr.GetComponent('TeammateAI')
        if not oElement or not (oElement.m_AIMember):
            return None
        if dMsgInfo['LevelType'] not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        if dMsgInfo['Layer'] <= AIMEMBER_GETPET_MINLAYER and dMsgInfo['Level'] < AIMEMBER_GETPET_MINLEVEL:
            return None
        oGame = self.m_Game
        dPet = GetAllPet()
        dAbility = GetAIMemberPetAbility()
        for iAIMember in oElement.m_AIMember:
            iHero = self.m_WarMgr.GetHeroIDByPlayerID(iAIMember)
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oPetCon = oHero.m_PetCon
            oCurPet = oPetCon.GetCurPet()
            if oCurPet:
                oPetCon.RemovePet(oCurPet.m_ID, 'AIMember')
            iSID = ChooseKey(oGame, dPet)
            oPet = cl_pet.CreatePet(oGame, oHero, iSID, 0, { })
            if not oPet:
                continue
            iCount = oGame.Random(ABILITY_MAX_COUNT) + 1
            dAbilityWeight = { }
            for iAbility in dAbility:
                iWeight = oPet.m_AbilityCon.GetAbilityWeight(iAbility)
                if not iWeight:
                    continue
                dAbilityWeight[iAbility] = iWeight
            
            lstAbility = ChooseMulKeys(oGame, dAbilityWeight, iCount)
            for iAbility in lstAbility:
                oPet.m_AbilityCon.AddAbility(iAbility, 'AIMember')
            
            oPetCon.AddPet(oPet)
            oPetCon.SetCurPet(oPet.m_ID)
        

    
    def OnPlayerChooseLeaveGame(self, oListener, oWarMgr, dMsgInfo):
        oHero = self.m_Game.GetObject(dMsgInfo['Hero'])
        oHero.m_PetCon.HatchAllEgg('LeaveGame')

    
    def OnLevelNodeFinishBefore(self, oListener, oWarMgr, dMsgInfo):
        dNotifyPlayer = { }
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            oScene = oGame.m_SceneMgr.GetScene(oNode.m_Scene)
            if not oScene:
                continue
            lstDrop = oScene.GetObjectsByType('Drop')
            for iDrop in lstDrop:
                oDrop = oGame.GetObject(iDrop)
                if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_PETEGG or not (oDrop.m_Owner):
                    continue
                iHero = oDrop.m_Owner
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                oDrop.Pick(iHero)
                dNotifyPlayer[oHero.m_PlayerID] = 1
            
        
        if dNotifyPlayer:
            cl_notify.SendCommonNotify(self.m_Game, dNotifyPlayer, 9542, { })

    
    def OnAddAllPlayer(self, oListener, oWarMgr, dMsgInfo):
        dPetGrowth = self.m_PetGrowthData
        if self.m_PetGrowthData:
            iHeroNum = len(oWarMgr.GetAllHero())
            self.m_PetGrowth['HPMax'] = dPetGrowth.get('HPMax', 10)
            self.m_PetGrowth['Att'] = dPetGrowth.get('AttInfo', { }).get(iHeroNum, 32)



def GetComponentClass(oWarManager):
    return CConquerElement

