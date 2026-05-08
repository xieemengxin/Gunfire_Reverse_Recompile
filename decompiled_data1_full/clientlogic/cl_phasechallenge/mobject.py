# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_phasechallenge/mobject.pyc
# RelativePath: clientlogic/cl_phasechallenge/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import CHASTATUS_WAIT, CHASTATUS_CONTINUE, CHASTATUS_SUCCESS, CHASTATUS_OVER, PHASE_CHALLENGE_BOXMONSTER, CHALLENGE_SUCCESS, CHALLENGE_FAIL, CHALLENGE_GOAL_TARGET, MODEL_TYPE_SPHERE, DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, LEVEL_TYPE_FIGHT, MG_SOURCE_PHASECHALLENGE, NWARRIOR_DROP_DEMON, CHASTATUS_FAILED, PHASE_CHALLENGE_KILLBOXMONSTER, PHASE_CHALLENGE_START, PHASE_CHALLENGE_END, PHASE_CHALLENGE_OVER, PHASE_CHALLENGE_PLAYERLEAVE, PHASE_CHALLENGE_SEARCHTREASURE, SCENEICON_OPER_SHOW, SCENEICON_OPER_HIDE, SCENEICON_TYPE_SEARCHTHREASURE, PHASE_CHALLENGE_GOLDENELITE, NWARRIOR_DROP_ENCHANTING_BULLET, MINIMAPPT_OPER_SHOW, MINIMAPPT_OPER_HIDE, MINIMAPPT_SHOW_HIGHLIGHT, MINIMAPPT_SHOW_SHALLOW, MINIMAPPT_TYPE_PREBOXMONSTERPOS, MINIMAPPT_TYPE_SEARCHTHREASURE, WARRIOR_HERO, ATT_SHAPE_SPHERE, WARRIOR_NORMAL, REWARD_DROP_DIRECT, REWARD_DROP_DEMON, MINIMAPPT_TYPE_GOALDENELITEMONSTERPOS, SIDE_TYPE_MONSTER, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, LEVEL_STATE_FINISH, MONSTERAI_TYPE_HATESEARCH, PHASE_CHALLENGE_SINGLEPOINTOCCUPY, ATT_SHAPE_CYLINDER
from cl_object.logging import SurvivorLog
from cl_only import SendAlert, Time2Frame, Frame2Time, WFunctor, ChooseKey, ShufferList, PY_FLAG_DEAD, PythonError, Functor
from cl_pxlayer import PXLAYER_DEVENT, PXMASK_MONSTER, PXMASK_PLAYER
from cl_resmgr.aitempparam import GetAIConfParam
import cl_math
import cl_notify
import cl_msgcenter
import cl_reward
import cl_snetwar
import cl_object
import cl_formula
import cl_world
import cl_engphyobj
import cl_random
import cl_gamedebug as debug
import cllib.lib_flag
import math

class CPhaseChallengeMgr(cl_world.CObject):
    
    def __init__(self, oSurvivorElement, iID):
        super(CPhaseChallengeMgr, self).__init__(oSurvivorElement.m_Game, iID)
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_CallFlag = 'PhaseChallenge'
        self.m_ColdFrame = 0
        self.m_Challenge = { }
        self.m_Choosed = { }
        self.m_MonterPreCollect = []
        self.m_ChallengeRecord = { }
        self.m_Compensate = { }
        self.InitAttention()

    
    def Release(self):
        self.ReleaseAttention()
        for oChallenge in list(self.m_Challenge.values()):
            oChallenge.Release()
        
        self.m_Choosed = { }
        self.m_Challenge = None
        self.m_Survivor = None
        self.m_Game = None

    
    def Save(self):
        dData = { }
        dData['CR'] = self.m_ChallengeRecord
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ChallengeRecord = dData['CR']

    
    def InitAttention(self):
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag, -1, 0)
        cl_msgcenter.AddAttentionFunc(self.m_Survivor, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PICK, self.OnPick, self.m_CallFlag)

    
    def ReleaseAttention(self):
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self.m_Survivor, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_CallFlag)

    
    def OnPhaseStart(self, oSurvivor, dMsgInfo):
        iPhase = dMsgInfo['Phase']
        iChallenge = self.ChooseChallenge(iPhase)
        if iChallenge:
            self.AddChallenge(iPhase, iChallenge)

    
    def OnPlayerMapLoadOK(self, oSurvivor, oHero, dInfo):
        if self.m_Challenge:
            dPlayer = {
                oHero.m_PlayerID: 1 }
            for oChallenge in self.m_Challenge.values():
                oChallenge.HeroReEnterScene(dPlayer)
            
        if self.m_Game.m_WarMgr.IsTransferGame():
            self.CompensateReward(oHero.m_PlayerID)

    
    def OnReleaseChallenge(self, iPhase):
        if iPhase not in self.m_Challenge:
            return None
        self.m_ChallengeRecord[iPhase]['IsOver'] = 1
        self.m_Challenge.pop(iPhase)
        dPhaseInfo = self.m_Survivor.GetPhaseInfo()
        if iPhase not in dPhaseInfo or 'PhaseChallengeConfig' not in dPhaseInfo[iPhase]:
            return None
        dPhaseChallengeConfig = dPhaseInfo[iPhase]['PhaseChallengeConfig']
        iColdFrame = Time2Frame(dPhaseChallengeConfig['ColdTime'])
        iCurFrame = self.m_Survivor.m_FightTimerMgr.GetPlayFrame()
        self.m_ColdFrame = iCurFrame + iColdFrame

    
    def OnLevelNodeInit(self, oSurvivor, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_FIGHT:
            self.m_MonterPreCollect = [
                2349]
        else:
            self.m_MonterPreCollect = []

    
    def GetMonsterPreCollect(self):
        return self.m_MonterPreCollect

    
    def ValidChooseChallenge(self):
        if self.m_Challenge:
            return 0
        if self.m_ColdFrame:
            iCurFrame = self.m_Survivor.m_FightTimerMgr.GetPlayFrame()
            if iCurFrame < self.m_ColdFrame:
                return 0
        return 1

    
    def GetChooseChallenge(self, iPhase):
        dPhaseInfo = self.m_Survivor.GetPhaseInfo()
        dChallengeWeight = dPhaseInfo[iPhase]['PhaseChallengeConfig']['ChallengeWeight']
        if not dChallengeWeight:
            return { }
        dChallenge = { }
        dSingleChallenge = { }
        bIsSingelGame = self.m_Game.m_WarMgr.IsSingleGame()
        dTeamPhaseChallenge = self.m_Game.m_WarData.m_TeamPhaseChallenge
        for iChallenge, iWeight in dChallengeWeight.items():
            if bIsSingelGame:
                if iChallenge in dTeamPhaseChallenge:
                    continue
                dSingleChallenge[iChallenge] = iWeight
            if iChallenge not in self.m_Choosed:
                dChallenge[iChallenge] = iWeight
        
        if not dChallenge:
            if bIsSingelGame:
                return dSingleChallenge
            return dChallengeWeight
        return dChallenge

    
    def ChooseChallenge(self, iPhase):
        if self.m_Game.m_WarMgr.Query('AssignPhaseRoomChallenge'):
            oWarMgr = self.m_Game.m_WarMgr
            iChallenge = oWarMgr.Query('AssignPhaseRoomChallenge')
            oWarMgr.Delete('AssignPhaseRoomChallenge')
            return iChallenge
        if self.m_Game.m_WarMgr.IsTransferGame() and iPhase in self.m_ChallengeRecord:
            if not self.m_ChallengeRecord[iPhase]['IsOver']:
                return self.m_ChallengeRecord[iPhase]['Challenge']
            return 0
        if not self.ValidChooseChallenge():
            return 0
        dPhaseInfo = self.m_Survivor.GetPhaseInfo()
        if iPhase not in dPhaseInfo or 'PhaseChallengeConfig' not in dPhaseInfo[iPhase]:
            return 0
        dPhaseChallengeConfig = dPhaseInfo[iPhase]['PhaseChallengeConfig']
        iRatio = dPhaseChallengeConfig['Ratio']
        if self.m_Game.Random(10000) >= iRatio:
            return 0
        dChallengeWeight = self.GetChooseChallenge(iPhase)
        if not dChallengeWeight:
            return 0
        iChallenge = ChooseKey(self.m_Game, dChallengeWeight)
        self.m_Choosed[iChallenge] = 1
        return iChallenge

    
    def AddChallenge(self, iPhase, iChallenge):
        if self.m_Challenge:
            return None
        oChallenge = self.CreatePhaseChallenge(iPhase, iChallenge)
        if not oChallenge:
            return None
        if iPhase not in self.m_ChallengeRecord:
            self.m_ChallengeRecord[iPhase] = {
                'Challenge': iChallenge,
                'IsOver': 0,
                'Reward': { } }
        self.m_Challenge[iPhase] = oChallenge

    
    def CreatePhaseChallenge(self, iPhase, iChallenge):
        oGame = self.m_Game
        clsChallengeData = oGame.m_WarData.GetPhaseChallengeData(iChallenge)
        if not clsChallengeData:
            SendAlert('err', '战场%d未配置阶段挑战 %d' % (oGame.GetWarMgr().m_SID, iChallenge))
            return None
        dAddData = {
            'Phase': iPhase }
        oChallenge = clsChallengeData.Create(oGame, dAddData)
        return oChallenge

    
    def RecordReward(self, iPhase, iChallenge, pid, iRewardType):
        if iPhase not in self.m_ChallengeRecord:
            SurvivorLog.Alert('%d phasechallenge %d not record' % (self.m_Game.m_ID, iPhase))
            return None
        if iChallenge != self.m_ChallengeRecord[iPhase]['Challenge']:
            SurvivorLog.Alert('%d %d phasechallenge reward %d not equal %d' % (self.m_Game.m_ID, iPhase, iChallenge, self.m_ChallengeRecord[iPhase]['Challenge']))
            return None
        dReward = self.m_ChallengeRecord[iPhase]['Reward'].setdefault(pid, { })
        iNewCnt = dReward.get(iRewardType, 0) + 1
        dReward[iRewardType] = iNewCnt

    
    def OnPick(self, oSurvivor, oHero, dInfo):
        if dInfo['Type'] != NWARRIOR_DROP_DEMON:
            return None
        if 'PhaseChallenge' not in dInfo:
            return None
        dPhaseChallenge = dInfo['PhaseChallenge']
        iPhase = dPhaseChallenge['Phase']
        if iPhase not in self.m_ChallengeRecord:
            SurvivorLog.Alert('%d phasechallenge %d not record in challengerecord' % (self.m_Game.m_ID, iPhase))
            return None
        if dPhaseChallenge['Challenge'] != self.m_ChallengeRecord[iPhase]['Challenge']:
            SurvivorLog.Alert('%d %d phasechallenge onpick %d not equal %d' % (self.m_Game.m_ID, iPhase, dPhaseChallenge['Challenge'], self.m_ChallengeRecord[iPhase]['Challenge']))
            return None
        dReward = self.m_ChallengeRecord[iPhase]['Reward']
        pid = oHero.m_PlayerID
        if pid not in dReward:
            return None
        iRewardType = dPhaseChallenge['RewardType']
        if iRewardType not in dReward[pid]:
            return None
        iNewCnt = dReward[pid][iRewardType] - 1
        if iNewCnt <= 0:
            dReward[pid].pop(iRewardType)
        else:
            dReward[pid][iRewardType] = iNewCnt

    
    def CompensateReward(self, iTargetPlayer):
        oGame = self.m_Game
        if iTargetPlayer in self.m_Compensate:
            return None
        self.m_Compensate[iTargetPlayer] = 1
        for iPhase, dRecord in self.m_ChallengeRecord.items():
            iChallenge = dRecord['Challenge']
            clsData = oGame.m_WarData.GetPhaseChallengeData(iChallenge)
            if not clsData:
                SendAlert('err', '战场%d未配置阶段挑战 %d' % (oGame.m_WarMgr.m_SID, iChallenge))
                continue
            dReward = clsData.m_Reward
            if iTargetPlayer not in dRecord['Reward']:
                continue
            dCompensate = dRecord['Reward'][iTargetPlayer]
            oHero = oGame.m_WarMgr.GetHeroByPlayer(iTargetPlayer)
            if not oHero:
                continue
            SurvivorLog.Debug(f'''game：{oGame.m_ID} phasechallenge compensate {iTargetPlayer} {iPhase} {iChallenge} {dCompensate}''')
            for iRewardType, iCnt in dCompensate.items():
                if iRewardType not in dReward:
                    continue
                dStaticInfo = {
                    'PhaseChallenge': {
                        'Phase': iPhase,
                        'Challenge': iChallenge,
                        'RewardType': iRewardType } }
                for _ in range(iCnt):
                    
                    try:
                        self.TrueReward(oHero, dReward[iRewardType], dStaticInfo)
                    except:
                        PythonError()

                
            
        

    
    def TrueReward(self, oHero, dReward, dStaticInfo):
        iHero = oHero.m_ID
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'CanReward': 0,
            'AutoReward': 0,
            'OnlyRewardAttack': 1,
            'RepeatReward': 1 }
        dHeroMGInfo = cl_reward.RewardItemByMiniGame(oHero, iHero, dReward, 'PhaseChallengeMgr', MG_SOURCE_PHASECHALLENGE, dExtInfo)
        if not dHeroMGInfo or iHero not in dHeroMGInfo:
            return None
        dMGInfo = dHeroMGInfo[iHero]
        oResMgr = self.m_Game.GetResMgr()
        oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_DEMON, GetDropPos(self.m_Game, oHero), [
            dMGInfo], { }, dStaticInfo = dStaticInfo, iOwner = iHero)

    
    def OnSurvivorOver(self):
        for oChallenge in list(self.m_Challenge.values()):
            oChallenge.Release()
        
        self.m_MonterPreCollect = []



