# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/mobject.pyc
# RelativePath: clientlogic/cl_warmgr/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import GAME_FRAME, SendAlert, Functor, Time2Frame, PythonError, Frame2Time, DeepCopy, ChooseKey
from cl_commondefines import MODE_WEAPONSTORE, BIGDATA_BOSS_PHASE, SETTLE_DIRECTLEAVE, LEVEL_TYPE_NONE, SETTLE_SYSKICK, SETTLE_MASTERLEAVE, SETTLE_TRANSFER, LEAVE_TYPE_NORECORDE, SETTLE_FINISHWAR, SETTLE_LOSEWAR, STATE_DYING, DIFFICULTY_ADVANCE_CYCLE, DIFFICULTY_COMMON_ROUND, PLAY_TYPE_MULTI, PLAY_TYPE_SINGLE, GetPlayMode, SETTLE_OVER_NORMAL, LEVEL_TYPE_BOSS, SETTLE_HANGUP, ENDLESS_TIME, MODE_REAL_ENDLESS, PF_TYPE_RELIC, MODE_SNOWMOUNTAINS
from cl_commondefines import VOTE_CONTINUE, ROUND_MAX, LEVEL_TYPE_FIGHT, PLAYMODE_MOBILE_DEMO, MODETYPE_TO_ELEMENT, ALL_MODETYPE, SUIT_RELIC, PLAYMODE_ROGUELIKE, PLAYMODE_SURVIVOR, ADJUST_RELIC, TYPE_REMOVE, TYPE_REPLACE, BENE_SOURCE_LAYER, PLAYMODE_NEWSURVIVOR
from cl_cscommondef import GetMaxCycle
from cl_chatinfo import GS2CShowText
from cl_object.logging import FightserverLog, WarobjLog, SeasonLog
from cllib.lib_only import RunMobileData, log_file_long
from cl_season import GetSeasonNumByPlayMode, GetOldSeasonPutInfo, IsUseDefaultSeasonByPlayMode, GetEnableSeasonPlayRound, IsAssignSeason, GetSeasonVersion
import time
import itertools
import cl_hero
import cl_world
import cl_object.timeunit
import cl_object.reason
import cl_notify
import cl_msgcenter
import cl_snetwar
import cl_cnetwar
import cli_player
import cl_item.load
import cl_platformdata
import cl_perform.load
import cl_item.defines as itemdef
import cllib.lib_server as lib_server
import cllib.lib_flag as lib_flag
import cl_putdata
import cl_anima

