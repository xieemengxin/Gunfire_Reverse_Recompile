# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/device/devicechallengemgr.pyc
# RelativePath: clientlogic/cl_warmgr/device/devicechallengemgr.pyc
# Source Generated with Decompyle++
# File: devicechallengemgr.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_FIGHT, MODEL_TYPE_CAPSULE, MODE_SNOWMOUNTAINS, NWARRIOR_DROP_DEVICECOMP, VIRTUAL_ITEM_DROP, SETTLE_DIRECTLEAVE, SETTLE_LOSEWAR, SETTLE_FINISHWAR
from cl_only import GetRandomCard, SendAlert, Frame2Time, CopyList
from cl_object.logging import SeasonLog
import cl_reward
import cl_msgcenter
import cl_modeldefine
CHALLENGE_RESULT_UNACTIVATE = 0
CHALLENGE_RESULT_SUCCESS = 1
CHALLENGE_RESULT_FAIL = 2
CHALLENGE_RESULT_QUIT = 3

class CDeviceChallenge(object):
    
    def __init__(self, oMgr, iLevel, iRoomPos):
        self.m_Key = 'DeviceChallenge_%s_%s' % (iLevel, iRoomPos)
        self.m_Mgr = oMgr
        self.m_Game = oMgr.m_Game
        self.m_Level = iLevel
        self.m_RoomPos = iRoomPos
        self.m_SummonStelaSet = set()
        self.m_CreateMonsterSet = set()
        self.m_CreatingCount = 0
        self.m_RewardConfig = oMgr.m_ChallengeReward
        self.m_StartFrame = 0
        self.m_BigDataCollectDict = {
            'TotalHP': 0,
            'CostHP': [
                0,
                0,
                0,
                0] }

    
    def ChallengeStart(self):
        SeasonLog.Info('%s devicechallenge start %s' % (self.m_Game.m_ID, self.m_Key))
        iWarMgrID = self.m_Game.m_WarMgr.m_ID
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_SUMMONSTELE_TRIGGER, self.OnSummonSteleActivated, self.m_Key)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.OnCreateMonster, self.m_Key)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.OnPlayerSettle, self.m_Key)
        self.CreateSummonStela()

    
    def ChallengeEnd(self):
        SeasonLog.Info('%s devicechallenge over %s' % (self.m_Game.m_ID, self.m_Key))
        iRoomPos = self.m_RoomPos
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(self.m_Level)
        oLevelNode.UnlockRoom(iRoomPos, self.m_Key)
        self.Release()

    
    def OnDie(self, oWarMgr, oVictim, dMsgInfo):
        if not oVictim.m_LineIdx:
            return None
        (iLevel, iRoomPos, _) = oVictim.m_LineIdx
        if iLevel != self.m_Level or iRoomPos != self.m_RoomPos:
            return None
        CreateMonsterSet = self.m_CreateMonsterSet
        iVictimID = oVictim.m_ID
        if iVictimID not in CreateMonsterSet:
            return None
        SummonStelaSet = self.m_SummonStelaSet
        if iVictimID in SummonStelaSet:
            lstCostHP = self.m_BigDataCollectDict['CostHP']
            for iIndex, iValue in enumerate(oVictim.m_DamageCollectList):
                lstCostHP[iIndex] += iValue
            
            SummonStelaSet.remove(iVictimID)
            self.OnReward(oVictim)
            if not SummonStelaSet:
                self.OnFinish(oVictim)
        CreateMonsterSet.remove(iVictimID)
        if not CreateMonsterSet and self.m_CreatingCount == 0:
            self.ChallengeEnd()

    
    def OnSummonSteleActivated(self, oWarMgr, oSummonStele, dMsgInfo):
        if oSummonStele.m_ID not in self.m_SummonStelaSet:
            return None
        if self.m_StartFrame:
            return None
        self.m_StartFrame = self.m_Game.GetFrameNum()

    
    def OnCreateMonster(self, oWarMgr, oMonster, dInfo):
        if 'SummonStela' not in dInfo:
            return None
        (iLevel, iRoomPos, _) = oMonster.m_LineIdx
        if iLevel != self.m_Level or iRoomPos != self.m_RoomPos:
            return None
        self.m_CreateMonsterSet.add(oMonster.m_ID)

    
    def OnPlayerSettle(self, oWarMgr, oHero, dInfo):
        iSettleType = dInfo['SettleType']
        oGame = self.m_Game
        if iSettleType == SETTLE_DIRECTLEAVE and len(oWarMgr.GetRoomPlayer()) == 1:
            if self.IsSummonStelaUnactivate():
                self.SendBigData(oGame, CHALLENGE_RESULT_UNACTIVATE)
                return None
            self.SendBigData(oGame, CHALLENGE_RESULT_QUIT)
        elif iSettleType in (SETTLE_LOSEWAR, SETTLE_FINISHWAR) and oHero.m_PlayerID == self.GetSendPlayer(oWarMgr):
            if self.IsSummonStelaUnactivate():
                self.SendBigData(oGame, CHALLENGE_RESULT_UNACTIVATE)
                return None
            self.SendBigData(oGame, CHALLENGE_RESULT_FAIL)

    
    def IsSummonStelaUnactivate(self):
        oGame = self.m_Game
        for iSummonStela in self.m_SummonStelaSet:
            oSummonStela = oGame.GetObject(iSummonStela)
            if not oSummonStela:
                continue
            if not oSummonStela.m_bActivated:
                return True
        
        return False

    
    def CreateSummonStela(self):
        iSummonStelaSID = self.m_Mgr.m_SummonStelaSID
        clsSummonData = self.m_Game.m_WarData.GetBuildData(iSummonStelaSID)
        iLevel = self.m_Level
        if not clsSummonData:
            SendAlert('err', '赛季挑战战场%d未配置建筑 %d, 关卡%d' % (self.m_Game.m_WarMgr.m_SID, iSummonStelaSID, iLevel))
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelConfData = oLevelCtrl.m_LevelConfData
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iRoomPos = self.m_RoomPos
        (tPos, dEliteDrop) = oLevelNode.GetEliteInfo(iRoomPos, oLevelConfData)
        if not tPos:
            SendAlert('err', 'game:%d : 关卡%d，房间%d未配置精英点位' % (self.m_Game.m_ID, iLevel, iRoomPos))
            return None
        tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Physx')
        iScene = oLevelNode.m_Scene
        dInfo = {
            'Angle': [
                0,
                0,
                0],
            'Center': [
                0,
                tModelData[1] * 0.5,
                0],
            'Origin': tPos,
            'SID': iSummonStelaSID,
            'Scale': [
                1,
                1,
                1],
            'Shape': MODEL_TYPE_CAPSULE,
            'Size': (tModelData[1], tModelData[0], 0) }
        tLineIdx = (iLevel, iRoomPos, 0)
        oBuild = self.m_Game.m_ResMgr.CreateBuild(iScene, iSummonStelaSID, dInfo, tLineIdx)
        if not oBuild:
            SendAlert('err', 'game:%d : 赛季挑战创建%d建筑失败' % (self.m_Game.m_ID, iSummonStelaSID))
            return None
        if dEliteDrop:
            oBuild.Set('FixDropPos', dEliteDrop['FixDropPos'])
            oBuild.Set('CheckDropInfo', dEliteDrop['CheckDropInfo'])
        self.m_SummonStelaSet.add(oBuild.m_ID)
        self.m_CreateMonsterSet.add(oBuild.m_ID)
        oLevelNode.LockRoom(iRoomPos, self.m_Key)
        self.m_BigDataCollectDict['TotalHP'] += oBuild.QueryAttr('HPMax')

    
    def OnFinish(self, oVictim):
        SeasonLog.Info('%s devicechallenge finish %s %s %s' % (self.m_Game.m_ID, self.m_Key, self.m_CreateMonsterSet, self.m_CreatingCount))
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.m_Key)
        oGame = oVictim.m_Game
        self.SendBigData(oGame, CHALLENGE_RESULT_SUCCESS)

    
    def OnReward(self, oBuild):
        oGame = oBuild.m_Game
        vPos = oBuild.GetPos()
        dRewardConfig = self.m_RewardConfig
        lstHero = oGame.m_WarMgr.GetRoomHero(iCalAI = 0)
        iBuild = oBuild.m_ID
        oDeviceElement = oGame.m_WarMgr.GetComponent('DeviceElement')
        dCompRewardConfig = oDeviceElement.GetRewardInfoByType('DeviceChallenge')
        dMGInfo = { }
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dExtInfo = {
                'Player': oHero.m_ID }
            lstReward = []
            for iSID in oHero.m_DevicePerformCon.ChooseComponent(dCompRewardConfig):
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_DEVICECOMP,
                        'DropInfo': [
                            iSID],
                        'DropPos': vPos } }
                lstReward.append(dReward)
            
            lstEnergyPointReward = oDeviceElement.GetDeviceEnergyPointReward(dRewardConfig['EnergyPoint'], vPos)
            if lstEnergyPointReward:
                lstReward.extend(lstEnergyPointReward)
            dMGInfo[iHero] = {
                0: [
                    0,
                    lstReward,
                    dExtInfo] }
        
        cl_reward.CreateDemon(oGame, iBuild, dMGInfo)

    
    def Release(self):
        iWarMgrID = self.m_Game.m_WarMgr.m_ID
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_SUMMONSTELE_TRIGGER, self.m_Key)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.m_Key)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.m_Key)
        self.m_Mgr.ChallengeRelease(self.m_Level, self.m_RoomPos)
        self.m_Mgr = None
        self.m_Game = None

    
    def GetSendPlayer(self, oWarMgr):
        lstRoomPlayer = oWarMgr.GetRoomPlayer()
        if not lstRoomPlayer:
            return 0
        iLeaderPlayer = oWarMgr.GetLeaderPlayer()
        if iLeaderPlayer in lstRoomPlayer:
            return iLeaderPlayer
        return lstRoomPlayer[0]

    
    def SendBigData(self, oGame, iResult):
        oWarMgr = oGame.m_WarMgr
        iSendPlayer = self.GetSendPlayer(oWarMgr)
        if not iSendPlayer:
            return None
        dInfo = {
            'LevelID': self.m_Level,
            'Result': iResult,
            'Duration': Frame2Time(oGame.GetFrameNum() - self.m_StartFrame) if self.m_StartFrame else 0,
            'TotalHP': self.m_BigDataCollectDict['TotalHP'] // 100 }
        lstCostHP = CopyList(self.m_BigDataCollectDict['CostHP'])
        for iSummonStela in self.m_SummonStelaSet:
            oSummonStela = oGame.GetObject(iSummonStela)
            if not oSummonStela:
                continue
            for iIndex, iValue in enumerate(oSummonStela.m_DamageCollectList):
                lstCostHP[iIndex] += iValue
            
        
        for iIndex, iValue in enumerate(lstCostHP):
            lstCostHP[iIndex] = iValue // 100
        
        dInfo['CostHP'] = lstCostHP
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        dInfo['LayerNum'] = oLevelCtrl.m_LayerNum
        oDeviceElement = oWarMgr.GetComponent('DeviceElement')
        dInfo['DeviceList'] = list(oDeviceElement.m_PlayerChooseInfo.values())
        oWarMgr.SendDeviceChallengeBigData(iSendPlayer, dInfo)



class CDeviceChallengeMgr(object):
    
    def __init__(self, oDeviceElement, oData):
        self.m_Key = 'DeviceChallengeMgr'
        self.m_Game = oDeviceElement.m_Game
        self.m_SummonStelaSID = oData.m_Config.get('SummonStela', 0)
        self.m_MaxLayerCount = oData.m_Config.get('MaxLayerCount', 2)
        self.m_MaxLevelCount = oData.m_Config.get('MaxLevelCount', 1)
        self.m_ExcludeLevelDict = oData.m_Config.get('ExcludeLevel', { })
        self.m_ChallengeReward = oData.m_Config.get('DeviceChallengeReward', { })
        self.m_ChanllengeDict = { }
        self.m_ChallengeLevelDict = { }
        self.m_LastLayerNum = 0

    
    def Init(self):
        iWarMgrID = self.m_Game.m_WarMgr.m_ID
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, self.m_Key)
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelInit, self.m_Key, -1, 0)
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, self.m_Key, -1, 0)

    
    def ValidLevelType(self, iLevelType):
        if iLevelType != LEVEL_TYPE_FIGHT:
            return False
        return True

    
    def OnLevelInit(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if not self.ValidLevelType(iLevelType):
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iLayerNum = oLevelCtrl.m_LayerNum
        if iLayerNum != self.m_LastLayerNum:
            self.m_LastLayerNum = iLayerNum
            self.GenerateLevel(iLayerNum)
        iLevelNum = dInfo['Level']
        if iLevelNum not in self.m_ChallengeLevelDict:
            return None
        iLevel = dInfo['LevelID']
        self.GenerateRoomPos(iLevelNum, iLevel)

    
    def OnLevelFinish(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        if iLevel in self.m_ChanllengeDict:
            for iRoomPos in list(self.m_ChanllengeDict[iLevel].keys()):
                oChallenge = self.m_ChanllengeDict[iLevel][iRoomPos]
                if oChallenge:
                    oChallenge.Release()
            

    
    def OnRoomStart(self, oWarMgr, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        if iLevel not in self.m_ChanllengeDict:
            return None
        iRoomPos = dInfo['Room']
        if iRoomPos in self.m_ChanllengeDict[iLevel]:
            oChallenge = CDeviceChallenge(self, iLevel, iRoomPos)
            self.m_ChanllengeDict[iLevel][iRoomPos] = oChallenge
            oChallenge.ChallengeStart()

    
    def GetChallenge(self, iLevel, iRoomPos):
        if iLevel not in self.m_ChanllengeDict:
            return None
        if iRoomPos not in self.m_ChanllengeDict[iLevel]:
            return None
        return self.m_ChanllengeDict[iLevel][iRoomPos]

    
    def IncreaseCreatingCount(self, tLineIdx):
        (iLevel, iRoomPos, _) = tLineIdx
        oChallenge = self.GetChallenge(iLevel, iRoomPos)
        if not oChallenge:
            return None
        oChallenge.m_CreatingCount += 1

    
    def DecreaseCreatingCount(self, tLineIdx):
        (iLevel, iRoomPos, _) = tLineIdx
        oChallenge = self.GetChallenge(iLevel, iRoomPos)
        if not oChallenge:
            return None
        oChallenge.m_CreatingCount -= 1

    
    def GenerateLevel(self, iLayerNum):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        iMaxChooseLevelCount = oLevelCtrl.GetFightMaxLevel()
        lstChooseLevelNum = [ iLevelNum for iLevelNum in range(1, iMaxChooseLevelCount + 1) ]
        lstExcludeLevel = []
        if iLayerNum in self.m_ExcludeLevelDict:
            lstExcludeLevel = self.m_ExcludeLevelDict[iLayerNum]
        for iLevel in lstExcludeLevel:
            lstChooseLevelNum.remove(iLevel)
        
        if not lstChooseLevelNum:
            return None
        iMaxLevelCount = self.m_MaxLevelCount
        self.m_ChallengeLevelDict = { }
        for _ in range(self.m_MaxLayerCount):
            iLevelNum = lstChooseLevelNum[oGame.Random(len(lstChooseLevelNum))]
            self.m_ChallengeLevelDict.setdefault(iLevelNum, 0)
            self.m_ChallengeLevelDict[iLevelNum] += 1
            if self.m_ChallengeLevelDict[iLevelNum] >= iMaxLevelCount:
                lstChooseLevelNum.remove(iLevelNum)
                if not lstChooseLevelNum:
                    break
        
        SeasonLog.Debug('game:%d, layer:%d generate challenge level %s' % (self.m_Game.m_ID, oLevelCtrl.m_LayerNum, self.m_ChallengeLevelDict))

    
    def GenerateRoomPos(self, iLevelNum, iLevel):
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        bExcludeLastRoom = False
        iMaxLevel = oLevelCtrl.GetFightMaxLevel()
        if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and iLevelNum == iMaxLevel:
            bExcludeLastRoom = True
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if bExcludeLastRoom:
            iTempRoomCount = len(oLevelNode.m_RoomList[:-1])
        else:
            iTempRoomCount = len(oLevelNode.m_RoomList)
        lstEliteRoomPos = []
        oLevelConfData = oLevelCtrl.m_LevelConfData
        for iRoomPos in range(iTempRoomCount):
            (tPos, _) = oLevelNode.GetEliteInfo(iRoomPos, oLevelConfData)
            if tPos:
                lstEliteRoomPos.append(iRoomPos)
        
        iRoomCount = len(lstEliteRoomPos)
        if iRoomCount == 0:
            return None
        if iRoomCount == 1:
            iRoomPos = lstEliteRoomPos[0]
            self.m_ChanllengeDict[iLevel] = {
                iRoomPos: None }
        else:
            iCount = self.m_ChallengeLevelDict[iLevelNum]
            lstIndex = GetRandomCard(self.m_Game, min(iCount, iRoomCount), iRoomCount)
            self.m_ChanllengeDict[iLevel] = { }
            for iIndex in lstIndex:
                iRoomPos = lstEliteRoomPos[iIndex]
                self.m_ChanllengeDict[iLevel][iRoomPos] = None
            
        SeasonLog.Debug('game:%d, level:%d generate challenge pos %s' % (self.m_Game.m_ID, iLevel, list(self.m_ChanllengeDict[iLevel].keys())))

    
    def ChallengeRelease(self, iLevel, iRoomPos):
        if iLevel not in self.m_ChanllengeDict:
            return None
        dChallenge = self.m_ChanllengeDict[iLevel]
        if iRoomPos not in dChallenge:
            return None
        dChallenge.pop(iRoomPos)
        if not dChallenge:
            self.m_ChanllengeDict.pop(iLevel)

    
    def ReleaseAllChanllenge(self):
        for iLevel in list(self.m_ChanllengeDict.keys()):
            for iRoomPos in list(self.m_ChanllengeDict[iLevel].keys()):
                oChallenge = self.m_ChanllengeDict[iLevel][iRoomPos]
                if oChallenge:
                    oChallenge.Release()
            
        

    
    def Release(self):
        self.ReleaseAllChanllenge()
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.m_Key)
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_Key)
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Key)
        self.m_Game = None



def NewDeviceChallengeMgr(oDeviceElement, oData):
    oDeviceChallengeMgr = CDeviceChallengeMgr(oDeviceElement, oData)
    return oDeviceChallengeMgr

