# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/actions/waitframe.pyc
# RelativePath: clientlogic/cl_behavior/nodes/actions/waitframe.pyc
# Source Generated with Decompyle++
# File: waitframe.pyc (Python 3.6)

from __future__ import absolute_import
from ... import meta
from ... import defines
from ... import behaviortree
from ... import behaviortreetask
from ... import workspace

class CWaitFrame(behaviortree.CBehaviorNode):
    CLASS_NAME = 'WaitFrame'
    
    def __init__(self):
        super(CWaitFrame, self).__init__()
        self.m_Frames = 0

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CWaitFrame, self).LoadProperties(iVersion, sAgentType, dProperties)
        for key, value in dProperties.items():
            if key == 'Frames' or isinstance(value, tuple):
                self.m_Frames = meta.ParseMethod(dProperties, 'Frames', None)
                continue
            self.m_Frames = meta.ParseProperty(dProperties, 'Frames', 0)
        

    
    def CreateTask(self):
        return CWaitFramesTask()

    
    def GetFrames(self, oAgent):
        if isinstance(self.m_Frames, int):
            return self.m_Frames
        return self.m_Frames(oAgent)

    
    def GetExportData(self):
        dData = super(CWaitFrame, self).GetExportData()
        dData.update({
            'Frames': meta.TransMethod2(self.m_Frames) })
        return dData



class CWaitFramesTask(behaviortreetask.CLeafTask):
    
    def __init__(self):
        super(CWaitFramesTask, self).__init__()
        self.m_Start = 0
        self.m_Frames = 0
        self.m_EndFunc = None

    
    def GetFrames(self, oAgent):
        oWaitFrameNode = self.GetNode()
        if oWaitFrameNode:
            return oWaitFrameNode.GetFrames(oAgent)
        return 0

    
    def OnEnter(self, oAgent):
        self.m_Start = oAgent.GetGameSpace().GetFrameSinceStartup()
        self.m_Frames = self.GetFrames(oAgent)
        if self.m_Frames <= 0:
            return False
        return True

    
    def Update(self, oAgent, iChildStatus):
        
        def WaitEnd():
            oAgent.SetData('WaitFrame', False)
            oAgent.Remove_Call_Out('WaitFrame')

        
        def WaitFrameCallBack():
            if oAgent.IsActive():
                oAgent.BTExec()

        iFrame = oAgent.GetGameSpace().GetFrameSinceStartup()
        iPassedFrame = iFrame - self.m_Start
        if iPassedFrame >= self.m_Frames:
            return defines.BT_SUCCESS
        if not oAgent.GetData('WaitFrame', False):
            oAgent.SetData('WaitFrame', True)
            iRemainFrame = self.m_Frames - iPassedFrame
            oAgent.Call_Out(WaitFrameCallBack, iRemainFrame, 'WaitFrame')
            self.m_EndFunc = WaitEnd
        return defines.BT_RUNNING

    
    def OnExit(self, oAgent, status):
        if self.m_EndFunc:
            self.m_EndFunc()
            self.m_EndFunc = None


