# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/task.pyc
# RelativePath: clientlogic/cl_behavior/nodes/task.pyc
# Source Generated with Decompyle++
# File: task.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from .. import behaviortree
from .. import behaviortreetask
from .. import meta

class CTask(behaviortree.CDecoratorNode):
    CLASS_NAME = 'Task'
    
    def __init__(self):
        super(CTask, self).__init__()
        self.m_Task = None

    
    def CreateTask(self):
        return CTaskTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CTask, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Task = meta.ParseMethod(dProperties, 'Prototype', None)



class CTaskTask(behaviortreetask.CCompositeTask):
    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = -1
        return super(CTaskTask, self).OnEnter(oAgent)

    
    def Update(self, oAgent, iChildStatus):
        iStatus = iChildStatus
        if iChildStatus == defines.BT_RUNNING:
            iStatus = self.m_Children[0].Exec(oAgent)
        return iStatus


