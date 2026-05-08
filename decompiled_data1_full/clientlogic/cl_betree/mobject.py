# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/mobject.pyc
# RelativePath: clientlogic/cl_betree/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import Functor
from cl_behavior.defines import BT_RUNNING, BT_INVALID
from cl_action.ac_common import HaltAllCasting
from cl_object.logging import BehaviorLog
import cl_world
import cl_msgcenter
import cl_behavior
EVENT_SELF = 0
EVENT_SCENE = 1
SWITCH_TREE_VERTIGO = 1
SWITCH_TREE_SNEER = 2
SWITCH_TREE_MONSTERCHANGE = 3
SWITCH_TREE_PRIORITY = {
    SWITCH_TREE_MONSTERCHANGE: 3,
    SWITCH_TREE_VERTIGO: 2,
    SWITCH_TREE_SNEER: 1 }

class CAgent(cl_behavior.GetAgentClass()):
    m_EventKey = { }
    m_AgentEventKey = { }
    
    def __init__(self):
        super(CAgent, self).__init__()
        self.m_Game = None
        self.m_OwnerObj = None
        self.m_CallTime = None
        self.m_Fsm = None
        self.m_Pause = []
        self.m_AttentionInfo = { }
        self.m_GlobalAttentionInfo = { }
        self.m_AgentEvent = []
        self.m_SceneData = None
        self.m_RestoreTree = ''
        self.m_SwitchTreeInfo = { }
        self.m_CurMaxTreePriority = 0

    
    def Config(self, oOwner, dConfig):
        self.m_OwnerObj = oOwner
        oGame = oOwner.m_Game
        self.m_Game = oGame
        iTimerID = oGame.NewNPCID()
        self.m_CallTime = cl_world.CObject(oGame, iTimerID)
        oGame.CreateObject(iTimerID, self.m_CallTime)
        self.m_Config.update(dConfig)

    
    def Release(self):
        super(CAgent, self).Release()
        if self.m_Fsm:
            self.m_Fsm.Release()
            self.m_Fsm = None
        self.ClearAttention(self.m_OwnerObj)
        self.m_Game = None
        self.m_OwnerObj = None
        self.m_SceneData = None
        if self.m_CallTime:
            self.m_CallTime.RemoveFromList()
            self.m_CallTime = None

    
    def __str__(self):
        oCurrentBT = self.PYGetCurrentBT()
        if oCurrentBT:
            sPathName = oCurrentBT.GetPathName()
        else:
            sPathName = 'None'
        return '%s-%s-%s' % (self.__class__, sPathName, self.m_OwnerObj)

    
    def __repr__(self):
        return self.__str__()

    
    def PYGetCurrentBT(self):
        return self.m_CurrentBT

    
    def GetTreeVar(self, sKey, default = None):
        if not (self.m_CurrentBT) or sKey not in self.m_CurrentBT.m_LocalVars:
            return default
        return self.m_CurrentBT.m_LocalVars[sKey]

    
    def UpdateData(self, sData, value):
        if sData in self.m_Data:
            if isinstance(value, dict):
                self.m_Data[sData].update(value)
            elif isinstance(value, int):
                self.m_Data[sData] += value
            else:
                self.m_Data[sData] = value

    
    def SetFsm(self, oFsmTask):
        if self.m_Fsm:
            self.m_Fsm.Release()
        self.m_Fsm = oFsmTask

    
    def BTExec(self):
        if self.m_bActive:
            self.UpdateVariableRegistry()
            if self.m_Fsm:
                return self.m_Fsm.Exec(self)
            self.m_ReferenceTree = False
            s = self.TrueBTExec()
            while True:
                if self.m_ReferenceTree and s == BT_RUNNING:
                    self.m_ReferenceTree = False
                    s = self.TrueBTExec()
                    continue
            return s
        return BT_INVALID

    
    def PauseAgent(self, sReason):
        self.m_Pause.append(sReason)
        self.m_bActive = False

    
    def ResumeAgent(self, sReason):
        lstPause = []
        for sPauseReason in self.m_Pause:
            if sPauseReason == sReason:
                continue
            lstPause.append(sPauseReason)
        
        self.m_Pause = lstPause
        if not self.m_Pause:
            self.m_bActive = True

    
    def QueryPauseAgent(self, sReason):
        return sReason in self.m_Pause

    
    def OnBuildInCreateTimerCallBack(self, sNodeName, *args, **kwargs):
        if sNodeName == 'WaitFrame':
            self.Remove_Call_Out('WaitFrame')
            (_cbfunc, iRemainFrame) = args
            self.Call_Out(self.WaitFrameCallBack, iRemainFrame, 'WaitFrame')

    
    def OnBuildInDestroyTimerCallBack(self, sNodeName, *args, **kwargs):
        if sNodeName == 'WaitFrame':
            self.Remove_Call_Out('WaitFrame')

    
    def WaitFrameCallBack(self):
        self.Remove_Call_Out('WaitFrame')
        if self.IsActive():
            self.BTExec()

    
    def AddSwitchCurrentBT(self, iType, sBTName, sReason):
        oCurrentBT = self.m_CurrentBT
        if not oCurrentBT:
            return False
        sOldTree = oCurrentBT.GetPathName()
        if sOldTree == sBTName:
            return False
        if not self.m_RestoreTree:
            self.m_RestoreTree = sOldTree
        if self.SetSwitchPriority(iType, sBTName, sReason):
            self.SwitchCurrentBT(sReason)
        return True

    
    def RemoveSwitchCurrentBT(self, iType, sReason):
        oCurrentBT = self.m_CurrentBT
        if not oCurrentBT:
            return False
        sOldTree = oCurrentBT.GetPathName()
        if sOldTree == self.m_RestoreTree:
            return False
        if self.ClearSwitchPriority(iType, sReason):
            self.SwitchCurrentBT(sReason)
        return True

    
    def SetSwitchPriority(self, iAddType, sAddTree, sReason):
        sLog = 'setswitchpriority %s %s %s %s' % (self.m_Fsm.m_Node.m_Name, iAddType, sAddTree, sReason)
        if iAddType not in SWITCH_TREE_PRIORITY or not sAddTree:
            BehaviorLog.Alert('%s err' % sLog)
            return False
        BehaviorLog.Debug(sLog)
        iAddPriority = SWITCH_TREE_PRIORITY[iAddType]
        self.m_SwitchTreeInfo[iAddPriority] = sAddTree
        if self.m_CurMaxTreePriority > iAddPriority:
            return False
        self.m_CurMaxTreePriority = iAddPriority
        return True

    
    def ClearSwitchPriority(self, iRemoveType, sReason):
        sLog = 'clearswitchpriority %s %s %s' % (self.m_Fsm.m_Node.m_Name, iRemoveType, sReason)
        if iRemoveType not in SWITCH_TREE_PRIORITY:
            BehaviorLog.Alert('%s err' % sLog)
            return False
        BehaviorLog.Debug(sLog)
        iRemovePriority = SWITCH_TREE_PRIORITY[iRemoveType]
        self.m_SwitchTreeInfo.pop(iRemovePriority, '')
        if iRemovePriority != self.m_CurMaxTreePriority:
            return False
        if not self.m_SwitchTreeInfo:
            self.m_CurMaxTreePriority = 0
        else:
            iNewMaxPriority = max(self.m_SwitchTreeInfo)
            self.m_CurMaxTreePriority = iNewMaxPriority
        return True

    
    def SwitchTreeByPriority(self):
        if not self.m_CurMaxTreePriority:
            self.m_Fsm.LockStateChange(iLock = 0)
            sEnableBT = self.m_RestoreTree
            self.m_RestoreTree = ''
        elif not self.m_Fsm.IsLockStateChange():
            self.m_Fsm.LockStateChange(iLock = 1)
        sEnableBT = self.m_SwitchTreeInfo[self.m_CurMaxTreePriority]
        if not sEnableBT:
            BehaviorLog.Alert('switchtree fail %s %s %s' % (self.m_CurMaxTreePriority, self.m_SwitchTreeInfo, self.m_RestoreTree))
            return None
        self.BTSetCurrent(sEnableBT)

    
    def SwitchCurrentBT(self, sReason):
        oTarget = self.m_OwnerObj
        HaltAllCasting(oTarget, sReason)
        oTarget.Stop()
        self.SwitchTreeByPriority()

    
    def Call_Out(self, func, delay, sFlag):
        self.m_CallTime.Call_Out(func, delay, sFlag)

    
    def Remove_Call_Out(self, sFlag):
        self.m_CallTime.Remove_Call_Out(sFlag)

    
    def RemoveAllCallOut(self):
        self.m_CallTime.RemoveAllCallOut()

    
    def Find_Call_Out(self, sFlag):
        return self.m_CallTime.Find_Call_Out(sFlag)

    
    def OnRegisterEvent(self, lstEvent):
        for sEventName in lstEvent:
            if sEventName not in self.m_EventKey:
                continue
            (iMsg, iSub, iAttentionWay, _) = self.m_EventKey[sEventName]
            if iAttentionWay == EVENT_SELF:
                self.AddAttention(self.m_OwnerObj, iMsg, Functor(OnEventCallBack, sEventName), 'betreeagent', iSub)
                continue
            if iAttentionWay == EVENT_SCENE:
                self.AddSceneAttention(self.m_OwnerObj, iMsg, Functor(OnEventCallBack, sEventName), 'betreeagent', iSub)
        

    
    def AddAttention(self, oOwner, iMsg, Func, sKey, iSub = -1, iOnce = 0, iPriority = 0):
        tKey = (iMsg, iSub, sKey)
        if tKey in self.m_AttentionInfo:
            return None
        self.m_AttentionInfo[tKey] = 1
        cl_msgcenter.AddFunction(oOwner, iMsg, Func, sKey, iSub, iOnce, iPriority)

    
    def DoneAttention(self, oOwner, iMsg, sKey, iSub = -1):
        if (iMsg, iSub, sKey) in self.m_AttentionInfo:
            self.m_AttentionInfo.pop((iMsg, iSub, sKey))
        cl_msgcenter.DoneEvent(oOwner, iMsg, sKey, iSub)

    
    def ClearAttention(self, oOwner):
        lstClear = self.m_AttentionInfo.keys()
        self.m_AttentionInfo = { }
        for iMsg, iSub, sKey in lstClear:
            cl_msgcenter.DoneEvent(oOwner, iMsg, sKey, iSub)
        

    
    def AddSceneAttention(self, oOwner, iMsg, cbFunc, sKey, iSub = -1):
        oScene = self.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            self.m_GlobalAttentionInfo[(iMsg, iSub, sKey)] = cbFunc
            return None
        oScene.m_SceneData.AddAttention(iMsg, iSub, oOwner.m_ID, sKey, cbFunc)

    
    def DoneSceneAttention(self, oOwner, iMsg, sKey, iSub = -1):
        oScene = self.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return None
        oScene.m_SceneData.DoneAtention(oOwner.m_ID, iMsg, iSub, sKey)

    
    def EnterScene(self, oScene):
        oOwner = self.m_OwnerObj
        for (iMsg, iSub, sKey), cbFunc in self.m_GlobalAttentionInfo.items():
            self.AddSceneAttention(oOwner, iMsg, cbFunc, sKey, iSub)
        
        lstAreaName = self.GetConfig('SceneAttentionArea', [])
        if lstAreaName:
            setArea = set(lstAreaName)
            self.SetData('AttentionArea', setArea)
        self.m_SceneData = oScene.m_SceneData

    
    def LeaveScene(self):
        self.m_SceneData = None

    
    def CheckInAttentionArea(self, oTarget):
        setArea = self.GetData('AttentionArea')
        if not setArea:
            return 1
        if set(oTarget.m_Area) & setArea:
            return 1
        return 0

    
    def AgentAddAttention(self, sMsgType):
        if sMsgType not in self.m_AgentEventKey:
            return False
        (iMsg, iSub, iAttentionWay, cbFunc, sKey) = self.m_AgentEventKey[sMsgType]
        self.m_AgentEvent.append(sMsgType)
        if iAttentionWay == EVENT_SELF:
            self.AddAttention(self.m_OwnerObj, iMsg, cbFunc, sKey, iSub)
        elif iAttentionWay == EVENT_SCENE:
            self.AddSceneAttention(self.m_OwnerObj, iMsg, cbFunc, sKey, iSub)
        return True

    
    def ClearAgentAttention(self):
        lstAgentEvent = self.m_AgentEvent
        self.m_AgentEvent = []
        for sMsgType in lstAgentEvent:
            (iMsg, iSub, iAttentionWay, _, sKey) = self.m_AgentEventKey[sMsgType]
            if iAttentionWay == EVENT_SELF:
                self.DoneAttention(self.m_OwnerObj, iMsg, sKey, iSub)
                continue
            if iAttentionWay == EVENT_SCENE:
                self.DoneSceneAttention(self.m_OwnerObj, iMsg, sKey, iSub)
        



def OnEventCallBack(sEventName, oOwner, iMsg, sKey, dMsgInfo):
    if sEventName not in oOwner.m_Agent.m_EventKey:
        return None
    (_, _, _, lstExchange) = oOwner.m_Agent.m_EventKey[sEventName]
    dParams = { }
    for sAttr, sParams in lstExchange:
        dParams[sParams] = dMsgInfo[sAttr]
    
    oGameSpace = oOwner.m_Game.m_Betree
    oOwner.Call_Out(Functor(oGameSpace.OnEvent, oOwner.m_Agent, sEventName, dParams), 1, 'betreeevent')

