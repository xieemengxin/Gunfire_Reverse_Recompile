# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/mobject.pyc
# RelativePath: clientlogic/cl_behavior/debug/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from __future__ import absolute_import
from .. import debug, GetWorkSpace, GetTools, CreateBehaviorTree

class BTDebug:
    
    def __init__(self, oGameSpace, iDebugPlayer, iFromServer):
        self.m_GameSpace = oGameSpace
        self.m_DebugPlayer = iDebugPlayer
        self.m_Server = iFromServer
        self.m_BehaviorTrees = { }
        self.m_BTData = { }
        self.m_BTStr = { }
        self.SetDebugFunc()
        self.m_DebugTarget = 0

    
    def Release(self):
        debug.SendGameEnd(self.m_DebugPlayer, self.m_Server)
        for oBT in self.m_BehaviorTrees.values():
            oBT.Clear()
        
        self.m_BehaviorTrees = { }
        self.m_BTData = { }
        self.m_BTStr = { }
        del self.m_GameSpace.GetBTVersion
        del self.m_GameSpace.CreateBehaviorTreeTask
        del self.m_GameSpace.Update
        del self.m_GameSpace.CreateFsmTask
        self.m_GameSpace = None

    
    def SetDebugFunc(self):
        self.m_GameSpace.GetBTVersion = self.GetBTVersion
        self.m_GameSpace.CreateBehaviorTreeTask = self.CreateDebugBTTask
        self.m_GameSpace.Update = self.DebugUpdate
        self.m_GameSpace.CreateFsmTask = self.CreateDebugFsmTask

    
    def GetPlayer(self):
        return self.m_DebugPlayer

    
    def GetServer(self):
        return self.m_Server

    
    def DebugUpdate(self, contextID):
        oGameSpace = self.m_GameSpace
        if isinstance(contextID, int):
            contextID = [
                contextID]
        if not contextID:
            contextID = list(oGameSpace.m_Context)
        for iID in contextID:
            oContext = oGameSpace.m_Context[iID]
            
            try:
                oContext.ExecAgents(oGameSpace)
            except Exception as e:
                GetTools().Notify(self.m_DebugPlayer, '联调行为树运行出错：%s' % e)
                continue

        

    
    def GetBTVersion(self, sRelativePath):
        if sRelativePath in self.m_BTData:
            return self.m_BTData[sRelativePath]['data']['Ver']
        return GetWorkSpace().GetBTVersion(sRelativePath)

    
    def GetModuleNameByBehaviorTree(self, oNode):
        for sPath, _o in self.m_BehaviorTrees.items():
            if _o is oNode:
                return sPath
        
        return GetWorkSpace().GetModuleNameByBehaviorTree(oNode)

    
    def SetBTData(self, sRelativePath, sCode):
        if not GetTools().IsInternalNetServer():
            debug.NotifyMsg(self.m_DebugPlayer, self.m_Server, '本服务器不是内服,禁止调试行为树')
            return False
        err = GetTools().CheckPythonSyntax(sCode)
        if err:
            sReason = '%s有错误\n#R%s#n' % (sRelativePath, err)
            debug.NotifyMsg(self.m_DebugPlayer, self.m_Server, sReason)
            return False
        dRet = { }
        
        try:
            exec(sCode, dRet)
        except:
            debug.NotifyMsg(self.m_DebugPlayer, self.m_Server, 'SetBTDataError')
            return False

        bLoadResult = self.Load(sRelativePath, dRet, sCode)
        return bLoadResult

    
    def SaveBTData(self, sRelativePath, sDescription, sTaskID):
        from gamegm.net import GetIMByPid
        if sRelativePath not in self.m_BTStr:
            return False
        sNewCode = self.m_BTStr[sRelativePath].replace('\r\n', '\n')
        sIM = GetIMByPid(self.m_DebugPlayer)
        sName = GetIMByPid(self.m_DebugPlayer, iType = 0)
        if self.m_Server in (4430101,):
            iServer = 4430102
        else:
            iServer = self.m_Server
        tCommitInfo = (sDescription, sTaskID, sName)
        debug.SaveTree(iServer, self.m_DebugPlayer, sIM, tCommitInfo, sRelativePath, sNewCode)
        return True

    
    def Load(self, sRelativePath, dCode, sCode):
        module = dCode
        if module['data']['IsFSM']:
            oBT = self.m_GameSpace.CreateFsm(sRelativePath)
        else:
            oBT = CreateBehaviorTree()
        
        try:
            bLoadResult = oBT.LoadForPython(module['data'])
        except:
            debug.NotifyMsg(self.m_DebugPlayer, self.m_Server, '%s LoadError' % sRelativePath)
            return False

        oBT.SetPathName(sRelativePath)
        if bLoadResult:
            if sRelativePath in self.m_BehaviorTrees:
                oOld = self.m_BehaviorTrees.pop(sRelativePath)
                oOld.Clear()
            self.m_BTStr[sRelativePath] = sCode
            self.m_BTData[sRelativePath] = dCode
            self.m_BehaviorTrees[sRelativePath] = oBT
        return bLoadResult

    
    def CreateDebugBTTask(self, sRelativePath):
        if sRelativePath not in self.m_BehaviorTrees:
            return GetWorkSpace().CreateBehaviorTreeTask(sRelativePath)
        oBT = self.m_BehaviorTrees[sRelativePath]
        oTask = oBT.CreateAndInitTask()
        return oTask

    
    def CreateDebugFsmTask(self, sRelativePath):
        if sRelativePath not in self.m_BehaviorTrees:
            oFsm = self.m_GameSpace.CreateFsm(sRelativePath)
        else:
            oFsm = self.m_BehaviorTrees[sRelativePath]
        return oFsm.CreateTask()

    
    def SetDebugTarget(self, iTarget):
        self.m_DebugTarget = iTarget


