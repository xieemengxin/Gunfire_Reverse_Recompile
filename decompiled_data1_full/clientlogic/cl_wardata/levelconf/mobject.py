# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/levelconf/mobject.pyc
# RelativePath: clientlogic/cl_wardata/levelconf/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

import cllib.lib_flag
from . import load

class CLevelConfDataMgr(object):
    
    def __init__(self, oLevelCtrl = None):
        self.m_LevelConf = { }
        self.m_CtrlMgr = oLevelCtrl

    
    def Release(self):
        for _, oConf in self.m_LevelConf.items():
            oConf.Release()
        
        self.m_LevelConf = { }
        self.m_CtrlMgr = None

    
    def LoadLevelConf(self, iLevel):
        iLevel = self.GetConfigLevel(iLevel)
        if iLevel in self.m_LevelConf:
            return None
        dConfData = load.GetLevelConfData(iLevel)
        if dConfData:
            oConf = CLevelConfData(iLevel, dConfData)
            self.m_LevelConf[iLevel] = oConf

    
    def UnLoadLevelConf(self, lstLevel):
        for iLevel in lstLevel:
            iLevel = self.GetConfigLevel(iLevel)
            if iLevel not in self.m_LevelConf:
                continue
            oConf = self.m_LevelConf.pop(iLevel)
            oConf.Release()
            if cllib.lib_flag.g_AutoDelMapRes:
                load.ReleaseLevelConfig(iLevel)
        

    
    def GetLineConfig(self, iLevel, sLineName, *sKeyList, default = None):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return default
        oConf = self.m_LevelConf[iLevel]
        return oConf.GetLineConfig(sLineName, *sKeyList, **{
            'default': default })

    
    def GetLevelConfig(self, iLevel, *sKeyList, default = { }):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return default
        oConf = self.m_LevelConf[iLevel]
        return oConf.GetLevelConfig(*sKeyList, **{
            'default': default })

    
    def GetMapConfig(self, iLevel, *sKeyList, default = { }):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return default
        oConf = self.m_LevelConf[iLevel]
        return oConf.GetMapConfig(*sKeyList, **{
            'default': default })

    
    def GetCertainMonsterNo(self, iLevel, sLineName, iGroupID, iPrefabID):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return []
        lstMonsterNo = []
        oConf = self.m_LevelConf[iLevel]
        lstSceneMonsters = oConf.GetLineConfig(sLineName, 'monsterconf')
        for dInfo in lstSceneMonsters:
            if iGroupID != dInfo['GroupID']:
                continue
            if iPrefabID and iPrefabID != dInfo['PrefabID']:
                continue
            iMonsterNo = dInfo['MonsterID']
            lstMonsterNo.append(iMonsterNo)
        
        return lstMonsterNo

    
    def GetMonsterInfo(self, iLevel, sLineName, iMonsterNo):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return { }
        oConf = self.m_LevelConf[iLevel]
        lstSceneMonsters = oConf.GetLineConfig(sLineName, 'monsterconf')
        for dInfo in lstSceneMonsters:
            if dInfo['MonsterID'] == iMonsterNo:
                return dInfo
        
        return { }

    
    def GetLevelResData(self, iLevel, lstLineName):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return { }
        lstEvt = []
        oConf = self.m_LevelConf[iLevel]
        for sLineName in lstLineName:
            lstEvt.extend(oConf.GetLineConfig(sLineName, 'staticevt'))
        
        dLevelLine = oConf.GetLevelConfig('arealine')
        dResData = {
            'Areas': list(dLevelLine.keys()),
            'Events': lstEvt }
        return dResData

    
    def GetAreaMonsterSpawnInfo(self, iLevel, sLineName, lstSpawnArea):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return { }
        dAreaMonsterSpawn = { }
        oConf = self.m_LevelConf[iLevel]
        dMonsterSpawn = oConf.GetLineConfig(sLineName, 'monsterspawn')
        for iArea in lstSpawnArea:
            if iArea in dMonsterSpawn:
                dAreaMonsterSpawn[iArea] = dMonsterSpawn[iArea]
        
        return dAreaMonsterSpawn

    
    def GetLineSpawnRule(self, iLevel, sLineName, iRound):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return []
        oConf = self.m_LevelConf[iLevel]
        lstSpawnRule = oConf.GetLineConfig(sLineName, 'roundspawnrule', iRound, 'SpawnRule', default = -1)
        if lstSpawnRule != -1:
            return lstSpawnRule
        return oConf.GetLineConfig(sLineName, 'SpawnRule', default = [])

    
    def GetLineSpawnGoal(self, iLevel, sLineName, iRound):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return { }
        oConf = self.m_LevelConf[iLevel]
        dSpawnRule = oConf.GetLineConfig(sLineName, 'roundspawnrule', iRound, 'GoalRule', default = -1)
        if dSpawnRule != -1:
            return dSpawnRule
        return oConf.GetLineConfig(sLineName, 'linegoal', default = { })

    
    def GetLineMergeFlag(self, iLevel, sLineName, iRound):
        iLevel = self.GetConfigLevel(iLevel)
        self.LoadLevelConf(iLevel)
        if iLevel not in self.m_LevelConf:
            return 0
        oConf = self.m_LevelConf[iLevel]
        iMerge = oConf.GetLineConfig(sLineName, 'roundspawnrule', iRound, 'Merge', default = -1)
        if iMerge != -1:
            return iMerge
        return oConf.GetLineConfig(sLineName, 'Merge', default = 0)

    
    def GetConfigLevel(self, iLevel):
        oLevelCtrl = self.m_CtrlMgr
        if not oLevelCtrl:
            return iLevel
        return oLevelCtrl.GetConfigLevel(iLevel)

    
    def GetLevelBaseConf(self, iLevel, sAttr):
        if iLevel in load.g_LevelConfig and sAttr in load.g_LevelConfig[iLevel]:
            return load.g_LevelConfig[iLevel][sAttr]



class CLevelConfData(object):
    
    def __init__(self, iLevel, dConfData):
        self.m_Level = iLevel
        self.m_ConfData = dConfData

    
    def Release(self):
        self.m_ConfData = { }

    
    def GetLineConfig(self, sLineName, *sKeyList, default = None):
        dLineConfig = self.m_ConfData['line'].get(sLineName, { })
        for sKey in sKeyList:
            if sKey in dLineConfig:
                dLineConfig = dLineConfig[sKey]
                continue
            return default
        
        return dLineConfig

    
    def GetLevelConfig(self, *sKeyList, default = { }):
        dLevelConfig = self.m_ConfData['level']
        for sKey in sKeyList:
            if sKey in dLevelConfig:
                dLevelConfig = dLevelConfig[sKey]
                continue
            return default
        
        return dLevelConfig

    
    def GetMapConfig(self, *sKeyList, default = { }):
        dMapConfig = self.m_ConfData['map']
        for sKey in sKeyList:
            if sKey in dMapConfig:
                dMapConfig = dMapConfig[sKey]
                continue
            return default
        
        return dMapConfig


