# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/teammateaielement.pyc
# RelativePath: clientlogic/cl_warmgr/teammateaielement.pyc
# Source Generated with Decompyle++
# File: teammateaielement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_object.logging import TeammateaiLog
from cl_commondefines import TYPE_RELIFE_PASS, CURWEAPON_SWITCH, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, PLAY_TYPE_SINGLE, DEBUG_STATUS_NOCOSTBULLET, GetMaxMemberNum, LINK_ONLINE, LINK_DISCONNECT, LINK_QUIT, LINK_DELEGATE, LINK_ACTIVEDELEGATE, NWARRIOR_DROP_RELIC, NWARRIOR_NPC_ALL_GOLDENCUP, INTERACT_TYPE_FORBID, TYPE_RELIFE_RELIC, NWARRIOR_NPC_TRANSFER, TRANSFER_DIRTO_HIDE, WARRIOR_BOSS, BOSS_DONOT_COUNT, MG_SOURCE_AIKILLBOSS, NWARRIOR_DROP_EQUIP, LEVEL_TYPE_HALL, BENE_SOURCE_LAYER, WEAPON_MAIN_PERFORM
from cl_cscommondef import PF_TYPE_PASSIVE, EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_MASK_WEAPON
from cl_only import ChooseKey, DeepCopy, MIN_NPC_ID, PythonError, PY_FLAG_DEAD, ShufferList
from cl_npc.benedictionnpc import DealBeneWeight, MAX_BENE_CNT
from cl_signal.load import GetAIShareSignalFightType
from cl_pxlayer import PXMASK_SIGHTBLK, PXMASK_AIRWALL
import cl_msgcenter
import cl_betree
import cl_perform
import cllib.lib_flag as lib_flag
import cl_item
import cl_reward
import cli_player
import cl_platformdata
import cl_perform.load

