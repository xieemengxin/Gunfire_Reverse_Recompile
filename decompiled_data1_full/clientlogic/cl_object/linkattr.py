# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/linkattr.pyc
# RelativePath: clientlogic/cl_object/linkattr.pyc
# Source Generated with Decompyle++
# File: linkattr.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH
from cl_only import Functor, WeakProxy

class CLinkAttr(object):
    m_Type = 'Link'
    
    def __init__(self):
        self.m_BaseAttrDict = { }
        self.m_ReGetValueNotRefreshFunc = { }
        self.m_ReRefreshClientFunc = { }
        self.m_ReFlag = { }
        self.m_Refresh = 0
        self.m_MaxValue = 0
        self.m_LinkMul = 10000

    
    def AddLink(self, iItem, oBaseAttr):
        self.m_BaseAttrDict[iItem] = oBaseAttr
        self.m_ReGetValueNotRefreshFunc[iItem] = oBaseAttr.GetValueNotRefresh
        self.m_ReRefreshClientFunc[iItem] = oBaseAttr.RefreshClient
        self.m_ReFlag[iItem] = oBaseAttr.m_Flag
        oBaseAttr.GetValueNotRefresh = Functor(BindGetValueNotRefresh, WeakProxy(self))
        oBaseAttr.RefreshClient = Functor(BindRefreshClient, WeakProxy(self))
        oBaseAttr.m_Flag |= BASEATTR_REFRESH

    
    def DelLink(self, iItem):
        if iItem not in self.m_BaseAttrDict:
            return None
        oBaseAttr = self.m_BaseAttrDict.pop(iItem)
        self.m_ReGetValueNotRefreshFunc.pop(iItem)
        self.m_ReRefreshClientFunc.pop(iItem)
        del oBaseAttr.GetValueNotRefresh
        del oBaseAttr.RefreshClient
        oBaseAttr.m_Flag = self.m_ReFlag.pop(iItem)
        return oBaseAttr

    
    def GetLink(self, iItem):
        if iItem not in self.m_BaseAttrDict:
            return None
        return self.m_BaseAttrDict[iItem]

    
    def __getattr__(self, attr):
        return Functor(self.AdaptToBaseAttr, attr)

    
    def AdaptToBaseAttr(self, attr, obj, *args, **kwargs):
        if not obj or obj.m_ID not in self.m_BaseAttrDict:
            return None
        oBaseAttr = self.m_BaseAttrDict[obj.m_ID]
        getattr(oBaseAttr, attr)(obj, *args, **kwargs)

    
    def ClearAll(self):
        for oBaseAttr in self.m_BaseAttrDict.values():
            oBaseAttr.ClearAll()
        
        lstOwner = list(self.m_BaseAttrDict.keys())
        for iItem in lstOwner:
            self.DelLink(iItem)
        

    
    def GetValue(self, obj):
        return self.GetValueNotRefresh(obj)

    
    def GetValueNotRefresh(self, obj = None):
        fTotalValue = self.GetTotalValue(obj)
        if self.m_MaxValue and fTotalValue > self.m_MaxValue:
            return self.m_MaxValue
        return fTotalValue

    
    def GetTotalValue(self, obj):
        if obj and obj.m_ID in self.m_BaseAttrDict:
            oBaseAttr = self.m_BaseAttrDict[obj.m_ID]
            if oBaseAttr.m_IgnoreLinkInfo:
                funcGetValue = self.m_ReGetValueNotRefreshFunc[obj.m_ID]
                return funcGetValue(obj)
        fTotalValue = 0
        for funcGetValue in self.m_ReGetValueNotRefreshFunc.values():
            fTotalValue += funcGetValue(obj)
        
        fTotalValue = fTotalValue * self.m_LinkMul // 10000
        return fTotalValue

    
    def RefreshClient(self, obj):
        if not obj or obj.m_ID not in self.m_BaseAttrDict:
            return None
        oContainer = obj.m_Container
        for iWeapon, funcRefresh in self.m_ReRefreshClientFunc.items():
            oWeapon = oContainer.GetItemByID(iWeapon)
            funcRefresh(oWeapon)
        

    
    def GetKeyFactorInfo(self, sKey):
        return (0, 0)

    
    def HasFactor(self, sKey):
        return 0

    
    def SetMaxValue(self, fValue):
        self.m_MaxValue = fValue

    
    def GetOverFlowValue(self, obj):
        if not self.m_MaxValue:
            return 0
        fTotalValue = self.GetTotalValue(obj)
        if fTotalValue <= self.m_MaxValue:
            return 0
        return fTotalValue - self.m_MaxValue

    
    def SetLinkMul(self, iMul):
        self.m_LinkMul = iMul

    
    def GetChangeValue(self, obj):
        iItem = obj.m_ID
        if iItem not in self.m_ReGetValueNotRefreshFunc:
            return 0
        fTotalValue = self.GetValueNotRefresh(obj)
        funcGetValue = self.m_ReGetValueNotRefreshFunc[iItem]
        return fTotalValue - funcGetValue(obj)



class CLinkPFAttr(CLinkAttr):
    
    def __init__(self):
        super().__init__()
        self.m_LinkPerform = { }

    
    def RefreshClient(self, oPerform):
        if not oPerform or oPerform.m_ID not in self.m_LinkPerform:
            return None
        oOwner = oPerform.GetOwner()
        for iPerformID, funcRefresh in self.m_ReRefreshClientFunc.items():
            (iItemID, iPerformSID) = self.m_LinkPerform[iPerformID]
            oPerform = oOwner.GetPerform(iPerformSID, iItemID)
            funcRefresh(oPerform)
        

    
    def AddLink(self, iPerformID, oBaseAttr, tKey):
        super().AddLink(iPerformID, oBaseAttr)
        self.m_LinkPerform[iPerformID] = tKey

    
    def DelLink(self, iPerformID):
        self.m_LinkPerform.pop(iPerformID, 0)
        return super().DelLink(iPerformID)



def BindGetValueNotRefresh(oLinkAttr, obj):
    return oLinkAttr.GetValueNotRefresh(obj)


def BindRefreshClient(oLinkAttr, obj):
    oLinkAttr.RefreshClient(obj)

