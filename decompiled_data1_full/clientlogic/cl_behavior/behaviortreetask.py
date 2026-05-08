# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/behaviortreetask.pyc
# RelativePath: clientlogic/cl_behavior/behaviortreetask.pyc
# Source Generated with Decompyle++
# File: behaviortreetask.pyc (Python 3.6)

from cl_only import SendAlert
from . import defines
from . import debug
import time

class CBehaviorTask(object):
    
    def __init__(self):
        self.m_ID = -1
        self.m_Node = None
        self.m_Parent = None
        self.m_Status = defines.BT_INVALID
        self.m_bHasManagingParent = False

    
    def GetTickInfo(pAgent, oBehaviorTask, sAction):
        return CBehaviorTask.GetTickInfoByNode(pAgent, oBehaviorTask.GetNode(), sAction)

    GetTickInfo = staticmethod(GetTickInfo)
    
    def GetTickInfoByNode(pAgent, oNode, sAction):
        if pAgent:
            oParent = oNode
            sRootName = ''
            while True:
                if oParent:
                    if oParent.CLASS_NAME in ('BehaviorTree', 'ReferenceBehavior'):
                        sRootName = debug.GetModuleNameByBehaviorTree(pAgent, oParent)
                        sRootName = sRootName if sRootName else oParent.GetName()
                        break
                    oParent = oParent.GetParent()
                    continue
            sClassName = oNode.CLASS_NAME
            nID = oNode.GetId()
            return '%s.py-> %s[%s]:%s' % (sRootName, sClassName, nID, sAction)

    GetTickInfoByNode = staticmethod(GetTickInfoByNode)
    
    def GetPathName(self):
        if self.m_Node:
            return self.m_Node.GetPathName()
        return 'None'

    
    def Release(self):
        self.m_Parent = None
        self.m_Node = None

    
    def __str__(self):
        if self.m_Node:
            iNode = self.m_Node.GetId()
            sTree = self.m_Node.GetBelongTreePath(None)
        else:
            iNode = -1
            sTree = 'None'
        return '%s-%s-%s-%s' % (self.__class__, sTree, self.GetPathName(), iNode)

    
    def __repr__(self):
        return self.__str__()

    
    def GetNode(self):
        return self.m_Node

    
    def SetId(self, iID):
        self.m_ID = iID

    
    def GetId(self):
        return self.m_ID

    
    def SetParent(self, oParent):
        self.m_Parent = oParent

    
    def GetParent(self):
        return self.m_Parent

    
    def SetCurrentTask(self, oNode):
        pass

    
    def GetCurrentTask(self):
        pass

    
    def GetStatus(self):
        return self.m_Status

    
    def SetHasManagingParent(self, bHasManagingParent):
        self.m_bHasManagingParent = bHasManagingParent

    
    def Init(self, oNode):
        self.m_Node = oNode
        self.m_ID = oNode.GetId()

    
    def GetTaskById(self, iID):
        if self.m_ID == iID:
            return self

    
    def GetNextStateID(self):
        return -1

    
    def Save(self, oIONode):
        pass

    
    def Load(self, oIONode):
        pass

    
    def Update(self, oAgent, iChildStatus):
        return defines.BT_SUCCESS

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        return self.Update(oAgent, iChildStatus)

    
    def CheckEvent(self, oAgent, sEventName, dEventParams):
        return self.m_Node.CheckEvent(oAgent, sEventName, dEventParams)

    
    def OnEvent(self, oAgent, sEventName, dEventParams):
        if not self.m_Status == defines.BT_RUNNING and self.m_Node.m_bHasEvents and self.CheckEvent(oAgent, sEventName, dEventParams):
            return False
        return True

    
    def OnEnter(self, oAgent):
        return True

    
    def OnExit(self, oAgent, status):
        pass

    
    def OnReset(self, oAgent):
        pass

    
    def OnEnterAction(self, oAgent):
        bResult = self.CheckPreconditions(oAgent, False)
        if bResult:
            self.m_bHasManagingParent = False
            self.SetCurrentTask(None)
            bResult = self.OnEnter(oAgent)
            if not bResult:
                return False
            if oAgent.GetGameSpace() and oAgent.GetGameSpace().m_Debug:
                debug.CHECK_BREAKPOINT(oAgent, self.GetNode(), 'enter', defines.EActionResult.EAR_success)
        return bResult

    
    def OnExitAction(self, oAgent, status):
        self.OnExit(oAgent, status)
        if self.m_Node:
            iPhase = defines.E_SUCCESS
            if status == defines.BT_FAILURE:
                iPhase = defines.E_FAILURE
            elif status != defines.BT_SUCCESS:
                oCurrentBT = oAgent.PYGetCurrentBT()
                if oCurrentBT and oCurrentBT.m_Node:
                    sPathName = oCurrentBT.m_Node.GetPathName()
                    SendAlert('behavior', f'''{sPathName} status {status}''')
                status = defines.BT_SUCCESS
            self.m_Node.ApplyEffects(oAgent, iPhase)
            if oAgent.GetGameSpace() and oAgent.GetGameSpace().m_Debug:
                if status == defines.BT_SUCCESS:
                    debug.CHECK_BREAKPOINT(oAgent, self.GetNode(), 'exit', defines.EActionResult.EAR_success)
                else:
                    debug.CHECK_BREAKPOINT(oAgent, self.GetNode(), 'exit', defines.EActionResult.EAR_failure)

    
    def Exec(self, oAgent, iChildStatus = defines.BT_RUNNING):
        if self.m_Status == defines.BT_RUNNING:
            bEnterResult = True
        else:
            self.m_Status = defines.BT_INVALID
            bEnterResult = self.OnEnterAction(oAgent)
        if bEnterResult:
            bValid = self.CheckParentUpdatePreconditions(oAgent)
            if bValid:
                self.m_Status = self.UpdateCurrent(oAgent, iChildStatus)
            else:
                self.m_Status = defines.BT_FAILURE
                if self.GetCurrentTask():
                    self.UpdateCurrent(oAgent, defines.BT_FAILURE)
            if self.m_Status != defines.BT_RUNNING:
                self.OnExitAction(oAgent, self.m_Status)
            else:
                branchTree = self.GetTopManageBranchTask()
                if branchTree:
                    branchTree.SetCurrentTask(self)
                if oAgent.GetGameSpace() and oAgent.GetGameSpace().m_Debug:
                    debug.CHECK_BREAKPOINT(oAgent, self.GetNode(), 'running', defines.EActionResult.EAR_running)
                else:
                    self.m_Status = defines.BT_FAILURE
        return None.m_Status

    
    def CheckParentUpdatePreconditions(self, oAgent):
        bValid = True
        if self.m_bHasManagingParent:
            bHasManagingParent = False
            lstParents = []
            oParentBranch = self.GetParent()
            lstParents.append(self)
            while True:
                if oParentBranch:
                    lstParents.append(oParentBranch)
                    if oParentBranch.GetCurrentTask() is self:
                        bHasManagingParent = True
                        break
                    oParentBranch = oParentBranch.GetParent()
                    continue
            if bHasManagingParent:
                while True:
                    if lstParents:
                        pb = lstParents.pop()
                        bValid = pb.CheckPreconditions(oAgent, True)
                        if not bValid:
                            break
                        continue
            else:
                bValid = self.CheckPreconditions(oAgent, True)

    
    def CheckPreconditions(self, oAgent, bIsAlive):
        bResult = True
        if self.m_Node and self.m_Node.m_PreConditions:
            bResult = self.m_Node.CheckPreconditions(oAgent, bIsAlive)
        return bResult

    
    def GetTopManageBranchTask(self):
        oTree = None
        oTask = self.m_Parent
        while True:
            if oTask:
                if issubclass(oTask.__class__, CBehaviorTreeTask):
                    oTree = oTask
                    break
                if oTask.m_Node.IsManagingChildrenAsSubTrees():
                    break
                if issubclass(oTask.__class__, CBranchTask):
                    oTree = oTask
                    break
                oTask = oTask.m_Parent
                continue
        return oTree

    
    def GetRootTask(self):
        oTask = self
        while True:
            if oTask.m_Parent:
                oTask = oTask.m_Parent
                continue
        return oTask

    
    def traverse(self, childFirst, handler, oAgent, user_data):
        pass

    
    def AbortHandler(self, oNode, oAgent, user_data):
        if oNode.m_Status == defines.BT_RUNNING:
            oNode.OnExitAction(oAgent, defines.BT_FAILURE)
            oNode.m_Status = defines.BT_FAILURE
            oNode.SetCurrentTask(None)
        return True

    
    def ResetHandler(self, oNode, oAgent, user_data):
        oNode.m_Status = defines.BT_INVALID
        oNode.SetCurrentTask(None)
        oNode.OnReset(oAgent)

    
    def EndHandler(self, oNode, oAgent, user_data):
        if oNode.m_Status == defines.BT_RUNNING or oNode.m_Status == defines.BT_INVALID:
            status = user_data
            oNode.OnExitAction(oAgent, status)
            oNode.m_Status = status
            oNode.SetCurrentTask(None)
        return True

    
    def Abort(self, oAgent):
        self.traverse(True, self.AbortHandler, oAgent, 0)

    
    def Reset(self, oAgent):
        self.traverse(True, self.ResetHandler, oAgent, 0)



