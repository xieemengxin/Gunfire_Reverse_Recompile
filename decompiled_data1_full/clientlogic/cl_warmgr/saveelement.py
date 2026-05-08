# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/saveelement.pyc
# RelativePath: clientlogic/cl_warmgr/saveelement.pyc
# Source Generated with Decompyle++
# File: saveelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, LEVEL_TYPE_BOSS, TYPE_RELIFE_GSCASH, UPDATE_RECORD_ALL, UPDATE_RECORD_HERO, WARRIOR_HERO, UPDATE_RECORD_DROP, SETTING_BOSS_RECORD, PLAY_TYPE_SINGLE, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_CASH, NWARRIOR_DROP_RELIC, NWARRIOR_DROP_GSCASH, VIRTUAL_ITEM_DROP, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, VIRTUAL_ITEM_GOLDENCUP, NWARRIOR_DROP_MAGIC_POWER
from cl_object.logging import WarobjLog
from cl_warmgr.levelline.linespawnaction import SpawnCreateBuild, SpawnTriggerGateCtrl
from cl_commondecorator import CheckFaultTolerance
import cl_msgcenter
import cl_notify
import cllib.lib_server as lib_server
import cl_reward
import cl_item

class CBasePlayerSave:
    
    def __init__(self, oGame, *args):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_PlayerID = 0

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, 'LoadRecord')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'LoadRecord')
        self.m_WarMgr = None
        self.m_Data = { }

    
    def ValidSaveLoad(self):
        return 0

    
    def GetPlayerID(self):
        if not self.m_PlayerID:
            self.m_PlayerID = self.m_WarMgr.GetAllPlayer()[0]
        return self.m_PlayerID

    
    def SaveLevelInfo(self, dInfo):
        pass

    
    def OnAddPlayer(self, oWarMgr, oTarget, dInfo):
        pass

    
    def GetHeroObj(self):
        iPlayer = self.GetPlayerID()
        return self.m_WarMgr.GetHeroByPlayer(iPlayer)

    
    def Save(self):
        dAll = { }
        if not self.ValidSaveLoad():
            return dAll
        dHero = self.GetSavedHeroInfo()
        if dHero:
            dAll['Hero'] = dHero
        dLevel = self.GetSavedLevelInfo()
        if dLevel:
            dAll['Level'] = dLevel
        dReport = self.GetSavedWarReport()
        if dReport:
            dAll['WarReport'] = dReport
        dBigData = self.GetSavedBigData()
        if dBigData:
            dAll['BigData'] = dBigData
        dDrop = self.GetSavedDropInfo()
        if dDrop:
            dAll['Drop'] = dDrop
        dWarMgr = self.GetSavedWarMgrInfo()
        if dWarMgr:
            dAll['WarMgr'] = dWarMgr
        if dAll:
            dAll['NoSceneObjNum'] = self.m_Game.m_NoSceneObjID
            dAll['SeasonNum'] = self.m_WarMgr.m_SeasonNum
            dAll['WarMask'] = self.m_WarMgr.m_WarMask
        return dAll

    
    def Load(self, dData, iTeamLoaded = 0):
        if not dData:
            return None
        if dData['WarNo'] != self.m_WarMgr.m_SID:
            return None
        if dData['Round'] != self.m_WarMgr.m_Round:
            return None
        if not self.ValidSaveLoad():
            return None
        self.m_Data = dData
        if not iTeamLoaded and 'WarMgr' in dData:
            self.LoadWarMgrInfo(dData)
        if 'Hero' in dData:
            self.LoadHeroInfo(dData)
        if 'WarReport' in dData:
            self.LoadWarReport(dData)
        if iTeamLoaded:
            return None
        if 'Level' in dData:
            self.LoadLevelInfo(dData)
        if 'BigData' in dData:
            self.LoadBigData(dData)

    
    def LoadLevelInfo(self, dData):
        if not dData:
            return None
        dLevel = dData['Level']
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl:
            oLevelCtrl.Load(dLevel)

    
    def SaveDropInfo(self, dInfo):
        if dInfo is None or 'BossLevelGoal' not in dInfo:
            return None
        oHero = self.GetHeroObj()
        oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        if not oScene:
            return None
        lstDrop = oScene.GetObjectsByType('Drop')
        dDrop = { }
        lstWeaponInfo = []
        lstCashInfo = []
        lstGSCashInfo = []
        lstRelicInfo = []
        lstMagicPower = []
        tGoldenCup = ()
        for iDrop in lstDrop:
            oDrop = self.m_Game.GetObject(iDrop)
            tPos = oDrop.GetPos()
            if oDrop.m_FightType == NWARRIOR_DROP_EQUIP:
                for oWeapon in oDrop.m_DropInfo.values():
                    lstWeaponInfo.append((oWeapon.Save(), tPos))
                
            if oDrop.m_FightType == NWARRIOR_DROP_CASH:
                for dCashInfo in oDrop.m_DropInfo.values():
                    lstCashInfo.append((dCashInfo, tPos))
                
            if oDrop.m_FightType == NWARRIOR_DROP_GSCASH:
                for dGSCashInfo in oDrop.m_DropInfo.values():
                    lstGSCashInfo.append((dGSCashInfo, tPos))
                
            if oDrop.m_FightType == NWARRIOR_DROP_RELIC:
                for iRelic in oDrop.m_DropInfo.values():
                    lstRelicInfo.append((iRelic, tPos))
                
            if oDrop.m_FightType == NWARRIOR_DROP_MAGIC_POWER:
                for dMagicPowerInfo in oDrop.m_DropInfo.values():
                    lstMagicPower.append((dMagicPowerInfo, tPos))
                
        
        lstCacheDrop = self.m_Game.m_ResMgr.GetDropCache()
        for dCacheDrop in lstCacheDrop:
            iType = dCacheDrop[1]
            tPos = dCacheDrop[2]
            lstDropData = dCacheDrop[3]
            if iType == NWARRIOR_DROP_EQUIP:
                for oWeapon in lstDropData:
                    lstWeaponInfo.append((oWeapon.Save(), tPos))
                
            if iType == NWARRIOR_DROP_CASH:
                for dCashInfo in lstDropData:
                    lstCashInfo.append((dCashInfo, tPos))
                
            if iType == NWARRIOR_DROP_GSCASH:
                for dGSCashInfo in lstDropData:
                    lstGSCashInfo.append((dGSCashInfo, tPos))
                
            if iType == NWARRIOR_DROP_RELIC:
                for iRelic in lstDropData:
                    lstRelicInfo.append((iRelic, tPos))
                
            if iType == NWARRIOR_DROP_MAGIC_POWER:
                for dMagicPowerInfo in lstDropData:
                    lstMagicPower.append((dMagicPowerInfo, tPos))
                
        
        lstNPC = oScene.GetObjectsByType('NPC')
        iGoldencupNum = 0
        for iNPC in lstNPC:
            oNpc = self.m_Game.GetObject(iNPC)
            if oNpc.m_FightType in (NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP):
                iGoldencupNum += 1
                tGoldenCup = GetGoldenCupData(oNpc)
        
        if iGoldencupNum > 1:
            WarobjLog.Alert(f'''goldencup num={iGoldencupNum} err''')
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iLevelID = 0
        if oLevelCtrl.m_CurNode:
            iLevelID = oLevelCtrl.m_CurNode.m_Level
        dDrop['WP'] = lstWeaponInfo
        dDrop['CH'] = lstCashInfo
        dDrop['GCH'] = lstGSCashInfo
        dDrop['RC'] = lstRelicInfo
        dDrop['MP'] = lstMagicPower
        dDrop['DNPC'] = tGoldenCup
        dDrop['LEVEL'] = iLevelID
        self.m_Data['Drop'] = dDrop

    
    def LoadDropInfo(self, dData):
        dDrop = dData['Drop']
        if not dDrop:
            return None
        iLevelID = dDrop.get('LEVEL', 0)
        if iLevelID:
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl.m_CurNode and oLevelCtrl.m_CurNode.m_Level != iLevelID:
                return None
        lstWeaponInfo = dDrop['WP']
        lstCashInfo = dDrop['CH']
        lstGSCashInfo = dDrop['GCH']
        lstRelicInfo = dDrop['RC']
        lstMagicPower = dDrop.get('MP', [])
        tGoldenCup = dDrop['DNPC']
        oHero = self.GetHeroObj()
        lstReward = []
        for dEquip, tPos in lstWeaponInfo:
            oEquip = cl_item.CreateEquip(self.m_Game, dEquip['SID'], cl_item.GetBaseGrade(dEquip), dEquip.get('ID', 0))
            oEquip.Load(dEquip)
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_EQUIP,
                    'DropInfo': [
                        oEquip],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        for dCash, tPos in lstCashInfo:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_CASH,
                    'DropInfo': [
                        dCash],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        for dGSCash, tPos in lstGSCashInfo:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_GSCASH,
                    'DropInfo': [
                        dGSCash],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        for iRelic, tPos in lstRelicInfo:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iRelic],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        for dMagicPower, tPos in lstMagicPower:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_MAGIC_POWER,
                    'DropInfo': [
                        dMagicPower],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        if tGoldenCup:
            (dGoldenCup, tPos) = tGoldenCup
            iNPC = dGoldenCup['SID']
            dReward = {
                'item': VIRTUAL_ITEM_GOLDENCUP,
                'info': {
                    'sid': iNPC,
                    'DropPos': tPos,
                    'RecordData': dGoldenCup } }
            lstReward.append(dReward)
        cl_reward.RewardItem(self.m_Game, oHero, lstReward, 'loaddrop', {
            'Player': oHero.m_ID })

    
    def SaveHeroInfo(self, dInfo = None):
        oHero = self.GetHeroObj()
        if oHero:
            dData = oHero.GetHeroDetailData(dInfo)
            self.m_Data['Hero'] = dData
            return dData

    
    def LoadHeroInfo(self, dData):
        if not dData:
            return None
        dHero = dData['Hero']
        oHero = self.GetHeroObj()
        if oHero:
            oHero.LoadHero(dHero)

    
    def SaveWarReport(self, dInfo = None):
        oReport = self.m_WarMgr.GetComponent('Warreport')
        if not oReport:
            return { }
        iPlayerID = self.GetPlayerID()
        dReport = oReport.Save(iPlayerID, dInfo)
        self.m_Data['WarReport'] = dReport

    
    def LoadWarReport(self, dData):
        oReport = self.m_WarMgr.GetComponent('Warreport')
        if not oReport:
            return None
        iPlayerID = self.GetPlayerID()
        oReport.Load(iPlayerID, dData['WarReport'])

    LoadWarReport = CheckFaultTolerance(LoadWarReport)
    
    def SaveBigData(self):
        oBigDataAnaMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if not oBigDataAnaMgr:
            return None
        dBigData = oBigDataAnaMgr.Save()
        self.m_Data['BigData'] = dBigData
        oWeaponAna = self.m_WarMgr.GetComponent('WeaponAnalyse')
        if not oWeaponAna:
            return None
        self.m_Data['BigData']['WeaponAna'] = oWeaponAna.SaveBigData()

    
    def LoadBigData(self, dData):
        oBigDataAnaMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if not oBigDataAnaMgr:
            return None
        oBigDataAnaMgr.Load(dData['BigData'])
        oWeaponAna = self.m_WarMgr.GetComponent('WeaponAnalyse')
        if not oWeaponAna:
            return None
        if 'WeaponAna' in dData['BigData']:
            oWeaponAna.LoadBigData(dData['BigData']['WeaponAna'])

    LoadBigData = CheckFaultTolerance(LoadBigData)
    
    def SaveWarMgrInfo(self):
        self.m_Data['WarMgr'] = self.m_WarMgr.Save()

    
    def SaveData(self, sKey, dData):
        self.m_Data[sKey] = dData

    
    def GetData(self, sKey, iDefault):
        if sKey in self.m_Data:
            return self.m_Data[sKey]
        return iDefault

    
    def LoadWarMgrInfo(self, dData):
        self.m_WarMgr.Load(dData['WarMgr'])

    
    def GetSavedLevelInfo(self):
        return self.m_Data.get('Level', { })

    
    def GetSavedHeroInfo(self):
        return self.m_Data.get('Hero', { })

    
    def GetSavedWarReport(self):
        return self.m_Data.get('WarReport', { })

    
    def GetSavedBigData(self):
        return self.m_Data.get('BigData', { })

    
    def GetSavedDropInfo(self):
        return self.m_Data.get('Drop', { })

    
    def GetSavedWarMgrInfo(self):
        return self.m_Data.get('WarMgr', { })

    
    def SaveCurRecord(self, dInfo):
        self.SaveHeroInfo(dInfo)
        self.SaveLevelInfo(dInfo)
        self.SaveWarReport(dInfo)
        self.SaveBigData()
        self.SaveDropInfo(dInfo)
        self.SaveWarMgrInfo()



