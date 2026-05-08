# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/__init__.pyc
# RelativePath: clientlogic/cl_wardata/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import TYPE_REMOVE, TYPE_REPLACE, ADJUST_RELIC
import importlib
import cl_msgcenter
import cl_putdata
import cl_summon
if 'g_WarDataObj' not in globals():
    g_WarDataObj = { }

def LoadWarData(iWarNo):
    if iWarNo in g_WarDataObj:
        return g_WarDataObj[iWarNo]
    mod = importlib.import_module('cl_wardata.w%4d' % iWarNo)
    g_WarDataObj[iWarNo] = mod.CWarData(iWarNo)
    return g_WarDataObj[iWarNo]


class CWarData(object):
    m_MainScene = 0
    m_BornPos = [
        (0, 0, 0, 0)]
    m_MapInfo = { }
    m_DataList = { }
    m_AtomList = { }
    m_MonsterData = { }
    m_NpcData = { }
    m_BuildData = { }
    m_MiniGameData = { }
    m_SummonData = { }
    m_ChallengeData = { }
    m_RewardGroup = { }
    m_WeightRewardGroup = { }
    m_HeroData = { }
    m_RewardInfo = { }
    m_SettleParam = { }
    m_QualityParam = { }
    m_UrgentBulletParam = { }
    m_WeaponGradeInfo = { }
    m_GoldenCupLimit = { }
    m_WeightInfo = { }
    m_HideLevelChooseInfo = { }
    m_NpcChooseInfo = { }
    m_PassiveMap = { }
    m_PhaseChallenge = { }
    m_TeamPhaseChallenge = { }
    m_CurseRelic = None
    m_MonsterExcludePassive = { }
    
    def __init__(self, iWarNo):
        self.m_WarNo = iWarNo

    
    def GetBornPos(self):
        return self.m_BornPos

    
    def GetMapInfo(self, iSceneSID):
        if iSceneSID in self.m_MapInfo:
            return self.m_MapInfo[iSceneSID]
        return iSceneSID

    
    def GetMainScene(self):
        return self.m_MainScene

    
    def GetResData(self, iDataSID):
        if iDataSID not in self.m_DataList:
            return None
        return self.m_DataList[iDataSID]

    
    def GetAtom(self, iAtomID):
        if iAtomID in self.m_AtomList:
            return self.m_AtomList[iAtomID]

    
    def GetAtoms(self):
        return self.m_AtomList

    
    def GetMonsterData(self, iMonsterSID):
        if iMonsterSID in self.m_MonsterData:
            clsMonsterData = self.m_MonsterData[iMonsterSID]
            clsMonsterData.InitBaseData()
            return clsMonsterData

    
    def GetMonsterPartData(self, iMonsterPartSID):
        if iMonsterPartSID in self.m_MonsterPartData:
            clsMonsterData = self.m_MonsterPartData[iMonsterPartSID]
            return clsMonsterData

    
    def GetBuildData(self, iBuildSID):
        if iBuildSID in self.m_BuildData:
            clsBuildData = self.m_BuildData[iBuildSID]
            clsBuildData.InitBaseData()
            return clsBuildData

    
    def GetNpcData(self, iNpcSID):
        if iNpcSID not in self.m_NpcData:
            return None
        return self.m_NpcData[iNpcSID]

    
    def GetMiniGameData(self, iMiniGameSID):
        if iMiniGameSID not in self.m_MiniGameData:
            return None
        return self.m_MiniGameData[iMiniGameSID]

    
    def GetRewardInfo(self):
        return self.m_RewardInfo

    
    def GetSummonData(self, iSummonSID):
        if iSummonSID in self.m_SummonData:
            clsSummonData = self.m_SummonData[iSummonSID]
            clsSummonData.InitBaseData()
            return clsSummonData

    
    def GetHeroData(self, iHero):
        if iHero in self.m_HeroData:
            return self.m_HeroData[iHero]

    
    def GetChallengeData(self, iChallengeSID):
        if iChallengeSID in self.m_ChallengeData:
            return self.m_ChallengeData[iChallengeSID]

    
    def GetWeightRewardGroup(self, iGroup):
        if iGroup in self.m_WeightRewardGroup:
            return dict(self.m_WeightRewardGroup[iGroup])
        return { }

    
    def GetRewardGroup(self, iGroup):
        if iGroup in self.m_RewardGroup:
            return dict(self.m_RewardGroup[iGroup])
        return { }

    
    def GetSettleConf(self):
        return self.m_SettleParam

    
    def GetQualityConf(self):
        return self.m_QualityParam

    
    def GetUrgentBulletConf(self):
        return self.m_UrgentBulletParam

    
    def GetRewardWeightConf(self):
        return self.m_WeightInfo

    
    def GetHideLevelChooseInfo(self):
        return self.m_HideLevelChooseInfo

    
    def GetWeaponGrade(self, iLayer, iLevel, oGame):
        dMsgInfo = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_WEAPONGRADE, oGame.m_WarMgr, dMsgInfo)
        iGrade = 0
        if 'Grade' in dMsgInfo:
            iGrade = dMsgInfo['Grade']
        else:
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl:
                (iLayer, iLevel) = oLevelCtrl.GetLayerAndLevelMap(iLayer, iLevel)
            dWeaponGrade = self.m_WeaponGradeInfo['WeaponGrade']
            if iLayer in dWeaponGrade:
                dLayer = dWeaponGrade[iLayer]
                if iLevel in dLayer:
                    iGrade = dLayer[iLevel]
        iMaxGrade = self.GetMaxWeaponGrade(oGame)
        if iGrade > iMaxGrade:
            iGrade = iMaxGrade
        return iGrade

    
    def GetInscriptionProb(self):
        return self.m_WeaponGradeInfo['InscriptionTypeProb']

    
    def GetWeaponUpgradeCost(self, iCurGrade):
        dUpgrade = self.m_WeaponGradeInfo['WeaponUpGradeCost']
        if not dUpgrade:
            return 0
        iNewGrade = self.GetWeaponNewGrade(dUpgrade, iCurGrade)
        return dUpgrade[iNewGrade]

    
    def GetMaxWeaponGrade(self, oGame = None):
        return 65000

    
    def GetWeaponNewGrade(self, dConfig, iCurGrade):
        lstGrade = list(dConfig)
        iMaxGrade = max(lstGrade)
        iMinGrade = min(lstGrade)
        iCurGrade = max(iMinGrade, iCurGrade)
        iCurGrade = min(iMaxGrade, iCurGrade)
        if iCurGrade not in dConfig:
            lstGrade.sort()
            lstGrade = lstGrade[:-1]
            for _ in range(len(lstGrade)):
                iGrade = lstGrade.pop()
                if iCurGrade > iGrade:
                    iCurGrade = iGrade
                    break
            
        return iCurGrade

    
    def GetWeaponGradeAddition(self, iGrade):
        dAddition = self.m_WeaponGradeInfo['WeaponGradeAddition'] if 'WeaponGradeAddition' in self.m_WeaponGradeInfo else { }
        if iGrade in dAddition:
            return dAddition[iGrade]
        dNewAddition = { }
        iNewGrade = self.GetWeaponNewGrade(dAddition, iGrade)
        for skey, (iAdd, iMul) in dAddition[iNewGrade].items():
            dNewAddition[skey] = (iAdd, iMul + 1500 * (iGrade - iNewGrade))
        
        return dNewAddition

    
    def GetInscriptionNum(self, iLayer, iLevel, oLevelCtrl = None):
        if oLevelCtrl:
            dMsgInfo = { }
            oWarMgr = oLevelCtrl.m_Game.m_WarMgr
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMSG_INSCRIPTIONNUM, oWarMgr, dMsgInfo)
            if 'InscriptionNum' in dMsgInfo:
                return dMsgInfo['InscriptionNum']
            (iLayer, iLevel) = oLevelCtrl.GetLayerAndLevelMap(iLayer, iLevel)
        dInscriptionNum = self.m_WeaponGradeInfo.get('InscriptionNum', { })
        iNum = 0
        for (layer, level), num in dInscriptionNum.items():
            if layer > iLayer:
                continue
            if layer == iLayer and level > iLevel:
                continue
            iNum = num
        
        return iNum

    
    def GetMaxInscriptionNum(self):
        dInscriptionNum = self.m_WeaponGradeInfo.get('InscriptionNum', { })
        if dInscriptionNum:
            return max(dInscriptionNum.values())
        return 0

    
    def GetGoldenCupLimit(self):
        return self.m_GoldenCupLimit

    
    def GetNpcChooseInfo(self):
        return self.m_NpcChooseInfo

    
    def GetMonsterExcludePassive(self):
        return self.m_MonsterExcludePassive

    
    def GetPhaseChallengeData(self, iChallenge):
        if iChallenge in self.m_PhaseChallenge:
            return self.m_PhaseChallenge[iChallenge]

    
    def GetPassiveMapByType(self, iType):
        if iType not in self.m_PassiveMap:
            return { }
        return self.m_PassiveMap[iType]

    
    def GetTruePassive(self, iType, iSID):
        if iType not in self.m_PassiveMap:
            return iSID
        dTypeMap = self.m_PassiveMap[iType]
        if iSID in dTypeMap[TYPE_REMOVE]:
            return 0
        if iSID in dTypeMap[TYPE_REPLACE]:
            return dTypeMap[TYPE_REPLACE][iSID]
        return iSID

    
    def GetAllCurseRelic(self):
        if self.m_CurseRelic is not None:
            return self.m_CurseRelic
        lstAllPutCurseRelic = cl_putdata.GetAllPutCurseRelic()
        if ADJUST_RELIC not in self.m_PassiveMap:
            self.m_CurseRelic = lstAllPutCurseRelic
            return self.m_CurseRelic
        lstCurseRelic = []
        dRelicMap = self.m_PassiveMap[ADJUST_RELIC]
        for iRelic in lstAllPutCurseRelic:
            if iRelic in dRelicMap[TYPE_REMOVE]:
                continue
            if iRelic in dRelicMap[TYPE_REPLACE]:
                iRelic = dRelicMap[TYPE_REPLACE][iRelic]
            lstCurseRelic.append(iRelic)
        
        self.m_CurseRelic = lstCurseRelic
        return self.m_CurseRelic



