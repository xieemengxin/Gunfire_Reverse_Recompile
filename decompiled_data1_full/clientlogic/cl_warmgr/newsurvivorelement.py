# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/newsurvivorelement.pyc
# RelativePath: clientlogic/cl_warmgr/newsurvivorelement.pyc
# Source Generated with Decompyle++
# File: newsurvivorelement.pyc (Python 3.6)

from cl_only import ShufferList, SendAlert, ChooseKey, Functor, Time2Frame, Frame2Time, PY_FLAG_DEAD, DeepCopy, RoundDivide, GAME_FRAME
from cl_warmgr.mobject import CBaseElement
from cl_commondefines import SURVIVOR_PLAY, LEVEL_TYPE_FIGHT, DAM_TYPE_TRUE, DAM_USE_HP, STATE_UNDER_ATTACK, NWARRIOR_NPC_RAREGOLDENCUP, NPCMGR_SURVIVOR, LEVEL_STATE_PREPARE, LEVEL_STATE_FIGHT, LEVEL_STATE_FINISH, VOTE_TYPE_SURVIVOR, LEVEL_TYPE_BOSS
from cl_commondefines import STATE_NODIE, STATE_TIME_LIMIT, TYPE_RELIFE_RESTPHASE, STATE_TIME_FOREVER, WARRIOR_MONSTER, NWARRIOR_DROP_CASH, CBEHAVIOR_GLOBALAUTOPICK
from cl_object.logging import SurvivorLog
from cl_warmgr.levelline import survivorspawnaction
from cl_warmgr.survivor import survivorrewardmgr
from cl_warmgr.survivor import npcrefreshmgr
from cl_warmgr.survivor import survivorbornctrl
from cl_warmgr.survivor import survivorrareitemmgr
from cl_warmgr.levelline.mainlevelnode import OnMonsterDie
from cl_warmgr.survivor import survivormonstersupermgr
from cl_npc.net import GS2CVoteStat
from cl_warmgr.bigdataanalyse import CNewSurvivorCom
from cl_platformdata import GetCommonNotify
import cl_object
import cl_msgcenter
import cl_state
import cl_formula
import cl_random
import cl_notify
import cl_phasechallenge
import cl_snetwar
NOTIFY_REST = 17146
NOTIFY_FIGHT = 17147
NOTIFY_PAUSE = 17156
NOTIFY_REMAINCNT = 17166
NOTIFY_FINISH_2 = 17164
NOTIFY_FINISH_1 = 17163
GROUPNUM = 50

class CNewSurvivorElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CNewSurvivorElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'NewSurvivorElement'
        self.m_PhaseConfig = oData.m_PhaseConfig
        self.m_LevelMap = oData.m_LevelMap
        self.m_NpcConfigMap = oData.m_NpcConfigMap
        self.m_DropSurvivalTime = oData.m_DropSurvivalTime
        self.m_RefreshAreaPhase = oData.m_Config.get('REFRESHAREA', [])
        self.m_RareTalentInfo = oData.m_Config.get('m_RareTalentInfo', { })
        self.m_HeroRareCupRefresh = { }
        self.m_InscriptionConfig = oData.m_Config.get('InscriptionConfig', { })
        self.m_InitEquipInfo = oData.m_Config.get('InitEquipInfo', (0, 1))
        self.m_NotifyPhase = oData.m_Config.get('NotifyPhase', [])
        self.m_RemainNotifyCnt = oData.m_Config.get('RemainNotifyCnt', 0)
        self.m_PhaseData = { }
        self.m_CurSpawn = -1
        self.m_Phase = 0
        self.m_RestFlag = 0
        self.m_MaxPhase = 0
        self.m_PhaseReward = []
        self.m_PhaseStartFrame = 0
        self.m_Pause = 0
        self.m_PauseStartFrame = 0
        self.m_PauseTotalFrame = 0
        self.m_RestPhaseStartFrame = 0
        self.m_CurLine = None
        self.m_LevelState = 0
        self.m_SuspendableCallOut = { }
        self.m_CallCout = { }
        self.m_CallCoutRemoveFlag = { }
        self.m_CanPause = True
        self.m_Pause = False
        self.m_RestNodieState = { }
        self.m_ExecFunc = []
        self.m_ElitePhaseNotify = []
        self.m_RewardMgr = survivorrewardmgr.NewSurvivorRewardMgr(self, oData)
        self.m_NpcRefreshMgr = npcrefreshmgr.NewNpcRefreshMgr(self, oData, NPCMGR_SURVIVOR)
        self.m_BornCtrl = survivorbornctrl.NewSurvivorBornManager(self, oData)
        self.m_SuperMonsterMgr = survivormonstersupermgr.NewSurvivorMonsterSuperMgr(self, oData, iNew = 1)
        self.m_PhaseChallengeMgr = cl_phasechallenge.NewPhaseChallengeMgr(self, iNew = 1)
        self.m_RareItemMgr = survivorrareitemmgr.NewSurvivorRareItemMgr(self, oData)

    
    def Init(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oWarMgr.Set('AdditionalGemini', self.m_InscriptionConfig.get('AdditionalGemini', 0))
        oWarMgr.Set('ExclusiveInscription', self.m_InscriptionConfig.get('ExclusiveInscription', 0))
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, self.m_CallFlag)
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.OnWeaponGrade, self.m_CallFlag)
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMSG_INSCRIPTIONNUM, self.OnInscriptionNum, self.m_CallFlag)
        oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnWarriorDie, self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WAR_DROP, self.OnDrop, self.m_CallFlag, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnWarRemovePlayer, self.m_CallFlag)

    
    def InitAfter(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.OnLevelCtrlInit, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WAR_DROP, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.m_CallFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.m_CallFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMSG_INSCRIPTIONNUM, self.m_CallFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        oGame.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag + 'GroupWeaponDrop')
        self.m_RewardMgr.Release()
        self.m_NpcRefreshMgr.Release()
        self.m_BornCtrl.Release()
        self.m_SuperMonsterMgr.Release()
        self.m_PhaseChallengeMgr.Release()
        self.m_RareItemMgr.Release()
        self.m_RewardMgr = None
        self.m_NpcRefreshMgr = None
        self.m_BornCtrl = None
        self.m_SuperMonsterMgr = None
        self.m_PhaseChallengeMgr = None
        self.m_CurLine = None
        self.m_RareItemMgr = None
        self.m_PhaseData = { }
        self.m_SuspendableCallOut = { }
        self.m_CallCout = { }
        self.m_CallCoutRemoveFlag = { }
        self.m_ExecFunc = []
        self.m_RestNodieState = { }

    
    def OnAddAllPlayer(self, oTarget, oWarMgr, dInfo):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, self.m_CallFlag)
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnHeroRelife, self.m_CallFlag)
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_CallFlag)
        
        oBigdataMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CNewSurvivorCom(self.m_Game)
            oBigdataMgr.SetCom('NewSurvivor', oAnalyseCom)

    
    def OnWarRemovePlayer(self, oTarget, oWarMgr, dInfo):
        oWarMgr.RefreshPlayerCnt()
        if not self.m_Phase:
            return None
        self.CheckAllDiePause()

    
    def OnLevelNodeInit(self, oTarget, oWarMgr, dInfo):
        if dInfo['LevelType'] == LEVEL_TYPE_FIGHT:
            iLevel = dInfo['LevelID']
            oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
            self.m_CurLine = oLevelCtrl.m_CurNode.m_RoomList[0][0]
            oLevelCtrl.m_CurNode.LockRoom(0, 'survivor')
            self.m_ConfigSID = self.m_LevelMap[iLevel]
            self.m_PhaseData = self.m_PhaseConfig[self.m_ConfigSID]
            self.m_MaxPhase = len(self.m_PhaseData)
            self.m_NpcRefreshMgr.InitNpcPos()
            self.m_BornCtrl.InitHeroBorn()
            self.m_NpcRefreshMgr.m_SID = self.m_NpcConfigMap[self.m_ConfigSID]
        else:
            self.m_RestFlag = 0
            self.RemoveNodieState()
            self.m_BornCtrl.m_HeroBorn = []
            self.Remove_Call_Out('FinishNotify-%s' % self.m_CallFlag)
        self.m_LevelState = LEVEL_STATE_PREPARE

    
    def Save(self):
        dData = { }
        dData['PR'] = self.m_RewardMgr.Save()
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_RewardMgr.Load(dData['PR'])

    
    def Start(self, *args):
        self.m_LevelState = LEVEL_STATE_FIGHT
        self.AddPhase(1)
        self.m_RewardMgr.InitWeaponCountDown()

    
    def PhaseReward(self, *args):
        lstReward = self.m_PhaseReward
        self.m_PhaseReward = []
        for dAction in lstReward:
            func = dAction['func']
            if isinstance(func, int):
                func = survivorspawnaction.GetSpawnFunc(func)
            tParam = dAction['param']
            func(self, tParam, *args)
        

    
    def PreAddPhase(self, dExtraInfo = None):
        dInfo = {
            'Phase': self.m_Phase }
        if dExtraInfo:
            dInfo.update(dExtraInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_RESTPHASE, self, dInfo)
        self.ClearPhaseData()
        self.SceneMonsterAllDie()
        if self.m_Phase not in self.m_PhaseData:
            return None
        iRestTime = cl_formula.GetFormulaResult(self, self.m_PhaseData[self.m_Phase]['RestTime'])
        oGame = self.m_Game
        dPlayer = oGame.GetRealPlayers()
        self.m_RestPhaseStartFrame = oGame.GetFrameNum()
        self.m_RestFlag = 1
        self.RelifeHero()
        self.TriggerAutoPickCash()
        if iRestTime:
            cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 1)
            cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_FIGHT)
            cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_REMAINCNT)
            cl_notify.SendCommonNotify(oGame, dPlayer, NOTIFY_REST, {
                '$time': str(iRestTime) }, iTime = iRestTime)
            func = Functor(self.AddPhase, 1)
            sCallFlag = 'PreAddPhase' + self.m_CallFlag
            self.Remove_Call_Out_Suspendable(sCallFlag)
            iRestFrame = Time2Frame(iRestTime)
            self.Call_Out_Suspendable(func, iRestFrame, sCallFlag)
            self.m_NpcRefreshMgr.TryNpcRefresh(1)
            self.AddRestNodieState(iRestFrame)
            self.StartPrepareVote()
        elif self.m_Phase == self.m_MaxPhase:
            cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 1)
            cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_FIGHT)
            self.m_NpcRefreshMgr.TryNpcRefresh(1)
            cl_snetwar.GS2CPrepareTimeInfo(dPlayer, -1, -1)
            self.AddRestNodieState(0)
            self.AddPhase(1)
        else:
            self.AddPhase(1)

    
    def AddPhase(self, iPhase):
        if self.m_Phase >= self.m_MaxPhase:
            self.FinishSurvivor()
            return None
        self.m_Phase += iPhase
        self.m_RestFlag = 0
        oGame = self.m_Game
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_PHASESTART, self, {
            'Phase': self.m_Phase })
        SurvivorLog.Debug('game:%d addphase:%d curspawn:%d %d' % (oGame.m_ID, self.m_Phase, self.m_CurSpawn, oGame.GetFrameNum()))
        self.StopPrepareVote()
        dPlayer = oGame.GetRealPlayers()
        cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_REST)
        self.RemoveNodieState()
        self.m_NpcRefreshMgr.RemoveNpcOnFight()
        cl_snetwar.GS2CPhaseInfo(dPlayer, self.m_Phase, iIsFinish = 0)
        self.m_NpcRefreshMgr.TryRemoveEventNpc()
        self.m_NpcRefreshMgr.TryNpcRefresh(0)
        self.m_PhaseStartFrame = oGame.GetFrameNum()
        self.PhaseFightTime()
        self.SpawnInit()

    
    def ClearPhaseData(self):
        self.ClearCallOut()
        self.m_CurLine.m_MonsterCtrl.ClearSpawnData()
        self.ClearTrigger()

    
    def ClearTrigger(self):
        oLevelNode = self.m_CurLine.m_LevelNode
        lstLineIdx = []
        for lstLine in oLevelNode.m_RoomList:
            for oLine in lstLine:
                lstLineIdx.append(oLine.GetLineIdx())
            
        
        oLevelNode.m_CtrlMgr.m_LevelTrigger.ClearLevel(oLevelNode.m_Scene, lstLineIdx)

    
    def ValidSetInfo(self, oNpc, oHero):
        if not oNpc:
            return False
        if oNpc.m_FightType != NWARRIOR_NPC_RAREGOLDENCUP:
            return False
        if oNpc.GetMaxRefreshTimes(oHero):
            return False
        return True

    
    def OnInteract(self, oSurvivor, oTarget, dInfo):
        iNpc = dInfo['NPC']
        oGame = self.m_Game
        oNpc = oGame.GetObject(iNpc)
        oHero = oGame.GetObject(dInfo['Hero'])
        if self.ValidSetInfo(oNpc, oHero):
            oNpc.SetRefreshCost(self.m_RareTalentInfo['RefreshCost'])
            oNpc.SetMaxRefreshTimes(self.m_RareTalentInfo['RefreshMaxTimes'], dInfo['Hero'])

    
    def FinishSurvivor(self):
        self.m_CanPause = False
        self.m_LevelState = LEVEL_STATE_FINISH
        self.InitGoalPos()
        self.m_CurLine.m_LevelNode.LevelGoal({ })
        self.ClearCallOut()
        self.FinishNotify()

    
    def InitGoalPos(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iLevel = oLevelCtrl.m_CurNode.m_Level
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        oMiniMap.m_LevelGoalPos.Init()

    
    def FinishNotify(self):
        oGame = self.m_Game
        dPlayer = oGame.GetRealPlayers()
        tResult = GetCommonNotify(NOTIFY_FINISH_1)
        if not tResult:
            return None
        (_, iTime) = tResult
        cl_notify.SendCommonNotify(oGame, dPlayer, NOTIFY_FINISH_1, { })
        self.Call_Out(self.FinishNotify2, Time2Frame(iTime), 'FinishNotify-%s' % self.m_CallFlag)

    
    def FinishNotify2(self):
        oGame = self.m_Game
        dPlayer = oGame.GetRealPlayers()
        cl_notify.SendCommonNotify(oGame, dPlayer, NOTIFY_FINISH_2, { })

    
    def ClearCallOut(self):
        self.Remove_Call_Out_Suspendable('PhaseFightTime')

    
    def PhaseFightTime(self):
        self.m_PauseTotalFrame = 0
        sCallFlag = 'PhaseFightTime'
        self.Remove_Call_Out_Suspendable(sCallFlag)
        iFightTime = self.m_PhaseData[self.m_Phase]['FightTime']
        if iFightTime:
            oGame = self.m_Game
            cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), NOTIFY_FIGHT, {
                '$time': str(iFightTime) }, iTime = iFightTime)
            self.Call_Out_Suspendable(self.PreAddPhase, Time2Frame(iFightTime), sCallFlag)

    
    def IsPreKillAllMonster(self):
        iFrame = self.m_Game.GetFrameNum() - self.m_PhaseStartFrame - self.m_PauseTotalFrame
        iFightFrame = Time2Frame(self.m_PhaseData[self.m_Phase]['FightTime'])
        if iFrame < iFightFrame:
            return 1
        return 0

    
    def OnLevelCtrlInit(self, oTarget, oLevelCtrl, dMsgInfo):
        dExtraInfo = self.m_Game.m_WarMgr.m_ExtraInfo
        iLayerNum = 1
        iLevelNum = 1
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

    
    def SpawnInit(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        lstSpwanInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_CurLine.m_Name, 'SurvivorSpawn')
        dSpawnAreaInfo = lstSpwanInfo[self.m_Phase]
        iGMCurSpawn = oGame.m_WarMgr.Query('GMCurSpawn', 0)
        if iGMCurSpawn:
            self.m_CurSpawn = iGMCurSpawn
            oGame.m_WarMgr.Set('GMCurSpawn', 0)
        elif self.m_Phase in self.m_RefreshAreaPhase:
            dArea = dict.fromkeys(dSpawnAreaInfo, 10)
            if not dArea:
                SendAlert('err', 'game:%d 当前阶段%d没有刷怪区域可用了 %s %s' % (self.m_Game.m_ID, self.m_Phase, self.m_CurSpawn, list(dSpawnAreaInfo.keys())))
                self.PreAddPhase()
                return None
            iSpawnArea = ChooseKey(oGame, dArea)
            self.m_CurSpawn = iSpawnArea
        if self.m_CurSpawn not in dSpawnAreaInfo:
            dArea = dict.fromkeys(dSpawnAreaInfo, 10)
            self.m_CurSpawn = ChooseKey(oGame, dArea)
            SendAlert('err', 'game:%d 当前阶段%d 不存在刷怪区域%s %s' % (self.m_Game.m_ID, self.m_Phase, self.m_CurSpawn, list(dSpawnAreaInfo.keys())))
        lstSpawnRule = dSpawnAreaInfo[self.m_CurSpawn]['SpawnRule']
        for dSpawn in lstSpawnRule:
            tAction = dSpawn['Action']
            for dAction in tAction:
                func = GetSpawnFunc(dAction['type'])
                if not func:
                    continue
                func(self, dAction)
            
        
        self.ChooseMonsterDrop()
        self.m_CurLine.m_MonsterCtrl.SpawnMonster()

    
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
            self.Call_Out(self.SuspendableCallBack, iDelay, 'newsurvivor%d' % iCallFrame)

    
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
        SurvivorLog.Debug('game:%d newcallout %s %s' % (self.m_Game.m_ID, self.m_CallCout, iCurFrame))

    
    def RestoreCallOut(self, dAllCallOut):
        self.m_SuspendableCallOut = { }
        iCurFrame = self.m_Game.GetFrameNum()
        SurvivorLog.Debug('game:%d newrestorecallout %s %s' % (self.m_Game.m_ID, dAllCallOut, iCurFrame))
        for iFrame, dCall in dAllCallOut.items():
            iCallFrame = iCurFrame + iFrame
            self.m_SuspendableCallOut[iCallFrame] = dCall
            if iFrame == 0:
                self.SuspendableCallBack()
                continue
            self.Call_Out(self.SuspendableCallBack, iFrame, 'newsurvivor%d' % iCallFrame)
        

    
    def Exec_Suspendable(self, func):
        if self.m_Pause:
            self.m_ExecFunc.append(func)
        else:
            func()

    
    def ExecFunc(self):
        if not self.m_ExecFunc:
            return None
        for func in self.m_ExecFunc:
            func()
        
        self.m_ExecFunc = []

    
    def SceneMonsterAllDie(self):
        oGame = self.m_Game
        oLevelNode = self.m_CurLine.m_LevelNode
        iScene = oLevelNode.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oReason = cl_object.reason.CStrReason('SurvivorGoalOK', None, {
            'DamType': DAM_TYPE_TRUE | DAM_USE_HP })
        for iMonsterSID in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonsterSID, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oMonster.m_Reward = { }
            oMonster.HPModifyDam(0, [
                [
                    oMonster.HP(),
                    oReason]])
        
        for iHero in oScene.GetHeros():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            cl_state.RemoveState(oHero, STATE_UNDER_ATTACK)
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMGOAL, oLevelNode.m_CtrlMgr, {
            'Room': 0,
            'Level': oLevelNode.m_Level,
            'oScene': oScene })

    
    def TriggerAutoPickCash(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dPlayer = oWarMgr.GetRoomPlayer()
        for iPlayer in dPlayer:
            oHero = oWarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, oHero.m_ID, CBEHAVIOR_GLOBALAUTOPICK, [
                iPlayer])
        
        self.Call_Out(self.DelayAutoPickCash, GAME_FRAME, self.m_CallFlag + 'DelayAutoPickCash')

    
    def DelayAutoPickCash(self):
        oGame = self.m_Game
        oLevelNode = self.m_CurLine.m_LevelNode
        iScene = oLevelNode.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        lstDrop = oScene.GetObjectsByType('Drop')
        lstWarCash = []
        for iDrop in lstDrop:
            oDrop = oGame.GetObject(iDrop)
            if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_CASH:
                continue
            lstWarCash.append(iDrop)
        
        self.DelayPickCash(lstWarCash)

    
    def DelayPickCash(self, lstWarCash):
        sFlag = self.m_CallFlag + 'DelayPickCash'
        self.Remove_Call_Out(sFlag)
        lstCurWarCash = lstWarCash[:GROUPNUM]
        lstRestCash = lstWarCash[GROUPNUM:]
        if lstRestCash:
            self.Call_Out(Functor(self.DelayPickCash, lstRestCash), 1, sFlag)
        oGame = self.m_Game
        for iDrop in lstCurWarCash:
            oDrop = oGame.GetObject(iDrop)
            if not oDrop:
                continue
            oHero = oGame.GetObject(oDrop.m_Owner)
            if not oHero:
                continue
            oDrop.OnPick(oHero)
        

    
    def ChooseMonsterDrop(self):
        oGame = self.m_Game
        oLevelNode = self.m_CurLine.m_LevelNode
        dLineCnt = oLevelNode.GetAllLineMonsterCnt()
        dPreNum = self.m_CurLine.m_MonsterCtrl.GetSpecialPreNum()
        for tLineIdx, iNum in dPreNum.items():
            if tLineIdx in dLineCnt:
                dLineCnt[tLineIdx] += iNum
                continue
            dLineCnt[tLineIdx] = iNum
        
        dChoose = { }
        for tLineIdx, iCnt in dLineCnt.items():
            for idx in range(iCnt):
                dChoose[(tLineIdx, idx)] = 1
            
        
        if not dChoose:
            return None
        dWeaponDrop = self.m_PhaseData[self.m_Phase]['WeaponDrop']
        (iExcept, iSigma, iMiniGame) = dWeaponDrop
        iExcept = cl_formula.GetFormulaResult(self, iExcept)
        iSigma = cl_formula.GetFormulaResult(self, iSigma)
        oRandomMgr = oGame.m_RandomMgr
        if not oRandomMgr.ValidRandom('weapondrop'):
            oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, 'weapondrop', dChoose)
        else:
            oRandomMgr.SetChoose('weapondrop', dChoose)
        dMonsterChoose = oRandomMgr.ChooseKey('weapondrop', {
            'Expect': iExcept,
            'Sigma': iSigma,
            'Game': oGame })
        if dMonsterChoose:
            SurvivorLog.Debug('game:%d monsterchoose:%s phase:%s' % (self.m_Game.m_ID, sum(dMonsterChoose.values()), self.m_Phase))
            oGame.AddGlobalAttention(oLevelNode.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, Functor(self.OnMonsterDie, { }, dMonsterChoose, iMiniGame, 'WeaponDrop'), self.m_CallFlag + 'GroupWeaponDrop')

    
    def GetInitEquipInfo(self):
        return self.m_InitEquipInfo

    
    def OnWeaponGrade(self, oSurvivor, oTarget, dInfo):
        iPhase = self.m_Phase
        if iPhase > self.m_MaxPhase:
            iPhase = self.m_MaxPhase
        if iPhase not in self.m_PhaseData:
            return None
        (iWeaponGrade, _) = self.m_PhaseData[iPhase]['WeaponArgs']
        dInfo['Grade'] = iWeaponGrade

    
    def OnInscriptionNum(self, oSurvivor, oTarget, dInfo):
        iPhase = self.m_Phase
        if iPhase > self.m_MaxPhase:
            iPhase = self.m_MaxPhase
        if iPhase not in self.m_PhaseData:
            return None
        (_, iInscriptionNum) = self.m_PhaseData[iPhase]['WeaponArgs']
        dInfo['InscriptionNum'] = iInscriptionNum

    
    def OnPlayerMapLoadOK(self, oSurvivor, oHero, dInfo):
        if self.m_Phase not in self.m_PhaseData:
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_FIGHT:
            return None
        oGame = self.m_Game
        pid = dInfo['pid']
        cl_snetwar.GS2CPhaseInfo({
            pid: 1 }, self.m_Phase, iIsFinish = self.m_RestFlag)
        iCurFrame = oGame.GetFrameNum()
        if self.m_RestFlag:
            self.m_RewardMgr.GS2CPhaseGoldenCount(oHero.m_PlayerID)
            iRestTime = cl_formula.GetFormulaResult(self, self.m_PhaseData[self.m_Phase]['RestTime'])
            dPlayer = {
                oHero.m_PlayerID: 1 }
            if iRestTime:
                iFrame = iCurFrame - self.m_RestPhaseStartFrame
                iTime = Frame2Time(iFrame)
                iTime = iRestTime - iTime
                cl_snetwar.GS2CPrepareTimeInfo(dPlayer, iTime, iRestTime)
                GS2CVoteStat(oGame, oGame.m_WarMgr.Query('VoteStatus', { }), VOTE_TYPE_SURVIVOR)
                cl_notify.SendCommonNotify(oGame, {
                    pid: 1 }, NOTIFY_REST, {
                    '$time': str(iTime) }, iTime = iTime)
            else:
                cl_snetwar.GS2CPrepareTimeInfo(dPlayer, -1, -1)
                cl_notify.SendCommonNotify(oGame, dPlayer, NOTIFY_FINISH_2, { })
        else:
            self.ResumeFightNotify({
                pid: 1 })

    
    def OnMonsterDie(self, dMonsterCnt, dMonsterChoose, iMiniGame, sKey, oWarMgr, oTarget, dInfo):
        oReason = dInfo['RS'] if 'RS' in dInfo else None
        if oReason and oReason.GetStrReason() == 'SurvivorGoalOK':
            return None
        OnMonsterDie(dMonsterCnt, dMonsterChoose, iMiniGame, sKey, oWarMgr, oTarget, dInfo)

    
    def OnHeroDie(self, oSurvivor, oHero, dInfo):
        self.CheckAllDiePause()

    
    def OnHeroRelife(self, oSurvivor, oHero, dInfo):
        if not self.m_Pause:
            return None
        self.m_Pause = False
        if self.m_CallCout:
            self.RestoreCallOut(self.m_CallCout)
            self.m_CallCout = { }
        self.ExecFunc()
        self.ResumeTime()

    
    def CheckAllDiePause(self):
        if not self.m_CanPause:
            return None
        for iHeroID in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHeroID)
            if not oHero:
                continue
            if oHero.IsDead():
                continue
        else:
            self.m_Pause = True
            self.SuspendCallOut()
            self.PauseTime()

    
    def RemoveFightNotify(self, lstPlayer):
        cl_notify.ClearCommonNotify(self.m_Game, lstPlayer, NOTIFY_FIGHT)

    
    def ResumeFightNotify(self, lstPlayer):
        if self.m_Phase in self.m_PhaseChallengeMgr.m_Challenge:
            return None
        iTime = self.GetRemainFightTime()
        if not iTime:
            self.ElitePhaseNotify(lstPlayer)
            return None
        oGame = self.m_Game
        if self.m_Pause:
            cl_notify.SendCommonNotify(oGame, lstPlayer, NOTIFY_PAUSE, {
                '$text': str(RoundDivide(iTime, 100)) })
        elif not self.TryNotifyRemainMonsterCnt():
            cl_notify.SendCommonNotify(oGame, lstPlayer, NOTIFY_FIGHT, {
                '$time': str(iTime) }, iTime = iTime)

    
    def GetRemainFightTime(self):
        iFightTime = self.m_PhaseData[self.m_Phase]['FightTime']
        if not iFightTime:
            return 0
        oGame = self.m_Game
        iFrame = oGame.GetFrameNum() - self.m_PhaseStartFrame - self.m_PauseTotalFrame
        iTime = Frame2Time(iFrame)
        iTime = iFightTime - iTime
        return iTime

    
    def PauseTime(self):
        self.m_Pause = 1
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        SurvivorLog.Debug('game:%d pausetime:%s phase:%s' % (oGame.m_ID, iCurFrame, self.m_Phase))
        self.m_PauseStartFrame = iCurFrame
        dPlayer = oGame.GetRealPlayers()
        cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_FIGHT)
        self.ResumeFightNotify(dPlayer)

    
    def ResumeTime(self):
        self.m_Pause = 0
        oGame = self.m_Game
        dPlayer = oGame.GetRealPlayers()
        iCurFrame = oGame.GetFrameNum()
        self.m_PauseTotalFrame += iCurFrame - self.m_PauseStartFrame
        SurvivorLog.Debug('game:%d resumetime:%s total:%s phase:%s' % (oGame.m_ID, iCurFrame, self.m_PauseTotalFrame, self.m_Phase))
        cl_notify.ClearCommonNotify(oGame, dPlayer, NOTIFY_PAUSE)
        self.ResumeFightNotify(dPlayer)

    
    def GetMaxDamageTarget(self):
        return self.m_CurLine.m_MonsterCtrl.GetSpawnHero()

    
    def RemovePauseCorrelation(self):
        self.m_CanPause = False
        self.Remove_Call_Out_Suspendable('PhaseFightTime')

    
    def ResumePauseCorrelation(self):
        self.m_CanPause = True

    
    def StartPrepareVote(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oWarMgr.Set('VoteStatus', { })
        dPlayer = oGame.GetRealPlayers()
        iRestTime = cl_formula.GetFormulaResult(self, self.m_PhaseData[self.m_Phase]['RestTime'])
        cl_snetwar.GS2CPrepareTimeInfo(dPlayer, iRestTime, iRestTime)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemoveVotePlayer, self.m_CallFlag, iOnce = 0)

    
    def StopPrepareVote(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)

    
    def UpdateVoteStatus(self, oHero, iStatus):
        if not self.m_RestFlag:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dStat = oWarMgr.SetDefault('VoteStatus', { })
        dStat[oHero.m_PlayerID] = iStatus
        GS2CVoteStat(oGame, dStat, VOTE_TYPE_SURVIVOR)
        lstPlayer = oGame.m_WarMgr.GetLivePlayer()
        SurvivorLog.Debug('game:%d votestatus %s %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, iStatus, dStat, lstPlayer))
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
        
        sCallFlag = 'PreAddPhase' + self.m_CallFlag
        self.Remove_Call_Out_Suspendable(sCallFlag)
        self.AddPhase(1)
        iRestTime = cl_formula.GetFormulaResult(self, self.m_PhaseData[self.m_Phase]['RestTime'])
        cl_snetwar.GS2CPrepareTimeInfo(lstPlayer, 0, iRestTime)

    
    def OnRemoveVotePlayer(self, oWarMgr, dInfo):
        pid = dInfo['pid']
        self.RemoveVotePlayer(pid)

    
    def RemoveVotePlayer(self, pid):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dStat = oWarMgr.Query('VoteStatus', { })
        dStat.pop(pid, 0)
        SurvivorLog.Debug('game:%d removevoteplayer %s %s %s' % (oGame.m_ID, pid, dStat, oWarMgr.GetLivePlayer()))
        if dStat:
            self.TrySkipRestPhase()

    
    def AddRestNodieState(self, iRestFrame):
        oGame = self.m_Game
        iTimeType = STATE_TIME_LIMIT if iRestFrame else STATE_TIME_FOREVER
        for iHero in oGame.m_WarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dArgs = {
                'AID': iHero,
                'RS': cl_object.reason.CStrReason('ReterSurviorRestTime'),
                'arg': { } }
            oState = cl_state.AddState(oHero, STATE_NODIE, iTimeType, iRestFrame, dArgs)
            if oState:
                SurvivorLog.Debug('game:%d %d addrestnodie %d %d' % (oGame.m_ID, oHero.m_PlayerID, oState.m_ID, iRestFrame))
                oState.Enable(oHero)
                self.m_RestNodieState[oHero.m_ID] = oState.m_ID
        

    
    def RemoveNodieState(self):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetAllHero():
            if iHero not in self.m_RestNodieState:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oState = oHero.m_State.GetItem(self.m_RestNodieState[iHero])
            if oState:
                SurvivorLog.Debug('game:%d %d removerestnodie %d' % (oGame.m_ID, oHero.m_PlayerID, oState.m_ID))
                oHero.m_State.RemoveItem(oState.m_ID)
        

    
    def RelifeHero(self):
        oGame = self.m_Game
        oWatch = oGame.m_WarMgr.GetComponent('WatchElement')
        oDieElement = oGame.m_WarMgr.GetComponent('PVEDieElement')
        for iHero in oGame.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dRelife = {
                'HP': max(100, oHero.QueryAttr('HPMax') // 10),
                'Shield': 0,
                'Armor': 0 }
            if oHero.IsDying() or oHero.IsDied():
                SurvivorLog.Info('game: %d pid: %d restphase relife flag %d' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_Dead))
                dReason = {
                    'AID': iHero,
                    'Type': TYPE_RELIFE_RESTPHASE }
                oHero.Relife(dReason, dRelife)
                continue
            if oHero.IsRealDied():
                SurvivorLog.Info('game: %d pid: %d restphase relife flag %d' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_Dead))
                if oWatch:
                    oWatch.RelifeWatch(oHero)
                if oDieElement:
                    oDieElement.WatcherRelife(oHero, TYPE_RELIFE_RESTPHASE, iHero, dRelife)
        

    
    def OnDrop(self, oWarMgr, dInfo):
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

    
    def OnWarriorDie(self, oSurvivor, oTarget, dInfo):
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            return None
        if self.m_ElitePhaseNotify:
            self.ElitePhaseNotify()
        else:
            self.TryNotifyRemainMonsterCnt()

    
    def TryNotifyRemainMonsterCnt(self):
        if self.m_RestFlag:
            return False
        if self.m_Phase not in self.m_NotifyPhase:
            return False
        iNotifyCnt = cl_formula.GetFormulaResult(self, self.m_RemainNotifyCnt)
        iRemainCnt = self.m_CurLine.m_MonsterCtrl.GetAllRemainCount()
        if iNotifyCnt < iRemainCnt:
            return False
        iTime = self.GetRemainFightTime()
        if not iTime:
            return False
        oGame = self.m_Game
        cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), NOTIFY_REMAINCNT, {
            '$text': str(iRemainCnt),
            '$time': str(iTime) }, iTime = iTime)
        return True

    
    def StartElitePhaseNotify(self, iChat, iDelay, iGroup):
        self.m_ElitePhaseNotify = (iChat, iGroup)
        if iDelay:
            self.Call_Out(self.ElitePhaseNotify, Time2Frame(iDelay), 'DelayElitePhaseNotify')

    
    def ElitePhaseNotify(self, lstPlayer = None):
        if not self.m_ElitePhaseNotify:
            return None
        oGame = self.m_Game
        (iChat, iGroup) = self.m_ElitePhaseNotify
        if not lstPlayer:
            lstPlayer = oGame.GetRealPlayers()
        dReplaceInfo = { }
        if iGroup:
            dReplaceInfo['$text'] = str(self.m_CurLine.m_MonsterCtrl.GetSpecialGroupRemainCount(iGroup))
        cl_notify.SendCommonNotify(oGame, lstPlayer, iChat, dReplaceInfo)

    
    def StopElitePhaseNotify(self):
        (iChat, iGroup) = self.m_ElitePhaseNotify
        self.m_ElitePhaseNotify = []
        oGame = self.m_Game
        self.Remove_Call_Out('DelayElitePhaseNotify')
        cl_notify.ClearCommonNotify(oGame, oGame.GetRealPlayers(), iChat)

    
    def GetPassPhase(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS and oLevelNode.HasGoaledCurNode():
            return self.m_MaxPhase + 1
        return self.m_Phase



def SpawnSurAreaMonster(oSurvivor, dAction):
    oSurvivor.m_CurLine.m_MonsterCtrl.AddSpawnInfo(dAction['param'])


def SpawnSurHeroPosMonster(oSurvivor, dAction):
    oSurvivor.m_CurLine.m_MonsterCtrl.AddHeroPosSpawnInfo(dAction['param'])

g_SpawnMonsterFunc = {
    'SurAreaMonster': SpawnSurAreaMonster,
    'SurHeroPosMonster': SpawnSurHeroPosMonster }

def GetSpawnFunc(sType):
    if sType in g_SpawnMonsterFunc:
        return g_SpawnMonsterFunc[sType]


def GetComponentClass(oMgrManager):
    return CNewSurvivorElement

