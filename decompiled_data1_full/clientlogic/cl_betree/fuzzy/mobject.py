# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/mobject.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from .variable import CFuzzyVariable
from .defines import VARSET_NAME, SHAPE_LEFTSHOULDER, SHAPE_TRIANGULAR, SHAPE_RIGHTSHOULDER

class CFuzzy(object):
    m_Name = ''
    
    def __init__(self):
        self.m_Variables = { }
        self.m_Rules = []
        self.InitializeFuzzyModule()

    
    def Release(self):
        for oRule in self.m_Rules:
            oRule.Release()
        
        for oVar in self.m_Variables.values():
            oVar.Release()
        
        self.m_Variables = { }
        self.m_Rules = []

    
    def CreateFLV(self, sVarName):
        oVar = CFuzzyVariable()
        self.m_Variables[sVarName] = oVar
        return oVar

    
    def AddRule(self, oAntecedent, oConsequence):
        oRule = CFuzzyRule(oAntecedent, oConsequence)
        self.m_Rules.append(oRule)

    
    def Fuzzify(self, sVarName, fValue):
        self.m_Variables[sVarName].Fuzzify(fValue)

    
    def DeFuzzify(self, sVarName, iMethod = 1):
        for oRule in self.m_Rules:
            oRule.SetConfidenceOfConsequentToZero()
        
        for oRule in self.m_Rules:
            oRule.Calculate()
        
        if iMethod == 1:
            return self.m_Variables[sVarName].DeFuzzifyMaxAv()
        if iMethod == 2:
            return self.m_Variables[sVarName].DeFuzzifyCentroid()
        return 0

    
    def InitializeFuzzyModule(self):
        pass

    
    def InitDesirability(self):
        oFzVarDesirability = self.CreateFLV('Desirability')
        oVeryDesirable = oFzVarDesirability.AddSet('VeryDesirable', SHAPE_RIGHTSHOULDER, 50, 75, 100)
        oDesirable = oFzVarDesirability.AddSet('Desirable', SHAPE_TRIANGULAR, 25, 50, 75)
        oUndesirable = oFzVarDesirability.AddSet('Undesirable', SHAPE_LEFTSHOULDER, 0, 25, 50)
        return (oVeryDesirable, oDesirable, oUndesirable)

    
    def GetDesirability(self, obj):
        return self.DeFuzzify('Desirability', iMethod = 1)

    
    def CollectDebugInfo(self):
        sInfo = ''
        for sVarName, oVar in self.m_Variables.items():
            if sVarName == 'Desirability':
                continue
            sMaxSet = ''
            fMaxDom = 0
            dDom = oVar.GetAllDom()
            for sSet, fDom in dDom.items():
                if fDom > fMaxDom:
                    sMaxSet = sSet
                    fMaxDom = fDom
            
            if sMaxSet in VARSET_NAME:
                sMaxSet = VARSET_NAME[sMaxSet]
            sInfo += '%s 隶属度:%0.2f\n' % (sMaxSet, fMaxDom)
        
        return sInfo



class CFuzzyRule(object):
    
    def __init__(self, oAntecedent, oConsequence):
        self.m_Antecedent = oAntecedent
        self.m_Consequent = oConsequence

    
    def Release(self):
        self.m_Antecedent = None
        self.m_Consequent = None

    
    def SetConfidenceOfConsequentToZero(self):
        self.m_Consequent.ClearDOM()

    
    def Calculate(self):
        self.m_Consequent.ORWithDOM(self.m_Antecedent.GetDOM())


