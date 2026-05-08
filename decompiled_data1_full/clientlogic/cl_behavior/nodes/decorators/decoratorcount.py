# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratorcount.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratorcount.pyc
# Source Generated with Decompyle++
# File: decoratorcount.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CDecoratorCount(behaviortree.CDecoratorNode):
    CLASS_NAME = 'DecoratorCount'
    
    def __init__(self):
        super(CDecoratorCount, self).__init__()
        self.m_nCount = -1

    
    def CreateTask(self):
        return CDecoratorCountTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CDecoratorCount, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_nCount = dProperties['Count']

    
    def GetCount(self, oAgent):
        return self.m_nCount

    
    def GetExportData(self):
        dData = super(CDecoratorCount, self).GetExportData()
        dData.update({
            'Count': self.m_nCount })
        return dData



class CDecoratorCountTask(behaviortreetask.CDecoratorTask):
    
    def __init__(self):
        super(CDecoratorCountTask, self).__init__()
        self.m_n = 0

    
    def GetCount(self, oAgent):
        if self.m_Node:
            return self.m_Node.GetCount(oAgent)
        return 0

    
    def Decorate(self, iStatus):
        return iStatus

    
    def OnEnter(self, oAgent):
        super(CDecoratorCountTask, self).OnEnter(oAgent)
        self.m_n = self.GetCount(oAgent)
        nCount = self.GetCount(oAgent)
        if nCount == 0:
            return False
        self.m_n = nCount
        return True


