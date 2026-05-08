# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/attachments/event.pyc
# RelativePath: clientlogic/cl_behavior/attachments/event.pyc
# Source Generated with Decompyle++
# File: event.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from .. import behaviortree
from .. import behaviortreetask
from .. import meta
from .. import workspace

class CEvent(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Event'
    
    def __init__(self):
        super(CEvent, self).__init__()
        self.m_EventName = ''
        self.m_RefrenceBehaviorPath = ''
        self.m_bTriggeredOnce = False
        self.m_TriggerNode = defines.TM_Transfer

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CEvent, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_EventName = meta.ParseProperty(dProperties, 'Task', None)
        self.m_RefrenceBehaviorPath = meta.ParseProperty(dProperties, 'ReferenceFilename', '')
        oInstance = workspace.GetInstance()
        if oInstance.PreloadBehaviors() and self.m_RefrenceBehaviorPath:
            oInstance.Load(self.m_RefrenceBehaviorPath)
        self.m_bTriggeredOnce = meta.ParseProperty(dProperties, 'TriggeredOnce', False)
        self.m_TriggerNode = meta.ParseProperty(dProperties, 'TriggerNode', defines.TM_Transfer)

    
    def CreateTask(self):
        return CEventTask()

    
    def TriggeredOnce(self):
        return self.m_bTriggeredOnce

    
    def GetEventName(self):
        return self.m_EventName

    
    def SwitchTo(self, oAgent, dEventParams):
        if self.m_RefrenceBehaviorPath and oAgent:
            oAgent.BTEventTree(self.m_RefrenceBehaviorPath, self.m_TriggerNode)
            oCurrentTree = oAgent.GetCurrentBT()
            oCurrentTree.AddVariables(dEventParams)
            oAgent.BTExec()

    
    def GetExportData(self):
        dData = super(CEvent, self).GetExportData()
        dData.update({
            'Task': self.m_EventName,
            'ReferenceFilename': self.m_RefrenceBehaviorPath,
            'Flag': 'event',
            'TriggeredOnce': self.m_bTriggeredOnce,
            'TriggerNode': self.m_TriggerNode })
        return dData



class CEventTask(behaviortreetask.CAttachmentTask):
    
    def Update(self, oAgent, iChildStatus):
        if self.m_Node.m_RefrenceBehaviorPath:
            oAgent.BTEventTree(self.m_Node.m_RefrenceBehaviorPath, self.m_Node.m_TriggerNode)
            oAgent.BTExec()
        return defines.BT_SUCCESS


