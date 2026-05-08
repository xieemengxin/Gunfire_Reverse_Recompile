# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/linenewmonsterctrl.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/linenewmonsterctrl.pyc
# Source Generated with Decompyle++
# File: linenewmonsterctrl.pyc (Python 3.6)

from cl_commondefines import MONSTER_CLASSIFY_FOOT, MONSTER_CLASSIFY_BOXMONSTER, MONSTER_CLASSIFY_PETROCHEMICAL, MONSTER_CLASSIFY_BATTERY, MONSTER_CLASSIFY_DART, MONSTER_CLASSIFY_BOSS, MONSTER_CLASSIFY_FLY, MONSTER_CLASSIFY_MAGIC, MONSTER_CLASSIFY_SNIPE, MONSTER_CLASSIFY_HEVNEAR, MONSTER_CLASSIFY_HEVFAR, MONSTER_CLASSIFY_THROW, MONSTER_CLASSIFY_MEDFAR, MONSTER_CLASSIFY_MEDNEAR, MONSTER_CLASSIFY_SMAFAR, MONSTER_CLASSIFY_SMANEAR, MONSTER_CLASSIFY_BADGER, SIDE_TYPE_MONSTER, WARRIOR_ELITE, MONSTER_CLASSIFY_LARGESUMMON, MONSTER_CLASSIFY_RIDE, MONSTER_CLASSIFY_CANNONFODDER, MONSTER_CLASSIFY_PART, MONSTER_CLASSIFY_DURABILITY, MONSTER_CLASSIFY_TWOLAYER_BADGER, MONSTER_CLASSIFY_TWOLAYER_BATTERY, MONSTER_CLASSIFY_TWOLAYER_SMANEAR, MONSTER_CLASSIFY_TWOLAYER_HEVNEAR, MONSTER_CLASSIFY_TWOLAYER_MEDFAR, MONSTER_CLASSIFY_TWOLAYER_MEDNEAR, MONSTER_CLASSIFY_TWOLAYER_HEVFAR
from cl_commondefines import MONSTER_CLASSIFY_THREELAYER_SMAFAR, MONSTER_CLASSIFY_THREELAYER_MEDFAR, MONSTER_CLASSIFY_THREELAYER_HEVFAR, MONSTER_CLASSIFY_THREELAYER_MEDNEAR, MONSTER_CLASSIFY_THREELAYER_FOOT, MONSTER_CLASSIFY_THREELAYER_HEVNEAR, MONSTER_CLASSIFY_THREELAYER_MAGIC
from cl_commondefines import MONSTER_CLASSIFY_ONELAYER_FLY, MONSTER_CLASSIFY_ONELAYER_SMANEAR, MONSTER_CLASSIFY_ONELAYER_MEDNEAR
from cl_only import Functor, ShufferList, Time2Frame, ChooseKey, SendAlert
from cl_only import ChooseMulKeys, WeakProxy, GAME_FRAME_INF, RandomFloat2Int
from cl_resmgr import GetMonsterSID
import cl_msgcenter
import cl_formula
import cl_math
import cl_snetwar
import cl_notify

