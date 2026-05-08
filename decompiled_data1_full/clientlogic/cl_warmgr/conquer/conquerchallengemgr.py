# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/conquer/conquerchallengemgr.pyc
# RelativePath: clientlogic/cl_warmgr/conquer/conquerchallengemgr.pyc
# Source Generated with Decompyle++
# File: conquerchallengemgr.pyc (Python 3.6)

from cl_commondefines import STATE_TIME_FOREVER, MODE_SNOWMOUNTAINS, LEVEL_TYPE_FIGHT, WARRIOR_ELITE, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, SIDE_TYPE_MONSTER, DAM_USE_HP, DAM_TYPE_PERFORM, WARRIOR_HERO, DIE_PRIORITY_WEAK, DIE_PRIORITY_CONQUER_SUCC, PF_TYPE_MONSTERAF, PET_EGG_RARE, PET_EGG_NORMAL, NWARRIOR_DROP_PETEGG, VIRTUAL_ITEM_DROP, LINK_DELEGATE, LINK_ONLINE
from cl_commondefines import CONQUER_CHALLENGE_START, CONQUER_CHALLENGE_REWARD, CONQUER_MONSTER_WEAK_START, CONQUER_MONSTER_WEAK_END
from cl_resmgr.aitempparam import GetAIConfParam
from cl_object.logging import SeasonLog
from cl_only import ChooseKey, Functor, SendAlert, Time2Frame, Frame2Time, PY_FLAG_DEAD
import cl_msgcenter
import cl_state
import cl_math
import cl_snetwar
import cl_formula
import cl_platformdata
import cl_reward
import cl_gamedebug
import cl_object.reason
import cl_warmgr.warcondition
NORMAL_DEMON_STATE = 8122
PLUS_DEMON_STATE = 8130
WEAK_STATE = 8123
WEAK_RECOVER_STATE = 8124
CONQUER_INTENSIFY_STATE = 8125
BEING_CONQUERED_STATE = 8129
CONQUER_TYPE_START = 1
CONQUER_TYPE_STOP = 2
CONQUER_TYPE_HALT = 3
CONQUER_TYPE_FAIL = 4
CONQUER_TYPE_NOT_START = 5
CONQUER_STATUS_NONE = 0
CONQUER_STATUS_CLOSE = 1
CONQUER_STATUS_OPEN = 2
CHALLENGE_STATE_START = 1
CHALLENGE_STATE_END = 2
CHALLENGE_STATE_DIE = 3
DEVIL_PASSIVE = 50703

