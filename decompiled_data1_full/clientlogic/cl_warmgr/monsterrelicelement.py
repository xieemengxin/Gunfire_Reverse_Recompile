# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/monsterrelicelement.pyc
# RelativePath: clientlogic/cl_warmgr/monsterrelicelement.pyc
# Source Generated with Decompyle++
# File: monsterrelicelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import WARRIOR_ELITE, WARRIOR_BOSS, WARRIOR_MONSTER, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_RULE_EXCLUDEMONSTER, MONSTERRELIC_SUBRULE_MONSTER, MONSTERRELIC_SUBRULE_MONSTERTYPE, MONSTERRELIC_SUBRULE_DEFENDTREND, LEVEL_TYPE_HALL, RELIC_SUBMSG_GENERATE_CHOOSE, NWARRIOR_DROP_RELIC, NPC_CB_VALUE, NPC_CB_VALUELIST, PF_TYPE_RELIC, TREASURERELIC_GENERATELIST, TREASURERELIC_SELECTRELIC, MONSTER_CLASSIFY_BOXMONSTER, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, SIDE_TYPE_MONSTER, STATE_TIME_FOREVER, SOURCE_REASON_MODE_MONSTERRELIC, WARRIOR_NORMAL, VIRTUAL_ITEM_DROP, FAKEMG_MONSTERRELIC, MONSTERRELIC_SUBRULE_MONSTERSOURCE, DROP_REASON_MONSTERRELIC, NWARRIOR_DROP_DEMON, DYNAMIC_DEMON_MONSTERRELIC, RELIC_TYPE_CURSE, NWARRIOR_DROP_RELIC_CURSE, LEVEL_TYPE_FIGHT, PERFORMCHOOSE_TYPE_MONSTERRELIC
from cl_only import SendAlert, ChooseKey, ShufferList, DeepCopy, Functor, PY_FLAG_DEAD
from cl_platformdata import GetRelic2Monster
from cl_object.logging import WarrelicLog
from cl_npc import net
from cl_warmgr.bigdataanalyse import CMonsterRelicAnalyseCom
from cl_resmgr.aitempparam import GetAIConfParam
from cl_commondecorator import ChooseRewardEnd
import cl_msgcenter
import cl_putdata
import cl_perform
import cl_perform.load
import cl_snetwar
import cl_math
import cl_war
import cl_state
import cl_object.reason
import cl_reward
import cllib.lib_flag as lib_flag