class CLineMonsterCtrl(object):
    
    def __init__(self, oLevelLine):
        self.m_LevelLine = WeakProxy(oLevelLine)
        self.m_Game = oLevelLine.m_Game
        self.m_Monster = { }
        self.m_GroupInfo = { }
        self.m_CallOutCnt = 0
        self.m_CallOutFlag = { }
        self.m_Notify = 0
        self.m_NotifyGroup = { }
        self.m_ExtAmount = -1
        self.m_MonsterSpawnDict = { }

    
    def SetExtAmount(self, tAmount):
        self.m_ExtAmount = tAmount

    
    def SetNotify(self, iNotify):
        self.m_Notify = iNotify

    
    def ClearPendSpawnMonster(self):
        for sFlag in self.m_CallOutFlag:
            self.m_Game.m_WarMgr.Remove_Call_Out(sFlag)
        
        tLineIdx = self.m_LevelLine.GetLineIdx()
        for iGroup, dGroupInfo in self.m_GroupInfo.items():
            if not dGroupInfo['Wait']:
                if dGroupInfo['Live']:
                    dGroupInfo['Wait'] = { }
                    dGroupInfo['Live'] = []
                    continue
        
        for iGroup in self.m_GroupInfo.keys():
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.m_Game.m_WarMgr, {
                'GroupID': iGroup,
                'LineIdx': tLineIdx,
                'VID': 0,
                'AID': 0 })
        

    
    def Release(self):
        for sFlag in self.m_CallOutFlag:
            self.m_Game.m_WarMgr.Remove_Call_Out(sFlag)
        
        self.m_CallOutFlag = { }
        self.m_Monster = { }
        self.m_GroupInfo = { }
        self.m_LevelLine = None
        self.m_Game = None

    
    def NewCallOutFlag(self):
        self.m_CallOutCnt += 1
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        sFlag = 'Spawn%s-%d-%d' % (self.m_LevelLine.m_Name, self.m_CallOutCnt, iScene)
        self.m_CallOutFlag[sFlag] = 1
        return sFlag

    
    def AddSpawnInfo(self, tSpawnInfo):
        (iGroupID, dSpawnArea, dAmount, _, iLimitExtAmount) = tSpawnInfo
        if not dAmount or not dSpawnArea:
            return None
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstSpawnArea = list(dSpawnArea.keys())
        dAreaMonsterSpawn = oLevelConfData.GetAreaMonsterSpawnInfo(oLevelNode.m_Level, self.m_LevelLine.m_Name, lstSpawnArea)
        lstMonsterInfo = self.ChooseMonsterInfo(dAreaMonsterSpawn, dSpawnArea, dAmount, iLimitExtAmount)
        self.PreprocessCreateMonster(iGroupID, dAreaMonsterSpawn, lstMonsterInfo)

    
    def AddSpawnInfoByChooseArea(self, tSpawnInfo):
        (iGroupID, dSpawnArea, iAreaChoose, dAmount, _, iLimitExtAmount) = tSpawnInfo
        if not dAmount or not dSpawnArea:
            return None
        lstArea = ChooseMulKeys(self.m_Game, dSpawnArea, iAreaChoose)
        dNewSpawnArea = { }
        for iArea in lstArea:
            dNewSpawnArea[iArea] = 100
        
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstSpawnArea = list(dNewSpawnArea.keys())
        dAreaMonsterSpawn = oLevelConfData.GetAreaMonsterSpawnInfo(oLevelNode.m_Level, self.m_LevelLine.m_Name, lstSpawnArea)
        lstMonsterInfo = self.ChooseMonsterInfo(dAreaMonsterSpawn, dNewSpawnArea, dAmount, iLimitExtAmount)
        self.PreprocessCreateMonster(iGroupID, dAreaMonsterSpawn, lstMonsterInfo)

    
    def AddSpawnInfoByChooseAreaAndNumber(self, tSpawnInfo):
        (iGroupID, dSpawnArea, iAreaChoose, dAmount, _, iLimitExtAmount) = tSpawnInfo
        if not dAmount or not dSpawnArea:
            return None
        lstArea = ChooseMulKeys(self.m_Game, dSpawnArea, iAreaChoose)
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstMonsterInfo = []
        dAreaMonsterSpawn = { }
        for iArea in lstArea:
            if iArea not in dAmount:
                continue
            dNewSpawnArea = { }
            dNewSpawnArea[iArea] = 100
            lstSpawnArea = list(dNewSpawnArea.keys())
            dAreaMonsterSpawn.update(oLevelConfData.GetAreaMonsterSpawnInfo(oLevelNode.m_Level, self.m_LevelLine.m_Name, lstSpawnArea))
            lstMonsterInfo.extend(self.ChooseMonsterInfo(dAreaMonsterSpawn, dNewSpawnArea, dAmount[iArea], iLimitExtAmount))
        
        self.PreprocessCreateMonster(iGroupID, dAreaMonsterSpawn, lstMonsterInfo)

    
    def ChooseMonsterInfo(self, dAreaMonsterSpawn, dSpawnArea, dAmount, iLimitExtAmount):
        tAmount = ChooseKey(self.m_Game, dAmount)
        if tAmount is None:
            SendAlert('err', '地图%d线路%s 怪物刷新数量配置有误（权重均为0），请检查' % (self.m_LevelLine.m_LevelNode.m_Map, self.m_LevelLine.m_Name))
            return []
        iAmount = cl_formula.GetLegacyFormulaResult(self, tAmount)
        iExtAmount = int(cl_formula.GetLegacyFormulaResult(self, self.m_ExtAmount))
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        dMsgInfo = {
            'ExtAmount': iExtAmount,
            'LayerNum': oLevelCtrl.m_LayerNum }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_LAYERMONSTERCNT, oLevelCtrl, dMsgInfo)
        iExtAmount = dMsgInfo['ExtAmount']
        if iLimitExtAmount >= 0:
            iExtAmount = min(iLimitExtAmount, iExtAmount)
        if iAmount != 0:
            iAmount += iExtAmount
        iRound = self.m_Game.m_WarMgr.m_Round
        lstSpawnArea = list(dSpawnArea.keys())
        iLevelLayer = oLevelCtrl.GetLevelLayer(oLevelNode.m_Level)
        dSpawnPos = {
            'Pos': { },
            'Weight': { } }
        dSpawnPos['Weight'].update(dSpawnArea)
        for iArea in lstSpawnArea:
            if iArea not in dAreaMonsterSpawn:
                SendAlert('err', '地图%d线路%s 不存在刷怪区域%d' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea))
                continue
            iLen = len(dAreaMonsterSpawn[iArea]['SpawnPos'])
            dSpawnPos['Pos'][iArea] = [ i for i in range(iLen) ]
        
        lstMonsterInfo = []
        oWarData = self.m_Game.GetWarData()
        iSpawnCnt = 0
        lstSpawnArea = ShufferList(self.m_Game, lstSpawnArea)
        for iArea in lstSpawnArea:
            if iArea not in dAreaMonsterSpawn:
                continue
            dSpawnInfo = dAreaMonsterSpawn[iArea]
            dAssignSID = dSpawnInfo.get('AssignSID', { })
            if not dAssignSID:
                continue
            for iClassify, lstBaseSID in dAssignSID.items():
                dAllBaseSID = GetMonsterSID(iRound, iLevelLayer, iClassify, dSpawnInfo['IsElite'])
                for iBaseSID in lstBaseSID:
                    if iSpawnCnt >= iAmount:
                        continue
                    if iBaseSID not in dSpawnInfo['CustomAI']:
                        continue
                    if iBaseSID not in dAllBaseSID:
                        SendAlert('err', '地图%d线路%s刷怪区域%d 配置的基础怪物%d不存在' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea, iBaseSID))
                        continue
                    dAIConf = dSpawnInfo['CustomAI'][iBaseSID]
                    iMonsterSID = dAIConf.get('MonsterSID', 0)
                    iDefCnt = dAIConf.get('DefCnt', 0)
                    if not iMonsterSID or not iDefCnt:
                        continue
                    for _ in range(iDefCnt):
                        if iArea not in dSpawnPos['Pos']:
                            SendAlert('err', '地图%d线路%s 刷怪区域%s过小' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea))
                            break
                        iSpawnCnt += 1
                        fPower = max(1 / dAllBaseSID[iBaseSID], 1)
                        iCnt = RandomFloat2Int(self.m_Game, fPower)
                        lstPosIdx = dSpawnPos['Pos'][iArea]
                        iPosLen = len(lstPosIdx)
                        if iCnt > iPosLen:
                            SendAlert('err', '地图%d线路%s 刷怪区域%d过小' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea))
                            iCnt = iPosLen
                        lstPosIdx = ShufferList(self.m_Game, dSpawnPos['Pos'][iArea])
                        for iPos in lstPosIdx[:iCnt]:
                            tPos = dSpawnInfo['SpawnPos'][iPos]
                            lstMonsterInfo.append((iArea, iClassify, iBaseSID, iMonsterSID, tPos))
                        
                        dSpawnPos['Pos'][iArea] = lstPosIdx[iCnt:]
                        if not dSpawnPos['Pos'][iArea]:
                            dSpawnPos['Pos'].pop(iArea)
                            dSpawnPos['Weight'].pop(iArea)
                    
                
            
        
        iAmount -= iSpawnCnt
        if iAmount > 0:
            for _ in range(iAmount):
                if not dSpawnPos['Weight']:
                    break
                iArea = ChooseKey(self.m_Game, dSpawnPos['Weight'])
                if iArea not in dAreaMonsterSpawn:
                    continue
                dSpawnInfo = dAreaMonsterSpawn[iArea]
                iClassify = ChooseKey(self.m_Game, dSpawnInfo['Weight'])
                dAssignSID = dSpawnInfo.get('AssignSID', { })
                dAllBaseSID = GetMonsterSID(iRound, iLevelLayer, iClassify, dSpawnInfo['IsElite'])
                lstBaseSID = []
                if iClassify in dAssignSID:
                    for iBaseSID in dAssignSID[iClassify]:
                        if iBaseSID not in dAllBaseSID:
                            SendAlert('err', '地图%d线路%s刷怪区域%d 配置的基础怪物%d不存在' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea, iBaseSID))
                            continue
                        lstBaseSID.append(iBaseSID)
                    
                else:
                    lstBaseSID = list(dAllBaseSID.keys())
                if not lstBaseSID:
                    sClassify = g_ClassifyNotify[iClassify]
                    SendAlert('err', '周目%d 第%d幕 怪物分类%s 未配置怪物' % (iRound, iLevelLayer, sClassify))
                    continue
                lstBaseSID = ShufferList(self.m_Game, lstBaseSID)
                iBaseSID = lstBaseSID[0]
                iMonsterSID = 0
                if iBaseSID in dSpawnInfo['CustomAI']:
                    dAIConf = dSpawnInfo['CustomAI'][iBaseSID]
                    iMonsterSID = dAIConf.get('MonsterSID', 0)
                if not iMonsterSID:
                    lstMonsterSID = oWarData.GetBaseMonsterMap(iBaseSID)
                    if not lstMonsterSID:
                        SendAlert('err', '基础怪物配置%d未配置对应的战场怪物' % (iBaseSID,))
                        continue
                    iMonsterSID = lstMonsterSID[0]
                fPower = max(1 / dAllBaseSID[iBaseSID], 1)
                iCnt = RandomFloat2Int(self.m_Game, fPower)
                lstPosIdx = dSpawnPos['Pos'][iArea]
                iPosLen = len(lstPosIdx)
                if iCnt > iPosLen:
                    SendAlert('err', '地图%d线路%s 刷怪区域%d过小' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea))
                    iCnt = iPosLen
                lstPosIdx = ShufferList(self.m_Game, dSpawnPos['Pos'][iArea])
                for iPos in lstPosIdx[:iCnt]:
                    tPos = dSpawnInfo['SpawnPos'][iPos]
                    lstMonsterInfo.append((iArea, iClassify, iBaseSID, iMonsterSID, tPos))
                
                dSpawnPos['Pos'][iArea] = lstPosIdx[iCnt:]
                if not dSpawnPos['Pos'][iArea]:
                    dSpawnPos['Pos'].pop(iArea)
                    dSpawnPos['Weight'].pop(iArea)
            
        return lstMonsterInfo

    
    def PreprocessCreateMonster(self, iGroupID, dAreaMonsterSpawn, lstMonsterInfo):
        dGroup = self.m_GroupInfo.setdefault(iGroupID, {
            'Wait': { },
            'Live': [],
            'Die': [],
            'TotalWait': 0,
            'CurWait': 0 })
        lstWait = []
        dPatrolInfo = { }
        for idx, tMonsterInfo in enumerate(lstMonsterInfo):
            (iArea, iClassify, iBaseSID, iMonsterSID, tPos) = tMonsterInfo
            dSpawnInfo = dAreaMonsterSpawn[iArea]
            dAIConf = { }
            if iBaseSID in dSpawnInfo['CustomAI']:
                dAIConf = dSpawnInfo['CustomAI'][iBaseSID]
            else:
                dAIConf = dSpawnInfo['DefaultAI'][iClassify]
            lstPatrolPos = dAIConf.get('NewPatrolPos', [])
            dInfo = {
                'AIConfig': { } }
            dInfo['Grade'] = dSpawnInfo['Grade']
            if 'IsFixedFace' in dSpawnInfo and dSpawnInfo['IsFixedFace']:
                dInfo['Angle'] = dSpawnInfo['Angle']
            if 'HatePrefab' in dSpawnInfo and dSpawnInfo['HatePrefab']:
                dInfo['HatePrefab'] = dSpawnInfo['HatePrefab']
                dInfo['HateValue'] = dSpawnInfo['HateValue']
                dInfo['HateType'] = dSpawnInfo['HateType']
            if 'FixDropPos' in dSpawnInfo and dSpawnInfo['FixDropPos']:
                dInfo['FixDropPos'] = dSpawnInfo['FixDropPos']
            if 'CheckDropInfo' in dSpawnInfo and dSpawnInfo['CheckDropInfo']:
                dInfo['CheckDropInfo'] = dSpawnInfo['CheckDropInfo']
            if 'Index' in dSpawnInfo:
                dInfo['AreaIndex'] = dSpawnInfo['Index']
            dInfo['BaseSID'] = iBaseSID
            dInfo['MonsterSID'] = iMonsterSID
            dInfo['Pos'] = tPos
            dInfo['AIConfig'].update(dAIConf)
            dInfo['AIConfig']['GroupID'] = iGroupID
            lstParamLv = dAIConf['AIParamLv']
            if isinstance(lstParamLv, list):
                lstParamLv = ShufferList(self.m_Game, lstParamLv)
                dInfo['AIConfig']['AIParamLv'] = lstParamLv[0]
            tPatrolKey = (iArea, iBaseSID)
            iPatrolIdx = dPatrolInfo.setdefault(tPatrolKey, 0)
            iPatrolCnt = len(lstPatrolPos)
            if iPatrolCnt:
                index = iPatrolIdx % iPatrolCnt
                dInfo['AIConfig']['PatrolPos'] = lstPatrolPos[index]
                dPatrolInfo[tPatrolKey] += 1
            lstWait.append(dInfo)
            self.m_MonsterSpawnDict[iMonsterSID] = 1
        
        idx = dGroup['TotalWait']
        dGroup['TotalWait'] += 1
        dGroup['Wait'][idx] = lstWait

    
    def StartSpawn(self, tSpawnInfo, **kwargs):
        (iGroupID, _, _, iDelay, _) = tSpawnInfo
        if iGroupID not in self.m_GroupInfo:
            return None
        if not self.m_GroupInfo[iGroupID]['Wait']:
            return None
        if self.m_Notify and iGroupID not in self.m_NotifyGroup:
            self.m_NotifyGroup[iGroupID] = 1
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelLine.m_LevelNode.m_Scene)
            cl_snetwar.GS2CMonsterNotify(self.m_Game, cl_notify.GetCommonNotifyMsg(2223), {
                '$group': str(iGroupID) }, iDelay, oScene.GetPlayers())
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.m_LevelLine.m_LevelNode.m_CtrlMgr, {
            'GroupID': iGroupID,
            'MaxGroup': self.MaxGroup(),
            'Delay': iDelay,
            'LineIdx': self.m_LevelLine.GetLineIdx() })
        if not iDelay:
            self.CreateMonsters(iGroupID, **kwargs)
        else:
            sFlag = self.NewCallOutFlag()
            func = Functor(self.CreateMonsters, iGroupID, **kwargs)
            self.m_Game.m_WarMgr.Call_Out(func, Time2Frame(iDelay), sFlag)

    
    def MaxGroup(self):
        if self.m_GroupInfo:
            return max(self.m_GroupInfo)
        return 0

    
    def NowGroup(self):
        if self.m_NotifyGroup:
            return max(self.m_NotifyGroup)
        return 0

    
    def CreateMonsters(self, iGroupID, **kwargs):
        oWarData = self.m_Game.m_WarData
        oLevelNode = self.m_LevelLine.m_LevelNode
        tLineIdx = self.m_LevelLine.GetLineIdx()
        dGroup = self.m_GroupInfo[iGroupID]
        iCurWait = dGroup['CurWait']
        if iCurWait not in dGroup['Wait']:
            return None
        lstWait = dGroup['Wait'][iCurWait]
        dGroup['CurWait'] += 1
        dDelay = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER_PRE, oLevelNode.m_CtrlMgr, {
            'LineIdx': tLineIdx,
            'CreateInfo': lstWait })
        for dInfo in lstWait:
            iMonsterSID = dInfo['MonsterSID']
            clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
            if not clsMonsterData:
                iWarNo = self.m_Game.GetWarMgr().m_SID
                sLineName = self.m_LevelLine.m_Name
                SendAlert('err', '战场%d地图%d线路%s 未配置怪物SID%d' % (iWarNo, oLevelNode.m_Map, sLineName, iMonsterSID))
                continue
            iDelayFrame = clsMonsterData.m_CreateDelayFrame
            lstSameDelayInfo = dDelay.setdefault(iDelayFrame, [])
            lstSameDelayInfo.append(dInfo)
        
        self.DelayCreateMonsters(iGroupID, tLineIdx, dDelay, iCurWait, **kwargs)
        if not lstWait:
            dGroup['Wait'].pop(iCurWait)
        self.TriggerGroupDie(iGroupID, 0, 0)

    
    def DelayCreateMonsters(self, iGroupID, tLineIdx, dDelay, iCurWait, **kwargs):
        oGame = self.m_Game
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        dPlayer = oGame.GetRealPlayers()
        oWarData = oGame.m_WarData
        for iDelayFrame, lstInfo in dDelay.items():
            for dInfo in lstInfo:
                clsMonsterData = oWarData.GetMonsterData(dInfo['MonsterSID'])
                iEffectSID = clsMonsterData.m_CreateEffect
                if iEffectSID:
                    iEffectID = oGame.NewNoSceneObjID()
                    cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], dPlayer)
                if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                    cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
            
            if iDelayFrame:
                sFlag = self.NewCallOutFlag()
                func = Functor(self.TrueCreateMonsters, iGroupID, tLineIdx, lstInfo, iCurWait, **kwargs)
                self.m_Game.m_WarMgr.Call_Out(func, iDelayFrame, sFlag)
                continue
            self.TrueCreateMonsters(iGroupID, tLineIdx, lstInfo, iCurWait, **kwargs)
        

    
    def TrueCreateMonsters(self, iGroupID, tLineIdx, lstInfo, iCurWait, **kwargs):
        oGame = self.m_Game
        oLevelNode = self.m_LevelLine.m_LevelNode
        iScene = oLevelNode.m_Scene
        iSide = SIDE_TYPE_MONSTER
        dGroup = self.m_GroupInfo[iGroupID]
        if iCurWait in dGroup['Wait']:
            dGroup['Wait'].pop(iCurWait)
        dHateTarget = { }
        for dInfo in lstInfo:
            iMonsterSID = dInfo['MonsterSID']
            tPos = dInfo['Pos']
            iGrade = dInfo['Grade']
            iBaseSID = dInfo['BaseSID']
            dAI = dInfo['AIConfig']
            if 'Angle' not in dInfo:
                tFace = self.GetMonsterFacing(tPos)
            else:
                iAngleY = int(dInfo['Angle'][1])
                tFace = cl_math.RotateByEuler((0, 0, 1), (0, iAngleY, 0))
            iID = oGame.NewNPCID()
            dExtInfo = {
                'ID': iID }
            if 'super' in kwargs:
                dExtInfo['SuperInfo'] = kwargs['super']
            dGroup['Live'].append(iID)
            self.m_Monster[iID] = (iGroupID, iBaseSID, iMonsterSID)
            dExtInfo['SetInfo'] = {
                'Room': 1 }
            if 'AreaIndex' in dInfo:
                dExtInfo['AreaIndex'] = dInfo['AreaIndex']
            oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, iSide, iGrade, dAI, tLineIdx, dExtInfo)
            if 'HatePrefab' in dInfo and dInfo['HatePrefab']:
                iPrefab = dInfo['HatePrefab']
                iHateTarget = 0
                if iPrefab in dHateTarget:
                    iHateTarget = dHateTarget[iPrefab]
                else:
                    oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelLine.m_LevelNode.m_Scene)
                    if oScene:
                        for iTarget in oScene.GetObjectsByType(dInfo['HateType']):
                            oTarget = self.m_Game.GetObject(iTarget)
                            if not oTarget or oTarget.m_Prefab != iPrefab:
                                continue
                            iHateTarget = iTarget
                        
                    dHateTarget[iPrefab] = iHateTarget
                if iHateTarget and oMonster.m_Agent:
                    dHateData = {
                        iHateTarget: {
                            'Dam': { },
                            'Hate': [
                                dInfo['HateValue'],
                                GAME_FRAME_INF],
                            'Immutable': 1 } }
                    oMonster.m_Agent.SetData('HateData', dHateData)
            if 'FixDropPos' in dInfo and dInfo['FixDropPos']:
                oMonster.Set('FixDropPos', dInfo['FixDropPos'])
            if 'CheckDropInfo' in dInfo and dInfo['CheckDropInfo']:
                oMonster.Set('CheckDropInfo', dInfo['CheckDropInfo'])
            self.AfterCreateMonster(oMonster, tLineIdx, iGroupID, **kwargs)
        

    
    def AfterCreateMonster(self, oMonster, tLineIdx, iGroupID, **kwargs):
        iID = oMonster.m_ID
        oLevelCtrl = self.m_LevelLine.m_LevelNode.m_CtrlMgr
        if 'super' in kwargs:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER, oLevelCtrl, {
                'Monster': iID,
                'MonsterNo': 0,
                'LineIdx': tLineIdx,
                'Group': iGroupID,
                'SuperInfo': kwargs['super'] })
        else:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER, oLevelCtrl, {
                'Monster': iID,
                'MonsterNo': 0,
                'LineIdx': tLineIdx,
                'Group': iGroupID })
        if 'Owner' in kwargs:
            oOwner = self.m_Game.GetObject(kwargs['Owner'])
            if oOwner:
                oOwner.m_MonsterSummon[iID] = oMonster.m_SID

    
    def IsGroupAllDie(self, iGroup):
        if iGroup not in self.m_GroupInfo:
            return False
        dGroup = self.m_GroupInfo[iGroup]
        if dGroup['Wait'] or dGroup['Live']:
            return False
        return True

    
    def IsMonsterAllDie(self):
        for _, dGroup in self.m_GroupInfo.items():
            if not dGroup['Wait']:
                if dGroup['Live']:
                    return False
        
        return True

    
    def OnWarriorDie(self, dMsgInfo):
        iMonster = dMsgInfo['VID']
        iAttack = dMsgInfo['AID']
        if iMonster not in self.m_Monster:
            return None
        (iGroupID, _, _) = self.m_Monster[iMonster]
        dGroup = self.m_GroupInfo[iGroupID]
        if iMonster in dGroup['Live']:
            dGroup['Live'].remove(iMonster)
            dGroup['Die'].append(iMonster)
        self.TriggerGroupDie(iGroupID, iMonster, iAttack)

    
    def TriggerGroupDie(self, iGroup, iVictim, iAttack):
        tLineIdx = self.m_LevelLine.GetLineIdx()
        if self.IsGroupAllDie(iGroup):
            cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.m_Game.m_WarMgr, {
                'GroupID': iGroup,
                'LineIdx': tLineIdx,
                'VID': iVictim,
                'AID': iAttack })
        if self.IsMonsterAllDie():
            cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WAR_KILLALLMONSTER, self.m_Game.m_WarMgr, {
                'LineIdx': tLineIdx,
                'VID': iVictim,
                'AID': iAttack })

    
    def GetMonsterSummary(self):
        (iDead, iLive, dWait, dMonsterSID) = (0, 0, { }, { })
        for iGroup, dInfo in self.m_GroupInfo.items():
            iDead += len(dInfo['Die'])
            iLive += len(dInfo['Live'])
            dWait[iGroup] = 0
            for lstMonsterInfo in dInfo['Wait'].values():
                dWait[iGroup] += len(lstMonsterInfo)
                for dMonsterInfo in lstMonsterInfo:
                    iMonsterSID = dMonsterInfo['MonsterSID']
                    dMonsterSID.setdefault(iMonsterSID, 0)
                    dMonsterSID[iMonsterSID] += 1
                
            
        
        for _, (_, _, iMonsterSID) in self.m_Monster.items():
            dMonsterSID.setdefault(iMonsterSID, 0)
            dMonsterSID[iMonsterSID] += 1
        
        return {
            'Live': iLive,
            'Die': iDead,
            'Wait': dWait,
            'Variety': dMonsterSID }

    
    def GetGroupRemainCount(self, iGroup):
        iRemain = 0
        if iGroup in self.m_GroupInfo:
            dInfo = self.m_GroupInfo[iGroup]
            iRemain += len(dInfo['Live'])
            for lstMonsterInfo in dInfo['Wait'].values():
                iRemain += len(lstMonsterInfo)
            
        return iRemain

    
    def GetGroupAliveMonster(self, iGroup):
        if iGroup not in self.m_GroupInfo:
            return []
        return list(self.m_GroupInfo[iGroup]['Live'])

    
    def GetMonsterBelong(self, oMonster):
        if oMonster.m_ID in self.m_Monster:
            (iGroup, iBaseSID, _) = self.m_Monster[oMonster.m_ID]
            return (iGroup, iBaseSID)
        return (0, 0)

    
    def GetMonsterByNo(self, iMonsterNo):
        return []

    
    def GetRealMonsterCnt(self):
        iCnt = 0
        for dInfo in self.m_GroupInfo.values():
            for dMonsterInfo in dInfo['Wait'].values():
                iCnt += len(dMonsterInfo)
            
        
        return iCnt

    
    def GetMonsterFacing(self, vOriPos):
        oWarMgr = self.m_Game.m_WarMgr
        lstLive = oWarMgr.GetLiveHero()
        if lstLive:
            iCnt = 1 / len(lstLive)
            vDstPos = (0, 0, 0)
            for iHero in lstLive:
                oHero = self.m_Game.GetObject(iHero)
                tPos = oHero.GetPos()
                vDstPos = cl_math.Vec3Mad(vDstPos, tPos, iCnt)
            
            return cl_math.Vec3Minus(vDstPos, vOriPos)
        return (0, 0, 0)

    
    def GetMonsterCategory(self):
        lstCategory = []
        for dGroup in self.m_GroupInfo.values():
            for lstChosen in dGroup['Wait'].values():
                for dInfo in lstChosen:
                    iBaseSID = dInfo['BaseSID']
                    if iBaseSID in lstCategory:
                        continue
                    lstCategory.append(iBaseSID)
                
            
        
        return lstCategory

    
    def GetMonsterSpawnInfo(self):
        return self.m_MonsterSpawnDict


