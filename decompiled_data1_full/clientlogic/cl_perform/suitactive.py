# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/suitactive.pyc
# RelativePath: clientlogic/cl_perform/suitactive.pyc
# Source Generated with Decompyle++
# File: suitactive.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_NORMAL, PF_TYPE_SUITACTIVE, PF_SUBMSG_SUITACTIVE, SUIT_PERFORM_POS_NOTCONTROL, THUNDERSTEP_CONDUCT_DAMAGE
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype

class CPerform(CCustomPerform):
    m_Name = '套装主动'
    m_PFType = PF_TYPE_SUITACTIVE
    m_SubMsg = PF_SUBMSG_SUITACTIVE
    m_ElementType = DAM_TYPE_NORMAL
    m_UnCrtByOwnerSign = 1
    m_Pos = SUIT_PERFORM_POS_NOTCONTROL
    
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

    
    def GetPerformPos(self):
        return self.m_Pos

    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['ExShowTips'] = THUNDERSTEP_CONDUCT_DAMAGE
        super().UsePerform(oWarrior, oSkill)