class CAttachmentTask(CBehaviorTask):
    
    def traverse(self, childFirst, handler, oAgent, user_data):
        handler(self, oAgent, user_data)



class CLeafTask(CBehaviorTask):
    
    def traverse(self, childFirst, handler, oAgent, user_data):
        handler(self, oAgent, user_data)



class CBranchTask(CBehaviorTask):
    
    def __init__(self):
        super(CBranchTask, self).__init__()
        self.m_CurrentNodeId = -1
        self.m_CurrentTask = None

    
    def Release(self):
        super(CBranchTask, self).Release()
        self.m_CurrentTask = None

    
    def GetCurrentNodeId(self):
        return self.m_CurrentNodeId

    
    def SetCurrentNodeId(self, iID):
        self.m_CurrentNodeId = iID

    
    def SetCurrentTask(self, oTask):
        if not oTask or self.m_CurrentTask:
            self.m_CurrentTask = oTask
            oTask.SetHasManagingParent(True)
        elif self.m_Status != defines.BT_RUNNING:
            self.m_CurrentTask = oTask

    
    def GetCurrentTask(self):
        return self.m_CurrentTask

    
    def Resume(self, oAgent, iStatus):
        if self.m_CurrentTask.m_Node.IsManagingChildrenAsSubTrees():
            oParent = self.m_CurrentTask
        else:
            oParent = self.m_CurrentTask.GetParent()
        self.m_CurrentTask = None
        return oParent.Exec(oAgent, iStatus)

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        if self.m_CurrentTask:
            iStatus = self.ExecCurrentTask(oAgent, iChildStatus)
            if not iStatus == defines.BT_RUNNING and iStatus != defines.BT_RUNNING and not (self.m_CurrentTask):
                SendAlert('behavior', f'''update curtask err {self} {oAgent} {self.m_Status} {iChildStatus}, {self.m_CurrentTask} {iStatus}''')
                return defines.BT_FAILURE
        iStatus = self.Update(oAgent, iChildStatus)
        return iStatus

    
    def ExecCurrentTask(self, oAgent, iChildStatus):
        if self.m_CurrentTask:
            iTaskStatus = self.m_CurrentTask.GetStatus()
            if iTaskStatus != defines.BT_RUNNING:
                SendAlert('behavior', f'''exec curtask err {self} {oAgent} {self.m_Status} {iChildStatus}, {self.m_CurrentTask} {iTaskStatus}''')
                self.m_CurrentTask = None
                return defines.BT_FAILURE
            iStatus = self.m_CurrentTask.Exec(oAgent, iChildStatus)
            if iStatus != defines.BT_RUNNING:
                if not (self.m_CurrentTask) or self.m_CurrentTask.m_Status != iStatus or iStatus not in (defines.BT_SUCCESS, defines.BT_FAILURE):
                    iCurrentTask = self.m_CurrentTask.m_Status if self.m_CurrentTask else -1
                    SendAlert('behavior', f'''curtask status err {self} {oAgent} {self.m_Status} {iChildStatus} {iCurrentTask} {iStatus}''')
                    return iStatus
                parentBranch = self.m_CurrentTask.GetParent()
                self.m_CurrentTask = None
                while True:
                    if parentBranch:
                        if parentBranch is self:
                            iStatus = parentBranch.Update(oAgent, iStatus)
                        else:
                            iStatus = parentBranch.Exec(oAgent, iStatus)
                        if iStatus == defines.BT_RUNNING:
                            return defines.BT_RUNNING
                        if not parentBranch is self or parentBranch.m_Status == iStatus:
                            SendAlert('behavior', f'''parent err {self} {oAgent} {self.m_Status} {iChildStatus} {parentBranch} {parentBranch.m_Status} {iStatus}''')
                            break
                        if parentBranch is self:
                            break
                        parentBranch = parentBranch.GetParent()
                        continue
            return iStatus
        return defines.BT_FAILURE

    
    def OnEvent(self, oAgent, sEventName, dEventParams):
        if self.m_Node.HasEvents():
            bGoOn = True
            if self.m_CurrentTask:
                bGoOn = self.OnEventCurrentNode(oAgent, sEventName, dEventParams)
            if bGoOn:
                bGoOn = super(CBranchTask, self).OnEvent(oAgent, sEventName, dEventParams)
        return True

    
    def OnEventCurrentNode(self, oAgent, sEventName, dEventParams):
        if self.m_CurrentTask:
            iStatus = self.m_CurrentTask.GetStatus()
            bGoOn = self.m_CurrentTask.OnEvent(oAgent, sEventName, dEventParams)
            if bGoOn and self.m_CurrentTask:
                oParentBranch = self.m_CurrentTask.GetParent()
                while True:
                    if oParentBranch and oParentBranch is not self:
                        bGoOn = oParentBranch.OnEvent(oAgent, sEventName, dEventParams)
                        if not bGoOn:
                            return False
                        oParentBranch = oParentBranch.GetParent()
                        continue
            return bGoOn
        return True



