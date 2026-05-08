# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/comhold.pyc
# RelativePath: clientlogic/cl_item/component/comhold.pyc
# Source Generated with Decompyle++
# File: comhold.pyc (Python 3.6)

import cl_item.defines as itemdef
import cl_object
import cl_object.lifecycle
import cl_msgcenter
from .mobject import CItemComponent
from cl_cscommondef import WEAPON_HOLD

class CHoldComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CHoldComponent, self).__init__(oItem, dParser)
        self.m_OnHold = 0
        self.m_WarriorAttr = dParser['WarriorAttr']
        self.m_HoldAction = dParser['HoldAction']
        self.m_LifeCycle = cl_object.lifecycle.CLifeCycle()
        self.m_LifeCycle.Init(oItem, self.m_HoldAction, None)
        oItem.AddAttention(itemdef.MSG_ITEM_REMOVE, ItemRemoveUnHold, 'RemoveUnhold')

    
    def Release(self):
        self.m_LifeCycle.Release()
        self.m_LifeCycle = None
        super().Release()

    
    def HoldPos(self):
        return self.m_OnHold

    
    def IsHold(self):
        return self.m_OnHold != 0

    
    def Hold(self, iHoldPos):
        self.m_OnHold = iHoldPos
        oOwner = self.m_Item.GetOwner()
        self.m_LifeCycle.Enable(oOwner)
        self.m_Item.SendMsg(itemdef.MSG_ITEM_HOLD)
        self._AttrEnable(oOwner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_WEAPON, oOwner, {
            'ItemType': self.m_Item.m_Type,
            'HoldType': iHoldPos,
            'ItemID': self.m_Item.m_ID,
            'ItemSID': self.m_Item.m_SID })

    
    def Unhold(self):
        if not self.m_OnHold:
            return None
        oOwner = self.m_Item.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, oOwner, {
            'ItemID': self.m_Item.m_ID,
            'HoldType': self.m_OnHold }, iSub = self.m_OnHold)
        self.m_LifeCycle.Disable(oOwner)
        oOwner.SwitchSnipe(0)
        self.m_OnHold = 0
        self.m_Item.SendMsg(itemdef.MSG_ITEM_UNHOLD)
        self._AttrDisable(oOwner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, oOwner, {
            'ItemID': self.m_Item.m_ID,
            'Weapon': self.m_Item.m_ID,
            'oItem': self.m_Item })
        self.m_Item.ClearAllForbid()

    
    def GetWarriorAttr(self):
        return self.m_WarriorAttr

    
    def _AttrEnable(self, oOwner):
        sKey = self.m_Key
        for sAttr, (iAdd, iMul) in self.m_WarriorAttr.items():
            if not oOwner.CheckIgnoreAttrChange(WEAPON_HOLD, sAttr, iAdd, iMul):
                oOwner.AttrChange(sAttr, iMul, iAdd, sKey)
        

    
    def _AttrDisable(self, oOwner):
        sKey = self.m_Key
        for sAttr in self.m_WarriorAttr:
            oOwner.AttrClear(sAttr, sKey)
        

    
    def AttrCache(self):
        return {
            'HoldType': self.m_OnHold }



def ItemRemoveUnHold(oItem, oOwner):
    oItem.GetComponent('Hold').Unhold()

