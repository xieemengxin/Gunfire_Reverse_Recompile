# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/attachments/precondition.pyc
# RelativePath: clientlogic/cl_behavior/attachments/precondition.pyc
# Source Generated with Decompyle++
# File: precondition.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from . import attachaction
from .. import meta

class CPrecondition(attachaction.CAttachAction):
    CLASS_NAME = 'Precondition'
    
    def __init__(self):
        super(CPrecondition, self).__init__()
        self.m_Phase = defines.E_ENTER
        self.m_IsAnd = True

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CPrecondition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Phase = meta.ParseProperty(dProperties, 'Phase', defines.E_ENTER)
        self.m_IsAnd = meta.ParseProperty(dProperties, 'BinaryOperator', 'And') == 'And'

    
    def GetPhase(self):
        return self.m_Phase

    
    def IsAnd(self):
        return self.m_IsAnd

    
    def GetExportData(self):
        dData = super(CPrecondition, self).GetExportData()
        dData.update({
            'Phase': self.m_Phase,
            'Flag': 'precondition',
            'BinaryOperator': 'And' if self.m_IsAnd else 'Or' })
        return dData