class CCompositeTask(CBranchTask):
    
    def __init__(self):
        super(CCompositeTask, self).__init__()
        self.m_Children = []
        self.m_ActiveChildIndex = -1

    
    def Init(self, oNode):
        super(CCompositeTask, self).Init(oNode)
        childrenCount = oNode.GetChildrenCount()
        for i in range(childrenCount):
            oChildNode = oNode.GetChild(i)
            oChildTask = oChildNode.CreateAndInitTask()
            self.AddChild(oChildTask)
        

    
    def Release(self):
        super(CCompositeTask, self).Release()
        for oChild in self.m_Children:
            oChild.Release()
        
        self.m_Children = []

    
    def Load(self, oIONode):
        if self.m_Status == defines.BT_INVALID:
            return None

    
    def AddChild(self, oBehaviorTask):
        oBehaviorTask.SetParent(self)
        self.m_Children.append(oBehaviorTask)

    
    def GetChildById(self, iNodeID):
        for oChild in self.m_Children:
            if oChild.GetId() == iNodeID:
                return oChild
        

    
    def GetTaskById(self, iID):
        oTask = super(CCompositeTask, self).GetTaskById(iID)
        if oTask:
            return oTask
        for oChild in self.m_Children:
            oTask = oChild.GetTaskById(iID)
            if oTask:
                return oTask
        

    
    def traverse(self, childFirst, handler, oAgent, user_data):
        if childFirst:
            for oTask in self.m_Children:
                oTask.traverse(childFirst, handler, oAgent, user_data)
            
            handler(self, oAgent, user_data)
        elif handler(self, oAgent, user_data):
            for oTask in self.m_Children:
                oTask.traverse(childFirst, handler, oAgent, user_data)
            



