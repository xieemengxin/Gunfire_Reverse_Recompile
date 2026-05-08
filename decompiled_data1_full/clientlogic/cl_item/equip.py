# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/equip.pyc
# RelativePath: clientlogic/cl_item/equip.pyc
# Source Generated with Decompyle++
# File: equip.pyc (Python 3.6)

from cl_only import RaiseError
from cl_item.baseitem import CBaseItem
import cl_item.defines as itemdef

class CEquip(CBaseItem):
    m_Type = itemdef.ITEM_TYPE_NONE
    
    def GetTargetContainer(self, oHero):
        return [
            oHero.m_WieldCon]

    
    def PutToContainer(self, lstCon, sReason):
        if not self.m_ID:
            RaiseError('Equip PutContainer NoTemp %s' % sReason)
            return 0
        for oContainer in lstCon:
            iPos = oContainer.AddItem(self)
            if iPos:
                return iPos
        
        return 0


