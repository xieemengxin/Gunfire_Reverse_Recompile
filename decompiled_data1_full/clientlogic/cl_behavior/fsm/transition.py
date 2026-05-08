# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/transition.pyc
# RelativePath: clientlogic/cl_behavior/fsm/transition.pyc
# Source Generated with Decompyle++
# File: transition.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from . import startcondition
from .. import behaviortreetask
from .. import meta

class CTransition(startcondition.CStartCondition):
    CLASS_NAME = 'Transition'
    
    def __init__(self):
        super(CTransition, self).__init__()
        self.m_Opl = None
        self.m_Opr = None
        self.m_Operator = defines.E_EQUAL
        self.m_TransitionPhase = defines.ETP_ALWAYS

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CTransition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_TransitionPhase = meta.ParseProperty(dProperties, 'TransitionPhase', defines.ETP_ALWAYS)

    
    def GetExportData(self):
        dData = super(CTransition, self).GetExportData()
        dData.update({
            'Flag': 'transition',
            'Method': meta.TransMethod3(self.m_Opl, self.m_Operator, self.m_Opr),
            'TransitionPhase': self.m_TransitionPhase })
        return dData

    
    def Evaluate(self, oAgent, iChildStatus = None):
        bResult = super(CTransition, self).Evaluate(oAgent, iChildStatus)
        if iChildStatus is None:
            return bResult
        if self.m_TransitionPhase == defines.ETP_ALWAYS:
            return bResult
        if iChildStatus == defines.BT_SUCCESS:
            if self.m_TransitionPhase == defines.ETP_SUCCESS or self.m_TransitionPhase == defines.ETP_EXIT:
                return bResult
        if iChildStatus == defines.BT_FAILURE:
            if self.m_TransitionPhase == defines.ETP_FAILURE or self.m_TransitionPhase == defines.ETP_EXIT:
                return bResult
        return False


