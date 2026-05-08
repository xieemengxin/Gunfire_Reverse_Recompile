# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/ifelse.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/ifelse.pyc
# Source Generated with Decompyle++
# File: ifelse.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ... import tools
from ... import GetWorkSpace

class CIfElse(behaviortree.CBehaviorNode):
    CLASS_NAME = 'IfElse'
    
    def CreateTask(self):
        return CIfElseTask()

    
    def AddChild(self, oChild):
        if len(self.m_Children) >= 3:
            tools.g_Tools.Print('最多三个节点')
            return False
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        if len(self.m_Children) >= 3:
            tools.g_Tools.Print('最多三个节点')
            return False
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True



class CIfElseTask(behaviortreetask.CCompositeTask):
    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = -1
        if len(self.m_Children) == 3:
            return True
        oCurrentBT = oAgent.PYGetCurrentBT()
        sTreeInfo = GetWorkSpace().GetModuleNameByBehaviorTree(oCurrentBT.m_Node) if oCurrentBT else ''

    
    def Update(self, oAgent, iChildStatus):
        iResult = defines.BT_INVALID
        if iChildStatus == defines.BT_SUCCESS or iChildStatus == defines.BT_FAILURE:
            iResult = iChildStatus
        if self.m_ActiveChildIndex == -1:
            oCondition = self.m_Children[0]
            oIf = self.m_Children[1]
            oElse = self.m_Children[2]
            if iResult == defines.BT_INVALID:
                iResult = oCondition.Exec(oAgent)
            if iResult == defines.BT_SUCCESS:
                self.m_ActiveChildIndex = 1
                iResult = oIf.Exec(oAgent)
            elif iResult == defines.BT_FAILURE:
                self.m_ActiveChildIndex = 2
                iResult = oElse.Exec(oAgent)
            else:
                iResult = defines.BT_RUNNING
        return iResult