class CPVEWarMgr(CWarData):
    m_LevelInfo = { }
    m_LevelEvent = { }
    m_ResArea = { }
    m_SpawnInfo = { }
    m_ObjSpawnInfo = { }
    m_LevelNotifyText = { }
    m_BaseMonsterMap = { }
    m_Config = { }
    m_Layer2MonsterRelifeTime = { }
    m_ThresholdInfo = { }
    
    def __init__(self, iWarNo):
        super().__init__(iWarNo)
        self.m_LevelEventType = { }
        for dLevel in self.m_LevelEvent.values():
            for iType, setMap in dLevel.items():
                for iMap in setMap:
                    self.m_LevelEventType[iMap] = iType
                
            
        

    
    def GetSpawnInfo(self, iLevelNodeSID, iType):
        if iLevelNodeSID not in self.m_SpawnInfo:
            return { }
        if iType not in self.m_SpawnInfo[iLevelNodeSID]:
            return { }
        return self.m_SpawnInfo[iLevelNodeSID][iType]

    
    def GetConfig(self):
        return self.m_Config

    
    def GetLevelInfo(self, iLevel):
        if iLevel not in self.m_LevelInfo:
            return { }
        return self.m_LevelInfo[iLevel]

    
    def GetLevelEvent(self, iLevel):
        if iLevel not in self.m_LevelEvent:
            return { }
        return self.m_LevelEvent[iLevel]

    
    def GetEventType(self, iSceneSID):
        if iSceneSID not in self.m_LevelEventType:
            return 0
        return self.m_LevelEventType[iSceneSID]

    
    def GetObjSpawnInfo(self, iLevelNodeSID, iType):
        if iLevelNodeSID not in self.m_ObjSpawnInfo:
            return { }
        if iType not in self.m_ObjSpawnInfo[iLevelNodeSID]:
            return { }
        return self.m_ObjSpawnInfo[iLevelNodeSID][iType]

    
    def GetLevelNotifyText(self, iType, iLeveltype, iGametype, *lstArgs):
        tKey = (iType, iLeveltype, iGametype)
        if tKey not in self.m_LevelNotifyText:
            return None
        sText = self.m_LevelNotifyText[tKey]
        if lstArgs and '%' in sText:
            sText = sText % lstArgs
        return sText

    
    def GetMonsterRelifeTime(self):
        return self.m_Layer2MonsterRelifeTime

    
    def GetBaseMonsterMap(self, iBaseSID):
        if iBaseSID not in self.m_BaseMonsterMap:
            return []
        return self.m_BaseMonsterMap[iBaseSID]

    
    def GetThreshold(self, skey, *args):
        dInfo = self.m_ThresholdInfo
        if skey in dInfo and args in dInfo[skey]:
            return self.m_ThresholdInfo[skey][args]



