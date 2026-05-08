# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/__init__.pyc
# RelativePath: clientlogic/cl_behavior/debug/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from __future__ import absolute_import
from __future__ import print_function
from cli_player import GetPlayer
import cllib.lib_flag
if cllib.lib_flag.g_UseCBehavior:
    from pubbehaviorc.tools import GetTools
else:
    from ..tools import GetTools

def CreateDebug(*args):
    from . import mobject
    return mobject.BTDebug(*args)


def CHECK_BREAKPOINT(pAgent, oNode, sAction, nResult):
    from . import logmanager
    oGameSpace = pAgent.GetGameSpace()
    oDebug = oGameSpace.m_Debug
    if oDebug.m_DebugTarget and oDebug.m_DebugTarget != pAgent.m_OwnerObj.m_ID:
        return None
    logmanager.CLogManager.SendSignal(pAgent, oNode, sAction, nResult)


def SendGameEnd(pid, iServer):
    GetTools().RpcCallFunc(iServer, __name__ + '.net.R_SendGameEnd', None, pid)


def NotifyMsg(pid, iServer, sMsg):
    import cl_interface
    import cl_notify
    if cllib.lib_flag.g_IsMobile:
        who = GetPlayer(pid)
        if not who:
            return None
        oGame = cl_interface.GetGame(who.m_GameID)
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        cl_notify.GS2CMessage(oHero, sMsg)
    else:
        GetTools().RpcCallFunc(iServer, __name__ + '.net.R_NotifyMsg', None, pid, sMsg)


def R_UpdateTree(resfunc, pid, sBTName, sCode):
    iServer = resfunc.m_FromServer
    bRet = UpdateTree(pid, sBTName, sCode)
    if bRet:
        NotifyMsg(pid, iServer, '更新行为树%s【成功】' % sBTName)
    else:
        NotifyMsg(pid, iServer, '更新行为树%s【失败】' % sBTName)


def UpdateTree(pid, sRelativePath, sCode):
    oGameSpace = GetTools().GetGameSpace(pid)
    if not oGameSpace or not oGameSpace.IsDebugging():
        return False
    bRet = oGameSpace.m_Debug.SetBTData(sRelativePath, sCode)
    if not bRet:
        return False
    return True


def R_SaveTree(resfunc, pid, lstNames, sDescription, sTaskID):
    iServer = resfunc.m_FromServer
    if cllib.lib_flag.g_IsMobile:
        NotifyMsg(pid, iServer, '手游禁止服务器导出')
        return None
    for sName in lstNames:
        bRet = TrySaveTree(pid, sName, sDescription, sTaskID)
        if not bRet:
            NotifyMsg(pid, iServer, '行为树%s无变化，请先进行在线联调或检查改动' % sName)
    


def TrySaveTree(pid, sRelativePath, sDescription, sTaskID):
    oGameSpace = GetTools().GetGameSpace(pid)
    if not oGameSpace or not oGameSpace.IsDebugging():
        return False
    bRet = oGameSpace.m_Debug.SaveBTData(sRelativePath, sDescription, sTaskID)
    return bRet


def SaveTree(iServer, *args):
    GetTools().RpcCallFunc(iServer, __name__ + '.net.R_SaveBT', None, *args)


def R_SetDebug(resfunc, pid):
    iServer = resfunc.m_FromServer
    oGameSpace = GetTools().GetGameSpace(pid)
    if oGameSpace:
        if not oGameSpace.IsDebugging():
            oDebug = CreateDebug(oGameSpace, pid, iServer)
            oGameSpace.SetDebugging(oDebug)
        iRet = 1
        NotifyMsg(pid, iServer, '设置Debug成功')
    else:
        iRet = 3
        NotifyMsg(pid, iServer, '设置Debug失败')
    resfunc(iRet)


def R_ReleaseDebug(resfunc, pid):
    iServer = resfunc.m_FromServer
    oGameSpace = GetTools().GetGameSpace(pid)
    if oGameSpace:
        if oGameSpace.IsDebugging():
            oGameSpace.ReleaseDebug()
        NotifyMsg(pid, iServer, '断开联调成功')
    else:
        NotifyMsg(pid, iServer, '断开联调失败')
    resfunc()


def SetDebugTarget(pid, iTarget):
    oGameSpace = GetTools().GetGameSpace(pid)
    if not oGameSpace or not oGameSpace.IsDebugging():
        return False
    oGameSpace.m_Debug.SetDebugTarget(iTarget)
    return True


def R_GetBTVersion(resfunc, pid, lstBTNames):
    dVer = GetBTVersion(pid, lstBTNames)
    resfunc(dVer)


def GetBTVersion(pid, lstBTName):
    dVer = { }
    oGameSpace = GetTools().GetGameSpace(pid)
    if not oGameSpace:
        return dVer
    for sName in lstBTName:
        iVer = oGameSpace.GetBTVersion(sName)
        dVer[sName] = iVer
    
    return dVer


def SendNodeResult(pAgent, sAgentName, sRootPath, iNodeID, iAction, iResult):
    (pid, iServer) = GetDebugInfoByAgent(pAgent)
    GetTools().RpcCallFunc(iServer, __name__ + '.net.R_NodeResult', None, pid, sAgentName, sRootPath, iNodeID, iAction, iResult)


def SendBreakPointHitResult(pAgent, sRootPath, iNodeID, iAction, iHit):
    (pid, iServer) = GetDebugInfoByAgent(pAgent)
    GetTools().RpcCallFunc(iServer, __name__ + '.net.R_BreakPointResult', None, pid, sRootPath, iNodeID, iAction, iHit)


def GetDebugInfoByAgent(oAgent):
    oGameSpace = oAgent.GetGameSpace()
    pid = oGameSpace.m_Debug.GetPlayer()
    iServer = oGameSpace.m_Debug.GetServer()
    return (pid, iServer)


def GetModuleNameByBehaviorTree(oAgent, oNode):
    from .. import workspace
    if oAgent:
        oGameSpace = oAgent.GetGameSpace()
        if oGameSpace.IsDebugging():
            return oGameSpace.m_Debug.GetModuleNameByBehaviorTree(oNode)
    return workspace.GetInstance().GetModuleNameByBehaviorTree(oNode)


def ShowActionRun():
    dNonLoacl = {
        'funcName': '',
        'agentCls': None }
    
    def _Trace(f, e, a):
        agentCls = dNonLoacl['agentCls']
        if e == 'call' and agentCls and hasattr(agentCls, f.f_code.co_name):
            func = getattr(agentCls, f.f_code.co_name)
            if func.__doc__:
                lstDoc = func.__doc__.split('\n')
                if len(lstDoc) > 1 and 'showname' in lstDoc[1]:
                    dNonLoacl['funcName'] = lstDoc[1].split('showname')[1]

    
    def _Run(func):
        
        def _(*args, **kwargs):
            dNonLoacl['agentCls'] = args[1].__class__
            import sys
            sys.settrace(_Trace)
            
            try:
                r = func(*args, **kwargs)
            finally:
                sys.settrace(None)

            oNode = args[0]
            oAgent = args[1]
            sRootPath = ''
            oCurrentBT = oAgent.PYGetCurrentBT()
            if oCurrentBT:
                sRootPath = oCurrentBT.GetPathName()
            iNodeID = oNode.GetId()
            print('frame: %d %s node:%s-%d action: %s %s' % (oAgent.m_Game.GetFrameNum(), oAgent.m_OwnerObj.m_SID, sRootPath, iNodeID, dNonLoacl['funcName'], r))
            return r

        return _

    return _Run

