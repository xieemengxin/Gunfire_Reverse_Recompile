# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/logmanager.pyc
# RelativePath: clientlogic/cl_behavior/debug/logmanager.pyc
# Source Generated with Decompyle++
# File: logmanager.pyc (Python 3.6)

from __future__ import absolute_import
from ..defines import EActionResult, EActionType

class CLogManager(object):
    
    def Log(pAgent, sBtMsg, nActionResult):
        sAgentName = pAgent.GetName()
        if nActionResult == EActionResult.EAR_success:
            sResult = 'success'
        elif nActionResult == EActionResult.EAR_failure:
            sResult = 'failure'
        else:
            sResult = 'running'
        sText = '[tick]%s %s [%s]' % (sAgentName, sBtMsg, sResult)
        CLogManager.Print(sText)

    Log = staticmethod(Log)
    
    def Print(sText):
        print(sText)

    Print = staticmethod(Print)
    
    def SendSignal(pAgent, oNode, sAction, nResult):
        from .. import debug
        sAgentName = pAgent.GetName()
        oParent = oNode
        sRootPath = ''
        while True:
            if oParent:
                if oParent.CLASS_NAME in ('BehaviorTree',):
                    sRootPath = debug.GetModuleNameByBehaviorTree(pAgent, oParent)
                    sRootPath = sRootPath if sRootPath else oParent.GetName()
                    break
                oParent = oParent.GetParent()
                continue
        iNodeID = oNode.GetId()
        if sAction == 'enter':
            nAction = EActionType.EAT_enter
        else:
            nAction = EActionType.EAT_exit
        debug.SendNodeResult(pAgent, sAgentName, sRootPath, iNodeID, nAction, nResult)

    SendSignal = staticmethod(SendSignal)
    
    def SendBreakPointHitResult(pAgent, oNode, sAction, iHit):
        from .. import debug
        oParent = oNode
        sRootPath = ''
        while True:
            if oParent:
                if oParent.CLASS_NAME in ('BehaviorTree',):
                    sRootPath = debug.GetModuleNameByBehaviorTree(pAgent, oParent)
                    sRootPath = sRootPath if sRootPath else oParent.GetName()
                    break
                oParent = oParent.GetParent()
                continue
        iNodeID = oNode.GetId()
        if sAction == 'enter':
            nAction = EActionType.EAT_enter
        else:
            nAction = EActionType.EAT_exit
        debug.SendBreakPointHitResult(pAgent, sRootPath, iNodeID, nAction, iHit)

    SendBreakPointHitResult = staticmethod(SendBreakPointHitResult)