class SingleGameSaveElement(CBaseElement, CBasePlayerSave):
    
    def __init__(self, oGame, nid, oData):
        CBaseElement.__init__(self, oGame, nid, oData)
        self.m_AutoSave = self.m_Data.m_Config.get('AutoSave', 0)
        self.m_PreventSL = self.m_Data.m_Config.get('PreventSL', 0)
        self.m_ForbidSaveFlag = 0
        self.m_BossRecord = 0
        self.m_AIMember = []
        CBasePlayerSave.__init__(self, oGame)
        self.InitAttention()

    
    def Init(self):
        CBaseElement.Init(self)
        CBasePlayerSave.Init(self)

    
    def InitAttention(self):
        if self.m_AutoSave:
            self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'AutoRecord')
        if self.m_PreventSL:
            self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'PreventSL')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.OnSettleWar, 'SingleGameSave')
        self.AddBossRecordAttention()

    
    def Load(self, dData, iTeamLoaded = 0):
        return CBasePlayerSave.Load(self, dData, iTeamLoaded)

    
    def AddBossRecordAttention(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, 'BossRecord', -1)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TALENT_GEN, self.OnTalentGen, 'BossRecord', -1)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, 'BossRecord', -1, 0)

    
    def Release(self):
        if self.m_AutoSave:
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'AutoRecord')
        if self.m_PreventSL:
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RELIFE, 'PreventSL')
        if self.m_BossRecord:
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'BossRecord')
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TALENT_GEN, 'BossRecord')
            cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'BossRecord')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'SingleGameSave')
        CBasePlayerSave.Release(self)
        CBaseElement.Release(self)

    
    def OnAddPlayer(self, oWarMgr, oTarget, dInfo):
        dCreateInfo = dInfo['CreateInfo']
        if 'IsAI' in dCreateInfo:
            return None
        self.m_PlayerID = dInfo['pid']
        self.Load(dCreateInfo.get('SavedRecord', { }))
        dSettings = dCreateInfo.get('Settings', { })
        if SETTING_BOSS_RECORD in dSettings and dSettings[SETTING_BOSS_RECORD]:
            self.SetBossRecord(1)

    
    def ValidSaveLoad(self):
        if not self.m_WarMgr.GetPlayType():
            return 0
        if not self.m_WarMgr.IsSingleGame(bExcludeAIMember = True):
            return 0
        if self.m_WarMgr.IsTransferGame():
            return 0
        return 1

    
    def CheckHasSaved(self):
        if not self.ValidSaveLoad():
            return 0
        if not self.m_Data:
            return 0
        if not self.IsAtSavePoint():
            return 0
        return 1

    
    def IsAtSavePoint(self):
        if not self.m_AutoSave:
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            if not oLevelCtrl or oLevelCtrl.m_CurNode.m_LevelType != LEVEL_TYPE_HALL:
                return 0
        if self.m_ForbidSaveFlag:
            return 0
        return 1

    
    def ManualSave(self):
        if not self.ValidSaveLoad():
            return None
        if not self.IsAtSavePoint():
            return None
        pid = self.GetPlayerID()
        WarobjLog.Info('%s %s manualsave' % (self.m_Game.m_ID, pid))
        self.RealSave()
        cl_notify.SendCommonNotify(self.m_Game, [
            pid], 7100, { })

    
    def AutoSave(self):
        if not self.ValidSaveLoad():
            return None
        self.RealSave()

    
    def RealSave(self, dInfo = None):
        self.SaveCurRecord(dInfo)
        self.HandleRecord(self.Save(), UPDATE_RECORD_ALL, dInfo)

    
    def HandleRecord(self, dSavedRecord, iUpdateType, dInfo = None):
        oHero = self.GetHeroObj()
        dReport = {
            'FightIndex': oHero.Query('FightIndex'),
            'PlayType': PLAY_TYPE_SINGLE,
            'Round': self.m_WarMgr.m_Round,
            'Cycle': self.m_WarMgr.m_Cycle,
            'WarNo': self.m_WarMgr.m_SID,
            'UpdateType': iUpdateType,
            'SavedRecord': dSavedRecord }
        if dInfo and 'TriggerCloudStore' in dInfo:
            dReport['TriggerCloudStore'] = 1
        pid = self.GetPlayerID()
        self.m_WarMgr.HandleRecordReport(pid, dReport)

    
    def SaveCurWeaponRecord(self):
        oHero = self.GetHeroObj()
        if oHero and 'Hero' in self.m_Data:
            dData = oHero.GetHeroWeaponDetailData()
            self.m_Data['Hero'].update(dData)
            self.HandleRecord({
                'Hero': dData }, UPDATE_RECORD_HERO)

    
    def SaveCurWeaponDropRecord(self):
        if 'Drop' not in self.m_Data:
            return None
        oHero = self.GetHeroObj()
        oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        if not oScene:
            return None
        lstDrop = oScene.GetObjectsByType('Drop')
        dDrop = self.m_Data['Drop']
        lstWeaponInfo = []
        for iDrop in lstDrop:
            oDrop = self.m_Game.GetObject(iDrop)
            tPos = oDrop.GetPos()
            if oDrop.m_FightType != NWARRIOR_DROP_EQUIP:
                continue
            for oWeapon in oDrop.m_DropInfo.values():
                lstWeaponInfo.append((oWeapon.Save(), tPos))
            
        
        lstCacheDrop = self.m_Game.m_ResMgr.GetDropCache()
        for dCacheDrop in lstCacheDrop:
            iType = dCacheDrop[1]
            if iType != NWARRIOR_DROP_EQUIP:
                continue
            tPos = dCacheDrop[2]
            lstDropData = dCacheDrop[3]
            for oWeapon in lstDropData:
                lstWeaponInfo.append((oWeapon.Save(), tPos))
            
        
        dDrop['WP'] = lstWeaponInfo
        self.HandleRecord({
            'Drop': dDrop }, UPDATE_RECORD_DROP)

    
    def SaveLevelInfo(self, dInfo):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        dLevel = {
            'LevelID': oLevelCtrl.m_CurNode.m_Level,
            'LayerNum': oLevelCtrl.m_LayerNum,
            'LevelNum': oLevelCtrl.m_LevelNum }
        if dInfo:
            dLevel.update(dInfo)
        dLevel.update(oLevelCtrl.Save())
        self.m_Data['Level'] = dLevel

    
    def ValidAutoSave(self):
        if not self.m_WarMgr.IsSingleGame():
            return 0
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        if oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_HALL and oLevelCtrl.m_LayerNum == 1:
            return 0
        oHero = self.GetHeroObj()
        oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        iLevel = oScene.m_Level if oScene else 0
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode or oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
            return 0
        return 1

    
    def OnLevelStart(self, oWarMgr, oTarget, dInfo):
        if not IsContinueGame(self.m_WarMgr, dInfo['LevelID']) and self.ValidAutoSave():
            self.AutoSave()

    
    def OnRelife(self, oWarMrg, oHero, dInfo):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if not self.ValidSaveLoad():
            return None
        HandleRelifeCnt(self, oHero, dInfo)
        HandleGSChange(self, dInfo)

    
    def OnLevelGoal(self, oWarMrg, dInfo):
        if not self.m_BossRecord:
            return None
        if dInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        if not self.ValidSaveLoad():
            return None
        if not self.IsAtSavePoint():
            return None
        if ExistBossLevelGoalMark(self.m_WarMgr, dInfo['LevelID']):
            return None
        self.RealSave({
            'BossLevelGoal': 1,
            'TriggerCloudStore': 1 })
        oHero = self.GetHeroObj()
        oWarMrg.HandleUnlockProgress(oHero.m_PlayerID, oHero.m_UnlockProgressCon.GetProgress())

    
    def OnMapLoadOK(self, oWarMrg, oHero, dMsgInfo):
        if GetCurLevelType(self.m_WarMgr) != LEVEL_TYPE_BOSS:
            return None
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'BossRecord')
        self.LoadDropInfo({
            'Drop': self.m_Data.get('Drop', { }) })
        if ExistBossRecord(self):
            CreateBossLevelBuild(self.m_WarMgr, dMsgInfo)

    
    def OnTalentGen(self, oWarMgr, oHero, dInfo):
        if GetCurLevelType(self.m_WarMgr) != LEVEL_TYPE_BOSS:
            return None
        if not CheckLevelPass(oWarMgr):
            return None
        if not self.ValidSaveLoad():
            return None
        oNpc = self.m_Game.GetObject(dInfo['NPC'])
        if not oNpc:
            WarobjLog.Alert('npc nonexistent')
            return None
        if self.m_BossRecord or ExistBossRecord(self):
            dTalent = dInfo['Talent']
            oNpc.SetTalentReward(oHero.m_PlayerID, dTalent)
            tData = GetGoldenCupData(oNpc)
            self.HandleRecord({
                'Drop': {
                    'DNPC': tData } }, UPDATE_RECORD_DROP)

    
    def OnSettleWar(self, oWarMgr, oHero, dInfo):
        self.m_ForbidSaveFlag = 1

    
    def SetBossRecord(self, iOpen):
        self.m_BossRecord = iOpen

    
    def GetAIMember(self):
        if not self.m_AIMember:
            oTeammateAI = self.m_WarMgr.GetComponent('TeammateAI')
            if oTeammateAI:
                self.m_AIMember = list(oTeammateAI.m_AIMember)
        return self.m_AIMember

    
    def LoadHeroInfo(self, dData):
        super().LoadHeroInfo(dData)
        if not self.GetAIMember():
            return None
        if 'AIMember' not in dData:
            return None
        for iPlayer in dData['AIMember']:
            oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
            if oHero:
                dHero = dData['AIMember'][iPlayer]
                oHero.LoadHero(dHero)
        

    
    def Save(self):
        dAll = CBasePlayerSave.Save(self)
        if not dAll:
            return dAll
        dAIMemberInfo = self.GetData('AIMember', { })
        if dAIMemberInfo:
            dAll['AIMember'] = dAIMemberInfo
        return dAll

    
    def SaveCurRecord(self, dInfo):
        super().SaveCurRecord(dInfo)
        self.SaveAIMember(dInfo)

    
    def SaveAIMember(self, dInfo):
        lstAIMember = self.GetAIMember()
        if not lstAIMember:
            return None
        dAIMemberInfo = { }
        for iPlayer in lstAIMember:
            oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
            if oHero:
                dAIMemberInfo[iPlayer] = oHero.GetHeroDetailData(dInfo)
        
        self.SaveData('AIMember', dAIMemberInfo)