class CWarManager(cl_world.CEventObject):
    m_InitStep = []
    m_StepInfo = { }
    m_SID = 0
    m_ComponentCls = { }
    m_UseMasterTransfer = 1
    m_SaveElement = [
        'EndlessElement',
        'MonsterRelicElement',
        'TalentFusionElement',
        'WeaponStoreElement',
        'TeammateAI',
        'RealEndlessElement',
        'RelicTalentElement',
        'SuitElement',
        'ConquerElement',
        'NewbieTutorialElement',
        'SeasonSuitElement',
        'RegroupRelicElement',
        'TaskElement',
        'WandElement',
        'WatchElement',
        'DiceElement',
        'BackpackElement']
    m_SaveSeedElement = [
        'SuitElement',
        'SeasonSuitElement',
        'MonsterRelicElement',
        'EndlessElement',
        'RealEndlessElement']
    m_SeasonFuncConfing = { }
    m_SeasonElement = { }
    m_NewVerLayer = set()
    m_AllSeasonElement = { }
    
    def __init__(self, oGame, nid):
        super(CWarManager, self).__init__(oGame, nid)
        self.m_TimeUnit = cl_object.timeunit.CWarMgrTimeUnit(self)
        self.m_Component = { }
        self.m_Data = { }
        self.m_PlayerMask = {
            'All': { },
            'Live': { },
            'Room': { },
            'Hero': { },
            'LiveHero': { } }
        self.m_SettledPlayer = { }
        self.m_PlayType = 0
        self.m_ReportID = ()
        self.m_Round = 1
        self.m_Cycle = 0
        self.m_MaxRoundInfo = (1, 0, 0)
        self.m_MaxLayer = 0
        self.m_WarMask = ''
        self.m_RefreshPlayerCnt = 0
        self.m_IsTransfer = False
        self.m_QuittedPlayerInfo = { }
        self.m_WarMaster = 0
        self.m_Leader = 0
        self.m_ExtraInfo = { }
        self.m_DelayRemove = 0
        self.m_PlayMode = GetPlayMode(self.m_SID)
        self.m_IsUseRecord = False
        self.m_ModeType = []
        self.m_PutRelic = set()
        self.m_ForbidRelic = set()
        self.m_SeasonNum = 0
        self.m_WarStartSeason = GetSeasonVersion()
        self.m_DropGroup = { }
        self.m_DropGroupIdx = 0
        self.m_BigDataHero = []

    
    def Set(self, key, value):
        self.m_Data[key] = value

    
    def SetDefault(self, key, value):
        if key not in self.m_Data:
            self.m_Data[key] = value
            return value
        return self.m_Data[key]

    
    def Add(self, key, value):
        if key in self.m_Data:
            self.m_Data[key] += value
        else:
            self.m_Data[key] = value

    
    def Query(self, key, default = 0):
        if key in self.m_Data:
            default = self.m_Data[key]
        return default

    
    def UniqueSet(self, key, value):
        if key in self.m_Data:
            WarobjLog.Alert('warmgr save the same key: %s' % key)
            return None
        self.m_Data[key] = value

    
    def Delete(self, key):
        if key in self.m_Data:
            del self.m_Data[key]

    
    def Save(self):
        dData = {
            'ExtraInfo': self.m_ExtraInfo,
            'ModeType': self.m_ModeType,
            'Settled': dict(self.m_SettledPlayer),
            'WarStartSeason': self.m_WarStartSeason }
        for sElementType in self.m_SaveElement:
            oElement = self.GetComponent(sElementType)
            if oElement:
                dData[sElementType] = oElement.Save()
        
        return dData

    
    def Load(self, dData):
        self.m_SettledPlayer.update(dData.get('Settled', { }))
        for sElementType in self.m_SaveElement:
            if sElementType not in dData:
                continue
            oElement = self.GetComponent(sElementType)
            if not oElement:
                oElement = self.OpenElement(sElementType)
            if oElement:
                oElement.Load(dData[sElementType])
        
        self.m_WarStartSeason = dData.get('WarStartSeason', 0)

    
    def SaveSeed(self, oHero):
        dData = {
            'ExtraInfo': self.m_ExtraInfo,
            'ModeType': self.m_ModeType,
            'Round': (self.m_Round, self.m_Cycle),
            'WarStartSeason': self.m_WarStartSeason }
        for sElementType in self.m_SaveSeedElement:
            oElement = self.GetComponent(sElementType)
            if oElement:
                dData[sElementType] = oElement.SaveSeed(oHero)
        
        return dData

    
    def LoadSeed(self, dData):
        if not dData:
            return None
        dExtraInfo = dData.get('ExtraInfo', { })
        lstModeType = dData.get('ModeType', [])
        self.m_ExtraInfo = dExtraInfo
        self.m_ModeType = lstModeType
        if 'Season' in self.m_ExtraInfo:
            self.m_SeasonNum = self.m_ExtraInfo['Season']
        for sElementType, oElement in dict(self.m_Component).items():
            if not self.IsOpenElement(sElementType):
                oElement.Release()
                self.m_Component.pop(sElementType)
        
        lstElement = self.GetModeTypeToElement(lstModeType)
        for sElementType in itertools.chain(lstElement, self.m_SeasonElement.get(self.m_SeasonNum, [])):
            oElement = self.GetComponent(sElementType)
            if not oElement:
                oElement = self.OpenElement(sElementType)
            if sElementType not in dData:
                continue
            if sElementType in self.m_SaveElement and oElement:
                oElement.LoadSeed(dData[sElementType])
        

    
    def Release(self):
        for iHero in self.GetAllHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                oHero.LeaveGame()
        
        for pid in self.m_PlayerMask['Hero']:
            oHero = self.GetHeroByPlayer(pid)
            if not oHero:
                continue
            oHero.Remove('gameend')
        
        self.m_TimeUnit.Release()
        self.m_TimeUnit = None
        for oElement in self.m_Component.values():
            oElement.Release()
        
        self.m_Component = { }
        self.m_Data = { }
        super(CWarManager, self).Release()

    
    def InitWarInfo(self, dInfo, dPlayerInfo):
        self.m_PlayType = PLAY_TYPE_SINGLE if len(dPlayerInfo) == 1 else PLAY_TYPE_MULTI
        self.m_ReportID = dInfo['ReportID']
        self.ValidInitWarInfo(dInfo)
        self.m_Round = dInfo['Round']
        self.m_Cycle = dInfo['Cycle']
        self.m_MaxRoundInfo = dInfo['MaxRoundInfo'] if 'MaxRoundInfo' in dInfo else (self.m_Round, self.m_Cycle, 0)
        if 'ExtraInfo' in dInfo and dInfo['ExtraInfo']:
            self.m_ExtraInfo = dInfo['ExtraInfo']
            if 'CloseElement' in self.m_ExtraInfo:
                lstModeType = self.m_ExtraInfo['CloseElement']
                self.RemoveModeTypeBySubModeType(dInfo['ModeType'], lstModeType)
                self.m_ExtraInfo['CloseElement'] = self.GetModeTypeToElement(lstModeType)
            if 'Season' in self.m_ExtraInfo:
                self.m_SeasonNum = self.m_ExtraInfo['Season']
        self.m_ModeType = dInfo['ModeType']
        WarobjLog.Debug('%s initwar %s %s %s' % (self.m_Game.m_ID, self.m_ModeType, self.m_ExtraInfo, self.m_SeasonNum))

    
    def ValidInitWarInfo(self, dInfo):
        if dInfo['Round'] > ROUND_MAX:
            WarobjLog.Warn('game: %d initwarinfo round %d' % (self.m_Game.m_ID, dInfo['Round']))
            dInfo['Round'] = ROUND_MAX
        if dInfo['Round'] < 1:
            WarobjLog.Warn('game: %d initwarinfo round %d' % (self.m_Game.m_ID, dInfo['Round']))
            dInfo['Round'] = 1
        if self.m_PlayMode == PLAYMODE_SURVIVOR:
            dInfo['Round'] = 1
            if 'MaxRoundInfo' in dInfo:
                dInfo['MaxRoundInfo'] = (*(1,), *dInfo['MaxRoundInfo'][:1])
        iCycle = dInfo.setdefault('Cycle', 0)
        iMaxCycle = GetMaxCycle(dInfo['Round'])
        if dInfo['Cycle'] < 0:
            dInfo['Cycle'] = 0
            WarobjLog.Warn('game: %d initwarinfo cycle is negative number %d' % (self.m_Game.m_ID, iCycle))
        if dInfo['Cycle'] > iMaxCycle:
            dInfo['Cycle'] = iMaxCycle
            WarobjLog.Warn('game: %d initwarinfo cycle illegal %d %d' % (self.m_Game.m_ID, dInfo['Round'], iCycle))
        lstMode = dInfo.setdefault('ModeType', [])
        if lstMode:
            if self.m_PlayMode != PLAYMODE_ROGUELIKE or dInfo['Cycle'] == 0:
                dInfo['ModeType'] = []
                WarobjLog.Warn('game: %d initwarinfo lstmode illegal %s %d' % (self.m_Game.m_ID, lstMode, iCycle))
        iCurSeasonNum = GetSeasonNumByPlayMode(self.m_PlayMode)
        dExtraInfo = dInfo.setdefault('ExtraInfo', { })
        if dExtraInfo is None:
            dExtraInfo = { }
        if 'Season' in dExtraInfo:
            iSeason = dExtraInfo['Season']
            if self.m_PlayMode == PLAYMODE_ROGUELIKE:
                if not self.CheckSeasonFightData(dExtraInfo, iSeason, iCurSeasonNum, dInfo['Round']):
                    WarobjLog.Warn('game: %d initwarinfo season illegal %s %d ' % (self.m_Game.m_ID, iSeason, dInfo['Round']))
                    dExtraInfo['Season'] = iCurSeasonNum
            elif IsUseDefaultSeasonByPlayMode(self.m_PlayMode) or iSeason != iCurSeasonNum:
                WarobjLog.Warn('game: %d default season illegal %s %d' % (self.m_Game.m_ID, iSeason, iCurSeasonNum))
                dExtraInfo['Season'] = iCurSeasonNum
            else:
                WarobjLog.Warn('game: %d playmode: %d no season' % (self.m_Game.m_ID, self.m_PlayMode))
                dExtraInfo['Season'] = 0
        elif self.m_PlayMode == PLAYMODE_ROGUELIKE:
            WarobjLog.Debug('game: %d no season %s' % (self.m_Game.m_ID, dInfo))
            dExtraInfo['Season'] = 0
        elif IsUseDefaultSeasonByPlayMode(self.m_PlayMode):
            WarobjLog.Debug('game: %d playmode season %d' % (self.m_Game.m_ID, iCurSeasonNum))
            dExtraInfo['Season'] = iCurSeasonNum

    
    def CheckSeasonFightData(self, dExtraInfo, iSeason, iCurSeasonNum, iCurRound):
        dPut = GetOldSeasonPutInfo()
        if lib_flag.g_IsAuthorityRun and iSeason in dPut:
            return True
        iEnableRound = GetEnableSeasonPlayRound()
        
        try:
            if iSeason and iSeason != iCurSeasonNum:
                if not dPut.get(iSeason, 0):
                    return False
                if iCurRound != iEnableRound:
                    return False
        except:
            WarobjLog.Alert('%d seasondata err %s %s' % (self.m_Game.m_ID, iSeason, dExtraInfo))
            return False

        return True

    
    def InitWar(self):
        self.InitStep()
        self.OnWarInit(self.m_Game)

    
    def InitPlayer(self, dPlayerInfo):
        self.CheckUseRecordGame(dPlayerInfo)
        self.CheckTransferGame(dPlayerInfo)
        self.CheckAndSetWarMaster(dPlayerInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_PREADDPLAYER, self, {
            'CreateInfo': dPlayerInfo })
        for pid, dInfo in dPlayerInfo.items():
            self.AddPlayer(pid, dInfo)
        
        self.OnInitPlayer(dPlayerInfo)
        self.InitUseSealedInscription(dPlayerInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self, {
            'CreateInfo': dPlayerInfo })
        self.m_RefreshPlayerCnt = self.GetAllPlayerCnt()
        if self.IsTransferGame() and not self.GetAllAIHero():
            self.m_RefreshPlayerCnt += 1
        self.InitMaxLayer(dPlayerInfo)
        self.InitWarMask(dPlayerInfo)

    
    def OnReady(self, pid):
        pass

    
    def AddPlayer(self, pid, dInfo):
        iNpcID = self.m_Game.NewNPCID()
        oCtrlHero = cl_hero.NewCtrlHero(self.m_Game, iNpcID, pid, dInfo['CurHero'], dInfo['HeroGrade'], dInfo['Grade'])
        iSide = dInfo['Side']
        self.m_PlayerMask['All'][pid] = {
            'LGS': dInfo['LGS'],
            'Acc': dInfo.get('Account', 0) }
        self.m_PlayerMask['Hero'][pid] = iNpcID
        self.m_PlayerMask['Live'][pid] = 1
        self.m_PlayerMask['Room'][pid] = 1
        self.m_PlayerMask['LiveHero'][pid] = iNpcID
        oCtrlHero.SetSide(iSide)
        self.OnAddPlayer(oCtrlHero, dInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_ADDPLAYER, self, {
            'pid': pid,
            'Hero': iNpcID,
            'CreateInfo': dInfo,
            'oCtrlHero': oCtrlHero })

    
    def RemovePlayer(self, pid, iNowDisconnect, iForce = 0):
        if pid not in self.m_PlayerMask['Room'] and not iForce:
            return None
        oCtrlHero = self.GetHeroByPlayer(pid)
        if oCtrlHero:
            oCtrlHero.LeaveGame()
        self.m_PlayerMask['Room'].pop(pid, 0)
        self.RemoveLivePlayer(pid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self, {
            'pid': pid,
            'Hero': oCtrlHero.m_ID })
        lib_server.LogicKickOut(self.m_Game.m_ID, pid, iNowDisconnect)

    
    def ReAddPlayer(self, pid):
        oCtrlHero = self.GetHeroByPlayer(pid)
        if not oCtrlHero:
            WarobjLog.Alert('%s readdfail %s %s' % (self.m_Game.m_ID, pid, self.GetAllPlayer()))
            return None
        self.m_PlayerMask['Room'][pid] = 1
        if not oCtrlHero.IsRealDied():
            self.AddLivePlayer(pid)
        if self.m_PlayType != PLAY_TYPE_MULTI:
            self.m_PlayType = PLAY_TYPE_MULTI
            for iRoomPlayer in self.GetRoomPlayer():
                if iRoomPlayer == pid:
                    continue
                cl_snetwar.GS2CPlayType(self.m_Game, iRoomPlayer)
            
            oWatch = self.OpenElement('WatchElement')
            if oWatch:
                oWatch.OnHalfOpen()

    
    def RemoveLivePlayer(self, pid):
        self.m_PlayerMask['Live'].pop(pid, 0)
        self.m_PlayerMask['LiveHero'].pop(pid, 0)

    
    def AddLivePlayer(self, pid):
        iHero = self.GetHeroIDByPlayerID(pid)
        if iHero:
            self.m_PlayerMask['LiveHero'][pid] = iHero
        if pid not in self.m_PlayerMask['Room']:
            WarobjLog.Info('game: %d pid: %d unexist in room' % (self.m_Game.m_ID, pid))
            return None
        if pid not in self.m_PlayerMask['Live']:
            self.m_PlayerMask['Live'][pid] = 1

    
    def GetHeroByPlayer(self, pid):
        if pid not in self.m_PlayerMask['Hero']:
            return None
        iHero = self.m_PlayerMask['Hero'][pid]
        return self.m_Game.GetObject(iHero)

    
    def GetRoomHeroByPlayer(self, pid):
        if pid not in self.m_PlayerMask['Room']:
            return None
        iHero = self.m_PlayerMask['Hero'][pid]
        return self.m_Game.GetObject(iHero)

    
    def InitStep(self):
        for idx in self.m_InitStep:
            self.DoStep(idx)
        

    
    def AddStep(self, idx, iCallTime):
        pass

    
    def DoStep(self, idx):
        if idx not in self.m_StepInfo:
            return None
        func = self.m_StepInfo[idx]
        func(self)

    
    def InitElement(self):
        for sType, lstData in self.m_ComponentCls.items():
            if not self.IsOpenElement(sType):
                continue
            iID = self.m_Game.NewNPCID()
            (elefunc, oData) = lstData
            clsElement = elefunc(self)
            oElement = clsElement(self.m_Game, iID, oData)
            self.m_Game.CreateObject(iID, oElement)
            self.m_Component[sType] = oElement
            oElement.Init()
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_INITELEMENT, self, {
                'element': sType })
        
        for oElement in list(self.m_Component.values()):
            oElement.InitAfter()
        

    
    def GetComponent(self, sType):
        if sType not in self.m_Component:
            return None
        return self.m_Component[sType]

    
    def GetComponentBySeasonFunc(self, iSeasonFunc):
        dSeasonFuncConfing = self.m_SeasonFuncConfing
        if iSeasonFunc not in dSeasonFuncConfing:
            return None
        sType = dSeasonFuncConfing[iSeasonFunc]
        if sType not in self.m_Component:
            return None
        return self.m_Component[sType]

    
    def IsOpenSeasonElement(self):
        iSeason = self.m_SeasonNum
        if iSeason not in self.m_SeasonElement:
            return 0
        lstSeason = self.m_SeasonElement[iSeason]
        for sSeason in lstSeason:
            oSeasonTalentElement = self.GetComponent(sSeason)
            if not not oSeasonTalentElement:
                if not (oSeasonTalentElement.m_Enable):
                    return 0
        
        return 1

    
    def IsOpenElement(self, sType, bForce = False):
        if lib_flag.g_IsAuthorityRun and 'CloseElement' in self.m_ExtraInfo and sType in self.m_ExtraInfo['CloseElement']:
            return 0
        if bForce:
            return 1
        if sType == 'HangUpKickElement':
            if lib_flag.g_IsPCRunFight:
                return 1
            if lib_flag.g_IsMobile and not (lib_flag.g_IsLogicLayer):
                return 1
            return 0
        if sType == 'TeammateAI':
            if lib_flag.g_IsMobile:
                dExtraInfo = self.m_ExtraInfo[sType]
                if not dExtraInfo.get('DelegateAI', 0) and not dExtraInfo.get('AIMember', []):
                    return 0
            if self.m_PlayMode not in (PLAYMODE_ROGUELIKE,):
                return 0
            return 1
        if sType == 'EndlessElement':
            if 'Endless' in self.m_ExtraInfo and self.m_ExtraInfo['Endless']:
                return 1
            return 0
        if sType == 'ThunderstormElement':
            (_, oData) = self.m_ComponentCls['ThunderstormElement']
            iInitWarRound = oData.m_Config.get('InitWarRound', 1)
            if self.m_Round >= iInitWarRound:
                return 1
            return 0
        if sType == 'RidingAloneElement' and self.GetPlayType(bCheckAIMember = False) != PLAY_TYPE_SINGLE:
            return 0
        for iModeType, sElementType in MODETYPE_TO_ELEMENT.items():
            if sType == sElementType and iModeType not in self.m_ModeType:
                return 0
        
        if sType == 'RealEndlessElement' and self.m_ExtraInfo.get('Endless', 0):
            WarobjLog.Alert('game:%d open realendless err %s %s' % (self.m_Game.m_ID, self.m_ModeType, self.m_ExtraInfo))
            return 0
        if sType in self.m_AllSeasonElement:
            if not lib_flag.g_OpenSeason:
                return 0
            iSeason = self.m_SeasonNum
            if iSeason in self.m_SeasonElement and sType in self.m_SeasonElement[iSeason]:
                return 1
            return 0
        return 1

    
    def OpenElement(self, sType, bForce = False):
        oGame = self.m_Game
        if sType in self.m_Component:
            return self.m_Component[sType]
        if not self.IsOpenElement(sType, bForce):
            return None
        WarobjLog.Info('%s openelement %s %s' % (oGame.m_ID, sType, bForce))
        lstData = self.m_ComponentCls[sType]
        iID = oGame.NewNPCID()
        (elefunc, oData) = lstData
        clsElement = elefunc(self)
        oElement = clsElement(oGame, iID, oData)
        oGame.CreateObject(iID, oElement)
        self.m_Component[sType] = oElement
        oElement.Init()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_INITELEMENT, self, {
            'element': sType })
        oElement.InitAfter()
        oElement.OnHalfOpen()
        return oElement

    
    def GetCurSeasonAllElement(self):
        iSeason = self.m_SeasonNum
        if iSeason in self.m_SeasonElement:
            return self.m_SeasonElement[iSeason]
        return []

    
    def RemoveModeTypeBySubModeType(self, lstModeType, lstSubModeType):
        for iModeType in lstSubModeType:
            if iModeType in lstModeType:
                lstModeType.remove(iModeType)
        

    
    def GetModeTypeToElement(self, lstModeType):
        lstElement = []
        for iModeType in lstModeType:
            if iModeType in MODETYPE_TO_ELEMENT:
                lstElement.append(MODETYPE_TO_ELEMENT[iModeType])
        
        return lstElement

    
    def SetModeType(self, lstModeType):
        self.m_ModeType = lstModeType
        for iModeType in self.m_ModeType:
            if iModeType not in MODETYPE_TO_ELEMENT:
                continue
            sElementType = MODETYPE_TO_ELEMENT[iModeType]
            self.OpenElement(sElementType)
        
        oRoundElement = self.GetComponent('RoundElement')
        oRoundElement.m_ModeMonsterAttrAdjust = oRoundElement.GetModeMonsterAttrAdjust()

    
    def GetSurvivorElement(self):
        if self.m_PlayMode == PLAYMODE_SURVIVOR:
            return self.GetComponent('SurvivorElement')
        if self.m_PlayMode == PLAYMODE_NEWSURVIVOR:
            return self.GetComponent('NewSurvivorElement')

    
    def GetSeasonSuitElement(self):
        oElement = self.GetComponent('SeasonSuitElement')
        if oElement and oElement.CheckEnable():
            return oElement

    
    def GetWandElement(self):
        oElement = self.GetComponent('WandElement')
        if oElement and oElement.CheckEnable():
            return oElement

    
    def GetDiceElement(self):
        oElement = self.GetComponent('DiceElement')
        if oElement and oElement.CheckEnable():
            return oElement

    
    def GetBackpackElement(self):
        oElement = self.GetComponent('BackpackElement')
        if oElement and oElement.CheckEnable():
            return oElement

    
    def GetS8Element(self):
        oElement = self.GetComponent('S8Element')
        if oElement and oElement.CheckEnable():
            return oElement

    
    def GetBigDataPhase(self, oSurvivorElement):
        oLevelCtrl = self.GetComponent('LevelCtrl')
        if self.m_PlayMode == PLAYMODE_NEWSURVIVOR and oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
            iPhase = BIGDATA_BOSS_PHASE
        else:
            iPhase = oSurvivorElement.m_Phase
        return iPhase

    
    def GetSurvivorPhase(self):
        oSurvivorElement = self.GetSurvivorElement()
        if oSurvivorElement:
            return oSurvivorElement.GetPassPhase()
        return 0

    
    def GetAllPlayer(self):
        return list(self.m_PlayerMask['All'])

    
    def GetLivePlayer(self, iCalAI = 1):
        lstPlayer = list(self.m_PlayerMask['Live'])
        if not iCalAI:
            oAIElement = self.GetComponent('TeammateAI')
            if oAIElement:
                lstPlayer = list(set(lstPlayer) - set(oAIElement.m_UnderControl.values()))
        return lstPlayer

    
    def GetRoomPlayer(self, iCalAI = 1):
        lstPlayer = list(self.m_PlayerMask['Room'])
        if not iCalAI:
            oAIElement = self.GetComponent('TeammateAI')
            if oAIElement:
                lstPlayer = list(set(lstPlayer) - set(oAIElement.m_UnderControl.values()))
        return lstPlayer

    
    def GetAllHero(self):
        return list(self.m_PlayerMask['Hero'].values())

    
    def GetLiveHero(self, iCalAI = 1):
        if not iCalAI:
            return list(set(self.m_PlayerMask['LiveHero'].values()) - set(self.GetAllAIHero()))
        return list(self.m_PlayerMask['LiveHero'].values())

    
    def GetRoomHero(self, iCalAI = 1):
        lstRoomHero = [ self.m_PlayerMask['Hero'][pid] for pid in self.m_PlayerMask['Room'] ]
        if iCalAI:
            lstRoomHero = list(set(lstRoomHero) | set(self.GetAllAIHero()))
        else:
            lstRoomHero = list(set(lstRoomHero) - set(self.GetAllAIHero()))
        return lstRoomHero

    
    def GetLiveOnlinePlayer(self):
        return list(set(self.m_PlayerMask['Live']) & set(self.m_Game.GetRealPlayers()))

    
    def GetRoomOnlinePlayer(self):
        return list(set(self.m_PlayerMask['Room']) & set(self.m_Game.GetRealPlayers()))

    
    def GetAllPlayerHero(self):
        return self.m_PlayerMask['Hero']

    
    def GetAllAIHero(self, iIncludeWait = 0, bExcludeAIMember = False):
        oElement = self.GetComponent('TeammateAI')
        if oElement:
            return oElement.GetAllAIHero(iIncludeWait, bExcludeAIMember)
        return []

    
    def GetAllHeroExceptAI(self):
        dHeroExcAI = { }
        lstHero = self.GetAllHero()
        lstAIHero = self.GetAllAIHero()
        for iHero in lstHero:
            if iHero not in lstAIHero:
                dHeroExcAI[iHero] = 1
        
        return dHeroExcAI

    
    def GetBigDataHero(self):
        if self.m_BigDataHero:
            return self.m_BigDataHero
        lstHero = self.GetAllHero()
        oElement = self.GetComponent('TeammateAI')
        if not oElement:
            self.m_BigDataHero = lstHero
            return lstHero
        lstAI = oElement.GetAIMember()
        for iPlayer in lstAI:
            iHero = self.GetHeroIDByPlayerID(iPlayer)
            if iHero in lstHero:
                lstHero.remove(iHero)
        
        self.m_BigDataHero = lstHero
        return lstHero

    
    def IsInRoom(self, pid):
        return pid in self.m_PlayerMask['Room']

    
    def HasSettled(self, pid):
        return pid in self.m_SettledPlayer

    
    def IsAIHero(self, iHero):
        oElement = self.GetComponent('TeammateAI')
        if oElement:
            return iHero in oElement.m_UnderControl
        return 0

    
    def IsCycleWar(self):
        return self.m_Cycle > 0

    
    def IsDelayRemove(self):
        return self.m_DelayRemove

    
    def SetDelayRemove(self, iDelayRemove):
        self.m_DelayRemove = iDelayRemove

    
    def GetWarDifficultyInfo(self):
        if self.IsCycleWar():
            return (DIFFICULTY_ADVANCE_CYCLE, self.m_Cycle)
        return (DIFFICULTY_COMMON_ROUND, self.m_Round)

    
    def GetAllPlayerCnt(self):
        if self.Query('GMPlayerCnt'):
            return self.Query('GMPlayerCnt')
        if self.m_RefreshPlayerCnt:
            return self.m_RefreshPlayerCnt
        return len(self.m_PlayerMask['All'])

    
    def RefreshPlayerCnt(self):
        iRefreshedCnt = self.m_RefreshPlayerCnt
        iRoomCnt = len(self.m_PlayerMask['Room'])
        iAICnt = len(self.GetAllAIHero())
        iAll = len(self.m_PlayerMask['All'])
        iNewCnt = min(iAll, iRoomCnt + iAICnt)
        WarobjLog.Info('refreshplayercnt %s %s' % (iRefreshedCnt, iNewCnt))
        if iRefreshedCnt != iNewCnt:
            self.m_RefreshPlayerCnt = iNewCnt
            return True
        return False

    
    def IsSingleGame(self, bExcludeAIMember = False):
        if self.m_PlayType == PLAY_TYPE_SINGLE:
            pass
        return not self.GetAllAIHero(bExcludeAIMember = bExcludeAIMember)

    
    def CheckInitSingleGame(self):
        if self.m_PlayType == PLAY_TYPE_SINGLE:
            pass
        return not (self.m_IsTransfer)

    
    def CheckUseRecordGame(self, dPlayer):
        data = { }
        iNoSceneObjNum = 0
        for dInfo in dPlayer.values():
            iUseRecord = dInfo.get('UseRecord', 0)
            if not iUseRecord:
                self.m_IsUseRecord = False
                return None
            iNoSceneObjNum = dInfo.get('NoSceneObjNum', 0)
        
        self.m_IsUseRecord = True
        data['NoSceneObjNum'] = iNoSceneObjNum
        self.OnCheckUseRecordGame(data)

    
    def OnCheckUseRecordGame(self, dInfo):
        iNoSceneObjNum = dInfo['NoSceneObjNum']
        if iNoSceneObjNum:
            self.m_Game.m_NoSceneObjID = iNoSceneObjNum

    
    def CheckTransferGame(self, dPlayer):
        dTransfer = { }
        for dInfo in dPlayer.values():
            dTransfer = dInfo.get('TransferRecord', None)
            if not dTransfer:
                self.m_IsTransfer = False
                return 0
        
        dFormerPlayer = dTransfer.get('FormerPlayerInfo', { })
        self.CheckQuittedPlayer(dPlayer, dFormerPlayer)
        self.m_IsTransfer = True
        return 1

    
    def CheckAndSetWarMaster(self, dPlayer):
        for pid, dInfo in dPlayer.items():
            if dInfo.get('IsMaster', 0):
                self.m_WarMaster = pid
        

    
    def CheckQuittedPlayer(self, dCurPlayer, dFormer):
        dQuitted = { }
        for pid in dFormer:
            if pid not in dCurPlayer:
                dQuitted[pid] = dFormer[pid]
        
        self.m_QuittedPlayerInfo = dQuitted

    
    def UseQuittedPlayerInfo(self):
        dQuited = self.m_QuittedPlayerInfo
        self.m_QuittedPlayerInfo = { }
        return dQuited

    
    def IsTransferGame(self):
        return self.m_IsTransfer

    
    def GetPlayType(self, bCheckAIMember = True):
        if bCheckAIMember and self.CheckHasAIMember():
            return PLAY_TYPE_MULTI
        return self.m_PlayType

    
    def GetReportPlayType(self):
        if self.m_IsTransfer:
            return PLAY_TYPE_MULTI
        return self.m_PlayType

    
    def GetPlayerLGS(self, iPlayer):
        if iPlayer in self.m_PlayerMask['All']:
            return self.m_PlayerMask['All'][iPlayer]['LGS']
        return 0

    
    def GetPlayerAccount(self, iPlayer):
        if iPlayer in self.m_PlayerMask['All']:
            return self.m_PlayerMask['All'][iPlayer]['Acc']
        return 0

    
    def GetPlayerIDByHeroID(self, iHero):
        for pid, iNpcID in self.m_PlayerMask['Hero'].items():
            if iHero != iNpcID:
                continue
            return pid
        
        return 0

    
    def GetHeroIDByPlayerID(self, pid):
        if pid not in self.m_PlayerMask['Hero']:
            return 0
        return self.m_PlayerMask['Hero'][pid]

    
    def InitMaxLayer(self, dPlayer):
        iMax = 3
        for pid, dInfo in dPlayer.items():
            if 'MaxLayer' in dInfo:
                iMax = dInfo['MaxLayer']
                break
            if 'MaxRoundInfo' not in dInfo:
                continue
            (iRound, iCycle, iLayer) = dInfo['MaxRoundInfo']
            WarobjLog.Info('%s maxround %s %s %s %s' % (self.m_Game.m_ID, pid, iRound, iCycle, iLayer))
            if not iRound > 1 or iCycle > 1:
                if iLayer >= 3:
                    iMax = 4
                    break
        
        self.m_MaxLayer = iMax
        WarobjLog.Info('%s maxlayer %s' % (self.m_Game.m_ID, iMax))

    
    def GetMaxLayer(self):
        return self.m_MaxLayer

    
    def GetWarCycle(self):
        return self.m_Cycle

    
    def SetNewVerLayer(self, iIsNew):
        if iIsNew not in (0, 1):
            WarobjLog.Alert('%s err newverlayer arg %s' % (self.m_Game.m_ID, iIsNew))
            return None
        self.m_ExtraInfo['NewVerLayer'] = iIsNew

    
    def GetNewVerLayer(self):
        if 'NewVerLayer' in self.m_ExtraInfo:
            return self.m_ExtraInfo['NewVerLayer']
        return 0

    
    def IsPassRound(self, tRound):
        if self.m_MaxRoundInfo[0] > tRound[0]:
            return 1
        if self.m_MaxRoundInfo[0] == tRound[0]:
            if self.m_MaxRoundInfo[1] > tRound[1]:
                return 1
            if self.m_MaxRoundInfo[1] == tRound[1] and self.m_MaxRoundInfo[2] >= tRound[2]:
                return 1
        return 0

    
    def InitWarMask(self, dPlayer):
        if self.m_IsUseRecord:
            sRecordKey = 'TransferRecord' if self.m_IsTransfer else 'SavedRecord'
            for dInfo in dPlayer.values():
                if 'WarMask' in dInfo[sRecordKey]:
                    self.m_WarMask = dInfo[sRecordKey]['WarMask']
                    return None
            
        if not self.m_WarMask:
            self.m_WarMask = '%s-%s' % (time.strftime('%m%d%H%M', time.localtime(time.time())), self.m_ReportID)
            self.m_WarMask = self.m_WarMask.replace(', ', '_')

    
    def OnWarInit(self, oGame):
        pass

    
    def OnInitPlayer(self, dPlayerInfo):
        lstLvInfo = []
        for dInfo in dPlayerInfo.values():
            lstLvInfo.append(dInfo.get('LvInfo', { }))
        
        oLevelCtrl = self.GetComponent('LevelCtrl')
        if oLevelCtrl:
            oLevelCtrl.RebuildLevel(lstLvInfo)
            oLevelCtrl.RoundLevelFilter()

    
    def GetValidRelic(self, dPlayerInfo = None):
        dRelicMap = self.m_Game.m_WarData.GetPassiveMapByType(ADJUST_RELIC)
        dRemoveRelic = dRelicMap[TYPE_REMOVE] if TYPE_REMOVE in dRelicMap else { }
        dReplaceRelic = dRelicMap[TYPE_REPLACE] if TYPE_REPLACE in dRelicMap else { }
        setExcludeRelic = set(cl_perform.load.GetGameExcludeRelic(self.GetPlayType())) | set(dRemoveRelic)
        setRelic = set(cl_putdata.GetAllPutRelic()) - setExcludeRelic
        if dPlayerInfo:
            setUnlock = set(cl_perform.load.GetUnlockRelic()) | set(dPlayerInfo['Relic']['Unlock'])
            setRelic &= setUnlock
        for iRelic, iReplace in dReplaceRelic.items():
            if iRelic in setRelic:
                setRelic.add(iReplace)
        
        setRoundForbitRelic = set(cl_platformdata.GetRoundForbidRelic(self.m_Round))
        return setRelic - set(dReplaceRelic) - self.m_ForbidRelic - setRoundForbitRelic

    
    def GetWarPutRelic(self):
        if not self.m_PutRelic:
            self.m_PutRelic = self.GetValidRelic()
        return self.m_PutRelic - self.m_ForbidRelic

    
    def AddForbidRelic(self, lstRelic):
        self.m_ForbidRelic.update(lstRelic)
        for pid in self.GetRoomPlayer():
            oHero = self.GetHeroByPlayer(pid)
            if not oHero:
                continue
            dIllus = oHero.Query('Illus', { })
            if not dIllus or 'Relic' not in dIllus or not dIllus['Relic']:
                continue
            dIllus['Relic'] = dIllus['Relic'] - self.m_ForbidRelic
        

    
    def GetForbidRelic(self):
        return self.m_ForbidRelic

    
    def OnAddPlayer(self, oHero, dPlayerInfo):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self, {
            'Info': dPlayerInfo,
            'Hero': oHero })
        sName = dPlayerInfo.get('Name', 'Test%d' % oHero.m_ID)
        if sName == '':
            WarobjLog.Alert('%s empty name' % oHero.m_PlayerID)
        oHero.m_OwnerName = sName
        setUnlockWeapon = (set(cl_item.load.GetUnlockWeapon()) | set(dPlayerInfo['Weapon']['Unlock'])) & set(cl_putdata.GetAllPutWeapon())
        setValidRelic = self.GetValidRelic(dPlayerInfo)
        dIllus = {
            'Weapon': setUnlockWeapon,
            'Relic': setValidRelic,
            'Talent': dPlayerInfo.get('Talent', { }),
            'Emotion': dPlayerInfo.get('Emotion', { }),
            'Sublimation': dPlayerInfo.get('Sublimation', { }) }
        oHero.Set('Illus', dIllus)
        oHero.m_UnlockProgressCon.Register(dPlayerInfo.get('UnlockProgress', { }))
        oHero.m_UnlockProgressCon.InitAdjustWeaponData(dPlayerInfo.get('AdjustWeaponInfo', { }))
        oHero.InitGSCash(dPlayerInfo.get('Cash', 0))
        oHero.m_NewUnlockProgressMgr.LoadProgress(dPlayerInfo.get('NewUnlockProgress', { }))
        if 'Sublimation' in dPlayerInfo:
            oHero.AddSublimation(dPlayerInfo['Sublimation'])
        if 'SeasonTalent' in dPlayerInfo and self.IsOpenSeasonElement():
            oHero.AddSeasonTalent(dPlayerInfo['SeasonTalent'])
        if 'AnimaModule' in dPlayerInfo:
            oHero.AddAnimaModule(dPlayerInfo['AnimaModule'])
            oHero.Set('UnlockBlocPoskNum', dPlayerInfo.get('UnlockBlocPoskNum', 0))
            oHero.Set('UsedBlocPoskNum', cl_anima.GetAnimaModuleShapeNum(dPlayerInfo['AnimaModule']))
        oHero.m_WeaponSkinCon.LoadWeaponSkin(dPlayerInfo.get('WeaponSkin', { }))
        oHero.m_Achievement.LoadStats(dPlayerInfo.get('Achieve', { }))
        oHero.m_SeasonTaskMgr.LoadSeasonTask(dPlayerInfo.get('SeasonTask', {
            'War': { },
            'GS': { },
            'Done': { },
            'ExtInfo': { } }))
        if oHero.m_PetCon:
            oHero.m_PetCon.SetCompanionPet(dPlayerInfo.get('Pet', { }))
        iTeamPos = dPlayerInfo['TeamPos'] if 'TeamPos' in dPlayerInfo else self.GetAllPlayerCnt()
        oHero.Set('TeamPos', iTeamPos)
        dLevelRecord = dPlayerInfo.get('MainLvInfo', { })
        lstLevel = dLevelRecord.get('Record', [])
        oHero.Set('LevelRecord', lstLevel)
        dMonster = dPlayerInfo.get('MainMonster', { })
        WarobjLog.Info('game: %d pid: %d monsterinfo %s' % (self.m_Game.m_ID, oHero.m_PlayerID, dMonster))
        oHero.Set('Monster', dMonster)
        oHero.Set('FightIndex', dPlayerInfo.get('FightIndex', 0))
        oHero.Set('CheckTips', dPlayerInfo.get('CheckTips', { }))
        oHero.Set('DayTrialStartCnt', dPlayerInfo.get('DayTrialStartCnt', 0))
        oHero.Set('Account', dPlayerInfo.get('Account', 0))
        oHero.Set('UnlockSuit', dPlayerInfo.get('UnlockSuit', { }))
        oHero.Set('WeaponStore', dPlayerInfo.get('WeaponStore', { }))
        oHero.Set('NewVerLayer', dPlayerInfo.get('NewVerLayer', { }))
        lstCompensateWeaponInfo = dPlayerInfo.get('CompensateWeaponInfo', [])
        if lstCompensateWeaponInfo:
            oHero.SetSavedData('CompensateWeaponInfo', lstCompensateWeaponInfo)
        if 'SeasonLevel' in dPlayerInfo:
            oHero.Set('SeasonLevel', dPlayerInfo['SeasonLevel'])
        if 'AllSeasonRGPlayTimes' in dPlayerInfo:
            oHero.Set('AllSeasonRGPlayTimes', dPlayerInfo['AllSeasonRGPlayTimes'])

    
    def OnPlayingCG(self, iStopTime, iDelayTime):
        self.StopDyingState(iStopTime, iDelayTime)

    
    def StopDyingState(self, iStopTime, iDelayTime):
        
        def StartStateCount(oWarMgr):
            oWarMgr.Remove_Call_Out('StartStateCount')
            for pid in oWarMgr.GetAllPlayer():
                pobj = oWarMgr.GetHeroByPlayer(pid)
                if not pobj:
                    continue
                oState = pobj.m_State.GetItemBySID(STATE_DYING)
                if not oState:
                    continue
                oState.StartCount(pobj)
            

        
        def StopStateCount(oWarMgr, iStopTime):
            oWarMgr.Remove_Call_Out('StopStateCount')
            iFlag = 0
            for pid in oWarMgr.GetAllPlayer():
                pobj = oWarMgr.GetHeroByPlayer(pid)
                if not pobj:
                    continue
                oState = pobj.m_State.GetItemBySID(STATE_DYING)
                if not oState:
                    continue
                oState.StopCount(pobj)
                iFlag = 1
            
            if iFlag:
                func = Functor(StartStateCount, oWarMgr)
                oWarMgr.Call_Out(func, Time2Frame(iStopTime), 'StartStateCount')

        if iDelayTime:
            func = Functor(StopStateCount, self, iStopTime)
            self.Call_Out(func, Time2Frame(iDelayTime), 'StopStateCount')
        else:
            StopStateCount(self, iStopTime)

    
    def OnPlayerDead(self, oHero):
        self.RemoveLivePlayer(oHero.m_PlayerID)
        self.CheckWarEnd()

    
    def CheckWarEnd(self):
        if lib_flag.g_IsStandaloneClient:
            lstRest = self.GetLiveOnlinePlayer()
        else:
            lstRest = self.GetLivePlayer()
        if not lstRest and self.m_PlayerMask['Room']:
            self.OnFinishLevel(SETTLE_LOSEWAR)
            self.OnLoseWar()

    
    def OnFinishLevel(self, iType):
        for pid in self.m_PlayerMask['Room']:
            self.HandlePlayerLevelReport(pid, iType)
        
        self.SendReloadFightRecord(iType)
        if not lib_flag.g_IsLogicLayer:
            dTeamBuildInfo = { }
            for pid in self.m_PlayerMask['Room']:
                dTeamBuildInfo[pid] = self.GetPlayerBuildInfo(pid)
            
            log_file_long('debug/warobj', f'''{self.m_Game.m_ID} buildinfo {dTeamBuildInfo}''')

    
    def OnFinishWar(self):
        for pid in list(self.m_PlayerMask['Room']):
            self.HandlePlayerSettle(pid, SETTLE_FINISHWAR)
            self.RemovePlayer(pid, 0)
        
        lstPlayer = self.GetAllPlayer()
        lib_server.WarEnd(self.m_Game.m_ID, lstPlayer)

    
    def OnLoseWar(self):
        self.SettleRoomPlayerAndDelayRemove(SETTLE_LOSEWAR, GAME_FRAME)
        lstPlayer = self.GetAllPlayer()
        lib_server.WarEnd(self.m_Game.m_ID, lstPlayer)

    
    def UpdateHeroLevelRecord(self, iLevel):
        oGame = self.m_Game
        for iHero in self.GetRoomHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstLevelRecord = oHero.SetDefault('LevelRecord', [])
            if iLevel not in lstLevelRecord:
                lstLevelRecord.append(iLevel)
        

    
    def SettleRoomPlayerAndDelayRemove(self, iSettleType, iDelayFrame):
        lstPlayer = self.GetRoomPlayer()
        for pid in lstPlayer:
            self.HandlePlayerSettle(pid, iSettleType)
            self.m_PlayerMask['Room'].pop(pid, 0)
            self.RemoveLivePlayer(pid)
        
        self.SetDelayRemove(1)
        self.m_Game.m_Timer.Logic_Call_Out(Functor(self.LoseWarDelayRemovePlayers, lstPlayer), Frame2Time(iDelayFrame), 'LoseWarRemove')

    
    def LoseWarDelayRemovePlayers(self, lstPlayer):
        self.SetDelayRemove(0)
        for pid in lstPlayer:
            self.RemovePlayer(pid, 0, iForce = 1)
        
        if not (lib_flag.g_IsLogicLayer):
            if (lib_flag.g_IsPCRunFight or lib_flag.g_IsMobile) and not self.m_Game.m_LinkMgr.GetLink():
                self.m_Game.m_Timer.Logic_Call_Out(Functor(lib_server.CtrlWarRelease, self.m_Game.m_ID, 'AllQuit'), 1, 'LoseWarRelease')

    
    def OnDirectLeave(self, pid, iLeaveType, iAssignSettleType = 0):
        if not self.IsInRoom(pid):
            return None
        oCtrlHero = self.GetHeroByPlayer(pid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self, {
            'Hero': oCtrlHero.m_ID,
            'pid': pid,
            'AssignSettleType': iAssignSettleType })
        iSettleType = SETTLE_DIRECTLEAVE
        if self.IsSingleGame() and oCtrlHero.IsDead():
            iSettleType = SETTLE_LOSEWAR
        if iAssignSettleType:
            iSettleType = iAssignSettleType
        bGiveUpRecord = False
        if iLeaveType in (LEAVE_TYPE_NORECORDE,) and RunMobileData():
            bGiveUpRecord = True
        iTeamSettleType = self.CheckMasterLeaveSettle(pid)
        if iTeamSettleType == SETTLE_TRANSFER:
            self.MasterTransfer(pid)
        self.HandlePlayerLevelReport(pid, iSettleType, iLeaveType)
        self.HandlePlayerSettle(pid, iSettleType, bGiveUpRecord)
        self.RemovePlayer(pid, 0)
        self.RoomBroadcastNotify(7006, {
            '$$name': oCtrlHero.m_OwnerName })
        if iTeamSettleType:
            self.HandleMasterLeave(pid, iTeamSettleType)
        if not iAssignSettleType:
            self.CheckWarEnd()

    
    def GetRealSettleType(self, iSettleType, bGiveUpRecord = False):
        if iSettleType in (SETTLE_MASTERLEAVE, SETTLE_FINISHWAR, SETTLE_TRANSFER):
            return iSettleType
        oSave = self.GetComponent('SaveElement')
        if oSave and oSave.CheckHasSaved() and not bGiveUpRecord:
            return iSettleType
        if self.IsEndless():
            return SETTLE_FINISHWAR
        return iSettleType

    
    def OnSystemKickOut(self, pid):
        if not self.IsInRoom(pid):
            return None
        oCtrlHero = self.GetHeroByPlayer(pid)
        if not oCtrlHero or not (oCtrlHero.m_UnlockProgressCon):
            return None
        self.HandlePlayerLevelReport(pid, SETTLE_SYSKICK)
        self.HandlePlayerSettle(pid, SETTLE_SYSKICK)
        self.RemovePlayer(pid, 1)
        self.RoomBroadcastNotify(7006, {
            '$$name': oCtrlHero.m_OwnerName })
        self.CheckWarEnd()

    
    def OnSystemKickOutAll(self):
        lstPlayer = self.GetRoomPlayer()
        for pid in lstPlayer:
            self.OnSystemKickOut(pid)
        

    
    def HandleVote(self, dVote):
        oLevelCtrl = self.GetComponent('LevelCtrl')
        dContinue = { }
        dQuit = { }
        lstAllPlayer = self.GetRoomPlayer()
        for pid in lstAllPlayer:
            if pid in dVote and dVote[pid] == VOTE_CONTINUE:
                dContinue[pid] = 1
                continue
            dQuit[pid] = 1
        
        if oLevelCtrl.m_CurTransfer:
            dTransfer = list(oLevelCtrl.m_CurTransfer.values())[0]
        else:
            dTransfer = { }
        iMaster = self.GetWarMasterPlayer()
        self.RecordFormerPlayer()
        if iMaster and iMaster in dQuit:
            oAIElement = self.GetComponent('TeammateAI')
            if oAIElement:
                for pid in dQuit:
                    iHero = self.GetHeroIDByPlayerID(pid)
                    oAIElement.m_UnderControl[iHero] = pid
                
            for pid in dQuit:
                if pid == iMaster:
                    continue
                self.OnDirectLeave(pid, iLeaveType = 0, iAssignSettleType = SETTLE_FINISHWAR)
            
            if dContinue:
                dTransfer['HandleVoteTransfer'] = 1
                oSaveElement = self.GetComponent('TeamSaveElement')
                if oSaveElement:
                    oSaveElement.SaveCurRecord({
                        'Transfer': dTransfer })
            self.OnDirectLeave(iMaster, iLeaveType = 0, iAssignSettleType = SETTLE_FINISHWAR)
            self.CheckWarEnd()
        else:
            for pid in dQuit:
                self.OnDirectLeave(pid, iLeaveType = 0, iAssignSettleType = SETTLE_FINISHWAR)
            
            if not dContinue:
                self.CheckWarEnd()
                return None
            lstHero = []
            for pid in dContinue:
                oHero = self.GetHeroByPlayer(pid)
                if not oHero:
                    continue
                lstHero.append(oHero.m_ID)
            
            self.CheckQuittedPlayer(dContinue, self.GetFormerPlayerInfo())
            oLevelCtrl.m_CurNode.TryTriggerPassLevel(lstHero, dTransfer)

    
    def RecordFormerPlayer(self):
        dInfo = { }
        for pid in self.GetRoomPlayer():
            oHero = self.GetHeroByPlayer(pid)
            if not oHero:
                continue
            dInfo[pid] = {
                'Name': oHero.Name() }
        
        self.Set('FormerPlayer', dInfo)

    
    def GetFormerPlayerInfo(self):
        return self.Query('FormerPlayer', { })

    
    def InitUseSealedInscription(self, dPlayerInfo):
        bInitSealedInscription = False
        for pid in dPlayerInfo:
            oHero = self.GetHeroByPlayer(pid)
            if not oHero:
                continue
            if oHero.m_SID == 214:
                bInitSealedInscription = True
                break
        
        self.Set('InitSealInscription', bInitSealedInscription)

    
    def IsUseSealedInscription(self):
        return self.Query('InitSealInscription', False)

    
    def CheckMasterLeaveSettle(self, pid):
        if not lib_flag.g_IsStandaloneClient:
            return 0
        who = cli_player.GetPlayer(pid)
        if who.m_WarMaster and len(self.GetRoomOnlinePlayer()) > 1:
            iSettleType = SETTLE_LOSEWAR
            oSurvivorElement = self.GetComponent('SurvivorElement')
            if oSurvivorElement and not (oSurvivorElement.m_Phase):
                return iSettleType
            oLevelCtrl = self.GetComponent('LevelCtrl')
            iPassAll = oLevelCtrl.CheckFinishWar() & oLevelCtrl.m_CurNode.HasGoaledCurNode()
            if iPassAll:
                iSettleType = SETTLE_FINISHWAR
            iAtFirstHall = oLevelCtrl.CheckFirstHall()
            lstLive = self.GetLivePlayer()
            if pid in lstLive:
                lstLive.remove(pid)
            if lstLive and not iPassAll and not iAtFirstHall:
                if self.m_UseMasterTransfer:
                    iSettleType = SETTLE_TRANSFER
                else:
                    iSettleType = SETTLE_MASTERLEAVE
            return iSettleType
        return 0

    
    def HandleMasterLeave(self, iOldMaster, iSettleType):
        if iSettleType == SETTLE_TRANSFER:
            self.TeamTransfer(iOldMaster)
        self.OnFinishLevel(iSettleType)
        self.SettleRoomPlayerAndDelayRemove(iSettleType, 1)

    
    def MasterTransfer(self, pid):
        iGameID = self.m_Game.m_ID
        lstPlayer = self.GetRoomOnlinePlayer()
        lstPlayer.remove(pid)
        iTempMaster = lstPlayer[0]
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        dInfo = {
            'Master': pid,
            'TempMaster': iTempMaster }
        lib_server.L2SMasterTransfer(iLGS, iGameID, pid, dInfo)

    
    def TeamTransfer(self, iOldMaster):
        iGameID = self.m_Game.m_ID
        lstPlayer = self.GetRoomOnlinePlayer()
        lstLive = self.GetLivePlayer()
        dAllRecord = self.GetTransferRecord(lstPlayer)
        for pid in lstPlayer:
            iLGS = self.m_PlayerMask['All'][pid]['LGS']
            iSingleContinue = 1 if pid in lstLive else 0
            dInfo = {
                'Master': iOldMaster,
                'SingleContinue': iSingleContinue,
                'Team': lstPlayer }
            dInfo['TransferRecord'] = dAllRecord[pid]
            lib_server.L2SMasterTransfer(iLGS, iGameID, pid, dInfo)
        

    
    def GetTransferRecord(self, lstPlayer):
        dAllRecord = { }
        oTeamSaveElement = self.GetComponent('TeamSaveElement')
        if not oTeamSaveElement:
            return dAllRecord
        lstLive = self.GetLivePlayer()
        dFormerPlayerInfo = self.GetFormerPlayerInfo()
        oAIElement = self.GetComponent('TeammateAI')
        dUpdate = oAIElement.TrueSave() if oAIElement else { }
        iLastMaster = self.GetWarMasterPlayer()
        for pid in lstPlayer:
            iSingleContinue = 1 if pid in lstLive else 0
            dRecord = oTeamSaveElement.Save(pid)
            if not dRecord:
                continue
            dRecord['FormerPlayerInfo'] = dFormerPlayerInfo
            if 'WarMgr' in dRecord:
                dRecord['WarMgr']['TeammateAI'] = dUpdate
            if iSingleContinue:
                iRecordDead = dRecord['Hero'].pop('DEAD', 0)
                if iRecordDead:
                    oHero = self.GetHeroByPlayer(pid)
                    dRecord['Hero']['HP'] = oHero.m_HP if oHero else 100
            dRecord['LastMaster'] = iLastMaster
            dAllRecord[pid] = dRecord
        
        return dAllRecord

    
    def SendReloadFightRecord(self, iType = None, lstPlayer = None):
        if not lib_flag.g_IsStandaloneClient:
            return None
        if iType and iType != SETTLE_FINISHWAR:
            return None
        if self.m_PlayMode != PLAYMODE_ROGUELIKE:
            return None
        if self.GetReportPlayType() == PLAY_TYPE_SINGLE:
            return None
        oLevelCtrl = self.GetComponent('LevelCtrl')
        if oLevelCtrl.CheckFinishWar():
            return None
        if not lstPlayer:
            lstPlayer = self.GetRoomPlayer()
        dAllRecord = self.GetTransferRecord(lstPlayer)
        if not dAllRecord:
            return None
        iGameID = self.m_Game.m_ID
        for pid in lstPlayer:
            dRecord = dAllRecord[pid]
            iLGS = self.m_PlayerMask['All'][pid]['LGS']
            FightserverLog.Debug('%s %s reloadrecord' % (iGameID, pid))
            lib_server.L2SSendReloadFightRecord(iLGS, iGameID, pid, dRecord)
        

    
    def ReSendCacheReport(self, pid):
        if not self.IsInRoom(pid):
            return None
        iMaster = self.GetWarMasterPlayer()
        if not iMaster:
            return None
        iLGS = self.m_PlayerMask['All'][iMaster]['LGS']
        iGameID = self.m_Game.m_ID
        dInfo = {
            'Player': pid }
        lib_server.L2SReSendCacheReport(iLGS, iGameID, iMaster, dInfo)

    
    def GetWarMasterPlayer(self):
        if not lib_flag.g_IsStandaloneClient:
            return 0
        if not self.m_WarMaster:
            for pid in self.GetRoomPlayer():
                who = cli_player.GetPlayer(pid)
                if who and who.m_WarMaster:
                    self.m_WarMaster = pid
                    break
            
        return self.m_WarMaster

    
    def GetLeaderPlayer(self):
        if not self.m_Leader:
            self.m_Leader = self.GetWarMasterPlayer()
            if not self.m_Leader:
                lstRoomPlayer = self.GetRoomPlayer()
                if lstRoomPlayer:
                    self.m_Leader = lstRoomPlayer[0]
        return self.m_Leader

    
    def IsLeavingAtFirstHall(self, iType):
        if iType not in (SETTLE_DIRECTLEAVE, SETTLE_MASTERLEAVE, SETTLE_LOSEWAR):
            return False
        oLevelCtrl = self.GetComponent('LevelCtrl')
        if not oLevelCtrl or not oLevelCtrl.CheckFirstHall():
            return False
        return True

    
    def GetReportGSCash(self, oHero, iType):
        if self.IsLeavingAtFirstHall(iType):
            return oHero.m_InitGSCash
        iExtGSCash = 0
        oSurvivorElement = self.GetComponent('SurvivorElement')
        if oSurvivorElement:
            iExtGSCash = oSurvivorElement.GetExtGSCash(iType)
        return oHero.m_WarGSCash + iExtGSCash

    
    def CreateWarEndBigDataAnalyseInfo(self, pid, iType, dWarReport):
        oHero = self.GetHeroByPlayer(pid)
        oBigDataAnaMgr = self.GetComponent('BigDataAnalyseMgr')
        if not oBigDataAnaMgr:
            return { }
        dEndReport = dWarReport['Report']
        dWarReport['InitType'] = iType
        dBigDataReport = self.GenerateCommonBigDataInfo(dWarReport, dEndReport, oHero)
        dBigDataAna = oBigDataAnaMgr.GetWarStatistics(oHero.m_PlayerID)
        dBigDataAna['Unlock'] = {
            'Weapon': [],
            'Relic': [] }
        lstUnlockInfo = dWarReport['DoneLock']
        if lstUnlockInfo:
            for iUnlockType, iUnlockId in lstUnlockInfo:
                if iUnlockType == 1:
                    dBigDataAna['Unlock']['Weapon'].append(iUnlockId)
                    continue
                if iUnlockType == 2:
                    dBigDataAna['Unlock']['Relic'].append(iUnlockId)
            
        dBigDataReport['BigDataAna'] = dBigDataAna
        dBigDataReport['Saved'] = dWarReport['Saved']
        dBigDataReport['Busted'] = oHero.IsCheat()
        self.DealWarEndlessTimeInfo(dBigDataReport)
        oTeammateAI = self.GetComponent('TeammateAI')
        if oTeammateAI and oTeammateAI.m_AIMember and len(self.GetRoomOnlinePlayer()) == 1:
            dAIMember = { }
            for dTeammateInfo in dWarReport['Team'].values():
                iPlayer = dTeammateInfo['pid']
                if iPlayer not in oTeammateAI.m_AIMember:
                    continue
                dAIMemberInfo = oTeammateAI.m_AIMember[iPlayer]
                if 'Diedist' in dAIMemberInfo:
                    iDiedist = dAIMemberInfo['Diedist']
                else:
                    iDiedist = 0
                dAIMember[iPlayer] = {
                    'hero': dTeammateInfo['SID'],
                    'damage': dTeammateInfo['Damage'] // 100,
                    'death': dTeammateInfo['DyingTimes'],
                    'death_ex_perform': iDiedist }
            
            if dAIMember:
                dBigDataReport['AIMember'] = dAIMember
        if lib_flag.g_IsMobile:
            dBigDataReport['Earphones'] = oHero.QuerySavedData('Earphones', [])
        return dBigDataReport

    
    def CreateWarEndReport(self, pid, iType, bGiveUpRecord):
        iSaved = 0
        if not bGiveUpRecord:
            oSave = self.GetComponent('SaveElement')
            if oSave and oSave.CheckHasSaved():
                iSaved = 1
        oHero = self.GetHeroByPlayer(pid)
        oReport = self.GetComponent('Warreport')
        lstBossLevel = []
        lstTeamMember = self.GetAllHero()
        iExtGSCash = 0
        dExtGSCashInfo = { }
        oSurvivorElement = self.GetComponent('SurvivorElement')
        if oSurvivorElement:
            iExtGSCash = oSurvivorElement.GetExtGSCash(iType)
            dExtGSCashInfo = oSurvivorElement.GetExtGSCashInfo()
        if oReport:
            
            try:
                dReport = oReport.m_WarReportData.GetPlayerWarStatistics(pid)
                dReport['GSCash'] = 0 if self.IsLeavingAtFirstHall(iType) else dReport['GSCash'] + iExtGSCash
                for dLevel in dReport['LvSum'].values():
                    for tInfo in dLevel.values():
                        if tInfo[0] == LEVEL_TYPE_BOSS:
                            lstBossLevel.append(tInfo[1])
                    
                
            except:
                0
                oLevelCtrl = self.GetComponent('LevelCtrl')
                dReport = {
                    'SettleErr': 1,
                    'LvCnt': oLevelCtrl.GetMaxLevel(),
                    'CurLv': oLevelCtrl.m_CurNode.m_Level if oLevelCtrl.m_CurNode else 0,
                    'Level': oLevelCtrl.m_LevelNum,
                    'Layer': oLevelCtrl.m_LayerNum,
                    'Goaled': oLevelCtrl.m_CurNode.HasGoaledCurNode() if oLevelCtrl.m_CurNode else 0,
                    'GSCash': 0 if self.IsLeavingAtFirstHall(iType) else oHero.m_WarGSCash - oHero.m_InitGSCash,
                    'MakeDamage': oReport.GetTotalDamageByHeroID(oHero.m_ID),
                    'Relic': oHero.m_RelicCon.GetPerformSIDByType(PF_TYPE_RELIC) }
                PythonError()

            dReport['Talent'] = oHero.m_TalentCon.GetAllTalentList()
            if oHero.m_PetCon:
                dReport['Pet'] = oHero.m_PetCon.GetAllPetWarReportInfo()
            dReport['SurvivorPhase'] = self.GetSurvivorPhase()
            dTeamData = oReport.m_WarReportData.GetTeamMemberStatistics(lstTeamMember)
        else:
            dReport = { }
            dTeamData = { }
            lstBossLevel = []
        (iEndlessPassLevelNum, iEndlessKillBossNum) = self.GetEndlessReportInfo()
        lDoneUnLock = oHero.m_UnlockProgressCon.GetDoneProgress()
        lstCheek = oHero.m_CheekCon.GetAddCheek()
        oDayTrial = self.GetComponent('DayTrialElement')
        dDayTrialInfo = oDayTrial.GetWarReportInfo() if oDayTrial else { }
        dPayInfo = { }
        if self.m_Game.m_WarPayMgr:
            dPayInfo = self.m_Game.m_WarPayMgr.GetPlayerPayNote(pid)
        dFrameInfo = { }
        if self.m_Game.m_FrameMonitor:
            dFrameInfo = self.m_Game.m_FrameMonitor.GetFrameInfo()
        dInfo = {
            'FightIndex': oHero.Query('FightIndex'),
            'Saved': iSaved,
            'WarMask': self.m_WarMask,
            'Round': self.m_Round,
            'Cycle': self.m_Cycle,
            'ReNo': self.m_ReportID,
            'WarNo': self.m_SID,
            'PlayType': self.GetReportPlayType(),
            'Type': iType,
            'Hero': oHero.m_SID,
            'HeroID': oHero.m_ID,
            'Pay': dPayInfo,
            'RealDie': oHero.IsRealDied(),
            'CurWarCash': oHero.m_WarCash,
            'Report': dReport,
            'Team': dTeamData,
            'DoneLock': lDoneUnLock,
            'DayTrial': dDayTrialInfo,
            'OverType': self.Query('OverType', SETTLE_OVER_NORMAL),
            'Cheek': lstCheek,
            'BossLevel': lstBossLevel,
            'FrameInfo': dFrameInfo,
            'ModeType': self.m_ModeType,
            'ExtGSCashInfo': dExtGSCashInfo,
            'EndlessPassLevelNum': iEndlessPassLevelNum,
            'EndlessKillBossNum': iEndlessKillBossNum,
            'HPMax': oHero.QueryAttr('HPMax'),
            'Device': oHero.GetDeviceSID(),
            'SeasonNum': self.m_SeasonNum,
            'WarStartSeason': self.m_WarStartSeason,
            'EndLessStartLayer': self.GetEndLessStartLayer() }
        lstBene = oHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER)
        if lstBene:
            dInfo['Bene'] = lstBene
        lstWeapon = oHero.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
        lstWeaponType = []
        for oWeapon in lstWeapon:
            if oWeapon.m_Type not in lstWeaponType:
                lstWeaponType.append(oWeapon.m_Type)
        
        if lstWeaponType:
            dInfo['WeaponType'] = lstWeaponType
        oSeasonSuitElement = self.GetSeasonSuitElement()
        if oSeasonSuitElement:
            dInfo['SuitInfo'] = oSeasonSuitElement.GetSeasonSuitData(oHero.m_ID)
            dInfo['SuitTemp'] = oSeasonSuitElement.GetCurSuitTemp(oHero.m_PlayerID)
        oWeaponStore = self.GetComponent('WeaponStoreElement')
        if oWeaponStore:
            dInfo['WeaponStoreAnimaInfo'] = oWeaponStore.GetInjectWeaponInfo(pid)
        oWandElement = self.GetWandElement()
        if oWandElement:
            dInfo['WandInfo'] = oWandElement.GetCurWandData(oHero)
        oDiceElement = self.GetDiceElement()
        if oDiceElement:
            dInfo['DiceInfo'] = oDiceElement.GetCurDiceData(oHero)
        oBackPackElement = self.GetBackpackElement()
        if oBackPackElement:
            dInfo['BackPackInfo'] = oBackPackElement.GetCurBackPackData(oHero)
        return dInfo

    
    def CreateLevelBigDataInfo(self, dWarReport, iLevel, pid):
        if not dWarReport['Report'] or 'SettleErr' in dWarReport['Report']:
            return { }
        dLevelReport = dWarReport['Report'][iLevel]
        oHero = self.GetHeroByPlayer(pid)
        dBigDataReport = self.GenerateCommonBigDataInfo(dWarReport, dLevelReport, oHero)
        oBigDataAnaMgr = self.GetComponent('BigDataAnalyseMgr')
        if oBigDataAnaMgr:
            dBigDataReport['BigDataAna'] = { }
            iLevelType = dBigDataReport['LevelType']
            if iLevelType in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
                oMonsterCom = oBigDataAnaMgr.GetCom('Monster')
                dBigDataReport['BigDataAna']['LevelMonster'] = oMonsterCom.GetLevelStatistics(pid, iLevel)
            if MODE_WEAPONSTORE in self.m_ModeType:
                if iLevelType == LEVEL_TYPE_BOSS or not dLevelReport['Finish']:
                    oWeaponStore = oBigDataAnaMgr.GetCom('WeaponStore')
                    if oWeaponStore:
                        dBigDataReport['BigDataAna']['WeaponStore'] = oWeaponStore.GetStatistics(pid)
                        oWeaponStore.Refresh(pid)
            oServantCom = oBigDataAnaMgr.GetCom('Servant')
            if oServantCom:
                dBigDataReport['BigDataAna']['Servant'] = oServantCom.GetLevelStatistics(pid, iLevel)
            oConquerCom = oBigDataAnaMgr.GetCom('Conquer')
            if oConquerCom:
                dBigDataReport['BigDataAna']['Conquer'] = oConquerCom.GetLevelStatistics(pid, iLevel)
            oLevelCtrl = self.GetComponent('LevelCtrl')
            if oLevelCtrl.m_CurNode and oLevelCtrl.m_CurNode.m_Level == iLevel:
                oWeaponCom = oBigDataAnaMgr.GetCom('Weapon')
                if oWeaponCom:
                    dBigDataReport['BigDataAna']['Weapon'] = oWeaponCom.GetLevelStatistics(pid)
                    iFinishLayer = 1 if oLevelCtrl.CheckLayerEndLevel() else 0
                    if not iFinishLayer and dWarReport['Type'] in (SETTLE_DIRECTLEAVE, SETTLE_LOSEWAR, SETTLE_SYSKICK, SETTLE_HANGUP):
                        iFinishLayer = 1
                    if iFinishLayer:
                        dBigDataReport['BigDataAna']['LayerWeapon'] = oWeaponCom.GetLayerStatistics(pid)
            oSeasonSuitCom = oBigDataAnaMgr.GetCom('SeasonSuit')
            if oSeasonSuitCom:
                dBigDataReport['BigDataAna']['SeasonSuit'] = oSeasonSuitCom.GetLevelStatistics(pid)
            oSpecialHeroSkillCom = oBigDataAnaMgr.GetCom('SpecialHeroSkill')
            if oSpecialHeroSkillCom:
                dBigDataReport['BigDataAna']['SpecialHeroSkill'] = oSpecialHeroSkillCom.GetStatistics(pid)
            oHeroSkillCom = oBigDataAnaMgr.GetCom('HeroSkill')
            if oHeroSkillCom:
                dBigDataReport['BigDataAna']['HeroSkill'] = oHeroSkillCom.GetStatistics(pid)
            oInscriptionCom = oBigDataAnaMgr.GetCom('Inscription')
            if oInscriptionCom:
                dBigDataReport['BigDataAna']['Inscription'] = oInscriptionCom.GetStatistics(pid)
            oSeasonBenedictionCom = oBigDataAnaMgr.GetCom('SeasonBenediction')
            if oSeasonBenedictionCom:
                dBigDataReport['BigDataAna']['SeasonBenediction'] = oSeasonBenedictionCom.GetLevelStatistics(pid)
            oDyingTimeAndRealDeathCom = oBigDataAnaMgr.GetCom('DyingAndRealDeath')
            if oDyingTimeAndRealDeathCom:
                dBigDataReport['BigDataAna']['DyingAndRealDeath'] = oDyingTimeAndRealDeathCom.GetLevelStatistics(pid)
            oBigDataAnaMgr.GetWandSeasonLevelStatistics(pid, dBigDataReport)
            oBigDataAnaMgr.GetDiceSeasonLevelStatistics(pid, dBigDataReport)
            oBigDataAnaMgr.GetSeason7LevelStatistics(pid, dBigDataReport)
        self.DealLevelEndlessTimeInfo(dBigDataReport)
        return dBigDataReport

    
    def GenerateCommonBigDataInfo(self, dWarReport, dReport, oHero):
        if not dReport or 'SettleErr' in dReport:
            return { }
        iType = dWarReport['InitType'] if 'InitType' in dWarReport else dWarReport['Type']
        iLevelResult = dReport.get('Result', 0)
        iType = iLevelResult if iLevelResult else iType
        oSurvivorElement = self.GetSurvivorElement()
        oLevelCtrl = self.GetComponent('LevelCtrl')
        dCommonBigData = {
            'WarMask': dWarReport['WarMask'] if 'WarMask' in dWarReport else 0,
            'FightIndex': dWarReport['FightIndex'],
            'Type': iType,
            'WarNo': dWarReport['WarNo'],
            'Round': dWarReport['Round'],
            'Cycle': dWarReport.get('Cycle', 0),
            'LevelType': dReport['LevelType'] if 'LevelType' in dReport else LEVEL_TYPE_NONE,
            'Layer': oLevelCtrl.m_LayerNum,
            'TeamNumber': len(dWarReport['Team']),
            'Hero': dWarReport['Hero'],
            'Die': dReport['Die'],
            'Injured': dReport['Injured'] // 100,
            'HpDown': dReport['HpDown'] // 100,
            'HpUp': dReport['HpUp'] // 100,
            'ShieldDown': dReport['ShieldDown'] // 100,
            'ShieldUp': dReport['ShieldUp'] // 100,
            'Damage': dReport['Damage'] // 100,
            'Kill': dReport['Kill'],
            'KillElite': dReport['KillElite'],
            'KillMonster': dReport['KillMonster'],
            'EnterHide': dReport['EnterHide'],
            'Relic': dReport['Relic'],
            'Talent': dReport['Talent'],
            'TalentGen': [],
            'FightTime': dReport['FightFrame'] // GAME_FRAME,
            'Cash': dReport['Cash'],
            'GSCash': 0 if self.IsLeavingAtFirstHall(dWarReport['Type']) else dReport['GSCash'],
            'PlayFrame': dReport.get('StayFrame', 0),
            'FightFrame': dReport['FightFrame'],
            'RemoveRelic': dReport['RemoveRelic'],
            'PlayType': self.GetReportPlayType(),
            'MaxWeaponDamage': dReport['MaxWeaponDamage'] // 100,
            'MaxWeaponDamageSID': dReport['MaxWeaponDamageSID'],
            'FPS': dReport['FPS'],
            'SystemInfo': dReport.get('SystemInfo', { }),
            'BenedGen': [],
            'Bened': [],
            'RelicRelife': dReport['RelicRelife'] if 'RelicRelife' in dReport else 0,
            'ModeType': dWarReport['ModeType'],
            'AddSuit': dReport['AddSuit'],
            'IsSurvivor': 1 if oSurvivorElement else 0,
            'CommonTalentGen': [],
            'CommonTalentChosen': dReport.get('CommonTalentChosen', []) }
        if self.IsOpenSeasonElement():
            dCommonBigData['Season'] = self.m_SeasonNum
        if oSurvivorElement:
            if self.m_PlayMode == PLAYMODE_SURVIVOR:
                iGrade = 0
                iExperience = 0
                if oHero.m_ID in oSurvivorElement.m_UpgradeMgr.m_HeroUpgradeInfo:
                    (iExperience, iGrade, _, _, _, _) = oSurvivorElement.m_UpgradeMgr.m_HeroUpgradeInfo[oHero.m_ID]
                iPhase = oSurvivorElement.m_Phase
                dSurvivorLevelData = {
                    'RareTalent': dReport['RareTalent'],
                    'RareTalentGen': dReport['RareTalentGen'],
                    'UpGradeTalent': dReport['UpGradeTalent'],
                    'UpGradeTalentGen': dReport['UpGradeTalentGen'],
                    'UpGradeRelic': dReport['UpGradeRelic'],
                    'UpGradeRelicGen': dReport['UpGradeRelicGen'],
                    'UpGradeWeapon': dReport['UpGradeWeapon'],
                    'UpGradeWeaponGen': dReport['UpGradeWeaponGen'],
                    'Grade': iGrade,
                    'Experience': iExperience,
                    'Phase': BIGDATA_BOSS_PHASE if dCommonBigData['LevelType'] != LEVEL_TYPE_FIGHT and iPhase > oSurvivorElement.m_MaxPhase else iPhase,
                    'PhaseDeath': dReport['PhaseDeath'] }
            elif self.m_PlayMode == PLAYMODE_NEWSURVIVOR:
                iPhase = oSurvivorElement.m_Phase
                dSurvivorLevelData = {
                    'RareTalent': dReport['RareTalent'],
                    'RareTalentGen': dReport['RareTalentGen'],
                    'PhaseDeath': dReport['PhaseDeath'],
                    'Phase': self.GetBigDataPhase(oSurvivorElement) }
            dCommonBigData.update(dSurvivorLevelData)
        if 'Enhancement' in dReport and 'EnhancementList' in dReport:
            dCommonBigData['Enhancement'] = dReport['Enhancement']
            dCommonBigData['EnhancementList'] = dReport['EnhancementList']
        for lstBened in dReport.get('BenedGen', []):
            for iBened in lstBened:
                dCommonBigData['BenedGen'].append(iBened)
            
        
        if 'Bened' in dReport:
            dCommonBigData['Bened'] = dReport['Bened']
        if 'FourthBened' in dReport:
            dCommonBigData['FourthBened'] = dReport['FourthBened']
        for lstTalent in dReport.get('TalentGen', []):
            for iTalent in lstTalent:
                dCommonBigData['TalentGen'].append(iTalent)
            
        
        for lstTalent in dReport.get('CommonTalentGen', []):
            for iTalent in lstTalent:
                dCommonBigData['CommonTalentGen'].append(iTalent)
            
        
        dCommonBigData['LevelID'] = dReport['CurLv'] if dReport.get('CurLv', 0) else dReport.get('LevelID', 0)
        dCommonBigData['FightLevel'] = dReport.get('FightLevel', 0)
        dCommonBigData['BossLevel'] = dReport.get('BossLevel', 0)
        dCommonBigData['Prog'] = dReport.get('Prog', 0)
        dCommonBigData['DreamGame'] = self.GenerateDreamGameBigDataInfo()
        oDayTrial = self.GetComponent('DayTrialElement')
        if oDayTrial:
            dCommonBigData['Trial'] = oDayTrial.GetReportData()
        if 'EventNpc' in dReport:
            dCommonBigData['EventNpc'] = dReport['EventNpc']
        if 'SeasonDamage' in dReport:
            dCommonBigData['SeasonDamage'] = dReport['SeasonDamage']
        if 'TrusteeshipFrame' in dReport and dReport['TrusteeshipFrame']:
            dCommonBigData['TrusteeshipFrame'] = dReport['TrusteeshipFrame']
        return dCommonBigData

    
    def CreatePhaseEndReport(self, pid, iType, iLeaveType = 0):
        oHero = self.GetHeroByPlayer(pid)
        lstTeamMember = self.GetAllHero()
        oReport = self.GetComponent('Warreport')
        if oReport:
            dReport = oReport.m_WarReportData.GetPlayerLevelStatustics(pid)
            tLayerLevel = oReport.m_WarReportData.m_CurIndex
        else:
            dReport = { }
            tLayerLevel = (0, 0)
        dInfo = {
            'FightIndex': oHero.Query('FightIndex'),
            'WarMask': self.m_WarMask,
            'Round': self.m_Round,
            'Cycle': self.m_Cycle,
            'ReNo': self.m_ReportID,
            'WarNo': self.m_SID,
            'TeamNumber': len(lstTeamMember),
            'PlayType': self.GetReportPlayType(),
            'Type': iType,
            'Hero': oHero.m_SID,
            'LayerLv': tLayerLevel,
            'Report': dReport,
            'Talent': oHero.m_TalentCon.GetAllTalentLevel(),
            'TalentSubDesc': oHero.m_TalentCon.GetAllTalentSubDesc(),
            'Relic': oHero.m_RelicCon.GetAllPerformLevel(),
            'NewCash': self.GetReportGSCash(oHero, iType),
            'Bened': oHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER),
            'CheckTips': oHero.Query('CheckTips', { }),
            'TodayDayTrailStartCnt': oHero.Query('TodayDayTrailStartCnt', 0),
            'LeaveType': iLeaveType,
            'UnlockSuit': oHero.Query('UnlockSuit', { }) }
        return dInfo

    
    def CreatePhaseBigDataInfo(self, dWarReport, iLevel):
        if not dWarReport['Report']:
            return { }
        dLevelReport = dWarReport['Report'][iLevel]
        dBigDataReport = self.GeneratePhaseBigDataInfo(dWarReport, dLevelReport)
        return dBigDataReport

    
    def GeneratePhaseBigDataInfo(self, dWarReport, dReport):
        if not dReport:
            return { }
        iType = dWarReport['Type']
        iLevelResult = dReport.get('Result', 0)
        iType = iLevelResult if iLevelResult else iType
        dCommonBigData = {
            'WarMask': dWarReport['WarMask'] if 'WarMask' in dWarReport else 0,
            'FightIndex': dWarReport['FightIndex'],
            'Type': iType,
            'WarNo': dWarReport['WarNo'],
            'Round': dWarReport['Round'],
            'Cycle': dWarReport.get('Cycle', 0),
            'LevelType': dReport['LevelType'] if 'LevelType' in dReport else LEVEL_TYPE_NONE,
            'TeamNumber': dWarReport['TeamNumber'],
            'Hero': dWarReport['Hero'],
            'Die': dReport['Die'],
            'Injured': dReport['Injured'] // 100,
            'HpDown': dReport['HpDown'] // 100,
            'HpUp': dReport['HpUp'] // 100,
            'ShieldDown': dReport['ShieldDown'] // 100,
            'ShieldUp': dReport['ShieldUp'] // 100,
            'Damage': dReport['Damage'] // 100,
            'Kill': dReport['Kill'],
            'KillElite': dReport['KillElite'],
            'KillMonster': dReport['KillMonster'],
            'Relic': dReport['Relic'],
            'Talent': dReport['Talent'],
            'TalentGen': [],
            'FightTime': dReport['FightFrame'] // GAME_FRAME,
            'Cash': dReport['Cash'],
            'PlayFrame': dReport.get('StayFrame', 0),
            'FightFrame': dReport['FightFrame'],
            'RemoveRelic': dReport['RemoveRelic'],
            'PlayType': self.GetReportPlayType(),
            'MaxWeaponDamage': dReport['MaxWeaponDamage'] // 100,
            'MaxWeaponDamageSID': dReport['MaxWeaponDamageSID'],
            'FPS': dReport['FPS'],
            'SystemInfo': dReport.get('SystemInfo', { }),
            'RelicRelife': dReport['RelicRelife'] if 'RelicRelife' in dReport else 0 }
        if 'Enhancement' in dReport and 'EnhancementList' in dReport:
            dCommonBigData['Enhancement'] = dReport['Enhancement']
            dCommonBigData['EnhancementList'] = dReport['EnhancementList']
        for lstTalent in dReport.get('TalentGen', []):
            for iTalent in lstTalent:
                dCommonBigData['TalentGen'].append(iTalent)
            
        
        dCommonBigData['LevelID'] = dReport['CurLv'] if dReport.get('CurLv', 0) else dReport.get('LevelID', 0)
        return dCommonBigData

    
    def GenerateDreamGameBigDataInfo(self):
        dInfo = { }
        lstChoose = []
        for iMode in ALL_MODETYPE:
            if iMode in self.m_ModeType:
                lstChoose.append('1')
                continue
            lstChoose.append('0')
        
        iIndex = ALL_MODETYPE.index(MODE_REAL_ENDLESS)
        if self.GetEndlessMode() == ENDLESS_TIME:
            lstChoose.insert(iIndex, '1')
        else:
            lstChoose.insert(iIndex, '0')
        lstChoose.reverse()
        dInfo['GameMode'] = ''.join(lstChoose)
        oRidingAlone = self.GetComponent('RidingAloneElement')
        if oRidingAlone:
            dInfo['RidingAlone'] = {
                'Difficulty': oRidingAlone.m_SpawnCnt,
                'RidingAloneBened': [
                    oRidingAlone.m_Bene] }
        return dInfo

    
    def GetEndlessReportInfo(self):
        oEndlessElement = self.GetEndlessElement()
        if not oEndlessElement:
            return (0, 0)
        return (oEndlessElement.m_PassLevelNum, oEndlessElement.m_KillBossNum)

    
    def CreateLevelEndReport(self, pid, iType, iLeaveType = 0):
        oHero = self.GetHeroByPlayer(pid)
        lstTeamMember = self.GetAllHero()
        oReport = self.GetComponent('Warreport')
        if oReport:
            dReport = oReport.m_WarReportData.GetPlayerLevelStatustics(pid)
            dTeamData = oReport.m_WarReportData.GetTeamMemberStatistics(lstTeamMember)
            tLayerLevel = oReport.m_WarReportData.m_CurIndex
        else:
            dReport = { }
            dTeamData = { }
            tLayerLevel = (0, 0)
        for iHero in lstTeamMember:
            oTeamHero = self.m_Game.GetObject(iHero)
            if not oTeamHero:
                continue
            dTeammateData = dTeamData.setdefault(iHero, { })
            dTeammateData['Name'] = oTeamHero.m_OwnerName
            dTeammateData['Hero'] = oTeamHero.m_SID
            dTeammateData['pid'] = oTeamHero.m_PlayerID
            dTeammateData['Account'] = oTeamHero.Query('Account', 0)
            lstWeaponInfo = self.GetWeaponInfo(oTeamHero, dTeamData[oTeamHero.m_ID])
            dTeammateData['Weapon'] = lstWeaponInfo
            dTeammateData['Relic'] = oTeamHero.m_RelicCon.GetAllPerformLevel()
            dTeammateData['Talent'] = oTeamHero.m_TalentCon.GetAllTalentLevel()
            dTeammateData['TalentSubDesc'] = oTeamHero.m_TalentCon.GetAllTalentSubDesc()
            dTeammateData['Bened'] = oTeamHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER)
        
        oWeaponAna = self.GetComponent('WeaponAnalyse')
        if oWeaponAna:
            dWeaponAnalyse = oWeaponAna.ExportWeaponAnalyse(pid)
        else:
            dWeaponAnalyse = { }
        dUnlock = { }
        dAdjustWeaponInfo = { }
        oUnlockProgressCon = oHero.m_UnlockProgressCon
        if oUnlockProgressCon:
            dUnlock = dict(oUnlockProgressCon.GetProgress())
            dAdjustWeaponInfo = oUnlockProgressCon.GetAdjustWeaponData()
        lstWeaponInfo = self.GetWeaponInfo(oHero, dTeamData[oHero.m_ID])
        iEndlessCurLevelNum = self.GetEndlessCurLevelNum()
        iLayerNum = tLayerLevel[0]
        dInfo = {
            'FightIndex': oHero.Query('FightIndex'),
            'WarMask': self.m_WarMask,
            'Round': self.m_Round,
            'Cycle': self.m_Cycle,
            'ReNo': self.m_ReportID,
            'WarNo': self.m_SID,
            'Team': dTeamData,
            'PlayType': self.GetReportPlayType(),
            'Type': iType,
            'Hero': oHero.m_SID,
            'LayerLv': tLayerLevel,
            'Report': dReport,
            'WeaponAna': dWeaponAnalyse,
            'UnlockProgress': dUnlock,
            'AdjustWeaponInfo': dAdjustWeaponInfo,
            'Weapon': lstWeaponInfo,
            'Talent': oHero.m_TalentCon.GetAllTalentLevel(),
            'TalentSubDesc': oHero.m_TalentCon.GetAllTalentSubDesc(),
            'Relic': oHero.m_RelicCon.GetAllPerformLevel(),
            'NewCash': self.GetReportGSCash(oHero, iType),
            'Bened': oHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER),
            'CheckTips': oHero.Query('CheckTips', { }),
            'TodayDayTrailStartCnt': oHero.Query('TodayDayTrailStartCnt', 0),
            'LeaveType': iLeaveType,
            'UnlockSuit': oHero.Query('UnlockSuit', { }),
            'ModeType': self.m_ModeType,
            'EndlessCurLevelNum': iEndlessCurLevelNum,
            'BaseLayer': self.GetBaseLayer(iLayerNum),
            'EndlessMode': self.GetEndlessMode(),
            'SeasonNum': self.m_SeasonNum }
        return dInfo

    
    def GetWeaponInfo(self, oHero, dData):
        lstWeapon = oHero.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
        lstWeapon.sort(key = (lambda x: x.m_Pos))
        if MODE_WEAPONSTORE in self.m_ModeType:
            oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
            if oWeaponStoreElement:
                lstChangeWeapon = oWeaponStoreElement.GetWeaponStoreChangeWeapon(oHero, lstWeapon)
                lstWeapon = lstChangeWeapon
        lstWeaponInfo = []
        iTotalDam = 0
        for oWeapon in lstWeapon:
            iDam = dData['WeaponDamage'][oWeapon.m_ID] if oWeapon.m_ID in dData['WeaponDamage'] else 0
            iTotalDam += iDam
        
        for oWeapon in lstWeapon:
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            lstInscription = oInscriptionCom.GetAllInscription(iFill = 0) if oInscriptionCom else []
            oEnhanceCom = oWeapon.GetComponent('Enhance')
            lstEnhance = oEnhanceCom.GetAllEnhanceSID() if oEnhanceCom else []
            iWeapon = oWeapon.m_ID
            iDam = dData['WeaponDamage'][iWeapon] if iWeapon in dData['WeaponDamage'] else 0
            iWeaknessTimes = dData['WeaknessTimes'][iWeapon] if iWeapon in dData['WeaknessTimes'] else 0
            iDebuffTimes = dData['DebuffTimes'][iWeapon] if iWeapon in dData['DebuffTimes'] else 0
            iRatio = int(iDam * 10000 / iTotalDam) if iTotalDam else 0
            iWeaponSkin = oWeapon.m_Shape
            lstWeaponInfo.append([
                oWeapon.m_SID,
                oWeapon.m_BaseGrade,
                oWeapon.m_ElementType,
                lstInscription,
                lstEnhance,
                iDam,
                iDebuffTimes,
                iWeaknessTimes,
                iRatio,
                iWeaponSkin])
        
        return lstWeaponInfo

    
    def GetPlayerBuildInfo(self, pid):
        oHero = self.GetHeroByPlayer(pid)
        if not oHero:
            return { }
        dInfo = { }
        dInfo['Hero'] = oHero.m_SID
        dInfo['Relic'] = oHero.m_RelicCon.GetAllPerformLevel()
        dInfo['Talent'] = oHero.m_TalentCon.GetAllTalentLevel()
        dInfo['TalentSubDesc'] = oHero.m_TalentCon.GetAllTalentSubDesc()
        dInfo['Bened'] = oHero.m_BenedictionCon.GetBenedictionSID()
        lstWeapon = oHero.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
        lstWeapon.sort(key = (lambda x: x.m_Pos))
        if MODE_WEAPONSTORE in self.m_ModeType:
            oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
            if oWeaponStoreElement:
                lstChangeWeapon = oWeaponStoreElement.GetWeaponStoreChangeWeapon(oHero, lstWeapon)
                lstWeapon = lstChangeWeapon
        lstWeaponInfo = []
        for oWeapon in lstWeapon:
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            lstInscription = oInscriptionCom.GetAllInscription(iFill = 0) if oInscriptionCom else []
            oEnhanceCom = oWeapon.GetComponent('Enhance')
            lstEnhance = oEnhanceCom.GetAllEnhanceSID() if oEnhanceCom else []
            lstWeaponInfo.append([
                oWeapon.m_SID,
                oWeapon.m_Grade,
                oWeapon.m_ElementType,
                lstInscription,
                lstEnhance])
        
        dInfo['Weapon'] = lstWeaponInfo
        return dInfo

    
    def GetSeasonLevelEndInfo(self, pid):
        lstSeasonElement = self.GetCurSeasonAllElement()
        dSeasonLevelEndInfo = { }
        for sElement in lstSeasonElement:
            oElement = self.GetComponent(sElement)
            if not oElement:
                continue
            dSeasonLevelEndInfo.update(oElement.GetLevelEndInfo(pid))
        
        return dSeasonLevelEndInfo

    
    def HandleLevelNoFinish(self, pid):
        oReportComponent = self.GetComponent('Warreport')
        if oReportComponent:
            oReportData = oReportComponent.m_WarReportData
            lstLevel = oReportData.m_Index2Level.get(oReportData.m_CurIndex, [])
            for iLevel in lstLevel:
                oReport = oReportData.GetLayerLevelReport(iLevel)
                if not oReport:
                    continue
                if pid not in oReport.m_PlayerData:
                    continue
                if not oReport.m_Finish:
                    oReport.SummaryLevelStayTime(pid, 0)
                    oReportData.SummaryLevelSuit(iLevel, pid)
            

    
    def HandlePlayerSettle(self, pid, iType, bGiveUpRecord = False):
        self.m_SettledPlayer[pid] = 1
        iRealSettleType = self.GetRealSettleType(iType, bGiveUpRecord)
        iGameID = self.m_Game.m_ID
        WarobjLog.Info('game:%s %s settle %s %s' % (iGameID, pid, iType, iRealSettleType))
        self.HandleLevelNoFinish(pid)
        dInfo = self.CreateWarEndReport(pid, iRealSettleType, bGiveUpRecord)
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        oHero = self.GetHeroByPlayer(pid)
        lib_server.L2SPlayerReport(iLGS, iGameID, pid, dInfo)
        
        try:
            dBigDataReport = self.CreateWarEndBigDataAnalyseInfo(pid, iType, dInfo)
            if dBigDataReport:
                lib_server.L2SPlayerWarEndBigData(iLGS, iGameID, pid, dBigDataReport)
        except:
            PythonError()

        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PLAYERSETTLE, oHero, {
            'SettleType': iRealSettleType,
            'pid': pid })
        self.HandleSeasonTaskReport(pid, iWarEnd = 1)
        oHero.OnSettleWar()
        
        try:
            cl_cnetwar.C2GSNowInfo(oHero)
        except:
            pass


    
    def HandleNewUnlockProgressReport(self, pid):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        oHero = self.GetHeroByPlayer(pid)
        dNewUnlcokProgress = oHero.m_NewUnlockProgressMgr.LevelReport() if oHero and oHero.m_NewUnlockProgressMgr else { }
        if not dNewUnlcokProgress:
            return None
        lib_server.L2SPlayerNewUnlockProgress(iLGS, iGameID, pid, dNewUnlcokProgress)

    
    def HandlePlayerLevelReport(self, pid, iType, iLeaveType = 0):
        if self.m_PlayMode == PLAYMODE_MOBILE_DEMO:
            return None
        if pid not in self.m_PlayerMask['Room']:
            return None
        oHero = self.GetHeroByPlayer(pid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PLAYERLEVELREPORT_BEFORE, oHero, { })
        self.HandleAchievementReport(pid)
        self.HandleSeasonTaskReport(pid)
        self.HandleNewUnlockProgressReport(pid)
        self.HandleLevelNoFinish(pid)
        dInfo = self.CreateLevelEndReport(pid, iType, iLeaveType)
        if MODE_WEAPONSTORE in self.m_ModeType:
            oWeaponStoreCom = oHero.m_WeaponStoreCon
            oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
            dAnimaChangeData = oWeaponStoreElement.DealLevelWeaponAnimaInfo(pid)
            lstSavePos = oWeaponStoreElement.GetUnAnimaPos(pid, oWeaponStoreCom.m_LevelSavePos)
            dWeaponStoreSaveData = { }
            if lstSavePos:
                dWeaponStoreSaveData = oWeaponStoreCom.GetWeaponSaveInfo(lstSavePos)
                oWeaponStoreCom.m_LevelSavePos = []
            if dAnimaChangeData:
                dWeaponStoreSaveData.update(dAnimaChangeData)
            if dWeaponStoreSaveData:
                dInfo['WeaponStore'] = dWeaponStoreSaveData
                oSave = self.GetComponent('SaveElement')
                if oSave.CheckHasSaved():
                    oSave.SaveCurWeaponRecord()
                    oSave.SaveCurWeaponDropRecord()
        dSeasonLevelEndInfo = self.GetSeasonLevelEndInfo(pid)
        if dSeasonLevelEndInfo:
            dInfo['SeasonInfo'] = dSeasonLevelEndInfo
        oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        iEndLevel = oScene.m_Level if oScene else 0
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SPlayerLevelReport(iLGS, iGameID, pid, dInfo)
        lstLevel = list(dInfo['Report'])
        oWeaponAna = self.GetComponent('WeaponAnalyse')
        if oWeaponAna:
            oBigDataAna = self.GetComponent('BigDataAnalyseMgr')
            if oBigDataAna:
                dWeaponBigData = oWeaponAna.ExportWeaponAnalyseToBigData(pid)
                oWeaponCom = oBigDataAna.GetCom('Weapon')
                oWeaponCom.AddLevelWeaponAna(pid, dWeaponBigData)
                iLayer = dInfo['LayerLv'][0]
                for iLevel in lstLevel:
                    dLevelReport = dInfo['Report'].get(iLevel, { })
                    iLevelType = dLevelReport['LevelType'] if 'LevelType' in dLevelReport else LEVEL_TYPE_NONE
                    oWeaponCom.AddLayerWeaponAna(pid, iLayer, dWeaponBigData, iLevelType)
                
            oWeaponAna.ClearWeaponAnalyse(pid)
        for iLevel in lstLevel:
            
            try:
                dBigDataReport = self.CreateLevelBigDataInfo(dInfo, iLevel, pid)
            except:
                PythonError()
                continue

            if not dBigDataReport:
                continue
            if iEndLevel == iLevel:
                dBigDataReport['Type'] = iType
            lib_server.L2SPlayerLevelBigData(iLGS, iGameID, pid, dBigDataReport)
        
        oCheckCheatElement = self.GetComponent('CheckCheatElement')
        if oCheckCheatElement:
            oCheckCheatElement.CheckLevelCash(oHero.m_ID, oHero.Cash(), oHero.GSCash())
            oCheckCheatElement.CheckPyErrorBusted(oHero)
        
        try:
            cl_snetwar.GS2CNowSeed(oHero)
        except:
            pass


    
    def DealLevelEndlessTimeInfo(self, dInfo):
        oEndlessElement = self.GetComponent('EndlessElement')
        if not oEndlessElement:
            return None
        iDuration = 0
        iRemain = 0
        if oEndlessElement.m_Totaltime and oEndlessElement.m_StartEndless and oEndlessElement.m_RemainFrame:
            oEndlessElement.UpdateRemainTime()
            iDuration = Frame2Time(oEndlessElement.m_CurLevelStartRemainFarme - oEndlessElement.m_RemainFrame - oEndlessElement.m_CurLevelAddFrame)
            iRemain = Frame2Time(oEndlessElement.m_RemainFrame)
        dInfo['Duration'] = iDuration
        dInfo['RemainTime'] = iRemain

    
    def DealWarEndlessTimeInfo(self, dInfo):
        oEndlessElement = self.GetComponent('EndlessElement')
        if not oEndlessElement:
            return None
        iDuration = 0
        iRemainTime = oEndlessElement.m_InitTime
        if oEndlessElement.m_Totaltime and oEndlessElement.m_StartEndless:
            oEndlessElement.UpdateRemainTime()
            iRemainTime = Frame2Time(oEndlessElement.m_RemainFrame)
            iDuration = oEndlessElement.m_Totaltime - iRemainTime
        dInfo['Duration'] = iDuration
        dInfo['RemainTime'] = iRemainTime

    
    def HandleBuyItemReport(self, pid, iAmount, sReason, iType):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        dReport = {
            'Reason': sReason,
            'Cash': abs(iAmount),
            'Type': iType,
            'WarMask': self.m_WarMask,
            'WarNo': self.m_SID }
        lib_server.L2SPlayerBuyItemReport(iLGS, iGameID, pid, dReport)

    
    def HandleUpGradeReport(self, pid, iGrade, iPhase, iFightFrame):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        dReport = {
            'Grade': iGrade,
            'WarMask': self.m_WarMask,
            'Phase': iPhase,
            'FightFrame': iFightFrame }
        lib_server.L2SPlayerSurvivoUpGradeBigData(iLGS, iGameID, pid, dReport)

    
    def HandlePhaseEndReport(self, pid, iPhase, iGrade, iExperience):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        iType = SETTLE_LOSEWAR
        dPhaseEndReport = self.CreatePhaseEndReport(pid, iType)
        lstLevel = list(dPhaseEndReport['Report'])
        oBigDataAnaMgr = self.GetComponent('BigDataAnalyseMgr')
        oServantCom = None
        oDyingAndRealDeath = None
        if oBigDataAnaMgr:
            oServantCom = oBigDataAnaMgr.GetCom('Servant')
            oDyingAndRealDeath = oBigDataAnaMgr.GetCom('DyingAndRealDeath')
        for iLevel in lstLevel:
            dBigDataReport = self.CreatePhaseBigDataInfo(dPhaseEndReport, iLevel)
            dBigDataReport['Phase'] = iPhase
            dBigDataReport['Grade'] = iGrade
            dBigDataReport['Experience'] = iExperience
            if oServantCom:
                dBigDataReport['Servant'] = oServantCom.GetLevelStatistics(pid, iLevel)
            if oDyingAndRealDeath:
                dBigDataReport['DyingAndRealDeath'] = oDyingAndRealDeath.GetLevelStatistics(pid)
            lib_server.L2SPlayerPhaseEndBigData(iLGS, iGameID, pid, dBigDataReport)
        

    
    def SendIntervalPhaseBigData(self, pid, iPhase, dData):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        dData['Phase'] = iPhase
        dData['WarNo'] = self.m_SID
        dData['Round'] = self.m_Round
        dData['WarMask'] = self.m_WarMask
        dData['TeamNumber'] = len(self.GetAllHero())
        dData['Type'] = SETTLE_LOSEWAR
        lib_server.L2SPlayerIntervalPhaseBigData(iLGS, iGameID, pid, dData)

    
    def SendDeviceChallengeBigData(self, pid, dData):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        oHero = self.GetHeroByPlayer(pid)
        dData['WarMask'] = self.m_WarMask
        dData['WarNo'] = self.m_SID
        dData['Round'] = self.m_Round
        dData['Cycle'] = self.m_Cycle
        dData['TeamNumber'] = len(self.GetAllHero())
        dData['Hero'] = oHero.m_SID
        lib_server.L2SDeviceChallengeBigData(iLGS, iGameID, pid, dData)

    
    def HandleAchievementReport(self, pid, dAchievement = None):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        if not dAchievement:
            oHero = self.GetHeroByPlayer(pid)
            dAchievement = oHero.m_Achievement.LevelReport() if oHero and oHero.m_Achievement else None
            if not dAchievement:
                return None
        lib_server.L2SPlayerAchievement(iLGS, iGameID, pid, dAchievement)

    
    def HandleRecordReport(self, pid, dReport):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SPlayerRecord(iLGS, iGameID, pid, dReport)

    
    def HandleUnlockProgress(self, pid, dInfo):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SPlayerUnlockProgress(iLGS, iGameID, pid, dInfo)

    
    def HandleWeaponStoreSave(self, pid, dInfo):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SPlayerWeaponStoreSave(iLGS, iGameID, pid, dInfo)

    
    def HandlePlayerUnWarSetInfo(self, pid, dInfo):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SPlayerUnWarSetInfo(iLGS, iGameID, pid, dInfo)

    
    def HandleSeasonTaskReport(self, pid, dSeasonTask = None, iWarEnd = 0):
        iLGS = self.m_PlayerMask['All'][pid]['LGS']
        iGameID = self.m_Game.m_ID
        if not dSeasonTask:
            oHero = self.GetHeroByPlayer(pid)
            dSeasonTask = oHero.m_SeasonTaskMgr.SeasonTaskChangedReport() if oHero and oHero.m_SeasonTaskMgr else None
            if not dSeasonTask:
                return None
        dInfo = {
            'WarEnd': iWarEnd }
        if 'SeasonTask' in dSeasonTask:
            dInfo['SeasonTask'] = dSeasonTask['SeasonTask']
        if 'SeasonTaskExtInfo' in dSeasonTask:
            dInfo['SeasonTaskExtInfo'] = dSeasonTask['SeasonTaskExtInfo']
        lib_server.L2SPlayerSeasonTask(iLGS, iGameID, pid, dInfo)

    
    def RoomBroadcastNotify(self, iChat, dReplaceInfo):
        lstPlayer = self.GetRoomPlayer()
        for pid in lstPlayer:
            cl_notify.SendCommonNotify(self.m_Game, [
                pid], iChat, dReplaceInfo)
        

    
    def GetPropValue(self, sAttr, iSID):
        if sAttr == 'Suit':
            oSuitElement = self.GetComponent('SuitElement')
            if not oSuitElement:
                return []
            lstRes = oSuitElement.m_Condtion[SUIT_RELIC][iSID] if iSID in oSuitElement.m_Condtion[SUIT_RELIC] else []
            lstSuit = [ x[0] for x in lstRes ]
            return lstSuit
        return []

    
    def GetEndlessElement(self):
        oEndlessElement = self.GetComponent('EndlessElement')
        if oEndlessElement:
            return oEndlessElement
        return self.GetComponent('RealEndlessElement')

    
    def IsEndless(self):
        oEndlessElement = self.GetEndlessElement()
        if oEndlessElement and oEndlessElement.IsEndless():
            return 1
        return 0

    
    def GetBaseLayer(self, iLayerNum):
        oEndlessElement = self.GetEndlessElement()
        if not oEndlessElement:
            return iLayerNum
        iBaseLayer = oEndlessElement.GetBaseLayer(iLayerNum)
        return iBaseLayer

    
    def GetEndlessBossAttrAdjust(self):
        oEndlessElement = self.GetEndlessElement()
        if not oEndlessElement or not oEndlessElement.IsEndless():
            return { }
        return oEndlessElement.m_BossAttrAdjust

    
    def IsEndlessTimeOut(self):
        oEndlessElement = self.GetComponent('EndlessElement')
        if oEndlessElement:
            return oEndlessElement.IsTimeOut()
        return False

    
    def GetEndlessCurLevelNum(self):
        oEndlessElement = self.GetEndlessElement()
        if oEndlessElement:
            return oEndlessElement.m_CurLevelNum
        return 0

    
    def GetEndlessMode(self):
        oEndlessElement = self.GetEndlessElement()
        if oEndlessElement:
            return oEndlessElement.GetEndlessMode()
        return 0

    
    def GetEndLessStartLayer(self):
        oEndlessElement = self.GetEndlessElement()
        if oEndlessElement:
            return oEndlessElement.GetEndLessStartLayer()
        return 99999

    
    def AddRoundExtRule(self, iType, dParam, sReason):
        oRoundElement = self.GetComponent('RoundElement')
        if not oRoundElement:
            SendAlert('err', '周目组件不存在，添加额外规则失败 %s %s %s' % (iType, dParam, sReason))
            return None
        oRoundElement.AddRoundExtRule(iType, dParam, sReason)

    
    def AddDropGroup(self):
        self.m_DropGroupIdx += 1
        iGroup = self.m_DropGroupIdx
        self.m_DropGroup[iGroup] = { }
        return iGroup

    
    def SetDropGroup(self, oDrop, iGroup):
        if iGroup not in self.m_DropGroup:
            return None
        iHero = oDrop.m_Owner
        if not iHero:
            return None
        self.m_DropGroup[iGroup][iHero] = oDrop.m_ID

    
    def RemoveDropGroup(self, iGroup, iHero):
        if iGroup not in self.m_DropGroup:
            return None
        dDropGroup = self.m_DropGroup[iGroup]
        dDropGroup.pop(iHero, 0)
        if not dDropGroup:
            self.m_DropGroup.pop(iGroup)

    
    def GetDropGroupInfo(self, iGroup):
        if iGroup in self.m_DropGroup:
            return self.m_DropGroup[iGroup]
        return { }

    
    def CheckHasAIMember(self):
        oTeammateAI = self.GetComponent('TeammateAI')
        if not oTeammateAI:
            return 0
        if not oTeammateAI.CheckHasAIMember():
            return 0
        return 1

    
    def DebugMessage(self, dHero, sMsg):
        for iHero in dHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            cl_notify.GS2CMessage(oHero, sMsg)
        



