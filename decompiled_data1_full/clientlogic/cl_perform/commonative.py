# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/commonative.pyc
# RelativePath: clientlogic/cl_perform/commonative.pyc
# Source Generated with Decompyle++
# File: commonative.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_NORMAL, PF_TYPE_COMMON, PF_SUBMSG_COMMON
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype

class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_COMMON
    m_SubMsg = PF_SUBMSG_COMMON
    m_ElementType = DAM_TYPE_NORMAL
    m_UnCrtByOwnerSign = 1
    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        for sAttr, iValue in self.m_BaseArgData.items():
            dData[sAttr] = iValue
        
        dData['ArgData'] = { }
        for sAttr, iValue in self.m_ArgData.items():
            dData['ArgData'][sAttr] = iValue
        
        dData['ElementType'] = self.m_ElementType
        return dData