def GetComponentClass(oWarMgr):
    return SingleGameSaveElement


def ExistBossRecord(oSaveElement):
    dLevelInfo = oSaveElement.GetSavedLevelInfo()
    if 'BossLevelGoal' in dLevelInfo:
        return True
    return False


def HandleRelifeCnt(oSaveElement, oHero, dInfo):
    dHeroInfo = oSaveElement.GetSavedHeroInfo()
    if not dHeroInfo or not dHeroInfo['RLF']:
        return None
    oReason = dInfo['RS']
    iType = oReason.Query('Type')
    if iType != TYPE_RELIFE_GSCASH:
        return None
    dCurRelifeInfo = oHero.Query('RelifeInfo', { })
    if TYPE_RELIFE_GSCASH in dCurRelifeInfo:
        dHeroInfo['RLF'][TYPE_RELIFE_GSCASH] = dCurRelifeInfo[TYPE_RELIFE_GSCASH]
    else:
        dHeroInfo['RLF'].pop(TYPE_RELIFE_GSCASH, None)
    dHeroInfo['SET']['GSCashRelifeTimes'] = oHero.QuerySavedData('GSCashRelifeTimes', 0)
    oSaveElement.HandleRecord({
        'Hero': {
            'RLF': dHeroInfo['RLF'],
            'SET': dHeroInfo['SET'] } }, UPDATE_RECORD_HERO)