class CBaseElement(cl_world.CEventObject):
    
    def __init__(self, oGame, nid, oData):
        super(CBaseElement, self).__init__(oGame, nid)
        self.m_Data = oData
        self.m_AddWarMsgcenterInfo = []

    
    def Init(self):
        pass

    
    def InitAfter(self):
        pass

    
    def Release(self):
        self.DoneAllWarMsgEvent()
        super(CBaseElement, self).Release()

    
    def OnHalfOpen(self):
        pass

    
    def SaveSeed(self, oHero):
        return { }

    
    def LoadSeed(self, dData):
        pass

    
    def GetLevelEndInfo(self, pid):
        return { }

    
    def GetWarMgr(self):
        return self.m_Game.m_WarMgr

    
    def AddWarMsgFunction(self, iMsg, oFunc, sKey, iOnce):
        oWarMgr = self.GetWarMgr()
        if not oWarMgr:
            WarobjLog.Alert('%s addwarmsgfunction no warmgr %s' % (self.m_Game.m_ID, sKey))
            return None
        self.m_AddWarMsgcenterInfo.append([
            iMsg,
            sKey])
        cl_msgcenter.AddFunction(oWarMgr, iMsg, oFunc, sKey, iOnce = iOnce)

    
    def DoneAllWarMsgEvent(self):
        oWarMgr = self.GetWarMgr()
        if not oWarMgr:
            WarobjLog.Alert('%s donewarevent no warmgr' % self.m_Game.m_ID)
            return None
        for iMsg, sKey in self.m_AddWarMsgcenterInfo:
            cl_msgcenter.DoneEvent(oWarMgr, iMsg, sKey)
        
        self.m_AddWarMsgcenterInfo = []



