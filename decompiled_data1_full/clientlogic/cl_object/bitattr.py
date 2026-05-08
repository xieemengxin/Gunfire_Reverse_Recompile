# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/bitattr.pyc
# RelativePath: clientlogic/cl_object/bitattr.pyc
# Source Generated with Decompyle++
# File: bitattr.pyc (Python 3.6)


class CBitAttr(object):
    m_JoinAttrCache = False
    
    def __init__(self, sAttr):
        self.m_Attr = sAttr
        self.m_CurVal = 0
        self.m_Refresh = 0
        self.m_BitList = { }

    
    def ClearAll(self):
        self.m_CurVal = 0
        self.m_Refresh = 0
        self.m_BitList = { }

    
    def AddValue(self, sKey, iKey):
        if iKey not in self.m_BitList:
            self.m_BitList[iKey] = { }
        self.m_BitList[iKey][sKey] = 1
        if len(self.m_BitList[iKey]) == 1:
            self.m_Refresh = 1

    
    def ClearValue(self, sKey, iKey):
        if iKey not in self.m_BitList:
            return None
        if sKey not in self.m_BitList[iKey]:
            return None
        del self.m_BitList[iKey][sKey]
        if not self.m_BitList[iKey]:
            self.m_Refresh = 1

    
    def GetValue(self):
        if self.m_Refresh:
            self.Refresh()
        return self.m_CurVal

    
    def GetKeyInfo(self, iKey):
        if self.m_Refresh:
            self.Refresh()
        if iKey not in self.m_BitList:
            return { }
        return self.m_BitList[iKey]

    
    def CheckBit(self, iBit):
        if self.m_Refresh:
            self.Refresh()
        return self.m_CurVal & iBit == iBit

    
    def Refresh(self):
        self.m_Refresh = 0
        self.m_CurVal = 0
        for iKey, dInfo in self.m_BitList.items():
            if dInfo:
                self.m_CurVal |= iKey
        

    
    def NeedRefresh(self):
        return self.m_Refresh

    
    def CheckKey(self, iCheckKey):
        for iKey in self.m_BitList:
            if iKey & iCheckKey == iCheckKey:
                return 1
        
        return 0


