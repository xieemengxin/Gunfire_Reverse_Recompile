# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/attachments/effector.pyc
# RelativePath: clientlogic/cl_behavior/attachments/effector.pyc
# Source Generated with Decompyle++
# File: effector.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from . import attachaction
from .. import meta

class CEffector(attachaction.CAttachAction):
    CLASS_NAME = 'Effector'
    
    def __init__(self):
        super(CEffector, self).__init__()
        self.m_Phase = defines.E_SUCCESS

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CEffector, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Phase = meta.ParseProperty(dProperties, 'Phase', defines.E_SUCCESS)

    
    def GetPhase(self):
        return self.m_Phase

    
    def GetExportData(self):
        dData = super(CEffector, self).GetExportData()
        dData.update({
            'Phase': self.m_Phase,
            'Flag': 'effector' })
        return dData


