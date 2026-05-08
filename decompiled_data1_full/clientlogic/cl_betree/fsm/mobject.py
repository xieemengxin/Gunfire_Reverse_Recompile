# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fsm/mobject.pyc
# RelativePath: clientlogic/cl_betree/fsm/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

import importlib
import cl_behavior
from . import fsmstate
from cl_behavior import defines
from cl_object.logging import BehaviorLog
from types import MethodType

class CFsm(object):
    CLASS_NAME = 'FSM'
    m_SID = 0
    
    def __init__(self, sBetree = None):
        self.m_Name = self.__class__.__name__
        self.m_ID = -1
        self.m_nVersion = -1
        self.m_InitialID = -1
        self.m_Children = { }
        self.m_Valid = 0
        if sBetree:
            self.LoadProperties(sBetree)

    
    def CreateTask(self):
        if self.m_Valid:
            return CFsmTask(self)

    
    def GetInitialID(self):
        return self.m_InitialID

    
    def SetInitialID(self, iInitialID):
        self.m_InitialID = iInitialID

    
    def GetParent(self):
        pass

    
    def GetId(self):
        return self.m_ID

    
    def LoadProperties(self, sRelativePath):
        sProjectPath = cl_behavior.GetTools().GetProjectTreePath()
        if sProjectPath:
            sPath = '%s.%s' % (sProjectPath, sRelativePath)
        else:
            sPath = sRelativePath
        
        try:
            module = importlib.import_module(sPath)
            self.LoadForPython(module.data)
        except:
            BehaviorLog.Error('behavior %s load fail' % sRelativePath)
            return None

        self.m_Valid = 1

    
    def LoadForPython(self, dData):
        self.m_ID = dData['ID']
        self.m_Name = dData['Name']
        self.m_nVersion = dData['Ver']
        self.m_InitialID = dData['Node'][0]['InitialID']
        dStates = dData['Node'][0]['Node']
        for dChild in dStates:
            if dChild['Class'] == 'ReferenceBehavior':
                oChildNode = fsmstate.CBeTreeState()
            else:
                oChildNode = fsmstate.CState()
            oChildNode.LoadForPython(dChild)
            self.m_Children[dChild['ID']] = oChildNode
        
        return True

    
    def CreateStateTask(self, iStateID):
        if iStateID not in self.m_Children:
            return None
        return fsmstate.CStateTask(self.m_Children[iStateID])

    
    def SetPathName(self, sName):
        pass

    
    def Clear(self):
        pass



class CFsmTask(object):
    
    def __init__(self, oFsm):
        self.m_Node = oFsm
        self.m_InitialID = oFsm.GetInitialID()
        self.m_CurStatus = -1
        self.m_Children = { }
        self.m_CurrentTask = None

    
    def Release(self):
        for oTask in self.m_Children.values():
            if 'GetNextStateID' in oTask.__dict__:
                del oTask.GetNextStateID
            oTask.Release()
        
        self.m_Children = { }
        self.m_Node = None
        self.m_CurrentTask = None

    
    def Exec(self, oAgent, iChildStatus = defines.BT_RUNNING):
        if not self.m_CurrentTask:
            self.ChangeState(oAgent, self.m_InitialID, defines.BT_SUCCESS)
        oTask = self.m_CurrentTask
        for _ in range(10):
            if not oTask:
                return defines.BT_FAILURE
            iResult = oTask.Exec(oAgent)
            iNextStateID = oTask.GetNextStateID()
            if iNextStateID < 0:
                break
            oTask = self.ChangeState(oAgent, iNextStateID, iResult)
        
        return iChildStatus

    
    def ChangeState(self, oAgent, iStatus, iResult):
        if iStatus == self.m_CurStatus:
            return None
        if iStatus not in self.m_Children:
            oTask = self.AddChildTask(iStatus)
            if not oTask:
                return None
        if self.m_CurStatus != -1:
            oOldStatus = self.m_Children[self.m_CurStatus]
            oOldStatus.OnLeave(oAgent, iResult)
        oNewStatus = self.m_Children[iStatus]
        self.m_CurStatus = iStatus
        self.m_CurrentTask = oNewStatus
        oNewStatus.OnEnter(oAgent)
        self.OnChangeStatus(oAgent)
        return oNewStatus

    
    def LockStateChange(self, iLock = 1):
        oTask = self.m_CurrentTask
        if not oTask:
            BehaviorLog.Error('fsm %s lock fail' % self.m_Node.m_Name)
            return None
        BehaviorLog.Debug('fsm %s lock %s' % (self.m_Node.m_Name, iLock))
        if iLock or 'GetNextStateID' not in oTask.__dict__:
            oTask.GetNextStateID = MethodType(fsmstate.CStateTask.GetLockNextStateID, oTask)
        elif 'GetNextStateID' in oTask.__dict__:
            del oTask.GetNextStateID

    
    def IsLockStateChange(self):
        oTask = self.m_CurrentTask
        if not oTask:
            return False
        return 'GetNextStateID' in oTask.__dict__

    
    def OnChangeStatus(self, oAgent):
        pass

    
    def AddChildTask(self, iNodeID):
        oTask = self.m_Node.CreateStateTask(iNodeID)
        if oTask:
            self.m_Children[iNodeID] = oTask
        return oTask

    
    def GetChildTaskById(self, iNodeID):
        if iNodeID in self.m_Children:
            return self.m_Children[iNodeID]
        return self.AddChildTask(iNodeID)


