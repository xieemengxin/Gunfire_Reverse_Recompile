# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_random.pyc
# RelativePath: clientlogic/cl_random.pyc
# Source Generated with Decompyle++
# File: cl_random.pyc (Python 3.6)

import random
import math
from cl_only import SendAlert, ShufferList, ChooseKey
RANDOM_NORMAL = 1
RANDOM_LEVEL = 2
RANDOM_DIRECT = 3
MAX_LEVEL_CHOOSENUM = 10

class CRandomMgr(object):
    
    def __init__(self):
        self.m_Random = { }

    
    def InitRandom(self, iType, sKey, dChoose):
        if iType not in g_RandClass:
            SendAlert('err', '%s init random no type %s' % (sKey, iType))
            return None
        if iType in g_NeedChoose and not dChoose:
            SendAlert('err', '%s init random no choose' % sKey)
            return None
        if sKey in self.m_Random:
            SendAlert('err', '%s repeat init random' % sKey)
            return None
        self.m_Random[sKey] = g_RandClass[iType](dChoose)

    
    def SetChoose(self, sKey, dChoose):
        if sKey not in self.m_Random:
            return None
        self.m_Random[sKey].SetChoose(dChoose)

    
    def ReleaseRandom(self, sKey):
        if sKey not in self.m_Random:
            return None
        oRandom = self.m_Random.pop(sKey)
        oRandom.Release()

    
    def ChooseKey(self, sKey, dData = None):
        if sKey not in self.m_Random:
            return None
        if dData is None:
            dData = { }
        return self.m_Random[sKey].ChooseKey(dData)

    
    def Release(self):
        for sKey in list(self.m_Random):
            self.ReleaseRandom(sKey)
        

    
    def ValidRandom(self, sKey):
        return sKey in self.m_Random



class CBaseRandom(object):
    
    def __init__(self, dChoose):
        self.m_RandObj = random.Random()
        self.m_Choose = dChoose

    
    def Release(self):
        self.m_RandObj = None
        self.m_Choose = { }

    
    def SetChoose(self, dChoose):
        raise NotImplementedError('subclasses must implement')

    
    def ChooseKey(self, dData):
        raise NotImplementedError('subclasses must implement')



class CNormalRandom(CBaseRandom):
    
    def __init__(self, dChoose):
        super(CNormalRandom, self).__init__(dChoose)
        self.m_RandomExpect = { }
        self.m_Probability = { }
        self.Init()

    
    def Init(self):
        iTotal = sum(self.m_Choose.values())
        for sKey, iWeight in self.m_Choose.items():
            if iWeight != 0:
                self.m_Probability[sKey] = iWeight / iTotal
        
        for sKey, p in self.m_Probability.items():
            fExpect = self.m_RandObj.normalvariate(1 / p, 1 / p / 3)
            self.m_RandomExpect[sKey] = fExpect
        

    
    def ChooseKey(self, dData):
        lstSelect = dData['Select'] if 'Select' in dData else []
        bCheck = True if 'Select' in dData else False
        minKey = None
        for randomKey, _ in sorted(self.m_RandomExpect.items(), key = (lambda x: x[1])):
            if bCheck and randomKey not in lstSelect:
                continue
            p = self.m_Probability[randomKey]
            fExpect = self.m_RandObj.normalvariate(1 / p, 1 / p / 3)
            self.m_RandomExpect[randomKey] += fExpect
            minKey = randomKey
        
        return minKey

    
    def SetChoose(self, dChoose):
        if not dChoose:
            return None
        self.m_Choose = dChoose
        self.m_Probability = { }
        dRandomExpect = { }
        iTotal = sum(self.m_Choose.values())
        for sKey, iWeight in self.m_Choose.items():
            if not iWeight:
                continue
            p = iWeight / iTotal
            self.m_Probability[sKey] = p
            if sKey in self.m_RandomExpect:
                dRandomExpect[sKey] = self.m_RandomExpect[sKey]
                continue
            fExpect = self.m_RandObj.normalvariate(1 / p, 1 / p / 3)
            dRandomExpect[sKey] = fExpect
        
        self.m_RandomExpect = dRandomExpect

    
    def Release(self):
        self.m_RandomExpect = { }
        self.m_Probability = { }
        super(CNormalRandom, self).Release()



class CLevelRandom(CBaseRandom):
    
    def __init__(self, dChoose):
        super(CLevelRandom, self).__init__(dChoose)
        self.m_LevelProbability = []
        self.Init()

    
    def Init(self):
        for iLevel, iCnt in self.m_Choose.items():
            self.m_LevelProbability.extend([ iLevel for _ in range(iCnt) ])
        

    
    def ChooseKey(self, dData):
        oGame = dData['Game'] if 'Game' in dData else None
        if not oGame:
            return { }
        fExpect = dData['Expect'] if 'Expect' in dData else 0
        dLevelBaseCnt = dData['LevelBaseCnt'] if 'LevelBaseCnt' in dData else { }
        dLevelCnt = { }
        dChoose = { }
        dLimit = dData['Limit'] if 'Limit' in dData else { }
        for iLevel in self.m_Choose:
            dLevelCnt[iLevel] = dLevelBaseCnt[iLevel] if iLevel in dLevelBaseCnt else 0
            if not not dLimit:
                if dLevelCnt[iLevel] < dLimit.get(iLevel, 0):
                    dChoose[iLevel] = self.m_Choose[iLevel]
                    continue
        
        if not fExpect:
            return dLevelCnt
        fSigma = dData['Sigma'] if 'Sigma' in dData else 0
        fSigma = max(0, fSigma)
        iExpect = round(self.m_RandObj.normalvariate(fExpect, fSigma / 3))
        if 'Min' in dData:
            iExpect = max(dData['Min'], iExpect)
        if 'Max' in dData:
            iExpect = min(dData['Max'], iExpect)
        if not iExpect:
            return dLevelCnt
        for _ in range(MAX_LEVEL_CHOOSENUM):
            if not iExpect or not dChoose:
                break
            iLevel = ChooseKey(oGame, dChoose)
            if not iLevel:
                continue
            if dLimit and dLevelCnt[iLevel] >= dLimit.get(iLevel, 0):
                dChoose.pop(iLevel)
                continue
            dLevelCnt[iLevel] += 1
            iExpect -= 1
        
        return dLevelCnt

    
    def SetChoose(self, dChoose):
        self.m_Choose = dChoose
        self.m_LevelProbability = []
        for iLevel, iCnt in self.m_Choose.items():
            self.m_LevelProbability.extend([ iLevel for _ in range(iCnt) ])
        



class CDirectRandom(CBaseRandom):
    
    def ChooseKey(self, dData):
        iExpect = dData['Expect'] if 'Expect' in dData else 0
        iSigma = dData['Sigma'] if 'Sigma' in dData else 0
        iSigma = max(0, iSigma)
        if not iExpect:
            return 0
        iExpect = self.m_RandObj.normalvariate(iExpect, iSigma / 3)
        iExpect = round(iExpect)
        return iExpect

    
    def SetChoose(self, dChoose):
        pass


g_RandClass = {
    RANDOM_DIRECT: CDirectRandom,
    RANDOM_LEVEL: CLevelRandom,
    RANDOM_NORMAL: CNormalRandom }
g_NeedChoose = (RANDOM_NORMAL, RANDOM_LEVEL)