class CNewPhaseChallengeMgr(cl_world.CObject):
    
    def __init__(self, oSurvivorElement, iID):
        super(CNewPhaseChallengeMgr, self).__init__(oSurvivorElement.m_Game, iID)
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_CallFlag = 'NewPhaseChallenge'
        self.m_Challenge = { }
        self.m_ReleaseFlag = 0
        self.InitAttention()

    
    def InitAttention(self):
        self.m_Game.AddGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_CallFlag)

    
    def ReleaseAttention(self):
        self.m_Game.DoneGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)

    
    def Release(self):
        self.m_ReleaseFlag = 1
        for oChallenge in list(self.m_Challenge.values()):
            oChallenge.Release()
        
        self.m_Challenge = { }
        self.m_Survivor = None
        self.m_Game = None

    
    def OnReleaseChallenge(self, iPhase):
        if self.m_ReleaseFlag:
            return None
        oSurvivor = self.m_Survivor
        dExtraInfo = { }
        if iPhase in self.m_Challenge:
            oChallenge = self.m_Challenge.pop(iPhase)
            if oChallenge.m_OverStatus == CHASTATUS_FAILED:
                dExtraInfo['NoReWard'] = 1
        if oSurvivor.m_LevelState == LEVEL_STATE_FINISH:
            return None
        oSurvivor.ResumePauseCorrelation()
        oSurvivor.PreAddPhase(dExtraInfo)

    
    def RecordReward(self, iPhase, iChallenge, pid, iRewardType):
        pass

    
    def AddChallenge(self, iPhase, iChallenge):
        if self.m_Challenge:
            return None
        oChallenge = self.CreatePhaseChallenge(iPhase, iChallenge)
        if not oChallenge:
            return None
        self.m_Challenge[iPhase] = oChallenge
        self.m_Survivor.RemovePauseCorrelation()

    
    def OnPlayerMapLoadOK(self, oSurvivor, oHero, dInfo):
        if self.m_Challenge:
            dPlayer = {
                oHero.m_PlayerID: 1 }
            for oChallenge in self.m_Challenge.values():
                oChallenge.HeroReEnterScene(dPlayer)
            

    
    def CreatePhaseChallenge(self, iPhase, iChallenge):
        oGame = self.m_Game
        clsChallengeData = oGame.m_WarData.GetPhaseChallengeData(iChallenge)
        if not clsChallengeData:
            SendAlert('err', '战场%d未配置阶段挑战 %d' % (oGame.GetWarMgr().m_SID, iChallenge))
            return None
        dAddData = {
            'Phase': iPhase }
        oChallenge = clsChallengeData.Create(oGame, dAddData)
        return oChallenge



