# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/round/extrule.pyc
# RelativePath: clientlogic/cl_warmgr/round/extrule.pyc
# Source Generated with Decompyle++
# File: extrule.pyc (Python 3.6)

from cl_only import SendAlert, ChooseKey, WeakProxy, PY_FLAG_DEAD
from cl_commondefines import ROUND_EXTRULE_REPLACEMONSTER, ROUND_EXTRULE_APPEARCHALLENGE, MODE_SNOWMOUNTAINS, ROUND_EXTRULE_REPLACECONFIG_CHALLENGE, LEVEL_TYPE_FIGHT, ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE, LEVEL_TYPE_HIDE, SPAWN_ADDROOMCHALLENGE, ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM, ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER, SIDE_TYPE_MONSTER, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH
from cl_object.logging import WarobjLog
from cl_resmgr.aitempparam import GetAIConfParam
import cl_msgcenter
import cl_math

class CBaseRoundExtRule(object):
    m_Type = 0
    m_ExtRuleName = ''
    
    def __init__(self, oRoundElement, oGame):
        self.m_RoundElement = oRoundElement
        self.m_Game = oGame
        self.m_Key = '%s-%s' % (self.m_Type, self.__class__.__name__[1:])

    
    def Init(self, dParam):
        pass

    
    def Release(self):
        self.m_RoundElement = None
        self.m_Game = None



class CReplaceMonster(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_REPLACEMONSTER
    m_ExtRuleName = '替换怪物'
    
    def Init(self, dParam):
        self.m_ReplaceDict = dParam
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.OnCreateMonsterPre, self.m_Key)

    
    def Release(self):
        cl_msgcenter.DoneAttention(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_Key)
        super(CReplaceMonster, self).Release()

    
    def OnCreateMonsterPre(self, oListener, oWarMgr, dMsgInfo):
        oWarData = self.m_Game.m_WarData
        iOldMonsterSID = dMsgInfo['MonsterSID']
        if iOldMonsterSID not in self.m_ReplaceDict:
            return None
        iNewMonsterSID = self.m_ReplaceDict[iOldMonsterSID]
        clsNewMonsterData = oWarData.GetMonsterData(iNewMonsterSID)
        if not clsNewMonsterData:
            iWarNo = self.m_Game.GetWarMgr().m_SID
            SendAlert('err', '战场%d 未配置怪物SID%d' % (iWarNo, iNewMonsterSID))
            return None
        dMsgInfo['MonsterSID'] = iNewMonsterSID



