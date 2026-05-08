# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/levelconf/unitobj.pyc
# RelativePath: clientlogic/cl_wardata/levelconf/unitobj.pyc
# Source Generated with Decompyle++
# File: unitobj.pyc (Python 3.6)

from cl_commondefines import SURVIVOR_SPAWN_CREATEAREAMONSTER, SPAWN_CREATEAREAMONSTER, LEVEL_SPAWN_TRIGGERNPC, SPAWN_DIFFERENTAREATRIGGERMONSTER, SPAWN_TRIGGERBUILD, SPAWN_TRIGGERMONSTERCHOOSE, SPAWN_TRIGGERSUPMONSTER, SPAWN_TIGGERREWARDNPC, SPAWN_TRIGGERMONSTER, SPAWN_TRIGGERWINDCREATE, SPAWN_TIGGERSURVIVORCREATEHINDER, SURVIVOR_SPAWN_HEROPOSMONSTER

class CBaseJsonUnit(dict):
    m_TransferKeys = ()
    
    def __init__(self, data):
        super(CBaseJsonUnit, self).__init__({ })
        self.AddConfigData(data)

    
    def __setitem__(self, key, val):
        if key in self:
            return None
        dict.__setitem__(self, key, val)

    
    def TransferConfig(self, key, val):
        pass

    
    def AddConfigData(self, data):
        for key, val in data.items():
            if key in self.m_TransferKeys:
                newval = self.TransferConfig(key, val)
                dict.__setitem__(self, key, newval)
                continue
            dict.__setitem__(self, key, val)
        



class CLevelJsonUnit(CBaseJsonUnit):
    m_TransferKeys = 'SpawnRule'
    
    def TransferConfig(self, key, val):
        if key == 'SpawnRule':
            return self.TransferSpawnRule(val)

    
    def TransferSpawnRule(self, val):
        for dSpawn in val:
            lstAction = dSpawn['Action']
            for dAction in lstAction:
                iType = dAction['func']
                if iType not in g_LevelSpawnTransfer:
                    continue
                func = g_LevelSpawnTransfer[iType]
                dAction['param'] = func(dAction['param'])
            
        
        return val



class CMapJsonUnit(CBaseJsonUnit):
    m_TransferKeys = ('hideob', 'rewardpos', 'shoppos', 'eventpos', 'bossrewardpos', 'intervalpos', 'staypos', 'supplypos', 'hinderob')
    
    def TransferConfig(self, key, val):
        if key == 'supplypos':
            return self.TransferStayPos(val)
        if key == 'hinderob':
            return self.TransferHinderob(val)
        return TransferJsonDict(val)

    
    def TransferStayPos(self, val):
        if not val:
            return { }
        dNewVal = { }
        for sArea, info in val.items():
            dTmp = { }
            for sGroup, dPos in info.items():
                iGroup = int(sGroup)
                dTmp[iGroup] = dPos
            
            dNewVal[int(sArea)] = dTmp
        
        return dNewVal

    
    def TransferHinderob(self, val):
        if not val:
            return { }
        dNewVal = { }
        for sArea, info in val.items():
            dTmp = { }
            for sGroup, dGroupInfo in info.items():
                dTmp[int(sGroup)] = TransferJsonDict(dGroupInfo)
            
            dNewVal[int(sArea)] = dTmp
        
        return dNewVal



