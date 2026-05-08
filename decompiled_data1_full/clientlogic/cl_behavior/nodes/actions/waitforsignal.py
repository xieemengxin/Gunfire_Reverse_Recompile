# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/actions/waitforsignal.pyc
# RelativePath: clientlogic/cl_behavior/nodes/actions/waitforsignal.pyc
# Source Generated with Decompyle++
# File: waitforsignal.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ... import workspace

class CWaitforSignal(behaviortree.CBehaviorNode):
    CLASS_NAME = 'WaitforSignal'
    
    def CreateTask(self):
        return CWaitforSignalTask()

    
    def CheckIfSignaled(self, oAgent):
        return self.EvaluateCustomCondition(oAgent)



class CWaitforSignalTask(behaviortreetask.CSingeChildTask):
    
    def __init__(self):
        super(CWaitforSignalTask, self).__init__()
        self.m_bTriggered = False

    
    def Load(self, oIONode):
        super(CWaitforSignalTask, self).Load(oIONode)
        if self.m_Status != defines.BT_INVALID:
            pass

    
    def OnEnter(self, oAgent):
        self.m_bTriggered = False
        return True

    
    def Update(self, oAgent, iChildStatus):
        if iChildStatus != defines.BT_RUNNING:
            return iChildStatus
        if not self.m_bTriggered:
            oNode = self.GetNode()
            self.m_bTriggered = oNode.CheckIfSignaled(oAgent)
        if self.m_bTriggered:
            if not self.m_Root:
                return defines.BT_SUCCESS
            return super(CWaitforSignalTask, self).Update(oAgent, iChildStatus)
        return defines.BT_RUNNING


