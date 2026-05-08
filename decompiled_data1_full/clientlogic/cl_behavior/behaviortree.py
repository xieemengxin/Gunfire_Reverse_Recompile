# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/behaviortree.pyc
# RelativePath: clientlogic/cl_behavior/behaviortree.pyc
# Source Generated with Decompyle++
# File: behaviortree.pyc (Python 3.6)

from . import defines
from . import behaviortreetask
if 'g_NodeClass' not in globals():
    g_NodeClass = { }

def InitNode():
    if g_NodeClass:
        return None
    from .nodes.actions import action
    from .nodes.actions import assignment
    from .nodes.actions import noop
    from .nodes.actions import waitforsignal
    from .nodes.actions import waitframe
    from .nodes.composites import sequence
    from .nodes.composites import ifelse
    from .nodes.composites import parallel
    from .nodes.composites import referencebehavior
    from .nodes.composites import select
    from .nodes.composites import selectorprobability
    from .nodes.conditions import andnode
    from .nodes.conditions import condition
    from .nodes.conditions import false
    from .nodes.conditions import ornode
    from .nodes.conditions import true
    from .nodes.decorators import decoratorloopuntil
    from .nodes.decorators import decoratorloop
    from .nodes.decorators import decoratorrepeat
    from .nodes.decorators import decoratorweight
    from .nodes.decorators import decoratoralwaysfailure
    from .nodes.decorators import decoratoralwaysrunning
    from .nodes.decorators import decoratoralwayssuccess
    from .nodes import task
    from .attachments import effector
    from .attachments import event
    from .attachments import precondition
    from .fsm import fsm
    from .fsm import fsmstate
    from .fsm import transition
    from .fsm import alwaystransition
    from .fsm import fuzzytransition
    lNodeClass = [
        action.CAction,
        assignment.CAssignment,
        noop.CNoop,
        waitforsignal.CWaitforSignal,
        waitframe.CWaitFrame,
        sequence.CSequence,
        ifelse.CIfElse,
        parallel.CParallel,
        referencebehavior.CReferenceBehavior,
        select.CSelector,
        selectorprobability.CSelectorProbability,
        andnode.CAnd,
        condition.CCondition,
        false.CFalse,
        ornode.COr,
        true.CTrue,
        decoratoralwaysfailure.CDecoratorAlwaysFailure,
        decoratoralwaysrunning.CDecoratorAlwaysRunning,
        decoratoralwayssuccess.CDecoratorAlwaysSuccess,
        decoratorloopuntil.CDecoratorLoopUntil,
        decoratorloop.CDecoratorLoop,
        decoratorrepeat.CDecoratorRepeat,
        decoratorweight.CDecoratorWeight,
        task.CTask,
        effector.CEffector,
        event.CEvent,
        precondition.CPrecondition,
        fsm.CFsm,
        fsmstate.CState,
        transition.CTransition,
        alwaystransition.CAlwaysTransition,
        fuzzytransition.CFuzzyTransition]
    for oClass in lNodeClass:
        g_NodeClass[oClass.CLASS_NAME] = oClass
    


