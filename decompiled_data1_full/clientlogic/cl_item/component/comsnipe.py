# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/comsnipe.pyc
# RelativePath: clientlogic/cl_item/component/comsnipe.pyc
# Source Generated with Decompyle++
# File: comsnipe.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, BASEATTR_CLIENT
from .mobject import CItemComponent
import cl_formula
import cl_object

class CSnipeComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CSnipeComponent, self).__init__(oItem, dParser)
        self.m_InSnipe = False
        self.m_IsSupport = dParser['IsSupport']
        self.m_Shape = dParser['Shape']
        self.m_WarriorAttr = dParser['WarriorAttr']
        self.m_ItemAttr = dParser['ItemAttr']
        for sAttr in ('SnipeFov', 'SnipeTime'):
            iValue = cl_formula.GetFormulaResultByLV(oItem, dParser[sAttr], self.m_Item.m_Grade)
            self.m_Item.m_PrivateAttr[sAttr] = cl_object.baseattr.NewAttr(oItem, sAttr, iValue, BASEATTR_REFRESH | BASEATTR_CLIENT)
        

    
    def IsSupport(self):
        return bool(self.m_IsSupport)

    
    def IsSnipe(self):
        return self.m_InSnipe

    
    def Snipe(self):
        if self.m_InSnipe:
            return None
        self.m_InSnipe = True
        oOwner = self.m_Item.GetOwner()
        self._AttrEnable(oOwner)

    
    def UnSnipe(self):
        if not self.m_InSnipe:
            return None
        self.m_InSnipe = False
        oOwner = self.m_Item.GetOwner()
        self._AttrDisable(oOwner)

    
    def GetSnipeShape(self):
        return self.m_Shape

    
    def GetWarriorAttr(self):
        return self.m_WarriorAttr

    
    def _AttrEnable(self, oOwner):
        oItem = self.m_Item
        sKey = self.m_Key
        for sAttr, (iAdd, iMul) in self.m_WarriorAttr.items():
            oOwner.AttrChange(sAttr, iMul, iAdd, sKey)
        
        for sAttr, (iAdd, iMul) in self.m_ItemAttr.items():
            oItem.AttrChange(sAttr, iMul, iAdd, sKey)
        

    
    def _AttrDisable(self, oOwner):
        oItem = self.m_Item
        sKey = self.m_Key
        for sAttr in self.m_WarriorAttr:
            oOwner.AttrClear(sAttr, sKey)
        
        for sAttr in self.m_ItemAttr:
            oItem.AttrClear(sAttr, sKey)
        


