# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/fuzzytransition.pyc
# RelativePath: clientlogic/cl_behavior/fsm/fuzzytransition.pyc
# Source Generated with Decompyle++
# File: fuzzytransition.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from . import transition
from .. import meta

class CFuzzyTransition(transition.CTransition):
    CLASS_NAME = 'FuzzyTransition'
    
    def __init__(self):
        super(CFuzzyTransition, self).__init__()
        self.m_Method = None

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CFuzzyTransition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = meta.ParseMethod(dProperties, 'Method', None)

    
    def GetExportData(self):
        dData = {
            'ID': self.m_ID,
            'Class': self.CLASS_NAME,
            'Method': meta.TransMethod(self.m_Method),
            'Flag': 'transition',
            'TargetFSMNodeID': self.m_TargetID }
        return dData