class CConquerMonsterChallenge(object):
    
    def __init__(self, oMgr, iLevel, iRoomPos):
        self.m_Key = 'ConquerMonsterChallenge_%s_%s' % (iLevel, iRoomPos)
        self.m_Mgr = oMgr
        self.m_Game = oMgr.m_Game
        dConfig = oMgr.m_Config
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iBaseLayerNum = oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        self.m_MonsterFirstWeakTime = dConfig.get('FirstWeakTime', 700)
        self.m_MonsterWeakAddTime = dConfig.get('WeakAddTime', 100)
        self.m_ConquerTargetProcess = cl_formula.GetResultByData(self, dConfig.get('ConquerProcess', 80), { })
        self.m_ConquerRate = dConfig.get('ConquerRate', 40)
        self.m_HaltInfoDict = dConfig.get('HaltInfo', { })
        self.m_MonsterBanPlusPFTuple = dConfig.get('BanPlusPF', ())
        self.m_MonsterBanAttrPlusTuple = dConfig.get('BanAttrPlus', ())
        self.m_IgnoreHaltTuple = dConfig.get('IgnoreHalt', ())
        self.m_PlusScale = dConfig.get('PlusScale', 150)
        self.m_ConquerRadius = dConfig.get('ConquerRadius', 5)
        self.m_MonsterWeakCount = 0
        self.m_MonsterLastWeakCount = 0
        self.m_MonsterWeakStartFrameNum = 0
        self.m_MonsterLastWeakTime = 0
        self.m_Level = iLevel
        self.m_RoomPos = iRoomPos
        self.m_MonsterID = 0
        self.m_MonsterSID = 0
        self.m_ConquerStartFrameNum = 0
        self.m_ConquerLastProcess = 0
        self.m_ConquerCacheDict = { }
        self.m_DemonPlusPerform = None
        self.m_IncreasePerform = 0
        self.m_HeroPerform = 0
        self.m_RewardPetEggCnt = 1
        if not oWarMgr.IsEndless():
            self.m_bPlusLevel = (iBaseLayerNum, oLevelNode.m_LevelNum) in dConfig.get('PlusLevel', { })
        else:
            self.m_bPlusLevel = True
        if self.m_bPlusLevel:
            dConquerPFWeight = cl_platformdata.GetConquerPFWeight()
            self.m_HeroPerform = ChooseKey(self.m_Game, dConquerPFWeight)
            self.m_ConquerRadius = self.m_ConquerRadius * self.m_PlusScale / 100
            dDemonPlusWeight = cl_platformdata.GetDemonPlusWeight()
            dWeight = dDemonPlusWeight[iBaseLayerNum] if iBaseLayerNum in dDemonPlusWeight else { }
            self.m_IncreasePerform = ChooseKey(self.m_Game, dWeight)
            self.m_RewardPetEggCnt += dConfig.get('PlusLevelExtEggCnt', 1)
        self.m_Scene = oLevelNode.m_Scene
        self.m_Reward = 0
        self.m_ParticipatePlayer = { }
        self.m_CreateMonsterFrame = 0
        self.m_bMonsterWeakHalt = False
        self.InitEvent()
        SeasonLog.Info('%s conquerchallenge init %s' % (self.m_Game.m_ID, self.m_Key))

    
    def InitEvent(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iWarMgrID = oWarMgr.m_ID
        oGame.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        oGame.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_Key)
        oGame.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HALT_CASTINGSKILL, self.OnHaltCastingSkill, self.m_Key)
            if self.m_HeroPerform:
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnLinkStatusChange, self.m_Key)
        
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.OnLevelStartSpawn, self.m_Key, -1, 0)

    
    def ChallengeStart(self):
        SeasonLog.Info('%s conquerchallenge start %s' % (self.m_Game.m_ID, self.m_Key))
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(self.m_Level)
        oLevelNode.LockRoom(self.m_RoomPos, self.m_Key)
        self.AddHeroPerform()
        self.CreateMonster()
        self.SendChallengeInfo(CHALLENGE_STATE_START)
        dMsgInfo = {
            'MonsterSID': self.m_MonsterSID,
            'PlusLevel': self.m_bPlusLevel,
            'Level': self.m_Level }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Game.m_WarMgr, dMsgInfo, iSub = CONQUER_CHALLENGE_START)

    
    def ChallengeEnd(self, bForceEnd = False):
        SeasonLog.Info('%s conquerchallenge end %s %s' % (self.m_Game.m_ID, self.m_Key, bForceEnd))
        if bForceEnd:
            iRoomPos = self.m_RoomPos
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            oLevelNode = oLevelCtrl.GetLevelNode(self.m_Level)
            oLevelNode.UnlockRoom(iRoomPos, self.m_Key)
        self.SendChallengeInfo(CHALLENGE_STATE_END)
        self.Release()

    
    def GetScenePlayers(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return []
        return oScene.GetPlayers()

    
    def GetSceneHeros(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return []
        return oScene.GetHeros()

    
    def AddHeroPerform(self):
        if not self.m_HeroPerform:
            return None
        for iHero in self.GetSceneHeros():
            oHero = self.m_Game.GetObject(iHero)
            if oHero and oHero.Online() == LINK_ONLINE:
                oHero.AddPerform(self.m_HeroPerform, 1)
        

    
    def RemoveHeroPerform(self):
        if not self.m_HeroPerform:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.RemovePerform(self.m_HeroPerform)
        

    
    def CreateMonster(self):
        oGame = self.m_Game
        iLevel = self.m_Level
        iRoomPos = self.m_RoomPos
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iLayerNum = oLevelCtrl.m_LayerNum
        iBaseLayerNum = oWarMgr.GetBaseLayer(iLayerNum)
        iLevelNum = oLevelNode.m_LevelNum
        iLayVer = cl_warmgr.warcondition.WarCheckNewVerLayer(oWarMgr, iLevel)
        iMonsterSID = self.m_Mgr.GetCreateMonster(iLayVer, iLayerNum, iBaseLayerNum, iLevelNum)
        SeasonLog.Debug('game:%d, level:%d, room:%d create monster info %d, %d, %d, %d, %d' % (oGame.m_ID, iLevel, iRoomPos, iLayVer, iLayerNum, iBaseLayerNum, iLevelNum, iMonsterSID))
        if not iMonsterSID:
            SeasonLog.Alert('%s no monster sid %s, %s, %s' % (oGame.m_ID, iLayerNum, iBaseLayerNum, iLevelNum))
            self.ChallengeEnd(bForceEnd = True)
            return None
        iScene = oLevelNode.m_Scene
        oWarData = oGame.m_WarData
        oLevelConfData = oLevelCtrl.m_LevelConfData
        (tPos, dEliteDrop) = oLevelNode.GetEliteInfo(iRoomPos, oLevelConfData)
        oLineNode = oLevelNode.m_RoomList[iRoomPos][-1]
        tFace = oLineNode.m_MonsterCtrl.GetMonsterFacing(tPos)
        (iRet, tPos2) = self.m_Game.Scene_GetSpace(iScene, tPos)
        if iRet:
            tPos = tPos2
        else:
            SendAlert('err', 'game:%d, level:%d, room:%d, pos%s err' % (oGame.m_ID, iLevel, iRoomPos, tPos))
        clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
        iDelayFrame = clsMonsterData.GetCreateDelayFrame()
        iEffectSID = clsMonsterData.m_CreateEffect
        if iEffectSID:
            iEffectID = oGame.NewNoSceneObjID()
            cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, tPos, self.GetScenePlayers())
        if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
        if iDelayFrame:
            oFunc = Functor(self.TrueCreateMonster, iMonsterSID, iScene, tPos, tFace, dEliteDrop)
            oLevelCtrl.Call_Out(oFunc, iDelayFrame, self.m_Key)
        else:
            self.TrueCreateMonster(iMonsterSID, iScene, tPos, tFace, dEliteDrop)

    
    def TrueCreateMonster(self, iMonsterSID, iScene, tPos, tFace, dEliteDrop):
        tLineIdx = (self.m_Level, self.m_RoomPos, 0)
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        oMonster = self.m_Game.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, SIDE_TYPE_MONSTER, 0, dAI, tLineIdx, {
            'Demon': 1,
            'NoEnemyNotify': False })
        if not oMonster:
            self.ChallengeEnd(bForceEnd = True)
            return None
        oReason = cl_object.reason.CStrReason('ConquerChallengeCreateMonster')
        oMonster.SetDiePriority(DIE_PRIORITY_WEAK, 'ConquerChallengeCreateMonster')
        oMonster.Set('NoRelife', 1)
        if oMonster.IsDead():
            SeasonLog.Alert('%s create monster isdead %s, %s, %s' % (self.m_Game.m_ID, iMonsterSID, oMonster.m_FinalDam, oMonster.m_DeadReason))
            self.ChallengeEnd(bForceEnd = True)
            return None
        if dEliteDrop:
            oMonster.Set('FixDropPos', dEliteDrop['FixDropPos'])
            oMonster.Set('CheckDropInfo', dEliteDrop['CheckDropInfo'])
        oMonster.AddPerform(DEVIL_PASSIVE, 1)
        iMonsterID = oMonster.m_ID
        self.m_ParticipatePlayer[iMonsterID] = { }
        self.m_CreateMonsterFrame = self.m_Game.GetFrameNum()
        iState = PLUS_DEMON_STATE if self.m_bPlusLevel else NORMAL_DEMON_STATE
        dArgs = {
            'AID': iMonsterID,
            'RS': oReason }
        oState = cl_state.AddState(oMonster, iState, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(oMonster)
        cl_msgcenter.AddAttentionFunc(self.m_Game.m_WarMgr, iMonsterID, cl_msgcenter.MSG_WAR_DIE_BEFORE, self.OnMonsterDieBefore, self.m_Key)
        self.m_MonsterID = iMonsterID
        self.m_MonsterSID = iMonsterSID
        self.m_Mgr.AddCreatedMonster(iMonsterSID)
        self.MonsterIncrease(oMonster)

    
    def MonsterIncrease(self, oMonster):
        if self.m_IncreasePerform:
            oMonster.SetModelScale(self.m_PlusScale)
            self.m_DemonPlusPerform = oMonster.AddPerform(self.m_IncreasePerform, 1)
        oMonster.m_BanPF = tuple(set(oMonster.m_BanPF + self.m_MonsterBanPlusPFTuple))
        lstAttrPlus = []
        for iPlusPF in oMonster.m_AttrPlusPF:
            if iPlusPF in self.m_MonsterBanAttrPlusTuple:
                continue
            lstAttrPlus.append(iPlusPF)
        
        oMonster.m_AttrPlusPF = tuple(lstAttrPlus)
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oSuperCom = oWarMgr.GetComponent('MonsterSuper')
        if oSuperCom:
            oLevelNode = oLevelCtrl.GetLevelNode(self.m_Level)
            (iAfPF, iPlusPF) = oSuperCom.RandomMonsterSuperInfo(oMonster, [], oLevelNode.m_LevelType)
            iSuperLevel = oSuperCom.GetMonsterSuperLevel(oLevelNode.m_LevelType)
            oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)

    
    def OnDie(self, oWarMgr, oVictim, dMsgInfo):
        if oVictim.m_FightType & WARRIOR_HERO:
            oTarget = self.m_Game.GetObject(self.m_MonsterID)
            if oTarget:
                self.HaltConquer(oVictim, oTarget)
        if oVictim.m_ID != self.m_MonsterID:
            return None
        oVictim.Remove_Call_Out('MonsterWeak')
        oVictim.Remove_Call_Out('ConquerMonster')
        oReason = dMsgInfo['RS']
        sReason = oReason.GetStrReason()
        if sReason != 'FinishConquerDie':
            SeasonLog.Alert('game:%d, level:%d, room:%d, monster:%d not conquer die, %s' % (self.m_Game.m_ID, self.m_Level, self.m_RoomPos, oVictim.m_SID, sReason))
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HALT_CASTINGSKILL, self.m_Key)
        
        self.OnReward(oVictim)
        self.SendChallengeInfo(CHALLENGE_STATE_DIE)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(self.m_Level)
        oLevelNode.UnlockRoom(self.m_RoomPos, self.m_Key)

    
    def OnReward(self, oMonster):
        if self.m_Reward:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oConquerElement = oWarMgr.GetComponent('ConquerElement')
        if not oConquerElement:
            return None
        lstHero = oWarMgr.GetLiveHero()
        dConquerRewardEggSID = oConquerElement.m_ConquerRewardEggSID
        self.m_Reward = 1
        iMonster = oMonster.m_ID
        lstRewardEggInfo = []
        for _ in range(self.m_RewardPetEggCnt):
            iGroup = oGame.m_WarMgr.AddDropGroup()
            iEggType = self.ChooseRewardEggType(oConquerElement)
            iEggSID = dConquerRewardEggSID[iEggType] if iEggType in dConquerRewardEggSID else 0
            lstRewardEggInfo.append((iGroup, iEggType, iEggSID))
        
        dMGInfo = { }
        dParticipatePlayer = self.m_ParticipatePlayer[iMonster]
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dExtInfo = {
                'Player': iHero }
            lstReward = []
            for iGroup, iEggType, iEggSID in lstRewardEggInfo:
                dDrop = {
                    'Type': iEggType,
                    'Group': iGroup }
                if iEggSID:
                    dDrop['SID'] = iEggSID
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_PETEGG,
                        'DropInfo': [
                            dDrop] } }
                lstReward.append(dReward)
            
            iPlayer = oHero.m_PlayerID
            if iPlayer in dParticipatePlayer:
                lstReward.extend(oConquerElement.GetConquerExtraReward(iHero))
            dMGInfo[iHero] = {
                0: [
                    0,
                    lstReward,
                    dExtInfo] }
            SeasonLog.Debug('game:%d, level%d, room%d conquer reward %d %s' % (oGame.m_ID, self.m_Level, self.m_RoomPos, iPlayer, lstReward))
        
        cl_reward.CreateDemon(oGame, iMonster, dMGInfo, 'ConquerChallenge')
        oConquerElement.LiveHeroHatchEgg(True)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Game.m_WarMgr, { }, iSub = CONQUER_CHALLENGE_REWARD)

    
    def ChooseRewardEggType(self, oConquerElement):
        iConquerDropNormalCnt = oConquerElement.GetConquerDropNormalCnt()
        if iConquerDropNormalCnt < oConquerElement.m_RarePetEggMinimum:
            iProb = self.m_Game.Random(100)
            if iProb > oConquerElement.m_ConquerRewardRareEggProb:
                oConquerElement.SetConquerDropNormalCnt(iConquerDropNormalCnt + 1)
                return PET_EGG_NORMAL
        oConquerElement.SetConquerDropNormalCnt(0)
        return PET_EGG_RARE

    
    def CanConquer(self, oHero, oTarget):
        iHeroID = oHero.m_ID
        iTargetID = oTarget.m_ID
        if iHeroID == iTargetID:
            return False
        if iTargetID != self.m_MonsterID:
            return None
        if oHero.IsDead():
            return False
        if oHero.m_Scene != oTarget.m_Scene:
            return False
        if iHeroID in self.m_ConquerCacheDict:
            return False
        if oTarget.Query('ConquerStatus', 0) != CONQUER_STATUS_OPEN:
            return False
        tHeroPos = oHero.GetPos()
        tTargetPos = oTarget.GetPos()
        if not cl_math.CheckDistance(tHeroPos, tTargetPos, self.m_ConquerRadius):
            return False
        return True

    
    def RefreshConquerTime(self, oHero, oTarget, bIsAdd = True):
        oGame = self.m_Game
        iHeroID = oHero.m_ID
        iTargetID = oTarget.m_ID
        iCurProcess = self.GetCurConquerProcess()
        self.m_ConquerLastProcess = iCurProcess
        self.m_ConquerStartFrameNum = oGame.GetFrameNum()
        if bIsAdd:
            self.m_ConquerCacheDict[iHeroID] = 1
        else:
            self.m_ConquerCacheDict.pop(iHeroID)
        sTimerFlag = 'ConquerMonster'
        oTarget.Remove_Call_Out(sTimerFlag)
        if self.m_ConquerCacheDict:
            iConquerTime = int(((self.m_ConquerTargetProcess - iCurProcess) / self.GetConquerRate()) * 100)
            iFrame = Time2Frame(iConquerTime)
            if iFrame > 0:
                oTarget.Call_Out(Functor(self.StopConquer, iTargetID, iHeroID), iFrame, sTimerFlag)
            else:
                self.StopConquer(iTargetID, iHeroID)

    
    def StartConquer(self, oHero, oTarget):
        iHero = oHero.m_ID
        iTarget = oTarget.m_ID
        if not self.CanConquer(oHero, oTarget):
            self.SendConquerState(CONQUER_TYPE_NOT_START, iHero, iTarget, iPlayerID = oHero.m_PlayerID)
            return None
        self.m_ParticipatePlayer[iTarget][oHero.m_PlayerID] = 1
        dArgs = {
            'AID': iHero,
            'RS': cl_object.reason.CStrReason('StartConquer') }
        oState = cl_state.AddState(oHero, CONQUER_INTENSIFY_STATE, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(oHero)
        self.HaltMonsterWeak(oTarget)
        self.RefreshConquerTime(oHero, oTarget)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_START_CONQUER, oHero, { })
        if not self.m_Game:
            return None
        self.SendConquerState(CONQUER_TYPE_START, iHero, iTarget)

    
    def HaltConquer(self, oHero, oTarget):
        iHeroID = oHero.m_ID
        if iHeroID not in self.m_ConquerCacheDict:
            return None
        oHero.m_State.RemoveAllItemBySID(CONQUER_INTENSIFY_STATE)
        self.RefreshConquerTime(oHero, oTarget, False)
        if not self.m_Game:
            return None
        self.SendConquerState(CONQUER_TYPE_HALT, oHero.m_ID, oTarget.m_ID)
        if not self.m_ConquerCacheDict:
            oTarget.Remove_Call_Out('ConquerMonster')
            self.SendConquerState(CONQUER_TYPE_STOP, 0, oTarget.m_ID)
            if oTarget.IsDead():
                return None
            self.MonsterWeakStart(oTarget, True)

    
    def StopConquer(self, iTarget, iAttack = 0):
        oGame = self.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            return None
        for iHeroID in self.m_ConquerCacheDict:
            oHero = self.m_Game.GetObject(iHeroID)
            oHero.m_State.RemoveAllItemBySID(CONQUER_INTENSIFY_STATE)
        
        oTarget.Remove_Call_Out('ConquerMonster')
        SeasonLog.Debug('game:%d, level:%d, room%d stop conquer' % (oGame.m_ID, self.m_Level, self.m_RoomPos))
        self.m_ConquerLastProcess = 0
        self.m_ConquerCacheDict = { }
        if iTarget in self.m_ParticipatePlayer:
            iSpendTime = Frame2Time(oGame.GetFrameNum() - self.m_CreateMonsterFrame)
            for iPlayer in self.m_ParticipatePlayer[iTarget]:
                self.m_Mgr.AddPlayerConquerCount(iPlayer, iSpendTime, self.m_MonsterID)
            
        self.m_Mgr.FinishConquer()
        self.SendConquerState(CONQUER_TYPE_STOP, 0, oTarget.m_ID)
        self.MonsterDie(oTarget, iAttack)

    
    def MonsterDie(self, oTarget, iAttack = 0):
        oGame = self.m_Game
        cl_msgcenter.DoneAttention(oGame.m_WarMgr, oTarget.m_ID, cl_msgcenter.MSG_WAR_DIE_BEFORE, self.m_Key)
        oReason = cl_object.reason.CStrReason('FinishConquerDie', None, {
            'DamType': DAM_TYPE_PERFORM | DAM_USE_HP })
        oTarget.Set('FinishConquerNoRecover', 1)
        oTarget.SetDiePriority(DIE_PRIORITY_CONQUER_SUCC, 'FinishConquerDie')
        oTarget.m_State.RemoveAllItemBySID(WEAK_STATE)
        oTarget.HPDirectModify('HP', iAttack, -(oTarget.m_HP), oReason)
        if not oTarget.IsDead():
            dInfo = cl_gamedebug.GetMonsterStateInfo(oTarget)
            (iLevel, iRoomPos, _) = oTarget.m_LineIdx
            SeasonLog.Alert('game:%d, level%d, room%d, monster%d conquer die err, hp:%s stateinfo:%s' % (oGame.m_ID, iLevel, iRoomPos, oTarget.m_SID, oTarget.HP(), dInfo))
            oTarget.Die(0, oReason)

    
    def GetCurConquerProcess(self):
        iConquerRate = self.GetConquerRate()
        iCurProcess = int(self.m_ConquerLastProcess + iConquerRate * (Frame2Time(self.m_Game.GetFrameNum() - self.m_ConquerStartFrameNum) / 100))
        return iCurProcess

    
    def GetConquerRate(self):
        iHeroCount = len(self.m_ConquerCacheDict)
        if iHeroCount == 0:
            return 0
        return cl_formula.GetResultByData(self, self.m_ConquerRate, { }) * (10000 + self.m_Mgr.GetExtraAttr('ConquerRate')) // 10000

    
    def OnPlayerMapLoadOK(self, oWarMgr, oHero, dInfo):
        if not self.m_Game:
            return None
        if self.m_HeroPerform:
            if dInfo['LevelID'] != self.m_Level:
                oHero.RemovePerform(self.m_HeroPerform)
            else:
                oHero.AddPerform(self.m_HeroPerform, 1)
        if oHero.m_Scene != self.m_Scene:
            return None
        oTarget = self.m_Game.GetObject(self.m_MonsterID)
        if not oTarget:
            return None
        iHeroID = dInfo['Hero']
        iPlayerID = dInfo['pid']
        self.SendChallengeInfo(CHALLENGE_STATE_START, iPlayerID)
        if oTarget.Query('ConquerStatus', 0) == CONQUER_STATUS_OPEN:
            self.SendMonsterWeakInfo(oTarget, iPlayerID)
        if iHeroID in self.m_ConquerCacheDict:
            self.SendConquerState(CONQUER_TYPE_START, iHeroID, oTarget.m_ID, iPlayerID)

    
    def OnRoomGoal(self, oWarMgr, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        if iLevel != self.m_Level or self.m_RoomPos != iRoomPos:
            return None
        self.ChallengeEnd()

    
    def OnLevelStartSpawn(self, oLevelCtrl, dMsgInfo):
        (iLevel, iRoomPos, _) = dMsgInfo['LineIdx']
        if iLevel != self.m_Level or self.m_RoomPos != iRoomPos:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.m_Key)
        self.ChallengeStart()

    
    def OnHaltCastingSkill(self, oWarMgr, oHero, dInfo):
        iHeroID = oHero.m_ID
        if iHeroID not in self.m_ConquerCacheDict:
            return None
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in self.m_IgnoreHaltTuple:
                return None
        iKey = dInfo['MsgKey']
        if iKey not in self.m_HaltInfoDict or not self.m_HaltInfoDict[iKey]:
            return None
        oTarget = self.m_Game.GetObject(self.m_MonsterID)
        self.HaltConquer(oHero, oTarget)

    
    def OnLinkStatusChange(self, oWarMgr, oHero, dInfo):
        iHeroLinkStatus = dInfo['LinkStatus']
        if iHeroLinkStatus == LINK_DELEGATE:
            oHero.RemovePerform(self.m_HeroPerform)

    
    def GetMonsterWeakTime(self):
        return self.m_MonsterFirstWeakTime + self.m_MonsterLastWeakCount * self.m_MonsterWeakAddTime + self.m_Mgr.GetExtraAttr('WeakTime')

    
    def GetMonsterCurWeakTime(self):
        return self.m_MonsterLastWeakTime + Frame2Time(self.m_Game.GetFrameNum() - self.m_MonsterWeakStartFrameNum)

    
    def OnMonsterDieBefore(self, oWarMgr, oTarget, dInfo):
        self.MonsterWeakStart(oTarget)

    
    def MonsterWeakStart(self, oTarget, bIsContinue = False):
        iMonsterID = oTarget.m_ID
        if bIsContinue:
            if not self.m_bMonsterWeakHalt:
                return None
            oTarget.m_State.RemoveAllItemBySID(BEING_CONQUERED_STATE)
        elif oTarget.m_State.HasState(WEAK_STATE) or oTarget.m_State.HasState(WEAK_RECOVER_STATE):
            return None
        self.m_MonsterWeakCount += 1
        if oTarget.m_Agent:
            oTarget.m_Agent.HaltPerform(oTarget.m_Agent)
            oTarget.m_Agent.PauseAgent('MonsterWeak')
        oTarget.Stop()
        oTarget.StopShieldRecover('MonsterWeak')
        dArgs = {
            'AID': iMonsterID,
            'RS': cl_object.reason.CStrReason('MonsterWeak') }
        oState = cl_state.AddState(oTarget, WEAK_STATE, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(oTarget)
        oState.AddCount(oTarget, self.m_MonsterWeakCount)
        if self.m_DemonPlusPerform and self.m_DemonPlusPerform.m_WeakDisable:
            self.m_DemonPlusPerform.Disable(oTarget, iNotify = 0)
        for iPerform in oTarget.GetPerformSIDByType(PF_TYPE_MONSTERAF):
            oPerform = oTarget.GetPerform(iPerform)
            oPerform.Disable(oTarget, iNotify = 0)
        
        self.m_bMonsterWeakHalt = False
        self.m_MonsterWeakStartFrameNum = self.m_Game.GetFrameNum()
        sTimerFlag = 'MonsterWeak'
        oTarget.Remove_Call_Out(sTimerFlag)
        oTarget.Call_Out(Functor(self.MonsterWeakEnd, iMonsterID), Time2Frame(self.GetMonsterWeakTime() - self.GetMonsterCurWeakTime()), sTimerFlag)
        self.SendMonsterWeakInfo(oTarget)
        dMsgInfo = {
            'IsContinue': bIsContinue }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Game.m_WarMgr, dMsgInfo, iSub = CONQUER_MONSTER_WEAK_START)

    
    def MonsterWeakEnd(self, iTargetID):
        oTarget = self.m_Game.GetObject(iTargetID)
        for iHeroID in list(self.m_ConquerCacheDict.keys()):
            oHero = self.m_Game.GetObject(iHeroID)
            self.HaltConquer(oHero, oTarget)
        
        self.m_MonsterWeakStartFrameNum = 0
        self.m_MonsterLastWeakTime = 0
        self.m_MonsterLastWeakCount = self.m_MonsterWeakCount
        oTarget.m_State.RemoveAllItemBySID(WEAK_STATE)
        if self.m_DemonPlusPerform and self.m_DemonPlusPerform.m_WeakDisable:
            self.m_DemonPlusPerform.Enable(oTarget, iNotify = 0)
        for iPerform in oTarget.GetPerformSIDByType(PF_TYPE_MONSTERAF):
            oPerform = oTarget.GetPerform(iPerform)
            oPerform.Enable(oTarget)
        
        if oTarget.m_Agent:
            oTarget.m_Agent.ResumeAgent('MonsterWeak')
        oTarget.StartShieldRecover('MonsterWeak')
        self.SendMonsterWeakInfo(oTarget)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Game.m_WarMgr, { }, iSub = CONQUER_MONSTER_WEAK_END)

    
    def HaltMonsterWeak(self, oTarget):
        if self.m_bMonsterWeakHalt:
            return None
        self.m_bMonsterWeakHalt = True
        self.m_MonsterLastWeakTime = self.GetMonsterCurWeakTime()
        oTarget.Remove_Call_Out('MonsterWeak')
        dArgs = {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason('BeingConquered') }
        oState = cl_state.AddState(oTarget, BEING_CONQUERED_STATE, STATE_TIME_FOREVER, 0, dArgs)
        if oState:
            oState.Enable(oTarget)

    
    def SendConquerState(self, iState, iHeroID, iTargetID, iPlayerID = 0):
        if self.m_ConquerCacheDict:
            iCurProcess = self.GetCurConquerProcess()
            iConquerRate = self.GetConquerRate()
        else:
            iCurProcess = 0
            iConquerRate = 0
        lstPlayer = [
            iPlayerID] if iPlayerID else self.GetScenePlayers()
        cl_snetwar.GS2CConquerState(self.m_Game, iState, iHeroID, iTargetID, self.m_ConquerTargetProcess, iCurProcess, iConquerRate, lstPlayer)

    
    def SendMonsterWeakInfo(self, oTarget, iPlayerID = 0):
        if oTarget.Query('ConquerStatus', 0) != CONQUER_STATUS_OPEN:
            iTotalTime = 0
            iRemainTime = 0
        else:
            iTotalTime = self.GetMonsterWeakTime()
            iRemainTime = iTotalTime - self.GetMonsterCurWeakTime()
        lstPlayer = [
            iPlayerID] if iPlayerID else self.GetScenePlayers()
        cl_snetwar.GS2CMonsterWeakInfo(self.m_Game, self.m_MonsterID, iTotalTime, iRemainTime, lstPlayer)

    
    def SendChallengeInfo(self, iState, iPlayerID = 0):
        lstPlayer = [
            iPlayerID] if iPlayerID else self.GetScenePlayers()
        cl_snetwar.GS2CConquerChallengeInfo(self.m_Game, iState, self.m_MonsterID, self.m_bPlusLevel, self.m_HeroPerform, lstPlayer)

    
    def Release(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iWarMgrID = oWarMgr.m_ID
        oGame.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        oGame.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        oGame.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HALT_CASTINGSKILL, self.m_Key)
            if self.m_HeroPerform:
                cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.m_Key)
        
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.m_Key)
        self.RemoveHeroPerform()
        self.m_Mgr.ChallengeRelease(self.m_Level, self.m_RoomPos)
        self.m_Mgr = None
        self.m_Game = None



