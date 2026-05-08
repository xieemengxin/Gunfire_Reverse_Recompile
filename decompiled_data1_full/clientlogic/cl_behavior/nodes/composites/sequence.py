# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/sequence.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/sequence.pyc
# Source Generated with Decompyle++
# File: sequence.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CSequence(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Sequence'
    
    def CreateTask(self):
        return CSequenceTask()

    
    def AddChild(self, oChild):
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True

    
    def Evaluate(self, oAgent, iChildStatus):
        ret = True
        for oChild in self.m_Children:
            ret = oChild.Evaluate(oAgent, iChildStatus)
            if not ret:
                break
        
        return ret

    
    def CheckIfInterrupted(self, oAgent):
        return self.EvaluateCustomCondition(oAgent)

    
    def SequenceUpdate(self, oAgent, iChildStatus, oSequenceTask):
        iResult = iChildStatus
        iChildSize = len(oSequenceTask.m_Children)
        while True:
            if iResult == defines.BT_RUNNING:
                pBehaviorTask = oSequenceTask.m_Children[oSequenceTask.m_ActiveChildIndex]
                if self.CheckIfInterrupted(oAgent):
                    return defines.BT_FAILURE
                iResult = pBehaviorTask.Exec(oAgent)
            if iResult != defines.BT_SUCCESS:
                return iResult
            oSequenceTask.m_ActiveChildIndex += 1
            if oSequenceTask.m_ActiveChildIndex >= iChildSize:
                return defines.BT_SUCCESS
            iResult = defines.BT_RUNNING
        return iResult



class CSequenceTask(behaviortreetask.CCompositeTask):
    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = 0
        return True

    
    def Update(self, oAgent, iChildStatus):
        return self.m_Node.SequenceUpdate(oAgent, iChildStatus, self)