class CBaseChallenge(object):
    m_SID = 0
    m_Type = 0
    m_ReadyNotify = ''
    m_ChallengeName = ''
    m_ChallengeNotify = ''
    m_SuccessNotify = ''
    m_FailedNotify = ''
    m_RewardNpc = 0
    m_EffectState = 0
    m_ReadyTime = 0
    m_ChallengeTime = 0
    m_TargetValue = 0
    m_OverStatus = 0
    m_Reward = { }
    m_HpConfig = { }
    
    def __init__(self, oChallengeMgr, oLevelNode, iPhase):
        self.m_ChallengeMgr = oChallengeMgr
        self.m_Game = oChallengeMgr.m_Game
        self.m_LevelNode = oLevelNode
        self.m_Phase = iPhase
        self.m_Status = CHASTATUS_WAIT
        self.m_RewardType = CHALLENGE_FAIL
        self.m_StartFrame = 0
        self.m_Key = '%s_%d_%d' % (self.__class__.__name__[1:], oLevelNode.m_Level, iPhase)
        self.m_MiniMapPosInfo = { }

    
    def Init(self, clsData, dAddData):
        self.m_SID = clsData.m_SID
        self.m_Reward = clsData.m_Reward
        self.m_EffectState = clsData.m_EffectState
        self.m_ChallengeName = clsData.m_ChallengeName
        self.m_ReadyNotify = clsData.m_ReadyNotify
        self.m_ChallengeNotify = clsData.m_ChallengeNotify
        self.m_SuccessNotify = clsData.m_SuccessNotify
        self.m_FailedNotify = clsData.m_FailedNotify
        self.m_ReadyTime = clsData.m_ReadyTime
        self.m_ChallengeTime = cl_formula.GetFormulaResult(self, clsData.m_ChallengeTime)
        self.m_HpConfig = clsData.m_HpConfig
        dPlayer = self.GetScenePlayers()
        SurvivorLog.Info('%s %s phasechallenge:%s init %d-%d' % (self.m_Game.m_ID, dPlayer, self.m_SID, self.m_LevelNode.m_Level, self.m_Phase))
        if self.m_ReadyTime:
            self.m_StartFrame = self.m_Game.GetFrameNum()
            self.RateNotify(dPlayer)
            self.OnEnterReady()
            self.m_ChallengeMgr.m_Survivor.Call_Out(self.StartChallenge, Time2Frame(self.m_ReadyTime), self.m_Key + 'Start')
        else:
            self.StartChallenge()
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayeLeave, 'PhaseChallenge')

    
    def Release(self):
        self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'Start')
        self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'Over')
        dPlayer = self.GetScenePlayers()
        SurvivorLog.Info('%s %s phasechallenge:%s release rlt:%d %d-%d' % (self.m_Game.m_ID, dPlayer, self.m_SID, self.m_Status, self.m_LevelNode.m_Level, self.m_Phase))
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, 'PhaseChallenge')
        self.m_ChallengeMgr.OnReleaseChallenge(self.m_Phase)
        self.m_ChallengeMgr = None
        self.m_LevelNode = None
        self.m_Game = None

    
    def OnPlayeLeave(self, oWarMgr, oTarget, dInfo):
        if self.m_Status not in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            lstHero = self.m_Game.m_WarMgr.GetLiveHero()
            iOver = len(lstHero) <= 1
            dData = {
                'Rlt': self.m_Status == CHASTATUS_SUCCESS,
                'LevelID': self.m_LevelNode.m_Level,
                'Phase': self.m_Phase,
                'Type': self.m_Type,
                'OtherInfo': { },
                'Reward': self.m_RewardType != CHALLENGE_FAIL,
                'Over': iOver,
                'pid': 0 }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_PLAYERLEAVE)

    
    def OnEnterReady(self):
        pass

    
    def GetScenePlayers(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if not oScene:
            return { }
        return oScene.GetPlayers()

    
    def GetSceneHero(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if not oScene:
            return { }
        return oScene.GetHeros()

    
    def ChangeRewardType(self, iType):
        if iType == self.m_RewardType:
            return None
        if self.m_RewardType not in (CHALLENGE_SUCCESS, CHALLENGE_FAIL, CHALLENGE_GOAL_TARGET):
            return None
        self.m_RewardType = iType

    
    def ChallengeNotify(self, dPlayer, iTime, sRplMsg, dReplace):
        cl_notify.SendCommonNotifyNoTransfer(self.m_Game, dPlayer, iTime, sRplMsg, dReplace)

    
    def StartChallenge(self):
        if not self.m_ChallengeTime:
            SendAlert('err', '阶段挑战%d 未设置持续时间' % self.m_SID)
            return None
        self.m_Status = CHASTATUS_CONTINUE
        self.m_StartFrame = self.m_Game.GetFrameNum()
        dData = {
            'Level': self.m_LevelNode.m_Level,
            'Type': self.m_Type,
            'Phase': self.m_Phase }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_START)
        self.OnStartChallenge()
        self.m_ChallengeMgr.m_Survivor.Call_Out(WFunctor(self.OverChallenge, { }), Time2Frame(self.m_ChallengeTime), self.m_Key + 'Over')
        self.RateNotify(self.GetScenePlayers())

    
    def OnStartChallenge(self):
        pass

    
    def CheckChallengeStatus(self):
        if self.m_Status == CHASTATUS_OVER:
            return self.m_Status
        return CHASTATUS_SUCCESS

    
    def OverChallenge(self, dParam):
        self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'Over')
        iStatus = self.CheckChallengeStatus()
        if iStatus not in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            return None
        self.m_Status = iStatus
        self.m_OverStatus = iStatus
        dPlayer = self.GetScenePlayers()
        cl_notify.ClearCommonNotifyNoTransfer(self.m_Game, dPlayer, self.m_ChallengeNotify, { })
        if self.m_Status == CHASTATUS_SUCCESS:
            self.ChallengeNotify(dPlayer, 500, self.m_SuccessNotify, { })
        else:
            self.ChallengeNotify(dPlayer, 500, self.m_FailedNotify, { })
        SurvivorLog.Info('%s %s phasechallenge:%s over rlt:%d %d-%d' % (self.m_Game.m_ID, dPlayer, self.m_SID, self.m_Status, self.m_LevelNode.m_Level, self.m_Phase))
        dData = {
            'Rlt': self.m_Status == CHASTATUS_SUCCESS,
            'LevelID': self.m_LevelNode.m_Level,
            'Phase': self.m_Phase,
            'Type': self.m_Type,
            'OtherInfo': dParam }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_END)
        self.OnOverChallenge(dParam)
        self.Reward()
        self.m_Status = CHASTATUS_OVER
        self.Release()

    
    def OnOverChallenge(self, dParam):
        pass

    
    def RateNotify(self, dPlayer):
        if self.m_Status not in (CHASTATUS_CONTINUE, CHASTATUS_WAIT):
            return None
        if self.m_Status == CHASTATUS_WAIT:
            iRemainTime = self.m_ReadyTime - Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
            dReplace = {
                '$remain': str(iRemainTime),
                '$total': str(self.m_ReadyTime) }
            self.ChallengeNotify(dPlayer, iRemainTime, self.m_ReadyNotify, dReplace)
        else:
            iRemainTime = self.m_ChallengeTime - Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
            dReplace = {
                '$remain': str(iRemainTime),
                '$total': str(self.m_ChallengeTime) }
            self.ChallengeNotify(dPlayer, iRemainTime, self.m_ChallengeNotify, dReplace)
            cl_snetwar.GS2CStartChallenge(self.m_Game, self.m_Type, self.m_ChallengeTime, self.m_ChallengeNotify, dReplace, dPlayer)

    
    def Reward(self):
        if self.m_Status not in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            return None
        iRewardType = self.m_RewardType
        if not (self.m_Reward) or iRewardType not in self.m_Reward:
            return None
        dReward = self.m_Reward[iRewardType]
        self.m_Reward = { }
        self.SendReward(dReward, iRewardType, REWARD_DROP_DEMON)

    
    def SendReward(self, dReward, iRewardType, iDropType):
        oResMgr = self.m_Game.GetResMgr()
        iAutoReward = 0
        if iDropType == REWARD_DROP_DIRECT:
            iAutoReward = 1
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            dExtInfo = {
                'CalOffset': 0,
                'CheckGoldenCup': 1,
                'CanReward': 0,
                'AutoReward': iAutoReward,
                'OnlyRewardAttack': 1,
                'RepeatReward': 1 }
            dHeroMGInfo = cl_reward.RewardItemByMiniGame(oHero, iHero, dReward, self.m_Key, MG_SOURCE_PHASECHALLENGE, dExtInfo)
            if iDropType == REWARD_DROP_DEMON:
                self.m_ChallengeMgr.RecordReward(self.m_Phase, self.m_SID, oHero.m_PlayerID, iRewardType)
            
            if not dHeroMGInfo or iHero not in dHeroMGInfo:
                continue
            dStaticInfo = {
                'PhaseChallenge': {
                    'Phase': self.m_Phase,
                    'Challenge': self.m_SID,
                    'RewardType': iRewardType } }
            dMGInfo = dHeroMGInfo[iHero]
            oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_DEMON, GetDropPos(self.m_Game, oHero), [
                dMGInfo], { }, dStaticInfo = dStaticInfo, iOwner = iHero)
        

    
    def HeroReEnterScene(self, dPlayer):
        if self.m_Status not in (CHASTATUS_OVER, CHASTATUS_WAIT):
            self.RateNotify(dPlayer)

    
    def GetChallengePos(self, dGroup):
        lstPos = []
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dChallengePos = oLevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'phasechallengepos')
        for iGroup in dGroup:
            if iGroup not in dChallengePos:
                continue
            lstPos.extend(dChallengePos[iGroup])
        
        return lstPos

    
    def ChooseMonsterPos(self, iMinDistance, iMaxDistance, iNum, lstPos):
        lstPos = [ dPos['Center'] for dPos in lstPos ]
        if len(lstPos) <= iNum:
            return lstPos
        lstChallengePos = []
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oTarget = oSurvivor.GetMaxDamageTarget()
        lstDistance = []
        if oTarget:
            vTarget = oTarget.GetPos()
            lstBestPos = []
            for vPos in lstPos:
                fDistance = cl_math.CalDistance(vTarget, vPos)
                if fDistance > iMaxDistance:
                    continue
                if fDistance >= iMinDistance:
                    lstBestPos.append(vPos)
                    continue
                lstDistance.append((fDistance, vPos))
            
            if lstBestPos:
                if len(lstBestPos) > iNum:
                    lstChallengePos = ShufferList(self.m_Game, lstBestPos, iNum)
                    return lstChallengePos
                lstChallengePos = lstBestPos
        iNum -= len(lstChallengePos)
        if iNum and lstDistance:
            iLen = len(lstDistance)
            if iLen <= iNum:
                iTimes = iLen
            else:
                lstDistance.sort(reverse = True)
                iTimes = iNum
            for iIndex in range(iTimes):
                lstChallengePos.append(lstDistance[iIndex][1])
            
            iNum -= iTimes
        if iNum:
            lstLeftPos = []
            for vPos in lstPos:
                if vPos not in lstChallengePos:
                    lstLeftPos.append(vPos)
            
            lstChallengePos.extend(ShufferList(self.m_Game, lstLeftPos, iNum))
        return lstChallengePos

    
    def OnCreateMonsters(self, lstMonster):
        if not self.m_HpConfig:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iCount = oWarMgr.GetAllPlayerCnt()
        if iCount not in self.m_HpConfig:
            return None
        fRatio = self.m_HpConfig[iCount]
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oMonster.AttrForceSet('HPMax', int(oMonster.QueryAttr('HPMax') * fRatio), 'HpConfig')
            oMonster.AttrForceSet('ShieldMax', int(oMonster.QueryAttr('ShieldMax') * fRatio), 'HpConfig')
            oMonster.AttrForceSet('ArmorMax', int(oMonster.QueryAttr('ArmorMax') * fRatio), 'HpConfig')
        

    
    def CreateMiniMapPosInfo(self, iType, iShowType, lstPos):
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        iLevel = oLevelCtrl.m_CurNode.m_Level
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        dMiniMap = { }
        for idx, vPos in enumerate(lstPos):
            dMiniMap[idx] = [
                oMiniMap.NewPtID(),
                iType,
                iShowType,
                vPos]
        
        return dMiniMap

    
    def UpdateMiniMapPos(self, iOperate, lstPosInfo, dPlayer):
        oCtrlMgr = self.m_LevelNode.m_CtrlMgr
        if not oCtrlMgr:
            return None
        oLevelNode = oCtrlMgr.m_CurNode
        if not oLevelNode:
            return None
        cl_snetwar.GS2CUpdateMiniMapPos(self.m_Game, oLevelNode.m_Level, iOperate, lstPosInfo, dPlayer)



def GetDropPos(oGame, oHero):
    vBasePos = oHero.GetPos()
    vFace = oHero.GetFacing()
    vDir = (vFace[0], 0, vFace[2])
    vDropPos = oGame.Scene_RandomPointSectorInMesh(oHero.m_Scene, vBasePos, vDir, 9, 10, 0, 60)
    if not vDropPos:
        vDropPos = vBasePos
    return vDropPos


def GetMonsterArgs(oSurvivor):
    dAI = {
        'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
        'AIMethod': MONSTERAI_TYPE_DEFAULT }
    dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
    dAI.update(dHateSearchAI)
    dPhaseInfo = oSurvivor.m_PhaseData
    iGrade = dPhaseInfo[oSurvivor.m_Phase]['MonsterGrade']
    return (iGrade, dAI)