class CAppearChallenge(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_APPEARCHALLENGE
    m_ExtRuleName = '必刷挑战事件'
    
    def Init(self, dParam):
        self.m_ReplaceDict = dParam
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.AppearChallenge, self.m_Key)

    
    def Release(self):
        cl_msgcenter.DoneAttention(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECHALLENGE, self.m_Key)
        super(CAppearChallenge, self).Release()

    
    def AppearChallenge(self, oRoundElement, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType != LEVEL_TYPE_FIGHT:
            return None
        iLayerNum = dMsgInfo['Layer']
        sGameMode = 'Default'
        if oWarMgr.IsEndless():
            sGameMode = oWarMgr.GetEndlessMode()
            iLayerNum = oWarMgr.GetBaseLayer(iLayerNum)
        iLevelNum = dMsgInfo['Level']
        if iLayerNum < 2 and iLevelNum < 4:
            return None
        if sGameMode not in self.m_ReplaceDict:
            return None
        dRoomChallenge = self.m_ReplaceDict[sGameMode]
        if iLayerNum not in dRoomChallenge:
            return None
        iRoomChallengeSID = dRoomChallenge[iLayerNum]
        clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iRoomChallengeSID)
        if not clsChallengeData:
            SendAlert('err', '战场%d 房间挑战%d 配置错误' % (oWarMgr.m_SID, iRoomChallengeSID))
            return None
        dChooseChallenge = dMsgInfo['ChooseChallenge']
        dRoomPos = dict.fromkeys([ iRoom for _, iRoom in dChooseChallenge ], 1)
        lstExtArea = clsChallengeData.m_ExcludeArea
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelID = dMsgInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        if not oLevelNode:
            return None
        iMap = oLevelNode.m_Map
        roomList = oLevelNode.m_RoomList
        dExtRoomPos = { }
        dUnExtRoomPos = { }
        for iRoomPos, lstLine in enumerate(roomList):
            for oLine in lstLine:
                if (iMap, oLine.m_Area) in lstExtArea:
                    dExtRoomPos[iRoomPos] = 1
                    break
            
            if iRoomPos not in dExtRoomPos:
                dUnExtRoomPos[iRoomPos] = 1
        
        for iRoomPos in dExtRoomPos:
            dRoomPos.pop(iRoomPos, 0)
        
        iIgnoreAppearPos = dMsgInfo.get('IgnoreAppearPos', None)
        if iIgnoreAppearPos is not None:
            dRoomPos.pop(iIgnoreAppearPos, 0)
            if len(dUnExtRoomPos) > 1:
                dUnExtRoomPos.pop(iIgnoreAppearPos, 0)
        iMaxLevel = oLevelCtrl.GetFightMaxLevel()
        if (MODE_SNOWMOUNTAINS in oWarMgr.m_ModeType or oWarMgr.Query('BenedictionChallenge')) and iLevelNum == iMaxLevel:
            iRoomLastPos = len(roomList) - 1
            dRoomPos.pop(iRoomLastPos, 0)
            dUnExtRoomPos.pop(iRoomLastPos, 0)
        if dRoomPos:
            tKey = (iLevelID, ChooseKey(self.m_Game, dRoomPos))
            dChooseChallenge[tKey] = iRoomChallengeSID
            return None
        if dUnExtRoomPos:
            tKey = (iLevelID, ChooseKey(self.m_Game, dUnExtRoomPos))
            dChooseChallenge[tKey] = iRoomChallengeSID



class CReplaceConfigChallenge(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_REPLACECONFIG_CHALLENGE
    m_ExtRuleName = '替换配置挑战事件'
    
    def Init(self, dParam):
        self.m_ReplaceDict = dParam
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_REPLACECHALLENGE_PRE, self.ReplaceConfig, self.m_Key)

    
    def Release(self):
        cl_msgcenter.DoneAttention(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_LEVEL_REPLACECHALLENGE_PRE, self.m_Key)
        super(CReplaceConfigChallenge, self).Release()

    
    def ReplaceConfig(self, oRoundElement, oWarMgr, dMsgInfo):
        dChallengeInfo = dMsgInfo['ChallengeInfo']
        iLayerNum = dMsgInfo['Layer']
        if not dChallengeInfo or iLayerNum not in dChallengeInfo:
            return None
        if iLayerNum not in self.m_ReplaceDict:
            return None
        dRoomChallenge = self.m_ReplaceDict[iLayerNum]
        dReplaceRoomChallenge = { }
        for iRoomChallengeSID in dRoomChallenge:
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iRoomChallengeSID)
            if not clsChallengeData:
                SendAlert('err', '战场%d 房间挑战%d 配置错误' % (oWarMgr.m_SID, iRoomChallengeSID))
                continue
            dReplaceRoomChallenge[iRoomChallengeSID] = 1
        
        if dReplaceRoomChallenge:
            dChallengeInfo[iLayerNum] = dReplaceRoomChallenge