class CSeasonElement(CBaseElement):
    m_IsInheritSeasonElement = True
    m_CallFlag = 'SeasonElement'
    
    def __init__(self, oGame, nid, oData):
        super(CSeasonElement, self).__init__(oGame, nid, oData)
        self.m_SeasonFunc = { }
        self.m_AllSeasonFunc = oData.m_AllSeasonFunc
        if lib_flag.g_IsAuthorityRun and IsAssignSeason():
            self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerEnterGame, 'SeasonPlayerLogin', -1)
        self.InitSeasonNpcPut()
        self.InitSeasonChallengePut()

    
    def Init(self):
        self.OpenSeasonNpcPut()
        self.OpenSeasonChallengePut()

    
    def InitSeasonNpcPut(self):
        dConfig = self.m_Data.m_Config
        self.m_SeasonShopNpcSID = dConfig['SeasonShopNpcSID'] if 'SeasonShopNpcSID' in dConfig else 0

    
    def OpenSeasonNpcPut(self):
        if not self.m_SeasonShopNpcSID:
            return None
        dConfig = self.m_Data.m_Config
        if 'OpenBossShopNpc' in dConfig:
            self.AddWarMsgFunction(cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, 'CreateBossSeasonShop', iOnce = 0)
        if 'OpenFirstHallShopNpc' in dConfig:
            self.AddWarMsgFunction(cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'CreateFirstHallSeasonShop', iOnce = 1)

    
    def InitSeasonChallengePut(self):
        dConfig = self.m_Data.m_Config
        self.m_SeasonChallengePutWeight = dConfig.get('SeasonChallengePutWeight', { })
        self.m_SeasonChallengeIgnore = dConfig.get('SeasonChallengeIgnore', [])

    
    def OpenSeasonChallengePut(self):
        if not self.m_SeasonChallengePutWeight:
            return None
        self.AddWarMsgFunction(cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE_BEFORE, self.OnChooseChallengeBefore, 'ChooseSeasonChallengeBefore', iOnce = 0)
        self.AddWarMsgFunction(cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.OnChooseChallengeAfter, 'ChooseSeasonChallengeAfter', iOnce = 0)

    
    def OnPlayerEnterGame(self, oListener, oSender, dInfo):
        pid = dInfo['pid']
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iLGS = oWarMgr.m_PlayerMask['All'][pid]['LGS']
        iGameID = oGame.m_ID
        lib_server.L2SReSendSeasonInfo(iLGS, iGameID, pid, {
            'SeasonNum': oWarMgr.m_SeasonNum })

    
    def ChecKOpenFunc(self, iHero, iFuncType):
        if iHero not in self.m_SeasonFunc:
            return False
        return iFuncType in self.m_SeasonFunc[iHero]

    
    def AddSeasonFunc(self, iHero, iFuncType):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        dSeasonFunc = self.m_SeasonFunc
        if iFuncType not in self.m_AllSeasonFunc:
            return None
        if iHero not in dSeasonFunc:
            dSeasonFunc[iHero] = { }
        dSeasonFunc[iHero][iFuncType] = 1
        iPlayerID = oHero.m_PlayerID
        cl_snetwar.GS2CSeasonFunc(iPlayerID, self.m_SeasonFunc[iHero])
        SeasonLog.Info('add seasonfunc %d, %d, %d' % (self.m_Game.m_ID, iPlayerID, iFuncType))
        if len(dSeasonFunc[iHero]) == 1:
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.SynchronizeSeasonFunc, 'SynchronizeSeasonFunc')

    
    def ClearSeasonFunc(self, iHero, iFuncType):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        dSeasonFunc = self.m_SeasonFunc
        if iHero not in dSeasonFunc:
            return None
        dHeroSeasonFunc = dSeasonFunc[iHero]
        if iFuncType not in dHeroSeasonFunc:
            return None
        dHeroSeasonFunc.pop(iFuncType)
        iPlayerID = oHero.m_PlayerID
        cl_snetwar.GS2CSeasonFunc(iPlayerID, dHeroSeasonFunc)
        SeasonLog.Info('clear seasonfunc %d, %d, %d' % (self.m_Game.m_ID, iPlayerID, iFuncType))
        if not dHeroSeasonFunc:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'SynchronizeSeasonFunc')

    
    def SynchronizeSeasonFunc(self, oListener, oHero, dInfo):
        iHero = oHero.m_ID
        if iHero not in self.m_SeasonFunc:
            return None
        iPlayerID = oHero.m_PlayerID
        cl_snetwar.GS2CSeasonFunc(iPlayerID, self.m_SeasonFunc[iHero])

    
    def Release(self):
        if lib_flag.g_IsAuthorityRun and IsAssignSeason():
            self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'SeasonPlayerLogin', -1)
        for iHero in self.m_SeasonFunc:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'SynchronizeSeasonFunc')
        
        super(CSeasonElement, self).Release()

    
    def FilterAndFixAISeasonInfo(self, dDelegateAI):
        pass

    
    def DisableHeroSeasonEffect(self, oHero):
        return { }

    
    def EnableHeroSeasonEffect(self, oHero, dSeasonEffect):
        pass

    
    def EnableAIWhileList(self, oHero):
        pass

    
    def AddSeasonDropRecyclePrice(self, oHero, dDropPrice, sReason):
        dPrice = oHero.SetDefault('RecycleDropPrice', { })
        for iType, iPrice in dDropPrice.items():
            dPrice[iType] = (iPrice, sReason)
        

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if dInfo['LevelType'] != LEVEL_TYPE_BOSS or oLevelCtrl.CheckFinishWar():
            return None
        iLevelID = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'regrouprelicpos')
        self.CreateSeasonNpc(oLevelNode.m_Scene, oLevelNode, dAddInfo)

    
    def OnLevelStart(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelID = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        if not oLevelCtrl.CheckFirstHall():
            return None
        iLevelID = dInfo['LevelID']
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'seasonnpcpos')
        self.CreateSeasonNpc(oLevelNode.m_Scene, oLevelNode, dAddInfo)

    
    def CreateSeasonNpc(self, iScene, oLevelNode, dAddInfo):
        if not dAddInfo or not (self.m_SeasonShopNpcSID):
            SeasonLog.Alert('%s create seasonnpc err %s %s' % (self.m_Game.m_ID, dAddInfo, self.m_SeasonShopNpcSID))
            return None
        dAddInfo = DeepCopy(dAddInfo)
        dMsgInfo = {
            'NPC': self.m_SeasonShopNpcSID,
            'LevelNode': oLevelNode,
            'NPCInfo': dAddInfo,
            'Scene': iScene }
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
        if not dMsgInfo['NPC']:
            return None
        self.m_Game.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)

    
    def ValidPutSeasonChallenge(self, oWarMgr, iLevelID):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum == 1 and oLevelCtrl.m_LevelNum == 1:
            return 0
        iLevelType = oLevelCtrl.GetLevelType(iLevelID)
        if iLevelType != LEVEL_TYPE_FIGHT:
            return 0
        return 1

    
    def OnChooseChallengeBefore(self, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelID = dMsgInfo['Level']
        if not oLevelCtrl or not self.ValidPutSeasonChallenge(oWarMgr, iLevelID):
            return None
        if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and oLevelCtrl.m_LevelNum == oLevelCtrl.GetFightMaxLevel():
            oChallengeMgr = oLevelCtrl.m_RoomChallenge
            iAllRoom = oChallengeMgr.GetLevelRoomTotal(iLevelID)
            dMsgInfo['Info']['SeasonIgnore'] = {
                iLevelID: iAllRoom - 1 }
        dChallengeWeight = dMsgInfo['ChallengeWeight']
        dOldChallengeWeight = dict(dChallengeWeight)
        for iChallenge in self.m_SeasonChallengeIgnore:
            if iChallenge in dChallengeWeight:
                dChallengeWeight.pop(iChallenge, 0)
        
        dSeasonChallengePutWeight = self.m_SeasonChallengePutWeight
        if dSeasonChallengePutWeight:
            dChallengeWeight.update(dSeasonChallengePutWeight)
        SeasonLog.Debug('%d %d %s choosechallengebefore %s %s' % (self.m_Game.m_ID, iLevelID, self.m_CallFlag, dOldChallengeWeight, dChallengeWeight))

    
    def OnChooseChallengeAfter(self, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelID = dMsgInfo['LevelID']
        if not oLevelCtrl or not self.ValidPutSeasonChallenge(oWarMgr, iLevelID):
            return None
        oChallengeMgr = oLevelCtrl.m_RoomChallenge
        if not oChallengeMgr.ValidChooseChallenge(dMsgInfo):
            return None
        dSeasonChallengePutWeight = self.m_SeasonChallengePutWeight
        dChooseChallenge = dMsgInfo['ChooseChallenge']
        for (_, iRoomPos), iChallenge in dChooseChallenge.items():
            if iChallenge in dSeasonChallengePutWeight:
                dMsgInfo['IgnoreAppearPos'] = iRoomPos
                return None
        
        oGame = self.m_Game
        iGuaranteChallenge = ChooseKey(oGame, dSeasonChallengePutWeight)
        if iGuaranteChallenge:
            iAllRoom = oChallengeMgr.GetLevelRoomTotal(iLevelID)
            iGuaranteRoomPos = iAllRoom - 2
            if iGuaranteRoomPos < 0:
                return None
            SeasonLog.Debug('%d %d %s choosechallengeafter %s %s' % (oGame.m_ID, iLevelID, self.m_CallFlag, iGuaranteRoomPos, iGuaranteChallenge))
            dMsgInfo['IgnoreAppearPos'] = iGuaranteRoomPos
            dChooseChallenge[(iLevelID, iGuaranteRoomPos)] = iGuaranteChallenge



class CElementData(object):
    m_TimeList = ()
    m_Config = { }
    m_ExtRule = { }


class CSeasonElementData(CElementData):
    m_AllSeasonFunc = []


class CWarFlowElement(CBaseElement):
    m_StepFunc = { }
    m_CallFlag = 'WarMgr.Element'
    
    def __init__(self, oGame, nid, oData):
        super(CWarFlowElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Release = 0
        self.m_CurTimeIdx = 0
        self.m_Start = 0
        self.m_StartTime = 0

    
    def Init(self):
        self.OnInit()

    
    def GetCurFlowFrame(self):
        return Time2Frame(self.m_Data.m_TimeList[self.m_CurTimeIdx][0])

    
    def GetCurFlowStep(self):
        return self.m_Data.m_TimeList[self.m_CurTimeIdx][1]

    
    def Start(self):
        if not self.m_Data.m_TimeList:
            return None
        if self.m_Start:
            return None
        self.m_Start = 1
        self.m_StartTime = self.m_Game.GetFrameNum()
        iNextTime = self.GetCurFlowFrame()
        self.Call_Out(self.DoStep, iNextTime, self.m_CallFlag)

    
    def Stop(self):
        if self.m_Start:
            self.Remove_Call_Out(self.m_CallFlag)

    
    def Release(self):
        self.Stop()
        self.m_Release = 1
        super(CWarFlowElement, self).Release()

    
    def DoStep(self):
        if self.m_Release:
            return None
        if self.m_CurTimeIdx > len(self.m_Data.m_TimeList):
            return None
        dStep = self.GetCurFlowStep()
        if 'Act' in dStep:
            for sFunc in dStep['Act']:
                if sFunc not in self.m_StepFunc:
                    SendAlert('err', 'warflow not exist func %s' % sFunc)
                    continue
                func = self.m_StepFunc[sFunc]
                func(self)
            
        if 'Tips' in dStep:
            self.MiddleNotify(dStep['Tips'])
        self.m_CurTimeIdx += 1
        if self.m_CurTimeIdx < len(self.m_Data.m_TimeList):
            iNextTime = self.GetCurFlowFrame()
            iCallDelay = iNextTime + self.m_StartTime - self.m_Game.GetFrameNum()
            self.Call_Out(self.DoStep, iCallDelay, self.m_CallFlag)

    
    def MiddleNotify(self, lstMsg):
        for iMsg in lstMsg:
            GS2CShowText(self.m_Game, iMsg, cl_notify.MSG_TYPE_SAFEAREA)
        

    
    def OnInit(self):
        pass