class CLineJsonUnit(CBaseJsonUnit):
    m_TransferKeys = ('SpawnRule', 'monsterarea', 'monstershowpos', 'monsterspawn', 'lineob', 'dynaob', 'dynabuild', 'initbuild', 'monsterelitepos', 'roundspawnrule', 'summonarea', 'windsummonpos', 'survivalData', 'phasechallengepos', 'trapGroup', 'SurvivorSpawn', 'thunderstormsafepos', 'thundercenterpos')
    
    def TransferConfig(self, key, val):
        if key == 'SpawnRule':
            return self.TransferSpawnRule(val)
        if key in ('roundspawnrule',):
            return self.TransferRoundSpawnRule(val)
        if key == 'monsterarea':
            return self.TransferMonsterArea(val)
        if key == 'monstershowpos':
            return self.TransferShowPos(val)
        if key == 'monsterelitepos':
            return self.TransferElitePos(val)
        if key == 'monsterspawn':
            return self.TransferMonsterSpawn(val)
        if key in ('lineob', 'dynaob'):
            return self.TransferObstacle(val)
        if key in ('dynabuild', 'initbuild'):
            return self.TransferBuild(val)
        if key in 'summonarea':
            return self.TransferSummonArea(val)
        if key in 'windsummonpos':
            return self.TransferWindSummonPos(val)
        if key == 'survivalData':
            return self.TransferSurvivalData(val)
        if key == 'phasechallengepos':
            return self.TransferChallengePos(val)
        if key == 'trapGroup':
            return self.TransferTrapGroup(val)
        if key == 'SurvivorSpawn':
            return self.TransferSurvivorSpawn(val)
        if key == 'thunderstormsafepos':
            if val:
                return val
            return []
        if key == 'thundercenterpos':
            if val:
                return val
            return []

    
    def TransferSurvivalData(self, val):
        if not val:
            return { }
        dNewVal = { }
        for sKey, info in val.items():
            if sKey in ('CustomAI', 'SpareCustomAI'):
                dTmp = { }
                for sPhase, dPhase in info.items():
                    iPhase = int(sPhase)
                    dTmpInfo = { }
                    for sMonsterSID, dInfo in dPhase.items():
                        iMonsterSID = int(sMonsterSID)
                        dTmpInfo[iMonsterSID] = dInfo
                    
                    dTmp[iPhase] = dTmpInfo
                
                dNewVal[sKey] = dTmp
                continue
            if sKey == 'OccupyPos':
                dNewVal[sKey] = TransferJsonDict(info)
                continue
            dNewVal[sKey] = info
        
        return dNewVal

    
    def TransferSpawnRule(self, val):
        for dSpawn in val:
            lstAction = dSpawn['Action']
            for dAction in lstAction:
                iType = dAction['func']
                if iType not in g_LineSpawnTransfer:
                    continue
                func = g_LineSpawnTransfer[iType]
                dAction['param'] = func(dAction['param'])
            
        
        return val

    
    def TransferRoundSpawnRule(self, val):
        dNewVal = { }
        for sRound, info in val.items():
            dTmp = { }
            for sKey, spawn in info.items():
                if sKey == 'SpawnRule':
                    dTmp[sKey] = self.TransferSpawnRule(spawn)
                    continue
                dTmp[sKey] = spawn
            
            dNewVal[int(sRound)] = dTmp
        
        return dNewVal

    
    def TransferMonsterArea(self, val):
        dConfig = { }
        for idx, info in enumerate(val):
            lstPos = []
            for tPos in info['vertices']:
                lstPos.append(tuple(tPos))
            
            info['vertices'] = lstPos
            info['center'] = tuple(info['center'])
            dConfig[idx] = info
        
        return dConfig

    
    def TransferSummonArea(self, val):
        dConfig = { }
        for idx, info in enumerate(val):
            dConfig[idx] = {
                'group': info['group'],
                'center': tuple(info['center']) }
        
        return dConfig

    
    def TransferWindSummonPos(self, val):
        if val:
            return TransferJsonDict(val)

    
    def TransferShowPos(self, val):
        dConfig = { }
        for dPos in val:
            dConfig[dPos['ID']] = tuple(dPos['Center'])
        
        return dConfig

    
    def TransferElitePos(self, val):
        dConfig = { }
        for dPos in val:
            dConfig[dPos['ID']] = {
                'Center': tuple(dPos['Center']) }
            if 'FixDropPos' in dPos:
                dConfig[dPos['ID']].update({
                    'CheckDropInfo': dPos['CheckDropInfo'],
                    'FixDropPos': dPos['FixDropPos'] })
        
        return dConfig

    
    def TransferMonsterSpawn(self, val):
        dConfig = { }
        for dSpawn in val:
            idx = dSpawn['Index']
            dSpawn['Weight'] = TransferJsonDict(dSpawn['Weight'])
            dSpawn['DefaultAI'] = TransferJsonDict(dSpawn['DefaultAI'])
            dSpawn['CustomAI'] = TransferJsonDict(dSpawn['CustomAI'])
            if 'AssignSID' in dSpawn:
                dSpawn['AssignSID'] = TransferJsonDict(dSpawn['AssignSID'])
            dConfig[idx] = dSpawn
        
        return dConfig

    
    def TransferObstacle(self, val):
        dConfig = { }
        for info in val:
            prefab = info['Prefab']
            dConfig[prefab] = info
        
        return dConfig

    
    def TransferBuild(self, val):
        for info in val:
            if 'Perform' not in info:
                continue
            for dPerform in info['Perform']:
                lstParam = dPerform['CustomParam']
                for dParam in lstParam:
                    for key, value in dParam.items():
                        if type(value) != str:
                            continue
                        
                        try:
                            dParam[key] = int(value)
                            continue
                        except ValueError:
                            pass

                        
                        try:
                            dParam[key] = float(value)
                            continue
                        except ValueError:
                            continue

                    
                
            
        
        return val

    
    def TransferChallengePos(self, val):
        dConfig = { }
        for iKey, lstPos in val.items():
            dConfig[int(iKey)] = lstPos
        
        return dConfig

    
    def TransferTrapGroup(self, val):
        if val:
            return TransferJsonDict(val)

    
    def TransferSurvivorSpawn(self, val):
        if not val:
            return { }
        dNewVal = { }
        for sPhase, info in val.items():
            iPhase = int(sPhase)
            dPhase = { }
            for sArea, dSpawn in info.items():
                dTmp = { }
                for sKey, spawn in dSpawn.items():
                    if sKey == 'SpawnRule':
                        dTmp[sKey] = self.TransferSurvivorSpawnRule(spawn)
                        continue
                    if sKey == 'SpawnDistance':
                        dTmp[sKey] = TransferJsonDict(spawn)
                        continue
                    dTmp[sKey] = spawn
                
                dPhase[int(sArea)] = dTmp
            
            dNewVal[iPhase] = dPhase
        
        return dNewVal

    
    def TransferSurvivorSpawnRule(self, val):
        iIndex = 0
        for dSpawn in val:
            lstAction = dSpawn['Action']
            for dAction in lstAction:
                iType = dAction['func']
                if iType == SURVIVOR_SPAWN_HEROPOSMONSTER:
                    iIndex += 1
                    dAction['param'] = TransferSurvivorHeroPosMonster(dAction['param'], iIndex)
                    continue
                if iType not in g_SurvivorSpawnTransfer:
                    continue
                func = g_SurvivorSpawnTransfer[iType]
                dAction['param'] = func(dAction['param'])
            
        
        return val