class CBehaviorNode(object):
    
    def __init__(self):
        self.m_ID = -1
        self.m_Name = self.__class__.__name__
        self.m_PathName = self.m_Name
        self.m_Parent = None
        self.m_Children = []
        self.m_bHasEvents = False
        self.m_LoadAttachment = False
        self.m_LocalProps = { }
        self.m_PreConditions = []
        self.m_Events = []
        self.m_Effectors = []
        self.m_PrecondFlag = 0
        self.m_EffectorFlag = 0
        self.m_CustomCondition = None

    
    def Create(sClassName):
        InitNode()
        if sClassName in g_NodeClass:
            return g_NodeClass[sClassName]()
        raise ValueError('没有注册此种节点类型%s' % sClassName)

    Create = staticmethod(Create)
    
    def GetBelongTreePath(self, pAgent):
        from . import debug
        oParent = self
        sRootName = ''
        while True:
            if oParent:
                if oParent.CLASS_NAME in ('BehaviorTree', 'ReferenceBehavior'):
                    sRootName = debug.GetModuleNameByBehaviorTree(pAgent, oParent)
                    sRootName = sRootName if sRootName else oParent.GetName()
                    break
                oParent = oParent.GetParent()
                continue
        return sRootName

    
    def GetName(self):
        return self.m_Name

    
    def SetName(self, sName):
        self.m_Name = sName

    
    def GetPathName(self):
        return self.m_PathName

    
    def SetPathName(self, sName):
        self.m_PathName = sName

    
    def GetChildrenCount(self):
        return len(self.m_Children)

    
    def GetChildren(self):
        return self.m_Children

    
    def GetChild(self, index):
        return self.m_Children[index]

    
    def IndexOfChild(self, oNode):
        if oNode in self.m_Children:
            return self.m_Children.index(oNode)

    
    def GetParent(self):
        return self.m_Parent

    
    def CreateAndInitTask(self):
        oTask = self.CreateTask()
        oTask.Init(self)
        return oTask

    
    def SetClassNameString(self, className):
        self.m_ClassName = className

    
    def HasEvents(self):
        return self.m_bHasEvents

    
    def SetId(self, iID):
        self.m_ID = iID

    
    def GetId(self):
        return self.m_ID

    
    def AddChild(self, oChild):
        return False

    
    def InsertChild(self, nIndex, oChild):
        return False

    
    def RemoveChild(self, oChild):
        oChild.m_Parent = None
        if oChild in self.m_Children:
            self.m_Children.remove(oChild)

    
    def AddPreCodition(self, oAttachment):
        self.m_PreConditions.append(oAttachment)
        self.m_PrecondFlag |= oAttachment.GetPhase()
        return True

    
    def RemovePreCondition(self, oAttachment):
        if oAttachment in self.m_PreConditions:
            self.m_PreConditions.remove(oAttachment)
            self.m_PrecondFlag = 0
            for o in self.m_PreConditions:
                self.m_PrecondFlag |= o.GetPhase()
            

    
    def IndexOfPreCondition(self, oAttachment):
        if oAttachment in self.m_PreConditions:
            return self.m_PreConditions.index(oAttachment)

    
    def InsertPreCondition(self, nIndex, oAttachment):
        self.m_PreConditions.insert(nIndex, oAttachment)
        self.m_PrecondFlag |= oAttachment.GetPhase()
        return True

    
    def GetPreConditionCount(self):
        return len(self.m_PreConditions)

    
    def MoveAttachInfo(self, oNode):
        oNode.m_Events = self.m_Events
        oNode.m_bHasEvents = self.m_bHasEvents
        oNode.m_PreConditions = self.m_PreConditions
        oNode.m_PrecondFlag = self.m_PrecondFlag
        oNode.m_Effectors = self.m_Effectors
        oNode.m_EffectorFlag = self.m_EffectorFlag
        self.m_Events = []
        self.m_bHasEvents = False
        self.m_PreConditions = []
        self.m_PrecondFlag = False
        self.m_Effectors = []
        self.m_EffectorFlag = False

    
    def GetPreConditions(self):
        return self.m_PreConditions

    
    def AddEffector(self, oAttachment):
        self.m_Effectors.append(oAttachment)
        self.m_EffectorFlag |= oAttachment.GetPhase()
        return True

    
    def RemoveEffector(self, oAttachment):
        if oAttachment in self.m_Effectors:
            self.m_Effectors.remove(oAttachment)
            self.m_EffectorFlag = 0
            for o in self.m_Effectors:
                self.m_EffectorFlag |= o.GetPhase()
            

    
    def GetEffectors(self):
        return self.m_Effectors

    
    def IndexOfEffector(self, oAttachment):
        if oAttachment in self.m_Effectors:
            return self.m_Effectors.index(oAttachment)

    
    def InsertEffector(self, nIndex, oAttachment):
        self.m_Effectors.insert(nIndex, oAttachment)
        self.m_EffectorFlag |= oAttachment.GetPhase()
        return True

    
    def GetEffectorsCount(self):
        return len(self.m_Effectors)

    
    def AddEvent(self, oEvent):
        self.m_Events.append(oEvent)
        self.m_bHasEvents = True
        oParent = self.GetParent()
        while True:
            if oParent:
                oParent.SetHasEventFlag(True)
                oParent = oParent.GetParent()
                continue
        return True

    
    def RemoveEvent(self, oEvent):
        if oEvent in self.m_Events:
            self.m_Events.remove(oEvent)
        if self.m_Events:
            self.m_bHasEvents = True
        else:
            stack = [ o for o in self.m_Children ]
            while True:
                if stack:
                    o = stack.pop()
                    if o.GetHasEventFlag():
                        self.m_bHasEvents = True
                        return None
                    stack.extend([ oSubNode for oSubNode in o.GetChildren() ])
                    continue
            self.m_bHasEvents = False

    
    def GetEvents(self):
        return self.m_Events

    
    def IndexOfEvent(self, oAttachment):
        if oAttachment in self.m_Events:
            return self.m_Events.index(oAttachment)

    
    def InsertEvent(self, nIndex, oAttachment):
        self.m_Events.insert(nIndex, oAttachment)
        self.m_bHasEvents = True
        oParent = self.GetParent()
        while True:
            if oParent:
                oParent.SetHasEventFlag(True)
                oParent = oParent.GetParent()
                continue
        return True

    
    def GetEventsCount(self):
        return len(self.m_Events)

    
    def SetHasEventFlag(self, bFlag):
        self.m_bHasEvents = bFlag

    
    def GetHasEventFlag(self):
        return self.m_bHasEvents

    
    def EvaluateCustomCondition(self, oAgent):
        if self.m_CustomCondition:
            return self.m_CustomCondition.Evaluate(oAgent)
        return False

    
    def Clear(self):
        self.m_ClassName = ''
        self.m_Parent = None
        for oChild in self.m_Children:
            oChild.Clear()
        
        self.m_Children = []
        self.m_bHasEvents = False
        self.m_LoadAttachment = False
        self.m_LocalProps = { }
        for oPre in self.m_PreConditions:
            oPre.Clear()
        
        self.m_PreConditions = []
        for oEvent in self.m_Events:
            oEvent.Clear()
        
        self.m_Events = []
        for oEffectors in self.m_Effectors:
            oEffectors.Clear()
        
        self.m_Effectors = []

    
    def Load(iVersion, sAgentType, dData):
        oNode = CBehaviorNode.Create(dData['Class'])
        if oNode:
            oNode.SetId(dData['ID'])
            oNode.LoadNode(True, iVersion, sAgentType, dData)
        return oNode

    Load = staticmethod(Load)
    
    def LoadNode(self, bNode, iVersion, sAgentType, dData):
        bHasEvent = self.HasEvents()
        if bNode:
            for dChild in dData.get('Node', ()):
                oChildNode = CBehaviorNode.Load(iVersion, sAgentType, dChild)
                if not bHasEvent:
                    pass
                bHasEvent = oChildNode.HasEvents()
                self.AddChild(oChildNode)
            
            for dChild in dData.get('Attachment', ()):
                bRet = self.LoadAttachment(iVersion, sAgentType, bHasEvent, dChild)
                if not bHasEvent:
                    pass
                bHasEvent = bRet
            
        else:
            for dChild in dData.get('Attachment', ()):
                bHasEvent = self.LoadAttachment(iVersion, sAgentType, bHasEvent, dChild)
            
        self.LoadProperties(iVersion, sAgentType, dData)
        if not self.m_bHasEvents:
            pass
        self.m_bHasEvents = bHasEvent

    
    def LoadAttachment(self, iVersion, sAgentType, bHasEvent, dData):
        oAttachment = CBehaviorNode.Create(dData['Class'])
        oAttachment.SetClassNameString(dData['Class'])
        oAttachment.SetId(dData['ID'])
        oAttachment.LoadNode(False, iVersion, sAgentType, dData)
        self.Attach(oAttachment, dData)
        if dData['Class'] == 'Event':
            bHasEvent = True
        return bHasEvent

    
    def Attach(self, oAttachment, dData):
        if dData['Flag'] == 'precondition':
            self.AddPreCodition(oAttachment)
        elif dData['Flag'] == 'effector':
            self.AddEffector(oAttachment)
        else:
            self.m_Events.append(oAttachment)

    
    def CheckEvent(self, oAgent, sEventName, dEventParams):
        for oEvent in self.m_Events:
            if oEvent.GetEventName() == sEventName:
                oEvent.SwitchTo(oAgent, dEventParams)
                if oEvent.TriggeredOnce():
                    return False
        
        return True

    
    def CollectEventName(self, lstName):
        if not self.m_bHasEvents:
            return None
        for oEvent in self.m_Events:
            lstName.append(oEvent.GetEventName())
        
        for oChild in self.m_Children:
            oChild.CollectEventName(lstName)
        

    
    def CheckPreconditions(self, oAgent, bIsAlive):
        if not self.m_PreConditions:
            return True
        iPhase = defines.E_UPDATE if bIsAlive else defines.E_ENTER
        if not iPhase & self.m_PrecondFlag:
            return True
        bFirst = True
        bCombine = False
        for oAttachment in self.m_PreConditions:
            if iPhase & oAttachment.GetPhase():
                bOneAns = oAttachment.Evaluate(oAgent)
                if not isinstance(bOneAns, bool):
                    bOneAns = bOneAns == defines.BT_SUCCESS
                if bFirst:
                    bFirst = False
                    bCombine = bOneAns
                    continue
                if oAttachment.IsAnd():
                    if bCombine:
                        pass
                    bCombine = bOneAns
                    continue
                if not bCombine:
                    pass
            bCombine = bOneAns
        
        return bCombine

    
    def ApplyEffects(self, oAgent, iPhase):
        if not self.m_Effectors:
            return None
        if not iPhase & self.m_EffectorFlag:
            return None
        for oAttachment in self.m_Effectors:
            if iPhase & oAttachment.GetPhase():
                oAttachment.Evaluate(oAgent)
        

    
    def IsManagingChildrenAsSubTrees(self):
        return False

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        pass

    
    def CreateTask(self):
        pass

    
    def UpdateImpl(self, oAgent, iChildStatus):
        return defines.BT_FAILURE

    
    def GetExportData(self):
        dData = {
            'ID': self.m_ID,
            'Class': self.CLASS_NAME }
        lTemp = []
        for o in self.m_Effectors:
            lTemp.append(o.GetExportData())
        
        for o in self.m_PreConditions:
            lTemp.append(o.GetExportData())
        
        for o in self.m_Events:
            lTemp.append(o.GetExportData())
        
        if lTemp:
            dData['Attachment'] = tuple(lTemp)
        return dData



