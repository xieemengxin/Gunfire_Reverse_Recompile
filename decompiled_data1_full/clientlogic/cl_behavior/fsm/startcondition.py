# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/startcondition.pyc
# RelativePath: clientlogic/cl_behavior/fsm/startcondition.pyc
# Source Generated with Decompyle++
# File: startcondition.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from ..attachments import precondition
from .. import behaviortreetask
from .. import meta

class CStartCondition(precondition.CPrecondition):
    CLASS_NAME = 'StartCondition'
    
    def __init__(self):
        super(CStartCondition, self).__init__()
        self.m_TargetID = -1

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        lstEffectorsFunc = meta.ParseProperty(dProperties, 'EffectorsFunc', [])
        self.m_Effectors.extend(lstEffectorsFunc)
        super(CStartCondition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_TargetID = meta.ParseProperty(dProperties, 'TargetFSMNodeID', -1)

    
    def SetTargetStateID(self, iID):
        self.m_TargetID = iID

    
    def GetTargetStateID(self):
        return self.m_TargetID

    
    def ApplyEffects(self, oAgent, iPhase):
        for func in self.m_Effectors:
            func(oAgent)
        

    
    def GetExportData(self):
        dData = super(CStartCondition, self).GetExportData()
        dData.update({
            'EffectorsFunc': self.m_Effectors,
            'TargetFSMNodeID': self.m_TargetID,
            'Flag': 'startcondition' })
        return dData