class CBoxMonsterChallenge(CBaseChallenge):
    m_Type = PHASE_CHALLENGE_BOXMONSTER
    m_ChallengeName = '宝箱怪挑战'
    m_StartFrame = 0
    m_BoxMonster = 0
    
    def Init(self, clsData, dAddData):
        super(CBoxMonsterChallenge, self).Init(clsData, dAddData)
        self.m_MonsterSID = clsData.m_Param[0]
        self.m_MinDistance = clsData.m_Param[1]
        self.m_MaxDistance = clsData.m_Param[2]
        self.m_NotifyDie = clsData.m_Param[3]
        self.m_HPRatio = clsData.m_Param[4]
        self.m_NotifyUp = clsData.m_Param[5]
        self.m_NotifyDown = clsData.m_Param[6]
        self.m_DieRemoveDelay = clsData.m_Param[7]
        self.m_EscapeRemoveDelay = clsData.m_Param[8]
        self.m_HintInnerRadius = clsData.m_Param[9]
        self.m_HintRadius = clsData.m_Param[10]
        self.m_MonsterPos = self.ChooseBoxMonsterPos()
        self.m_MiniMapPos = self.ChooseMiniMapPos()
        self.m_MiniMapPosInfo = self.CreateMiniMapPosInfo(MINIMAPPT_TYPE_PREBOXMONSTERPOS, MINIMAPPT_SHOW_HIGHLIGHT, [
            self.m_MiniMapPos])
        self.UpdateMiniMapPos(MINIMAPPT_OPER_SHOW, self.m_MiniMapPosInfo.values(), self.GetScenePlayers())

    
    def Release(self):
        self.ClearAttention()
        super().Release()

    
    def OnStartChallenge(self):
        self.UpdateMiniMapPos(MINIMAPPT_OPER_HIDE, self.m_MiniMapPosInfo.values(), self.GetScenePlayers())
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        self.m_BoxMonster = self.CreateMonster()
        self.OnCreateMonsters([
            self.m_BoxMonster])
        self.m_Game.AddGlobalAttention(oSurvivor.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)

    
    def ClearAttention(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        self.m_Game.DoneGlobalAttention(oSurvivor.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)

    
    def ChooseBoxMonsterPos(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dElitePosInfo = oLevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'monsterelitepos')
        vMonsterPos = None
        oTarget = oSurvivor.GetMaxDamageTarget()
        lstDistance = []
        if oTarget:
            vTarget = oTarget.GetPos()
            lstBestDistance = []
            for dPos in dElitePosInfo.values():
                fHighLimit = dPos['HighLimit'] if 'HighLimit' in dPos else 0
                vPos = dPos['Center']
                fDistance = cl_math.CalDistance(vTarget, vPos)
                if fDistance > self.m_MaxDistance:
                    continue
                if fDistance >= self.m_MinDistance:
                    if fHighLimit > 1e-06 and abs(vTarget[1] - vPos[1]) > fHighLimit:
                        continue
                    lstBestDistance.append(vPos)
                    continue
                lstDistance.append((fDistance, vPos))
            
            if lstBestDistance:
                idx = self.m_Game.Random(len(lstBestDistance))
                vMonsterPos = lstBestDistance[idx]
        if not vMonsterPos:
            if lstDistance:
                lstDistance.sort()
                vMonsterPos = lstDistance[-1][1]
            else:
                lstEliteInfo = list(dElitePosInfo.values())
                idx = self.m_Game.Random(len(lstEliteInfo))
                vMonsterPos = lstEliteInfo[idx]['Center']
        return vMonsterPos

    
    def ChooseMiniMapPos(self):
        for _ in range(10):
            vPos = self.m_Game.Scene_RandomPointSectorInMesh(self.m_LevelNode.m_Scene, self.m_MonsterPos, (1, 0, 0), self.m_HintInnerRadius, self.m_HintRadius, 1, 179)
            if vPos:
                return vPos
        
        return self.m_MonsterPos

    
    def CreateMonster(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iGrade = dPhaseInfo[oSurvivor.m_Phase]['Grade']
        vMonsterPos = (self.m_MonsterPos, (0, 0, 0), [], ({ }, None), 0)
        oMonster = oSurvivor.m_CurLine.m_MonsterCtrl.CreateMonster(self.m_MonsterSID, iGrade, vMonsterPos)
        if not oMonster:
            return 0
        if self.m_EscapeRemoveDelay:
            oMonster.m_RemoveDelay = Time2Frame(self.m_EscapeRemoveDelay)
        return oMonster.m_ID

    
    def CheckNoPlayerLive(self):
        lstHero = self.m_Game.m_WarMgr.GetLiveHero()
        if len(lstHero) <= 1:
            return True
        return False

    
    def OnDie(self, oSurvivor, oVictim, dMsgInfo):
        if oVictim.m_ID != self.m_BoxMonster:
            return None
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if oTarget and self.m_DieRemoveDelay:
            oTarget.m_RemoveDelay = Time2Frame(self.m_DieRemoveDelay)
        self.OverChallenge({ })

    
    def CheckChallengeStatus(self):
        if self.m_Status == CHASTATUS_OVER:
            return self.m_Status
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if not oTarget or oTarget.m_HP == 0:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnOverChallenge(self, dParam):
        dPlayer = self.GetScenePlayers()
        oBoxMonster = self.m_Game.GetObject(self.m_BoxMonster)
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_RewardType = CHALLENGE_SUCCESS
            if self.m_NotifyDie:
                self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyDie), { })
            elif self.GetBoxMonsterHPRatio(oBoxMonster) > self.m_HPRatio:
                self.m_RewardType = CHALLENGE_FAIL
                self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyUp), { })
            else:
                self.m_RewardType = CHALLENGE_GOAL_TARGET
                self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyDown), { })
        dParam['targetHP'] = None.HP()
        dParam['targetHPMax'] = oBoxMonster.QueryAttr('HPMax')
        dData = {
            'Rlt': self.m_Status == CHASTATUS_SUCCESS,
            'LevelID': self.m_LevelNode.m_Level,
            'Phase': self.m_Phase,
            'Type': self.m_Type,
            'OtherInfo': dParam,
            'Reward': self.m_RewardType != CHALLENGE_FAIL }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_OVER)
        if oBoxMonster:
            oBoxMonster.DieRemove()

    
    def OnPlayeLeave(self, oWarMgr, oTarget, dInfo):
        oBoxMonster = self.m_Game.GetObject(self.m_BoxMonster)
        if not oBoxMonster:
            return None
        if self.m_Status not in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            lstHero = self.m_Game.m_WarMgr.GetLiveHero()
            iOver = len(lstHero) <= 1
            pid = oWarMgr.GetPlayerIDByHeroID(dInfo['Hero'])
            dParam = {
                'targetHP': oBoxMonster.HP(),
                'targetHPMax': oBoxMonster.QueryAttr('HPMax') }
            dData = {
                'Rlt': self.m_Status == CHASTATUS_SUCCESS,
                'LevelID': self.m_LevelNode.m_Level,
                'Phase': self.m_Phase,
                'Type': self.m_Type,
                'OtherInfo': dParam,
                'Reward': self.m_RewardType != CHALLENGE_FAIL,
                'Over': iOver,
                'pid': pid }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_PLAYERLEAVE)

    
    def GetBoxMonsterHPRatio(self, oTarget):
        return oTarget.m_HP * 100 // oTarget.QueryAttr('HPMax')



class CNewBoxMonsterChallenge(CBoxMonsterChallenge):
    
    def ChooseBoxMonsterPos(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        lstSpawnPos = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'survivalData', 'BoxMonsterPos')
        vMonsterPos = None
        oTarget = oSurvivor.GetMaxDamageTarget()
        if oTarget:
            vTarget = oTarget.GetPos()
            lstBestDistance = []
            for vPos in lstSpawnPos:
                fDistance = cl_math.CalDistance(vTarget, vPos)
                if fDistance > self.m_MaxDistance or fDistance < self.m_MinDistance:
                    continue
                lstBestDistance.append(vPos)
            
            if lstBestDistance:
                idx = self.m_Game.Random(len(lstBestDistance))
                vMonsterPos = lstBestDistance[idx]
        if not vMonsterPos:
            idx = self.m_Game.Random(len(lstSpawnPos))
            vMonsterPos = lstSpawnPos[idx]
        return vMonsterPos

    
    def CreateMonster(self):
        oGame = self.m_Game
        (iGrade, dAI) = GetMonsterArgs(self.m_ChallengeMgr.m_Survivor)
        oMonster = oGame.m_ResMgr.CreateMonster(self.m_LevelNode.m_Scene, self.m_MonsterSID, self.m_MonsterPos, None, SIDE_TYPE_MONSTER, iGrade, dAI)
        if not oMonster:
            return 0
        if self.m_EscapeRemoveDelay:
            oMonster.m_RemoveDelay = Time2Frame(self.m_EscapeRemoveDelay)
        return oMonster.m_ID



class CKillBoxMonsterChallenge(CBaseChallenge):
    m_Type = PHASE_CHALLENGE_KILLBOXMONSTER
    m_ChallengeName = '歼灭钱龙挑战'
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_Value = 0
        self.m_TargetValue = 0
        self.m_MonsterList = []

    
    def Init(self, clsData, dAddData):
        super(CKillBoxMonsterChallenge, self).Init(clsData, dAddData)
        self.m_MonsterSID = clsData.m_Param[0]
        self.m_MinDistance = clsData.m_Param[1]
        self.m_MaxDistance = clsData.m_Param[2]
        self.m_MonsterNum = cl_formula.GetFormulaResult(self, clsData.m_Param[3])
        self.m_PosGroup = list(clsData.m_Param[4])
        self.m_NotifySuccess = clsData.m_Param[5]
        self.m_TargetValue = cl_formula.GetFormulaResult(self, clsData.m_Param[6])
        self.m_TargetRatio = clsData.m_Param[7]
        self.m_NotifyUp = clsData.m_Param[8]
        self.m_NotifyDown = clsData.m_Param[9]

    
    def Release(self):
        self.ClearAttention()
        super().Release()

    
    def OnStartChallenge(self):
        self.m_MonsterList = self.CreateMonster()
        self.OnCreateMonsters(self.m_MonsterList)
        for iMonster in self.m_MonsterList:
            oMonster = self.m_Game.GetObject(iMonster)
            if oMonster:
                cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_Key)
        

    
    def ClearAttention(self):
        for iMonster in self.m_MonsterList:
            oMonster = self.m_Game.GetObject(iMonster)
            if oMonster:
                cl_msgcenter.DoneEvent(oMonster, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        

    
    def CreateMonster(self):
        lstMonster = []
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iGrade = dPhaseInfo[oSurvivor.m_Phase]['Grade']
        lstPos = self.ChooseMonsterPos(self.m_MinDistance, self.m_MaxDistance, self.m_MonsterNum, self.GetChallengePos(self.m_PosGroup))
        for vPos in lstPos:
            vMonsterPos = (vPos, (0, 0, 0), [], ({ }, None), 0)
            oMonster = oSurvivor.m_CurLine.m_MonsterCtrl.CreateMonster(self.m_MonsterSID, iGrade, vMonsterPos)
            if oMonster:
                lstMonster.append(oMonster.m_ID)
        
        return lstMonster

    
    def OnMonsterDie(self, oTarget, dMsgInfo):
        self.m_Value += 1
        dPlayer = self.GetScenePlayers()
        dReplace = {
            '$cur': str(self.m_Value),
            '$target': str(self.m_TargetValue) }
        cl_notify.SendCommonNotify(self.m_Game, dPlayer, 9395, dReplace)
        if self.m_Value >= self.m_TargetValue:
            self.OverChallenge({ })
        else:
            self.RateNotify()

    
    def CheckChallengeStatus(self):
        if self.m_Status == CHASTATUS_OVER:
            return self.m_Status
        if self.m_Value >= self.m_TargetValue:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnOverChallenge(self, dParam):
        dPlayer = self.GetScenePlayers()
        if self.m_Value >= self.m_TargetValue:
            self.m_RewardType = CHALLENGE_SUCCESS
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifySuccess), { })
        elif int(self.m_Value * 100 // self.m_TargetValue) > self.m_TargetRatio:
            self.m_RewardType = CHALLENGE_GOAL_TARGET
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyUp), { })
        else:
            self.m_RewardType = CHALLENGE_FAIL
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyDown), { })
        iTargetHP = 0
        iTargetHPMax = 0
        for iMonster in self.m_MonsterList:
            oMonster = self.m_Game.GetObject(iMonster)
            if not oMonster:
                continue
            iTargetHP += oMonster.HP()
            iTargetHPMax += oMonster.QueryAttr('HPMax')
        
        dParam['targetHP'] = iTargetHP
        dParam['targetHPMax'] = iTargetHPMax
        dData = {
            'Rlt': self.m_Status == CHASTATUS_SUCCESS,
            'LevelID': self.m_LevelNode.m_Level,
            'Phase': self.m_Phase,
            'Type': self.m_Type,
            'OtherInfo': dParam,
            'Reward': self.m_RewardType != CHALLENGE_FAIL }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_OVER)
        for iMonster in self.m_MonsterList:
            oMonster = self.m_Game.GetObject(iMonster)
            if oMonster:
                oMonster.DieRemove()
        

    
    def OnPlayeLeave(self, oWarMgr, oTarget, dInfo):
        if not self.m_MonsterList:
            return None
        dParam = { }
        iTargetHP = 0
        iTargetHPMax = 0
        for iMonster in self.m_MonsterList:
            oMonster = self.m_Game.GetObject(iMonster)
            if not oMonster:
                continue
            iTargetHP += oMonster.HP()
            iTargetHPMax += oMonster.QueryAttr('HPMax')
        
        dParam['targetHP'] = iTargetHP
        dParam['targetHPMax'] = iTargetHPMax
        if self.m_Status not in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            lstHero = self.m_Game.m_WarMgr.GetLiveHero()
            iOver = len(lstHero) <= 1
            pid = oWarMgr.GetPlayerIDByHeroID(dInfo['Hero'])
            dData = {
                'Rlt': self.m_Status == CHASTATUS_SUCCESS,
                'LevelID': self.m_LevelNode.m_Level,
                'Phase': self.m_Phase,
                'Type': self.m_Type,
                'OtherInfo': dParam,
                'Reward': self.m_RewardType != CHALLENGE_FAIL,
                'Over': iOver,
                'pid': pid }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_PLAYERLEAVE)

    
    def RateNotify(self, dPlayer = None):
        if self.m_Status not in (CHASTATUS_CONTINUE, CHASTATUS_WAIT):
            return None
        if not dPlayer:
            dPlayer = self.GetScenePlayers()
        if self.m_Status == CHASTATUS_WAIT:
            iRemainTime = self.m_ReadyTime - Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
            dReplace = {
                '$remain': str(iRemainTime),
                '$total': str(self.m_ReadyTime) }
            self.ChallengeNotify(dPlayer, iRemainTime, self.m_ReadyNotify, dReplace)
        else:
            iRemainTime = self.m_ChallengeTime - Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
            dReplace = {
                '$remain': str(iRemainTime),
                '$total': str(self.m_ChallengeTime),
                '$cur': str(self.m_Value),
                '$target': str(self.m_TargetValue) }
            self.ChallengeNotify(dPlayer, iRemainTime, self.m_ChallengeNotify, dReplace)
            cl_snetwar.GS2CStartChallenge(self.m_Game, self.m_Type, self.m_ChallengeTime, self.m_ChallengeNotify, dReplace, dPlayer)



