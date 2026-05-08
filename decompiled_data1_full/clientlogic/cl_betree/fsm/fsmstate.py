# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fsm/fsmstate.pyc
# RelativePath: clientlogic/cl_betree/fsm/fsmstate.pyc
# Source Generated with Decompyle++
# File: fsmstate.pyc (Python 3.6)

from cl_only import Functor
from cl_commondefines import SIDE_TYPE_VERTIGO, WARRIOR_MONSTER, WARRIOR_SERVANT
import cllib.lib_flag
if cllib.lib_flag.g_UseCBehavior:
    from pubbehaviorc import defines, meta
else:
    from cl_behavior import defines, meta
from .. import fuzzy

class CState(object):
    CLASS_NAME = 'State'
    m_ID = -1
    
    def __init__(self):
        self.m_Name = ''
        self.m_Method = None
        self.m_Transition = []
        self.m_Precondition = []
        self.m_Effectors = []
        self.m_Fuzzy = []

    
    def GetId(self):
        return self.m_ID

    
    def GetName(self):
        return self.m_Name

    
    def LoadForPython(self, dData):
        self.LoadAttachment(dData)
        self.m_Method = meta.ParseMethod(dData, 'Method', None)

    
    def LoadAttachment(self, dData):
        self.m_ID = dData['ID']
        lstAttachment = dData['Attachment'] if 'Attachment' in dData else ()
        for dChild in lstAttachment:
            if dChild['Class'] == 'AlwaysTransition':
                func = Functor(CState.EvaluateTransitionByResult, dChild['TransitionPhase'])
                self.m_Transition.append((dChild['TargetFSMNodeID'], func))
                continue
            if dChild['Class'] == 'Transition':
                iTransitionPhase = dChild['TransitionPhase'] if 'TransitionPhase' in dChild else defines.ETP_ALWAYS
                func = Functor(CState.EvaluateTransition, dChild['Method'][0], iTransitionPhase)
                self.m_Transition.append((dChild['TargetFSMNodeID'], func))
                continue
            if dChild['Class'] == 'FuzzyTransition':
                oFuzzy = meta.ParseMethod(dChild, 'Method', None)(None)
                self.m_Fuzzy.append((dChild['TargetFSMNodeID'], oFuzzy))
                continue
            if dChild['Class'] == 'Precondition' and dChild['Phase'] & defines.E_ENTER:
                func = meta.ParseMethod(dChild, 'Method', None)
                self.m_Precondition.append(func)
                continue
            if dChild['Class'] == 'Effector':
                func = meta.ParseMethod(dChild, 'Method', None)
                self.m_Effectors.append(func)
        
        if self.m_Fuzzy and self.m_Transition:
            pass

    
    def EvaluateTransition(func, iTransitionPhase, oAgent, iResult):
        if iTransitionPhase == defines.ETP_SUCCESS and iResult != defines.BT_SUCCESS:
            return False
        if iTransitionPhase == defines.ETP_FAILURE and iResult != defines.BT_FAILURE:
            return False
        if iTransitionPhase == defines.ETP_EXIT and iResult != defines.BT_SUCCESS and iResult != defines.BT_FAILURE:
            return False
        return func(oAgent)

    EvaluateTransition = staticmethod(EvaluateTransition)
    
    def EvaluateTransitionByResult(iPhase, oAgent, iResult):
        if iPhase == defines.ETP_ALWAYS:
            return True
        if iResult == defines.BT_SUCCESS:
            if iPhase == defines.ETP_SUCCESS or iPhase == defines.ETP_EXIT:
                return True
        if iResult == defines.BT_FAILURE:
            if iPhase == defines.ETP_FAILURE or iPhase == defines.ETP_EXIT:
                return True
        return False

    EvaluateTransitionByResult = staticmethod(EvaluateTransitionByResult)
    
    def Update(self, oAgent, oTask):
        if self.m_Method:
            iResult = self.m_Method(oAgent)
        else:
            iResult = defines.BT_SUCCESS
        if self.m_Fuzzy or iResult != defines.BT_RUNNING:
            self.UpdateFuzzy(oAgent, oTask)
        else:
            CState.UpdateTransitions(oAgent, oTask, self.m_Transition, iResult)
        return iResult

    
    def UpdateFuzzy(self, oAgent, oTask):
        fBest = -1
        iTargetStateID = -1
        dData = { }
        lstArgs = oAgent.m_Game.m_WarMgr.Query('DebugMonster', ())
        iDebug = 1 if 'fuzzy' in lstArgs else 0
        sDebugInfo = ''
        for iStateID, oFzMod in self.m_Fuzzy:
            fDesirability = oFzMod.GetDesirability(oAgent)
            if fDesirability > fBest:
                iTargetStateID = iStateID
                fBest = fDesirability
            dData[iStateID] = fDesirability
            if iDebug:
                sDebugInfo += '<color=#FFFF00>%s 得分:%0.2f\n<color=#FFFFFF>%s' % (oFzMod.m_Name, fDesirability, oFzMod.CollectDebugInfo())
        
        oTask.m_NextStateID = iTargetStateID
        if iDebug:
            import cl_gamegm
            oAgent.SetData('FuzzyDebug', sDebugInfo)
            cl_gamegm.SendMonsterDebugInfo(oAgent.m_OwnerObj)

    
    def UpdateTransitions(oAgent, oTask, lstTransitions, iResult):
        for iTargetStateID, evaluateFunc in lstTransitions:
            if evaluateFunc(oAgent, iResult):
                oTask.m_NextStateID = iTargetStateID
                return True
        
        return False

    UpdateTransitions = staticmethod(UpdateTransitions)
    
    def OnEnter(self, oAgent, oTask, *args):
        for func in self.m_Precondition:
            func(oAgent)
        

    
    def OnLeave(self, oAgent, oTask, iResult):
        for func in self.m_Effectors:
            func(oAgent)
        



