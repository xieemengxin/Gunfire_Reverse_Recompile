# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/agent.pyc
# RelativePath: clientlogic/cl_behavior/agent.pyc
# Source Generated with Decompyle++
# File: agent.pyc (Python 3.6)

from .defines import TM_Return, BT_RUNNING, BT_INVALID, TM_Transfer
if 'g_AgentIndex' not in globals():
    g_AgentIndex = 0

def NewAgentIndex():
    global g_AgentIndex, g_AgentIndex
    g_AgentIndex += 1
    if g_AgentIndex > 2147483647:
        g_AgentIndex = 1
    return g_AgentIndex


class CAgent(object):
    m_EventKey = { }
    m_ConfigKey = { }
    m_DataKey = { }
    m_CacheKey = { }
    
    def __init__(self):
        self.m_ID = -1
        self.m_GameSpace = None
        self.m_ContextID = -1
        self.m_CurrentBT = None
        self.m_Priority = 0
        self.m_bActive = True
        self.m_ReferenceTree = False
        self.m_ExcutingTreeTask = 0
        self.m_Name = ''
        self.m_BTStack = []
        self.m_BehaviorTreeTasks = []
        self.m_Config = { }
        self.m_Cache = { }
        self.m_Data = { }
        self.m_CurNodeEndFunc = None

    
    def GetClassTypeName():
        return 'CAgent'

    GetClassTypeName = staticmethod(GetClassTypeName)
    
    def Create(oGameSpace, classObject, sAgentInstanceName, iContextId = 0, iPriority = 0):
        oAgent = classObject()
        oAgent.m_GameSpace = oGameSpace
        oAgent.m_ContextID = iContextId
        oAgent.m_ID = NewAgentIndex()
        oAgent.m_Priority = iPriority
        oAgent.SetName(sAgentInstanceName)
        oContext = oGameSpace.GetContext(iContextId)
        oContext.AddAgent(oAgent)
        return oAgent

    Create = staticmethod(Create)
    
    def Release(self):
        from . import workspace
        oContext = self.m_GameSpace.GetContext(self.m_ContextID)
        oContext.RemoveAgent(self)
        oInstance = workspace.GetInstance()
        for oTask in self.m_BehaviorTreeTasks:
            oInstance.DestroyBehaviorTreeTask(oTask)
        
        self.m_BehaviorTreeTasks = []
        self.m_BTStack = []
        self.m_ExcutingTreeTask = 0
        self.m_CurrentBT = None
        self.m_GameSpace = None

    
    def GetId(self):
        return self.m_ID

    
    def GetPriority(self):
        return self.m_Priority

    
    def SetName(self, sName):
        self.m_Name = sName

    
    def GetName(self):
        return self.m_Name

    
    def GetVariable(self, variableName):
        pass

    
    def GetGameSpace(self):
        return self.m_GameSpace

    
    def _BTSetCurrent(self, sRelativePath, iTriggerMode, bByEvent):
        from . import workspace
        if not sRelativePath:
            return None
        bLoaded = workspace.GetInstance().Load(sRelativePath)
        if not bLoaded:
            return None
        if self.m_CurrentBT:
            if iTriggerMode == TM_Return:
                self.m_BTStack.append((self.m_CurrentBT, iTriggerMode, bByEvent))
                self.m_CurrentBT.SetInStack(True)
            elif iTriggerMode == TM_Transfer:
                self.m_CurrentBT.Abort(self)
                self.m_CurrentBT.Reset(self)
        oTask = None
        bNewTask = True
        for oTpTask in self.m_BehaviorTreeTasks:
            if oTpTask.GetPathName() != sRelativePath:
                continue
            bNewTask = False
            if not oTpTask.IsInStack():
                oTask = oTpTask
                break
        
        if oTask and oTask.GetStatus() != BT_INVALID:
            oTask.Reset(self)
        if not oTask:
            oGameSpace = self.GetGameSpace()
            oTask = oGameSpace.CreateBehaviorTreeTask(sRelativePath)
            self.m_BehaviorTreeTasks.append(oTask)
            if bNewTask:
                self.RegisterEvent(oTask)
        self.m_CurrentBT = oTask

    
    def BTSetCurrent(self, sRelativePath):
        self._BTSetCurrent(sRelativePath, TM_Transfer, False)

    
    def BTReferenceTree(self, sRelativePath):
        self.m_ReferenceTree = True
        self._BTSetCurrent(sRelativePath, TM_Return, False)

    
    def BTEventTree(self, sRelativePath, iTriggerMode):
        self._BTSetCurrent(sRelativePath, iTriggerMode, True)

    
    def BTResetCurrent(self):
        if self.m_CurrentBT:
            self.m_CurrentBT.Reset(self)

    
    def TrueBTExec(self):
        if not self.m_CurrentBT:
            return BT_INVALID
        oCurrent = self.m_CurrentBT
        s = oCurrent.Exec(self)
        while True:
            if s != BT_RUNNING:
                if self.m_BTStack:
                    (oTask, iTriggerMode, bByEvent) = self.m_BTStack.pop()
                    oTask.SetInStack(False)
                    self.m_CurrentBT = oTask
                    bExecCurrent = False
                    if iTriggerMode == TM_Return:
                        if bByEvent or self.m_CurrentBT != oCurrent:
                            s = self.m_CurrentBT.Resume(self, s)
                        
                    else:
                        bExecCurrent = True
                else:
                    bExecCurrent = True
                if bExecCurrent:
                    s = self.m_CurrentBT.Exec(self)
                    break
                continue
        if s != BT_RUNNING:
            self.m_ExcutingTreeTask = 0
        return s

    
    def BTExec(self):
        if self.m_bActive:
            self.UpdateVariableRegistry()
            self.m_ReferenceTree = False
            s = self.TrueBTExec()
            while True:
                if self.m_ReferenceTree and s == BT_RUNNING:
                    self.m_ReferenceTree = False
                    s = self.TrueBTExec()
                    continue
            return s
        return BT_INVALID

    
    def BTOnEvent(self, sEvent, dEventParams):
        if not self.m_CurrentBT:
            return None
        self.m_CurrentBT.OnEvent(self, sEvent, dEventParams)

    
    def RegisterEvent(self, oTask):
        lstEvent = []
        oTask.m_Node.CollectEventName(lstEvent)
        self.OnRegisterEvent(lstEvent)

    
    def GetCurrentBT(self):
        return self.m_CurrentBT

    
    def BTLoad(self, sRelativePath, bForce = False):
        from . import workspace
        return workspace.GetInstance().Load(sRelativePath, bForce)

    
    def SetActive(self, bActive):
        self.m_bActive = bActive

    
    def IsActive(self):
        return self.m_bActive

    
    def UpdateVariableRegistry(self):
        self.m_Cache = { }

    
    def SetCache(self, sKey, value):
        self.m_Cache[sKey] = value

    
    def GetCache(self, sKey, default = None):
        if sKey not in self.m_Cache:
            return default
        return self.m_Cache[sKey]

    
    def SetData(self, sKey, value):
        self.m_Data[sKey] = value

    
    def GetData(self, sKey, default = None):
        if sKey not in self.m_Data:
            return default
        return self.m_Data[sKey]

    
    def SetDefaultData(self, key, value):
        if key not in self.m_Data:
            self.m_Data[key] = value
            return value
        return self.m_Data[key]

    
    def GetConfig(self, sKey, default = None):
        if sKey not in self.m_Config:
            return default
        return self.m_Config[sKey]

    
    def AddCurNodeEndFunc(self, func):
        self.m_CurNodeEndFunc = func

    
    def OnRegisterEvent(self, lstEvent):
        pass


