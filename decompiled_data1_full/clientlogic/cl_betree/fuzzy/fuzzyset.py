# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/fuzzyset.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/fuzzyset.pyc
# Source Generated with Decompyle++
# File: fuzzyset.pyc (Python 3.6)


class CFuzzySet(object):
    
    def __init__(self, fRepVal):
        self.m_DOM = 0
        self.m_RepresentativeValue = fRepVal

    
    def ORWithDOM(self, fValue):
        if fValue > self.m_DOM:
            self.m_DOM = fValue

    
    def SetDOM(self, fDOM):
        self.m_DOM = fDOM

    
    def ClearDOM(self):
        self.m_DOM = 0

    
    def GetDOM(self):
        return self.m_DOM

    
    def GetRepresentativeVal(self):
        return self.m_RepresentativeValue

    
    def CalculateDOM(self, fValue):
        return 0



class CFuzzySetLeftShoulder(CFuzzySet):
    
    def __init__(self, fPeak, fLeftOffset, fRightOffset):
        super(CFuzzySetLeftShoulder, self).__init__(((fPeak - fLeftOffset) + fPeak) / 2)
        self.m_PeakPoint = fPeak
        self.m_LeftOffset = fLeftOffset
        self.m_RightOffset = fRightOffset

    
    def CalculateDOM(self, fValue):
        if fValue == self.m_PeakPoint:
            fRet = 1
        elif fValue > self.m_PeakPoint and fValue <= self.m_PeakPoint + self.m_RightOffset:
            fGrad = 1 / -(self.m_RightOffset)
            fRet = fGrad * (fValue - self.m_PeakPoint) + 1
        elif fValue < self.m_PeakPoint and fValue >= self.m_PeakPoint - self.m_LeftOffset:
            fRet = 1
        else:
            fRet = 0
        return fRet



class CFuzzySetRightShoulder(CFuzzySet):
    
    def __init__(self, fPeak, fLeftOffset, fRightOffset):
        super(CFuzzySetRightShoulder, self).__init__((fPeak + fRightOffset + fPeak) / 2)
        self.m_PeakPoint = fPeak
        self.m_LeftOffset = fLeftOffset
        self.m_RightOffset = fRightOffset

    
    def CalculateDOM(self, fValue):
        if fValue == self.m_PeakPoint:
            fRet = 1
        elif fValue < self.m_PeakPoint and fValue >= self.m_PeakPoint - self.m_LeftOffset:
            fGrad = 1 / self.m_LeftOffset
            fRet = fGrad * ((fValue - self.m_PeakPoint) + self.m_LeftOffset)
        elif fValue > self.m_PeakPoint and fValue <= self.m_PeakPoint + self.m_RightOffset:
            fRet = 1
        else:
            fRet = 0
        return fRet



class CFuzzySetTriangle(CFuzzySet):
    
    def __init__(self, fPeak, fLeft, fRight):
        super(CFuzzySetTriangle, self).__init__(fPeak)
        self.m_PeakPoint = fPeak
        self.m_LeftOffset = fLeft
        self.m_RightOffset = fRight

    
    def CalculateDOM(self, fValue):
        if fValue == self.m_PeakPoint:
            fRet = 1
        elif fValue < self.m_PeakPoint and fValue >= self.m_PeakPoint - self.m_LeftOffset:
            fGrad = 1 / self.m_LeftOffset
            fRet = fGrad * ((fValue - self.m_PeakPoint) + self.m_LeftOffset)
        elif fValue > self.m_PeakPoint and fValue <= self.m_PeakPoint + self.m_RightOffset:
            fGrad = 1 / -(self.m_RightOffset)
            fRet = fGrad * (fValue - self.m_PeakPoint) + 1
        else:
            fRet = 0
        return fRet



class CFuzzySetSingleton(CFuzzySet):
    
    def __init__(self, fMid, fLeft, fRight):
        super(CFuzzySetSingleton, self).__init__(fMid)
        self.m_Min = fMid - fLeft
        self.m_Max = fMid + fRight

    
    def CalculateDOM(self, fValue):
        if fValue >= self.m_Min and fValue <= self.m_Max:
            fRet = 1
        else:
            fRet = 0
        return fRet