class CNewKillBoxMonsterChallenge(CKillBoxMonsterChallenge):
    
    def CreateMonster(self):
        oGame = self.m_Game
        (iGrade, dAI) = GetMonsterArgs(self.m_ChallengeMgr.m_Survivor)
        lstPos = self.ChooseMonsterPos(self.m_MinDistance, self.m_MaxDistance, self.m_MonsterNum, self.GetChallengePos(self.m_PosGroup))
        lstMonster = []
        for vPos in lstPos:
            oMonster = oGame.m_ResMgr.CreateMonster(self.m_LevelNode.m_Scene, self.m_MonsterSID, vPos, None, SIDE_TYPE_MONSTER, iGrade, dAI)
            if oMonster:
                lstMonster.append(oMonster.m_ID)
        
        return lstMonster



class CSearchTreasureChallenge(CBaseChallenge):
    m_Type = PHASE_CHALLENGE_SEARCHTREASURE
    m_ChallengeName = '占点寻宝挑战'
    
    def Init(self, clsData, dAddData):
        self.PreInit(clsData, dAddData)
        super(CSearchTreasureChallenge, self).Init(clsData, dAddData)
        self.m_ChallengeHero = self.m_Game.m_WarMgr.GetRoomHero()
        for iHero in self.m_ChallengeHero:
            cl_msgcenter.AddAttentionFunc(self.m_ChallengeMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, 'SearchTreasure')
        

    
    def PreInit(self, clsData, dAddData):
        self.m_SingleRatio = cl_formula.GetFormulaResult(self, clsData.m_Param[0])
        self.m_TreasurePosNum = cl_formula.GetFormulaResult(self, clsData.m_Param[1])
        self.m_ChooseGroup = clsData.m_Param[2]
        self.m_ActualRadius = clsData.m_Param[3]
        self.m_ActualShape = clsData.m_Param[4]
        self.m_HintRadius = clsData.m_Param[5]
        self.m_HintShape = clsData.m_Param[6]
        self.m_Expect = cl_formula.GetFormulaResult(self, clsData.m_Param[7])
        self.m_Sigma = cl_formula.GetFormulaResult(self, clsData.m_Param[8])
        self.m_TreasurePos = []
        self.m_SearchNum = 0
        self.m_ExpectSearchNum = 1
        self.m_TreasureEvent = { }
        self.m_ChallengeRewardCnt = self.m_TreasurePosNum - 1

    
    def Release(self):
        for iHero in self.m_ChallengeHero:
            cl_msgcenter.DoneAttention(self.m_ChallengeMgr, iHero, cl_msgcenter.MSG_WAR_DIE, 'SearchTreasure')
        
        for iTreasureEvent in self.m_TreasureEvent.values():
            oTreasureEvent = self.m_Game.GetObject(iTreasureEvent)
            if oTreasureEvent:
                oTreasureEvent.Remove('ChallengeRelease')
        
        super(CSearchTreasureChallenge, self).Release()

    
    def OnEnterReady(self):
        oGame = self.m_Game
        self.ChooseTreasurePos()
        self.InitExpectSearchNum()
        for idx, vPos in enumerate(self.m_TreasurePos):
            oTreasureEvent = NewTreasureEvent(oGame)
            dInfo = {
                'Center': vPos,
                'Index': idx }
            oTreasureEvent.Init(self, dInfo)
            self.m_TreasureEvent[idx] = oTreasureEvent.m_ID
        

    
    def InitExpectSearchNum(self):
        oRandomMgr = self.m_Game.m_RandomMgr
        sKey = 'SearchTreasureChallenge'
        if not oRandomMgr.ValidRandom(sKey):
            oRandomMgr.InitRandom(cl_random.RANDOM_DIRECT, sKey, { })
        iSigma = self.m_Sigma * 3
        iRandom = oRandomMgr.ChooseKey(sKey, {
            'Expect': self.m_Expect,
            'Sigma': iSigma })
        iRandom = round(iRandom / 100)
        if iRandom < 1:
            iRandom = 1
        if iRandom > self.m_TreasurePosNum:
            iRandom = self.m_TreasurePosNum
        self.m_ExpectSearchNum = iRandom
        if self.m_Game.m_WarMgr.Query('DebugRandom'):
            dPlayer = self.GetScenePlayers()
            TestExpectSearchNum(self.m_Game, dPlayer, self.m_ExpectSearchNum, self.m_Expect, iSigma, self.m_TreasurePosNum)

    
    def OnStartChallenge(self):
        for iTreasureEvent in self.m_TreasureEvent.values():
            oTreasureEvent = self.m_Game.GetObject(iTreasureEvent)
            if oTreasureEvent:
                oTreasureEvent.OnStartChallenge()
        
        self.DebugTreasurePos()

    
    def OnOverChallenge(self, dParam):
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_RewardType = CHALLENGE_SUCCESS
        dData = {
            'Rlt': self.m_Status == CHASTATUS_SUCCESS,
            'LevelID': self.m_LevelNode.m_Level,
            'Phase': self.m_Phase,
            'Type': self.m_Type,
            'OtherInfo': dParam,
            'Reward': self.m_RewardType != CHALLENGE_FAIL }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.m_Game.m_WarMgr, dData, iSub = PHASE_CHALLENGE_OVER)

    
    def ChooseTreasurePos(self):
        iGroup = ChooseKey(self.m_Game, self.m_ChooseGroup)
        lstPosInfo = self.GetChallengePos({
            iGroup: 1 })
        if not lstPosInfo or len(lstPosInfo) < self.m_TreasurePosNum:
            SendAlert('err', '战场%d 阶段挑战%d 组%d 配置宝藏刷新点小于%d' % (self.m_Game.m_WarMgr.m_SID, self.m_SID, iGroup, self.m_TreasurePosNum))
            return None
        lstPos = []
        for dInfo in lstPosInfo:
            lstPos.append(dInfo['Center'])
        
        self.m_TreasurePos = ShufferList(self.m_Game, lstPos, self.m_TreasurePosNum)

    
    def CheckChallengeStatus(self):
        if self.m_SearchNum >= self.m_ExpectSearchNum:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def DoneSearch(self, idx):
        self.m_SearchNum += 1
        self.m_TreasureEvent.pop(idx)
        if self.m_SearchNum >= self.m_ExpectSearchNum:
            self.OverChallenge({ })
            return None
        self.DoneSearchReward()

    
    def DoneSearchReward(self):
        if self.m_ChallengeRewardCnt <= 0:
            return None
        if not (self.m_Reward) or CHALLENGE_GOAL_TARGET not in self.m_Reward:
            return None
        dReward = self.m_Reward[CHALLENGE_GOAL_TARGET]
        self.m_ChallengeRewardCnt -= 1
        self.SendReward(dReward, CHALLENGE_GOAL_TARGET, REWARD_DROP_DIRECT)

    
    def OnHeroDie(self, oChallengeMgr, oHero, dMsgInfo):
        pid = oHero.m_PlayerID
        for iTreasureEvent in self.m_TreasureEvent.values():
            oTreasureEvent = self.m_Game.GetObject(iTreasureEvent)
            if not oTreasureEvent:
                continue
            if pid in oTreasureEvent.m_OccuptPlayer:
                oTreasureEvent.ChangeOccupyState(oHero, 1)
                break
        

    
    def HeroReEnterScene(self, dPlayer):
        if self.m_Status in (CHASTATUS_OVER,):
            return None
        self.RateNotify(dPlayer)
        for iTreasureEvent in self.m_TreasureEvent.values():
            oTreasureEvent = self.m_Game.GetObject(iTreasureEvent)
            if not oTreasureEvent:
                continue
            oTreasureEvent.OnReEnter(dPlayer)
            for pid in dPlayer:
                if pid in oTreasureEvent.m_OccuptPlayer:
                    oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
                    if not oHero:
                        continue
                    oTreasureEvent.ChangeOccupyState(oHero, 0)
            
        

    
    def DebugTreasurePos(self):
        oGame = self.m_Game
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_NORMAL)
            for _, vPos in enumerate(self.m_TreasurePos):
                debug.DebugCircle(oGame, vPos, self.m_ActualRadius, debug.LINE_NORMAL, rgb = 65280)
            



