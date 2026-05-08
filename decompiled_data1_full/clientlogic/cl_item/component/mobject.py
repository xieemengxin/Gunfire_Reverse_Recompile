# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/mobject.pyc
# RelativePath: clientlogic/cl_item/component/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import WeakProxy

class CItemComponent(object):
    
    def __init__(self, oItem, dParser):
        self.m_Item = WeakProxy(oItem)
        self.m_Key = '%s-%s' % (oItem.Key(), self.__class__.__name__[1:])

    
    def Release(self):
        self.m_Item = None

    
    def Save(self):
        return { }

    
    def Load(self, dData):
        pass

    
    def Refresh(self):
        pass

    
    def TraceName(self):
        return ''

    
    def AttrChange(self, sAttr, iMul, iAdd, sKey, iRefresh = 1):
        self.m_Item.AttrChange(sAttr, iMul, iAdd, sKey, iRefresh)

    
    def AttrClear(self, sAttr, sKey, iRefresh = 1):
        self.m_Item.AttrClear(sAttr, sKey, iRefresh)

    
    def GetItemAttr(self, sAttr):
        return self.m_Item.GetItemAttr(sAttr)

    
    def QueryAttr(self, sAttr):
        return self.m_Item.QueryAttr(sAttr)

    
    def RefreshAttr(self, sAttr, iCurValue):
        self.m_Item.RefreshAttr(sAttr, iCurValue)

    
    def AttrCache(self):
        return { }


