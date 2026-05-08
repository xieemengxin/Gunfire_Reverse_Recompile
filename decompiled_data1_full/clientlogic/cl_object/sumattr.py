# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/sumattr.pyc
# RelativePath: clientlogic/cl_object/sumattr.pyc
# Source Generated with Decompyle++
# File: sumattr.pyc (Python 3.6)


class CSumAttr(object):
    m_JoinAttrCache = False
    
    def __init__(self, sAttr, bClient = 0):
        self.m_Attr = sAttr
        self.m_Client = bClient
        self.m_CurValue = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Order = []

    
    def ClearAll(self):
        self.m_CurValue = 0
        self.m_Refresh = 0
        self.m_Data = { }
        self.m_Order = []

    
    def ClearKeyValue(self, oWarrior, sKey):
        if sKey not in self.m_Data:
            return None
        self.m_CurValue -= self.m_Data[sKey]
        del self.m_Data[sKey]
        self.m_Order.remove(sKey)

    
    def AddValue(self, oWarrior, sKey, iValue):
        self.ClearKeyValue(oWarrior, sKey)
        self.m_Data[sKey] = iValue
        self.m_Order.append(sKey)
        self.m_CurValue += iValue
        if self.m_Client:
            oWarrior.GS2CPropChange(self.m_Attr)

    
    def UpdateValue(self, oWarrior, sKey, iValue):
        if sKey not in self.m_Data:
            self.m_Data[sKey] = 0
            self.m_Order.append(sKey)
        if iValue > 0:
            iOldValue = self.m_Data[sKey]
            self.m_Data[sKey] = iValue
            self.m_CurValue += iValue - iOldValue
        elif self.m_Data[sKey] + iValue > 0:
            self.m_Data[sKey] += iValue
            self.m_CurValue += iValue
        else:
            self.m_CurValue -= self.m_Data[sKey]
            self.m_Data[sKey] = 0
            self.ClearValue(oWarrior, sKey, 0)
        if self.m_Client:
            oWarrior.GS2CPropChange(self.m_Attr)

    
    def ClearValue(self, oWarrior, sKey, iRefresh = 1):
        if sKey not in self.m_Data:
            return None
        self.m_CurValue -= self.m_Data[sKey]
        del self.m_Data[sKey]
        self.m_Order.remove(sKey)
        if iRefresh and self.m_Client:
            oWarrior.GS2CPropChange(self.m_Attr)
        if sKey[:2] == 'ST':
            iState = int(sKey.split('-')[-1])
            oWarrior.m_State.RemoveItem(iState)

    
    def SubValue(self, oWarrior, iValue):
        lstRemove = []
        for sKey in self.m_Order:
            if iValue < self.m_Data[sKey]:
                self.m_Data[sKey] -= iValue
                self.m_CurValue -= iValue
                if sKey[:2] == 'ST':
                    self.CheckStateTips(oWarrior, sKey)
                break
            if iValue == self.m_Data[sKey]:
                self.m_CurValue -= self.m_Data[sKey]
                self.m_Data[sKey] = 0
                lstRemove.append(sKey)
                break
            self.m_CurValue -= self.m_Data[sKey]
            iValue -= self.m_Data[sKey]
            self.m_Data[sKey] = 0
            lstRemove.append(sKey)
        
        for sKey in lstRemove:
            self.ClearValue(oWarrior, sKey, 0)
        
        if self.m_Client:
            oWarrior.GS2CPropChange(self.m_Attr)

    
    def GetValue(self):
        return self.m_CurValue

    
    def CheckStateTips(self, oHero, sKey):
        pass

    
    def GetValueByKey(self, sKey):
        if sKey not in self.m_Data:
            return 0
        return self.m_Data[sKey]


