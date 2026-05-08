# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/fsm.pyc
# RelativePath: clientlogic/cl_behavior/fsm/fsm.pyc
# Source Generated with Decompyle++
# File: fsm.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from .. import behaviortree
from .. import behaviortreetask
from .. import meta
from . import fsmstate

class CFsm(behaviortree.CBehaviorNode):
    CLASS_NAME = 'FSM'
    
    def __init__(self):
        super(CFsm, self).__init__()
        self.m_InitialID = -1

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CFsm, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_InitialID = meta.ParseProperty(dProperties, 'InitialID', -1)

    
    def AddChild(self, oChild):
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def CreateTask(self):
        return CFsmTask()

    
    def GetInitialID(self):
        return self.m_InitialID

    
    def SetInitialID(self, iInitialID):
        self.m_InitialID = iInitialID

    
    def GetExportData(self):
        dData = super(CFsm, self).GetExportData()
        dData.update({
            'InitialID': self.m_InitialID })
        return dData



class CFsmTask(behaviortreetask.CCompositeTask):
    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = 0
        self.m_CurrentNodeId = self.m_Node.GetInitialID()
        return True

    
    def OnExit(self, oAgent, iChildStatus):
        self.m_CurrentNodeId = -1
        super(CFsmTask, self).OnExit(oAgent, iChildStatus)

    
    def UpdateFSM(self, oAgent, iChildStatus):
        for _ in range(10):
            oTask = self.GetChildById(self.m_CurrentNodeId)
            oTask.Exec(oAgent)
            if isinstance(oTask, fsmstate.CStateTask) and oTask.IsEndState():
                return defines.BT_SUCCESS
            iNextStateID = oTask.GetNextStateID()
            if iNextStateID < 0:
                break
            self.m_CurrentNodeId = iNextStateID
            self.m_CurrentTask = self.GetChildById(self.m_CurrentNodeId)
        
        return iChildStatus

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        return self.UpdateFSM(oAgent, iChildStatus)

    
    def Update(self, oAgent, iChildStatus):
        return self.UpdateFSM(oAgent, iChildStatus)


