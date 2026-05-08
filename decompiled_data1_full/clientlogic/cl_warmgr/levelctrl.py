# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelctrl.pyc
# RelativePath: clientlogic/cl_warmgr/levelctrl.pyc
# Source Generated with Decompyle++
# File: levelctrl.pyc (Python 3.6)

from cl_commondefines import HIDELV_TYPE_ELITE, LAYER_CHOOSE_HIDE, PLAYMODE_DAYLY_TRIAL, GetWarNo, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_GSCASHSHOP, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_SHOP, LAYER_CHOOSE_ELE, LAYER_CHOOSE_CHALLENGE, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, LEVEL_TYPE_NONE, LEVEL_DIFF_HARD, LEVEL_DIFF_MEDIUM, LEVEL_DIFF_NORMAL, LEVEL_TYPE_HIDE, GAMETYPE_NONE, LEVEL_TYPE_HALL, LEVEL_STATUS_GOAL, LAYER_CHOOSE_TASKNPC, LAYER_CHOOSE_PETSHOP, LAYER_CHOOSE_REGROUPRELIC, LAYER_CHOOSE_RELICLOTTERY, LAYER_CHOOSE_WANDSHOP, LAYER_CHOOSE_DICESHOP, LAYER_CHOOSE_S7SHOP, LAYER_CHOOSE_S8SHOP
from cl_warmgr.mobject import CBaseElement
from cl_only import ChooseKey, ShufferList, ChooseMulKeys, Frame2Time
from cl_object.logging import LevelLog
import itertools
import cl_wardata.levelconf.mobject as levelconfdata
import cl_msgcenter
import cl_notify
import cl_random
import cl_roomchallenge
import cllib.lib_flag
import cl_npc.net as npcnet
import cl_formula
from . import warcondition
from . import levelline

class CLevelCtrlElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CLevelCtrlElement, self).__init__(oGame, nid, oData)
        self.m_LevelCtrlConf = oData.m_LevelCtrlConf
        self.m_ChooseItem = oData.m_ChooseItem
        self.m_LayerAndLevelMap = oData.m_LayerAndLevelMap
        self.m_LayerNum = 1
        self.m_LevelNum = 0
        self.m_BaseLayerNum = 1
        self.m_DirectLevel = 0
        self.m_CurTransferNpc = 0
        self.m_ReadyTransferPlayer = { }
        self.m_TranserReadyFrame = 0
        self.m_CurLType = LEVEL_TYPE_HALL
        self.m_CurTType = GAMETYPE_NONE
        self.m_CurNode = None
        self.m_MainLevelRecord = { }
        self.m_HideLevelRecord = { }
        self.m_HideLevelTypeRecord = { }
        self.m_LastHideLevel = []
        self.m_HideLevelTypeNumRecord = { }
        self.m_FilterHideLevel = ()
        self.m_FilterHideLevelType = { }
        self.m_FilterMainLevel = ()
        self.m_LevelNodeLib = { }
        self.m_HideLevelLib = { }
        self.m_HeroLogin = set()
        self.m_CurTransfer = { }
        self.m_LevelAssignBornPos = { }
        self.m_SavedLevelInfo = { }
        self.m_RoomChallenge = cl_roomchallenge.NewRoomChallenge(self)
        self.m_LevelTrigger = levelline.NewLevelTrigger(self)
        self.m_LevelMiniMap = levelline.NewMiniMapMgr(self)
        self.m_LevelConfData = levelconfdata.CLevelConfDataMgr(self)
        self.m_LayerChoose = CLayerRandomChoose(self)
        self.m_LevelCountDict = { }
        self.m_HideLevelHeroMap = { }
        self.m_HideLevelIndexMap = { }

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerEnterGame, 'LevelCtrlPlayerLogin', -1)
        self.m_Game.m_Timer.Logic_Call_Out(self.InitLevelNode, 1000, 'LevelCtrlInitLevelNode')
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerReady, 'LevelCtrlPlayerReady', -1)
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'LevelStart', -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'LevelStart')
        self.m_LayerChoose.Release()
        self.m_RoomChallenge.Release()
        self.m_LevelMiniMap.Release()
        for oLevelNode in self.m_LevelNodeLib.values():
            oLevelNode.Release()
        
        self.m_HideLevelLib = { }
        self.m_LevelTrigger.Release()
        self.m_LevelConfData.Release()
        self.m_CurNode = None
        super(CLevelCtrlElement, self).Release()

    
    def Save(self):
        dData = { }
        dData['LevelCount'] = dict(self.m_LevelCountDict)
        if self.m_CurLType != LEVEL_TYPE_BOSS:
            dData.update(self.m_LayerChoose.Save())
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        if 'LevelCount' in dData:
            self.m_LevelCountDict = dData['LevelCount']
        self.m_SavedLevelInfo = dData
        LevelLog.Debug('%s load %s' % (self.m_Game.m_ID, dData))

    
    def OnPlayerEnterGame(self, oListener, oSender, dInfo):
        pid = dInfo['pid']
        Reenter = dInfo['reenter']
        if not Reenter:
            self.m_HeroLogin.add(pid)
            lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
            if len(self.m_HeroLogin) == len(lstPlayer):
                self.m_Game.m_Timer.Logic_Remove_Call_Out('LevelCtrlInitLevelNode')
                self.InitLevelNode()

    
    def OnPlayerReady(self, oListener, oSender, dInfo):
        iReEnter = dInfo['reenter']
        pid = dInfo['pid']
        if iReEnter:
            if self.m_TranserReadyFrame:
                iRemainFrame = self.m_TranserReadyFrame - self.m_Game.GetFrameNum()
                if iRemainFrame > 0:
                    iTime = Frame2Time(iRemainFrame)
                    cl_notify.SendCommonNotify(self.m_Game, [
                        pid], 2002, {
                        '$time': str(iTime) })
            dReady = self.GetReadyTransferPlayer()
            iNpc = self.GetCurTransferNpc()
            for iPlayer, iIsReady in dReady.items():
                oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(iPlayer)
                npcnet.GS2CTransferReadyStat(oHero, iNpc, iIsReady, {
                    pid: 1 })
            

    
    def OnLevelStart(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        self.m_LevelCountDict.setdefault(iLevelType, 0)
        self.m_LevelCountDict[iLevelType] += 1

    
    def InitLevelNode(self):
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'LevelCtrlPlayerLogin', -1)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self, { })
        if self.m_SavedLevelInfo:
            dTransfer = self.m_SavedLevelInfo
            iTranLevelID = dTransfer['LevelID']
            iTranLayer = dTransfer['LayerNum']
            iTranLevel = dTransfer['LevelNum']
            (iTranLType, iTranTType) = self.GetLevelInfo(iTranLayer, iTranLevel, iTranLevelID)
            self.m_LayerNum = iTranLayer
            self.m_LevelNum = iTranLevel
            self.m_CurLType = iTranLType
            self.m_CurTType = iTranLevel
            self.CreateMainLevel(iTranLevelID, iTranLayer, iTranLevel, iTranLType, iTranTType, True)
            self.ContinueGameInitData()
            self.m_SavedLevelInfo = { }
        else:
            dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
            iHallLevel = dLayerData['HallInfo']
            if self.m_DirectLevel:
                iLevel = self.m_DirectLevel
                if iLevel != iHallLevel:
                    self.m_CurLType = LEVEL_TYPE_FIGHT
                else:
                    iLevel = iHallLevel
            None.CreateMainLevel(iLevel, self.m_LayerNum, self.m_LevelNum, self.m_CurLType, self.m_CurTType, True)

    
    def NextLevel(self, dTransfer):
        if not dTransfer:
            return None
        iTranLevelID = dTransfer['LevelID']
        iTranLayer = dTransfer['LayerNum']
        iTranLevel = dTransfer['LevelNum']
        (iTranLType, iTranTType) = self.GetLevelInfo(iTranLayer, iTranLevel, iTranLevelID)
        self.CreateMainLevel(iTranLevelID, iTranLayer, iTranLevel, iTranLType, iTranTType, False)

    
    def GetLineNode(self, tLineIdx):
        if not tLineIdx:
            return None
        (iLevel, _, _) = tLineIdx
        oLevelNode = self.GetLevelNode(iLevel)
        if oLevelNode:
            return oLevelNode.GetLineNode(tLineIdx)

    
    def GetMonsterCtrl(self, tLineIdx):
        oLine = self.GetLineNode(tLineIdx)
        if not oLine:
            return None
        return oLine.m_MonsterCtrl

    
    def CreateMainLevel(self, iLevel, iLayerNum, iLevelNum, iLType, iTType, bInit):
        oWarMgr = self.m_Game.m_WarMgr
        iBaseLayerNum = self.m_Game.m_WarMgr.GetBaseLayer(iLayerNum)
        if bInit or self.m_LayerNum != iLayerNum or self.m_BaseLayerNum != iBaseLayerNum:
            self.m_BaseLayerNum = iBaseLayerNum
            dMsgInfo = {
                'Layer': iLayerNum }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_LAYERSTART, self, dMsgInfo)
            self.LayerStart(iLayerNum)
            if self.m_SavedLevelInfo:
                self.m_LayerChoose.Load(self.m_SavedLevelInfo)
            self.m_HideLevelTypeRecord = { }
            dFilterType = self.m_LayerChoose.GetHideLevelTypeCntDict()
            for iHideType in dFilterType:
                self.m_HideLevelTypeRecord[iHideType] = 0
            
        lstHero = oWarMgr.GetLiveHero()
        lstPlayer = oWarMgr.GetLivePlayer()
        if not bInit:
            self.m_LayerNum = iLayerNum
            self.m_LevelNum = iLevelNum
            self.m_CurLType = iLType
            self.m_CurTType = iTType
        LevelLog.Info('%s players%s %s createmainlevel layer:%d level:%d type:(%d, %d) levelid:%d' % (self.m_Game.m_ID, lstPlayer, lstHero, iLayerNum, iLevelNum, iLType, iTType, iLevel))
        oLevelNode = levelline.GetLevelNode(self, iLType, iTType, iLevel)
        if not oLevelNode:
            LevelLog.Error('%s Create MainLevel failed! (layercnt:%d, levelcnt:%d, levelid%d)' % (self.m_Game.m_ID, iLayerNum, iLevelNum, iLevel))
            return None
        if iLType == LEVEL_TYPE_FIGHT:
            tLevelKey = (iBaseLayerNum, iLevelNum)
            lstLevelMark = self.m_MainLevelRecord.get(tLevelKey, [])
            lstLevelMark.append(iLevel)
            self.m_MainLevelRecord[tLevelKey] = lstLevelMark[-2:]
        if oWarMgr.RefreshPlayerCnt():
            oLevelNode.m_NotifyPlayerCntChange = True
            oLevelNode.m_QuittedPlayerInfo = oWarMgr.UseQuittedPlayerInfo()
        dLastLevelInfo = { }
        if self.m_CurNode:
            dLastLevelInfo = self.m_CurNode.GetPassToNextLevelInfo()
        oLevelNode.SetLastLevelInfo(dLastLevelInfo)
        self.m_CurNode = oLevelNode
        self.InitLevelNodeLib()
        self.AddLevelNode(oLevelNode)
        self.ChooseHideLevel()
        self.m_CurTransfer = self.GetTransferInfo(self.m_CurNode.m_Difficulty)
        self.m_LevelAssignBornPos = { }
        LevelLog.Info('%s players%s %s (%d-%d) choosehidelevel:%s transfer%s' % (self.m_Game.m_ID, lstPlayer, lstHero, iLayerNum, iLevelNum, self.m_HideLevelLib, list(self.m_CurTransfer)))
        iAsyncload = cllib.lib_flag.g_OpenAsyncLoad
        if not iAsyncload:
            oLevelNode.LevelInit(self.m_Game.m_WarMgr, {
                'LevelID': iLevel,
                'iScene': oLevelNode.m_Scene })
        oLevelNode.TryHeroEnterLevel(lstHero)

    
    def LayerStart(self, iLayerNum):
        oWarMgr = self.m_Game.m_WarMgr
        dLayerData = self.m_LevelCtrlConf.get(iLayerNum, { })
        dRoundChooseData = dLayerData.get('LayerChoose', { })
        dChooseData = dRoundChooseData[oWarMgr.m_Round] if oWarMgr.m_Round in dRoundChooseData else { }
        dBaseGrade = dLayerData.get('BaseGrade', { })
        iCycle = oWarMgr.m_Cycle
        if iCycle in dBaseGrade:
            dCurBaseGrade = dBaseGrade[iCycle]
        else:
            dCurBaseGrade = dBaseGrade.get(0, { })
        self.m_LayerChoose.OnLayerStart(dChooseData, dCurBaseGrade, iLayerNum)

    
    def ChooseHideLevel(self):
        self.m_HideLevelLib = { }
        iLayerNum = self.m_LayerNum
        iLevelNum = self.m_LevelNum
        dWarData = self.m_LevelCtrlConf
        if iLayerNum not in dWarData:
            return None
        dLayerData = dWarData[iLayerNum]
        if iLevelNum not in dLayerData['CtrlInfo']:
            return None
        iCnt = self.m_LayerChoose.GetMainLevelHideCnt(iLevelNum)
        if not iCnt:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        iWarRound = oWarMgr.m_Round
        iWarCycle = oWarMgr.m_Cycle
        dSource = dLayerData['CtrlInfo'][iLevelNum]['HideLevelStore']
        if not dSource:
            return None
        dChooseWeight = { }
        bDone = False
        for iRound in range(iWarRound, -1, -1):
            for iCycle in range(iWarCycle, -1, -1):
                if (iRound, iCycle) in dSource:
                    dChooseWeight = dSource[(iRound, iCycle)]
                    bDone = True
                    break
            
            if bDone:
                break
        else:
            if iWarRound in dSource:
                dChooseWeight = dSource[iWarRound]
        if not dChooseWeight:
            return None
        iNewVerLayer = oWarMgr.GetNewVerLayer()
        dWeight = { }
        for (iLevel, iType, iLabel, (iMinGrade, iMaxGrade), iCheckNewVerLayer), iWeight in dChooseWeight.items():
            if iLevel in self.m_FilterHideLevel or iType in self.m_FilterHideLevelType:
                continue
            if iCheckNewVerLayer != -1 and iNewVerLayer != iCheckNewVerLayer:
                continue
            for iHero in oWarMgr.GetRoomHero():
                oHero = self.m_Game.GetObject(iHero)
                if (oHero or iMinGrade <= oHero.m_PlayerGrade) and oHero.m_PlayerGrade <= iMaxGrade and iWeight:
                    dWeight[(iLevel, iType, iLabel)] = iWeight
                    break
            
        
        dTypeWeight = { }
        lstTypeLimit = []
        dHideLevelChooseInfo = self.m_Game.m_WarData.GetHideLevelChooseInfo()
        for iCheckType in dHideLevelChooseInfo:
            if iCheckType in self.m_HideLevelTypeNumRecord and self.m_HideLevelTypeNumRecord[iCheckType] >= dHideLevelChooseInfo[iCheckType]:
                lstTypeLimit.append(iCheckType)
        
        for tLevelInfo, iWeight in dWeight.items():
            if tLevelInfo[1] not in lstTypeLimit:
                dTypeWeight[tLevelInfo] = iWeight
        
        if iCnt <= len(dTypeWeight):
            dWeight = dTypeWeight
        lstHideLevel = []
        dFilterType = self.m_LayerChoose.GetHideLevelTypeCntDict()
        if dFilterType:
            for i in range(iCnt):
                dFilterWeight = self.FilterRecordHideLevelByType(dWeight, lstHideLevel, 1)
                lstLevel = self.ChooseHideLevelByLabel(dFilterWeight)
                for iLevel, iType, iLabel in lstLevel:
                    self.m_HideLevelTypeRecord[iType] += 1
                
                lstHideLevel.extend(lstLevel)
            
        else:
            oWeaponStoreElement = oWarMgr.GetComponent('WeaponStoreElement')
            if oWeaponStoreElement:
                dWeight = oWeaponStoreElement.GetHideLevelByLimitType(self, dWeight)
            dFilterWeight = self.FilterRecordHideLevel(dWeight, iCnt)
            for i in range(iCnt):
                lstHideLevel.extend(self.ChooseHideLevelByLabel(dFilterWeight))
            
        for iLevel, iType, iLabel in lstHideLevel:
            self.m_HideLevelLib[iLevel] = iType
        

    
    def ChooseHideLevelByLabel(self, dHideLevel):
        dNewHideLevel = { }
        dNewExSelfHideLevel = { }
        if self.m_LastHideLevel:
            (iChooseLevel, iChooseType, iChooseLabel) = self.m_LastHideLevel[0]
            for (iLevel, iType, iLabel), iWeight in dHideLevel.items():
                if iChooseLabel != 0 and iType == iChooseType and iLabel == iChooseLabel:
                    continue
                dNewHideLevel[(iLevel, iType, iLabel)] = iWeight
                if iChooseLevel == iLevel:
                    continue
                dNewExSelfHideLevel[(iLevel, iType, iLabel)] = iWeight
            
            if len(dNewHideLevel) > 1:
                dNewHideLevel = dNewExSelfHideLevel
            elif len(dNewHideLevel) == 0:
                dNewHideLevel = dHideLevel
            else:
                dNewHideLevel = dHideLevel
        lstHideLevel = None(self.m_Game, dNewHideLevel, 1)
        self.m_LastHideLevel = lstHideLevel
        return lstHideLevel

    
    def FilterRecordHideLevel(self, dHideLevel, iCnt):
        dNewHideLevel = { }
        lstRecord = self.m_HideLevelRecord.get(self.m_LayerNum, [])
        for (iLevel, iType, iLabel), iWeight in dHideLevel.items():
            if iLevel in lstRecord:
                continue
            dNewHideLevel[(iLevel, iType, iLabel)] = iWeight
        
        if len(dNewHideLevel) < iCnt:
            return dHideLevel
        return dNewHideLevel

    
    def FilterRecordHideLevelByType(self, dHideLevel, lstData, iCnt):
        dNewHideLevel = { }
        lstFilter = [ tData[0] for tData in lstData ]
        lstRecord = self.m_HideLevelRecord.get(self.m_LayerNum, [])
        dFilterType = self.m_LayerChoose.GetHideLevelTypeCntDict()
        for (iLevel, iType, iLabel), iWeight in dHideLevel.items():
            if iLevel in lstRecord or iLevel in lstFilter:
                continue
            if iType in dFilterType and self.m_HideLevelTypeRecord[iType] >= dFilterType[iType]:
                continue
            dNewHideLevel[(iLevel, iType, iLabel)] = iWeight
        
        if len(dNewHideLevel) < iCnt:
            dNewHideLevel = { }
            for (iLevel, iType, iLabel), iWeight in dHideLevel.items():
                if iLevel in lstFilter:
                    continue
                if iType in dFilterType and self.m_HideLevelTypeRecord[iType] >= dFilterType[iType]:
                    continue
                dNewHideLevel[(iLevel, iType, iLabel)] = iWeight
            
        if len(dNewHideLevel) < iCnt:
            dNewHideLevel = { }
            for (iLevel, iType, iLabel), iWeight in dHideLevel.items():
                if iLevel in lstFilter:
                    continue
                dNewHideLevel[(iLevel, iType, iLabel)] = iWeight
            
        return dNewHideLevel

    
    def CreateHideLevel(self, iBaseLevel, iLevel = 0):
        if iBaseLevel not in self.m_HideLevelLib:
            return None
        if not iLevel:
            iLevel = iBaseLevel
        iLType = LEVEL_TYPE_HIDE
        iGType = self.GetLevelTypeInFight(iLevel)
        iHideType = self.m_HideLevelLib[iBaseLevel]
        oLevelNode = levelline.GetLevelNode(self, iLType, iGType, iLevel, iHideType)
        self.AddLevelNode(oLevelNode)
        lstRecord = self.m_HideLevelRecord.get(self.m_LayerNum, [])
        lstRecord.append(iBaseLevel)
        self.m_HideLevelRecord[self.m_LayerNum] = lstRecord[-2:]
        if iHideType in self.m_HideLevelTypeNumRecord:
            self.m_HideLevelTypeNumRecord[iHideType] += 1
        else:
            self.m_HideLevelTypeNumRecord[iHideType] = 1
        iAsyncload = cllib.lib_flag.g_OpenAsyncLoad
        if not iAsyncload:
            oLevelNode.LevelInit(self.m_Game.m_WarMgr, {
                'LevelID': iLevel,
                'iScene': oLevelNode.m_Scene })
        return oLevelNode

    
    def GetTransferInfo(self, iNowLevelDiff = LEVEL_DIFF_NORMAL):
        dTransfers = { }
        dWarData = self.m_LevelCtrlConf
        iLayerNum = self.m_LayerNum
        iLevelNum = self.m_LevelNum
        if iLayerNum not in dWarData:
            return dTransfers
        dLayerData = dWarData[iLayerNum]
        dNextLayerData = dWarData.get(iLayerNum + 1, { })
        iMaxLevel = dLayerData['CtrlSize']
        if iLevelNum == iMaxLevel + 1 and dNextLayerData:
            iLevel = dNextLayerData['HallInfo']
            dTransfers[iLevel] = {
                'LevelID': iLevel,
                'LayerNum': iLayerNum + 1,
                'LevelNum': 0 }
        elif iLevelNum == iMaxLevel:
            iLevel = self.ChooseBossLevel(dLayerData['BossInfo'])
            dTransfers[iLevel] = {
                'LevelID': iLevel,
                'LayerNum': iLayerNum,
                'LevelNum': iLevelNum + 1 }
        elif iLevelNum < iMaxLevel:
            dLevelInfo = dLayerData['CtrlInfo'][iLevelNum + 1]
            iBaseLayer = self.m_Game.m_WarMgr.GetBaseLayer(iLayerNum)
            lstLevelMark = self.m_MainLevelRecord.get((iBaseLayer, iLevelNum + 1), [])
            setDaobiaoFilter = self.DaobiaoLevelFilter(dLevelInfo)
            setAllLevelMark = set(lstLevelMark) | setDaobiaoFilter | set(self.m_FilterMainLevel)
            lstLevelInfo = self.ChooseLevel(dLevelInfo, setAllLevelMark, 2, iNowLevelDiff, setDaobiaoFilter)
            for iLevel in lstLevelInfo:
                dTransfers[iLevel] = {
                    'LevelID': iLevel,
                    'LayerNum': iLayerNum,
                    'LevelNum': iLevelNum + 1 }
            
        return dTransfers

    
    def ChooseBossLevel(self, dLevelInfo):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        dChooseWeight = { }
        dWeight = dLevelInfo['BossStore']
        dExtra = dLevelInfo['BossExtra']
        for lv, iWeight in dWeight.items():
            if lv not in dExtra or not iWeight:
                continue
            (funcChoose, funcFroce) = dExtra[lv]
            if funcFroce and funcFroce(oWarMgr, lv):
                return lv
            if not not funcChoose:
                if funcChoose(oWarMgr, lv):
                    dChooseWeight[lv] = iWeight
                    continue
        
        dMsgInfo = {
            'FilterLevel': { } }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self, dMsgInfo)
        dFilterLevel = dMsgInfo['FilterLevel']
        if dFilterLevel:
            dNewWeight = { }
            LevelLog.Debug('%s filter bosslevel %s %s' % (oGame.m_ID, dFilterLevel, dChooseWeight))
            for iLevel, iWeight in dChooseWeight.items():
                if iLevel not in dFilterLevel:
                    dNewWeight[iLevel] = iWeight
            
            if dNewWeight:
                dChooseWeight = dNewWeight
        if not dChooseWeight:
            LevelLog.Alert('%d bosslevel empty %s' % (oGame.m_ID, dWeight))
            dChooseWeight = dWeight
        iLevel = ChooseKey(oGame, dChooseWeight)
        LevelLog.Debug('%d choosebosslevel %s %s' % (oGame.m_ID, iLevel, dChooseWeight))
        if not iLevel:
            LevelLog.Alert('%d bosslevel %s err %s %s' % (oGame.m_ID, iLevel, dChooseWeight, dWeight))
        return iLevel

    
    def ChooseLevel(self, dLevelInfo, setMark, iCount, iNowLevelDiff, setDaobiaoFilter):
        dFilterLevel = {
            'Nor': list(set(dLevelInfo['NormalStore']) - setMark),
            'Med': list(set(dLevelInfo['MediumStore']) - setMark),
            'Har': list(set(dLevelInfo['HardStore']) - setMark) }
        iLCount = sum((len(value) for value in dFilterLevel.values()))
        if iLCount >= iCount:
            return self.ChooseFightLevelRule(dLevelInfo, dFilterLevel, iCount, iNowLevelDiff)
        return self.ChooseFightLevelRandom(dLevelInfo, setDaobiaoFilter, iCount)

    
    def ChooseFightLevelRandom(self, dLevelInfo, setFilterMark, iCount):
        lstRandLevel = []
        lstRandLevel.extend(list(set(dLevelInfo['NormalStore']) - setFilterMark))
        lstRandLevel.extend(dLevelInfo['MediumStore'])
        lstRandLevel.extend(dLevelInfo['HardStore'])
        if not lstRandLevel:
            LevelLog.Error('no enough level %s %s' % (setFilterMark, dLevelInfo['NormalStore']))
            lstRandLevel.extend(dLevelInfo['NormalStore'])
        lstRandLevel = ShufferList(self.m_Game, lstRandLevel)
        lstTransfer = lstRandLevel[:iCount]
        return lstTransfer

    
    def ChooseFightLevelRule(self, dLevelInfo, dFilterLevel, iCount, iNowLevelDiff):
        lstTransfer = []
        for _ in range(iCount):
            dRatio = { }
            dWeight = { }
            dRatio[LEVEL_DIFF_NORMAL] = 0 if not dFilterLevel['Nor'] else dLevelInfo['Ratio'][0]
            dRatio[LEVEL_DIFF_MEDIUM] = 0 if not dFilterLevel['Med'] else dLevelInfo['Ratio'][1]
            dRatio[LEVEL_DIFF_HARD] = 0 if not dFilterLevel['Har'] else dLevelInfo['Ratio'][2]
            if sum(dRatio.values()) <= 0:
                break
            if iNowLevelDiff == LEVEL_DIFF_HARD:
                dRatio[LEVEL_DIFF_HARD] = 0
            iDifficult = ChooseKey(self.m_Game, dRatio)
            if iDifficult == LEVEL_DIFF_NORMAL:
                dWeight = dLevelInfo['NormalWeight']
                lstStore = dFilterLevel['Nor']
            elif iDifficult == LEVEL_DIFF_MEDIUM:
                dWeight = dLevelInfo['MediumWeight']
                lstStore = dFilterLevel['Med']
            else:
                dWeight = dLevelInfo['HardWeight']
                lstStore = dFilterLevel['Har']
            iLevel = self.ChoosePerFightLevel(dWeight, lstStore)
            if iLevel:
                lstTransfer.append(iLevel)
        
        return lstTransfer

    
    def ChoosePerFightLevel(self, dWeight, lstStore):
        dLevelSummary = { }
        for iLevel in lstStore:
            iType = self.GetLevelTypeInFight(iLevel)
            lstLevel = dLevelSummary.setdefault(iType, [])
            lstLevel.append(iLevel)
        
        dFilterWeight = { }
        for iType, iWeight in dWeight.items():
            if iType not in dLevelSummary:
                continue
            dFilterWeight[iType] = iWeight
        
        if not dFilterWeight:
            return 0
        iLevelType = ChooseKey(self.m_Game, dFilterWeight)
        lstLevelID = dLevelSummary[iLevelType]
        iLevel = lstLevelID[self.m_Game.Random(len(lstLevelID))]
        lstStore.remove(iLevel)
        return iLevel

    
    def RebuildLevel(self, lstLevelInfo):
        lstMainPend = []
        lstHidePend = []
        for dLevelInfo in lstLevelInfo:
            for sType in ('Main', 'Hide'):
                if sType not in dLevelInfo:
                    continue
                if sType == 'Main':
                    lstMainPend.append(dLevelInfo[sType])
                    continue
                if sType == 'Hide':
                    lstHidePend.append(dLevelInfo[sType])
            
        
        dMainPend = { }
        for dLevelInfo in lstMainPend:
            for iLayerNum, dLayer in dLevelInfo.items():
                for iLevelNum, tLevel in dLayer.items():
                    tKey = (iLayerNum, iLevelNum)
                    dMainPend.setdefault(tKey, [])
                    dMainPend[tKey].extend(list(tLevel))
                
            
        
        self.ChooseLevelRecord(dMainPend, self.m_MainLevelRecord)
        dHidePend = { }
        for dLevelInfo in lstHidePend:
            for iLayerNum, tLayer in dLevelInfo.items():
                lstPerPend = list(tLayer)
                lstPerPend = lstPerPend[-2:]
                dHidePend.setdefault(iLayerNum, [])
                dHidePend[iLayerNum].extend(lstPerPend)
            
        
        self.ChooseLevelRecord(dHidePend, self.m_HideLevelRecord)
        lstLivePlayer = self.m_Game.m_WarMgr.GetLivePlayer()
        LevelLog.Info('%s players%s rebuildline main:%s hide:%s' % (self.m_Game.m_ID, lstLivePlayer, self.m_MainLevelRecord, self.m_HideLevelRecord))

    
    def ChooseLevelRecord(self, dLevelPend, dLevelRecord):
        for key, lstLevel in dLevelPend.items():
            lstPerLevel = dLevelRecord.setdefault(key, [])
            dSort = { }
            for iLevel in lstLevel:
                dSort.setdefault(iLevel, 0)
                dSort[iLevel] += 1
            
            lstSort = sorted(dSort.items(), key = (lambda item: item[1]), reverse = True)
            for tSort in lstSort:
                if len(lstPerLevel) >= 2:
                    break
                lstPerLevel.append(tSort[0])
            
        

    
    def ValidRoundLevel(self, tKey, iLevel):
        dRoundFilter = self.m_LevelConfData.GetLevelBaseConf(iLevel, 'roundfilter')
        if not dRoundFilter:
            return 1
        oWarMgr = self.m_Game.m_WarMgr
        if oWarMgr.GetAllPlayerCnt() >= 3 and 'Team' in dRoundFilter and not dRoundFilter['Team']:
            return 0
        if oWarMgr.GetAllPlayerCnt() <= 2 and 'Single' in dRoundFilter and not dRoundFilter['Single']:
            return 0
        sKey = 'Round%d' % oWarMgr.m_Round
        if sKey in dRoundFilter and dRoundFilter[sKey]:
            return 1
        if dRoundFilter['KillBoss'] and oWarMgr.IsPassRound((1, 0, tKey[0])):
            return 1
        iPassMaxRound = oWarMgr.m_MaxRoundInfo[0]
        for iPassRound in range(1, iPassMaxRound):
            sKey = 'RoundPass%d' % iPassRound
            if sKey in dRoundFilter and dRoundFilter[sKey]:
                return 1
        
        return 0

    
    def DaobiaoLevelFilter(self, dLevelInfo):
        oWarMgr = self.m_Game.m_WarMgr
        iPlayerCnt = oWarMgr.Query('GMPlayerCnt')
        if not iPlayerCnt:
            iPlayerCnt = len(oWarMgr.GetAllPlayer())
        iRound = oWarMgr.m_Round
        iCycle = oWarMgr.m_Cycle
        lstFilterLevel = []
        dNormalFilter = dLevelInfo.get('NormalFilter', { })
        for iLevel in dLevelInfo['NormalStore']:
            if iLevel not in dNormalFilter or iLevel in lstFilterLevel:
                continue
            iValid = 1
            dFilter = dNormalFilter[iLevel]
            iNeedPlayerCnt = dFilter['PlayerCnt']
            lstNeedRoundInfo = dFilter['RoundInfo']
            fChooseAction = dFilter.get('ChooseAction', None)
            if iNeedPlayerCnt and iNeedPlayerCnt > iPlayerCnt:
                iValid = 0
            elif fChooseAction and not fChooseAction(oWarMgr, iLevel):
                iValid = 0
            elif lstNeedRoundInfo:
                if iRound not in lstNeedRoundInfo:
                    iValid = 0
                elif lstNeedRoundInfo[iRound] and iCycle not in lstNeedRoundInfo[iRound]:
                    iValid = 0
            if not iValid:
                lstFilterLevel.append(iLevel)
        
        return set(lstFilterLevel)

    
    def RoundLevelFilter(self):
        for iLayerNum, dLayerInfo in self.m_LevelCtrlConf.items():
            for iLevelNum, dLevelInfo in dLayerInfo['CtrlInfo'].items():
                lstLevel = set(itertools.chain(dLevelInfo['NormalStore'], dLevelInfo['MediumStore'], dLevelInfo['HardStore']))
                tKey = (iLayerNum, iLevelNum)
                for iLevel in lstLevel:
                    if not self.ValidRoundLevel(tKey, iLevel):
                        lstFilterLevel = self.m_MainLevelRecord.setdefault(tKey, [])
                        lstFilterLevel.append(iLevel)
                
            
        
        LevelLog.Info('%s %s %s roundfilter info:%s' % (self.m_Game.m_ID, self.m_Game.m_WarMgr.m_Round, self.m_Game.m_WarMgr.m_MaxRoundInfo, self.m_MainLevelRecord))

    
    def GetLevelInfo(self, iLayerNum, iLevelNum, iLevel):
        dWarData = self.m_LevelCtrlConf
        iLevelType = LEVEL_TYPE_NONE
        iGameType = GAMETYPE_NONE
        if iLayerNum in dWarData:
            iMaxLevel = dWarData[iLayerNum]['CtrlSize']
            if iLevelNum == 0:
                iLevelType = LEVEL_TYPE_HALL
            elif iLevelNum == iMaxLevel + 1:
                iLevelType = LEVEL_TYPE_BOSS
            elif iLevelNum <= iMaxLevel:
                iLevelType = LEVEL_TYPE_FIGHT
            iGameType = self.GetLevelTypeInFight(iLevel)
        return (iLevelType, iGameType)

    
    def GetLevelLayer(self, iLevel):
        return iLevel // 100000 % 10

    
    def CheckFinishWar(self):
        iMaxLayer = self.GetMaxLayer()
        if self.m_LayerNum >= iMaxLayer or self.m_Game.m_WarMgr.IsEndlessTimeOut():
            dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
            iMaxLevel = dLayerData['CtrlSize']
            if dLayerData['BossInfo']['BossStore']:
                iMaxLevel += 1
            if self.m_LevelNum >= iMaxLevel:
                return True
        return False

    
    def CheckLayerEndLevel(self):
        dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
        iMaxLevel = dLayerData['CtrlSize']
        if dLayerData['BossInfo']['BossStore']:
            iMaxLevel += 1
        if self.m_LevelNum >= iMaxLevel:
            return True
        return False

    
    def CheckFirstHall(self):
        if self.m_LayerNum == min(self.m_LevelCtrlConf) and self.m_LevelNum == 0 and self.m_CurLType == LEVEL_TYPE_HALL:
            return True
        return False

    
    def GetMaxLevel(self):
        dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
        iMaxLevel = dLayerData['CtrlSize']
        if dLayerData['BossInfo']['BossStore']:
            iMaxLevel += 1
        return iMaxLevel

    
    def GetFightMaxLevel(self):
        dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
        iMaxLevel = dLayerData['CtrlSize']
        return iMaxLevel

    
    def GetMaxLayer(self):
        oWarMgr = self.m_Game.m_WarMgr
        iMax = oWarMgr.GetMaxLayer()
        iResult = min(iMax, len(self.m_LevelCtrlConf))
        return iResult

    
    def GetLevelType(self, iLevel):
        iRound = self.m_Game.m_WarMgr.m_Round
        for _, dLayerInfo in self.m_LevelCtrlConf.items():
            if iLevel == dLayerInfo['HallInfo']:
                return LEVEL_TYPE_HALL
            if iLevel in dLayerInfo['BossInfo']['BossStore']:
                return LEVEL_TYPE_BOSS
            for _, dLevelInfo in dLayerInfo['CtrlInfo'].items():
                if iLevel in dLevelInfo['NormalStore']:
                    return LEVEL_TYPE_FIGHT
                if iLevel in dLevelInfo['MediumStore']:
                    return LEVEL_TYPE_FIGHT
                if iLevel in dLevelInfo['HardStore']:
                    return LEVEL_TYPE_FIGHT
                if iRound in dLevelInfo['HideLevel'] and iLevel in dLevelInfo['HideLevel'][iRound]:
                    return LEVEL_TYPE_HIDE
            
        
        return LEVEL_TYPE_NONE

    
    def GetLevelTypeInFight(self, iLevel):
        return iLevel // 100 % 10

    
    def GetLevelLayerAndLevelNum(self, iLevel):
        dCtrlData = self.m_LevelCtrlConf
        for iLayerNum, dLayerInfo in dCtrlData.items():
            dLevelInfo = dLayerInfo['CtrlInfo']
            if iLevel == dLayerInfo['HallInfo']:
                return (iLayerNum, 0)
            if iLevel in dLayerInfo['BossInfo']['BossStore']:
                return (iLayerNum, len(dLevelInfo) + 1)
            for iLevelNum, dInfo in dLevelInfo.items():
                for sKey in ('NormalStore', 'MediumStore', 'HardStore'):
                    if iLevel in dInfo[sKey]:
                        return (iLayerNum, iLevelNum)
                
            
        
        return (1, 0)

    
    def GetCurTransferNpc(self):
        return self.m_CurTransferNpc

    
    def GetReadyTransferPlayer(self):
        return self.m_ReadyTransferPlayer

    
    def SetCurTransferNpc(self, iNpc):
        self.m_CurTransferNpc = iNpc

    
    def SetReadyTransferPlayer(self, dPlayer):
        self.m_ReadyTransferPlayer = dPlayer

    
    def SetTranserReadyFrame(self, iFrame):
        if iFrame:
            self.m_TranserReadyFrame = self.m_Game.GetFrameNum() + iFrame
        else:
            self.m_TranserReadyFrame = 0

    
    def GetTransferReadyFrame(self):
        return self.m_TranserReadyFrame

    
    def CleanTranserInfo(self):
        self.m_CurTransferNpc = 0
        self.m_ReadyTransferPlayer = { }
        self.m_TranserReadyFrame = 0
        self.Remove_Call_Out('VoteNextLayer')

    
    def ContinueGameInitData(self):
        if not self.m_CurNode:
            return None
        self.m_CurNode.m_CustomData['ContinueGame'] = 1
        if 'BossLevelGoal' in self.m_SavedLevelInfo:
            self.m_CurNode.m_CustomData['BossLevelGoal'] = 1

    
    def GetWeaponRewardGrade(self):
        return self.m_Game.m_WarData.GetWeaponGrade(self.m_LayerNum, self.m_LevelNum, self.m_Game)

    
    def GetMonsterBaseGrade(self, iLevel):
        oLevelNode = self.GetLevelNode(iLevel)
        if not oLevelNode:
            return 0
        iLevelType = oLevelNode.m_LevelType
        iGrade = self.m_LayerChoose.GetMonsterBaseGrade(iLevelType, self.m_LevelNum)
        return iGrade

    
    def GetConfigLevel(self, iLevel):
        iLayerNum = self.m_LayerNum
        iLevelNum = self.m_LevelNum
        dCtrlInfo = self.m_LevelCtrlConf[iLayerNum]['CtrlInfo']
        if iLevelNum not in dCtrlInfo:
            return iLevel
        dData = dCtrlInfo[iLevelNum]
        if 'HideLevelConfMap' not in dData:
            return iLevel
        dData = dData['HideLevelConfMap']
        if iLevel in dData and dData[iLevel]:
            return dData[iLevel]
        return iLevel

    
    def GetHeroHideLevel(self, iLevel, iHero):
        if iLevel in self.m_HideLevelHeroMap and iHero in self.m_HideLevelHeroMap[iLevel]:
            return self.m_HideLevelHeroMap[iLevel][iHero]
        dCtrlInfo = self.m_LevelCtrlConf[self.m_LayerNum]['CtrlInfo']
        if self.m_LevelNum not in dCtrlInfo:
            return iLevel
        dConfingLevel = dCtrlInfo[self.m_LevelNum]
        if 'HideLevelAllocMap' not in dConfingLevel:
            return iLevel
        dHideLevelAllocMap = dConfingLevel['HideLevelAllocMap']
        if iLevel not in dHideLevelAllocMap or not dHideLevelAllocMap[iLevel]:
            return iLevel
        if iLevel not in self.m_HideLevelIndexMap:
            self.m_HideLevelIndexMap[iLevel] = 0
        iIndex = self.m_HideLevelIndexMap[iLevel] % len(dHideLevelAllocMap[iLevel])
        self.m_HideLevelIndexMap[iLevel] += 1
        if iLevel not in self.m_HideLevelHeroMap:
            self.m_HideLevelHeroMap[iLevel] = { }
        self.m_HideLevelHeroMap[iLevel][iHero] = dHideLevelAllocMap[iLevel][iIndex]
        return self.m_HideLevelHeroMap[iLevel][iHero]

    
    def AddLevelNode(self, oLevelNode):
        iLevel = oLevelNode.m_Level
        if iLevel not in self.m_LevelNodeLib:
            self.m_LevelNodeLib[iLevel] = oLevelNode

    
    def InitLevelNodeLib(self):
        lstLevel = []
        for iLevel, oLevelNode in self.m_LevelNodeLib.items():
            oLevelNode.Release()
            lstLevel.append(iLevel)
        
        self.m_LevelConfData.UnLoadLevelConf(lstLevel)
        self.m_LevelNodeLib = { }

    
    def GetLevelNode(self, iLevel):
        if isinstance(iLevel, tuple):
            iLevel = iLevel[0]
        if iLevel in self.m_LevelNodeLib:
            return self.m_LevelNodeLib[iLevel]

    
    def GetLayerAndLevelMap(self, iLayer, iLevel):
        dMap = self.m_LayerAndLevelMap
        if (iLayer, iLevel) in dMap:
            return dMap[(iLayer, iLevel)]
        return (iLayer, iLevel)

    
    def GetLevelCount(self, iLevelType):
        if iLevelType not in self.m_LevelCountDict:
            return 0
        return self.m_LevelCountDict[iLevelType]



