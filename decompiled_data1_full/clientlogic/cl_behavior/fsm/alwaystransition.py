# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/alwaystransition.pyc
# RelativePath: clientlogic/cl_behavior/fsm/alwaystransition.pyc
# Source Generated with Decompyle++
# File: alwaystransition.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from . import transition
from .. import behaviortreetask
from .. import meta

class CAlwaysTransition(transition.CTransition):
    CLASS_NAME = 'AlwaysTransition'
    
    def __init__(self):
        super(CAlwaysTransition, self).__init__()
        self.m_TransitionPhase = defines.ETP_ALWAYS

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CAlwaysTransition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_TransitionPhase = meta.ParseProperty(dProperties, 'TransitionPhase', -1)

    
    def GetExportData(self):
        dData = {
            'ID': self.m_ID,
            'Class': self.CLASS_NAME,
            'TransitionPhase': self.m_TransitionPhase,
            'Flag': 'transition',
            'TargetFSMNodeID': self.m_TargetID }
        return dData

    
    def Evaluate(self, oAgent, iChildStatus = None):
        if iChildStatus is None:
            return super(CAlwaysTransition, self).Evaluate(oAgent)
        if self.m_TransitionPhase == defines.ETP_ALWAYS:
            return True
        if iChildStatus == defines.BT_SUCCESS:
            if self.m_TransitionPhase == defines.ETP_SUCCESS or self.m_TransitionPhase == defines.ETP_EXIT:
                return True
        if iChildStatus == defines.BT_FAILURE:
            if self.m_TransitionPhase == defines.ETP_FAILURE or self.m_TransitionPhase == defines.ETP_EXIT:
                return True
        return False