class ConquerChallengeMgr(object):
    
    def __init__(self, oConquerElement, oData):
        self.m_Key = 'ConquerMonsterChallenge'
        self.m_Game = oConquerElement.m_Game
        self.m_Config = oData.m_Config
        self.m_LevelMonsterDict = self.m_Config.get('LevelMonster', { })
        self.m_EndlessLevelDict = self.m_Config.get('EndlessLevel', { })
        self.m_ExcludeAreaTuple = self.m_Config.get('ExcludeArea', ())
        self.m_ChallengeDict = { }
        self.m_CreatedMonsterDict = { }
        self.m_ConquerProbabilityMul = 0
        self.m_PlayerConquerInfo = { }
        self.m_TeamSuccessConquer = 0
        self.m_ExtraAttr = {
            'ConquerProbability': CExtraAttr(),
            'ConquerRate': CExtraAttr(),
            'WeakTime': CExtraAttr() }

    
    def Init(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iWarMgrID = self.m_Game.m_WarMgr.m_ID
        oGame.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, self.m_Key)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelInit, self.m_Key, -1, 0, 1)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, self.m_Key, -1, 0)

    
    def Save(self):
        return {
            'CreatedMonster': self.m_CreatedMonsterDict,
            'PlayerConquerInfo': self.m_PlayerConquerInfo,
            'TeamSuccessConquer': self.m_TeamSuccessConquer }

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_CreatedMonsterDict = dData['CreatedMonster']
        self.m_PlayerConquerInfo = dData.get('PlayerConquerInfo', { })
        self.m_TeamSuccessConquer = dData.get('TeamSuccessConquer', 0)

    
    def OnRoomStart(self, oWarMgr, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        bAssignConquerChallenge = oWarMgr.Query('AssignConquerChallenge', False)
        if not bAssignConquerChallenge:
            if iLevel not in self.m_ChallengeDict:
                return None
            if iRoomPos not in self.m_ChallengeDict[iLevel]:
                return None
        oWarMgr.Delete('AssignConquerChallenge')
        iLayerNum = oLevelCtrl.m_LayerNum
        iLevelNum = oLevelCtrl.m_LevelNum
        iBaseLayerNum = oWarMgr.GetBaseLayer(iLayerNum)
        iLayVer = cl_warmgr.warcondition.WarCheckNewVerLayer(oWarMgr, iLevel)
        if not self.GetLevelMonster(iLayVer, iBaseLayerNum, iLevelNum):
            return None
        SeasonLog.Debug('game:%d, level:%d assign challenge pos:%s' % (self.m_Game.m_ID, iLevel, iRoomPos))
        if iLevel not in self.m_ChallengeDict:
            self.m_ChallengeDict[iLevel] = {
                iRoomPos: None }
        oChallenge = CConquerMonsterChallenge(self, iLevel, iRoomPos)
        self.m_ChallengeDict[iLevel][iRoomPos] = oChallenge

    
    def ValidLevelType(self, iLevelType):
        if iLevelType != LEVEL_TYPE_FIGHT:
            return False
        return True

    
    def OnLevelInit(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if not self.ValidLevelType(iLevelType):
            return None
        iLevel = dInfo['LevelID']
        iLevelNum = dInfo['Level']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayerNum = oLevelCtrl.m_LayerNum
        iBaseLayerNum = oWarMgr.GetBaseLayer(iLayerNum)
        iLayVer = cl_warmgr.warcondition.WarCheckNewVerLayer(oWarMgr, iLevel)
        if oWarMgr.IsEndless() and (iBaseLayerNum, iLevelNum) not in self.m_EndlessLevelDict:
            return None
        if not self.GetLevelMonster(iLayVer, iBaseLayerNum, iLevelNum):
            return None
        iLevel = dInfo['LevelID']
        self.GenerateRoomPos(iLevelNum, iLevel)

    
    def OnLevelFinish(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        if iLevel in self.m_ChallengeDict:
            for iRoomPos in list(self.m_ChallengeDict[iLevel].keys()):
                oChallenge = self.m_ChallengeDict[iLevel][iRoomPos]
                if oChallenge:
                    oChallenge.Release()
            

    
    def GenerateRoomPos(self, iLevelNum, iLevel):
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        bExcludeLastRoom = False
        iMaxLevel = oLevelCtrl.GetFightMaxLevel()
        if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and iLevelNum == iMaxLevel:
            bExcludeLastRoom = True
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        lstRoom = oLevelNode.m_RoomList
        if bExcludeLastRoom:
            iRoomCount = len(lstRoom[:-1])
        else:
            iRoomCount = len(lstRoom)
        if iRoomCount == 0:
            SeasonLog.Info('game:%d, level:%d roomcount is zero' % (self.m_Game.m_ID, iLevel))
            return None
        dChoose = { }
        dExcludeChoose = { }
        oLevelConfData = oLevelCtrl.m_LevelConfData
        iMap = oLevelNode.m_Map
        for iRoomPos in range(iRoomCount):
            (tPos, _) = oLevelNode.GetEliteInfo(iRoomPos, oLevelConfData)
            if not tPos:
                continue
            iProbability = 10 + iRoomPos * 5
            dChoose[iRoomPos] = iProbability
            if self.IsExcludeArea(lstRoom, iMap, iRoomPos):
                continue
            dExcludeChoose[iRoomPos] = iProbability
        
        if not dChoose:
            SeasonLog.Info('game:%d, level:%d no elite pos' % (self.m_Game.m_ID, iLevel))
            return None
        if dExcludeChoose:
            iRoomPos = ChooseKey(self.m_Game, dExcludeChoose)
        else:
            iRoomPos = ChooseKey(self.m_Game, dChoose)
        self.m_ChallengeDict[iLevel] = {
            iRoomPos: None }
        oLevelCtrl.m_RoomChallenge.AddIgnoreRoom(iLevel, iRoomPos)
        SeasonLog.Debug('game:%d, level:%d generate challenge pos %s' % (self.m_Game.m_ID, iLevel, iRoomPos))

    
    def IsExcludeArea(self, lstRoom, iMap, iRoomPos):
        for oLine in lstRoom[iRoomPos]:
            tArea = (iMap, oLine.m_Area)
            if tArea in self.m_ExcludeAreaTuple:
                return True
        
        return False

    
    def GetChallenge(self, iLevel, iRoomPos):
        if iLevel not in self.m_ChallengeDict:
            return None
        if iRoomPos not in self.m_ChallengeDict[iLevel]:
            return None
        return self.m_ChallengeDict[iLevel][iRoomPos]

    
    def AddCreatedMonster(self, iMonsterSID):
        self.m_CreatedMonsterDict[iMonsterSID] = 1

    
    def GetCreateMonster(self, iLayVer, iLayerNum, iBaseLayerNum, iLevelNum):
        oWarMgr = self.m_Game.m_WarMgr
        iGMConquerSID = oWarMgr.Query('GMConquerSID', 0)
        if iGMConquerSID:
            oWarMgr.Delete('GMConquerSID')
            return iGMConquerSID
        lstMonster = self.GetLevelMonster(iLayVer, iBaseLayerNum, iLevelNum)
        if not lstMonster:
            return 0
        if iLayerNum <= 4:
            lstRandom = []
            for iMonster in lstMonster:
                if iMonster in self.m_CreatedMonsterDict:
                    continue
                lstRandom.append(iMonster)
            
            if not lstRandom:
                return lstMonster[0]
            return lstRandom[self.m_Game.Random(len(lstRandom))]
        return lstMonster[self.m_Game.Random(len(lstMonster))]

    
    def GetLevelMonster(self, iLayVer, iBaseLayerNum, iLevelNum):
        tKey = (iLayVer, iBaseLayerNum, iLevelNum)
        if tKey not in self.m_LevelMonsterDict:
            return []
        return self.m_LevelMonsterDict[tKey]

    
    def ChallengeRelease(self, iLevel, iRoomPos):
        if iLevel not in self.m_ChallengeDict:
            return None
        dChallenge = self.m_ChallengeDict[iLevel]
        if iRoomPos not in dChallenge:
            return None
        dChallenge.pop(iRoomPos)
        if not dChallenge:
            self.m_ChallengeDict.pop(iLevel)
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelCtrl.m_RoomChallenge.RemoveIgnoreRoom(iLevel, iRoomPos)

    
    def ReleaseAllChallenge(self):
        for iLevel in list(self.m_ChallengeDict.keys()):
            for iRoomPos in list(self.m_ChallengeDict[iLevel].keys()):
                oChallenge = self.m_ChallengeDict[iLevel][iRoomPos]
                if oChallenge:
                    oChallenge.Release()
            
        

    
    def GetChallengeByTarget(self, oTarget):
        tLineIdx = oTarget.m_LineIdx
        if not tLineIdx:
            return None
        iLevel = tLineIdx[0]
        iRoomPos = tLineIdx[1]
        return self.GetChallenge(iLevel, iRoomPos)

    
    def StartConquer(self, oHero, iTargetID):
        oTarget = self.m_Game.GetObject(iTargetID, PY_FLAG_DEAD)
        if not oTarget:
            return None
        oChallenge = self.GetChallengeByTarget(oTarget)
        if not oChallenge:
            return None
        oChallenge.StartConquer(oHero, oTarget)

    
    def HaltConquer(self, oHero, iTargetID):
        oTarget = self.m_Game.GetObject(iTargetID, PY_FLAG_DEAD)
        if not oTarget:
            return None
        oChallenge = self.GetChallengeByTarget(oTarget)
        if not oChallenge:
            return None
        oChallenge.HaltConquer(oHero, oTarget)

    
    def ChangeConquerProbability(self, iMul):
        self.m_ConquerProbabilityMul = iMul

    
    def ClearConquerProbabilityChanged(self):
        self.m_ConquerProbabilityMul = 0

    
    def GetExtraAttr(self, sAttr):
        if sAttr not in self.m_ExtraAttr:
            return 0
        oAttr = self.m_ExtraAttr[sAttr]
        return oAttr.GetValue()

    
    def SetExtraAttr(self, sAttr, sKey, iValue):
        if sAttr not in self.m_ExtraAttr:
            return None
        oAttr = self.m_ExtraAttr[sAttr]
        oAttr.SetValue(sKey, iValue)

    
    def ClearExtraAttr(self, sAttr, sKey):
        if sAttr not in self.m_ExtraAttr:
            return None
        oAttr = self.m_ExtraAttr[sAttr]
        oAttr.ClearValue(sKey)

    
    def AddPlayerConquerCount(self, iPlayer, iSpendTime, iMonsterID):
        if iPlayer in self.m_PlayerConquerInfo:
            self.m_PlayerConquerInfo[iPlayer] += 1
        else:
            self.m_PlayerConquerInfo[iPlayer] = 1
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(iPlayer)
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SECCESSCONQUER_RECORD, oHero, {
                'SpendTime': iSpendTime,
                'VID': iMonsterID })

    
    def GetHeroConquerCount(self, iPlayer):
        if iPlayer not in self.m_PlayerConquerInfo:
            return 0
        return self.m_PlayerConquerInfo[iPlayer]

    
    def FinishConquer(self):
        self.m_TeamSuccessConquer += 1
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CONQUERSUCCESS, self.m_Game.m_WarMgr, { })

    
    def GetSuccessConquerCount(self):
        return self.m_TeamSuccessConquer

    
    def Release(self):
        if not self.m_Game:
            return None
        self.ReleaseAllChallenge()
        oWarMgr = self.m_Game.m_WarMgr
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.m_Key)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_Key)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Key)
        self.m_Game = None



class CExtraAttr(object):
    
    def __init__(self):
        self.m_Value = 0
        self.m_ChangeData = { }

    
    def GetValue(self):
        return self.m_Value

    
    def SetValue(self, sKey, iValue):
        if sKey in self.m_ChangeData:
            (iCount, iValue) = self.m_ChangeData[sKey]
            self.m_ChangeData[sKey] = (iCount + 1, iValue)
        else:
            self.m_ChangeData[sKey] = (1, iValue)
        self.CalValue()

    
    def ClearValue(self, sKey):
        if sKey in self.m_ChangeData:
            (iCount, iValue) = self.m_ChangeData[sKey]
            iCount -= 1
            if iCount == 0:
                self.m_ChangeData.pop(sKey)
            else:
                self.m_ChangeData[sKey] = (iCount, iValue)
            self.CalValue()

    
    def CalValue(self):
        self.m_Value = 0
        for iCount, iValue in self.m_ChangeData.values():
            self.m_Value += iValue
        



def NewConquerChallengeMgr(oConquerChallengeMgr, oData):
    oConquerChallengeMgr = ConquerChallengeMgr(oConquerChallengeMgr, oData)
    return oConquerChallengeMgr

