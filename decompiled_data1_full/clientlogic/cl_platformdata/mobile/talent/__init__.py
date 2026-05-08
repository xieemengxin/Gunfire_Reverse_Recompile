# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_TALENT

class CTalent(CPerform):
    m_MaxUpgradeTimes = 0
    m_MaxLevel = 1
    m_Career = None
    m_PFType = PF_TYPE_TALENT
    
    def __init__(self, oOwner, iLevel):
        super(CTalent, self).__init__(oOwner, iLevel)
        self.m_Pos = 0

    
    def GetMaxUpgradeLevel(cls):
        return cls.m_MaxUpgradeTimes + 1

    GetMaxUpgradeLevel = classmethod(GetMaxUpgradeLevel)

