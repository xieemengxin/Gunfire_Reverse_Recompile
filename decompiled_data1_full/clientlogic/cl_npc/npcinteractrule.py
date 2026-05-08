# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/npcinteractrule.pyc
# RelativePath: clientlogic/cl_npc/npcinteractrule.pyc
# Source Generated with Decompyle++
# File: npcinteractrule.pyc (Python 3.6)

from cl_only import WeakProxy, GAME_FRAME, Time2Frame
from cl_commondefines import PF_TYPE_RELIC, PF_TYPE_TALENT, CHALLENGE_REWARD_OPEN, CHALLENGE_REWARD_LOCK, CHALLENGE_REWARD_PEND, INTERACT_TYPE_FORBID, INTERACT_TYPE_ALLOW, INTERACT_RULE_CDNOTIFY, INTERACT_RULE_CDTIME, INTERACT_RULE_LEVELGOAL, INTERACT_RULE_ENDLESSTIME, INTERACT_RULE_CHALLENGE, INTERACT_RULE_SINGLE, INTERACT_RULE_INITWEAPON, INTERACT_RULE_MULCHOOSE, INTERACT_RULE_SMITHUPGRADE, INTERACT_RULE_AUTOFINISH
import cl_msgcenter
import cl_notify
import cl_minigame
from . import net

class CBaseInteractRule(object):
    
    def __init__(self, oOwner, dParam):
        self.m_Owner = WeakProxy(oOwner)
        self.m_Game = self.m_Owner.m_Game
        self.m_Notify = dParam.get('Notify', 0)
        self.OnInit(dParam)

    
    def OnInit(self, dParam):
        pass

    
    def Release(self):
        self.OnRelease()
        self.m_Owner = None

    
    def OnRelease(self):
        pass

    
    def ValidInteract(self, oHero):
        return True

    
    def SendValidInteractMsg(self, oHero):
        pass



class CCDTimeNotify(CBaseInteractRule):
    
    def OnInit(self, dParam):
        self.m_DelayCDFrame = Time2Frame(dParam['Time'])
        self.m_HeroCDTime = { }
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, 'NPCInteractRule', -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, 'NPCInteractRule')

    
    def ValidInteract(self, oHero):
        if oHero.m_ID in self.m_HeroCDTime:
            iNowFrame = self.m_Game.GetFrameNum()
            if iNowFrame <= self.m_HeroCDTime[oHero.m_ID]:
                return False
        return True

    
    def SendValidInteractMsg(self, oHero):
        if self.m_Notify:
            iRemainFrame = self.m_HeroCDTime[oHero.m_ID] - self.m_Game.GetFrameNum()
            iRemainTime = iRemainFrame // GAME_FRAME
            cl_notify.SendCommonNotify(self.m_Game, [
                oHero.m_PlayerID], self.m_Notify, {
                '$target': str(iRemainTime) })

    
    def OnInteract(self, oNpc, dInfo):
        if oNpc.m_ID != self.m_Owner.m_ID:
            return None
        pid = dInfo['Hero']
        self.m_HeroCDTime[pid] = self.m_Game.GetFrameNum() + self.m_DelayCDFrame



class CCDTimeRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        self.m_DelayCDFrame = Time2Frame(dParam['Time'])
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, 'CCDTimeRule', -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, 'CCDTimeRule')
        self.m_Owner.Remove_Call_Out('CCDTimeRule%d' % self.m_Owner.m_ID)

    
    def OnInteract(self, oNpc, dInfo):
        if oNpc.m_ID != self.m_Owner.m_ID:
            return None
        self.m_Owner.Call_Out(self.OnRevertInteractStatus, self.m_DelayCDFrame, 'CCDTimeRule%d' % self.m_Owner.m_ID)

    
    def OnRevertInteractStatus(self):
        oGame = self.m_Owner.m_Game
        lstPlayer = oGame.m_WarMgr.GetAllPlayer()
        self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)



class CLevelGoalRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        self.m_Trigger = False
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(self.m_Owner, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnGoalReward, 'LevelGoalPassbox')
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)

    
    def OnRelease(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(self.m_Owner, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelGoalPassbox')

    
    def OnGoalReward(self, oNpc, oWarMgr, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        tLineIdx = oNpc.m_LineIdx
        if not tLineIdx or tLineIdx[0] != iLevel:
            return None
        self.OnRelease()
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        if 'PassLevel' not in dMsgInfo or dMsgInfo['PassLevel'] is True:
            oNpc.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)
        self.m_Trigger = True

    
    def ValidInteract(self, oHero):
        return self.m_Trigger



class CEndlessTimeRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        oWarMgr = self.m_Game.m_WarMgr
        if oWarMgr.IsEndlessTimeOut():
            for pid in oWarMgr.GetAllPlayer():
                self.m_Owner.SetHeroInteractStatusDone(pid)
            
        else:
            cl_msgcenter.AddAttentionFunc(self.m_Owner, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ENDLESS_TIMEOUT, self.OnEndlessTimeOut, 'EndlessTimeRule')

    
    def OnRelease(self):
        cl_msgcenter.DoneAttention(self.m_Owner, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ENDLESS_TIMEOUT, 'EndlessTimeRule')

    
    def OnEndlessTimeOut(self, oNpc, oWarMgr, dMsgInfo):
        for pid in oWarMgr.GetAllPlayer():
            oNpc.SetHeroInteractStatusDone(pid)
        

    
    def ValidInteract(self, oHero):
        return not self.m_Game.m_WarMgr.IsEndlessTimeOut()



class CChallengeRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        self.m_DelaySuccessFrame = Time2Frame(dParam.get('Time', 0))
        self.m_Trigger = False
        self.m_Status = CHALLENGE_REWARD_PEND
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnGoalReward, 'ChallengePassBox')
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateOver, 'ChallengePassBoxCreate', -1, 0)
        self.m_Game.AddGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'ChallengePassBox%d' % self.m_Owner.m_ID)
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)

    
    def OnRelease(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'ChallengePassBox')
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_NPCCREATEOVER, 'ChallengePassBoxCreate')
        self.m_Game.DoneGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'ChallengePassBox%d' % self.m_Owner.m_ID)

    
    def OnGoalReward(self, oNpc, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iSuccess = dMsgInfo['Rlt']
        tLineIdx = oNpc.m_LineIdx
        if not tLineIdx or tLineIdx[0] != iLevel:
            return None
        if not iSuccess:
            self.m_Status = CHALLENGE_REWARD_LOCK
            self.SendRewardStatusInScene()
        elif not self.m_DelaySuccessFrame:
            self.OnDelaySuccess()
        else:
            self.m_Owner.Call_Out(self.OnDelaySuccess, self.m_DelaySuccessFrame, 'DelayChallengeSuccess%d' % self.m_Owner.m_ID)

    
    def OnDelaySuccess(self):
        if self.m_Status != CHALLENGE_REWARD_PEND:
            return None
        self.m_Trigger = True
        self.m_Status = CHALLENGE_REWARD_OPEN
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)
        self.SendRewardStatusInScene()

    
    def SendRewardStatusInScene(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Owner.m_Scene)
        if oScene:
            lstPlayer = oScene.GetPlayers()
            self.SendChallengeRewardStatus(lstPlayer)

    
    def OnPlayerMapLoadOK(self, oOwner, oTarget, dInfo):
        pid = dInfo['pid']
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero and oHero.m_Scene == oOwner.m_Scene:
            self.SendChallengeRewardStatus([
                pid])

    
    def ValidInteract(self, oHero):
        return self.m_Trigger

    
    def SendChallengeRewardStatus(self, lstPlayer):
        for pid in lstPlayer:
            net.GS2CNpcChallengeStatus(pid, self.m_Owner.m_ID, self.m_Status)
        

    
    def OnCreateOver(self, oNpc, dInfo):
        if oNpc.m_ID != self.m_Owner.m_ID:
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Owner.m_Scene)
        if oScene:
            lstPlayer = oScene.GetPlayers()
            self.SendChallengeRewardStatus(lstPlayer)



class CSingleRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, 'NPCInteractRule', -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_NPCINTERACT, 'NPCInteractRule')

    
    def OnInteract(self, oNpc, dInfo):
        if oNpc.m_ID != self.m_Owner.m_ID:
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        for pid in lstPlayer:
            self.m_Owner.SetHeroInteractStatus(pid, 0)
        
        self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)



class CInitWeaponRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        oGame = self.m_Game
        oOwner = self.m_Owner
        for pid in lstPlayer:
            oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
            if oHero.Query('InitWeaponDrop', { }):
                continue
            oOwner.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                pid])
        

    
    def ValidInteract(self, oHero):
        if oHero.Query('InitWeaponDrop', { }):
            return True
        return False



class CMultiInteractRule(CBaseInteractRule):
    m_Type2Msg = {
        PF_TYPE_RELIC: cl_msgcenter.MSG_WAR_ADDRELIC,
        PF_TYPE_TALENT: cl_msgcenter.MSG_WAR_TALENT_CHOOSE_END }
    
    def OnInit(self, dParam):
        iTimes = dParam['Times']
        self.m_PFType = dParam['PFType']
        if self.m_PFType not in self.m_Type2Msg:
            return None
        iMsg = self.m_Type2Msg[self.m_PFType]
        self.m_InteractTimes = { }
        oWarMgr = self.m_Game.m_WarMgr
        lstHero = oWarMgr.GetRoomHero()
        for iHero in lstHero:
            self.m_InteractTimes[iHero] = iTimes
            cl_msgcenter.AddAttentionFunc(self.m_Owner, iHero, iMsg, self.OnReward, 'MultiInteract%d' % self.m_Owner.m_ID)
        

    
    def OnRelease(self):
        iMsg = self.m_Type2Msg[self.m_PFType]
        for iHero in self.m_InteractTimes.keys():
            cl_msgcenter.DoneAttention(self.m_Owner, iHero, iMsg, 'MultiInteract%d' % self.m_Owner.m_ID)
        
        self.m_InteractTimes = { }

    
    def OnReward(self, oNpc, oHero, dInfo):
        iNpcID = dInfo['NpcID']
        if iNpcID != self.m_Owner.m_ID:
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_InteractTimes:
            return None
        iTimes = self.m_InteractTimes[iHero]
        if iTimes <= 0:
            return None
        self.m_InteractTimes[iHero] -= 1
        if self.m_InteractTimes[iHero] == 0:
            self.m_Owner.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                oHero.m_PlayerID])
        else:
            oNpc.ResetTalentReward(oHero.m_PlayerID)
            oMiniGame = cl_minigame.NewMiniGame(oNpc.m_Game, oNpc.Query('iMiniGame'), oNpc.m_ID, iHero, oNpc.Query('dExtInfo'))
            if oMiniGame:
                oMiniGame.SendChoose()

    
    def GetHeroInteractTimes(self, iHeroID):
        if iHeroID not in self.m_InteractTimes:
            return 0
        return self.m_InteractTimes[iHeroID]



class CSmithUpgradeRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        oWarMgr = self.m_Game.m_WarMgr
        lstHero = oWarMgr.GetRoomHero()
        self.m_UpgradeTimes = { }
        self.m_InitTimes = dParam['Times']
        for iHero in lstHero:
            self.m_UpgradeTimes[iHero] = 0
            cl_msgcenter.AddAttentionFunc(self.m_Owner, iHero, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, self.OnUpgradeWeapon, 'RuleUpgradeWeapon%d' % self.m_Owner.m_ID)
        

    
    def OnRelease(self):
        for iHero in self.m_UpgradeTimes.keys():
            cl_msgcenter.DoneAttention(self.m_Owner, iHero, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, 'RuleUpgradeWeapon%d' % self.m_Owner.m_ID)
        

    
    def OnUpgradeWeapon(self, oNpc, oHero, dInfo):
        if dInfo['NpcID'] != self.m_Owner.m_ID:
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_UpgradeTimes:
            return None
        self.m_UpgradeTimes[iHero] += 1

    
    def GetMaxUpgradeTimes(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return 0
        iForceSetWeaponUpgradeUnlimit = oHero.Query('ForceSetWeaponUpgradeUnlimit', 0)
        if iForceSetWeaponUpgradeUnlimit:
            return -1
        iExtra = oHero.Query('AdditionalWeaponUpgrade', 0)
        iMaxUpTimes = self.m_InitTimes + iExtra
        return iMaxUpTimes

    
    def GetUpgradeTimes(self, iHero):
        if iHero not in self.m_UpgradeTimes:
            return (0, 0)
        iMaxUpTimes = self.GetMaxUpgradeTimes(iHero)
        if iMaxUpTimes == -1:
            return (-1, -1)
        iRestUpTimes = iMaxUpTimes - self.m_UpgradeTimes[iHero]
        if iRestUpTimes < 0:
            iRestUpTimes = 0
        return (iRestUpTimes, iMaxUpTimes)

    
    def ValidUpgrade(self, iHero):
        iMaxUpTimes = self.GetMaxUpgradeTimes(iHero)
        if iMaxUpTimes == -1:
            return 1
        if iHero in self.m_UpgradeTimes and self.m_UpgradeTimes[iHero] < iMaxUpTimes:
            return 1
        return 0



class CAutoFinishRule(CBaseInteractRule):
    
    def OnInit(self, dParam):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnRoomChallenge, 'AutoFinishRule')

    
    def OnRelease(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'AutoFinishRule')

    
    def OnRoomChallenge(self, oNpc, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iSuccess = dMsgInfo['Rlt']
        tLineIdx = oNpc.m_LineIdx
        if not tLineIdx or tLineIdx[0] != iLevel:
            return None
        self.OnRelease()
        if not iSuccess:
            return None
        oNpc.m_CheckInteractDistance = False
        lstHero = self.m_Game.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            oNpc.Interact(oHero)
        


g_InteractRule = {
    INTERACT_RULE_AUTOFINISH: CAutoFinishRule,
    INTERACT_RULE_SMITHUPGRADE: CSmithUpgradeRule,
    INTERACT_RULE_MULCHOOSE: CMultiInteractRule,
    INTERACT_RULE_INITWEAPON: CInitWeaponRule,
    INTERACT_RULE_SINGLE: CSingleRule,
    INTERACT_RULE_CHALLENGE: CChallengeRule,
    INTERACT_RULE_ENDLESSTIME: CEndlessTimeRule,
    INTERACT_RULE_LEVELGOAL: CLevelGoalRule,
    INTERACT_RULE_CDTIME: CCDTimeRule,
    INTERACT_RULE_CDNOTIFY: CCDTimeNotify }

def GetInteractRule(iType, oNpc, dParam):
    if iType not in g_InteractRule:
        return None
    clsRule = g_InteractRule[iType]
    oRule = clsRule(oNpc, dParam)
    return oRule