class CBeTreeState(CState):
    CLASS_NAME = 'BeTreeState'
    
    def LoadForPython(self, dData):
        self.LoadAttachment(dData)
        self.m_BTPath = dData['ReferenceBehavior']
        self.m_Name = dData['ReferenceBehavior']

    
    def Update(self, oAgent, oTask):
        iResult = oAgent.TrueBTExec()
        if oAgent.m_OwnerObj.m_Side == SIDE_TYPE_VERTIGO:
            return iResult
        if self.m_Fuzzy or iResult != defines.BT_RUNNING:
            self.UpdateFuzzy(oAgent, oTask)
        else:
            CState.UpdateTransitions(oAgent, oTask, self.m_Transition, iResult)
        return iResult

    
    def OnEnter(self, oAgent, oTask, sTempBTPath):
        super(CBeTreeState, self).OnEnter(oAgent, oTask)
        oAgent.BTSetCurrent(sTempBTPath if sTempBTPath else self.m_BTPath)
        oTarget = oAgent.m_OwnerObj
        if oTarget.m_FightType & WARRIOR_MONSTER:
            lstArgs = oAgent.m_Game.m_WarMgr.Query('DebugMonster', ())
            if 'btree' in lstArgs:
                import cl_gamegm
                cl_gamegm.SendMonsterDebugInfo(oAgent.m_OwnerObj)
            elif oTarget.m_FightType & WARRIOR_SERVANT:
                lstArgs = oAgent.m_Game.m_WarMgr.Query('DebugServant', ())
                if 'btree' in lstArgs:
                    import cl_gamegm
                    cl_gamegm.SendServantDebugInfo(oAgent.m_OwnerObj)

    
    def OnLeave(self, oAgent, oTask, iResult):
        oTarget = oAgent.m_OwnerObj
        if oTarget.m_FightType & WARRIOR_MONSTER:
            lstArgs = oAgent.m_Game.m_WarMgr.Query('DebugMonster', ())
            if 'btree' in lstArgs:
                import cl_gamegm
                cl_gamegm.SendMonsterDebugInfo(oAgent.m_OwnerObj)
            elif oTarget.m_FightType & WARRIOR_SERVANT:
                lstArgs = oAgent.m_Game.m_WarMgr.Query('DebugServant', ())
                if 'btree' in lstArgs:
                    import cl_gamegm
                    cl_gamegm.SendServantDebugInfo(oAgent.m_OwnerObj)
        None(CBeTreeState, self).OnLeave(oAgent, oTask, iResult)
        if iResult == defines.BT_RUNNING:
            oAgent.m_CurrentBT.Abort(oAgent)



class CStateTask(object):
    m_TempBTPath = ''
    
    def __init__(self, oState):
        self.m_Node = oState
        self.m_PreStateID = -1
        self.m_NextStateID = -1

    
    def Release(self):
        self.m_Node = None

    
    def GetNextStateID(self):
        return self.m_NextStateID

    
    def GetLockNextStateID(self):
        return -1

    
    def OnEnter(self, oAgent):
        self.m_NextStateID = -1
        self.m_Node.OnEnter(oAgent, self, self.m_TempBTPath)

    
    def OnLeave(self, oAgent, iResult):
        self.m_NextStateID = -1
        self.m_Node.OnLeave(oAgent, self, iResult)

    
    def Exec(self, oAgent):
        return self.m_Node.Update(oAgent, self)


