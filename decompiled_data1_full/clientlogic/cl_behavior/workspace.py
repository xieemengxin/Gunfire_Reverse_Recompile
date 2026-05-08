# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/workspace.pyc
# RelativePath: clientlogic/cl_behavior/workspace.pyc
# Source Generated with Decompyle++
# File: workspace.pyc (Python 3.6)

from __future__ import absolute_import
import importlib
import weakref
from . import behaviortree
from . import context
from . import agent
from . import tools
if 'g_WorkSpaceInstance' not in globals():
    g_WorkSpaceInstance = None

def GetInstance():
    global g_WorkSpaceInstance
    if not g_WorkSpaceInstance:
        g_WorkSpaceInstance = CWorkSpace()
    return g_WorkSpaceInstance


def NewGame():
    return CGameSpace()


class CWorkSpace(object):
    
    def __init__(self):
        self.m_BehaviorTrees = { }

    
    def GetModuleNameByBehaviorTree(self, o):
        for sPath, _o in self.m_BehaviorTrees.items():
            if _o is o:
                return sPath
        
        return ''

    
    def PreloadBehaviors(self):
        return True

    
    def GetBTVersion(self, sRelativePath):
        sProjectPath = tools.g_Tools.GetProjectTreePath()
        if sProjectPath:
            sPath = '%s.%s' % (sProjectPath, sRelativePath)
        else:
            sPath = sRelativePath
        
        try:
            module = importlib.import_module(sPath)
            return module.data['Ver']
        except:
            return 0


    
    def Load(self, sRelativePath, bForce = False):
        import sys
        if sRelativePath in self.m_BehaviorTrees:
            if not bForce:
                return True
            oOld = self.m_BehaviorTrees.pop(sRelativePath)
            oOld.Clear()
        oBT = behaviortree.CBehaviorTree()
        sProjectPath = tools.g_Tools.GetProjectTreePath()
        if sProjectPath:
            sPath = '%s.%s' % (sProjectPath, sRelativePath)
        else:
            sPath = sRelativePath
        module = importlib.import_module(sPath)
        if bForce:
            if sys.version_info.major == 3:
                importlib.reload(module)
            else:
                reload(module)
        bLoadResult = oBT.LoadForPython(module.data)
        oBT.SetPathName(sRelativePath)
        if bLoadResult:
            self.m_BehaviorTrees[sRelativePath] = oBT
        return bLoadResult

    
    def LoadBehaviorTree(self, sRelativePath):
        if sRelativePath not in self.m_BehaviorTrees:
            self.Load(sRelativePath)
        return self.m_BehaviorTrees[sRelativePath]

    
    def DestroyBehavior(self, sRelativePath):
        if sRelativePath in self.m_BehaviorTrees:
            oOld = self.m_BehaviorTrees.pop(sRelativePath)
            oOld.Clear()

    
    def CreateBehaviorTreeTask(self, sRelativePath):
        if sRelativePath not in self.m_BehaviorTrees:
            self.Load(sRelativePath)
        if sRelativePath in self.m_BehaviorTrees:
            oBT = self.m_BehaviorTrees[sRelativePath]
            oTask = oBT.CreateAndInitTask()
            return oTask

    
    def DestroyBehaviorTreeTask(self, oTask):
        oTask.Release()

    
    def HotReload(self, sRelativePath):
        if tools.g_Tools.CanHotReload():
            self.Load(sRelativePath, True)

    
    def ClearAll(self):
        for oBT in self.m_BehaviorTrees.values():
            oBT.Clear()
        
        self.m_BehaviorTrees.clear()



class CGameSpace(object):
    
    def __init__(self):
        self.m_bIsExecAgents = True
        self.m_ContextID = 0
        self.m_Context = { }
        self.m_FrameSinceStartup = 0
        self.m_bDebugging = False
        self.m_Debug = None
        self.m_dBreakPoints = { }
        self.m_bNextStep = False

    
    def IsDebugging(self):
        if self.m_Debug:
            return True
        return False

    
    def SetDebugging(self, oDebug):
        if not self.m_Debug:
            self.m_Debug = oDebug

    
    def IsNextStep(self):
        bFlag = self.m_bNextStep
        self.m_bNextStep = False
        return bFlag

    
    def NextStepFlag(self):
        self.m_bNextStep = True

    
    def AddBreakPoint(self, sPath, iID, iActionType):
        if (sPath, iID) in self.m_dBreakPoints:
            self.m_dBreakPoints[(sPath, iID)] |= iActionType
        else:
            self.m_dBreakPoints[(sPath, iID)] = iActionType

    
    def RemoveBreakPoint(self, sPath, iID, iActionType):
        if (sPath, iID) in self.m_dBreakPoints:
            self.m_dBreakPoints[(sPath, iID)] &= ~iActionType
            if self.m_dBreakPoints[(sPath, iID)] == 0:
                del self.m_dBreakPoints[(sPath, iID)]

    
    def IsBreakPoint(self, oNode, pAgent):
        sPath = oNode.GetBelongTreePath(pAgent)
        iID = oNode.GetId()
        if (sPath, iID) in self.m_dBreakPoints:
            return self.m_dBreakPoints[(sPath, iID)]

    
    def SetEditorDebugging(self, bFlag):
        self.m_Debug = bFlag

    
    def GetBTVersion(self, sRelativePath):
        return GetInstance().GetBTVersion(sRelativePath)

    
    def CreateBehaviorTreeTask(self, sRelativePath):
        oTask = GetInstance().CreateBehaviorTreeTask(sRelativePath)
        return oTask

    
    def Clear(self):
        for oContext in self.m_Context.values():
            oContext.Clear()
        
        self.m_Context = { }
        if self.m_Debug:
            self.m_Debug.Release()
            self.m_Debug = None

    
    def Update(self, contextID):
        if isinstance(contextID, int):
            contextID = [
                contextID]
        if not contextID:
            contextID = list(self.m_Context)
        for iID in contextID:
            oContext = self.m_Context[iID]
            oContext.ExecAgents(self)
        

    
    def OnEvent(self, oAgent, iMsg, dParams):
        oAgent.BTOnEvent(iMsg, dParams)

    
    def ChooseContext(self):
        if not self.m_Context:
            oContext = self.NewContext()
            iContext = oContext.m_ContextID
            self.m_Context[iContext] = oContext
        else:
            iContext = list(self.m_Context)[0]
        return iContext

    
    def CreateAgent(self, oClass, sAgentName, iContext = 0, iPriority = 0):
        if not iContext:
            iContext = self.ChooseContext()
        elif iContext not in self.m_Context:
            return None
        return agent.CAgent.Create(weakref.proxy(self), oClass, sAgentName, iContext, iPriority)

    
    def NewContext(self):
        self.m_ContextID += 1
        return context.CContext(self.m_ContextID)

    
    def GetContext(self, iContext):
        if iContext in self.m_Context:
            return self.m_Context[iContext]

    
    def SetIsExecAgents(self, bExecAgents):
        self.m_bIsExecAgents = bExecAgents

    
    def IsExecAgents(self):
        return self.m_bIsExecAgents

    
    def SetFrameSinceStartup(self, iFrame):
        self.m_FrameSinceStartup = iFrame

    
    def GetFrameSinceStartup(self):
        return self.m_FrameSinceStartup