class CDecoratorNode(CBehaviorNode):
    
    def __init__(self):
        super(CDecoratorNode, self).__init__()
        self.m_bDecorateWhenChildEnds = False

    
    def AddChild(self, oChild):
        if len(self.m_Children) >= 1:
            return False
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        if len(self.m_Children) >= 1:
            return False
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True

    
    def IsManagingChildrenAsSubTrees(self):
        return True

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        self.m_bDecorateWhenChildEnds = dProperties['DecorateWhenChildEnds'] if 'DecorateWhileChildEns' in dProperties else False

    
    def GetExportData(self):
        dData = super(CDecoratorNode, self).GetExportData()
        dData.update({
            'DecorateWhenChildEnds': self.m_bDecorateWhenChildEnds })
        return dData



class CBehaviorTree(CBehaviorNode):
    CLASS_NAME = 'BehaviorTree'
    
    def __init__(self):
        super(CBehaviorTree, self).__init__()
        self.m_Name = ''
        self.m_AgentType = ''
        self.m_bIsFSM = False
        self.m_nVersion = 1

    
    def GetBehaviorFileName(self):
        from . import workspace
        return workspace.GetInstance().GetModuleNameByBehaviorTree(self)

    
    def IsFSM(self):
        return self.m_bIsFSM

    
    def GetAgentType(self):
        return self.m_AgentType

    
    def InstantiatePars(self, vars):
        pass

    
    def CreateTask(self):
        return behaviortreetask.CBehaviorTreeTask()

    
    def AddPreCodition(self, oAttachment):
        return False

    
    def AddEffector(self, oAttachment):
        return False

    
    def LoadForPython(self, dData):
        self.SetClassNameString(dData['Name'])
        self.m_Name = dData['Name']
        self.m_bIsFSM = dData['IsFSM']
        self.m_AgentType = dData['AgentType']
        self.m_ID = dData.get('ID', -1)
        self.m_nVersion = dData['Ver']
        self.LoadNode(True, dData['Ver'], dData['AgentType'], dData)
        return True

    
    def GetExportToPython(self):
        stack = []
        for o in self.m_Children:
            stack.append(o)
        
        dRoot = self.GetExportData()
        stack = [
            (self, dRoot)]
        while True:
            if stack:
                (oNode, dNodeData) = stack.pop()
                if oNode.m_Children:
                    dNodeData['Node'] = []
                for oSubNode in oNode.m_Children:
                    dSubData = oSubNode.GetExportData()
                    dNodeData['Node'].append(dSubData)
                    stack.append((oSubNode, dSubData))
                
                continue
        return dRoot

    
    def IsManagingChildrenAsSubTrees(self):
        return True

    
    def GetExportData(self):
        dData = super(CBehaviorTree, self).GetExportData()
        dData.update({
            'AgentType': self.m_AgentType,
            'IsFSM': self.m_bIsFSM,
            'Ver': self.m_nVersion })
        dData.pop('Class')
        return dData

    
    def AddChild(self, oChild):
        if len(self.m_Children) >= 1:
            return False
        oChild.m_Parent = self
        self.m_Children.append(oChild)
        return True

    
    def InsertChild(self, nIndex, oChild):
        if len(self.m_Children) >= 1:
            return False
        oChild.m_Parent = self
        self.m_Children.insert(nIndex, oChild)
        return True


