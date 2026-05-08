# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/context.pyc
# RelativePath: clientlogic/cl_behavior/context.pyc
# Source Generated with Decompyle++
# File: context.pyc (Python 3.6)

from __future__ import absolute_import

class CContext(object):
    
    def __init__(self, iContextID):
        self.m_ContextID = iContextID
        self.m_IsExecuting = False
        self.m_DelayAddedAgents = []
        self.m_DelayRemovedAgents = []
        self.m_Agents = []

    
    def Clear(self):
        lstAgent = self.m_Agents
        self.m_Agents = []
        for oAgent in lstAgent:
            oAgent.Release()
        

    
    def ExecAgents(self, oGameSpace):
        if not oGameSpace.m_bIsExecAgents:
            return None
        self.m_IsExecuting = True
        for oAgent in self.m_Agents:
            if oAgent.IsActive():
                oAgent.BTExec()
            if not oGameSpace.m_bIsExecAgents:
                break
        
        self.m_IsExecuting = False
        self.DelayProcessingAgents()

    
    def DelayProcessingAgents(self):
        for oAgent in self.m_DelayAddedAgents:
            self._AddAgent(oAgent)
        
        self.m_DelayAddedAgents = []
        for oAgent in self.m_DelayRemovedAgents:
            self._RemoveAgent(oAgent)
        
        self.m_DelayRemovedAgents = []

    
    def AddAgent(self, oAgent):
        oAgent.m_ContextID = self.m_ContextID
        if self.m_IsExecuting:
            self.m_DelayAddedAgents.append(oAgent)
        else:
            self._AddAgent(oAgent)

    
    def RemoveAgent(self, oAgent):
        if self.m_IsExecuting:
            self.m_DelayRemovedAgents.append(oAgent)
        else:
            self._RemoveAgent(oAgent)

    
    def _AddAgent(self, oAgent):
        if oAgent in self.m_Agents:
            return None
        self.m_Agents.append(oAgent)
        self.m_Agents.sort(key = (lambda o: o.GetPriority()))

    
    def _RemoveAgent(self, oAgent):
        if oAgent not in self.m_Agents:
            return None
        self.m_Agents.remove(oAgent)


