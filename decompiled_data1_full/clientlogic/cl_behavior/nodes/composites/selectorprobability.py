# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/selectorprobability.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/selectorprobability.pyc
# Source Generated with Decompyle++
# File: selectorprobability.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ..decorators import decoratorweight
from ... import meta

class CSelectorProbability(behaviortree.CBehaviorNode):
    CLASS_NAME = 'SelectorProbability'
    
    def __init__(self):
        super(CSelectorProbability, self).__init__()
        self.m_Method = None

    
    def CreateTask(self):
        return CSelectorProbabilityTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CSelectorProbability, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = dProperties.get('RandomGenerator', None)

    
    def AddChild(self, oChild):
        if not isinstance(oChild, decoratorweight.CDecoratorWeight):
            return False
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        if not isinstance(oChild, decoratorweight.CDecoratorWeight):
            return False
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True

    
    def GetRandomValue(self, oAgent):
        if self.m_Method:
            return self.m_Method(oAgent)

    
    def GetExportData(self):
        dData = super(CSelectorProbability, self).GetExportData()
        dData.update({
            'RandomGenerator': meta.TransMethod(self.m_Method) })
        return dData



class CSelectorProbabilityTask(behaviortreetask.CCompositeTask):
    
    def __init__(self):
        super(CSelectorProbabilityTask, self).__init__()
        self.m_WeightingMap = { }
        self.m_SumWeight = 0

    
    def OnEnter(self, oAgent):
        self.m_ActiveChildIndex = -1
        self.m_WeightingMap = { }
        for idx, oChild in enumerate(self.m_Children):
            iWeight = oChild.GetWeight(oAgent)
            self.m_WeightingMap[idx] = iWeight
            self.m_SumWeight += iWeight
        
        return True

    
    def OnExit(self, oAgent, iChildStatus):
        self.m_ActiveChildIndex = -1

    
    def Update(self, oAgent, iChildStatus):
        if iChildStatus != defines.BT_RUNNING:
            return iChildStatus
        if self.m_ActiveChildIndex != -1:
            oChild = self.m_Children[self.m_ActiveChildIndex]
            return oChild.Exec(oAgent)
        iRandom = self.m_Node.GetRandomValue(oAgent)
        if iRandom is None:
            import random
            nCount = sum(self.m_WeightingMap.values())
            iRandom = random.randint(0, int(nCount))
        iSum = 0
        for idx, oChild in enumerate(self.m_Children):
            iSum += self.m_WeightingMap[idx]
            if self.m_WeightingMap[idx] and iSum >= iRandom:
                iStatus = oChild.Exec(oAgent)
                if iStatus == defines.BT_RUNNING:
                    self.m_ActiveChildIndex = idx
                else:
                    self.m_ActiveChildIndex = -1
                return iStatus
        
        return defines.BT_FAILURE