class CSingeChildTask(CBranchTask):
    
    def __init__(self):
        super(CSingeChildTask, self).__init__()
        self.m_Root = None

    
    def Init(self, oNode):
        super(CSingeChildTask, self).Init(oNode)
        if oNode.GetChildrenCount() == 1:
            oChildNode = oNode.GetChild(0)
            oChildTask = oChildNode.CreateAndInitTask()
            self.AddChild(oChildTask)

    
    def Release(self):
        super(CSingeChildTask, self).Release()
        if self.m_Root:
            self.m_Root.Release()
        self.m_Root = None

    
    def Load(self, oIONode):
        super(CSingeChildTask, self).Load(oIONode)
        if self.m_Status != defines.BT_INVALID:
            pass

    
    def AddChild(self, oTask):
        oTask.SetParent(self)
        self.m_Root = oTask

    
    def traverse(self, childFirst, handler, oAgent, user_data):
        if childFirst:
            if self.m_Root:
                self.m_Root.traverse(childFirst, handler, oAgent, user_data)
            handler(self, oAgent, user_data)
        elif handler(self, oAgent, user_data) and self.m_Root:
            self.m_Root.traverse(childFirst, handler, oAgent, user_data)

    
    def Update(self, oAgent, iChildStatus):
        if self.m_Root:
            return self.m_Root.Exec(oAgent, iChildStatus)
        return defines.BT_FAILURE



