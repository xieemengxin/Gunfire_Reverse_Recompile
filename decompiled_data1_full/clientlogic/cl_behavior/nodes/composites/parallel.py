# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/composites/parallel.pyc
# RelativePath: clientlogic/cl_behavior/nodes/composites/parallel.pyc
# Source Generated with Decompyle++
# File: parallel.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CParallel(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Parallel'
    
    def __init__(self):
        super(CParallel, self).__init__()
        self.m_FailPolicy = defines.FAIL_ON_ONE
        self.m_SuccessPolicy = defines.SUCCEED_ON_ALL
        self.m_ExitPolicy = defines.EXIT_NONE
        self.m_ChildFinishPolicy = defines.CHILDFINISH_LOOP

    
    def AddChild(self, oChild):
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True

    
    def CreateTask(self):
        return CParallelTask()

    
    def IsManagingChildrenAsSubTrees(self):
        return True

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CParallel, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_FailPolicy = dProperties['FailurePolicy'] if 'FailurePolicy' in dProperties else defines.FAIL_ON_ONE
        self.m_SuccessPolicy = dProperties['SuccessPolicy'] if 'SuccessPolicy' in dProperties else defines.SUCCEED_ON_ALL
        self.m_ExitPolicy = dProperties['ExitPolicy'] if 'ExitPolicy' in dProperties else defines.EXIT_NONE
        self.m_ChildFinishPolicy = dProperties['ChildFinishPolicy'] if 'ChildFinishPolicy' in dProperties else defines.CHILDFINISH_LOOP

    
    def GetExportData(self):
        dData = super(CParallel, self).GetExportData()
        dData.update({
            'FailurePolicy': self.m_FailPolicy,
            'SuccessPolicy': self.m_SuccessPolicy,
            'ExitPolicy': self.m_ExitPolicy,
            'ChildFinishPolicy': self.m_ChildFinishPolicy })
        return dData

    
    def ParallelUpdate(self, oAgent, oParallelTask):
        bSawSuccess = False
        bSawFail = False
        bSawRunning = False
        bSawAllFails = True
        bSawAllSuccess = True
        bLoop = self.m_ChildFinishPolicy == defines.CHILDFINISH_LOOP
        for oChild in oParallelTask.m_Children:
            iTreeStatus = oChild.GetStatus()
            if bLoop or iTreeStatus == defines.BT_RUNNING or iTreeStatus == defines.BT_INVALID:
                iRetStatus = oChild.Exec(oAgent)
                if iRetStatus == defines.BT_FAILURE:
                    bSawFail = True
                    bSawAllSuccess = False
                elif iRetStatus == defines.BT_SUCCESS:
                    bSawSuccess = True
                    bSawAllFails = False
                elif iRetStatus == defines.BT_RUNNING:
                    bSawRunning = True
                    bSawAllFails = False
                    bSawAllSuccess = False
                elif iTreeStatus == defines.BT_SUCCESS:
                    bSawSuccess = True
                    bSawAllFails = False
                elif iTreeStatus == defines.BT_FAILURE:
                    bSawFail = True
                    bSawAllSuccess = False
            if None.m_FailPolicy == defines.FAIL_ON_ONE and bSawFail:
                break
            if self.m_SuccessPolicy == defines.SUCCEED_ON_ONE and bSawSuccess:
                break
        
        iStatus = defines.BT_RUNNING if bSawRunning else defines.BT_FAILURE
        if (self.m_FailPolicy == defines.FAIL_ON_ALL or bSawAllFails or self.m_FailPolicy == defines.FAIL_ON_ONE) and bSawFail:
            iStatus = defines.BT_FAILURE
        elif (self.m_SuccessPolicy == defines.SUCCEED_ON_ALL or bSawAllSuccess or self.m_SuccessPolicy == defines.SUCCEED_ON_ONE) and bSawSuccess:
            iStatus = defines.BT_SUCCESS
        if self.m_ExitPolicy == defines.EXIT_ABORT_RUNNINGSIBLINGS:
            if iStatus == defines.BT_FAILURE or iStatus == defines.BT_SUCCESS:
                for oChild in oParallelTask.m_Children:
                    if oChild.GetStatus() == defines.BT_RUNNING:
                        oChild.Abort(oAgent)
                
        return iStatus



class CParallelTask(behaviortreetask.CCompositeTask):
    
    def Update(self, oAgent, iChildStatus):
        return self.m_Node.ParallelUpdate(oAgent, self)

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        return self.Update(oAgent, iChildStatus)