def TransferJsonDict(dJson):
    dConfig = { }
    for key, val in dJson.items():
        dConfig[int(key)] = val
    
    return dConfig


def TransferMonster(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dPrefab = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dPrefab)
    dAmount = lstSpawnInfo[2]
    lstSpawnInfo[2] = TransferJsonDict(dAmount)
    return tuple(lstSpawnInfo)


def TransferRewardNpc(tSpawnInfo):
    (dNpcWeight, lstAmount) = tSpawnInfo
    dNewNpcWeight = TransferJsonDict(dNpcWeight)
    dNewAmount = { }
    if isinstance(lstAmount, int):
        dNewAmount[lstAmount] = 100
    else:
        for sAmount, iWeight in lstAmount:
            if isinstance(sAmount, list):
                dNewAmount[tuple(sAmount)] = iWeight
                continue
            dNewAmount[sAmount] = iWeight
        
    return (dNewNpcWeight, dNewAmount)


def TransferAreaMonster(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    if len(lstSpawnInfo) == 4:
        lstSpawnInfo.append(-1)
    dArea = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dArea)
    lstAmount = lstSpawnInfo[2]
    dAmount = { }
    for lstRule in lstAmount:
        (lstRule, iWeight) = lstRule
        if isinstance(lstRule, list):
            dAmount[tuple(lstRule)] = iWeight
            continue
        dAmount[lstRule] = iWeight
    
    lstSpawnInfo[2] = dAmount
    return tuple(lstSpawnInfo)


def TransferMonsterChoose(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dArea = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dArea)
    lstAmount = lstSpawnInfo[3]
    dAmount = { }
    for lstRule in lstAmount:
        (lstRule, iWeight) = lstRule
        if isinstance(lstRule, list):
            dAmount[tuple(lstRule)] = iWeight
            continue
        dAmount[lstRule] = iWeight
    
    lstSpawnInfo[3] = dAmount
    return tuple(lstSpawnInfo)


