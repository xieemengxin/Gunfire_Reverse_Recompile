# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/actions/assignment.pyc
# RelativePath: clientlogic/cl_behavior/nodes/actions/assignment.pyc
# Source Generated with Decompyle++
# File: assignment.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CAssignment(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Assignment'
    
    def __init__(self):
        super(CAssignment, self).__init__()
        self.m_Opl = None
        self.m_Opr = None
        self.m_bCast = False

    
    def CreateTask(self):
        return CAssignmentTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CAssignment, self).LoadProperties(iVersion, sAgentType, dProperties)
        valCast = dProperties['CastRight']
        valOpl = dProperties['Opl']
        valOpr = dProperties['Opr']
        self.m_bCast = valCast == 'true'



class CAssignmentTask(behaviortreetask.CLeafTask):
    
    def Update(self, oAgent, iChildStatus):
        oAssignmentNode = self.GetNode()
        iResult = defines.BT_SUCCESS
        if oAssignmentNode.m_Opl:
            oAssignmentNode.m_Opl.SetValueCast(oAgent, oAssignmentNode.m_Opr, oAssignmentNode.m_bCast)
        else:
            iResult = oAssignmentNode.UpdateImpl(oAgent, iChildStatus)
        return iResult


