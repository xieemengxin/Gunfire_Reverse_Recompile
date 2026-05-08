# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsterpf.pyc
# RelativePath: clientlogic/cl_perform/monsterpf.pyc
# Source Generated with Decompyle++
# File: monsterpf.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_MONSTERACT, DAM_TYPE_NORMAL, FORBID_MONSTERPF, NONE_DISTANCE, MONSTERPF_TYPE_ATTACK
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype

class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_MONSTERACT
    m_CheckForbid = FORBID_MONSTERPF
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 0
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_CacheAttr = []
    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def AttrCache(self):
        dData = super(CPerform, self).AttrCache()
        for sKey in self.m_CacheAttr:
            dData[sKey] = self.CalAttr(sKey)
        
        dData['ElementType'] = self.m_ElementType
        return dData


