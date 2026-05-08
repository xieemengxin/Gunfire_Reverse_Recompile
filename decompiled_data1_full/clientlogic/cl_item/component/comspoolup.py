# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/comspoolup.pyc
# RelativePath: clientlogic/cl_item/component/comspoolup.pyc
# Source Generated with Decompyle++
# File: comspoolup.pyc (Python 3.6)

import types
import cl_item.defines as itemdef
from .mobject import CItemComponent

class CSpoolupCompontent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CSpoolupCompontent, self).__init__(oItem, dParser)
        self.m_Action = dParser['Action']
        self.m_AttrChange = { }
        self.m_ChangeFactor = { }
        self.m_SpoolupCnt = 0
        self.m_Listen = 0
        if 'SpoolUp' in self.m_Action and self.m_Action['SpoolUp']:
            oItem.AddAttention(itemdef.MSG_ITEM_FIRE, self.OnFire, 'Spoolup')
            self.m_Listen = 1
        if 'Bullet' in self.m_Action and self.m_Action['Bullet']:
            oItem.AddAttention(itemdef.MSG_ITEM_BULLETMODIFY, self.OnBulletModify, 'Spoolup')
            oItem.AddAttention(itemdef.MSG_ITEM_HOLD, self.OnBulletModify, 'Spoolup')
            self.m_Listen = 1
        if self.m_Listen:
            self.m_Item.AddAttention(itemdef.MSG_ITEM_ADD, self.OnItemAdd, 'SpoolCom')
            self.m_Item.AddAttention(itemdef.MSG_ITEM_REMOVE, self.OnItemRemove, 'SpoolCom')
        self.m_IsInContainer = False

    
    def Release(self):
        if self.m_IsInContainer:
            oItem = self.m_Item
            del oItem.QueryAttr
            del oItem._QueryAttr
        super().Release()

    
    def ResetSpoolupCnt(self):
        self.m_SpoolupCnt = 0
        self.ClearAttrChange('SpoolUp')

    
    def OnItemAdd(self, oItem, oWarrior):
        if self.m_IsInContainer:
            return None
        self.m_IsInContainer = True
        oItem._QueryAttr = oItem.QueryAttr
        oItem.QueryAttr = types.MethodType(QueryAttrSpoolup, oItem)

    
    def OnItemRemove(self, oItem, oWarrior):
        if not self.m_IsInContainer:
            return None
        self.m_IsInContainer = False
        del oItem.QueryAttr
        del oItem._QueryAttr

    
    def OnFire(self, oItem, oOwner):
        self.m_SpoolupCnt += 1
        sKey = 'SpoolUp'
        if sKey not in self.m_Action or self.m_SpoolupCnt not in self.m_Action[sKey]:
            return None
        dAttrChange = self.m_Action[sKey][self.m_SpoolupCnt]
        self.SetAttrChange(sKey, dAttrChange)

    
    def OnBulletModify(self, oItem, oOwner):
        oBulletCom = oItem.GetComponent('Bullet')
        sKey = 'Bullet'
        iBullet = oBulletCom.Bullet()
        if sKey not in self.m_Action:
            return None
        if iBullet not in self.m_Action[sKey]:
            dChange = { }
        else:
            dChange = self.m_Action[sKey][iBullet]
        self.SetAttrChange(sKey, dChange)

    
    def QueryAttrChange(self, sAttr):
        if sAttr not in self.m_AttrChange:
            return None
        return sum(self.m_AttrChange[sAttr].values())

    
    def ClearAttrChange(self, sKey):
        dFactor = self.m_ChangeFactor.pop(sKey, { })
        for sAttr in dFactor:
            dChange = self.m_AttrChange.setdefault(sAttr, { })
            dChange.pop(sKey, 0)
        

    
    def SetAttrChange(self, sKey, dChange):
        self.ClearAttrChange(sKey)
        self.m_ChangeFactor[sKey] = dChange
        for sAttr, iChange in dChange.items():
            dAttrChange = self.m_AttrChange.setdefault(sAttr, { })
            dAttrChange[sKey] = iChange
        



def QueryAttrSpoolup(oItem, sAttr):
    iValue = oItem._QueryAttr(sAttr)
    oComSpoolup = oItem.GetComponent('Spoolup')
    if sAttr in oComSpoolup.m_AttrChange:
        iValue += oComSpoolup.QueryAttrChange(sAttr)
    return iValue

