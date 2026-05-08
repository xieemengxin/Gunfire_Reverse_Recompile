# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/conditions/condition.pyc
# RelativePath: clientlogic/cl_behavior/nodes/conditions/condition.pyc
# Source Generated with Decompyle++
# File: condition.pyc (Python 3.6)

from __future__ import absolute_import
from ... import meta
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CCondition(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Condition'
    
    def __init__(self):
        super(CCondition, self).__init__()
        self.m_Opl = None
        self.m_Opr = None
        self.m_Operator = defines.E_EQUAL

    
    def AddEffector(self, oAttachment):
        return False

    
    def AddPreCodition(self, oAttachment):
        return False

    
    def CreateTask(self):
        return CConditionTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CCondition, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = meta.ParseMethod(dProperties, 'Method', None)

    
    def Evaluate(self, oAgent):
        if self.m_Method:
            return self.m_Method(oAgent)
        iChildStatus = defines.BT_INVALID
        result = self.UpdateImpl(oAgent, iChildStatus)
        return result == defines.BT_SUCCESS

    
    def GetExportData(self):
        dData = super(CCondition, self).GetExportData()
        dData.update({
            'Method': meta.TransMethod3(self.m_Opl, self.m_Operator, self.m_Opr) })
        return dData



class CConditionTask(behaviortreetask.CLeafTask):
    
    def UpdateCurrent(self, oAgent, iChildStatus):
        oConditionNode = self.GetNode()
        iRet = oConditionNode.Evaluate(oAgent)
        if iRet:
            return defines.BT_SUCCESS
        return defines.BT_FAILURE