class CSinglePointOccupyChallenge(CBaseChallenge):
    m_Type = PHASE_CHALLENGE_SINGLEPOINTOCCUPY
    m_ChallengeName = '单点占领挑战'
    
    def Init(self, clsData, dAddData):
        self.m_OccupyEvent = -1
        self.m_Ratio = clsData.m_Param[0]
        self.m_ActualRadius = clsData.m_Param[1]
        self.m_ActualShape = clsData.m_Param[2]
        self.m_HintRadius = clsData.m_Param[3]
        self.m_HintShape = clsData.m_Param[4]
        self.m_PosIndex = clsData.m_Param[5]
        self.m_GoalProcess = clsData.m_Param[6]
        self.m_OccupyPos = (0, 0, 0)
        self.m_ProcessCbFun = { }
        super(CSinglePointOccupyChallenge, self).Init(clsData, dAddData)
        self.m_ChallengeHero = self.m_Game.m_WarMgr.GetRoomHero()
        for iHero in self.m_ChallengeHero:
            cl_msgcenter.AddAttentionFunc(self.m_ChallengeMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, 'SinglePointOccupy')
        

    
    def Release(self):
        for iHero in self.m_ChallengeHero:
            cl_msgcenter.DoneAttention(self.m_ChallengeMgr, iHero, cl_msgcenter.MSG_WAR_DIE, 'SinglePointOccupy')
        
        oOccupyEvent = self.m_Game.GetObject(self.m_OccupyEvent)
        if oOccupyEvent:
            oOccupyEvent.Remove('ChallengeRelease')
        self.m_ProcessCbFun = { }
        super(CSinglePointOccupyChallenge, self).Release()

    
    def CheckChallengeStatus(self):
        if self.m_OccupyEvent == 0:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnHeroDie(self, oChallengeMgr, oHero, dMsgInfo):
        pid = oHero.m_PlayerID
        oOccupyEvent = self.m_Game.GetObject(self.m_OccupyEvent)
        if not oOccupyEvent:
            return None
        if pid in oOccupyEvent.m_OccuptPlayer:
            oOccupyEvent.ChangeOccupyState(oHero, iLeave = 1)

    
    def OnEnterReady(self):
        oGame = self.m_Game
        self.ChoosePos()
        dInfo = {
            'Center': self.m_OccupyPos,
            'Index': 0 }
        oOccupyEvent = NewOccupyEvent(oGame)
        oOccupyEvent.Init(self, dInfo)
        self.m_OccupyEvent = oOccupyEvent.m_ID

    
    def ChoosePos(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        dSpawnPos = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'survivalData', 'OccupyPos')
        self.m_OccupyPos = dSpawnPos[self.m_PosIndex]

    
    def HeroReEnterScene(self, dPlayer):
        if self.m_Status in (CHASTATUS_OVER,):
            return None
        self.RateNotify(dPlayer)
        oOccupyEvent = self.m_Game.GetObject(self.m_OccupyEvent)
        if not oOccupyEvent:
            return None
        oOccupyEvent.OnReEnter(dPlayer)
        for pid in dPlayer:
            if pid in oOccupyEvent.m_OccuptPlayer:
                oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
                if not oHero:
                    continue
                oOccupyEvent.ChangeOccupyState(oHero, iLeave = 0)
        

    
    def OnStartChallenge(self):
        oOccupyEvent = self.m_Game.GetObject(self.m_OccupyEvent)
        if oOccupyEvent:
            oOccupyEvent.OnStartChallenge()
        self.DebugTreasurePos()

    
    def DoneOccupy(self, idx):
        self.m_OccupyEvent = 0
        self.OverChallenge({ })

    
    def OnOverChallenge(self, dParam):
        oOccupyEvent = self.m_Game.GetObject(self.m_OccupyEvent)
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_RewardType = CHALLENGE_SUCCESS
        elif oOccupyEvent and oOccupyEvent.GetCurProcess() / 100 >= self.m_GoalProcess:
            self.m_RewardType = CHALLENGE_GOAL_TARGET

    
    def AddProcessCbFun(self, iProcess, cbFun):
        self.m_ProcessCbFun[iProcess] = cbFun

    
    def RemoveProcessCbFun(self, iProcess):
        if iProcess in self.m_ProcessCbFun:
            self.m_ProcessCbFun.pop(iProcess)

    
    def DebugTreasurePos(self):
        oGame = self.m_Game
        if oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_NORMAL)
            debug.DebugCircle(oGame, self.m_OccupyPos, self.m_ActualRadius, debug.LINE_NORMAL, rgb = 65280)

    
    def GetFirstCbProcess(self):
        if not self.m_ProcessCbFun:
            return 0
        iFirstProcess = 10000
        for iProcess in self.m_ProcessCbFun:
            if iProcess < iFirstProcess:
                iFirstProcess = iProcess
        
        return iFirstProcess



