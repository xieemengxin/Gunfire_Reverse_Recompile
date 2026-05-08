# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/fsm/fsmstate.pyc
# RelativePath: clientlogic/cl_behavior/fsm/fsmstate.pyc
# Source Generated with Decompyle++
# File: fsmstate.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from .. import behaviortree
from .. import behaviortreetask
from .. import meta

class CState(behaviortree.CBehaviorNode):
    CLASS_NAME = 'State'
    
    def __init__(self):
        super(CState, self).__init__()
        self.m_bIsEndState = False
        self.m_Method = None
        self.m_Transition = []

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CState, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = meta.ParseMethod(dProperties, 'Method', None)
        self.m_bIsEndState = meta.ParseProperty(dProperties, 'IsEndState', False)

    
    def Attach(self, oAttachment, dData):
        if dData['Flag'] == 'transition':
            self.m_Transition.append(oAttachment)
            return None
        super(CState, self).Attach(oAttachment, dData)

    
    def CreateTask(self):
        return CStateTask()

    
    def Execute(self, oAgent):
        iResult = defines.BT_RUNNING
        if self.m_Method:
            self.m_Method(oAgent)
        else:
            iResult = self.UpdateImpl(oAgent, defines.BT_RUNNING)
        return iResult

    
    def Update(self, oAgent, oTreeTask):
        iResult = self.Execute(oAgent)
        if self.m_bIsEndState:
            iResult = defines.BT_SUCCESS
        else:
            bTransitioned = CState.UpdateTransitions(oAgent, oTreeTask, self, self.m_Transition, iResult)
            if bTransitioned:
                iResult = defines.BT_SUCCESS
        return iResult

    
    def UpdateTransitions(oAgent, oTreeTask, oNode, lstTransitions, iResult):
        for oTrans in lstTransitions:
            if oTrans.Evaluate(oAgent, iResult):
                iNextStateID = oTrans.GetTargetStateID()
                oTreeTask.m_NextStateID = iNextStateID
                oTrans.ApplyEffects(oAgent, defines.E_BOTH)
                return True
        
        return False

    UpdateTransitions = staticmethod(UpdateTransitions)
    
    def GetExportData(self):
        dData = super(CState, self).GetExportData()
        dData.update({
            'Method': meta.TransMethod(self.m_Method),
            'IsEndState': self.m_bIsEndState })
        return dData



class CStateTask(behaviortreetask.CLeafTask):
    
    def __init__(self):
        super(CStateTask, self).__init__()
        self.m_NextStateID = -1

    
    def GetNextStateID(self):
        return self.m_NextStateID

    
    def OnEnter(self, oAgent):
        self.m_NextStateID = -1
        return True

    
    def Update(self, oAgent, iChildStatus):
        return self.m_Node.Update(oAgent, self)

    
    def IsEndState(self):
        return self.m_Node.m_bIsEndState