class CHideLevelAppearChallenge(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE
    m_ExtRuleName = '隐藏关必刷挑战事件'
    
    def Init(self, dParam):
        self.m_ReplaceDict = dParam
        self.m_LimitChallengeType = dParam.get('LimitChallengeType', [])
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.AppearChallenge, self.m_Key, -1, 0)

    
    def Release(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.m_Key)
        super(CHideLevelAppearChallenge, self).Release()

    
    def AppearChallenge(self, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType != LEVEL_TYPE_HIDE:
            return None
        if not self.CheckHideLevelRoomChallenge(oLevelNode):
            return None
        oChallengeMgr = oLevelNode.m_CtrlMgr.m_RoomChallenge
        dChallengeInfo = {
            'LevelType': oLevelNode.m_LevelType,
            'LevelID': oLevelNode.m_Level,
            'Layer': oLevelNode.m_CtrlMgr.m_LayerNum,
            'Level': oLevelNode.m_CtrlMgr.m_LevelNum }
        dAllChallenge = oChallengeMgr.GetAllChallenge(dChallengeInfo, True)
        if not dAllChallenge:
            return None
        dChooseChallenge = { }
        levelExcludeAreaList = oChallengeMgr.GetLevelExcludeArea(dChallengeInfo)
        for iChallenge, iWeight in dAllChallenge.items():
            clsChallengeData = self.m_Game.m_WarData.GetChallengeData(iChallenge)
            if clsChallengeData.m_Type in self.m_LimitChallengeType:
                continue
            if not oChallengeMgr.ValidAddChallenge(dChallengeInfo['LevelID'], 0, levelExcludeAreaList, clsChallengeData):
                continue
            dChooseChallenge[iChallenge] = iWeight
        
        if not dChooseChallenge:
            return None
        iChallengeSID = ChooseKey(self.m_Game, dChooseChallenge)
        oWarMgr = self.m_Game.m_WarMgr
        dDebugChallengeHero = oWarMgr.Query('DebugChallengeHero', { })
        if dDebugChallengeHero:
            sPrintChallenge = '隐藏关必刷挑战抽取: %d %d %s' % (iLevel, iChallengeSID, dChooseChallenge)
            oWarMgr.DebugMessage(dDebugChallengeHero, sPrintChallenge)
        oChallengeMgr.AddChallenge(iLevel, dInfo['Room'], iChallengeSID, sReason = 'HideLevelAppear')

    
    def CheckHideLevelRoomChallenge(self, oLevelNode):
        lstRoom = oLevelNode.m_RoomList
        iRound = self.m_Game.m_WarMgr.m_Round
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        oLevelLine = lstRoom[0][0]
        lstSpawnRule = oLevelConfData.GetLineSpawnRule(oLevelNode.m_Level, oLevelLine.m_Name, iRound)
        for dSpawn in lstSpawnRule:
            tAction = dSpawn['Action']
            for dRule in tAction:
                if dRule['func'] == SPAWN_ADDROOMCHALLENGE:
                    return 0
            
        
        return 1



class CSmashObstacleCreateMonsterLockRoom(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM
    m_ExtRuleName = '击碎阻挡刷怪锁房间'
    
    def Init(self, dParam):
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        self.m_LevelCtrl = WeakProxy(oLevelCtrl)
        self.m_CreatedMonster = { }
        self.m_ObstacleRecord = { }
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_SMASHOBSTACLE_CREATEMONSTER, self.OnSmashObstacleCreateMonster, self.m_Key)

    
    def Release(self):
        cl_msgcenter.DoneAttention(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_SMASHOBSTACLE_CREATEMONSTER, self.m_Key)
        cl_msgcenter.DoneAttention(self.m_RoundElement, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_Key)
        super(CSmashObstacleCreateMonsterLockRoom, self).Release()

    
    def OnSmashObstacleCreateMonster(self, oListener, oWarMgr, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            WarobjLog.Alert('no lineidx %s %s' % (self.m_Key, dMsgInfo))
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        oLevelNode = self.m_LevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode or oLevelNode.m_LevelType == LEVEL_TYPE_HIDE or iRoomPos != oLevelNode.m_CurRoomPos or oLevelNode.CheckLevelPass():
            return None
        iOwnerObstacle = dMsgInfo['OwnerObstacle']
        self.m_ObstacleRecord[iOwnerObstacle] = dMsgInfo['MonsterNum']
        sKey = '%s-%s' % (self.m_Key, iOwnerObstacle)
        oLevelNode.LockRoom(iRoomPos, sKey)
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_Key)

    
    def OnCreateMonster(self, oListener, oWarMgr, dMsgInfo):
        if 'SmashObstacleSummon' not in dMsgInfo:
            return None
        iOwnerObstacle = dMsgInfo['OwnerObstacle']
        if iOwnerObstacle not in self.m_ObstacleRecord:
            return None
        self.SubObstacleRecord(oWarMgr, iOwnerObstacle)
        iMonster = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            self.TryUnlockRoom(dMsgInfo['LineIdx'], iOwnerObstacle)
            return None
        self.m_CreatedMonster[iMonster] = iOwnerObstacle
        cl_msgcenter.AddAttentionFunc(self.m_RoundElement, iMonster, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_Key)

    
    def OnMonsterDie(self, oListener, oMonster, dMsgInfo):
        iMonster = oMonster.m_ID
        if iMonster not in self.m_CreatedMonster:
            return None
        iOwnerObstacle = self.m_CreatedMonster.pop(iMonster, 0)
        cl_msgcenter.DoneAttention(self.m_RoundElement, iMonster, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.TryUnlockRoom(oMonster.m_LineIdx, iOwnerObstacle)

    
    def SubObstacleRecord(self, oWarMgr, iOwnerObstacle):
        self.m_ObstacleRecord[iOwnerObstacle] -= 1
        if self.m_ObstacleRecord[iOwnerObstacle] <= 0:
            self.m_ObstacleRecord.pop(iOwnerObstacle, 0)
            if len(self.m_ObstacleRecord) == 0:
                cl_msgcenter.DoneAttention(self.m_RoundElement, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_Key)

    
    def TryUnlockRoom(self, tLineIdx, iOwnerObstacle):
        if iOwnerObstacle in self.m_ObstacleRecord:
            return None
        if iOwnerObstacle in self.m_CreatedMonster.values():
            return None
        self.UnlockRoom(tLineIdx, iOwnerObstacle)

    
    def UnlockRoom(self, tLineIdx, iOwnerObstacle):
        (iLevel, iRoomPos, _) = tLineIdx
        oLevelNode = self.m_LevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return None
        sKey = '%s-%s' % (self.m_Key, iOwnerObstacle)
        oLevelNode.UnlockRoom(iRoomPos, sKey)



class CRondomTransObstacleToMonster(CBaseRoundExtRule):
    m_Type = ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER
    m_ExtRuleName = '初始动态阻挡概率转为怪物'
    
    def Init(self, dParam):
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        self.m_LevelCtrl = WeakProxy(oLevelCtrl)
        self.m_TransferInfo = { }
        for iBuildSID, dTransInfo in dParam.items():
            iTransRatio = dTransInfo['TransRatio']
            iMonsterSID = dTransInfo['MonsterSID']
            self.m_TransferInfo[iBuildSID] = (iTransRatio, iMonsterSID)
        
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_BEFORE_CREATEINITOBSTACLE, self.OnBeforeCreateInitObstale, self.m_Key, -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_LevelCtrl, cl_msgcenter.MSG_LEVEL_BEFORE_CREATEINITOBSTACLE, self.m_Key)
        super().Release()

    
    def OnBeforeCreateInitObstale(self, oLevelCtrl, dMsgInfo):
        iObstacleSID = dMsgInfo.get('SID', 0)
        if iObstacleSID not in self.m_TransferInfo:
            return None
        (iTransferRatio, iMonsterSID) = self.m_TransferInfo[iObstacleSID]
        if self.m_Game.Random(100) > iTransferRatio:
            return None
        if 'Origin' not in dMsgInfo or 'Angle' not in dMsgInfo:
            return None
        tPos = dMsgInfo['Origin']
        iScene = dMsgInfo['Scene']
        tLine = dMsgInfo['Line']
        tAngle = dMsgInfo['Angle']
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        oGame = self.m_Game
        (iRet, tMonsterPos) = oGame.Scene_GetSpace(iScene, tPos)
        if not iRet:
            return None
        tFacing = cl_math.RotateAroundVector((0, 0, 1), (0, 1, 0), tAngle[1])
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tMonsterPos, tFacing, SIDE_TYPE_MONSTER, dAI = dAI, tLineIdx = tLine)
        if oMonster:
            WarobjLog.Debug('%d transobstacletomonster %s %d %d %s %s' % (self.m_Game.m_ID, self.m_Key, iObstacleSID, iMonsterSID, tMonsterPos, tLine))
            dMsgInfo['Halt'] = 1
            oMonster.Set('TransObstacleToMonster', 1)


