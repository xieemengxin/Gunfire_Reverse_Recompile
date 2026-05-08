# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/keyitem.pyc
# RelativePath: clientlogic/cl_item/keyitem.pyc
# Source Generated with Decompyle++
# File: keyitem.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
from cl_object.logging import WarobjLog
import cl_item.defines as itemdef

class CKeyItem(CBaseItem):
    m_Type = itemdef.ITEM_TYPE_NONE
    
    def AddToContainer(self, oContainer):
        super().AddToContainer(oContainer)
        if self.m_Owner:
            WarobjLog.Debug('%d %d add keyitem %d' % (self.m_Game.m_ID, self.GetOwner().m_PlayerID, self.m_ID))

    
    def RemoveFromContainer(self, sReason = ''):
        if self.m_Owner:
            WarobjLog.Debug('%d %d remove keyitem %d %s' % (self.m_Game.m_ID, self.GetOwner().m_PlayerID, self.m_ID, sReason))
        super().RemoveFromContainer(sReason)

    
    def GetTargetContainer(self, oHero):
        return [
            oHero.m_ItemCon]


