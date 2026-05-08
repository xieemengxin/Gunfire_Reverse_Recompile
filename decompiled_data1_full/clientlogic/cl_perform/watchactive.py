# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/watchactive.pyc
# RelativePath: clientlogic/cl_perform/watchactive.pyc
# Source Generated with Decompyle++
# File: watchactive.pyc (Python 3.6)

from cl_perform.mobject import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_WATCHACTIVE, PF_SUBMSG_WATCHACTIVE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_Name = '观战主动'
    m_PFType = PF_TYPE_WATCHACTIVE
    m_SubMsg = PF_SUBMSG_WATCHACTIVE
    m_ElementType = DAM_TYPE_NORMAL
    
    def CanUse(self, oWarrior, dInfo):
        if not oWarrior.IsRealDied():
            return 0
        dInfo['IgnoreDie'] = 1
        return super().CanUse(oWarrior, dInfo)

    
    def AttrCache(self):
        dData = super(CPerform, self).AttrCache()
        dData['ElementType'] = self.m_ElementType
        return dData


