# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/linemonsterctrl.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/linemonsterctrl.pyc
# Source Generated with Decompyle++
# File: linemonsterctrl.pyc (Python 3.6)

from cl_commondefines import SIDE_TYPE_MONSTER
from cl_only import Functor, SendAlert, ShufferList, Time2Frame, ChooseKey, WeakProxy
import cl_msgcenter
import cl_snetwar

class CLineMonsterCtrl(object):
    
    def __init__(self, oLevelLine):
        self.m_LevelLine = WeakProxy(oLevelLine)
        self.m_Game = oLevelLine.m_Game
        self.m_Monster = { }
        self.m_MonsterNo = { }
        self.m_GroupInfo = { }
        self.m_CallOutCnt = 0
        self.m_CallOutFlag = { }
        self.m_MonsterSpawnDict = { }

    
    def Release(self):
        for sFlag in self.m_CallOutFlag:
            self.m_Game.m_WarMgr.Remove_Call_Out(sFlag)
        
        self.m_CallOutFlag = { }
        self.m_Monster = { }
        self.m_GroupInfo = { }
        self.m_LevelLine = None
        self.m_Game = None

    
    def ClearPendSpawnMonster(self):
        for sFlag in self.m_CallOutFlag:
            self.m_Game.m_WarMgr.Remove_Call_Out(sFlag)
        
        tLineIdx = self.m_LevelLine.GetLineIdx()
        for iGroup, dGroupInfo in self.m_GroupInfo.items():
            if not dGroupInfo['Wait']:
                if dGroupInfo['Live']:
                    dGroupInfo['Wait'] = { }
                    dGroupInfo['Live'] = []
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.m_Game.m_WarMgr, {
                        'GroupID': iGroup,
                        'LineIdx': tLineIdx,
                        'VID': 0,
                        'AID': 0 })
                    continue
        

    
    def NewCallOutFlag(self):
        self.m_CallOutCnt += 1
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        sFlag = 'Spawn%s-%d-%d' % (self.m_LevelLine.m_Name, self.m_CallOutCnt, iScene)
        self.m_CallOutFlag[sFlag] = 1
        return sFlag

    
    def AddSpawnInfo(self, tSpawnInfo):
        (iGroup, dPrefab, dAmount, _, iSpawnIdx) = tSpawnInfo
        dGroup = self.m_GroupInfo.setdefault(iGroup, {
            'Wait': { },
            'Live': [],
            'Die': [] })
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        iLevel = oLevelNode.m_Level
        sLineName = self.m_LevelLine.m_Name
        iAmount = 0
        if dAmount:
            iAmount = ChooseKey(self.m_Game, dAmount)
        elif dPrefab:
            for iPrefab, _ in dPrefab.items():
                lstNo = oLevelConfData.GetCertainMonsterNo(iLevel, sLineName, iGroup, iPrefab)
                iAmount += len(lstNo)
            
        else:
            lstNo = oLevelConfData.GetCertainMonsterNo(iLevel, sLineName, iGroup, 0)
            iAmount = len(lstNo)
        lstChosen = []
        if dPrefab:
            dWeight = { }
            dPrefabNo = { }
            for iPrefab, _ in dPrefab.items():
                lstNo = oLevelConfData.GetCertainMonsterNo(iLevel, sLineName, iGroup, iPrefab)
                lstNo = ShufferList(self.m_Game, lstNo)
                dPrefabNo[iPrefab] = lstNo
                if len(lstNo):
                    dWeight[iPrefab] = dPrefab[iPrefab]
            
            dChosen = { }
            for _ in range(iAmount):
                if not dWeight:
                    break
                iPrefab = ChooseKey(self.m_Game, dWeight)
                iCnt = dChosen.setdefault(iPrefab, 0)
                dChosen[iPrefab] = iCnt + 1
                if iCnt + 1 >= len(dPrefabNo[iPrefab]):
                    dWeight.pop(iPrefab)
            
            for iPrefab, iCnt in dChosen.items():
                lstChosen.extend(dPrefabNo[iPrefab][:iCnt])
            
        else:
            lstNo = oLevelConfData.GetCertainMonsterNo(iLevel, sLineName, iGroup, 0)
            lstNo = ShufferList(self.m_Game, lstNo)
            iMaxCnt = min(len(lstNo), iAmount)
            lstChosen.extend(lstNo[:iMaxCnt])
        dWaitInfo = { }
        for iWaitID, iMonsterNo in enumerate(lstChosen):
            dInfo = oLevelConfData.GetMonsterInfo(iLevel, sLineName, iMonsterNo)
            iMonsterSID = dInfo['MonsterSID']
            self.m_MonsterSpawnDict[iMonsterSID] = 1
            dWaitInfo[iWaitID] = iMonsterNo
        
        dGroup['Wait'][iSpawnIdx] = dWaitInfo

    
    def StartSpawn(self, tSpawnInfo, **kwargs):
        (iGroup, _, _, iDelay, iSpawnIdx) = tSpawnInfo
        if iGroup not in self.m_GroupInfo:
            return None
        if iSpawnIdx not in self.m_GroupInfo[iGroup]['Wait']:
            return None
        if not iDelay:
            self.CreateMonsters(iGroup, iSpawnIdx, **kwargs)
        else:
            sFlag = self.NewCallOutFlag()
            func = Functor(self.CreateMonsters, iGroup, iSpawnIdx, **kwargs)
            self.m_Game.m_WarMgr.Call_Out(func, Time2Frame(iDelay), sFlag)

    
    def CreateMonsters(self, iGroup, iSpawnIdx, **kwargs):
        oWarData = self.m_Game.m_WarData
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        iLevel = oLevelNode.m_Level
        sLineName = self.m_LevelLine.m_Name
        tLineIdx = self.m_LevelLine.GetLineIdx()
        dMonsterNo = self.m_GroupInfo[iGroup]['Wait'][iSpawnIdx]
        dDelay = { }
        for iWaitID, iMonsterNo in dMonsterNo.items():
            dInfo = oLevelConfData.GetMonsterInfo(iLevel, sLineName, iMonsterNo)
            dMonsterInfo = { }
            dMonsterInfo.update(dInfo)
            dMonsterInfo['AIConfig'].update(dInfo['AIConfig'])
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER_PRE, oLevelNode.m_CtrlMgr, {
                'LineIdx': tLineIdx,
                'CreateInfo': dMonsterInfo })
            iMonsterSID = dMonsterInfo['MonsterSID']
            clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
            if not clsMonsterData:
                iWarNo = self.m_Game.GetWarMgr().m_SID
                SendAlert('err', '战场%d 地图%d 线路%s 未配置怪物SID%d' % (iWarNo, oLevelNode.m_Map, sLineName, iMonsterSID))
                continue
            iDelayFrame = clsMonsterData.m_CreateDelayFrame
            dSameDelayInfo = dDelay.setdefault(iDelayFrame, { })
            dSameDelayInfo[iWaitID] = dMonsterInfo
        
        if dDelay:
            self.DelayCreateMonsters(iGroup, iSpawnIdx, tLineIdx, dDelay, **kwargs)
        else:
            self.m_GroupInfo[iGroup]['Wait'].pop(iSpawnIdx)
        self.TriggerGroupDie(iGroup, 0, 0)

    
    def DelayCreateMonsters(self, iGroup, iSpawnIdx, tLineIdx, dDelay, **kwargs):
        oGame = self.m_Game
        oWarData = oGame.m_WarData
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        dPlayer = oGame.GetRealPlayers()
        for iDelayFrame, dSameDelayInfo in dDelay.items():
            for dInfo in dSameDelayInfo.values():
                clsMonsterData = oWarData.GetMonsterData(dInfo['MonsterSID'])
                iEffectSID = clsMonsterData.m_CreateEffect
                if iEffectSID:
                    iEffectID = oGame.NewNoSceneObjID()
                    cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], dPlayer)
            
            if iDelayFrame:
                sFlag = self.NewCallOutFlag()
                func = Functor(self.TrueCreateMonsters, iGroup, iSpawnIdx, tLineIdx, dSameDelayInfo, **kwargs)
                self.m_Game.m_WarMgr.Call_Out(func, iDelayFrame, sFlag)
                continue
            self.TrueCreateMonsters(iGroup, iSpawnIdx, tLineIdx, dSameDelayInfo, **kwargs)
        

    
    def TrueCreateMonsters(self, iGroup, iSpawnIdx, tLineIdx, dSameDelayInfo, **kwargs):
        oGame = self.m_Game
        oLevelNode = self.m_LevelLine.m_LevelNode
        iScene = oLevelNode.m_Scene
        iSide = SIDE_TYPE_MONSTER
        dGroup = self.m_GroupInfo[iGroup]
        dWait = dGroup['Wait'][iSpawnIdx]
        for iWaitID, dInfo in dSameDelayInfo.items():
            iMonsterNo = dWait.pop(iWaitID)
            iPrefab = dInfo['PrefabID']
            iMonsterSID = dInfo['MonsterSID']
            tPos = dInfo['Pos']
            tFace = dInfo['Facing']
            if 'Grade' in dInfo:
                iGrade = dInfo['Grade']
            else:
                iGrade = self.m_LevelLine.m_CtrlMgr.m_LayerNum
            dAI = dInfo['AIConfig']
            dAI['MonsterNo'] = iMonsterNo
            dAI['GroupID'] = iGroup
            dExtInfo = {
                'SetInfo': {
                    'Room': 1 } }
            oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, iSide, iGrade, dAI, tLineIdx, dExtInfo)
            oMonster.Set('MonsterNo', iMonsterNo)
            iID = oMonster.m_ID
            dGroup['Live'].append(iID)
            self.m_MonsterNo.setdefault(iMonsterNo, []).append(iID)
            self.m_Monster[iID] = (iGroup, iPrefab, iMonsterNo)
            self.AfterCreateMonster(oMonster, iMonsterNo, tLineIdx, **kwargs)
        
        if not dWait:
            dGroup['Wait'].pop(iSpawnIdx)

    
    def AfterCreateMonster(self, oMonster, iMonsterNo, tLineIdx, **kwargs):
        iID = oMonster.m_ID
        oLevelCtrl = self.m_LevelLine.m_LevelNode.m_CtrlMgr
        if 'super' in kwargs:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER, oLevelCtrl, {
                'Monster': iID,
                'MonsterNo': iMonsterNo,
                'LineIdx': tLineIdx,
                'SuperInfo': kwargs['super'] })
        else:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATEMONSTER, oLevelCtrl, {
                'Monster': iID,
                'MonsterNo': iMonsterNo,
                'LineIdx': tLineIdx })
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
            if dGroup['Live']:
                return False
            for _, lstChosen in dGroup['Wait'].items():
                if len(lstChosen) > 0:
                    return False
            
        
        return True

    
    def OnWarriorDie(self, dMsgInfo):
        iMonster = dMsgInfo['VID']
        iAttack = dMsgInfo['AID']
        if iMonster not in self.m_Monster:
            return None
        (iGroup, _, iMonsterNo) = self.m_Monster[iMonster]
        dGroup = self.m_GroupInfo[iGroup]
        if iMonster in dGroup['Live']:
            dGroup['Live'].remove(iMonster)
            dGroup['Die'].append(iMonster)
        if iMonster in self.m_MonsterNo[iMonsterNo]:
            self.m_MonsterNo[iMonsterNo].remove(iMonster)
        self.TriggerGroupDie(iGroup, iMonster, iAttack)

    
    def TriggerGroupDie(self, iGroup, iVictim, iAttack):
        tLineIdx = self.m_LevelLine.GetLineIdx()
        if self.IsGroupAllDie(iGroup):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.m_Game.m_WarMgr, {
                'GroupID': iGroup,
                'LineIdx': tLineIdx,
                'VID': iVictim,
                'AID': iAttack })
        if self.IsMonsterAllDie():
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILLALLMONSTER, self.m_Game.m_WarMgr, {
                'LineIdx': tLineIdx,
                'VID': iVictim,
                'AID': iAttack })

    
    def GetMonsterSummary(self):
        (iDead, iLive, dWait, dMonsterSID) = (0, 0, { }, { })
        lstMonsterSID = []
        for iGroup, dInfo in self.m_GroupInfo.items():
            iDead += len(dInfo['Die'])
            iLive += len(dInfo['Live'])
            dWait[iGroup] = 0
            for _, lstChosen in dInfo['Wait'].items():
                dWait[iGroup] += len(lstChosen)
            
        
        return {
            'Live': iLive,
            'Die': iDead,
            'Wait': dWait,
            'Variety': dMonsterSID }

    
    def GetGroupAliveMonster(self, iGroup):
        if iGroup not in self.m_GroupInfo:
            return []
        return list(self.m_GroupInfo[iGroup]['Live'])

    
    def GetMonsterBelong(self, oMonster):
        if oMonster.m_ID in self.m_Monster:
            (iGroup, iPerfab, iMonsterNo) = self.m_Monster[oMonster.m_ID]
            return (iGroup, iPerfab)
        return (0, 0)

    
    def GetMonsterByNo(self, iMonsterNo):
        if iMonsterNo in self.m_MonsterNo:
            return self.m_MonsterNo[iMonsterNo]
        return []

    
    def GetRealMonsterCnt(self):
        iCnt = 0
        for dGroup in self.m_GroupInfo.values():
            for dChosen in dGroup['Wait'].values():
                iCnt += len(dChosen)
            
        
        return iCnt

    
    def GetMonsterCategory(self):
        lstCategory = []
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        iLevel = oLevelNode.m_Level
        sLineName = self.m_LevelLine.m_Name
        for dGroup in self.m_GroupInfo.values():
            for dChosen in dGroup['Wait'].values():
                for iMonsterNo in dChosen.values():
                    dInfo = oLevelConfData.GetMonsterInfo(iLevel, sLineName, iMonsterNo)
                    iBaseSID = dInfo['PrefabID']
                    if iBaseSID in lstCategory:
                        continue
                    lstCategory.append(iBaseSID)
                
            
        
        return lstCategory

    
    def GetMonsterSpawnInfo(self):
        return self.m_MonsterSpawnDict