class CDecoratorTask(CSingeChildTask):
    
    def __init__(self):
        super(CDecoratorTask, self).__init__()
        self.m_bDecorateWhenChildEnds = False

    
    def Init(self, oNode):
        super(CDecoratorTask, self).Init(oNode)
        self.m_bDecorateWhenChildEnds = oNode.m_bDecorateWhenChildEnds

    
    def Update(self, oAgent, iChildStatus):
        if iChildStatus != defines.BT_RUNNING:
            iStatus = iChildStatus
            if not (self.m_Node.m_bDecorateWhenChildEnds) or iStatus != defines.BT_RUNNING:
                iResult = self.Decorate(iStatus)
                if iResult != defines.BT_RUNNING:
                    return iResult
                return defines.BT_RUNNING
        iStatus = super(CDecoratorTask, self).Update(oAgent, iChildStatus)
        if not (self.m_Node.m_bDecorateWhenChildEnds) or iStatus != defines.BT_RUNNING:
            return self.Decorate(iStatus)
        return defines.BT_RUNNING

    
    def Decorate(self, iStatus):
        pass



class CBehaviorTreeTask(CSingeChildTask):
    
    def __init__(self):
        super(CBehaviorTreeTask, self).__init__()
        self.m_LastTreeTask = None
        self.m_LocalVars = { }
        self.m_EndStatus = defines.BT_INVALID
        self.m_bInStack = False

    
    def Init(self, oNode):
        super(CBehaviorTreeTask, self).Init(oNode)
        if self.m_Node:
            self.m_Node.InstantiatePars(self.m_LocalVars)

    
    def Release(self):
        super(CBehaviorTreeTask, self).Release()
        self.m_LastTreeTask = None

    
    def SetInStack(self, bStack):
        self.m_bInStack = bStack

    
    def IsInStack(self):
        return self.m_bInStack

    
    def UpdateCurrent(self, oAgent, iChildStatus):
        self.m_LastTreeTask = oAgent.m_ExcutingTreeTask
        oAgent.m_ExcutingTreeTask = self
        if self.m_Node.IsFSM():
            iStatus = self.Update(oAgent, iChildStatus)
        else:
            iStatus = super(CBehaviorTreeTask, self).UpdateCurrent(oAgent, iChildStatus)
        return iStatus

    
    def GetName(self):
        return self.m_Node.GetName()

    
    def AddVariables(self, dParams):
        self.m_LocalVars.update(dParams)

    
    def SetEndStatus(self, iStatus):
        self.m_EndStatus = iStatus

    
    def End(self, oAgent, iStatus):
        self.traverse(True, self.EndHandler, oAgent, iStatus)
        self.m_EndStatus = self.m_Status

    
    def Update(self, oAgent, iChildStatus):
        if iChildStatus != defines.BT_RUNNING:
            return iChildStatus
        self.m_EndStatus = defines.BT_INVALID
        iStatus = super(CBehaviorTreeTask, self).Update(oAgent, iChildStatus)
        if iStatus == defines.BT_RUNNING and self.m_EndStatus != defines.BT_INVALID:
            self.End(oAgent, self.m_EndStatus)
            return self.m_EndStatus
        return iStatus