class TreasureEvent(cl_world.CSceneObject):
    m_Occupying = 9382
    
    def __init__(self, oGame, nid):
        super(TreasureEvent, self).__init__(oGame, nid)
        self.m_Trigger = None
        self.m_Challenge = None
        self.m_Index = -1
        self.m_Process = 0
        self.m_ActualEffectID = 0
        self.m_ActualShape = 0
        self.m_HintEffectID = 0
        self.m_OccuptPlayer = { }
        self.m_OccuptFrame = 0
        self.m_IsDone = 0
        self.m_ActualPos = None
        self.m_HintPos = None
        self.m_MiniMapPosInfo = None
        self.m_IsReal = 0

    
    def Init(self, oChallenge, dInfo):
        self.m_Challenge = oChallenge
        self.m_Index = dInfo['Index']
        self.m_ActualShape = self.m_Challenge.m_ActualShape
        self.m_ActualPos = dInfo['Center']
        iScene = self.m_Challenge.m_LevelNode.m_Scene
        self.InitHintPos()
        dPlayer = self.m_Challenge.GetScenePlayers()
        self.m_MiniMapPosInfo = self.m_Challenge.CreateMiniMapPosInfo(MINIMAPPT_TYPE_SEARCHTHREASURE, MINIMAPPT_SHOW_SHALLOW, [
            self.m_HintPos])
        self.m_Challenge.UpdateMiniMapPos(MINIMAPPT_OPER_SHOW, self.m_MiniMapPosInfo.values(), dPlayer)
        self.m_HintEffectID = self.m_Game.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(self.m_Game, iScene, self.m_HintEffectID, self.m_Challenge.m_HintShape, self.m_HintPos, dPlayer)

    
    def InitHintPos(self):
        vDir = (1, 0, 0)
        iScene = self.m_Challenge.m_LevelNode.m_Scene
        fRadius = self.m_Challenge.m_HintRadius - self.m_Challenge.m_ActualRadius
        fInnerRadius = 3
        for _ in range(10):
            vPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, self.m_ActualPos, vDir, fInnerRadius, fRadius, 1, 179)
            if vPos:
                self.m_HintPos = vPos
                break
        
        if not self.m_HintPos:
            self.m_HintPos = self.m_ActualPos

    
    def OnStartChallenge(self):
        dPlayer = self.m_Challenge.GetScenePlayers()
        iScene = self.m_Challenge.m_LevelNode.m_Scene
        cl_snetwar.GS2CDeleteEffect(self.m_Game, iScene, self.m_HintEffectID, dPlayer)
        for lstInfo in self.m_MiniMapPosInfo.values():
            lstInfo[2] = MINIMAPPT_SHOW_HIGHLIGHT
            lstInfo[3] = self.m_ActualPos
        
        self.m_Challenge.UpdateMiniMapPos(MINIMAPPT_OPER_SHOW, self.m_MiniMapPosInfo.values(), dPlayer)
        self.Goto(iScene, self.m_ActualPos)
        self.m_Trigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self, PXLAYER_DEVENT, {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': self.m_Challenge.m_ActualRadius }, self.OnTrigger)
        self.m_Trigger.rigidbody.E_SetKinematic(1)
        self.m_ActualEffectID = self.m_Game.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(self.m_Game, self.m_Scene, self.m_ActualEffectID, self.m_ActualShape, self.m_ActualPos, dPlayer)
        self.UpdateSceneIcon(SCENEICON_OPER_SHOW)

    
    def OnReEnter(self, dPlayer):
        iScene = self.m_Challenge.m_LevelNode.m_Scene
        if self.m_Challenge.m_Status == CHASTATUS_WAIT:
            cl_snetwar.GS2CAddEffect(self.m_Game, iScene, self.m_HintEffectID, self.m_Challenge.m_HintShape, self.m_HintPos, dPlayer)
        else:
            cl_snetwar.GS2CAddEffect(self.m_Game, iScene, self.m_ActualEffectID, self.m_ActualShape, self.m_ActualPos, dPlayer)
        self.m_Challenge.UpdateMiniMapPos(MINIMAPPT_OPER_SHOW, self.m_MiniMapPosInfo.values(), dPlayer)
        self.UpdateSceneIcon(SCENEICON_OPER_SHOW, dPlayer)

    
    def OnTrigger(self, obj, iLeave):
        if not obj:
            return None
        if not obj.m_FightType & WARRIOR_HERO:
            return None
        if not iLeave:
            dMask = {
                'Mask': PXMASK_PLAYER,
                'BlockMask': 0 }
            fHalfHeight = self.m_Challenge.m_ActualRadius / 2
            vStart = (self.m_ActualPos[0], self.m_ActualPos[1] + fHalfHeight, self.m_ActualPos[2])
            lstArgs = [
                vStart,
                self.m_Challenge.m_ActualRadius,
                fHalfHeight + 1]
            lstVLST = cl_math.GetAttackTargetList(self.m_Game, self.m_Scene, ATT_SHAPE_CYLINDER, lstArgs, dMask)
            if obj.m_ID not in lstVLST:
                return None
        self.ChangeOccupyState(obj, iLeave)

    
    def ChangeOccupyState(self, oHero, iLeave):
        sFlag = 'SearchTreasureChallenge'
        self.Remove_Call_Out(sFlag)
        self.UpdateProcess()
        if iLeave:
            self.StopOccupy(oHero)
        else:
            self.StartOccupy(oHero)
        self.UpdateSceneIcon(SCENEICON_OPER_SHOW)
        if self.m_OccuptPlayer:
            iRemainTime = self.GetRemainTime()
            iTotalTime = self.GetTotalTime(iRemainTime)
            self.SendOccupyingMsg(iRemainTime, iTotalTime)
            self.Call_Out(self.TryDone, Time2Frame(iRemainTime) + 1, sFlag)

    
    def UpdateSceneIcon(self, iOperate, dPlayer = None):
        if self.m_IsDone:
            return None
        if not dPlayer:
            dPlayer = self.m_Challenge.GetScenePlayers()
        iLevel = self.m_Challenge.m_LevelNode.m_Level
        iOccupy = 1 if self.m_OccuptPlayer else 0
        iRatio = self.GetRatio()
        lstArgs = [
            ('Process', self.m_Process),
            ('TotalProcess', 10000),
            ('Ratio', iRatio),
            ('IsOccupy', iOccupy),
            ('idx', self.m_Index + 1)]
        lstIcon = [
            (self.m_ID, SCENEICON_TYPE_SEARCHTHREASURE, self.m_ActualPos, lstArgs)]
        cl_snetwar.GS2CUpdateSceneIcon(self.m_Game, dPlayer, iLevel, iOperate, lstIcon)

    
    def StartOccupy(self, oHero):
        if self.m_IsDone or oHero.IsDead():
            return None
        self.UpdateEffectState(1002)
        self.m_OccuptPlayer[oHero.m_PlayerID] = 1
        self.m_OccuptFrame = self.m_Game.GetFrameNum()

    
    def StopOccupy(self, oHero):
        if oHero.m_PlayerID not in self.m_OccuptPlayer:
            return None
        self.ClearOccupyingMsg()
        if self.m_IsDone:
            return None
        self.m_OccuptPlayer.pop(oHero.m_PlayerID)
        if not self.m_OccuptPlayer:
            self.UpdateEffectState(1001)
            return None

    
    def TryDone(self):
        self.UpdateProcess()
        if not self.m_IsDone:
            SendAlert('err', '占点寻宝进度异常 %d' % self.m_Process)
            self.Done()

    
    def Done(self):
        self.ClearRoundMonster()
        self.ClearOccupyingMsg()
        oChallenge = self.m_Challenge
        self.DoneHint(oChallenge)
        self.Remove('DoneSearch')
        self.m_IsDone = 1
        oChallenge.DoneSearch(self.m_Index)

    
    def DoneHint(self, oChallenge):
        if oChallenge.m_SearchNum + 1 == oChallenge.m_ExpectSearchNum:
            self.m_IsReal = 1
            cl_notify.SendCommonNotify(self.m_Game, self.m_OccuptPlayer, 9394, { })
            dPlayer = self.m_Challenge.GetScenePlayers()
            dOtherPlayer = { }
            for pid in dPlayer:
                if pid not in self.m_OccuptPlayer:
                    dOtherPlayer[pid] = 1
            
            if not dOtherPlayer:
                return None
            cl_notify.SendCommonNotify(self.m_Game, dOtherPlayer, 9393, { })
        else:
            cl_notify.SendCommonNotify(self.m_Game, self.m_OccuptPlayer, 9383, { })

    
    def ClearRoundMonster(self):
        dMask = {
            'Mask': PXMASK_MONSTER,
            'BlockMask': 0 }
        iRange = self.m_Challenge.m_ActualRadius + 2
        lstArgs = [
            self.m_ActualPos,
            iRange]
        lstVLST = cl_math.GetAttackTargetList(self.m_Game, self.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
        oReason = cl_object.reason.CStrReason('TreasureEventDone', None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        for iMonster in lstVLST:
            oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            if oMonster.m_FightType & WARRIOR_NORMAL != WARRIOR_NORMAL:
                continue
            oMonster.HPModifyDam(0, [
                [
                    oMonster.HP(),
                    oReason]])
        

    
    def UpdateProcess(self):
        if self.m_IsDone:
            return None
        if not self.m_OccuptPlayer:
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        iOccupyTime = Frame2Time(iNowFrame - self.m_OccuptFrame)
        iRatio = self.GetRatio()
        iNewProcess = self.m_Process + iRatio * iOccupyTime // 100
        self.m_Process = iNewProcess
        self.m_OccuptFrame = iNowFrame
        if iNewProcess >= 10000:
            self.Done()
            return None

    
    def GetRatio(self):
        return self.m_Challenge.m_SingleRatio * len(self.m_OccuptPlayer)

    
    def GetRemainTime(self):
        iProcess = self.m_Process
        iRemainProcess = max(10000 - iProcess, 0)
        iRatio = self.GetRatio()
        iRemainTime = math.ceil(iRemainProcess * 100 / iRatio)
        return iRemainTime

    
    def GetTotalTime(self, iRemainTime):
        iProcess = self.m_Process
        iRemainProcess = 10000 - iProcess
        iTotalTime = 10000 * iRemainTime // iRemainProcess
        return iTotalTime

    
    def SendOccupyingMsg(self, iRemainTime, iTotalTime):
        dReplace = {
            '$remain': str(iRemainTime),
            '$total': str(iTotalTime) }
        sMsg = cl_notify.GetCommonNotifyMsg(self.m_Occupying)
        cl_notify.SendCommonNotifyNoTransfer(self.m_Game, self.m_OccuptPlayer, iRemainTime, sMsg, dReplace)

    
    def ClearOccupyingMsg(self):
        sMsg = cl_notify.GetCommonNotifyMsg(self.m_Occupying)
        cl_notify.SendCommonNotifyNoTransfer(self.m_Game, self.m_OccuptPlayer, 0, sMsg, { })

    
    def UpdateEffectState(self, iConfig):
        dPlayer = self.m_Challenge.GetScenePlayers()
        cl_snetwar.GS2CTriggerAnimator(self.m_Game, dPlayer, self.m_ActualEffectID, iConfig)

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        dPlayer = self.m_Challenge.GetScenePlayers()
        if dPlayer:
            self.UpdateSceneIcon(SCENEICON_OPER_HIDE)
            self.ClearOccupyingMsg()
            iConfig = 1004
            if self.m_IsReal:
                iConfig = 1003
            self.UpdateEffectState(iConfig)
            self.m_Challenge.UpdateMiniMapPos(MINIMAPPT_OPER_HIDE, self.m_MiniMapPosInfo.values(), dPlayer)
        if self.m_Trigger:
            self.m_Trigger.Unstall()
        self.m_Trigger = None
        self.m_Challenge = None
        self.m_OccuptPlayer = { }
        super(TreasureEvent, self).Release()



class OccupyEvent(TreasureEvent):
    m_Occupying = 9399
    
    def DoneHint(self, oChallenge):
        if cllib.lib_flag.g_IsMobile:
            return None
        cl_notify.SendCommonNotify(self.m_Game, self.m_Challenge.GetScenePlayers(), 9443, { })

    
    def Done(self):
        self.ClearRoundMonster()
        self.ClearOccupyingMsg()
        oChallenge = self.m_Challenge
        self.DoneHint(oChallenge)
        self.m_IsReal = 1
        self.Remove('DoneOccupy')
        self.m_IsDone = 1
        oChallenge.DoneOccupy(self.m_Index)

    
    def ChangeOccupyState(self, oHero, iLeave):
        super().ChangeOccupyState(oHero, iLeave)
        self.OccupyProcessTrigger()

    
    def GetProcessRemainTime(self, iProcess):
        self.UpdateProcess()
        iRemainProcess = max(iProcess - self.m_Process, 0)
        if not iRemainProcess:
            return 0
        iRatio = self.GetRatio()
        iRemainTime = iRemainProcess * 100 // iRatio
        return iRemainTime

    
    def GetRatio(self):
        if not self.m_OccuptPlayer:
            return 0
        return cl_formula.GetFormulaResult(self, self.m_Challenge.m_Ratio)

    
    def TimeCallback(self, cbFun):
        cbFun()
        self.OccupyProcessTrigger()

    
    def OccupyProcessTrigger(self):
        if not self.m_Challenge:
            return None
        iProcess = self.m_Challenge.GetFirstCbProcess()
        if iProcess:
            sFlag = 'CbProcess_%s_%s' % (iProcess, self.m_ID)
            self.Remove_Call_Out(sFlag)
            if self.m_OccuptPlayer:
                iRemainTime = self.GetProcessRemainTime(iProcess)
                cbFun = self.m_Challenge.m_ProcessCbFun[iProcess]
                self.Call_Out(Functor(self.TimeCallback, cbFun), Time2Frame(iRemainTime) + 1, sFlag)

    
    def GetCurProcess(self):
        if self.m_IsDone:
            return 10000
        if not self.m_OccuptPlayer:
            return self.m_Process
        iNowFrame = self.m_Game.GetFrameNum()
        iOccupyTime = Frame2Time(iNowFrame - self.m_OccuptFrame)
        iRatio = self.GetRatio()
        iNewProcess = self.m_Process + iRatio * iOccupyTime // 100
        return iNewProcess

    
    def Release(self):
        for iProcess in self.m_Challenge.m_ProcessCbFun:
            sFlag = 'CbProcess_%s_%s' % (iProcess, self.m_ID)
            self.Remove_Call_Out(sFlag)
        
        super(OccupyEvent, self).Release()



def NewTreasureEvent(oGame):
    iID = oGame.NewNPCID()
    oTreasureEvent = TreasureEvent(oGame, iID)
    return oTreasureEvent


def NewOccupyEvent(oGame):
    iID = oGame.NewNPCID()
    oOccupyEvent = OccupyEvent(oGame, iID)
    return oOccupyEvent


def TestExpectSearchNum(oGame, dPlayer, iExpectSearchNum, iExpect, iSigma, iMax):
    sKey = 'SearchTreasureChallenge'
    dExpect = { }
    iCycly = 10000
    oRandomMgr = oGame.m_RandomMgr
    for _ in range(iCycly):
        iRandom = oRandomMgr.ChooseKey(sKey, {
            'Expect': iExpect,
            'Sigma': iSigma })
        iRandom = round(iRandom / 100)
        if iRandom < 1:
            iRandom = 1
        if iRandom > iMax:
            iRandom = iMax
        iNewCnt = dExpect.get(iRandom, 0) + 1
        dExpect[iRandom] = iNewCnt
    
    sText = f'''探索第{iExpectSearchNum}次找到大宝藏\n'''
    sText += f'''期望值:{iExpect / 100},标准差:{iSigma / 300},随机次数{iCycly}\n'''
    for idx in sorted(dExpect):
        fProb = dExpect[idx] / 100
        sText += f'''第{idx}次找到大宝藏,概率{fProb}%\n'''
    
    for pid in dPlayer:
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            cl_notify.GS2CMessage(oHero, sText)
    


class CGoldenEliteChallenge(CBaseChallenge):
    m_Type = PHASE_CHALLENGE_GOLDENELITE
    m_ChallengeName = '黄金精英怪挑战'
    m_EliteMonster = 0
    m_InitNormalTime = 500
    m_CreateFrame = 0
    m_KillTarget = False
    m_BulletPerformSID = 12014
    
    def Init(self, clsData, dAddData):
        super(CGoldenEliteChallenge, self).Init(clsData, dAddData)
        self.m_EliteMonsterSID = clsData.m_Param[0]
        self.m_EliteMinDistance = clsData.m_Param[1]
        self.m_EliteMaxDistance = clsData.m_Param[2]
        self.m_NormalMonsterSID = clsData.m_Param[3]
        self.m_NormalMinDistance = clsData.m_Param[4]
        self.m_NormalMaxDistance = clsData.m_Param[5]
        self.m_ReflashCD = cl_formula.GetFormulaResult(self, clsData.m_Param[6])
        self.m_NotifyDie = clsData.m_Param[7]
        self.m_HPRatio = clsData.m_Param[8]
        self.m_NotifyUp = clsData.m_Param[9]
        self.m_NotifyDown = clsData.m_Param[10]
        self.m_HintInnerRadius = clsData.m_Param[11]
        self.m_HintRadius = clsData.m_Param[12]
        self.m_NormalMonsters = { }
        self.m_BulletList = { }
        self.m_EliteMonsterPos = self.ChooseEliteMonsterPos()
        self.m_MiniMapPos = self.ChooseMiniMapPos()
        self.m_MiniMapPosInfo = self.CreateMiniMapPosInfo(MINIMAPPT_TYPE_GOALDENELITEMONSTERPOS, MINIMAPPT_SHOW_HIGHLIGHT, [
            self.m_MiniMapPos])
        self.UpdateMiniMapPos(MINIMAPPT_OPER_SHOW, self.m_MiniMapPosInfo.values(), self.GetScenePlayers())

    
    def Release(self):
        self.ClearAttention()
        self.m_NormalMonsters = { }
        self.m_BulletList = { }
        super().Release()

    
    def OnStartChallenge(self):
        self.UpdateMiniMapPos(MINIMAPPT_OPER_HIDE, self.m_MiniMapPosInfo.values(), self.GetScenePlayers())
        self.m_EliteMonster = self.CreateEliteMonster()
        self.m_ChallengeMgr.m_Survivor.Call_Out(self.CreateNormalMonster, Time2Frame(self.m_InitNormalTime), self.m_Key + 'CreateNormalMonster')
        oEliteMonster = self.m_Game.GetObject(self.m_EliteMonster)
        oGame = self.m_Game
        lstRoomHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstRoomHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oHero.AddPerform(self.m_BulletPerformSID, 1)
        
        if oEliteMonster:
            cl_msgcenter.AddFunction(oEliteMonster, cl_msgcenter.MSG_WAR_DIE, self.OnEliteMonsterDie, self.m_Key + 'EliteMonsterDie')

    
    def ClearAttention(self):
        self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'CreateNormalMonster')
        oGame = self.m_Game
        oEliteMonster = oGame.GetObject(self.m_EliteMonster)
        if oEliteMonster:
            cl_msgcenter.DoneEvent(oEliteMonster, cl_msgcenter.MSG_WAR_DIE, self.m_Key + 'EliteMonsterDie')
        for iNormalMonster in self.m_NormalMonsters.values():
            oNormalMonster = oGame.GetObject(iNormalMonster)
            if oNormalMonster:
                cl_msgcenter.DoneEvent(oNormalMonster, cl_msgcenter.MSG_WAR_DIE, self.m_Key + '%s-%sNormalMonsterDie' % (self.m_Key, oNormalMonster.m_ID))
        

    
    def ChooseNormalMonsterPos(self, lstNeedAdd):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        tMonsterRange = (self.m_NormalMinDistance, self.m_NormalMaxDistance, self.m_EliteMaxDistance)
        dPos = { }
        oGame = self.m_Game
        for iHero in lstNeedAdd:
            oHero = oGame.GetObject(iHero)
            if oHero:
                tSpawnPos = oSurvivor.m_CurLine.m_MonsterCtrl.GetMeetDistancePos(oHero, tMonsterRange)
                if tSpawnPos:
                    tNormalMonster = self.ChooseSinglePos(dPos, tSpawnPos)
            dPos[oHero.m_ID] = tNormalMonster if tNormalMonster else tSpawnPos[0]
        
        return dPos

    
    def ChooseSinglePos(self, dCurPos, tPosInfo):
        for lstTemp in tPosInfo:
            for tPos in lstTemp:
                if tPos in dCurPos.values():
                    continue
                return tPos
            
        

    
    def ChooseEliteMonsterPos(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dElitePosInfo = oLevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'monsterelitepos')
        vEliteMonsterPos = None
        oGame = self.m_Game
        oTarget = oSurvivor.GetMaxDamageTarget()
        lstDistance = []
        if oTarget:
            vTarget = oTarget.GetPos()
            lstBestDistance = []
            for dPos in dElitePosInfo.values():
                fHighLimit = dPos['HighLimit'] if 'HighLimit' in dPos else 0
                vPos = dPos['Center']
                fDistance = cl_math.CalDistance(vTarget, vPos)
                if fDistance > self.m_EliteMaxDistance:
                    continue
                if fDistance >= self.m_EliteMinDistance:
                    if fHighLimit > 1e-06 and abs(vTarget[1] - vPos[1]) > fHighLimit:
                        continue
                    lstBestDistance.append(vPos)
                    continue
                lstDistance.append((fDistance, vPos))
            
            if lstBestDistance:
                idx = oGame.Random(len(lstBestDistance))
                vEliteMonsterPos = lstBestDistance[idx]
        if not vEliteMonsterPos:
            if lstDistance:
                lstDistance.sort()
                vEliteMonsterPos = lstDistance[-1][1]
            else:
                lstMonsterInfo = list(dElitePosInfo.values())
                idx = oGame.Random(len(lstMonsterInfo))
                vEliteMonsterPos = lstMonsterInfo[idx]['Center']
        return vEliteMonsterPos

    
    def CreateNormalMonster(self):
        self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'CreateNormalMonster')
        oGame = self.m_Game
        self.m_CreateFrame = oGame.GetFrameNum()
        lstLiveHero = oGame.m_WarMgr.GetLiveHero()
        dNormalMonsters = self.m_NormalMonsters
        if len(dNormalMonsters) >= len(lstLiveHero):
            self.m_ChallengeMgr.m_Survivor.Call_Out(self.CreateNormalMonster, Time2Frame(self.m_ReflashCD), self.m_Key + 'CreateNormalMonster')
            return None
        if dNormalMonsters:
            lstNeedAdd = []
            for iHero in lstLiveHero:
                if iHero not in dNormalMonsters:
                    lstNeedAdd.append(iHero)
            
            dMonsterPos = self.ChooseNormalMonsterPos(lstNeedAdd)
        else:
            dMonsterPos = self.ChooseNormalMonsterPos(lstLiveHero)
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iGrade = dPhaseInfo[oSurvivor.m_Phase]['Grade']
        for iHero, vMonsterPos in dMonsterPos.items():
            oMonster = oSurvivor.m_CurLine.m_MonsterCtrl.CreateMonster(self.m_NormalMonsterSID, iGrade, vMonsterPos)
            if oMonster:
                cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_DIE, self.OnNormalMonsterDie, '%s-%sNormalMonsterDie' % (self.m_Key, oMonster.m_ID))
                self.m_NormalMonsters[iHero] = oMonster.m_ID
                self.OnCreateMonsters([
                    oMonster.m_ID])
        
        self.m_ChallengeMgr.m_Survivor.Call_Out(self.CreateNormalMonster, Time2Frame(self.m_ReflashCD), self.m_Key + 'CreateNormalMonster')

    
    def CreateEliteMonster(self):
        oSurvivor = self.m_ChallengeMgr.m_Survivor
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iGrade = dPhaseInfo[oSurvivor.m_Phase]['Grade']
        vMonsterPos = (self.m_EliteMonsterPos, (0, 0, 0), [], ({ }, None), 0)
        oMonster = oSurvivor.m_CurLine.m_MonsterCtrl.CreateMonster(self.m_EliteMonsterSID, iGrade, vMonsterPos)
        if not oMonster:
            return 0
        self.OnCreateMonsters([
            oMonster.m_ID])
        return oMonster.m_ID

    
    def OnNormalMonsterDie(self, oTarget, dMsgInfo):
        if oTarget.m_ID not in self.m_NormalMonsters.values() or self.m_KillTarget:
            return None
        oGame = self.m_Game
        iCostTime = Frame2Time(oGame.GetFrameNum() - self.m_CreateFrame)
        if iCostTime < self.m_InitNormalTime:
            self.m_ChallengeMgr.m_Survivor.Remove_Call_Out(self.m_Key + 'CreateNormalMonster')
            self.m_ChallengeMgr.m_Survivor.Call_Out(self.CreateNormalMonster, Time2Frame(self.m_InitNormalTime - iCostTime), self.m_Key + 'CreateNormalMonster')
        oBullet = oGame.m_ResMgr.CreateDrop(self.m_LevelNode.m_Scene, NWARRIOR_DROP_ENCHANTING_BULLET, oTarget.GetPos(), [
            {
                self.m_BulletPerformSID: 1 }], { })
        self.m_BulletList[oBullet.m_ID] = 1
        iRemoveHero = 0
        for iHero in self.m_NormalMonsters.keys():
            if self.m_NormalMonsters[iHero] == oTarget.m_ID:
                iRemoveHero = iHero
        
        self.m_NormalMonsters.pop(iRemoveHero, None)

    
    def OnEliteMonsterDie(self, oTarget, dMsgInfo):
        if oTarget.m_ID != self.m_EliteMonster or self.m_KillTarget:
            return None
        self.OverChallenge({ })

    
    def CheckChallengeStatus(self):
        if self.m_Status == CHASTATUS_OVER:
            return self.m_Status
        oTarget = self.m_Game.GetObject(self.m_EliteMonster)
        if not oTarget or oTarget.m_HP == 0:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnOverChallenge(self, dParam):
        dPlayer = self.GetScenePlayers()
        oGame = self.m_Game
        oEliteMonster = oGame.GetObject(self.m_EliteMonster)
        for iBullet in self.m_BulletList:
            oBullet = oGame.GetObject(iBullet)
            if oBullet:
                oBullet.Remove('GameOver')
        
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_RewardType = CHALLENGE_SUCCESS
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyDie), { })
        elif self.GetEliteMonsterHPRatio(oEliteMonster) > self.m_HPRatio:
            self.m_RewardType = CHALLENGE_FAIL
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyUp), { })
        else:
            self.m_RewardType = CHALLENGE_GOAL_TARGET
            self.ChallengeNotify(dPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_NotifyDown), { })
        oReason = cl_object.reason.CStrReason('EliteChallengeDone', None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        if oEliteMonster:
            self.m_KillTarget = True
            oEliteMonster.HPModifyDam(oEliteMonster.m_ID, [
                [
                    oEliteMonster.HP(),
                    oReason]])
        if self.m_NormalMonsters:
            for iNormalMonster in self.m_NormalMonsters.values():
                oNormalMonster = oGame.GetObject(iNormalMonster)
                if oNormalMonster:
                    oNormalMonster.HPModifyDam(oNormalMonster.m_ID, [
                        [
                            oNormalMonster.HP(),
                            oReason]])
            

    
    def GetEliteMonsterHPRatio(self, oTarget):
        return oTarget.m_HP * 100 // oTarget.QueryAttr('HPMax')

    
    def ChooseMiniMapPos(self):
        for _ in range(10):
            vPos = self.m_Game.Scene_RandomPointSectorInMesh(self.m_LevelNode.m_Scene, self.m_EliteMonsterPos, (1, 0, 0), self.m_HintInnerRadius, self.m_HintRadius, 1, 179)
            if vPos:
                return vPos
        
        return self.m_EliteMonsterPos


