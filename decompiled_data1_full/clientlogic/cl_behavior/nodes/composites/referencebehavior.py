# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/referencebehavior.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/referencebehavior.pyc
# Source Generated with Decompyle++
# File: referencebehavior.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ... import meta
from ... import workspace
from ...fsm import fsmstate

class CReferenceBehavior(behaviortree.CBehaviorNode):
    CLASS_NAME = 'ReferenceBehavior'
    
    def __init__(self):
        super(CReferenceBehavior, self).__init__()
        self.m_TaskMethod = None
        self.m_TaskNode = None
        self.m_Transitions = []
        self.m_ReferenceBetreePath = ''

    
    def GetBehaviorFileName(self):
        return workspace.GetInstance().GetModuleNameByBehaviorTree(self)

    
    def CreateTask(self):
        return CReferenceBehaviorTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CReferenceBehavior, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_ReferenceBetreePath = meta.ParseProperty(dProperties, 'ReferenceBehavior', '')
        self.m_Name = 'refTree : ' + self.m_ReferenceBetreePath
        oInstance = workspace.GetInstance()
        if self.m_ReferenceBetreePath and oInstance.PreloadBehaviors():
            oTree = oInstance.LoadBehaviorTree(self.m_ReferenceBetreePath)
            if oTree:
                self.m_bHasEvents |= oTree.HasEvents()

    
    def Attach(self, oAttachment, dData):
        if dData['Flag'] == 'transition':
            self.m_Transitions.append(oAttachment)
            return None
        super(CReferenceBehavior, self).Attach(oAttachment, dData)

    
    def RootTaskNode(self, oAgent):
        if not self.m_TaskNode:
            oTree = workspace.GetInstance().LoadBehaviorTree(self.m_ReferenceBetreePath)
            if oTree and oTree.GetChildrenCount() == 1:
                self.m_TaskNode = oTree.GetChild(0)
        return self.m_TaskNode

    
    def SetTaskParams(self, oAgent, oTreeTask):
        if self.m_TaskMethod:
            self.m_TaskMethod.SetTaskParams(oAgent, oTreeTask)

    
    def CollectEventName(self, lstName):
        super(CReferenceBehavior, self).CollectEventName(lstName)
        oInstance = workspace.GetInstance()
        oTree = oInstance.LoadBehaviorTree(self.m_ReferenceBetreePath)
        oTree.CollectEventName(lstName)

    
    def GetExportData(self):
        dData = super(CReferenceBehavior, self).GetExportData()
        dData.update({
            'ReferenceBehavior': self.m_ReferenceBetreePath })
        return dData



class CReferenceBehaviorTask(behaviortreetask.CSingeChildTask):
    
    def __init__(self):
        super(CReferenceBehaviorTask, self).__init__()
        self.m_NextStateID = -1
        self.m_SubTree = None

    
    def GetNextStateID(self):
        return self.m_NextStateID

    
    def OnEvent(self, oAgent, sEventName, dEventParams):
        if self.m_Status == defines.BT_RUNNING and self.m_Node.HasEvents():
            if not self.CheckEvent(oAgent, sEventName, dEventParams):
                return False
            return self.m_SubTree.OnEvent(oAgent, sEventName, dEventParams)
        return True

    
    def OnEnter(self, oAgent):
        self.m_NextStateID = -1
        if self.m_Node.m_ReferenceBetreePath and not (self.m_SubTree):
            oGameSpace = oAgent.GetGameSpace()
            oTask = oGameSpace.CreateBehaviorTreeTask(self.m_Node.m_ReferenceBetreePath)
            self.m_SubTree = oTask
            self.m_Node.SetTaskParams(oAgent, self.m_SubTree)
        elif self.m_SubTree:
            self.m_SubTree.Reset(oAgent)
        return True

    
    def Update(self, oAgent, iChildStatus):
        iResult = self.m_SubTree.Exec(oAgent)
        if fsmstate.CState.UpdateTransitions(oAgent, self, self.m_Node, self.m_Node.m_Transitions, iResult):
            if iResult == defines.BT_RUNNING:
                self.m_SubTree.Abort(oAgent)
            iResult = defines.BT_SUCCESS
        return iResult