class CTeammateAIElement(CBaseElement):
    m_CallFlag = 'TeammateAIElement'
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_AIMember = { }
        self.m_UnderControl = { }
        self.m_WaitingControl = { }
        self.m_CreateInfo = { }
        self.m_Loaded = False
        if lib_flag.g_IsMobile:
            self.m_OpenDelegate = self.m_WarMgr.m_ExtraInfo['TeammateAI'].get('DelegateAI', 0)
        else:
            self.m_OpenDelegate = 1
        self.m_InitPlayer = []
        self.m_HeroCache = { }
        self.m_InitPlayerNum = 0
        self.m_AIConvertRatio = oData.m_Config.get('AIConvertRatio', 0)
        self.m_FollowTarget = { }
        self.m_WeaponInfo = oData.m_Config.get('Weapon', { })
        self.m_HeroInitPassive = { }
        self.m_HeroBasicPassive = oData.m_Config.get('HeroBasicPassive', [])
        self.m_HeroPassive = oData.m_Config.get('HeroPassive', { })
        self.m_RelicWhiteList = oData.m_Config.get('RelicWhiteList', [])[:]
        self.m_RelicWhiteList.extend(cl_perform.load.GetGameExcludeRelic(PLAY_TYPE_SINGLE))
        self.m_RelicNoChoosedList = oData.m_Config.get('RelicNoChoosed', [])
        self.m_RelicNoChoosedList.extend(cl_platformdata.GetConsumableRelic())
        self.m_PerformWhiteList = oData.m_Config.get('PerformWhiteList', [])
        self.m_TaskPassiveWhiteList = oData.m_Config.get('TaskPassiveWhiteList', { })
        self.m_BeneWhiteList = oData.m_Config.get('BeneWhiteList', [])
        self.m_RewardBeneLayer = oData.m_Config.get('RewardBeneLayer', [])
        self.m_AIMemberChooseBene = oData.m_AIMemberChooseBene
        self.m_SeasonSuitRelicWeight = oData.m_Config.get('SeasonSuitRelicWeight', 10)
        self.m_SeasonSuitWhiteList = oData.m_Config.get('SeasonSuitWhiteList', [])
        self.m_DamThreshold = oData.m_Config.get('DamThreshold', 0)
        self.m_HeroDieInfo = { }
        self.m_HeroTotalDamage = { }
        self.m_RecordHeroDamage = { }
        self.m_BossShareDropProb = oData.m_Config.get('BossShareDropProb', 5)
        self.m_BossShareDropCnt = oData.m_Config.get('BossShareDropCnt', {
            1: 50,
            2: 50 })
        self.m_BossShareDropMG = oData.m_Config.get('BossShareDropMG', {
            1001: 10,
            2401: 10 })
        self.m_ShareItem = { }

    
    def Init(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_PREADDPLAYER, self.OnPreAddPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.CheckAllDead, self.m_CallFlag + 'AllDeadCheck')
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_TRIGGERGATECTRL, self.OnHeroTriggerGateCtrl, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnLogin, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, self.OnLeaveGame, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnNpcCreateOver, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_CallFlag)

    
    def AddHeroAttention(self, iHero):
        self.m_HeroDieInfo[iHero] = []
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnLinkStatusChange, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnDiedist, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnHeroRelife, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_TRIGGERGATETRANSFER, self.OnTriggerGateTransfer, self.m_CallFlag)

    
    def Release(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        lstHero = set(self.m_WarMgr.GetAllHero()) | set(self.GetAllAIHero())
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIEDIST, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_TRIGGERGATETRANSFER, self.m_CallFlag)
        
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_PREADDPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag + 'AllDeadCheck')
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_TRIGGERGATECTRL, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_WarMgr = None
        super().Release()

    
    def Save(self):
        for iPlayer in self.m_WarMgr.GetAllPlayer():
            self.RecordOnePlayerDamage(iPlayer)
        
        self.m_RecordHeroDamage = DeepCopy(self.m_HeroTotalDamage)
        return { }

    
    def TrueSave(self):
        oTeamSaveElement = self.m_WarMgr.GetComponent('TeamSaveElement')
        if not oTeamSaveElement:
            return { }
        lstPlayer = self.m_WarMgr.GetAllPlayer()
        dCreateInfo = { }
        lstPopKey = [
            'Level',
            'BigData',
            'Drop',
            'WarMgr']
        for pid in lstPlayer:
            if pid not in self.m_CreateInfo:
                TeammateaiLog.Alert('%s no createinfo %s' % (self.m_Game.m_ID, pid))
                continue
            dCreateInfo[pid] = self.m_CreateInfo[pid]
            dRecord = oTeamSaveElement.Save(pid)
            if pid in self.m_AIMember:
                for sKey in lstPopKey:
                    dRecord.pop(sKey, None)
                
            dCreateInfo[pid]['TransferRecord'] = dRecord
        
        dData = {
            'CreateInfo': dCreateInfo,
            'UnderControl': dict(self.m_UnderControl),
            'AIMember': self.m_AIMember,
            'HeroCache': self.m_HeroCache,
            'RecordHeroDamage': self.m_RecordHeroDamage,
            'InitPlayerNum': self.m_InitPlayerNum }
        TeammateaiLog.Info('%s save %s' % (self.m_Game.m_ID, list(dCreateInfo)))
        return dData

    
    def Load(self, dData):
        if not dData or self.m_Loaded:
            return None
        self.m_Loaded = True
        self.m_CreateInfo = dData.get('CreateInfo', { })
        self.m_AIMember = dData.get('AIMember', { })
        self.m_HeroCache = dData.get('HeroCache', { })
        self.m_RecordHeroDamage = dData.get('RecordHeroDamage', { })
        self.m_HeroTotalDamage = DeepCopy(self.m_RecordHeroDamage)
        self.m_InitPlayerNum = dData.get('InitPlayerNum', 0)
        TeammateaiLog.Info('%s load %s %s' % (self.m_Game.m_ID, list(self.m_CreateInfo), self.m_InitPlayer))
        for pid, dInfo in self.m_CreateInfo.items():
            if pid not in self.m_InitPlayer:
                self.m_WarMgr.AddPlayer(pid, dInfo)
                self.m_WarMgr.RemovePlayer(pid, iNowDisconnect = 1)
        

    
    def OnPreAddPlayer(self, oListener, oWarMgr, dMsgInfo):
        dPlayerInfo = dMsgInfo['CreateInfo']
        if oWarMgr.IsTransferGame():
            self.m_InitPlayer = list(dPlayerInfo)
            return None
        if 'TeammateAI' not in oWarMgr.m_ExtraInfo:
            return None
        dTeammateAI = oWarMgr.m_ExtraInfo['TeammateAI']
        if 'AIMember' not in dTeammateAI:
            return None
        if not dTeammateAI['AIMember']:
            return None
        iRealPlayerNum = len(dPlayerInfo)
        iMaxMemberNum = GetMaxMemberNum(oWarMgr.m_PlayMode)
        if iRealPlayerNum >= iMaxMemberNum:
            return None
        oGame = self.m_Game
        iRemainNum = iMaxMemberNum - iRealPlayerNum
        iClientAINum = len(dTeammateAI['AIMember'])
        iAINum = iRemainNum if iClientAINum > iRemainNum else iClientAINum
        self.m_InitPlayerNum = iRealPlayerNum + iAINum * self.m_AIConvertRatio
        iMaster = self.GetWarMaster(dPlayerInfo)
        if iMaster not in dPlayerInfo:
            TeammateaiLog.Alert('%s no master info %s %s' % (oGame.m_ID, oWarMgr.GetRoomPlayer(), iMaster))
            return None
        dMasterInfo = dPlayerInfo[iMaster]
        iDelegateAIPid = MIN_NPC_ID - 10
        for dAIInfo in dTeammateAI['AIMember']:
            iRemainNum -= 1
            if iRemainNum < 0:
                TeammateaiLog.Alert('%s aimember error %s %s' % (oGame.m_ID, iRealPlayerNum, len(dTeammateAI['AIMember'])))
                break
            for _ in range(10):
                iDelegateAIPid += 1
                if iDelegateAIPid not in dPlayerInfo:
                    break
            
            dDelegateAI = self.FilterAIMemberInfo(dMasterInfo)
            dDelegateAI['Name'] = dAIInfo['name']
            dDelegateAI['CurHero'] = dAIInfo['hero']
            dDelegateAI['IsAI'] = 1
            oWarMgr.AddPlayer(iDelegateAIPid, dDelegateAI)
            self.m_AIMember[iDelegateAIPid] = dDelegateAI
            oWarMgr.RemovePlayer(iDelegateAIPid, iNowDisconnect = 1)
            oHero = oWarMgr.GetHeroByPlayer(iDelegateAIPid)
            self.TakeOverHero(oHero.m_ID, bGoNewScene = False)
        

    
    def CheckHasAIMember(self):
        if self.m_AIMember:
            return 1
        if not self.m_OpenDelegate:
            return 0
        oWarMgr = self.m_Game.m_WarMgr
        if 'TeammateAI' not in oWarMgr.m_ExtraInfo:
            return 0
        if 'AIMember' not in oWarMgr.m_ExtraInfo['TeammateAI']:
            return 0
        if not oWarMgr.m_ExtraInfo['TeammateAI']['AIMember']:
            return 0
        return 1

    
    def GetAIMember(self):
        return list(self.m_AIMember.keys())

    
    def FilterAIMemberInfo(self, dMasterInfo):
        dDelegateAI = DeepCopy(dMasterInfo)
        dDelegateAI.pop('Account', 0)
        dDelegateAI.pop('UnlockProgress', { })
        dDelegateAI.pop('AdjustWeaponInfo', { })
        dDelegateAI.pop('NewUnlockProgress', { })
        dDelegateAI.pop('SeasonTask', { })
        dDelegateAI.pop('Achieve', { })
        dDelegateAI.pop('Pet', { })
        dDelegateAI.pop('SeasonSuit', { })
        self.FilterAISeasonInfo(dDelegateAI)
        return dDelegateAI

    
    def FilterAISeasonInfo(self, dDelegateAI):
        oWarMgr = self.m_WarMgr
        lstSeasonElement = oWarMgr.GetCurSeasonAllElement()
        for sElement in lstSeasonElement:
            oElement = oWarMgr.GetComponent(sElement)
            if not oElement:
                continue
            if oElement.m_IsInheritSeasonElement:
                oElement.FilterAndFixAISeasonInfo(dDelegateAI)
        

    
    def OnAddAllPlayer(self, _oListener, _oWarMgr, dMsgInfo):
        if lib_flag.g_IsStandaloneClient and dMsgInfo:
            dPlayerInfo = dMsgInfo.get('CreateInfo', { })
            for pid, dInfo in dPlayerInfo.items():
                if pid not in self.m_CreateInfo or pid in self.m_AIMember:
                    dInfo = self.FilterAIMemberInfo(dInfo)
                self.m_CreateInfo[pid] = dInfo
            
        lstHero = self.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            self.AddHeroAttention(iHero)
        
        for pid in self.m_CreateInfo:
            if not self.m_WarMgr.IsInRoom(pid):
                iHero = self.m_WarMgr.GetHeroIDByPlayerID(pid)
                self.TakeOverHero(iHero)
        
        TeammateaiLog.Debug('%s aimember %s' % (self.m_Game.m_ID, list(self.m_AIMember)))
        for iDelegateAIPid, dDelegateAI in self.m_AIMember.items():
            if iDelegateAIPid not in self.m_CreateInfo:
                self.m_CreateInfo[iDelegateAIPid] = dDelegateAI
        
        self.AssignFollowTarget(self.m_WarMgr.GetLiveHero(iCalAI = 0), bGotoNewScene = False)

    
    def CheckAllDead(self, _oListener, _Sender, _dMsgInfo):
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag + 'AllDeadCheck')
        if not self.m_WarMgr.GetLivePlayer():
            TeammateaiLog.Info('%s alldead' % self.m_Game.m_ID)
            self.m_WarMgr.CheckWarEnd()

    
    def GetWarMaster(self, dPlayerInfo):
        iMaster = self.m_WarMgr.GetWarMasterPlayer()
        if not iMaster:
            return list(dPlayerInfo)[0]
        return iMaster

    
    def GetAllAIHero(self, iIncludeWait = 0, bExcludeAIMember = False):
        lstAIHero = list(self.m_UnderControl)
        if iIncludeWait:
            lstAIHero.extend(list(self.m_WaitingControl))
        if bExcludeAIMember:
            for iPlayer in self.m_AIMember:
                iHero = self.m_WarMgr.GetHeroIDByPlayerID(iPlayer)
                if iHero in lstAIHero:
                    lstAIHero.remove(iHero)
            
        return lstAIHero

    
    def NeedToTakeOver(self, pid, iHero):
        if pid in self.m_AIMember:
            return 1
        if not self.m_OpenDelegate:
            return 0
        if iHero in self.m_UnderControl:
            return 0
        iHostPlayer = self.m_WarMgr.GetWarMasterPlayer()
        if iHostPlayer == pid:
            return 0
        lstRoom = self.m_WarMgr.GetRoomPlayer()
        if not lstRoom:
            return 0
        if len(lstRoom) == 1 and lstRoom[0] == pid:
            return 0
        return 1

    
    def NeedToHandOver(self, pid, iHero):
        if pid in self.m_AIMember:
            return 0
        if iHero not in self.m_UnderControl:
            return 0
        if self.m_WarMgr.HasSettled(pid):
            return 0
        return 1

    
    def OnLinkStatusChange(self, _oLinstener, oTarget, dMsgInfo):
        pid = oTarget.m_PlayerID
        iHero = oTarget.m_ID
        iNewStatus = dMsgInfo.get('LinkStatus', None)
        if iNewStatus in (LINK_QUIT, LINK_DISCONNECT):
            if not self.NeedToTakeOver(pid, iHero):
                return None
            self.TakeOverHero(iHero)
            self.AddtoScene(oTarget)
        elif iNewStatus == LINK_ONLINE and self.NeedToHandOver(pid, iHero):
            self.HandOverHero(iHero)

    
    def OnLogin(self, _oLinstener, oTarget, _dMsgInfo):
        pid = oTarget.m_PlayerID
        self.m_WarMgr.SendReloadFightRecord(lstPlayer = [
            pid])

    
    def OnLeaveGame(self, _oLinstener, oTarget, dMsgInfo):
        pid = oTarget.m_PlayerID
        iHero = oTarget.m_ID
        if not self.NeedToTakeOver(pid, iHero):
            return None
        self.m_WaitingControl[iHero] = pid
        dMsgInfo['Halt'] = 1

    
    def TakeOverHero(self, iHero, bGoNewScene = True):
        if iHero in self.m_UnderControl:
            TeammateaiLog.Alert('%s repeat %s' % (self.m_Game.m_ID, iHero))
            return None
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            TeammateaiLog.Alert('%s unexist %s' % (self.m_Game.m_ID, iHero))
            return None
        pid = oHero.m_PlayerID
        TeammateaiLog.Info('%s start %s %s' % (self.m_Game.m_ID, pid, iHero))
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.OnRemoveHero, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, self.OnHeroAddRelic, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, self.OnHeroActiveSeasonSuit, self.m_CallFlag)
        self.RecordOnePlayerDamage(pid)
        self.m_WaitingControl.pop(iHero, 0)
        self.m_UnderControl[iHero] = pid
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TAKEOVERHERO, oHero, {
            'pid': pid })
        oHero.ClearWaitSkill()
        iStatus = LINK_ACTIVEDELEGATE if pid in self.m_AIMember else LINK_DELEGATE
        oHero.SetLinkStatus(iStatus)
        oHero.Stop()
        self.m_HeroDieInfo[iHero] = []
        oDieElement = self.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement:
            oDieElement.OpenRescue(self.m_CallFlag)
        oReport = self.m_WarMgr.GetComponent('Warreport')
        if oReport:
            oReport.AddAttention([
                iHero])
        dCache = self.m_HeroCache.setdefault(pid, { })
        self.DisableHeroPower(oHero, dCache)
        if not oHero.m_Agent:
            dFsm = self.m_Data.m_Config.get('Fsm', { })
            sFsm = dFsm.get(oHero.m_SID, 'Hero.HeroTestFsm')
            oHero.m_Agent = cl_betree.InitFsmAI(oHero, 'cl_betree.heroagent', sFsm)
        self.EnableAIPerform(oHero)
        self.EnableWhileList(oHero)
        iDyingSecond = self.m_Data.m_Config.get('DyingSecond', 10)
        oHero.InitDyingSecond(iSecond = iDyingSecond)
        oHero.m_NoRayCheck = 1
        oHero.Set('DebugStatus', DEBUG_STATUS_NOCOSTBULLET)
        self.TryResetHeroLife(oHero)
        if bGoNewScene:
            lstUpdate = self.GetAIHeroByFollowTarget(iHero)
            lstUpdate.append(iHero)
            self.UpdateFollowTarget(lstUpdate)
        self.SetPlayerCommand(pid, bEnable = False)

    
    def HandOverHero(self, iHero):
        if iHero not in self.m_UnderControl:
            TeammateaiLog.Alert('%s repeat %s' % (self.m_Game.m_ID, iHero))
            return None
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not (oHero.m_Agent):
            TeammateaiLog.Alert('%s unexist %s' % (self.m_Game.m_ID, iHero))
            return None
        TeammateaiLog.Info('%s stop %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iHero))
        self.RecordOnePlayerDamage(oHero.m_PlayerID)
        self.m_UnderControl.pop(iHero)
        self.OnHandOverHero(oHero)
        oFollowTarget = self.GetFollowTarget(oHero.m_ID)
        if oFollowTarget and oFollowTarget.m_Scene and oFollowTarget.m_Scene == oHero.m_Scene:
            vFollowPos = oFollowTarget.GetPos()
            vSightFollowPos = (vFollowPos[0], vFollowPos[1] + oFollowTarget.m_ModelHeight * 0.85, vFollowPos[2])
            vHero = oHero.GetPos()
            vSightHeroPos = (vHero[0], vHero[1] + oHero.m_ModelHeight * 0.85, vHero[2])
            oGame = self.m_Game
            tRetPos = oGame.Scene_RaycastSingle(oFollowTarget.m_Scene, vSightFollowPos, vSightHeroPos, PXMASK_SIGHTBLK | PXMASK_AIRWALL)
            if tRetPos[0] != -1:
                oHero.WalkTo(vFollowPos, 'HandOverHero')
                TeammateaiLog.Debug('%s handover pos %s %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iHero, vFollowPos))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDOVERHERO, oHero, {
            'pid': oHero.m_PlayerID })
        cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, self.m_CallFlag)
        oHero.m_Agent.Disable(oHero, None)
        oHero.m_Agent.Release()
        oHero.m_Agent = None
        oHero.m_NoRayCheck = 0
        oHero.Set('DebugStatus', 0)
        dCache = self.m_HeroCache.pop(oHero.m_PlayerID, { })
        self.DisableAIPerform(oHero)
        self.EnableHeroPower(oHero, dCache)
        self.MakeUpReward(oHero, dCache)
        oReport = self.m_WarMgr.GetComponent('Warreport')
        if oReport:
            oReport.AddAttention([
                iHero])
        self.SetPlayerCommand(oHero.m_PlayerID, bEnable = True)

    
    def OnHandOverHero(self, oTarget):
        lstLiveHero = self.m_WarMgr.GetLiveHero(iCalAI = 0)
        self.AssignFollowTarget(lstLiveHero)

    
    def SetPlayerCommand(self, pid, bEnable):
        if not lib_flag.g_IsStandalone:
            return None
        if pid in self.m_AIMember:
            return None
        who = cli_player.GetPlayer(pid)
        if not who:
            return None
        who.SetPlayerCommand(bEnable)

    
    def OnRemoveHero(self, _oListener, oHero, _dMsgInfo):
        self.m_UnderControl.pop(oHero.m_ID, 0)

    
    def OnStartFight(self, _oListener, _oWarMgr, dMsgInfo):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        self.RewardBeneToAIMember(oLevelCtrl, dMsgInfo)
        if dMsgInfo['LevelType'] == LEVEL_TYPE_FIGHT:
            self.AddHideDoorShareItem(oLevelCtrl)
        if not oLevelCtrl.CheckFirstHall():
            return None
        oSaveElement = self.m_WarMgr.GetComponent('TeamSaveElement')
        if not oSaveElement or not oSaveElement.ValidSave():
            return None
        oSaveElement.SaveCurRecord({ })
        self.m_WarMgr.SendReloadFightRecord()

    
    def OnLevelGoal(self, _oListener, _oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo.get('LevelType', None)
        if iLevelType not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        self.UpdateWeapon()

    
    def OnEnterScene(self, _oLinstener, oTarget, dMsgInfo):
        if not self.m_UnderControl:
            return None
        oGame = self.m_Game
        if oTarget.m_ID in self.m_UnderControl:
            return None
        lstAIHero = self.GetAIHeroByFollowTarget(oTarget.m_ID)
        if not lstAIHero:
            return None
        iNewScene = oTarget.m_Scene
        if oTarget.ValidEnterNewScene(iNewScene):
            oScene = oGame.m_SceneMgr.GetScene(iNewScene)
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
            dPos = oLevelNode.GetGotoPos(lstAIHero)
        else:
            dPos = { }
        for iHero in lstAIHero:
            oAIHero = oGame.GetObject(iHero)
            dBornInfo = dPos[iHero] if oAIHero and oAIHero.m_Scene != iNewScene or iHero in dPos else { }
            self.GotoNewScene(oAIHero, oTarget, dBornInfo)
        

    
    def OnTriggerGateTransfer(self, _oLinstener, _oHero, dMsgInfo):
        iTarget = dMsgInfo['VID']
        self.TryTransferControlAI(iTarget)

    
    def OnHeroTriggerGateCtrl(self, _oListener, _oLevelCtrl, dMsgInfo):
        iTarget = dMsgInfo['VID']
        self.TryTransferControlAI(iTarget)

    
    def TryTransferControlAI(self, iTarget):
        if not self.m_UnderControl:
            return None
        if iTarget in self.m_UnderControl:
            return None
        lstAIHero = self.GetAIHeroByFollowTarget(iTarget)
        if not lstAIHero:
            return None
        oGame = self.m_Game
        for iHero in lstAIHero:
            oAIHero = oGame.GetObject(iHero)
            if oAIHero:
                self.GotoNewScene(oAIHero, None)
        

    
    def AssignFollowTarget(self, lstLiveHero, bGotoNewScene = True):
        if not (self.m_UnderControl) or not lstLiveHero:
            return None
        self.m_FollowTarget = { }
        oGame = self.m_Game
        lstLiveHero = ShufferList(oGame, lstLiveHero)
        iHeroNum = len(lstLiveHero)
        if iHeroNum == 1 or iHeroNum == 3:
            iTarget = lstLiveHero[0]
            for iAIHero in self.m_UnderControl:
                self.m_FollowTarget[iAIHero] = iTarget
            
        elif iHeroNum == 2:
            for iIndex, iAIHero in enumerate(self.m_UnderControl):
                self.m_FollowTarget[iAIHero] = lstLiveHero[iIndex]
            
        TeammateaiLog.Debug('%s assign follow %s %s %s ' % (oGame.m_ID, self.m_FollowTarget, list(self.m_UnderControl), lstLiveHero))
        if not bGotoNewScene:
            return None
        for iAIHero, iFollowTarget in self.m_FollowTarget.items():
            oFollowTarget = oGame.GetObject(iFollowTarget)
            if not oFollowTarget:
                continue
            oAIHero = oGame.GetObject(iAIHero)
            if oAIHero and oAIHero.m_Scene != oFollowTarget.m_Scene:
                self.GotoNewScene(oAIHero, oFollowTarget)
        

    
    def GotoNewScene(self, oHero, oTarget, dBornInfo = None):
        if not oTarget:
            oTarget = self.GetFollowTarget(oHero.m_ID)
        if oTarget:
            if not oTarget.m_Scene:
                return None
            if not dBornInfo:
                dBornInfo = { }
            TeammateaiLog.Debug('%s %s follow %s to %s' % (self.m_Game.m_ID, oHero.m_PlayerID, oTarget.m_Scene, oHero.m_Scene))
            vPos = dBornInfo.get('Pos', None)
            vFacing = dBornInfo.get('Facing', None)
            if not vFacing:
                vFacing = oTarget.GetFacing()
            if not vPos:
                vPos = oHero.m_Agent.ChooseTargetAroundPos(oTarget)
            if not vPos:
                vPos = oTarget.GetPos()
            oHero.Stop()
            if oTarget.m_Scene == oHero.m_Scene:
                oHero.WalkTo(vPos)
                oHero.SetFacing(vFacing)
            else:
                oHero.Goto(oTarget.m_Scene, vPos, vFacing)
            self.AddtoScene(oHero)
        else:
            TeammateaiLog.Debug('%s %s notarget %s' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_WarMgr.GetRoomPlayer()))

    
    def AddtoScene(self, oHero):
        oNewScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        if oNewScene:
            oNewScene.AddPlayer(oHero.m_PlayerID, oHero.m_ID)
            oNewScene.DelPlayer(oHero.m_PlayerID, 0)

    
    def UpdateFollowTarget(self, lstUpdate, iExcludeHero = 0):
        if not lstUpdate:
            return None
        lstLiveHero = self.m_WarMgr.GetLiveHero(iCalAI = 0)
        if iExcludeHero in lstLiveHero:
            lstLiveHero.remove(iExcludeHero)
        if not lstLiveHero:
            return None
        self.AssignFollowTarget(lstLiveHero)

    
    def GetFollowTarget(self, iAIHero):
        if iAIHero in self.m_FollowTarget:
            return self.m_Game.GetObject(self.m_FollowTarget[iAIHero])

    
    def GetAllFollowTargetInfo(self):
        return self.m_FollowTarget

    
    def DisableHeroPower(self, oHero, dCache):
        pid = oHero.m_PlayerID
        if pid not in self.m_AIMember:
            dStateData = oHero.m_State.Save()
            dRelifeData = oHero.SaveRelifeInfoByType(TYPE_RELIFE_RELIC)
        else:
            dStateData = { }
            dRelifeData = { }
        oHero.m_TaskCon.PauseSelf('AIControl')
        if oHero.m_SeasonTaskMgr:
            oHero.m_SeasonTaskMgr.Pause('AIControl')
        lstDiePerform = oHero.m_DieDisablePassive
        oHero.m_DieDisablePassive = None
        oHero.m_Perform.AllPerformDisable(iNotify = 0)
        oCareerPF = oHero.GetCareerPerform()
        if oCareerPF:
            oCareerPF.Enable(oHero, iNotify = 0)
        oThrowPF = oHero.GetThrowPerform()
        if oThrowPF:
            oThrowPF.Enable(oHero, iNotify = 0)
        oShiftPF = oHero.GetShiftPerform()
        if oShiftPF:
            oShiftPF.Enable(oHero, iNotify = 0)
        oHero.m_TalentCon.AllPerformDisable(iNotify = 0)
        dRelic = self.DisableHeroRelic(oHero)
        oHero.m_BenedictionCon.AllPerformDisable(iNotify = 0)
        self.DisableWeapon(oHero)
        dSeasonSuit = self.DisableHeroSeasonSuit(oHero)
        dDisabledState = oHero.m_State.DisableAllState(iRefresh = 1)
        dSeasonSeasonEffect = self.DisableHeroSeasonEffect(oHero)
        if pid not in self.m_AIMember:
            dCache['DiePerform'] = lstDiePerform
            dCache['State'] = dDisabledState
            dCache['StateData'] = dStateData
            dCache['Relic'] = dRelic
            dCache['Relife'] = dRelifeData
            dCache['SeasonSuit'] = dSeasonSuit
            dCache['SeasonEffect'] = dSeasonSeasonEffect

    
    def EnableHeroPower(self, oHero, dCache):
        lstDiePerform = dCache.get('DiePerform', [])
        if lstDiePerform:
            if oHero.m_DieDisablePassive:
                oHero.m_DieDisablePassive.extend(lstDiePerform)
            else:
                oHero.m_DieDisablePassive = lstDiePerform
            if not oHero.IsDead():
                oHero.RelifeEnablePassive()
        oHero.m_TaskCon.ResumeSelf('AIControl')
        if oHero.m_SeasonTaskMgr:
            oHero.m_SeasonTaskMgr.Resume('AIControl')
        oHero.m_Perform.AllPerformEnable(iNotify = 0)
        oHero.m_TalentCon.AllPerformEnable()
        self.EnableHeroRelic(oHero, dCache.get('Relic', { }))
        oHero.m_BenedictionCon.AllPerformEnable(iNotify = 0)
        self.EnableWeapon(oHero)
        self.EnableHeroSeasonSuit(oHero, dCache.get('SeasonSuit', { }))
        self.EnableHeroSeasonEffect(oHero, dCache.get('SeasonEffect', { }))
        oHero.m_State.EnableStates(dCache.get('State', { }))
        
        try:
            oHero.m_State.Load(dCache.get('StateData', { }))
        except:
            PythonError()

        oHero.LoadRelifeInfoByType(TYPE_RELIFE_RELIC, dCache.get('Relife', { }))

    
    def DisableHeroRelic(self, oHero):
        dResult = { }
        for iRelic in oHero.m_RelicCon.GetAllRelicSID():
            if iRelic in self.m_RelicWhiteList:
                continue
            oRelic = oHero.m_RelicCon.GetPerform(iRelic)
            if not oRelic or not (oRelic.m_Enable):
                continue
            dResult[iRelic] = 1
            oRelic.Disable(oHero, iNotify = 0)
        
        return dResult

    
    def EnableHeroRelic(self, oHero, dRelic):
        for iRelic in dRelic:
            oRelic = oHero.m_RelicCon.GetPerform(iRelic)
            if not oRelic:
                continue
            oRelic.Enable(oHero)
        

    
    def OnHeroAddRelic(self, _oLinstener, oTarget, dMsgInfo):
        iRelicSID = dMsgInfo['NewRelic']
        if iRelicSID in self.m_RelicWhiteList:
            return None
        dCache = self.m_HeroCache.setdefault(oTarget.m_PlayerID, { }).setdefault('Relic', { })
        dCache[iRelicSID] = 1
        dMsgInfo['Enable'] = 0

    
    def EnableWhileList(self, oHero):
        for iRelic in self.m_RelicWhiteList:
            oRelic = oHero.m_RelicCon.GetPerform(iRelic)
            if oRelic:
                oRelic.Enable(oHero, iNotify = 0)
        
        for iPerform in self.m_PerformWhiteList:
            oPerform = oHero.GetPerform(iPerform)
            if oPerform:
                oPerform.Enable(oHero, iNotify = 0)
        
        if self.m_TaskPassiveWhiteList:
            oHero.m_TaskCon.EnableTaskPerform(self.m_TaskPassiveWhiteList)
        for iBene in self.m_BeneWhiteList:
            oBene = oHero.m_BenedictionCon.GetPerform(iBene)
            if oBene:
                oBene.Enable(oHero, iNotify = 0)
        
        oWarMgr = self.m_Game.m_WarMgr
        oSeasonSuitElement = oWarMgr.GetSeasonSuitElement()
        if oSeasonSuitElement:
            for iSeasonSuit in self.m_SeasonSuitWhiteList:
                if oSeasonSuitElement.GetSuitOpenStatus(oHero, iSeasonSuit):
                    clsSuit = cl_platformdata.GetSeasonSuitCls(iSeasonSuit)
                    iGrade = oSeasonSuitElement.m_Enable[oHero.m_ID][iSeasonSuit]
                    oSeasonSuitElement.ActiveAction(clsSuit, oHero, iGrade)
            
        lstSeasonElement = oWarMgr.GetCurSeasonAllElement()
        for sElement in lstSeasonElement:
            oElement = oWarMgr.GetComponent(sElement)
            if not oElement:
                continue
            if not oElement.m_IsInheritSeasonElement:
                continue
            oElement.EnableAIWhileList(oHero)
        

    
    def DisableHeroSeasonSuit(self, oHero):
        dDisableSuit = { }
        oSeasonSuit = self.m_Game.m_WarMgr.GetSeasonSuitElement()
        if not oSeasonSuit:
            return { }
        iHero = oHero.m_ID
        if iHero not in oSeasonSuit.m_Enable:
            return { }
        for iSuitSID, iSuitGrade in oSeasonSuit.m_Enable[iHero].items():
            if iSuitGrade > 0 and oSeasonSuit.GetSuitOpenStatus(oHero, iSuitSID):
                dDisableSuit[iSuitSID] = iSuitGrade
                clsSuit = cl_platformdata.GetSeasonSuitCls(iSuitSID)
                oSeasonSuit.RemoveAction(clsSuit, oHero, iSuitGrade)
        
        return dDisableSuit

    
    def EnableHeroSeasonSuit(self, oHero, dSeasonSuit):
        oSeasonSuit = self.m_Game.m_WarMgr.GetSeasonSuitElement()
        if not oSeasonSuit:
            return None
        for iSuitSID, iSuitGrade in dSeasonSuit.items():
            if oSeasonSuit.GetSuitOpenStatus(oHero, iSuitSID):
                clsSuit = cl_platformdata.GetSeasonSuitCls(iSuitSID)
                oSeasonSuit.ActiveAction(clsSuit, oHero, iSuitGrade)
        

    
    def OnHeroActiveSeasonSuit(self, _oLinstener, oTarget, dMsgInfo):
        iSuitGrade = dMsgInfo['Grade']
        iSuitSID = dMsgInfo['SeasonSuit']
        if iSuitSID in self.m_SeasonSuitWhiteList:
            return None
        dCache = self.m_HeroCache.setdefault(oTarget.m_PlayerID, { }).setdefault('SeasonSuit', { })
        dCache[iSuitSID] = iSuitGrade
        dMsgInfo['Enable'] = 0

    
    def DisableHeroSeasonEffect(self, oHero):
        oWarMgr = self.m_WarMgr
        lstSeasonElement = oWarMgr.GetCurSeasonAllElement()
        dDisableEffect = { }
        for sElement in lstSeasonElement:
            oElement = oWarMgr.GetComponent(sElement)
            if not oElement:
                continue
            if not oElement.m_IsInheritSeasonElement:
                continue
            dEffect = oElement.DisableHeroSeasonEffect(oHero)
            dDisableEffect[sElement] = dEffect
        
        return dDisableEffect

    
    def EnableHeroSeasonEffect(self, oHero, dSeasonEffect):
        oWarMgr = self.m_WarMgr
        lstSeasonElement = oWarMgr.GetCurSeasonAllElement()
        for sElement in lstSeasonElement:
            oElement = oWarMgr.GetComponent(sElement)
            if not oElement:
                continue
            if sElement not in dSeasonEffect:
                continue
            if not oElement.m_IsInheritSeasonElement:
                continue
            oElement.EnableHeroSeasonEffect(oHero, dSeasonEffect[sElement])
        

    
    def OnLevelFinish(self, _oListener, _oWarMgr, _dMsgInfo):
        self.CollectReward()
        self.RewardRelicToAIMember(_dMsgInfo)

    
    def CollectReward(self):
        dTarget = { }
        oGame = self.m_Game
        for iHero, pid in self.m_UnderControl.items():
            if pid in self.m_AIMember:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dTarget[iHero] = 0
        
        if not dTarget:
            return None
        for iDrop in oGame.m_SceneMgr.GetAllSceneObjectsByType('Drop'):
            oDrop = oGame.GetObject(iDrop)
            if not oDrop or oDrop.m_ReleaseFlag:
                continue
            iOwner = oDrop.m_Owner
            if oDrop.m_FightType != NWARRIOR_DROP_RELIC or iOwner not in dTarget:
                continue
            oDrop.Remove(self.m_CallFlag)
            dTarget[iOwner] += 1
        
        for iHero, iRelicNum in dTarget.items():
            pid = self.m_UnderControl[iHero]
            if pid in self.m_HeroCache:
                self.m_HeroCache[pid].setdefault('RelicReward', 0)
                self.m_HeroCache[pid]['RelicReward'] += iRelicNum
                TeammateaiLog.Debug('%s %s collectrelic %s' % (self.m_Game.m_ID, pid, iRelicNum))
            dTarget[iHero] = 0
        
        for iNpc in oGame.m_SceneMgr.GetAllSceneObjectsByType('NPC'):
            oNpc = oGame.GetObject(iNpc)
            if not oNpc:
                continue
            if oNpc.m_FightType not in NWARRIOR_NPC_ALL_GOLDENCUP:
                continue
            for iHero in dTarget:
                pid = self.m_UnderControl[iHero]
                if not oNpc.IsVisibleTo(pid) or oNpc.GetPlayerInteractType(pid) == INTERACT_TYPE_FORBID or oNpc.m_IsExtraInteractRule:
                    continue
                oNpc.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                    pid])
                dTarget[iHero] += 1
            
        
        for iHero, iTalentNum in dTarget.items():
            pid = self.m_UnderControl[iHero]
            if pid not in self.m_HeroCache:
                continue
            self.m_HeroCache[pid].setdefault('TalentReward', 0)
            self.m_HeroCache[pid]['TalentReward'] += iTalentNum
            TeammateaiLog.Debug('%s %s collecttalent %s' % (self.m_Game.m_ID, pid, iTalentNum))
        

    
    def MakeUpReward(self, oHero, dCache):
        if not dCache:
            return None
        pid = oHero.m_PlayerID
        iRelicNum = dCache.pop('RelicReward', 0)
        iTalentNum = dCache.pop('TalentReward', 0)
        TeammateaiLog.Debug('%s %s makeup %s %s' % (self.m_Game.m_ID, pid, iRelicNum, iTalentNum))
        if iRelicNum:
            self.GiveRelic(oHero, iRelicNum, iCurse = 0)
        if iTalentNum:
            self.GiveTalent(oHero, iTalentNum)

    
    def RewardRelicToAIMember(self, dInfo):
        oWarMgr = self.m_WarMgr
        lstHero = oWarMgr.GetRoomHero(iCalAI = 0)
        oGame = self.m_Game
        (iTotal, iCnt) = (0, 0)
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            iTotal += oHero.m_RelicCon.GetAllRelicNum()
            iCnt += 1
        
        if not iCnt:
            return None
        iAverage = iTotal // iCnt
        for pid in self.m_AIMember:
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            iAIRelicNum = oHero.m_RelicCon.GetAllRelicNum()
            iCompensateNum = iAverage - iAIRelicNum
            if iCompensateNum <= 0:
                continue
            self.GiveRelic(oHero, iCompensateNum, iCurse = 1)
        

    
    def GiveRelic(self, oHero, iNum, iCurse):
        oGame = self.m_Game
        setAllRelic = oHero.m_RelicCon.GetAvailableRelic() - set(self.m_RelicNoChoosedList)
        if not iCurse:
            lstCurseRelic = oGame.m_WarData.GetAllCurseRelic()
            setAllRelic -= set(lstCurseRelic)
        dValid = dict.fromkeys(setAllRelic, 10)
        if not dValid:
            return None
        dValid = self.UpdateRelicChooseWeight(oHero, dValid)
        iMax = oHero.m_RelicCon.MaxRelicNum()
        for _ in range(iNum):
            iHas = oHero.m_RelicCon.GetAllRelicNum()
            if iHas >= 120:
                break
            if iMax and iHas >= iMax:
                break
            iRelic = ChooseKey(oGame, dValid)
            if iRelic:
                dValid.pop(iRelic)
                oHero.m_RelicCon.AddRelic(iRelic, 'ai')
            if not dValid:
                break
        

    
    def UpdateRelicChooseWeight(self, oHero, dWeight):
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in self.m_AIMember:
            return dWeight
        oSeasonSuitElement = self.m_WarMgr.GetSeasonSuitElement()
        if not oSeasonSuitElement:
            return dWeight
        for iRelic in oSeasonSuitElement.GetAllLackRelic(oHero):
            if iRelic in dWeight:
                dWeight[iRelic] = self.m_SeasonSuitRelicWeight
        
        return dWeight

    
    def GiveTalent(self, oHero, iTalentNum):
        oGame = self.m_Game
        oTalentCon = oHero.m_TalentCon
        dValid = dict.fromkeys(oTalentCon.GetAllValidTalent(iUseLib = 1, iExcludeCurTalent = 0), 100)
        for _ in range(iTalentNum):
            if not dValid:
                break
            iTalent = ChooseKey(oGame, dValid)
            if not iTalent:
                break
            oTalent = oTalentCon.GetPerform(iTalent)
            if not oTalent:
                iLevel = 1
            else:
                iLevel = oTalent.Level() + 1
            oTalent = oTalentCon.AddTalent(iTalent, iLevel, 'ai')
            if oTalent and oTalent.m_Level >= oTalent.m_MaxLevel:
                dValid.pop(iTalent)
        

    
    def RewardBeneToAIMember(self, oLevelCtrl, dMsgInfo):
        if not self.m_AIMember:
            return None
        if 'LevelType' not in dMsgInfo or not (dMsgInfo['LevelType'] == LEVEL_TYPE_HALL):
            return None
        oGame = self.m_Game
        if not oGame.m_WarMgr.IsCycleWar():
            return None
        iLayer = oLevelCtrl.m_LayerNum
        if iLayer not in self.m_RewardBeneLayer:
            return None
        for pid in self.m_AIMember:
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            lstHasBene = oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER)
            if len(lstHasBene) >= MAX_BENE_CNT:
                continue
            bChosen = False
            for oBenediction in lstHasBene:
                if oBenediction.m_Layer == iLayer:
                    bChosen = True
                    break
            
            if bChosen:
                continue
            dWeight = { }
            iHeroSID = oHero.m_SID
            if iHeroSID in self.m_AIMemberChooseBene and iLayer in self.m_AIMemberChooseBene[iHeroSID]:
                dWeight = self.m_AIMemberChooseBene[iHeroSID][iLayer]
                dWeight = DealBeneWeight(oHero, dWeight, lstExclude = [])
            if not dWeight:
                dWeight = cl_perform.load.GetBenedictionLibrary()
                dWeight = DealBeneWeight(oHero, dWeight, lstExclude = [])
            if not dWeight:
                lstHas = oHero.m_BenedictionCon.GetAllPerformSID()
                TeammateaiLog.Error('%s %s %s no enough bene %s' % (oGame.m_ID, oHero.m_PlayerID, iLayer, lstHas))
                continue
            iSID = ChooseKey(oGame, dWeight)
            TeammateaiLog.Debug('%s %s addbene %s' % (oGame.m_ID, oHero.m_PlayerID, iSID))
            oBenediction = oHero.m_BenedictionCon.AddBenediction(iSID, 1, 'AIMember')
            if oBenediction and iSID not in self.m_BeneWhiteList:
                oBenediction.Disable(oHero, iNotify = 0)
        

    
    def EnableAIPerform(self, oHero):
        if oHero.m_ID not in self.m_HeroInitPassive:
            self.m_HeroInitPassive[oHero.m_ID] = self.GetHeroInitPassive(oHero)
        lstAddInit = self.m_HeroInitPassive[oHero.m_ID]
        TeammateaiLog.Debug('%s %s addpf %s' % (self.m_Game.m_ID, oHero.m_SID, lstAddInit))
        for iPassive in lstAddInit:
            oHero.m_Perform.AddPerform(oHero, iPassive, 1, iEnable = 1, iItem = 0)
        
        iHeroGrade = oHero.m_PlayerGrade
        dAITalent = cl_platformdata.GetAITalentByHeroGrade(iHeroGrade)
        TeammateaiLog.Debug('%s %s aitalent %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iHeroGrade, dAITalent))
        for iTalent, iLevel in dAITalent.items():
            oHero.m_Perform.AddPerform(oHero, iTalent, iLevel, iEnable = 1, iItem = 0)
        

    
    def DisableAIPerform(self, oHero):
        lstRemoveInit = self.m_HeroInitPassive[oHero.m_ID]
        TeammateaiLog.Debug('%s %s delpf %s' % (self.m_Game.m_ID, oHero.m_SID, lstRemoveInit))
        for iPassive in lstRemoveInit:
            oHero.m_Perform.RemovePerform(oHero, iPassive)
        
        iHeroGrade = oHero.m_PlayerGrade
        dAITalent = cl_platformdata.GetAITalentByHeroGrade(iHeroGrade)
        for iTalent in dAITalent:
            oHero.m_Perform.RemovePerform(oHero, iTalent)
        

    
    def GetHeroInitPassive(self, oHero):
        iAIHeroSID = oHero.m_SID
        lstInitPassive = list(self.m_HeroBasicPassive)
        if iAIHeroSID in self.m_HeroPassive:
            lstPassive = self.m_HeroPassive[iAIHeroSID]
            lstInitPassive.extend(lstPassive)
        for iPassive in lstInitPassive:
            clsPerform = cl_perform.GetPerformModule(iPassive)
            if not not clsPerform:
                if not (clsPerform.m_PFType & PF_TYPE_PASSIVE):
                    TeammateaiLog.Alert('%s %s no passive %s' % (self.m_Game.m_ID, oHero.m_SID, iPassive))
                    lstInitPassive.pop(iPassive)
                    continue
        
        return lstInitPassive

    
    def DisableWeapon(self, oHero):
        dValid = { }
        lstItem = oHero.m_WieldCon.GetAllItem()
        for oWeapon in lstItem:
            if oWeapon.IsInitWeapon():
                continue
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            if oInscriptionCom:
                oInscriptionCom.OnItemRemoveFromContainer(oWeapon, oHero)
            oEnhanceCom = oWeapon.GetComponent('Enhance')
            if oEnhanceCom:
                oEnhanceCom.DisableItemEnhance()
            if oWeapon.m_SID in self.m_WeaponInfo:
                dValid[oWeapon.m_Pos] = 1
        
        if dValid:
            iPos = ChooseKey(self.m_Game, dValid)
        else:
            oFundWeapon = oHero.m_WieldCon.GetItemByType(EQUIP_TYPE_FUNDAMENTALWEAPON)
            iPos = oFundWeapon.m_Pos
        oHero.m_WieldCon.SetCurWeapon(iPos, CURWEAPON_SWITCH)

    
    def EnableWeapon(self, oHero):
        lstItem = oHero.m_WieldCon.GetAllItem()
        for oWeapon in lstItem:
            if oWeapon.IsInitWeapon():
                continue
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            if oInscriptionCom:
                oInscriptionCom.OnItemAddToContainer(oWeapon, oHero)
            oEnhanceCom = oWeapon.GetComponent('Enhance')
            if oEnhanceCom:
                oEnhanceCom.OnItemAddToContainer(oWeapon, oHero)
        

    
    def UpdateWeapon(self):
        oGame = self.m_Game
        dWeapon = self.m_WeaponInfo
        if not dWeapon:
            return None
        iGrade = cl_reward.GetWeaponRewardGrade(oGame)
        oSkillMgr = oGame.m_SkillMgr
        for iHero, pid in self.m_UnderControl.items():
            if pid not in self.m_AIMember:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero or oHero.IsRealDied():
                continue
            iWeaponSID = ChooseKey(oGame, dWeapon)
            oWeapon = cl_item.CreateEquip(oGame, iWeaponSID, iGrade, oOwner = oHero)
            if not oWeapon:
                continue
            oCon = oHero.m_WieldCon
            iUseNewWeapon = 1
            if not oCon.GetValidPos(oWeapon):
                lstPos = oCon.ItemValidPosByItem(oWeapon)
                if not lstPos:
                    continue
                iTargetPos = ChooseKey(oGame, dict.fromkeys(lstPos, 1))
                oCur = oCon.GetItemByPos(iTargetPos)
                if oCur:
                    iPerform = oCur.GetWeaponPerformByType(WEAPON_MAIN_PERFORM)
                    oSkill = oSkillMgr.GetSkillBySource(iPerform, iHero, oCur.m_ID)
                    if oSkill:
                        oSkill.Halt()
                    oCon.RemoveItem(oCur, 'AI')
                iUseNewWeapon = 0
            oWeapon.PutToContainer([
                oCon], 'AI')
            lstWeapon = oCon.GetAllItemByMask(EQUIP_MASK_WEAPON)
            if not lstWeapon:
                continue
            for oWeapon in lstWeapon:
                oInscriptionCom = oWeapon.GetComponent('Inscription')
                if oInscriptionCom:
                    oInscriptionCom.OnItemRemoveFromContainer(oWeapon, oHero)
            
            if iUseNewWeapon:
                iUsePos = oWeapon.m_Pos
            else:
                iUsePos = ChooseKey(oGame, dict.fromkeys([ oWeapon.m_Pos for oWeapon in lstWeapon ], 1))
            oCon.SetCurWeapon(iUsePos, CURWEAPON_SWITCH)
        

    
    def TryResetHeroLife(self, oHero):
        if oHero.IsDying():
            oDieElement = self.m_WarMgr.GetComponent('PVEDieElement')
            if not oDieElement:
                return None
            dReason = {
                'Type': TYPE_RELIFE_PASS,
                'AID': oHero.m_ID }
            dRelifeInfo = {
                'HP': max(100, oHero.QueryAttr('HPMax') * 20 // 100),
                'Shield': oHero.QueryAttr('ShieldMax') * 20 // 100,
                'Armor': oHero.QueryAttr('ArmorMax') * 20 // 100 }
            oDieElement.DirectHeroRelife(oHero, dReason, dRelifeInfo)
        elif oHero.IsRealDied():
            oHero.m_Agent.PauseAgent('Die')
        else:
            oHero.m_HP = oHero.QueryAttr('HPMax')
            oHero.GS2CPropChange('HP')
            oHero.m_Shield = oHero.QueryAttr('ShieldMax')
            oHero.GS2CPropChange('Shield')
            oHero.m_Armor = oHero.QueryAttr('ArmorMax')
            oHero.GS2CPropChange('Armor')

    
    def OnDie(self, _oLinstener, oTarget, _dMsgInfo):
        if oTarget.m_ID in self.m_UnderControl:
            return None
        iNowFrame = oTarget.m_Game.GetFrameNum()
        self.m_HeroDieInfo[oTarget.m_ID].insert(0, iNowFrame)

    
    def OnDiedist(self, _oLinstener, oTarget, _dMsgInfo):
        pid = oTarget.m_PlayerID
        if pid in self.m_AIMember:
            dInfo = self.m_AIMember[pid]
            if 'Diedist' in dInfo:
                dInfo['Diedist'] += 1
            else:
                dInfo['Diedist'] = 1
        lstNeed = self.GetAIHeroByFollowTarget(oTarget.m_ID)
        self.UpdateFollowTarget(lstNeed, oTarget.m_ID)

    
    def OnHeroRelife(self, _oLinstener, oTarget, _dMsgInfo):
        if not self.m_UnderControl:
            return None
        iTarget = oTarget.m_ID
        if iTarget in self.m_UnderControl:
            return None
        if iTarget in self.m_FollowTarget.values():
            return None
        lstLiveHero = self.m_WarMgr.GetLiveHero(iCalAI = 0)
        if iTarget in lstLiveHero:
            return None
        lstLiveHero.append(iTarget)
        self.AssignFollowTarget(lstLiveHero)

    
    def GetAIHeroByFollowTarget(self, iTarget):
        lstAIHero = []
        for iAIHero, iHero in self.m_FollowTarget.items():
            if iHero == iTarget:
                lstAIHero.append(iAIHero)
        
        return lstAIHero

    
    def RecordOnePlayerDamage(self, iPlayer):
        oWarMgr = self.m_WarMgr
        oReport = oWarMgr.GetComponent('Warreport')
        if not oReport:
            return None
        if iPlayer in self.m_AIMember:
            return None
        oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
        if not oHero:
            return None
        if iPlayer in self.m_HeroTotalDamage:
            dDamage = self.m_HeroTotalDamage[iPlayer]
        else:
            dDamage = {
                'RealMan': 0,
                'AI': 0 }
        iPreAIDamage = dDamage['RealMan']
        iAIDamage = dDamage['AI']
        iAllDamage = iPreAIDamage + iAIDamage
        iTotalAllDamage = oReport.GetTotalDamageByHeroID(oHero.m_ID)
        iAddDamage = iTotalAllDamage - iAllDamage
        if self.CheckIsAI(oHero.m_ID, oHero.Online()):
            dDamage['AI'] += iAddDamage
        else:
            dDamage['RealMan'] += iAddDamage
        self.m_HeroTotalDamage[iPlayer] = dDamage

    
    def GetHeroDamage(self, iPlayer):
        if iPlayer not in self.m_HeroTotalDamage:
            return (-1, -1)
        self.RecordOnePlayerDamage(iPlayer)
        dDamage = self.m_HeroTotalDamage[iPlayer]
        if not dDamage['AI']:
            return (-1, -1)
        return (dDamage['RealMan'] // 100, dDamage['AI'] // 100)

    
    def CheckIsAI(self, iHeroID, iOnline = LINK_ONLINE):
        if iHeroID in self.m_UnderControl and iOnline in (LINK_DELEGATE, LINK_ACTIVEDELEGATE):
            return 1
        return 0

    
    def OnNpcCreateOver(self, _oLinstener, oNpc, dMsgInfo):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        if oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
            return None
        if oNpc.m_FightType not in GetAIShareSignalFightType():
            return None
        if oNpc.m_FightType == NWARRIOR_NPC_TRANSFER and oNpc.m_TransferDir != TRANSFER_DIRTO_HIDE:
            return None
        self.m_ShareItem[oNpc.m_ID] = 1

    
    def OnMonsterDie(self, _oLinstener, oMonster, dMsgInfo):
        iFightType = oMonster.m_FightType
        if iFightType & WARRIOR_BOSS != WARRIOR_BOSS or iFightType in BOSS_DONOT_COUNT:
            return None
        if not self.m_UnderControl:
            return None
        oGame = self.m_Game
        if not oGame.Random(100) < self.m_BossShareDropProb:
            return None
        iCount = ChooseKey(oGame, self.m_BossShareDropCnt)
        if not iCount:
            return None
        iAIHero = ChooseKey(oGame, dict.fromkeys(self.m_UnderControl, 10))
        oAIHero = oGame.GetObject(iAIHero)
        iAIPlayer = oAIHero.m_PlayerID
        dMGReward = { }
        for _ in range(iCount):
            iMiniGame = ChooseKey(oGame, self.m_BossShareDropMG)
            if iMiniGame in dMGReward:
                (iProb, iCount) = dMGReward[iMiniGame]
                dMGReward[iMiniGame] = (iProb, iCount + 1)
                continue
            dMGReward[iMiniGame] = (10000, 1)
        
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 0,
            'Abandoner': oMonster.m_ID,
            'CanReward': 0,
            'AutoReward': 0,
            'OnlyRewardAttack': 1 }
        dMGInfo = cl_reward.RewardItemByMiniGame(oMonster, iAIHero, dMGReward, 'TeammateAIKillBoss', MG_SOURCE_AIKILLBOSS, dExtInfo)
        iScene = oMonster.m_Scene
        dExtraInfo = {
            'Abandoner': iAIHero,
            'DropReason': 0 }
        dStaticInfo = {
            'DropSource': iAIPlayer }
        for _, dInfo in dMGInfo.items():
            for iMiniGame, lstInfo in dInfo.items():
                (_, lstReward, dExtInfo) = lstInfo
                for dReward in lstReward:
                    dDropInfo = dReward['info']
                    oDrop = oGame.m_ResMgr.CreateDrop(iScene, dDropInfo['DropType'], dDropInfo['DropPos'], dDropInfo['DropInfo'], dExtraInfo, dStaticInfo, iOwner = iAIHero, iSplit = 0)
                    if oDrop:
                        self.m_ShareItem[oDrop.m_ID] = 1
                
            
        

    
    def AddHideDoorShareItem(self, oLevelCtrl):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oLevelCtrl.m_CurNode.m_Scene)
        for oid in oScene.GetObjectsByType('Obstacle'):
            oBuild = oGame.GetObject(oid)
            if not oBuild:
                continue
            if not oBuild.Query('HideLevel'):
                continue
            self.m_ShareItem[oBuild.m_ID] = 1
        

    
    def GetHideDoorNpc(self):
        oGame = self.m_Game
        for iItem in self.m_ShareItem:
            oItem = oGame.GetObject(iItem)
            if not oItem:
                continue
            if oItem.m_FightType == NWARRIOR_NPC_TRANSFER and oItem.m_TransferDir == TRANSFER_DIRTO_HIDE:
                return iItem
        
        return 0

    
    def GetNearestShareItem(self, oHero, iCheckDis):
        if not self.m_ShareItem:
            return 0
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
        if not oScene:
            return 0
        iCurLevel = oScene.m_Level
        oLevelNode = oLevelCtrl.GetLevelNode(iCurLevel)
        if not oLevelNode:
            return 0
        iMinDis = 99999
        iNearestItem = 0
        dDis = oGame.Scene_GetTargetDisMap(oHero.m_ID, list(self.m_ShareItem))
        for iItemID, iDis in dDis.items():
            oItem = oGame.GetObject(iItemID, PY_FLAG_DEAD)
            if not oItem:
                continue
            if oItem.m_LineIdx:
                (iLevel, iRoom, _) = oItem.m_LineIdx
                if iLevel != iCurLevel:
                    continue
                if iRoom > oLevelNode.m_CurRoomPos:
                    continue
                continue
            if not oItem.CanSharedByAI(oHero):
                continue
            if oItem.m_FightType in [
                NWARRIOR_DROP_RELIC,
                NWARRIOR_DROP_EQUIP]:
                return iItemID
            if iDis > iCheckDis or iDis > iMinDis:
                continue
            iMinDis = iDis
            iNearestItem = iItemID
        
        return iNearestItem

    
    def RemoveShareItem(self, iItem):
        self.m_ShareItem.pop(iItem, 0)



def GetComponentClass(oWarMgr):
    return CTeammateAIElement

