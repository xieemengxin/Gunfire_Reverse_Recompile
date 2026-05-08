# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_roomchallenge/roomchallenge.pyc
# RelativePath: clientlogic/cl_roomchallenge/roomchallenge.pyc
# Source Generated with Decompyle++
# File: roomchallenge.pyc (Python 3.6)

from cl_commondefines import GAMETYPE_LIMITLIVE, GAMETYPE_DEFEND, GAMETYPE_LIMITDEFEND, GAMETYPE_CONVOY, CHALLENGE_EXTRAMONSTER, CHALLENGE_EXTRAELITE, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, PLAYMODE_DAYLY_TRIAL, MODE_SNOWMOUNTAINS, ELITEINTRUDE_CHALLENGE, OLDVERLAYER_VALID, NEWVERLAYER_VALID, ALLVERLAYER_VALID
from cl_only import SendAlert, ChooseMulKeys, ChooseKey
import cl_msgcenter
from . import precollect

class CRoomChallengeMgr(object):
    
    def __init__(self, oLevelCtrl):
        self.m_LevelCtrl = oLevelCtrl
        self.m_Game = oLevelCtrl.m_Game
        self.m_Challenge = { }
        self.m_IgnoreRoom = { }
        self.m_IgnoreChallenge = set()
        self.m_ChooseChallenge = { }
        self.m_LastLevelChooseChallenge = []
        self.m_ChallengeLevelType = (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS)
        self.m_PreCollect = precollect.CPreCollect(self)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, 'RoomChallenge', -1, 0)
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnChooseChallenge, 'RoomChallenge', -1, 0)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'RoomChallenge')

    
    def Release(self):
        self.m_PreCollect.Release()
        lstTotalChallenge = []
        for _, dChallenge in self.m_Challenge.items():
            lstTotalChallenge.extend(list(dChallenge.values()))
        
        for oChallenge in lstTotalChallenge:
            oChallenge.Release()
        
        self.m_Challenge = { }
        oLevelCtrl = self.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMSTART, 'RoomChallenge')
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'RoomChallenge')
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'RoomChallenge')
        self.m_LevelCtrl = None
        self.m_Game = None

    
    def ClearLevel(self, iLevel):
        if iLevel not in self.m_Challenge:
            return None
        dChallenge = self.m_Challenge.pop(iLevel)
        for oChallenge in dChallenge.values():
            oChallenge.Release()
        

    
    def AddChallenge(self, iLevel, iRoomPos, iChallengeSID, iSkipReward = 0, sReason = ''):
        if iLevel in self.m_IgnoreRoom and iRoomPos in self.m_IgnoreRoom[iLevel]:
            return None
        dChallenge = self.m_Challenge.setdefault(iLevel, { })
        if iRoomPos in dChallenge:
            return None
        oChallenge = self.m_Game.m_ResMgr.CreateRoomChallenge(iLevel, iRoomPos, iChallengeSID, sReason)
        if not oChallenge:
            return None
        if iSkipReward:
            oChallenge.m_Reward = { }
        dChallenge[iRoomPos] = oChallenge
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGER_CHALLENGE_EVENT, self.m_Game.m_WarMgr, dInfo = {
            'ChallengeId': iChallengeSID,
            'ChallengeLevel': iLevel })

    
    def GetChallenge(self, tLineIdx):
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel not in self.m_Challenge:
            return None
        dChallenge = self.m_Challenge[iLevel]
        if iRoomPos not in dChallenge:
            return None
        return dChallenge[iRoomPos]

    
    def ChallengeRelease(self, iLevel, iRoomPos):
        if iLevel not in self.m_Challenge:
            return None
        dChallenge = self.m_Challenge[iLevel]
        if iRoomPos not in dChallenge:
            return None
        dChallenge.pop(iRoomPos)
        if not dChallenge:
            self.m_Challenge.pop(iLevel)

    
    def AddIgnoreRoom(self, iLevel, iRoomPos):
        dRoom = self.m_IgnoreRoom.setdefault(iLevel, { })
        dRoom[iRoomPos] = 1

    
    def RemoveIgnoreRoom(self, iLevel, iRoomPos):
        if iLevel not in self.m_IgnoreRoom:
            return None
        if iRoomPos not in self.m_IgnoreRoom[iLevel]:
            return None
        self.m_IgnoreRoom[iLevel].pop(iRoomPos)
        if not self.m_IgnoreRoom[iLevel]:
            self.m_IgnoreRoom.pop(iLevel)

    
    def AddIgnoreChallenge(self, lstChallenge):
        self.m_IgnoreChallenge |= set(lstChallenge)

    
    def OnRoomStart(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        oWarMgr = self.m_Game.m_WarMgr
        iChallengeSID = 0
        oLevelNode = self.m_LevelCtrl.GetLevelNode(iLevel)
        roomLst = oLevelNode.m_RoomList
        dWarData = self.m_LevelCtrl.m_LevelCtrlConf
        iLayerNum = self.m_LevelCtrl.m_LayerNum
        dLayerData = dWarData[iLayerNum]
        iMaxLevel = dLayerData['CtrlSize']
        iLevelNum = self.m_LevelCtrl.m_LevelNum
        iLevelType = self.m_LevelCtrl.GetLevelType(iLevel)
        if oWarMgr.Query('AssignRoomChallenge'):
            iChallengeSID = oWarMgr.Query('AssignRoomChallenge')
            oWarMgr.Delete('AssignRoomChallenge')
        if not iChallengeSID and (iLevel, iRoomPos) in self.m_ChooseChallenge:
            iChallengeSID = self.m_ChooseChallenge[(iLevel, iRoomPos)]
        iBaseLayerNum = self.m_Game.m_WarMgr.GetBaseLayer(iLayerNum)
        if oWarMgr.Query('BenedictionChallenge') and iLevelType == LEVEL_TYPE_FIGHT and iLevelNum == iMaxLevel and iRoomPos == len(roomLst) - 1:
            dChallengeInfo = oWarMgr.Query('BenedictionChallenge', { })
            dInfo = {
                'ChallengeInfo': dChallengeInfo,
                'Layer': iBaseLayerNum }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_REPLACECHALLENGE_PRE, self.m_Game.m_WarMgr, dInfo)
            if iBaseLayerNum not in dChallengeInfo:
                SendAlert('err', '祝福指定刷房间挑战出错：基础幕数%d 地图%d未配置房间挑战' % (iBaseLayerNum, oLevelNode.m_Map))
            else:
                dLayerChallengeInfo = dChallengeInfo[iBaseLayerNum]
                if not iChallengeSID:
                    iChallengeSID = self.GetReplaceRoomChallenge(dLayerChallengeInfo)
                else:
                    clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallengeSID)
                    if clsChallengeData.m_Type != CHALLENGE_EXTRAMONSTER:
                        iChallengeSID = self.GetReplaceRoomChallenge(dLayerChallengeInfo)
        if MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType and iLayerNum >= 2 and iLevelType == LEVEL_TYPE_FIGHT and iLevelNum == iMaxLevel and iRoomPos == len(roomLst) - 1:
            dChallengeInfo = oWarMgr.Query('SnowMountainChallenge', { })
            dInfo = {
                'ChallengeInfo': dChallengeInfo,
                'Layer': iBaseLayerNum }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_REPLACECHALLENGE_PRE, self.m_Game.m_WarMgr, dInfo)
            if iBaseLayerNum in dChallengeInfo:
                dLayerChallengeInfo = dChallengeInfo[iBaseLayerNum]
                iChallengeSID = self.GetReplaceRoomChallenge(dLayerChallengeInfo)
        if iChallengeSID:
            self.AddChallenge(iLevel, iRoomPos, iChallengeSID, sReason = 'Normal')

    
    def GetReplaceRoomChallenge(self, dLayerChallengeInfo):
        oWarMgr = self.m_Game.m_WarMgr
        if oWarMgr.GetNewVerLayer():
            iNowVerLayer = NEWVERLAYER_VALID
        else:
            iNowVerLayer = OLDVERLAYER_VALID
        dChallenge = { }
        for iChallengeSID in dLayerChallengeInfo:
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallengeSID)
            if not clsChallengeData:
                continue
            iVerLayer = clsChallengeData.GetValidVerLayer()
            if iVerLayer in (ALLVERLAYER_VALID, iNowVerLayer):
                dChallenge[iChallengeSID] = 1
        
        return ChooseKey(self.m_Game, dChallenge)

    
    def OnPlayerMapLoadOK(self, oLevelCtrl, oHero, dInfo):
        if not self.m_Challenge:
            return None
        iLevel = dInfo['LevelID']
        if iLevel not in self.m_Challenge:
            return None
        dChallenge = self.m_Challenge[iLevel]
        for oChallenge in dChallenge.values():
            lstPlayer = [
                oHero.m_PlayerID]
            oChallenge.HeroReEnterScene(lstPlayer)
        

    
    def OnChooseChallenge(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        self.m_PreCollect.CollectOnLevelInit(iLevel)
        dChooseChallenge = { }
        if self.ValidChooseChallenge(dInfo):
            self.m_ChooseChallenge = { }
            iCnt = self.GetChooseCnt(dInfo)
            if iCnt:
                dAllChallenge = self.GetAllChallenge(dInfo, False)
                if dAllChallenge:
                    dChooseBeforeMsgInfo = {
                        'ChallengeWeight': dAllChallenge,
                        'Info': dInfo,
                        'Level': iLevel }
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE_BEFORE, self.m_Game.m_WarMgr, dChooseBeforeMsgInfo)
                    if dAllChallenge:
                        dChooseChallenge = self.ChooseChallenge(iCnt, dAllChallenge, dInfo)
        dChooseMsgInfo = {
            'ChooseChallenge': dChooseChallenge }
        dChooseMsgInfo.update(dInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.m_Game.m_WarMgr, dChooseMsgInfo)
        if dChooseChallenge:
            self.m_ChooseChallenge = dChooseChallenge
            self.m_LastLevelChooseChallenge = list(dChooseChallenge.values())
            self.m_PreCollect.CollectOnChoose(iLevel, self.m_ChooseChallenge)

    
    def GetChooseChallengeInfo(self):
        return self.m_ChooseChallenge

    
    def ValidChooseChallenge(self, dInfo):
        iResult = 1
        if dInfo['LevelType'] not in self.m_ChallengeLevelType:
            iResult = 0
        if dInfo['GameType'] in (GAMETYPE_CONVOY, GAMETYPE_DEFEND, GAMETYPE_LIMITDEFEND, GAMETYPE_LIMITLIVE):
            iResult = 0
        if self.m_Game.m_WarMgr.m_Round == 1 and self.m_Game.m_WarMgr.m_PlayMode != PLAYMODE_DAYLY_TRIAL:
            iTargetRound = 1
            iTargetCycle = 0
            iTargetLayer = dInfo['Layer']
            if not self.m_Game.m_WarMgr.IsPassRound((iTargetRound, iTargetCycle, iTargetLayer)):
                iResult = 0
        return iResult

    
    def GetChooseCnt(self, dInfo):
        if dInfo['LevelType'] == LEVEL_TYPE_BOSS:
            iWarRound = self.m_Game.m_WarMgr.m_Round
            iWarCycle = self.m_Game.m_WarMgr.m_Cycle
            dLayerData = self.m_LevelCtrl.m_LevelCtrlConf[dInfo['Layer']]
            if self.IsChallengeModeLimit(dLayerData):
                return 1
            dChallenge = dLayerData['BossInfo']['ChallengeStore']
            for iRound in range(iWarRound, -1, -1):
                for iCycle in range(iWarCycle, -1, -1):
                    if (iRound, iCycle) in dChallenge:
                        return 1
                
            
            return 0
        return self.m_LevelCtrl.m_LayerChoose.GetMainLevelChallengeCnt(dInfo['Level'])

    
    def GetAllChallenge(self, dInfo, bHide):
        dLevelInfo = self.GetLevelInfo(dInfo)
        if not dLevelInfo:
            return []
        lstAllChallenge = []
        oWarMgr = self.m_Game.m_WarMgr
        iWarRound = oWarMgr.m_Round
        iWarCycle = oWarMgr.m_Cycle
        bSingleGame = oWarMgr.IsSingleGame()
        dLayerData = self.m_LevelCtrl.m_LevelCtrlConf[dInfo['Layer']]
        if dInfo['LevelType'] == LEVEL_TYPE_BOSS and self.IsChallengeModeLimit(dLayerData):
            dChallengeModeLimit = dLayerData['BossInfo']['ChallengeModeLimit']
            sModelLimit = 'SINGLE' if bSingleGame else 'MULTI'
            for iWarModeType in oWarMgr.m_ModeType:
                iCurMaxRound = 0
                iCurMaxCycle = 0
                dLimitExt = { }
                for tKey, dModeChallenge in dChallengeModeLimit.items():
                    (iRound, iCycle, iModeType) = tKey
                    if iModeType != iWarModeType:
                        continue
                    if (iRound > iWarRound or iRound == iWarRound) and iCycle > iWarCycle:
                        continue
                    if (iRound < iCurMaxRound or iRound == iCurMaxRound) and iCycle < iCurMaxCycle:
                        continue
                    iCurMaxRound = iRound
                    iCurMaxCycle = iCycle
                    dLimitExt = dModeChallenge
                
                if dLimitExt:
                    lstAllChallenge.extend(dLimitExt[sModelLimit])
            
        else:
            lstAllChallenge = self.GetFightLevelChallenge(iWarRound, iWarCycle, bSingleGame, dLevelInfo, lstAllChallenge)
        setExcludeChallenge = self.m_IgnoreChallenge.copy()
        if bHide:
            if not lstAllChallenge:
                dHideLevelChallenge = dLevelInfo['HideLevelRoomChallenge']
                for iRound in range(iWarRound, -1, -1):
                    bDone = False
                    for iCycle in range(iWarCycle, -1, -1):
                        tKey = (iRound, iCycle)
                        if tKey in dHideLevelChallenge:
                            bDone = True
                            lstAllChallenge = dHideLevelChallenge[tKey]
                            break
                    
                    if bDone:
                        break
                
            iLevel = dInfo['LevelID']
            dHideLevelExcludeChallenge = dLevelInfo['HideLevelExcludeChallenge']
            dExcludeChallenge = { }
            bDone = False
            for iRound in range(iWarRound, -1, -1):
                for iCycle in range(iWarCycle, -1, -1):
                    if (iRound, iCycle) in dHideLevelExcludeChallenge:
                        dExcludeChallenge = dHideLevelExcludeChallenge[(iRound, iCycle)]
                        if iLevel in dExcludeChallenge:
                            bDone = True
                            setExcludeChallenge.update(set(dExcludeChallenge[iLevel]))
                            break
                
                if bDone:
                    break
            else:
                dExcludeChallenge = dHideLevelExcludeChallenge[iWarRound] if iWarRound in dHideLevelExcludeChallenge else []
                if iLevel in dExcludeChallenge:
                    setExcludeChallenge.update(set(dExcludeChallenge[iLevel]))
        dTrueAllChallenge = { }
        if oWarMgr.GetNewVerLayer():
            iNowVerLayer = NEWVERLAYER_VALID
        else:
            iNowVerLayer = OLDVERLAYER_VALID
        for iChallenge, iWeight in lstAllChallenge:
            if iChallenge in setExcludeChallenge:
                continue
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallenge)
            if not clsChallengeData:
                continue
            iVerLayer = clsChallengeData.GetValidVerLayer()
            if iVerLayer not in (ALLVERLAYER_VALID, iNowVerLayer):
                continue
            dTrueAllChallenge[iChallenge] = iWeight
        
        return dTrueAllChallenge

    
    def GetFightLevelChallenge(self, iWarRound, iWarCycle, bSingleGame, dLevelInfo, lstAllChallenge):
        if bSingleGame:
            dSingleChallenge = dLevelInfo['SingleChallengeStore']
        else:
            dSingleChallenge = { }
        dChallenge = dLevelInfo['ChallengeStore']
        for iRound in range(iWarRound, -1, -1):
            bDone = False
            for iCycle in range(iWarCycle, -1, -1):
                tKey = (iRound, iCycle)
                if tKey in dSingleChallenge and dSingleChallenge[tKey]:
                    bDone = True
                    lstAllChallenge = dSingleChallenge[tKey]
                    break
                if tKey in dChallenge and dChallenge[tKey] is not None:
                    bDone = True
                    lstAllChallenge = dChallenge[tKey]
                    break
            
            if bDone:
                break
        
        return lstAllChallenge

    
    def IsChallengeModeLimit(self, dLayerData):
        oWarMgr = self.m_Game.m_WarMgr
        iWarRound = oWarMgr.m_Round
        iWarCycle = oWarMgr.m_Cycle
        dLimit = dLayerData['BossInfo']['ChallengeModeLimit']
        for tKey in dLimit:
            (iRound, iCycle, iModeType) = tKey
            if iModeType not in oWarMgr.m_ModeType:
                continue
            if not iRound < iWarRound:
                if iRound == iWarRound and iCycle <= iWarCycle:
                    return 1
        
        return 0

    
    def GetLevelInfo(self, dInfo):
        dLayerData = self.m_LevelCtrl.m_LevelCtrlConf[dInfo['Layer']]
        if dInfo['LevelType'] == LEVEL_TYPE_BOSS:
            dLevelInfo = dLayerData['BossInfo']
        else:
            dLevelInfo = dLayerData['CtrlInfo'].get(dInfo['Level'], { })
        return dLevelInfo

    
    def GetRoundInfo(self):
        return (self.m_Game.m_WarMgr.m_Round, self.m_Game.m_WarMgr.m_Cycle)

    
    def GetLevelRoomTotal(self, iLevelID):
        oLevelNode = self.m_LevelCtrl.GetLevelNode(iLevelID)
        roomList = oLevelNode.m_RoomList
        iAllRoom = len(roomList)
        return iAllRoom

    
    def GetLevelExcludeArea(self, dInfo):
        dLevelInfo = self.GetLevelInfo(dInfo)
        if not dLevelInfo:
            return { }
        (iWarRound, iWarCycle) = self.GetRoundInfo()
        dExcludeChallengeArea = dLevelInfo['ExcludeChallengeArea']
        for iRound in range(iWarRound, -1, -1):
            for iCycle in range(iWarCycle, -1, -1):
                tKey = (iRound, iCycle)
                if tKey in dExcludeChallengeArea:
                    return dExcludeChallengeArea[tKey]
            
        
        return { }

    
    def CreateRoom2Challenge(self, lstAllChallenge, dInfo):
        iAllRoom = self.GetLevelRoomTotal(dInfo['LevelID'])
        dRoom2Challenge = { []: k for k in range(iAllRoom) }
        dRoom2ChallengeType = { }
        levelExcludeAreaList = self.GetLevelExcludeArea(dInfo)
        for iChallenge in lstAllChallenge:
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallenge)
            if not clsChallengeData:
                continue
            oWarMgr = self.m_Game.m_WarMgr
            if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and clsChallengeData.m_Type == CHALLENGE_EXTRAELITE:
                continue
            for iRoomPos in range(iAllRoom):
                if self.ValidAddChallenge(dInfo['LevelID'], iRoomPos, levelExcludeAreaList, clsChallengeData):
                    dRoom2Challenge[iRoomPos].append(iChallenge)
                    dRoom2ChallengeType[iChallenge] = clsChallengeData.m_Type
            
        
        return (dRoom2Challenge, dRoom2ChallengeType)

    
    def ValidAddChallenge(self, iLevelID, iRoomPos, levelExcludeAreaList, clsChallengeData):
        oLevelNode = self.m_LevelCtrl.GetLevelNode(iLevelID)
        iMap = oLevelNode.m_Map
        roomList = oLevelNode.m_RoomList
        iAllRoom = len(roomList)
        if iRoomPos == iAllRoom - 1 and clsChallengeData.ExcludeLastRoom():
            iResult = 0
        else:
            iResult = 1
            for oLine in roomList[iRoomPos]:
                tArea = (iMap, oLine.m_Area)
                if not tArea in levelExcludeAreaList:
                    if tArea in clsChallengeData.m_ExcludeArea:
                        iResult = 0
                        break
            
        return iResult

    
    def ChooseChallenge(self, iCnt, dAllChallenge, dInfo):
        iLevelID = dInfo['LevelID']
        dSeasonIgnore = dInfo.get('SeasonIgnore', { })
        iSeasonIgnore = dSeasonIgnore[iLevelID] if iLevelID in dSeasonIgnore else None
        iAllRoom = self.GetLevelRoomTotal(iLevelID)
        lstAllChallengeID = []
        for iChallenge, iWeight in dAllChallenge.items():
            lstAllChallengeID.append(iChallenge)
        
        (dRoom2Challenge, dRoom2ChallengeType) = self.CreateRoom2Challenge(lstAllChallengeID, dInfo)
        dWeight = { }
        dChooseChallenge = { }
        lstIgnoreRoom = []
        if iLevelID in self.m_IgnoreRoom:
            lstIgnoreRoom = self.m_IgnoreRoom[iLevelID]
        for iRoomPos in range(iAllRoom):
            if iRoomPos == iSeasonIgnore:
                continue
            if iRoomPos in lstIgnoreRoom:
                continue
            if dRoom2Challenge[iRoomPos]:
                dWeight[iRoomPos] = 1
        
        if not dWeight:
            return dChooseChallenge
        iCnt = min(iCnt, len(dWeight))
        lstRoomPos = ChooseMulKeys(self.m_Game, dWeight, iCnt)
        bHasEliteIntrude = False
        oWarMgr = self.m_Game.m_WarMgr
        dDebugChallengeHero = oWarMgr.Query('DebugChallengeHero', { })
        sPrintChallenge = ''
        for i in lstRoomPos:
            dChallengeWeight = { }
            dNewChallengeWeight = { }
            for iRoomChallenge, iWeight in dAllChallenge.items():
                if (iRoomChallenge in dRoom2Challenge[i] or bHasEliteIntrude) and dRoom2ChallengeType[iRoomChallenge] in ELITEINTRUDE_CHALLENGE:
                    continue
                dChallengeWeight[iRoomChallenge] = iWeight
                if iRoomChallenge not in self.m_LastLevelChooseChallenge:
                    dNewChallengeWeight[iRoomChallenge] = iWeight
            
            if len(dNewChallengeWeight) > 0:
                dChallengeWeight = dNewChallengeWeight
            iChallenge = ChooseKey(self.m_Game, dChallengeWeight)
            if dDebugChallengeHero:
                if not sPrintChallenge:
                    sPrintChallenge = '主线关房间挑战抽取:'
                sPrintChallenge += '\n%d %d %d %s' % (iLevelID, i, iChallenge, dChallengeWeight)
            if not iChallenge:
                continue
            dChooseChallenge[(dInfo['LevelID'], i)] = iChallenge
            if dRoom2ChallengeType[iChallenge] in ELITEINTRUDE_CHALLENGE:
                bHasEliteIntrude = True
            for iPos in lstRoomPos:
                if iChallenge in dRoom2Challenge[iPos]:
                    dRoom2Challenge[iPos].remove(iChallenge)
                    if not dRoom2Challenge[iPos]:
                        (dNewRoom2Challenge, dRoom2ChallengeType) = self.CreateRoom2Challenge(lstAllChallengeID, dInfo)
                        dRoom2Challenge[iPos] = dNewRoom2Challenge[iPos]
                        if len(dRoom2Challenge[iPos]) > 1:
                            dRoom2Challenge[iPos].remove(iChallenge)
            
        
        if sPrintChallenge:
            oWarMgr.DebugMessage(dDebugChallengeHero, sPrintChallenge)
        return dChooseChallenge


