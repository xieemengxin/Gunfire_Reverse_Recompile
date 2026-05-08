# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/term.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/term.pyc
# Source Generated with Decompyle++
# File: term.pyc (Python 3.6)


class CFuzzyTerm(object):
    
    def ClearDOM(self):
        pass

    
    def ORWithDOM(self, fDOM):
        pass

    
    def GetDOM(self):
        return 0



class CFzAND(CFuzzyTerm):
    
    def __init__(self, *args):
        self.m_Terms = []
        for oTerm in args:
            self.m_Terms.append(oTerm)
        

    
    def Release(self):
        self.m_Terms = []

    
    def GetDOM(self):
        fMin = 100
        for oTerm in self.m_Terms:
            fDOM = oTerm.GetDOM()
            if fDOM < fMin:
                fMin = fDOM
        
        return fMin

    
    def ORWithDOM(self, fDOM):
        for oTerm in self.m_Terms:
            oTerm.ORWithDOM(fDOM)
        

    
    def ClearDOM(self):
        for oTerm in self.m_Terms:
            oTerm.ClearDOM()
        



class CFzOR(CFuzzyTerm):
    
    def __init__(self, *args):
        self.m_Terms = []
        for oTerm in args:
            self.m_Terms.append(oTerm)
        

    
    def Release(self):
        self.m_Terms = []

    
    def GetDOM(self):
        fMax = -1
        for oTerm in self.m_Terms:
            fDOM = oTerm.GetDOM()
            if fDOM > fMax:
                fMax = fDOM
        
        return fMax

    
    def ORWithDOM(self, fDOM):
        pass

    
    def ClearDOM(self):
        pass


