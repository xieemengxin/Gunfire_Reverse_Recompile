# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/variable.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/variable.pyc
# Source Generated with Decompyle++
# File: variable.pyc (Python 3.6)

from .fuzzyset import CFuzzySetLeftShoulder, CFuzzySetRightShoulder, CFuzzySetTriangle, CFuzzySetSingleton
from .defines import SHAPE_LEFTSHOULDER, SHAPE_RIGHTSHOULDER, SHAPE_TRIANGULAR, SHAPE_SINGLETON

class CFuzzyVariable(object):
    m_SetClsMap = {
        SHAPE_SINGLETON: CFuzzySetSingleton,
        SHAPE_TRIANGULAR: CFuzzySetTriangle,
        SHAPE_RIGHTSHOULDER: CFuzzySetRightShoulder,
        SHAPE_LEFTSHOULDER: CFuzzySetLeftShoulder }
    
    def __init__(self):
        self.m_MemberSets = { }
        self.m_MinRange = 0
        self.m_MaxRange = 0

    
    def Release(self):
        self.m_MemberSets = { }

    
    def AdjustRangeToFit(self, fMin, fMax):
        if fMin < self.m_MinRange:
            self.m_MinRange = fMin
        if fMax > self.m_MaxRange:
            self.m_MaxRange = fMax

    
    def Fuzzify(self, fValue):
        fValue = max(fValue, self.m_MinRange)
        fValue = min(fValue, self.m_MaxRange)
        for oSet in self.m_MemberSets.values():
            oSet.SetDOM(oSet.CalculateDOM(fValue))
        

    
    def AddSet(self, sName, iShapeType, fMinBound, fPeak, fMaxBound):
        setCls = self.m_SetClsMap[iShapeType]
        oSet = setCls(fPeak, fPeak - fMinBound, fMaxBound - fPeak)
        self.m_MemberSets[sName] = oSet
        self.AdjustRangeToFit(fMinBound, fMaxBound)
        return oSet

    
    def DeFuzzifyMaxAv(self):
        fBottom = 0
        fTop = 0
        for oSet in self.m_MemberSets.values():
            fDOM = oSet.GetDOM()
            fBottom += fDOM
            fTop += oSet.GetRepresentativeVal() * fDOM
        
        if fBottom:
            return fTop / fBottom
        return 0

    
    def DeFuzzifyCentroid(self, iNumSamples = 10):
        fStepSize = (self.m_MaxRange - self.m_MinRange) / iNumSamples
        fTotalArea = 0
        fSumOfMoments = 0
        for iSamp in range(1, iNumSamples + 1):
            for oSet in self.m_MemberSets.values():
                fValue = self.m_MinRange + iSamp * fStepSize
                fContribution = min(oSet.CalculateDOM(fValue), oSet.GetDOM())
                fTotalArea += fContribution
                fSumOfMoments += fValue * fContribution
            
        
        if fTotalArea:
            return fSumOfMoments / fTotalArea
        return 0

    
    def GetAllDom(self):
        dRet = { }
        for sName, oSet in self.m_MemberSets.items():
            dRet[sName] = oSet.GetDOM()
        
        return dRet


