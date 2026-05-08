# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/maxattr.pyc
# RelativePath: clientlogic/cl_object/maxattr.pyc
# Source Generated with Decompyle++
# File: maxattr.pyc (Python 3.6)


class CMaxAttr(object):
    m_JoinAttrCache = False
    
    def __init__(self, oGame, sAttr):
        self.m_Attr = sAttr
        self.m_Game = oGame
        self.m_CurVal = 0
        self.m_OnceVal = 0
        self.m_CurKey = 0
        self.m_CurTime = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Time = { }

    
    def ClearAll(self):
        self.m_Game = None
        self.m_CurVal = 0
        self.m_OnceVal = 0
        self.m_CurKey = 0
        self.m_CurTime = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Time = { }

    
    def AddValue(self, sKey, iValue, iTime):
        if not iTime:
            self.m_Time[sKey] = 0
            if self.m_OnceVal < iValue:
                self.m_OnceVal = iValue
                self.m_Data[sKey] = iValue
            return None
        self.m_Data[sKey] = iValue
        self.m_Time[sKey] = self.m_Game.GetFrameNum() + iTime
        if iValue > self.m_CurVal:
            self.m_CurVal = iValue
            self.m_CurKey = sKey
            self.m_CurTime = self.m_Time[sKey]
        elif iValue == self.m_CurVal and self.m_Time[sKey] > self.m_CurTime:
            self.m_CurKey = sKey
            self.m_CurTime = self.m_Time[sKey]

    
    def ClearValue(self, sKey):
        if sKey not in self.m_Data:
            return None
        if not self.m_Time[sKey] and self.m_Data[sKey] == self.m_OnceVal:
            self.m_OnceVal = 0
        del self.m_Data[sKey]
        del self.m_Time[sKey]
        if sKey == self.m_CurKey:
            self.m_Refresh = 1

    
    def GetTime(self):
        if self.m_Refresh or self.m_CurTime <= self.m_Game.GetFrameNum():
            self.Refresh()
        iRemain = self.m_CurTime - self.m_Game.GetFrameNum()
        if iRemain < 0:
            return 0
        return iRemain

    
    def GetValue(self):
        if self.m_Refresh or self.m_CurTime <= self.m_Game.GetFrameNum():
            self.Refresh()
        iValue = self.m_OnceVal
        self.m_OnceVal = 0
        if iValue > self.m_CurVal:
            return iValue
        return self.m_CurVal

    
    def Refresh(self):
        self.m_Refresh = 0
        self.m_CurVal = 0
        self.m_CurKey = 0
        self.m_CurTime = 0
        dData = self.m_Data
        dTime = self.m_Time
        self.m_Data = { }
        self.m_Time = { }
        iNowTime = self.m_Game.GetFrameNum()
        for sKey, iVal in dData.items():
            iTime = dTime[sKey]
            if iTime < iNowTime:
                continue
            self.m_Data[sKey] = iVal
            self.m_Time[sKey] = iTime
            if iVal > self.m_CurVal:
                self.m_CurVal = iVal
                self.m_CurKey = sKey
                self.m_CurTime = iTime
                continue
            if iVal == self.m_CurVal and self.m_CurTime < iTime:
                self.m_CurKey = sKey
                self.m_CurTime = iTime
        



class CMinAttr(object):
    m_Default = 0xFFFFFFFF
    
    def __init__(self, oGame, sAttr, iDefault):
        self.m_Attr = sAttr
        self.m_Game = oGame
        self.m_Default = iDefault
        self.m_CurVal = self.m_Default
        self.m_OnceVal = self.m_Default
        self.m_CurKey = 0
        self.m_CurTime = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Time = { }

    
    def ClearAll(self):
        self.m_Game = None
        self.m_CurVal = self.m_Default
        self.m_OnceVal = self.m_Default
        self.m_CurKey = 0
        self.m_CurTime = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Time = { }

    
    def AddValue(self, sKey, iValue, iTime):
        if iValue > self.m_Default:
            iValue = self.m_Default
        if not iTime:
            self.m_Time[sKey] = 0
            if self.m_OnceVal > iValue:
                self.m_OnceVal = iValue
                self.m_Data[sKey] = iValue
            return None
        self.m_Data[sKey] = iValue
        self.m_Time[sKey] = self.m_Game.GetFrameNum() + iTime
        if iValue < self.m_CurVal:
            self.m_CurVal = iValue
            self.m_CurKey = sKey
            self.m_CurTime = self.m_Time[sKey]
        elif iValue == self.m_CurVal and self.m_Time[sKey] > self.m_CurTime:
            self.m_CurKey = sKey
            self.m_CurTime = self.m_Time[sKey]

    
    def ClearValue(self, sKey):
        if sKey not in self.m_Data:
            return None
        if not self.m_Time[sKey] and self.m_Data[sKey] == self.m_OnceVal:
            self.m_OnceVal = 0
        del self.m_Data[sKey]
        del self.m_Time[sKey]
        if sKey == self.m_CurKey:
            self.m_Refresh = 1

    
    def GetTime(self):
        if self.m_Refresh or self.m_CurTime <= self.m_Game.GetFrameNum():
            self.Refresh()
        iRemain = self.m_CurTime - self.m_Game.GetFrameNum()
        if iRemain < 0:
            return 0
        return iRemain

    
    def GetValue(self):
        if self.m_Refresh or self.m_CurTime <= self.m_Game.GetFrameNum():
            self.Refresh()
        iValue = self.m_OnceVal
        self.m_OnceVal = self.m_Default
        if iValue < self.m_CurVal:
            return iValue
        return self.m_CurVal

    
    def Refresh(self):
        self.m_Refresh = 0
        self.m_CurVal = self.m_Default
        self.m_CurKey = 0
        self.m_CurTime = 0
        dData = self.m_Data
        dTime = self.m_Time
        self.m_Data = { }
        self.m_Time = { }
        iNowTime = self.m_Game.GetFrameNum()
        for sKey, iVal in dData.items():
            iTime = dTime[sKey]
            if iTime < iNowTime:
                continue
            self.m_Data[sKey] = iVal
            self.m_Time[sKey] = iTime
            if iVal < self.m_CurVal:
                self.m_CurVal = iVal
                self.m_CurKey = sKey
                self.m_CurTime = iTime
                continue
            if iVal == self.m_CurVal and self.m_CurTime < iTime:
                self.m_CurKey = sKey
                self.m_CurTime = iTime
        