class CMonsterRelicElement(CBaseElement):
    m_FightTypeDefine = {
        'Normal': WARRIOR_NORMAL,
        'Elite': WARRIOR_ELITE }
    
    def __init__(self, oGame, nid, oData):
        super(CMonsterRelicElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'MonsterRelicElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_PutRelic = []
        self.m_Relic2MonsterRelic = { }
        self.m_MonsterExcludeRelic = { }
        self.m_ChooseCount = self.m_Data.m_Config.get('PlayerChooseCnt', { })
        self.m_MonUseRelicCount = DeepCopy(self.m_Data.m_Config.get('MonsterUseRelicCnt', { }))
        dSeasonExtMonRelicCnt = self.m_Data.m_Config.get('SeasonExtMonRelicCnt', { })
        iSeason = self.m_WarMgr.m_SeasonNum
        if iSeason in dSeasonExtMonRelicCnt:
            for sType, iExtCnt in dSeasonExtMonRelicCnt[iSeason].items():
                for dCount in self.m_MonUseRelicCount.values():
                    if sType in dCount:
                        dCount[sType] += iExtCnt
                
            
        lstKillDropSeason = self.m_Data.m_Config.get('KillDropSeason', [])
        lstKillDropCycle = self.m_Data.m_Config.get('KillDropCycle', [])
        if self.m_WarMgr.m_SeasonNum in lstKillDropSeason or self.m_WarMgr.m_Cycle in lstKillDropCycle:
            self.m_KillDropRelic = 1
        else:
            self.m_KillDropRelic = 0
        self.m_QualityWeight = self.m_Data.m_Config.get('QualityWeight', { })
        self.m_TotalOptionCount = self.m_Data.m_Config.get('TotalOptionCnt', 24)
        self.m_OptionCount = self.m_Data.m_Config.get('OptionCnt', 6)
        self.m_OptionalCount = self.m_Data.m_Config.get('OptionalCnt', 2)
        self.m_AssignMonsterType = self.m_Data.m_Config.get('AssignMonsterType', { })
        dDropProbability = self.m_Data.m_Config.get('DropProbability', { })
        self.m_DropWeight = self.m_Data.m_Config.get('DropWeight', [
            30,
            10])
        self.m_FloorDropCnt = self.m_Data.m_Config.get('FloorDropCnt', 20)
        self.m_LevelDropLimit = self.m_Data.m_Config.get('LevelDropLimit', { })
        self.m_DelayPickTime = self.m_Data.m_Config.get('DelayPickTime', 500)
        self.m_DropProbability = { }
        for sFightType, iProb in dDropProbability.items():
            if sFightType in self.m_FightTypeDefine:
                self.m_DropProbability[self.m_FightTypeDefine[sFightType]] = iProb
        
        self.m_RelicMG = self.m_Data.m_Config.get('RelicMG', 0)
        self.m_EndlessConfigLayer = self.m_Data.m_Config.get('EndlessConfigLayer', 4)
        self.m_RelicWeight = { }
        self.m_LayerRelic = { }
        self.m_LayerSelect = { }
        self.m_SelectStep = { }
        self.m_SelectRelic = []
        self.m_SelectMonsterRelic = []
        self.m_MonUsedRelic = { }
        self.m_RoomRelic = { }
        self.m_ExtraRelic = { }
        self.m_MonUseExtRelic = { }
        self.m_MonsterRoom = { }
        self.m_RoomMonster = { }
        self.m_MonsterSummon = { }
        self.m_MonsterPrepareSummon = { }
        self.m_RoomSummonCnt = { }
        self.m_MonsterRelicRule = { }
        self.m_MonsterListenMsg = { }
        self.m_RoomStateCnt = { }
        self.m_RefreshRelic = { }
        self.m_BornPos = { }
        self.m_RoomDrop = { }
        self.m_LayerDrop = { }
        self.m_LevelReward = { }
        self.m_PlayerReward = { }
        self.m_KillMonsterCnt = 0
        self.m_DelayAddRelic = []
        self.m_Enable = 0
        self.m_CurLayer = 0
        self.m_LoadingPlayer = []
        self.m_ReEnter = []
        self.m_Master = 0
        self.m_DropInfo = { }

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, sFlag, -1, 0)

    
    def InitAfter(self):
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CMonsterRelicAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('MonsterRelic', oAnalyseCom)

    
    def Enable(self):
        if self.m_Enable:
            return None
        self.m_Enable = 1
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        self.m_Relic2MonsterRelic = GetRelic2Monster()
        self.m_MonsterExcludeRelic = cl_perform.load.GetMonsterExclude()
        setForbid = oWarMgr.GetForbidRelic()
        self.m_PutRelic = self.GetConfigReilc() - set(cl_perform.load.GetGameExcludeRelic(self.m_WarMgr.GetPlayType())) - setForbid
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, sFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, sFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, sFlag, iOnce = 0)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.OnPreRoomGoal, sFlag, iOnce = 0)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER, self.OnMonsterSuper, sFlag)
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerReady, sFlag)
        if self.m_KillDropRelic:
            oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, sFlag, SIDE_TYPE_MONSTER)
        self.AddHeroMapLoadOK()

    
    def GetConfigReilc(self):
        if self.m_RelicMG:
            clsMiniGame = self.m_Game.m_WarData.GetMiniGameData(self.m_RelicMG)
            if clsMiniGame:
                self.m_RelicWeight = clsMiniGame.m_ChooseWeight
                setPut = set(clsMiniGame.m_ChooseWeight)
            else:
                setPut = cl_putdata.GetAllPutMonsterRelic()
                WarrelicLog.Alert('灵界寻宝未配置遗物掉落%s' % self.m_RelicMG)
        else:
            setPut = cl_putdata.GetAllPutMonsterRelic()
        return set(cl_putdata.GetAllPutRelic()) & setPut

    
    def AddHeroMapLoadOK(self):
        oWarMgr = self.m_WarMgr
        oGame = self.m_Game
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.OnMapLoadOK)
        

    
    def SaveDropInfo(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl or oLevelCtrl.m_CurLType != LEVEL_TYPE_HALL:
            return { }
        if not oLevelCtrl.m_CurNode:
            return { }
        oScene = self.m_Game.m_SceneMgr.GetScene(oLevelCtrl.m_CurNode.m_Scene)
        if not oScene:
            return { }
        lstPlayer = self.m_WarMgr.GetAllPlayer()
        dDrop = { }
        for pid in lstPlayer:
            dDrop[pid] = []
        
        lstDrop = oScene.GetObjectsByType('Drop')
        iSourceReason = self.GetSourceReason()
        for iDrop in lstDrop:
            oDrop = self.m_Game.GetObject(iDrop)
            if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_RELIC or oDrop.m_SourceReason != iSourceReason:
                continue
            tPos = oDrop.GetPos()
            for pid in lstPlayer:
                if oDrop.m_Owner == self.m_WarMgr.GetHeroIDByPlayerID(pid):
                    for iRelic in oDrop.m_DropInfo.values():
                        dDrop[pid].append((iRelic, tPos, oDrop.m_Level))
                    
            
        
        return dDrop

    
    def LoadDropInfo(self, oHero):
        if oHero.m_PlayerID not in self.m_DropInfo:
            return None
        oResMgr = self.m_Game.m_ResMgr
        lstDrop = self.m_DropInfo.pop(oHero.m_PlayerID)
        iSourceReason = self.GetSourceReason()
        for iRelicSID, vPos, iLevel in lstDrop:
            dStaticInfo = {
                'DropLevel': iLevel,
                'DropSource': oHero.m_PlayerID,
                'SourceReason': iSourceReason }
            oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_RELIC, vPos, [
                iRelicSID], {
                'ValidRemoveCurseRelic': 1 }, dStaticInfo, oHero.m_ID)
        

    
    def Save(self):
        if not self.m_Enable:
            return { }
        dData = { }
        dData['LYS'] = DeepCopy(self.m_LayerSelect)
        dData['CLY'] = self.m_CurLayer
        dData['RD'] = self.m_RoomDrop
        dData['LD'] = self.m_LayerDrop
        dData['KMC'] = self.m_KillMonsterCnt
        dData['PR'] = self.m_PlayerReward
        dData['DROP'] = self.SaveDropInfo()
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_LayerSelect = dData['LYS']
        self.m_CurLayer = dData['CLY']
        self.m_RoomDrop = dData.get('RD', { })
        self.m_LayerDrop = dData.get('LD', { })
        self.m_KillMonsterCnt = dData.get('KMC', 0)
        self.m_PlayerReward = dData.get('PR', { })
        self.m_DropInfo = dData.get('DROP', { })
        self.Enable()
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag, iSub = -1, iOnce = 1)
        lstSelectRelic = []
        lstSelectMonsterRelic = []
        for lstLayerSelect in self.m_LayerSelect.values():
            for lstSelect in lstLayerSelect:
                iRelicSID = lstSelect[1]
                if not iRelicSID:
                    continue
                if iRelicSID not in self.m_Relic2MonsterRelic:
                    SendAlert('err', '怪物遗物%s 没配置对应遗物' % iRelicSID)
                    continue
                lstSelectRelic.append(iRelicSID)
                lstSelectMonsterRelic.append(self.m_Relic2MonsterRelic[iRelicSID])
            
        
        self.m_SelectRelic = lstSelectRelic
        self.m_SelectMonsterRelic = lstSelectMonsterRelic

    
    def LoadFilterRelic(self):
        if not self.m_PlayerReward:
            return None
        if self.m_CurLayer not in self.m_LayerSelect:
            return None
        oGame = self.m_Game
        lstHero = self.m_WarMgr.GetAllHero()
        for _, iRelic, _ in self.m_LayerSelect[self.m_CurLayer]:
            if not iRelic:
                continue
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                if oHero.m_PlayerID not in self.m_PlayerReward:
                    WarrelicLog.Debug('%d loadfilter err %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, self.m_PlayerReward, self.m_LayerSelect[self.m_CurLayer]))
                    self.m_PlayerReward[oHero.m_PlayerID] = { }
                    continue
                if iRelic in self.m_PlayerReward[oHero.m_PlayerID]:
                    continue
                oHero.m_RelicCon.AddFilterRelic(iRelic, self.m_CallFlag)
            
        

    
    def SaveSeed(self, oHero):
        if not self.m_Enable:
            return { }
        dData = {
            'LYS': DeepCopy(self.m_LayerSelect),
            'CLY': self.m_CurLayer,
            'PR': self.m_PlayerReward }
        return dData

    
    def LoadSeed(self, dData):
        if not dData:
            return None
        self.m_LayerSelect = dData['LYS']
        self.m_CurLayer = dData['CLY']
        self.m_PlayerReward = dData['PR']
        self.Enable()
        lstSelectRelic = []
        lstSelectMonsterRelic = []
        for lstLayerSelect in self.m_LayerSelect.values():
            for lstSelect in lstLayerSelect:
                iRelicSID = lstSelect[1]
                if not iRelicSID:
                    continue
                if iRelicSID not in self.m_Relic2MonsterRelic:
                    SendAlert('err', '怪物遗物%s 没配置对应遗物' % iRelicSID)
                    continue
                lstSelectRelic.append(iRelicSID)
                lstSelectMonsterRelic.append(self.m_Relic2MonsterRelic[iRelicSID])
            
        
        self.m_SelectRelic = lstSelectRelic
        self.m_SelectMonsterRelic = lstSelectMonsterRelic
        self.LoadFilterRelic()

    
    def Release(self):
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, sFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, sFlag)
        if self.m_Enable:
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, sFlag)
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, sFlag)
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, sFlag)
            cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, sFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER, sFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, sFlag)
            oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, sFlag, SIDE_TYPE_MONSTER)
        self.m_WarMgr = None
        super().Release()

    
    def OnStartFight(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        self.m_CurLayer = iLayer
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_HALL and iLayer > 1:
            oGame = self.m_Game
            if self.m_WarMgr.IsEndless():
                cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
                if self.m_KillDropRelic:
                    oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag, SIDE_TYPE_MONSTER)
                self.m_RoomDrop = { }
                return None
            if not self.m_Enable:
                self.Enable()
            lstHero = oWarMgr.GetAllHero()
            oLevelNode = oLevelCtrl.m_CurNode
            dGotoPos = oLevelNode.GetGotoPos(lstHero)
            for iHero in lstHero:
                dBornInfo = dGotoPos[iHero]
                tBornPos = dBornInfo['Pos']
                tBornFace = dBornInfo['Facing']
                self.m_BornPos[iHero] = (tBornPos, tBornFace)
            
            if iLayer not in self.m_LayerSelect:
                self.PrepareSelectList(iLayer)
                for iHero in oWarMgr.GetRoomHero(iCalAI = 0):
                    oHero = oGame.GetObject(iHero)
                    if not oHero:
                        continue
                    cbFun = Functor(self.SendReward, dInfo)
                    oHero.CoverCbFun(self.m_CallFlag, cbFun)
                
                iLastLayer = self.m_CurLayer - 1
                if iLastLayer in self.m_LayerSelect and len(self.m_RoomDrop) < len(self.m_LayerSelect[iLastLayer]):
                    WarrelicLog.Debug('%s monsterrelic layer %s drop less' % (oGame.m_ID, iLastLayer))
                self.m_RoomDrop = { }
                self.m_KillMonsterCnt = 0
        self.AddLastLevelCurseRelic()

    
    def AddLastLevelCurseRelic(self):
        oWarMgr = self.m_WarMgr
        dExtInfo = {
            'SourceReason': self.GetSourceReason(),
            'NotifyType': 1 }
        for pid, iRelic in self.m_DelayAddRelic:
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            oHero.m_RelicCon.AddRelic(iRelic, 'monsterrelic', dExtInfo = dExtInfo, iSource = oHero.m_PlayerID)
        
        self.m_DelayAddRelic = []

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        self.m_LoadingPlayer = self.m_WarMgr.GetRoomPlayer()
        self.AddHeroMapLoadOK()
        self.LoadFilterRelic()

    
    def SendReward(self, dInfo, oHero, dMsgInfo = None):
        bRet = self.TryChooseRelic(oHero, self.m_CurLayer)
        return bRet

    
    def PrepareSelectList(self, iLayer):
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        iCount = self.m_TotalOptionCount
        lstOptionalRelic = set(self.m_PutRelic)
        lstHero = oWarMgr.GetRoomHero(iCalAI = 1)
        iCheckCon = 1
        dRelicInCon = { }
        if len(lstOptionalRelic) - len(self.m_SelectRelic) >= iCount:
            lstOptionalRelic = set(lstOptionalRelic) - set(self.m_SelectRelic)
            lstHeroRelic = []
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                dRelicInCon[iHero] = oHero.m_RelicCon.GetFilterRelic()
                lstHeroRelic.extend(dRelicInCon[iHero])
            
            if len(set(lstOptionalRelic) - set(lstHeroRelic)) >= iCount:
                iCheckCon = 0
                lstOptionalRelic = set(lstOptionalRelic) - set(lstHeroRelic)
            else:
                WarrelicLog.Info('monsterrelic put not enough')
        else:
            WarrelicLog.Info('put all monsterrelic')
        dSource = { }
        iConfigLayer = self.GetConfigLayer(iLayer)
        dQualityWeight = self.m_QualityWeight[iConfigLayer]
        for iRelicSID in lstOptionalRelic:
            clsRelic = cl_perform.GetPerformModule(iRelicSID)
            if not clsRelic:
                continue
            if iRelicSID in self.m_RelicWeight:
                dSource[iRelicSID] = self.m_RelicWeight[iRelicSID]
                continue
            iQuality = clsRelic.m_Quality
            if iQuality not in dQualityWeight:
                SendAlert('err', '灵界寻宝抽取秘卷品质权重配置有缺失，请检查')
                continue
            dSource[iRelicSID] = dQualityWeight[iQuality]
        
        if len(dSource) < iCount:
            WarrelicLog.Alert('monsterrelic put not enough after filter')
            return None
        lstHero = oWarMgr.GetRoomHero(iCalAI = 0)
        iPlayerCount = len(lstHero)
        if iPlayerCount not in self.m_ChooseCount:
            return None
        dChooseCount = self.m_ChooseCount[iPlayerCount]
        iOption = self.m_OptionCount
        dLayerRelic = { }
        if not self.m_Master:
            self.RefreshMaster()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.m_PlayerID == self.m_Master:
                iChooseCount = dChooseCount['Master']
            else:
                iChooseCount = dChooseCount['Member']
            if not iChooseCount:
                continue
            self.m_SelectStep[iHero] = [
                0,
                iChooseCount]
            dHeroSource = { }
            if iCheckCon:
                for iRelicSID, iWeight in dSource.items():
                    if iRelicSID not in dRelicInCon[iHero]:
                        dHeroSource[iRelicSID] = iWeight
                
                if len(dHeroSource) < iChooseCount * iOption:
                    dHeroSource = dict(dSource)
                else:
                    dHeroSource = dict(dSource)
                for _ in range(iChooseCount):
                    dOptionRelic = { }
                    for _ in range(iOption):
                        iRelicSID = ChooseKey(oGame, dHeroSource)
                        dHeroSource.pop(iRelicSID)
                        dSource.pop(iRelicSID)
                        dMsgInfo = {
                            'Relic': iRelicSID }
                        if not self.m_KillDropRelic:
                            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_CHOOSE)
                        iLevel = dMsgInfo['RelicDropLevel'] if 'RelicDropLevel' in dMsgInfo else 1
                        dOptionRelic[iRelicSID] = iLevel
                    
                    dLayerRelic.setdefault(iHero, [])
                    dLayerRelic[iHero].append(dOptionRelic)
                
        
        dMsgInfo = {
            'Layer': iLayer,
            'LayerRelic': dLayerRelic }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_TREASURERELIC, oWarMgr, dMsgInfo, iSub = TREASURERELIC_GENERATELIST)
        self.m_LayerRelic[iLayer] = dLayerRelic

    
    def HeroChoosePerform(self, oHero, dOptionRelic):
        WarrelicLog.Info('%d treasure relics %s' % (oHero.m_PlayerID, dOptionRelic))
        net.GS2CChoosePerform(oHero, list(dOptionRelic.items()), PERFORMCHOOSE_TYPE_MONSTERRELIC)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnSelectRelic)

    
    def OnSelectRelic(self, oHero, iRelicSID):
        WarrelicLog.Debug('%d %d onselect relic %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iRelicSID))
        iHero = oHero.m_ID
        (iCurStep, iTotalStep) = self.m_SelectStep[iHero]
        if iCurStep >= iTotalStep:
            return 1
        iLayer = self.m_CurLayer
        if iLayer not in self.m_LayerRelic or iHero not in self.m_LayerRelic[iLayer]:
            return 1
        lstHeroOpt = self.m_LayerRelic[iLayer][iHero]
        if iCurStep > len(lstHeroOpt):
            return 1
        if iRelicSID:
            if iRelicSID not in lstHeroOpt[iCurStep]:
                return 1
            iLevel = lstHeroOpt[iCurStep][iRelicSID]
        else:
            iLevel = 1
        WarrelicLog.Info('%d %d select relic %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iRelicSID, iLevel))
        self.SelectRelic(iHero, iRelicSID, iLevel)
        iCurStep += 1
        self.m_SelectStep[iHero][0] = iCurStep
        if iCurStep < len(lstHeroOpt):
            self.HeroChoosePerform(oHero, lstHeroOpt[iCurStep])
            return 0
        return 1

    OnSelectRelic = ChooseRewardEnd(OnSelectRelic)
    
    def GMSelectRelic(self, oHero, lstRelic):
        if not self.m_Enable:
            return None
        for iRelicSID in lstRelic:
            if not iRelicSID:
                continue
            self.SelectRelic(oHero.m_ID, iRelicSID, 1)
        

    
    def GMRandomMonsterRelic(self, iNum):
        if not self.m_Enable:
            self.Enable()
        lstRelic = ShufferList(self.m_Game, list(self.m_PutRelic), iNum)
        for iRelicSID in lstRelic:
            if iRelicSID not in self.m_Relic2MonsterRelic:
                continue
            self.m_SelectMonsterRelic.append(self.m_Relic2MonsterRelic[iRelicSID])
        
        net.GS2CChosenRelicList(self.m_Game, self.m_SelectMonsterRelic, self.m_WarMgr.GetRoomPlayer(iCalAI = False))

    
    def SelectRelic(self, iHero, iRelicSID, iLevel):
        oWarMgr = self.m_WarMgr
        iLayer = self.m_CurLayer
        pid = oWarMgr.GetPlayerIDByHeroID(iHero)
        if not iRelicSID:
            self.m_LayerSelect.setdefault(iLayer, [])
            self.m_LayerSelect[iLayer].append([
                pid,
                iRelicSID,
                1])
            dMsgInfo = {
                'Relic': 0 }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_TREASURERELIC, oWarMgr, dMsgInfo, iSub = TREASURERELIC_SELECTRELIC)
            return None
        oGame = self.m_Game
        oHero = oGame.GetObject(iHero)
        clsRelic = cl_perform.GetPerformModule(iRelicSID)
        if not clsRelic:
            return None
        if iRelicSID not in self.m_Relic2MonsterRelic:
            SendAlert('err', '怪物遗物%s 没配置对应遗物' % iRelicSID)
            return None
        iMonsterRelicSID = self.m_Relic2MonsterRelic[iRelicSID]
        if not self.m_KillDropRelic:
            iSourceReason = self.GetSourceReason()
            oResMgr = oGame.GetResMgr()
            dStaticInfo = {
                'DropLevel': iLevel,
                'DropSource': pid,
                'SourceReason': iSourceReason }
            fMoveDis = 2 + oGame.Random(20) * 0.1
            vPos = cl_math.Vec3DisplaceDir(self.m_BornPos[iHero][0], self.m_BornPos[iHero][1], fMoveDis)
            oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_RELIC, vPos, [
                iRelicSID], { }, dStaticInfo, iHero)
            for iMatePid in oWarMgr.GetAllPlayer():
                if pid == iMatePid:
                    continue
                dStaticInfo = {
                    'DropLevel': 1,
                    'DropSource': iMatePid,
                    'SourceReason': iSourceReason }
                iTeammate = oWarMgr.GetHeroIDByPlayerID(iMatePid)
                vPos = cl_math.Vec3DisplaceDir(self.m_BornPos[iTeammate][0], self.m_BornPos[iTeammate][1], fMoveDis)
                oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_RELIC, vPos, [
                    iRelicSID], {
                    'ValidRemoveCurseRelic': 1 }, dStaticInfo, iTeammate)
            
        self.m_LayerSelect.setdefault(iLayer, [])
        self.m_LayerSelect[iLayer].append([
            pid,
            iRelicSID,
            iLevel])
        net.GS2CChosenRelicList(self.m_Game, [
            self.m_Relic2MonsterRelic[iRelicSID]], self.m_WarMgr.GetRoomPlayer(iCalAI = False))
        dMsgInfo = {
            'Relic': iRelicSID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_TREASURERELIC, oWarMgr, dMsgInfo, iSub = TREASURERELIC_SELECTRELIC)
        if iRelicSID in self.m_SelectRelic:
            return None
        self.m_SelectRelic.append(iRelicSID)
        self.m_SelectMonsterRelic.append(iMonsterRelicSID)
        clsMonsterRelic = cl_perform.GetPerformModule(iMonsterRelicSID)
        dRule = clsMonsterRelic.m_MonsterRule
        if dRule:
            self.m_MonsterRelicRule[iMonsterRelicSID] = dRule
        if self.m_KillDropRelic:
            for iHero in self.m_WarMgr.GetAllHero():
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                oHero.m_RelicCon.AddFilterRelic(iRelicSID, self.m_CallFlag)
                if oHero.m_PlayerID not in self.m_PlayerReward:
                    self.m_PlayerReward[oHero.m_PlayerID] = { }
            

    
    def OnCreateMonster(self, oWarMgr, dInfo):
        if not self.m_SelectMonsterRelic:
            return None
        iMonster = dInfo['Monster']
        if iMonster in self.m_MonUsedRelic:
            return None
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if oMonster and oMonster.m_FightType & MONSTER_CLASSIFY_BOXMONSTER != MONSTER_CLASSIFY_BOXMONSTER:
            self.MonsterUseRelic(oMonster, dInfo)

    
    def MonsterUseRelic(self, oMonster, dInfo):
        iCount = self.GetMonsterCanUseRelicCount(oMonster)
        if not iCount:
            return None
        (iLevel, iRoom) = (0, 0)
        if oMonster.m_LineIdx:
            (iLevel, iRoom, _) = oMonster.m_LineIdx
        elif oMonster.m_Owner:
            oOwner = self.m_Game.GetObject(oMonster.m_Owner)
            if oOwner and oOwner.m_LineIdx:
                (iLevel, iRoom, _) = oOwner.m_LineIdx
        if not iLevel:
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            iScene = oMonster.m_Scene
            oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
            iLevel = oScene.m_Level
            oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
            iRoom = oLevelNode.m_CurRoomPos
        self.m_MonsterRoom[oMonster.m_ID] = [
            iLevel,
            iRoom]
        self.m_RoomMonster.setdefault((iLevel, iRoom), { })[oMonster.m_ID] = 1
        lstRelic = []
        lstRoomRelic = self.GetRoomRelicList(iLevel, iRoom)
        for iRelic in lstRoomRelic:
            if not self.CheckMonsterUseRelic(oMonster, iRelic):
                continue
            lstRelic.append(iRelic)
            iCount -= 1
            if not iCount:
                break
        
        self.MonsterUseRelicList(oMonster, lstRelic)

    
    def OnMonsterSuper(self, oWarMgr, oMonster, dInfo):
        if not self.m_SelectMonsterRelic:
            return None
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUsedRelic:
            return None
        lstCurUseRelic = self.m_MonUsedRelic[iMonster]
        iNeedCnt = self.GetMonsterCanUseRelicCount(oMonster)
        iCurCnt = len(lstCurUseRelic)
        iDiff = iNeedCnt - iCurCnt
        if iDiff > 0:
            (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
            lstAdd = []
            lstRoomRelic = self.GetRoomRelicList(iLevel, iRoom)
            for iRelic in lstRoomRelic:
                if iRelic in lstCurUseRelic:
                    continue
                if not self.CheckMonsterUseRelic(oMonster, iRelic):
                    continue
                lstAdd.append(iRelic)
                iDiff -= 1
                if not iDiff:
                    break
            
            self.MonsterUseRelicList(oMonster, lstAdd)
        elif iDiff < 0:
            lstDisable = ShufferList(self.m_Game, lstCurUseRelic, -iDiff)
            self.MonsterDisableRelicList(oMonster, lstDisable)

    
    def MonsterUseRelicList(self, oMonster, lstRelic, iSyncClient = 1):
        lstMonsterRelic = self.m_MonUsedRelic.setdefault(oMonster.m_ID, [])
        WarrelicLog.Debug('%d %d %d addmonsterrelic %s' % (self.m_Game.m_ID, oMonster.m_SID, oMonster.m_ID, lstRelic))
        for iMonsterRelicSID in lstRelic:
            if oMonster.m_Perform.GetPerform(iMonsterRelicSID):
                continue
            oPerform = oMonster.AddPerform(iMonsterRelicSID, 1)
            if oPerform:
                lstMonsterRelic.append(iMonsterRelicSID)
                dInfo = {
                    'Perform': iMonsterRelicSID,
                    'NewMonsterRelic': iMonsterRelicSID }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, oMonster, dInfo)
        
        if iSyncClient:
            oScene = self.m_Game.m_SceneMgr.GetScene(oMonster.m_Scene)
            if oScene:
                dPlayer = oScene.GetPlayers()
                if dPlayer:
                    cl_snetwar.GS2CMonsterUseRelic(self.m_Game, oMonster.m_ID, lstMonsterRelic, dPlayer)
                else:
                    WarrelicLog.Alert('monster use relic no scene %d %d %s' % (oMonster.m_SID, oMonster.m_Scene, oMonster.m_LineIdx))

    
    def MonsterDisableRelicList(self, oMonster, lstRelic, iSyncClient = 1):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUsedRelic:
            return None
        lstMonsterRelic = self.m_MonUsedRelic[iMonster]
        for iMonsterRelicSID in lstRelic:
            if iMonsterRelicSID not in lstMonsterRelic:
                continue
            oMonster.m_Perform.RemovePerform(oMonster, iMonsterRelicSID)
            lstMonsterRelic.remove(iMonsterRelicSID)
        
        if iSyncClient:
            oScene = self.m_Game.m_SceneMgr.GetScene(oMonster.m_Scene)
            if oScene:
                dPlayer = oScene.GetPlayers()
                if dPlayer:
                    cl_snetwar.GS2CMonsterUseRelic(self.m_Game, iMonster, lstMonsterRelic, dPlayer)
                else:
                    WarrelicLog.Alert('monster disable relic no scene %d %d %s' % (oMonster.m_SID, oMonster.m_Scene, oMonster.m_LineIdx))

    
    def GetRoomRelicList(self, iLevel, iRoom):
        if iLevel in self.m_RoomRelic and iRoom in self.m_RoomRelic[iLevel]:
            return self.m_RoomRelic[iLevel][iRoom]
        lstPassRelic = []
        lstOption = self.m_SelectMonsterRelic
        dExcludeRelic = self.m_MonsterExcludeRelic
        lstPrior = []
        lstStandBy = []
        for iMonsterRelicSID in lstOption:
            if iMonsterRelicSID in lstPassRelic:
                continue
            if iMonsterRelicSID not in dExcludeRelic:
                lstPassRelic.append(iMonsterRelicSID)
                lstPrior.append(iMonsterRelicSID)
                continue
            lstExclude = [
                iMonsterRelicSID]
            for iExclude in dExcludeRelic[iMonsterRelicSID]:
                if iExclude in lstOption:
                    lstExclude.append(iExclude)
            
            lstPassRelic.extend(lstExclude)
            iIndex = self.m_Game.Random(len(lstExclude))
            iChooseRelic = lstExclude[iIndex]
            lstPrior.append(iChooseRelic)
            lstExclude.remove(iChooseRelic)
            lstStandBy.extend(lstExclude)
        
        lstOption = ShufferList(self.m_Game, lstPrior) + ShufferList(self.m_Game, lstStandBy)
        WarrelicLog.Info('%d level %d room %d monsterrelics %s' % (self.m_Game.m_ID, iLevel, iRoom, lstOption))
        dLevelRelic = self.m_RoomRelic.setdefault(iLevel, { })
        dLevelRelic[iRoom] = lstOption
        return lstOption

    
    def CheckMonsterUseRelic(self, oMonster, iMonsterRelicSID):
        if iMonsterRelicSID not in self.m_MonsterRelicRule:
            return 1
        dRule = self.m_MonsterRelicRule[iMonsterRelicSID]
        if MONSTERRELIC_RULE_LIMITMONSTER in dRule:
            dLimitRule = dRule[MONSTERRELIC_RULE_LIMITMONSTER]
            if MONSTERRELIC_SUBRULE_MONSTER in dLimitRule and dLimitRule[MONSTERRELIC_SUBRULE_MONSTER] and oMonster.m_DataSID not in dLimitRule[MONSTERRELIC_SUBRULE_MONSTER]:
                return 0
            if MONSTERRELIC_SUBRULE_MONSTERTYPE in dLimitRule and dLimitRule[MONSTERRELIC_SUBRULE_MONSTERTYPE] and oMonster.m_FightType not in dLimitRule[MONSTERRELIC_SUBRULE_MONSTERTYPE]:
                return 0
            if MONSTERRELIC_SUBRULE_DEFENDTREND in dLimitRule and dLimitRule[MONSTERRELIC_SUBRULE_DEFENDTREND] and oMonster.m_DefendTrend not in dLimitRule[MONSTERRELIC_SUBRULE_DEFENDTREND]:
                return 0
            if MONSTERRELIC_SUBRULE_MONSTERSOURCE in dLimitRule and dLimitRule[MONSTERRELIC_SUBRULE_MONSTERSOURCE]:
                for sMark in dLimitRule[MONSTERRELIC_SUBRULE_MONSTERSOURCE]:
                    if not oMonster.Query(sMark):
                        return 0
                
        if MONSTERRELIC_RULE_EXCLUDEMONSTER in dRule:
            dExcludeRule = dRule[MONSTERRELIC_RULE_EXCLUDEMONSTER]
            if MONSTERRELIC_SUBRULE_MONSTER in dExcludeRule and oMonster.m_DataSID in dExcludeRule[MONSTERRELIC_SUBRULE_MONSTER]:
                return 0
            if MONSTERRELIC_SUBRULE_MONSTERTYPE in dExcludeRule and oMonster.m_FightType in dExcludeRule[MONSTERRELIC_SUBRULE_MONSTERTYPE]:
                return 0
            if MONSTERRELIC_SUBRULE_DEFENDTREND in dExcludeRule and oMonster.m_DefendTrend in dExcludeRule[MONSTERRELIC_SUBRULE_DEFENDTREND]:
                return 0
            if MONSTERRELIC_SUBRULE_MONSTERSOURCE in dExcludeRule and dExcludeRule[MONSTERRELIC_SUBRULE_MONSTERSOURCE]:
                for sMark in dExcludeRule[MONSTERRELIC_SUBRULE_MONSTERSOURCE]:
                    if oMonster.Query(sMark):
                        return 0
                
        return 1

    
    def OnMapLoadOK(self, oHero, dMsgInfo):
        oWarMgr = self.m_WarMgr
        iCurScene = oHero.m_Scene
        pid = oHero.m_PlayerID
        oGame = self.m_Game
        lstSyncChosen = []
        iHero = oHero.m_ID
        bOver = True
        if pid in self.m_ReEnter:
            self.m_ReEnter.remove(pid)
            lstSyncChosen = self.m_SelectMonsterRelic
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_HALL:
            if iHero not in self.m_BornPos:
                oLevelNode = oLevelCtrl.m_CurNode
                dGotoPos = oLevelNode.GetGotoPos([
                    iHero])
                dBornInfo = dGotoPos[iHero]
                tBornPos = dBornInfo['Pos']
                tBornFace = dBornInfo['Facing']
                self.m_BornPos[iHero] = (tBornPos, tBornFace)
            if oHero.m_ID in self.m_SelectStep:
                iLayer = oLevelCtrl.m_LayerNum
                bRet = self.TryChooseRelic(oHero, iLayer)
                if not bRet:
                    bOver = False
            self.LoadDropInfo(oHero)
        elif self.m_MonUsedRelic:
            for iMonster, lstRelic in self.m_MonUsedRelic.items():
                if not lstRelic:
                    continue
                oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
                if not oMonster or oMonster.m_Scene != iCurScene:
                    continue
                cl_snetwar.GS2CMonsterUseRelic(self.m_Game, oMonster.m_ID, lstRelic, [
                    pid])
                if iMonster in self.m_RefreshRelic:
                    for iRelicSID, iStateSID in self.m_RefreshRelic[iMonster].items():
                        if iRelicSID not in lstRelic:
                            continue
                        oState = oMonster.m_State.GetItemBySID(iStateSID)
                        if oState:
                            cl_snetwar.GS2CMonsterRelicRefreshCnt(oGame, iMonster, iRelicSID, oState.GetCount(), [
                                pid])
                    
            
        if pid in self.m_LoadingPlayer:
            self.m_LoadingPlayer.remove(pid)
            lstSyncChosen = self.m_SelectMonsterRelic
        if lstSyncChosen:
            net.GS2CChosenRelicList(self.m_Game, lstSyncChosen, [
                pid])
        return bOver

    
    def TryChooseRelic(self, oHero, iLayer):
        iHero = oHero.m_ID
        if iLayer not in self.m_LayerRelic or iHero not in self.m_LayerRelic[iLayer]:
            return True
        (iCurStep, iTotalStep) = self.m_SelectStep[iHero]
        if iCurStep >= iTotalStep:
            return True
        lstHeroOpt = self.m_LayerRelic[iLayer][iHero]
        if iCurStep > len(lstHeroOpt):
            return True
        dOptionRelic = lstHeroOpt[iCurStep]
        self.HeroChoosePerform(oHero, dOptionRelic)
        return False

    
    def GetMonsterCanUseRelicCount(self, oMonster):
        if not self.m_MonUseRelicCount:
            return 0
        iLayer = self.GetConfigLayer(self.m_CurLayer)
        if iLayer not in self.m_MonUseRelicCount:
            return 0
        dMonUseRelicCount = self.m_MonUseRelicCount[iLayer]
        if oMonster.m_DataSID in self.m_AssignMonsterType and self.m_AssignMonsterType[oMonster.m_DataSID] in dMonUseRelicCount:
            return dMonUseRelicCount[self.m_AssignMonsterType[oMonster.m_DataSID]]
        if oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            return dMonUseRelicCount['Boss']
        if oMonster.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            return dMonUseRelicCount['Elite']
        if oMonster.Query('MonsterSuper'):
            return dMonUseRelicCount['Super']
        return dMonUseRelicCount['Normal']

    
    def GetMonsterRelicNumByQuality(self, oMonster, iQuality):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUsedRelic:
            return 0
        iCount = 0
        for iPerform in self.m_MonUsedRelic[iMonster]:
            oPerform = oMonster.m_Perform.GetPerform(iPerform)
            if oPerform.m_PFType != PF_TYPE_RELIC:
                continue
            if oPerform.m_Quality == iQuality:
                iCount += 1
        
        return iCount

    
    def GetMonsterRelicNum(self, oMonster):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUsedRelic:
            return 0
        return len(self.m_MonUsedRelic[iMonster])

    
    def GetMonsterRelic(self, iMonster):
        if iMonster not in self.m_MonUsedRelic:
            return []
        return self.m_MonUsedRelic[iMonster]

    
    def MonsterUseExtraRelic(self, oMonster, iRelicSID, iCount):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUseExtRelic:
            self.m_MonUseExtRelic[iMonster] = []
        if iRelicSID in self.m_MonUseExtRelic[iMonster]:
            return None
        oGame = self.m_Game
        if iMonster not in self.m_MonsterRoom:
            return None
        (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
        if iLevel not in self.m_ExtraRelic:
            self.m_ExtraRelic[iLevel] = { }
        if iRoom not in self.m_ExtraRelic[iLevel]:
            self.m_ExtraRelic[iLevel][iRoom] = { }
        if iRelicSID not in self.m_ExtraRelic[iLevel][iRoom]:
            self.m_ExtraRelic[iLevel][iRoom][iRelicSID] = []
        lstRelic = self.m_ExtraRelic[iLevel][iRoom][iRelicSID]
        if not lstRelic:
            lstCurUseRelic = self.m_MonUsedRelic[iMonster] if iMonster in self.m_MonUsedRelic else []
            lstOption = []
            for iRelic in self.m_SelectMonsterRelic:
                if iRelic not in lstCurUseRelic:
                    lstOption.append(iRelic)
            
            if len(lstOption) > iCount:
                lstExtend = ShufferList(oGame, lstOption, iCount)
                lstRelic.extend(lstExtend)
            else:
                lstRelic.extend(lstOption)
            self.m_MonUseExtRelic[iMonster].append(iRelicSID)
        WarrelicLog.Info('%d level %d room %d monsterextrarelics %d %s' % (self.m_Game.m_ID, iLevel, iRoom, iRelicSID, lstRelic))
        self.MonsterUseRelicList(oMonster, lstRelic, 0)

    
    def OnPlayerReady(self, oWarMgr, oHero, dMsgInfo):
        iReEnter = dMsgInfo['reenter']
        if iReEnter:
            self.m_ReEnter.append(dMsgInfo['pid'])

    
    def OnRemovePlayer(self, oWarMgr, dMsgInfo):
        if self.m_Master == dMsgInfo['pid']:
            self.RefreshMaster()

    
    def RefreshMaster(self):
        self.m_Master = self.m_WarMgr.GetWarMasterPlayer()
        if not self.m_Master:
            lstRoomPlayer = self.m_WarMgr.GetRoomPlayer(iCalAI = False)
            if lstRoomPlayer:
                self.m_Master = lstRoomPlayer[0]

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        iCurLevel = dMsgInfo['Level']
        iCurRoom = dMsgInfo['Room']
        oLevelNode = oLevelCtrl.GetLevelNode(iCurLevel)
        if not oLevelNode:
            return None
        if oLevelNode.IsLockRoom(iCurRoom):
            return None
        oGame = self.m_Game
        dMonUsedRelic = DeepCopy(self.m_MonUsedRelic)
        iLen = len(dMonUsedRelic)
        for iMonster, lstRelic in dMonUsedRelic.items():
            if iMonster not in self.m_MonsterRoom:
                continue
            (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
            if iLevel != iCurLevel or iRoom != iCurRoom:
                continue
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            self.MonsterDisableRelicList(oMonster, lstRelic, 0)
            if iLen != len(self.m_MonUsedRelic):
                WarrelicLog.Alert('preroomgoal iter err %s %s %s %s %s %s %s %s' % (self.m_Game.m_ID, self.m_MonUsedRelic, dMonUsedRelic, oMonster.m_ID, oMonster.m_SID, oMonster.Query('MonsterSuper', (0, 0)), oMonster.m_Perform.m_Perform.keys(), oMonster.m_State.m_StateBySid.keys()))
        

    
    def OnLevelFinish(self, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        for iDemon, tReward in self.m_LevelReward.items():
            (iHero, iRelic) = tReward
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if not iRelic:
                dRelic = { }
                for pid, iSelectRelic, _ in self.m_LayerSelect[self.m_CurLayer]:
                    if not iSelectRelic:
                        continue
                    if iSelectRelic in self.m_PlayerReward[oHero.m_PlayerID]:
                        continue
                    dRelic[iSelectRelic] = 10
                
                iRelic = ChooseKey(oGame, dRelic)
                if not iRelic:
                    WarrelicLog.Alert('%s %s demon %s no random' % (oGame.m_ID, oHero.m_PlayerID, iDemon))
                    continue
                WarrelicLog.Debug('%s %s demon %s random %s' % (oGame.m_ID, oHero.m_PlayerID, iDemon, iRelic))
                self.m_PlayerReward[oHero.m_PlayerID][iRelic] = 0
            oHero.m_RelicCon.DelFilterRelic(iRelic, self.m_CallFlag)
        
        self.m_LevelReward = { }
        self.m_MonUsedRelic = { }
        self.m_RefreshRelic = { }
        self.m_DelayFunc = { }
        self.m_MonsterSummon = { }
        self.m_MonsterPrepareSummon = { }
        self.m_RoomSummonCnt = { }
        self.m_RoomMonster = { }
        self.m_MonsterRoom = { }
        self.m_DropInfo = { }
        self.NextLevelAddRelic()

    
    def NextLevelAddRelic(self):
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iSourceReason = self.GetSourceReason()
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            iScene = oNode.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            if not oScene:
                continue
            lstDrop = oScene.GetObjectsByType('Drop')
            for iDrop in lstDrop:
                oDrop = oGame.GetObject(iDrop)
                if not oDrop:
                    continue
                if oDrop.m_FightType != NWARRIOR_DROP_RELIC_CURSE:
                    continue
                if oDrop.GetSourceReason()['Mode'] != iSourceReason:
                    continue
                iRelic = oDrop.GetReward()
                if not iRelic:
                    continue
                oHero = oGame.GetObject(oDrop.m_Owner)
                if not oHero:
                    continue
                WarrelicLog.Debug('%s %s auto pick %s' % (oGame.m_ID, oHero.m_PlayerID, iRelic))
                self.m_DelayAddRelic.append((oHero.m_PlayerID, iRelic))
                oDrop.Remove('Monsterrelic')
            
        

    
    def ClearData(self):
        self.m_SelectRelic = []
        self.m_SelectMonsterRelic = []
        self.m_LayerRelic = { }
        self.m_LayerSelect = { }
        self.m_RoomRelic = { }
        self.m_ExtraRelic = { }
        self.m_SelectStep = { }

    
    def MonsterListenMsg(self, iMonster, iMsg, iSub, iStateSID):
        if iMsg not in self.m_MonsterListenMsg:
            self.m_MonsterListenMsg[iMsg] = { }
        if iSub not in self.m_MonsterListenMsg[iMsg]:
            cbfunc = Functor(self.AddRoomStateCount, iMsg, iSub, iStateSID)
            self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, iMsg, cbfunc, self.m_CallFlag, iSub)
            self.m_MonsterListenMsg[iMsg][iSub] = []
        self.m_MonsterListenMsg[iMsg][iSub].append(iMonster)

    
    def AddRoomStateCount(self, iMsg, iSub, iStateSID, oWarMgr, oWarrior, dMsgInfo):
        if not oWarrior.m_FightType & WARRIOR_MONSTER:
            return None
        if iMsg not in self.m_MonsterListenMsg or iSub not in self.m_MonsterListenMsg[iMsg]:
            return None
        iTarget = oWarrior.m_ID
        if iTarget not in self.m_MonsterRoom:
            return None
        (iTargetLevel, iTargetRoom) = self.m_MonsterRoom[iTarget]
        if iTargetLevel not in self.m_RoomStateCnt:
            self.m_RoomStateCnt[iTargetLevel] = { }
        if iTargetRoom not in self.m_RoomStateCnt[iTargetLevel]:
            self.m_RoomStateCnt[iTargetLevel][iTargetRoom] = { }
        if iStateSID not in self.m_RoomStateCnt[iTargetLevel][iTargetRoom]:
            self.m_RoomStateCnt[iTargetLevel][iTargetRoom][iStateSID] = 0
        self.m_RoomStateCnt[iTargetLevel][iTargetRoom][iStateSID] += 1
        oGame = self.m_Game
        for iMonster in self.m_MonsterListenMsg[iMsg][iSub]:
            (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
            if iLevel != iTargetLevel or iRoom != iTargetRoom:
                continue
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oState = oMonster.m_State.GetItemBySID(iStateSID)
            if oState:
                oState.AddCount(oMonster, 1)
        

    
    def MonsterCancelListenMsg(self, iMonster, iMsg, iSub):
        self.m_MonsterListenMsg[iMsg][iSub].remove(iMonster)
        if not self.m_MonsterListenMsg[iMsg][iSub]:
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, iMsg, self.m_CallFlag, iSub)
            self.m_MonsterListenMsg[iMsg].pop(iSub)
            if not self.m_MonsterListenMsg[iMsg]:
                self.m_MonsterListenMsg.pop(iMsg)

    
    def GetRoomStateCount(self, iMonster, iStateSID):
        (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
        if iLevel not in self.m_RoomStateCnt or iRoom not in self.m_RoomStateCnt[iLevel] or iStateSID not in self.m_RoomStateCnt[iLevel][iRoom]:
            return 0
        return self.m_RoomStateCnt[iLevel][iRoom][iStateSID]

    
    def SetRefreshRelic(self, iMonster, iRelicSID, iStateSID):
        if iMonster not in self.m_RefreshRelic:
            self.m_RefreshRelic[iMonster] = { }
        if iRelicSID in self.m_RefreshRelic[iMonster]:
            return None
        self.m_RefreshRelic[iMonster][iRelicSID] = iStateSID

    
    def GetRoomKey(self, iMonster, sFlag = None):
        if iMonster not in self.m_MonsterRoom:
            return ''
        (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
        sKey = '%d-%d' % (iLevel, iRoom)
        if sFlag:
            sKey += '-%s' % sFlag
        return sKey

    
    def RelicCreateSummon(self, oMonster, dInfo):
        iMonster = oMonster.m_ID
        iRelic = dInfo['Relic']
        dMonsterSummon = self.m_MonsterSummon.setdefault(iRelic, { })
        if iMonster not in dMonsterSummon:
            dMonsterSummon[iMonster] = []
            iSummonCnt = 0
        else:
            iSummonCnt = len(dMonsterSummon[iMonster])
        if iSummonCnt >= dInfo['SummonLimit']:
            return None
        dMonsterPrepareSummon = self.m_MonsterPrepareSummon.setdefault(iRelic, [])
        for lstArgs in dMonsterPrepareSummon:
            if iMonster == lstArgs[0]:
                iSummonCnt += 1
        
        if iSummonCnt >= dInfo['SummonLimit']:
            return None
        sKey = self.GetRoomKey(iMonster, iRelic)
        iRoomSummonCnt = self.m_RoomSummonCnt.setdefault(sKey, 0)
        if iRoomSummonCnt >= dInfo['RoomSummonLimit']:
            dMonsterPrepareSummon.append((iMonster, dInfo))
        else:
            self.UseEffectPerform(oMonster, dInfo)

    
    def UseEffectPerform(self, oMonster, dInfo):
        oGame = self.m_Game
        iScene = oMonster.m_Scene
        tPos = oMonster.GetPos()
        tFace = oMonster.GetFacing()
        (iRadius1, iRadius2, iAngle1, iAngle2) = dInfo['PosArgs']
        vPos = oGame.Scene_RandomPointSectorInMesh(iScene, tPos, tFace, iRadius1, iRadius2, iAngle1, iAngle2)
        if not vPos:
            vPos = oMonster.GetPos()
        oPerform = oMonster.GetPerformIfNoThenNew(dInfo['EffectPf'])
        dData = {
            'vStart': oMonster.GetAttackPos(),
            'Custom': {
                'vEnd': vPos,
                'Info': dInfo } }
        iMonster = oMonster.m_ID
        iRelic = dInfo['Relic']
        sKey = self.GetRoomKey(iMonster, iRelic)
        self.m_RoomSummonCnt[sKey] += 1
        if len(self.m_MonsterSummon[iRelic][iMonster]) + 1 >= dInfo['SummonLimit']:
            dArgs = {
                'AID': iMonster,
                'RS': cl_object.reason.CStrReason('%d-CD' % iRelic),
                'arg': { } }
            oState = cl_state.AddState(oMonster, dInfo['CDState'], STATE_TIME_FOREVER, 0, dArgs)
            if oState:
                oState.Enable(oMonster)
        cl_war.UsePerform(oMonster, oPerform, dData)

    
    def TrueCreateRelicSummon(self, oMonster, iSummonSID, vPos, dInfo):
        iMonster = oMonster.m_ID
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        oSummon = self.m_Game.m_ResMgr.CreateMonster(oMonster.m_Scene, iSummonSID, vPos, oMonster.GetFacing(), SIDE_TYPE_MONSTER, oMonster.m_AddGrade, dAI, oMonster.m_LineIdx, {
            'Owner': iMonster })
        iSummon = oSummon.m_ID
        oMonster.m_MonsterSummon[iSummon] = iSummonSID
        oMonster.m_FollowDieObjs[iSummon] = 1
        iSuperLevel = oMonster.SuperLevel()
        if iSuperLevel:
            (iPlusPF, iAfPF) = oMonster.Query('MonsterSuper', (0, 0))
            oSummon.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)
        iRelic = dInfo['Relic']
        lstExcRelic = dInfo['ExcRelic']
        self.MonsterDisableRelicList(oSummon, lstExcRelic)
        self.m_MonsterSummon[iRelic][iMonster].append(iSummon)
        cl_msgcenter.AddFunction(oSummon, cl_msgcenter.MSG_WAR_DIE, Functor(self.OnSummonDie, dInfo), '%s-%d' % (self.m_CallFlag, iRelic))

    
    def OnSummonDie(self, dInfo, oSummon, dMsgInfo):
        iSummon = oSummon.m_ID
        iMonster = oSummon.m_Owner
        iRelic = dInfo['Relic']
        if iSummon not in self.m_MonsterSummon[iRelic][iMonster]:
            return None
        self.m_MonsterSummon[iRelic][iMonster].remove(iSummon)
        sKey = self.GetRoomKey(iMonster, iRelic)
        self.m_RoomSummonCnt[sKey] -= 1
        iCDState = dInfo['CDState']
        self.CreateRelicSummonFromQueue(iRelic, 1)
        if dMsgInfo['RS'].GetStrReason() == 'FollowDie':
            return None
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        if not oMonster.m_State:
            WarrelicLog.Alert('Relic25823 OnSummonDie not oMonster.m_State %d %d %d %s' % (oMonster.m_SID, oMonster.m_Dead, oMonster.m_ReleaseFlag, oMonster.m_LineIdx))
        oCdState = oMonster.m_State.GetItemBySID(iCDState)
        if oCdState and oCdState.m_TimeType == STATE_TIME_FOREVER:
            oMonster.m_State.RemoveItem(oCdState.m_ID)

    
    def CreateRelicSummonFromQueue(self, iRelic, iCount):
        if iRelic not in self.m_MonsterPrepareSummon:
            return None
        lstPrepare = self.m_MonsterPrepareSummon[iRelic]
        if not lstPrepare:
            return None
        iUsed = 0
        oGame = self.m_Game
        for iMonster, dInfo in lstPrepare:
            iUsed += 1
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            self.UseEffectPerform(oMonster, dInfo)
            iCount -= 1
            if iCount <= 0:
                break
        
        for _ in range(iUsed):
            if lstPrepare:
                lstPrepare.pop(0)
                continue
        

    
    def GetMonsterSummon(self, iRelic, iMonster):
        if iRelic not in self.m_MonsterSummon:
            return []
        if iMonster not in self.m_MonsterSummon[iRelic]:
            return []
        return self.m_MonsterSummon[iRelic][iMonster]

    
    def AddRelicRoomSummonCnt(self, iRelic, iMonster, iCount):
        sKey = self.GetRoomKey(iMonster, iRelic)
        if sKey in self.m_RoomSummonCnt:
            self.m_RoomSummonCnt[sKey] += iCount

    
    def ClearMonsterSummon(self, iRelic, iMonster):
        if iRelic in self.m_MonsterSummon and iMonster in self.m_MonsterSummon[iRelic]:
            self.m_MonsterSummon[iRelic][iMonster] = []
        if iRelic in self.m_MonsterPrepareSummon:
            self.m_MonsterPrepareSummon[iRelic] = list(filter((lambda item: item[0] != iMonster), self.m_MonsterPrepareSummon[iRelic]))

    
    def GetConfigLayer(self, iLayer):
        if self.m_WarMgr.IsEndless():
            return self.m_EndlessConfigLayer
        return iLayer

    
    def GetSourceReason(self):
        return SOURCE_REASON_MODE_MONSTERRELIC

    
    def ValidDropRelic(self, oMonster):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonUsedRelic:
            return 0
        if self.m_CurLayer not in self.m_LayerSelect or not self.m_LayerSelect[self.m_CurLayer]:
            return 0
        if iMonster not in self.m_MonsterRoom:
            return 0
        (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
        tKey = (iLevel, iRoom)
        if tKey in self.m_RoomDrop:
            return 0
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oMonster.m_Scene)
        if not oScene:
            return 0
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if not oLevelNode or oLevelNode.m_LevelType != LEVEL_TYPE_FIGHT:
            return 0
        if not self.m_PlayerReward:
            return 0
        iCurDropCnt = 0
        iLevelDropCnt = 0
        for iDropLevel, _ in self.m_RoomDrop:
            iCurDropCnt += 1
            if iDropLevel == iLevel:
                iLevelDropCnt += 1
        
        iMaxDropCnt = 0
        for _, iRelic, _ in self.m_LayerSelect[self.m_CurLayer]:
            if not iRelic:
                continue
            iMaxDropCnt += 1
        
        if iCurDropCnt >= iMaxDropCnt:
            return 0
        tLevelKey = (oLevelNode.m_LayerNum, oLevelNode.m_LevelNum)
        if tLevelKey in self.m_LevelDropLimit and iLevelDropCnt >= self.m_LevelDropLimit[tLevelKey]:
            return 0
        if self.CheckFloorDrop(iLevel, iRoom, iCurDropCnt, iMaxDropCnt):
            return 1
        iMonsterFightType = oMonster.m_FightType
        iDropProb = 0
        for iFightType, iProb in self.m_DropProbability.items():
            if iMonsterFightType & iFightType == iFightType:
                iDropProb = iProb
                break
        else:
            return 0
        oGame = self.m_Game
        if oGame.Random(10000) > iDropProb:
            self.m_KillMonsterCnt += 1
            return 0
        return 1

    
    def CheckFloorDrop(self, iLevel, iRoom, iCurDropCnt, iMaxDropCnt):
        if self.m_KillMonsterCnt >= self.m_FloorDropCnt:
            WarrelicLog.Debug('%d monsterrelic killfloor' % self.m_Game.m_ID)
            return 1
        if (iLevel, iRoom) not in self.m_RoomMonster or self.m_RoomMonster[(iLevel, iRoom)]:
            return 0
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        oCurNode = oLevelCtrl.m_CurNode
        if oCurNode.m_LevelType == LEVEL_TYPE_HALL:
            return 0
        if iLevel != oCurNode.m_Level:
            return 0
        iMaxLevelNum = oLevelCtrl.GetFightMaxLevel()
        iCurLevelNum = oLevelCtrl.m_LevelNum
        if iCurLevelNum < iMaxLevelNum:
            if self.m_CurLayer in self.m_LayerDrop:
                return 0
            if iRoom + 1 == oCurNode.GetMaxRoomCnt():
                WarrelicLog.Debug('%d monsterrelic roomfloor' % self.m_Game.m_ID)
                return 1
        if iCurLevelNum == iMaxLevelNum:
            iNeedCnt = iMaxDropCnt - iCurDropCnt
            if oCurNode.GetMaxRoomCnt() - iRoom <= iNeedCnt:
                WarrelicLog.Debug('%d monsterrelic roomfloor' % self.m_Game.m_ID)
                return 1
        return 0

    
    def OnMonsterDie(self, oWarMgr, oMonster, dMsgInfo):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_MonsterRoom:
            return None
        (iLevel, iRoom) = self.m_MonsterRoom[iMonster]
        tKey = (iLevel, iRoom)
        self.m_RoomMonster[tKey].pop(iMonster, 0)
        if not self.ValidDropRelic(oMonster):
            return None
        self.m_KillMonsterCnt = 0
        oGame = self.m_Game
        self.m_RoomDrop[tKey] = { }
        self.m_LayerDrop[self.m_CurLayer] = 1
        oResMgr = oGame.GetResMgr()
        vDropPos = cl_reward.GetDropBasePos(oMonster)
        iScene = oMonster.m_Scene
        dReward = { }
        oWarMgr = self.m_WarMgr
        dAIExtInfo = {
            'SourceReason': self.GetSourceReason() }
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oWarMgr.IsAIHero(iHero):
                iRelic = self.GetRelicReward(oHero)
                if oHero.m_RelicCon.CheckHasRelic(iRelic):
                    WarrelicLog.Debug('%d monsterrelic %s ai reward repeat %s' % (oGame.m_ID, oHero.m_PlayerID, iRelic))
                    continue
                self.m_PlayerReward[oHero.m_PlayerID][iRelic] = 1
                oHero.m_RelicCon.AddRelic(iRelic, 'monsterrelic-ai', dExtInfo = dAIExtInfo, iSource = oHero.m_PlayerID)
                continue
            oDemon = oResMgr.CreateDrop(iScene, NWARRIOR_DROP_DEMON, vDropPos, [
                { }], { }, dStaticInfo = {
                'Quality': 2,
                'DynamicReward': DYNAMIC_DEMON_MONSTERRELIC }, iOwner = iHero)
            if oDemon:
                self.m_LevelReward[oDemon.m_ID] = (iHero, 0)
                dReward[oHero.m_PlayerID] = oDemon.m_ID
                self.m_RoomDrop[tKey][oHero.m_PlayerID] = oDemon.m_ID
        
        WarrelicLog.Debug('%d monsterrelic %s demon %s' % (oGame.m_ID, tKey, dReward))

    
    def GetRelicReward(self, oHero):
        iCurPid = oHero.m_PlayerID
        dRelic = { }
        dAllRelic = { }
        dSelectNoReward = { }
        dHeroRelic = { }
        (iSelfWeight, iMateWeight) = self.m_DropWeight
        oRelicCon = oHero.m_RelicCon
        lstHasRelic = oRelicCon.GetAllRelicSID()
        for pid, iRelic, _ in self.m_LayerSelect[self.m_CurLayer]:
            if not iRelic:
                continue
            if pid == iCurPid:
                iWeight = iSelfWeight
                dHeroRelic[iRelic] = 1
            else:
                iWeight = iMateWeight
            dAllRelic[iRelic] = iWeight
            if iRelic in self.m_PlayerReward[iCurPid]:
                continue
            dSelectNoReward[iRelic] = iWeight
            if iRelic in lstHasRelic:
                continue
            dRelic[iRelic] = iWeight
        
        if not dRelic:
            if dSelectNoReward:
                dRelic = dSelectNoReward
            else:
                dRelic = dAllRelic
        return ChooseKey(self.m_Game, dRelic)

    
    def GetMonsterRelicDemonReward(self, oDemon, oHero):
        iDemon = oDemon.m_ID
        if iDemon not in self.m_LevelReward:
            return { }
        (iHero, iReward) = self.m_LevelReward[iDemon]
        if iReward or oHero.m_ID != iHero:
            return { }
        iCurPid = oHero.m_PlayerID
        oGame = self.m_Game
        iRelic = self.GetRelicReward(oHero)
        clsRelic = cl_perform.GetPerformModule(iRelic)
        if not clsRelic:
            WarrelicLog.Error(f'''{oGame.m_ID} monsterrelic {iCurPid} no reward''')
            return { }
        lstReward = [
            {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iRelic] } }]
        iValidRemoveCurseRelic = 1
        iNotifyType = 0
        if clsRelic.m_RelicType == RELIC_TYPE_CURSE:
            for pid, iSelectRelic, _ in self.m_LayerSelect[self.m_CurLayer]:
                if pid == iCurPid and iSelectRelic == iRelic:
                    iValidRemoveCurseRelic = 0
                    iNotifyType = 1
                    break
            
        dExtInfo = {
            'Player': oHero.m_ID,
            'ExtStaticInfo': {
                'SourceReason': self.GetSourceReason(),
                'NotifyType': iNotifyType,
                'DelayPickTime': self.m_DelayPickTime,
                'EnablePick': 1 },
            'DropReason': DROP_REASON_MONSTERRELIC,
            'ExtraInfo': {
                'ValidRemoveCurseRelic': iValidRemoveCurseRelic } }
        dInfo = {
            FAKEMG_MONSTERRELIC: (0, lstReward, dExtInfo) }
        WarrelicLog.Debug('%s monsterrelic %s drop %s %s' % (oGame.m_ID, iCurPid, iDemon, iRelic))
        self.m_LevelReward[iDemon] = (iHero, iRelic)
        self.m_PlayerReward[iCurPid][iRelic] = 1
        return dInfo



def GetComponentClass(oMgrManager):
    return CMonsterRelicElement