class CLayerRandomChoose(object):
    
    def __init__(self, oCtrlMgr):
        self.m_CtrlMgr = oCtrlMgr
        self.m_LayerComonChoose = { }
        self.m_LayerBossChoose = { }
        self.m_LayerMonsterGrade = { }
        self.m_LayerAnalysisParam = {
            LAYER_CHOOSE_S8SHOP: 's8shop',
            LAYER_CHOOSE_S7SHOP: 's7shop',
            LAYER_CHOOSE_DICESHOP: 'diceshop',
            LAYER_CHOOSE_WANDSHOP: 'wandshop',
            LAYER_CHOOSE_RELICLOTTERY: 'reliclottery',
            LAYER_CHOOSE_REGROUPRELIC: 'regrouprelic',
            LAYER_CHOOSE_PETSHOP: 'petshop',
            LAYER_CHOOSE_TASKNPC: 'layertask',
            LAYER_CHOOSE_GSCASHSHOP: 'layergscashshop',
            LAYER_CHOOSE_CRAFTSMAN: 'layercraftman',
            LAYER_CHOOSE_SHOP: 'layershop',
            LAYER_CHOOSE_EVENTNPC: 'layereventnpc',
            LAYER_CHOOSE_CHALLENGE: 'layerchallenge',
            LAYER_CHOOSE_ELE: 'layerele',
            LAYER_CHOOSE_HIDE: 'layerhide' }
        self.m_HideLevelTypeCnt = { }

    
    def Release(self):
        self.m_CtrlMgr = None

    
    def Save(self):
        return self.m_LayerComonChoose

    
    def Load(self, dData):
        if not dData:
            return None
        for sFlag in self.m_LayerAnalysisParam.values():
            if sFlag in dData:
                self.m_LayerComonChoose[sFlag] = dData[sFlag]
        

    
    def FixLayerChallengeChooseWeight(self, iLayerNum, dChoose):
        if not dChoose:
            return { }
        dFixChoose = dict(dChoose)
        oGame = self.m_CtrlMgr.m_Game
        oWarMgr = oGame.m_WarMgr
        iWarRound = oWarMgr.m_Round
        iWarCycle = oWarMgr.m_Cycle
        bSingleGame = oWarMgr.IsSingleGame()
        dLayerData = self.m_CtrlMgr.m_LevelCtrlConf.get(iLayerNum, { })
        dCtrlInfo = dLayerData['CtrlInfo']
        for iLevel in dChoose:
            dLevelInfo = dCtrlInfo.get(iLevel, { })
            if not dLevelInfo:
                dFixChoose.pop(iLevel, 0)
                continue
            lstAllChallenge = []
            if not self.m_CtrlMgr.m_RoomChallenge.GetFightLevelChallenge(iWarRound, iWarCycle, bSingleGame, dLevelInfo, lstAllChallenge):
                dFixChoose.pop(iLevel, 0)
        
        return dFixChoose

    
    def OnLayerStart(self, dChooseData, dBaseGrade, iLayerNum):
        self.m_LayerComonChoose = { }
        oGame = self.m_CtrlMgr.m_Game
        oWarMgr = oGame.m_WarMgr
        dExtraInfo = oWarMgr.m_ExtraInfo
        if 'NewVerLayer' in dExtraInfo:
            if not (self.m_CtrlMgr.m_SavedLevelInfo) or 'HandleVoteTransfer' in self.m_CtrlMgr.m_SavedLevelInfo:
                oWarMgr.SetNewVerLayer(iIsNew = 0)
        oRandomMgr = oGame.m_RandomMgr
        for iType, (fExpect, fSigma, iMin, iMax, dChoose, dLimit) in dChooseData.items():
            if iType not in self.m_LayerAnalysisParam:
                continue
            fExpect = GetExpect(self.m_CtrlMgr, fExpect)
            dData = {
                'Expect': fExpect,
                'Sigma': fSigma,
                'Min': iMin,
                'Max': iMax,
                'Limit': dLimit,
                'Game': oGame }
            sFlag = self.m_LayerAnalysisParam[iType]
            dMsgInfo = {
                'Type': iType,
                'ChooseData': dData,
                'Layer': iLayerNum }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CHOOSECNT, self.m_CtrlMgr, dMsgInfo)
            if iType == LAYER_CHOOSE_CHALLENGE and dData.get('Expect', 0):
                dChoose = self.FixLayerChallengeChooseWeight(iLayerNum, dChoose)
            if not oRandomMgr.ValidRandom(sFlag):
                oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, sFlag, dChoose)
            else:
                oRandomMgr.SetChoose(sFlag, dChoose)
            self.m_LayerComonChoose[sFlag] = oRandomMgr.ChooseKey(sFlag, dData)
        
        if not oRandomMgr.ValidRandom('monstergrade'):
            oRandomMgr.InitRandom(cl_random.RANDOM_DIRECT, 'monstergrade', { })
        self.m_LayerMonsterGrade = dBaseGrade
        self.ChooseHideLevelTypeCnt()

    
    def ChooseHideLevelTypeCnt(self):
        if self.m_CtrlMgr.m_Game.m_WarMgr.m_SID != GetWarNo(PLAYMODE_DAYLY_TRIAL):
            return None
        self.m_HideLevelTypeCnt[HIDELV_TYPE_ELITE] = 2
        dWeight = { }
        for k in levelline.g_HideLevelNode:
            if k == HIDELV_TYPE_ELITE:
                continue
            self.m_HideLevelTypeCnt[k] = 0
            dWeight[k] = 1
        
        iType = ChooseKey(self.m_CtrlMgr.m_Game, dWeight)
        self.m_HideLevelTypeCnt[iType] = 1

    
    def GetHideLevelTypeCntDict(self):
        return self.m_HideLevelTypeCnt

    
    def GetMainLevelHideCnt(self, iLevelNum):
        if 'layerhide' in self.m_LayerComonChoose and iLevelNum in self.m_LayerComonChoose['layerhide']:
            return self.m_LayerComonChoose['layerhide'][iLevelNum]
        return 0

    
    def GetMainLevelScrollCnt(self, iLevelNum):
        if 'layerele' in self.m_LayerComonChoose and iLevelNum in self.m_LayerComonChoose['layerele']:
            return self.m_LayerComonChoose['layerele'][iLevelNum]
        return 0

    
    def GetMainLevelChallengeCnt(self, iLevelNum):
        if 'layerchallenge' in self.m_LayerComonChoose and iLevelNum in self.m_LayerComonChoose['layerchallenge']:
            return self.m_LayerComonChoose['layerchallenge'][iLevelNum]
        return 0

    
    def GetMainLevelCnt(self, iType, iLevelNum):
        iCnt = 0
        sKey = self.m_LayerAnalysisParam[iType]
        if sKey in self.m_LayerComonChoose and iLevelNum in self.m_LayerComonChoose[sKey]:
            iCnt = self.m_LayerComonChoose[sKey][iLevelNum]
        return iCnt

    
    def GetMainLevelLayerCnt(self, iType):
        iCnt = 0
        sKey = self.m_LayerAnalysisParam[iType]
        if sKey in self.m_LayerComonChoose:
            iCnt = sum(self.m_LayerComonChoose[sKey].values())
        return iCnt

    
    def GetBossLevelCnt(self, iType):
        iCnt = 0
        sKey = self.m_LayerAnalysisParam[iType]
        for dInfo in self.m_LayerBossChoose.values():
            if sKey in dInfo:
                iCnt += dInfo[sKey]
        
        return iCnt

    
    def GetBossLevelCntByType(self, sSourceKey, iType):
        iCnt = 0
        sKey = self.m_LayerAnalysisParam[iType]
        if sSourceKey in self.m_LayerBossChoose and sKey in self.m_LayerBossChoose[sSourceKey]:
            iCnt = self.m_LayerBossChoose[sSourceKey][sKey]
        return iCnt

    
    def SetBossLevelCnt(self, sSourceKey, iType, iCnt):
        sKey = self.m_LayerAnalysisParam[iType]
        if sSourceKey not in self.m_LayerBossChoose:
            self.m_LayerBossChoose[sSourceKey] = { }
        self.m_LayerBossChoose[sSourceKey][sKey] = iCnt

    
    def GetMonsterBaseGrade(self, iLevelType, iLevelNum):
        if iLevelType not in self.m_LayerMonsterGrade:
            return 0
        oRandomMgr = self.m_CtrlMgr.m_Game.m_RandomMgr
        tGrade = (0, 0)
        if iLevelType in (LEVEL_TYPE_HALL, LEVEL_TYPE_BOSS):
            tGrade = self.m_LayerMonsterGrade[iLevelType]
        elif iLevelType in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE) and iLevelNum in self.m_LayerMonsterGrade[iLevelType]:
            tGrade = self.m_LayerMonsterGrade[iLevelType][iLevelNum]
        dData = {
            'Expect': tGrade[0],
            'Sigma': tGrade[1] }
        return oRandomMgr.ChooseKey('monstergrade', dData)



def GetComponentClass(oMgrManager):
    return CLevelCtrlElement


def GetExpect(obj, value):
    if isinstance(value, float):
        return value
    return float(cl_formula.GetFormulaResult(obj, value))