def R_OperateLevel(resfunc, dOperation):
    for (iWarNo, iLayerNum, iLevelNum, iLevel), iAdd in dOperation.items():
        
        try:
            mod = importlib.import_module('cl_wardata.wm%4d' % iWarNo)
        except:
            continue

        if hasattr(mod, 'CLevelCtrlElement'):
            dLevelCtrlConf = mod.CLevelCtrlElement.m_LevelCtrlConf
        elif hasattr(mod, 'CTestLevelCtrl'):
            dLevelCtrlConf = mod.CTestLevelCtrl.m_LevelCtrlConf
        elif hasattr(mod, 'CExploreLevelCtrl'):
            dLevelCtrlConf = mod.CExploreLevelCtrl.m_LevelCtrlConf
        
        if iLayerNum not in dLevelCtrlConf:
            continue
        dCtrlInfo = dLevelCtrlConf[iLayerNum]['CtrlInfo']
        if iAdd:
            iMaxLevel = len(dCtrlInfo)
            if iLevelNum == 0:
                dLevelCtrlConf[iLayerNum]['HallInfo'] = iLevel
            elif iLevelNum > iMaxLevel:
                dLevelCtrlConf[iLayerNum]['BossInfo']['BossStore'][iLevel] = 10
            else:
                tLevel = dCtrlInfo[iLevelNum]['NormalStore']
                if iLevel in tLevel:
                    continue
                lstNewLevel = [
                    iLevel]
                lstNewLevel.extend(tLevel)
                dCtrlInfo[iLevelNum]['NormalStore'] = tuple(lstNewLevel)
            continue
        if iLevelNum not in dCtrlInfo:
            continue
        lstNewLevel = list(dCtrlInfo[iLevelNum]['NormalStore'])
        if iLevel in lstNewLevel:
            lstNewLevel.remove(iLevel)
        dCtrlInfo[iLevelNum]['NormalStore'] = tuple(lstNewLevel)
        dNewHide = { }
        dNewHideStore = { }
        dHideStore = dCtrlInfo[iLevelNum]['HideLevelStore']
        for iRound, dHideInfo in dHideStore.items():
            for tHideLevel, iWeight in dHideInfo.items():
                if tHideLevel[0] == iLevel:
                    continue
                dNewHideType = dNewHide.setdefault(iRound, { })
                dNewHideType[tHideLevel[0]] = tHideLevel[1]
                dNewHideInfo = dNewHideStore.setdefault(iRound, { })
                dNewHideInfo[tHideLevel] = iWeight
            
        
        dCtrlInfo[iLevelNum]['HideLevel'] = dNewHide
        dCtrlInfo[iLevelNum]['HideLevelStore'] = dNewHideStore
    