def HandleGSChange(oSaveElement, dInfo):
    oReason = dInfo['RS']
    iCost = oReason.Query('Cost')
    if not iCost:
        return None
    dChangeInfo = {
        'ChangeCash': -iCost,
        'Reason': 'RelifeCost',
        'WarMask': oSaveElement.m_WarMgr.m_WarMask }
    lib_server.L2SChangeCash(0, oSaveElement.m_Game.m_ID, oSaveElement.GetPlayerID(), dChangeInfo)


def IsContinueGame(oWarMgr, iLevel):
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode:
        return False
    if 'ContinueGame' in oLevelNode.m_CustomData:
        return True
    return False


def ExistBossLevelGoalMark(oWarMgr, iLevel):
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode:
        return False
    if 'BossLevelGoal' in oLevelNode.m_CustomData:
        return True
    return False


def GetCurLevelType(oWarMgr):
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl or not (oLevelCtrl.m_CurNode):
        return 0
    return oLevelCtrl.m_CurNode.m_LevelType


def CheckLevelPass(oWarMgr):
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl or not (oLevelCtrl.m_CurNode):
        return 0
    return oLevelCtrl.m_CurNode.CheckLevelPass()


def CreateBossLevelBuild(oWarMgr, dMsgInfo):
    iLevelID = dMsgInfo['LevelID']
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    iDoorID = 26001
    if iLevelID in (1202001, 1202003):
        for lstLine in oLevelNode.m_RoomList:
            for oLine in lstLine:
                SpawnCreateBuild(oLine, [
                    iDoorID,
                    0])
                SpawnCreateBuild(oLine, [
                    57500,
                    0])
                SpawnTriggerGateCtrl(oLine, [
                    iDoorID,
                    0,
                    4])
            
        
    elif iLevelID in (1301002, 1301003):
        for lstLine in oLevelNode.m_RoomList:
            for oLine in lstLine:
                SpawnCreateBuild(oLine, [
                    iDoorID,
                    0])
                SpawnTriggerGateCtrl(oLine, [
                    iDoorID,
                    0,
                    4])
            
        


def GetGoldenCupData(oNpc):
    return (oNpc.Save(), oNpc.GetPos())

