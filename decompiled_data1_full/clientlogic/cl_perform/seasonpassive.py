# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/seasonpassive.pyc
# RelativePath: clientlogic/cl_perform/seasonpassive.pyc
# Source Generated with Decompyle++
# File: seasonpassive.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_SEASONPASSIVE

class CSeasonPassive(CPerform):
    m_PFType = PF_TYPE_SEASONPASSIVE
    
    def GetMyItem(self):
        oOwner = self.GetOwner()
        iItem = self.m_Item
        if oOwner and iItem:
            oSeasonCon = oOwner.m_SeasonCon
            if oSeasonCon:
                return oSeasonCon.GetItemByID(iItem)


