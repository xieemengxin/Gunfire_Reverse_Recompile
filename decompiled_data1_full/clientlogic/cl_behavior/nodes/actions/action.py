# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/actions/action.pyc
# RelativePath: clientlogic/cl_behavior/nodes/actions/action.pyc
# Source Generated with Decompyle++
# File: action.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ... import meta

class CAction(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Action'
    
    def __init__(self):
        super(CAction, self).__init__()
        self.m_Method = None
        self.m_ResultOption = defines.BT_INVALID
        self.m_ResultFuctor = None

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CAction, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = meta.ParseMethod(dProperties, 'Method', None)
        self.m_ResultOption = meta.ParseProperty(dProperties, 'ResultOption', defines.BT_INVALID)
        self.m_ResultFuctor = meta.ParseMethod(dProperties, 'ResultFunctor', None)

    
    def CreateTask(self):
        return CActionTask()

    
    def Execute(self, oAgent, iChildStatus):
        iResult = defines.BT_SUCCESS
        if self.m_Method:
            iStatus = self.m_Method(oAgent)
            if self.m_ResultOption != defines.BT_INVALID:
                iResult = self.m_ResultOption
            elif self.m_ResultFuctor:
                iResult = self.m_ResultFuctor(oAgent)
            elif iStatus is None:
                iResult = defines.BT_SUCCESS
            else:
                iResult = iStatus
        else:
            self.UpdateImpl(oAgent, iChildStatus)
        return iResult

    
    def GetExportData(self):
        dData = super(CAction, self).GetExportData()
        dData.update({
            'Method': meta.TransMethod(self.m_Method),
            'ResultOption': self.m_ResultOption,
            'ResultFunctor': meta.TransMethod(self.m_ResultFuctor) })
        return dData



class CActionTask(behaviortreetask.CLeafTask):
    
    def __init__(self):
        super(CActionTask, self).__init__()
        self.m_EndFunc = None

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        iResult = self.m_Node.Execute(oAgent, iChildStatus)
        if oAgent.m_CurNodeEndFunc:
            self.m_EndFunc = oAgent.m_CurNodeEndFunc
            oAgent.m_CurNodeEndFunc = None
        return iResult

    
    def OnExit(self, oAgent, status):
        if self.m_EndFunc:
            self.m_EndFunc(oAgent, status)
            self.m_EndFunc = None


