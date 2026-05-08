# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/select.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/select.pyc
# Source Generated with Decompyle++
# File: select.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CSelector(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Selector'
    
    def CreateTask(self):
        return CSelectorTask()

    
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

    
    def SelectorUpdate(self, oAgent, iChildStatus, oSelectTask):
        iResult = iChildStatus
        iChildSize = len(oSelectTask.m_Children)
        while True:
            if iResult == defines.BT_RUNNING:
                oTask = oSelectTask.m_Children[oSelectTask.m_ActiveChildIndex]
                if self.CheckIfInterrupted(oAgent):
                    return defines.BT_FAILURE
                iResult = oTask.Exec(oAgent)
            if iResult != defines.BT_FAILURE:
                return iResult
            oSelectTask.m_ActiveChildIndex += 1
            if oSelectTask.m_ActiveChildIndex >= iChildSize:
                return defines.BT_FAILURE
            iResult = defines.BT_RUNNING
        return iResult



class CSelectorTask(behaviortreetask.CCompositeTask):
    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = 0
        return True

    
    def Update(self, oAgent, iChildStatus):
        return self.m_Node.SelectorUpdate(oAgent, iChildStatus, self)


