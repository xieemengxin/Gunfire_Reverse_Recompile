# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivorchallenge.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivorchallenge.pyc
# Source Generated with Decompyle++
# File: survivorchallenge.pyc (Python 3.6)

from cl_object.logging import SurvivorLog
from cl_only import SendAlert, Functor
from cl_commondefines import MG_SOURCE_ELITEPHASEREWARD, WARRIOR_ELITE, CHASTATUS_WAIT, CHASTATUS_CONTINUE, CHASTATUS_OVER, CBEHAVIOR_GLOBALAUTOPICK
import cl_msgcenter
import cl_snetwar
import cl_math
import cl_reward
import cl_formula

class CEliteChallenge(object):
    
    def __init__(self, oSurvivorElement):
        self.m_CallFlag = 'survivorEliteChallenge'
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_EliteChallengeReward = []
        self.m_LockElite = []
        self.m_Reward = []
        self.m_State = CHASTATUS_WAIT
        self.m_CreateEffect = 1012
        self.m_DelayFrame = 75

    
    def Init(self):
        oGame = self.m_Game
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Survivor.Remove_Call_Out_Suspendable(self.m_CallFlag + 'DelayCreate')
        self.m_Survivor = None
        self.m_Game = None

    
    def OnDie(self, oWarMgr, oTarget, dInfo):
        if self.m_State != CHASTATUS_CONTINUE:
            return None
        if oTarget.m_FightType & WARRIOR_ELITE != WARRIOR_ELITE:
            return None
        if oTarget.m_ID in self.m_LockElite:
            self.m_LockElite.remove(oTarget.m_ID)
        if not self.m_LockElite:
            self.OnChallengeOver(oTarget, dInfo)

    
    def StartChallenge(self):
        self.m_Survivor.m_FightTimerMgr.PauseCounting('ElitePhase')
        self.m_Survivor.m_RareCupInteractRecord['Finish'] = 0
        self.OnEliteChallenge()

    
    def OnChallengeOver(self, oTarget, dInfo):
        self.m_State = CHASTATUS_OVER
        oSurvivor = self.m_Survivor
        oSurvivor.SceneMonsterAllDie()
        self.EliteChallengeReward(oTarget, dInfo)
        oSurvivor.Exec_Suspendable(self.CheckOver)

    
    def CheckOver(self):
        if not self.m_State == CHASTATUS_OVER:
            return None
        self.TriggerGlobalAutoPick()
        self.m_Survivor.PreAddPhase()
        self.m_Survivor.OnEliteChallengeOver()

    
    def TriggerGlobalAutoPick(self):
        oWarMgr = self.m_Game.m_WarMgr
        dPlayer = oWarMgr.GetLivePlayer()
        for iPlayer in dPlayer:
            oHero = oWarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, oHero.m_ID, CBEHAVIOR_GLOBALAUTOPICK, [
                iPlayer])
        

    
    def EliteChallengeReward(self, oTarget, dInfo):
        oSurvivor = self.m_Survivor
        self.m_Survivor.m_RareCupInteractRecord['Finish'] = 1
        if oSurvivor.m_Phase in self.m_EliteChallengeReward:
            return None
        if oSurvivor.m_Phase not in oSurvivor.m_RareCupDropPhase:
            return None
        SurvivorLog.Debug('game:%d elitechallengereward:%d' % (self.m_Game.m_ID, oSurvivor.m_Phase))
        self.m_EliteChallengeReward.append(oSurvivor.m_Phase)
        dRareInfo = oSurvivor.m_RareTalentInfo
        dReward = {
            dRareInfo['DropMiniGm']: (dRareInfo['DropProb'], dRareInfo['DropTimes']) }
        iAttack = dInfo['AID']
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'Abandoner': oTarget.m_ID,
            'CanReward': 1,
            'AutoReward': 1 }
        cl_reward.RewardItemByMiniGame(oTarget, iAttack, dReward, 'EliteChallengeReward%d' % iAttack, MG_SOURCE_ELITEPHASEREWARD, dExtInfo)

    
    def OnEliteChallenge(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oSurvivor = self.m_Survivor
        dEliteInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_CurLine.m_Name, 'monsterelitepos')
        vElitePos = None
        oTarget = oSurvivor.GetMaxDamageTarget()
        if oTarget:
            vTarget = oTarget.GetPos()
            fMin = 999999
            for dPos in dEliteInfo.values():
                fHighLimit = dPos['HighLimit'] if 'HighLimit' in dPos else 0
                vPos = dPos['Center']
                dCheckDropInfo = dPos['CheckDropInfo'] if 'CheckDropInfo' in dPos else { }
                vFixDropPos = dPos['FixDropPos'] if 'FixDropPos' in dPos else None
                fDistance = cl_math.CalDistance(vTarget, vPos)
                if fDistance < fMin:
                    fMin = fDistance
                    if fHighLimit > 1e-06 and abs(vTarget[1] - vPos[1]) > fHighLimit:
                        continue
                    vElitePos = (vPos, (0, 0, 0), [], (dCheckDropInfo, vFixDropPos), 0)
            
        if not vElitePos:
            SurvivorLog.Debug('game:%d no target:%d' % (oGame.m_ID, oSurvivor.m_Phase))
            lstEliteInfo = list(dEliteInfo.values())
            idx = oGame.Random(len(lstEliteInfo))
            vPos = lstEliteInfo[idx]['Center']
            vElitePos = (vPos, (0, 0, 0), [], ({ }, None), 0)
        dPhaseInfo = oSurvivor.m_PhaseConfig[oSurvivor.m_ConfigSID]
        iExpectedPower = dPhaseInfo[oSurvivor.m_Phase]['ExpectedMonsterNumber']
        iExtraPower = cl_formula.GetFormulaResult(self, dPhaseInfo[oSurvivor.m_Phase]['ExtraMonster'])
        iExtraMonsterLimit = dPhaseInfo[oSurvivor.m_Phase]['ExtraMonsterLimit']
        iExpectedPower = min(iExpectedPower + iExtraPower, iExpectedPower + iExtraMonsterLimit)
        iGrade = dPhaseInfo[oSurvivor.m_Phase]['Grade']
        dMonsterWeight = dPhaseInfo[oSurvivor.m_Phase]['MonsterWeight']
        dRes = oSurvivor.m_CurLine.m_MonsterCtrl.GetNeedSpawnMonster({ }, oSurvivor.m_MonsterPower, dMonsterWeight, iExpectedPower * 100)
        iScene = oLevelCtrl.m_CurNode.m_Scene
        dPlayer = oGame.GetRealPlayers()
        iEffectID = oGame.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, self.m_CreateEffect, vElitePos[0], dPlayer)
        func = Functor(self.DelayCreateMonster, dRes, iGrade, vElitePos)
        oSurvivor.Call_Out_Suspendable(func, self.m_DelayFrame, self.m_CallFlag + 'DelayCreate')

    
    def DelayCreateMonster(self, dCreateMonster, iGrade, tPos):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oSurvivor = self.m_Survivor
        for iMonsterSID, iCount in dCreateMonster.items():
            for _ in range(iCount):
                oMonster = oSurvivor.m_CurLine.m_MonsterCtrl.CreateMonster(iMonsterSID, iGrade, tPos)
                if not oMonster:
                    SendAlert('err', '关卡%s 幸存者模式配置怪物SID:%s不存在' % (oLevelCtrl.m_CurNode.m_Level, iMonsterSID))
                    continue
                self.m_LockElite.append(oMonster.m_ID)
            
        
        self.m_State = CHASTATUS_CONTINUE
        if not self.m_LockElite:
            SendAlert('err', '关卡%s 幸存者模式精英阶段%d没有怪物,直接跳下阶段' % (oLevelCtrl.m_CurNode.m_Level, oSurvivor.m_Phase))
            oSurvivor.PreAddPhase()
            oSurvivor.OnEliteChallengeOver()



def NewEliteChallenge(oSurvivorElement):
    oEliteChallenge = CEliteChallenge(oSurvivorElement)
    oEliteChallenge.Init()
    return oEliteChallenge

