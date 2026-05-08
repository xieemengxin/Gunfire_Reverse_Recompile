# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/conditions/ornode.pyc
# RelativePath: clientlogic/cl_behavior/nodes/conditions/ornode.pyc
# Source Generated with Decompyle++
# File: ornode.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ..composites import select

class COr(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Or'
    
    def AddEffector(self, oAttachment):
        return False

    
    def AddPreCodition(self, oAttachment):
        return False

    
    def CreateTask(self):
        return COrTask()

    
    def Evaluate(self, oAgent):
        iRet = True
        for oNode in self.m_Children:
            iRet = oNode.Evaluate(oAgent)
            if iRet:
                break
        
        return iRet

    
    def AddChild(self, oChild):
        if len(self.m_Children) >= 2:
            return False
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        if len(self.m_Children) >= 2:
            return False
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True



class COrTask(select.CSelectorTask):
    
    def Update(self, oAgent, iChildStatus):
        for oTask in self.m_Children:
            iRet = oTask.Exec(oAgent)
            if iRet == defines.BT_SUCCESS:
                return iRet
        
        return defines.BT_FAILURE


