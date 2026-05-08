# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratorweight.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratorweight.pyc
# Source Generated with Decompyle++
# File: decoratorweight.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CDecoratorWeight(behaviortree.CDecoratorNode):
    CLASS_NAME = 'DecoratorWeight'
    
    def __init__(self):
        super(CDecoratorWeight, self).__init__()
        self.m_Weight = 0

    
    def CreateTask(self):
        return CDecoratorWeightTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CDecoratorWeight, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Weight = dProperties['Weight']

    
    def GetWeight(self, oAgent):
        return self.m_Weight

    
    def IsManagingChildrenAsSubTrees(self):
        return False

    
    def GetExportData(self):
        dData = super(CDecoratorWeight, self).GetExportData()
        dData.update({
            'Weight': self.m_Weight })
        return dData



class CDecoratorWeightTask(behaviortreetask.CDecoratorTask):
    
    def GetWeight(self, oAgent):
        if self.m_Node:
            return self.m_Node.GetWeight(oAgent)
        return 0

    
    def Decorate(self, iStatus):
        return iStatus