g_ClassifyNotify = {
    MONSTER_CLASSIFY_ONELAYER_MEDNEAR: '新一幕中型远程',
    MONSTER_CLASSIFY_ONELAYER_SMANEAR: '新一幕小型近程',
    MONSTER_CLASSIFY_ONELAYER_FLY: '新一幕飞行',
    MONSTER_CLASSIFY_THREELAYER_MAGIC: '新三幕法师',
    MONSTER_CLASSIFY_THREELAYER_HEVNEAR: '新三幕重型近程',
    MONSTER_CLASSIFY_THREELAYER_FOOT: '新三幕四足',
    MONSTER_CLASSIFY_THREELAYER_MEDNEAR: '新三幕中型近程',
    MONSTER_CLASSIFY_THREELAYER_HEVFAR: '新三幕重型远程',
    MONSTER_CLASSIFY_THREELAYER_MEDFAR: '新三幕中型远程',
    MONSTER_CLASSIFY_THREELAYER_SMAFAR: '新三幕小型远程',
    MONSTER_CLASSIFY_TWOLAYER_HEVFAR: '新二幕重型远程',
    MONSTER_CLASSIFY_TWOLAYER_MEDNEAR: '新二幕中型近程',
    MONSTER_CLASSIFY_TWOLAYER_MEDFAR: '新二幕中型远程',
    MONSTER_CLASSIFY_TWOLAYER_HEVNEAR: '新二幕重型近程',
    MONSTER_CLASSIFY_TWOLAYER_SMANEAR: '新二幕小型近战',
    MONSTER_CLASSIFY_TWOLAYER_BATTERY: '新二幕炮台',
    MONSTER_CLASSIFY_TWOLAYER_BADGER: '新二幕冲脸',
    MONSTER_CLASSIFY_DURABILITY: '耐久度',
    MONSTER_CLASSIFY_PART: '物部位',
    MONSTER_CLASSIFY_CANNONFODDER: '炮灰怪',
    MONSTER_CLASSIFY_RIDE: '骑乘怪',
    MONSTER_CLASSIFY_LARGESUMMON: '巨型召唤怪',
    MONSTER_CLASSIFY_BOXMONSTER: '宝箱怪',
    MONSTER_CLASSIFY_PETROCHEMICAL: '石化',
    MONSTER_CLASSIFY_BATTERY: '炮台',
    MONSTER_CLASSIFY_DART: '投射',
    MONSTER_CLASSIFY_BOSS: 'BOSS',
    MONSTER_CLASSIFY_FLY: '飞行',
    MONSTER_CLASSIFY_FOOT: '四足',
    MONSTER_CLASSIFY_MAGIC: '法师',
    MONSTER_CLASSIFY_SNIPE: '狙击',
    MONSTER_CLASSIFY_THROW: '投雷',
    MONSTER_CLASSIFY_HEVFAR: '重型远程',
    MONSTER_CLASSIFY_HEVNEAR: '重型近程',
    MONSTER_CLASSIFY_MEDFAR: '中型远程',
    MONSTER_CLASSIFY_MEDNEAR: '中型近程',
    MONSTER_CLASSIFY_SMAFAR: '小型远程',
    MONSTER_CLASSIFY_SMANEAR: '小型近程',
    MONSTER_CLASSIFY_BADGER: '冲脸' }
