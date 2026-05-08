# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/rareitem.pyc
# RelativePath: clientlogic/cl_item/rareitem.pyc
# Source Generated with Decompyle++
# File: rareitem.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
import cl_item.defines as itemdef
import cl_drop
import cllib.lib_flag

class CRareItem(CBaseItem):
    m_Type = itemdef.ITEM_TYPE_NONE
    m_UseNotify = 0
    m_UseAction = None
    
    def GetTargetContainer(self, oHero):
        return [
            oHero.m_ItemCon]

    
    def PutToContainer(self, lstCon, sReason):
        for oItemCon in lstCon:
            iPos = oItemCon.AddItem(self)
            if iPos:
                return iPos
        
        return 0

    
    def OnAddToContainer(self):
        super(CRareItem, self).OnAddToContainer()
        lstRareItem = self.m_Container.GetAllItemByType(self.m_Type)
        lstRareItem.remove(self)
        oOwner = self.m_Container.m_Game.GetObject(self.m_Container.m_Owner)
        sReason = 'AddItem:%d-%d' % (self.Type(), self.m_SID)
        for oOldRareItem in lstRareItem:
            self.m_Container.RemoveItem(oOldRareItem, sReason)
            if not cllib.lib_flag.g_IsMobileRun:
                cl_drop.DropItem(oOwner, oOldRareItem, True)
        