def TranfserTriBuild(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    lstSpawnInfo[0] = TransferJsonDict(lstSpawnInfo[0])
    dRoundAmount = { }
    for sRound, dAmount in tSpawnInfo[1].items():
        iRound = int(sRound)
        dRoundAmount[iRound] = { }
        for sAmount, iRatio in dAmount.items():
            dRoundAmount[iRound][int(sAmount)] = iRatio
        
    
    lstSpawnInfo[1] = dRoundAmount
    return tuple(lstSpawnInfo)


def TranfserTriWind(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dRoundAmount = { }
    for sRound, dAmount in tSpawnInfo[2].items():
        iRound = int(sRound)
        dRoundAmount[iRound] = { }
        for sAmount, iRatio in dAmount.items():
            dRoundAmount[iRound][int(sAmount)] = iRatio
        
    
    lstSpawnInfo[2] = dRoundAmount
    return tuple(lstSpawnInfo)


def TranfserDifferentAreaTriggerMonster(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dArea = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dArea)
    dAmount = { }
    for sRule, dInfo in lstSpawnInfo[3].items():
        iRule = int(sRule)
        dAmount[iRule] = { }
        for sAmount, iRatio in dInfo.items():
            dAmount[iRule][int(sAmount)] = iRatio
        
    
    lstSpawnInfo[3] = dAmount
    return tuple(lstSpawnInfo)


def TransferSurvivorCreateHinder(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dExcludeHinder = { }
    for sHinder, iExcludeHinder in lstSpawnInfo[1].items():
        dExcludeHinder[int(sHinder)] = iExcludeHinder
    
    lstSpawnInfo[1] = dExcludeHinder
    return tuple(lstSpawnInfo)

g_LineSpawnTransfer = {
    SPAWN_TIGGERSURVIVORCREATEHINDER: TransferSurvivorCreateHinder,
    SPAWN_TRIGGERWINDCREATE: TranfserTriWind,
    SPAWN_DIFFERENTAREATRIGGERMONSTER: TranfserDifferentAreaTriggerMonster,
    SPAWN_TRIGGERBUILD: TranfserTriBuild,
    SPAWN_TRIGGERMONSTERCHOOSE: TransferMonsterChoose,
    SPAWN_CREATEAREAMONSTER: TransferAreaMonster,
    SPAWN_TRIGGERSUPMONSTER: TransferMonster,
    SPAWN_TIGGERREWARDNPC: TransferRewardNpc,
    SPAWN_TRIGGERMONSTER: TransferMonster }

def TransferTriNpc(tSpawnInfo):
    (sType, dNpcWeight, lstAmount) = tSpawnInfo
    dNewNpcWeight = TransferJsonDict(dNpcWeight)
    dNewAmount = { }
    if isinstance(lstAmount, int):
        dNewAmount[lstAmount] = 100
    else:
        for sAmount, iWeight in lstAmount:
            if isinstance(sAmount, list):
                dNewAmount[tuple(sAmount)] = iWeight
                continue
            dNewAmount[sAmount] = iWeight
        
    return (sType, dNewNpcWeight, dNewAmount)

g_LevelSpawnTransfer = {
    LEVEL_SPAWN_TRIGGERNPC: TransferTriNpc }

def TransferSurvivorAreaMonster(tSpawnInfo):
    lstSpawnInfo = list(tSpawnInfo)
    dArea = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dArea)
    lstAmount = lstSpawnInfo[2]
    dAmount = { }
    for lstRule in lstAmount:
        (lstRule, iWeight) = lstRule
        if isinstance(lstRule, list):
            dAmount[tuple(lstRule)] = iWeight
            continue
        dAmount[lstRule] = iWeight
    
    lstSpawnInfo[2] = dAmount
    return tuple(lstSpawnInfo)


def TransferSurvivorHeroPosMonster(tSpawnInfo, iIndex):
    lstSpawnInfo = list(tSpawnInfo)
    dArea = lstSpawnInfo[1]
    lstSpawnInfo[1] = TransferJsonDict(dArea)
    lstAmount = lstSpawnInfo[2]
    dAmount = { }
    for lstRule in lstAmount:
        (lstRule, iWeight) = lstRule
        if isinstance(lstRule, list):
            dAmount[tuple(lstRule)] = iWeight
            continue
        dAmount[lstRule] = iWeight
    
    lstSpawnInfo[2] = dAmount
    lstSpawnInfo.append(iIndex)
    return tuple(lstSpawnInfo)

g_SurvivorSpawnTransfer = {
    SURVIVOR_SPAWN_CREATEAREAMONSTER: TransferSurvivorAreaMonster }
