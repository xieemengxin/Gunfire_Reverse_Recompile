# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/__init__.pyc
# RelativePath: clientlogic/cl_behavior/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_UseCBehavior:
    import pubbehaviorc.tools as bttools
    import pubbehaviorc.agent as btagent
    import pubbehaviorc.behaviortree as bttree
    import pubbehaviorc.workspace as btworkspace
else:
    from . import tools as bttools
    from . import agent as btagent
    from . import behaviortree as bttree
    from . import workspace as btworkspace

def BaseStart(oProductFunc):
    if cllib.lib_flag.g_UseCBehavior:
        import cl_behavior.debug.logmanager as logmanager
        bttools.SetProductFunc(oProductFunc)
        bttools.SetSendSignal_Method(logmanager.CLogManager.SendSignal)
    else:
        bttools.SetProductFunc(oProductFunc)


def GetWorkSpace():
    return btworkspace.GetInstance()


def NewGameSpace():
    return btworkspace.NewGame()


def HotReload(sTree):
    btworkspace.GetInstance().HotReload(sTree)


def ParserAgent():
    from .debug import parseragent
    oParser = parseragent.CParserAgent()
    import C_rdev
    C_rdev.BeginDaobiao()
    oParser.Start()
    C_rdev.EndDaobiao()


def C2GSBehaviorCmd(oLink):
    from .debug import net
    net.C2GSBehaviorCmd(oLink)


def GetTools():
    return bttools.GetTools()


def GetGameSpaceClass():
    return btworkspace.CGameSpace


def GetAgentClass():
    return btagent.CAgent


def GetProductFuncClass():
    return bttools.CProductFunc


def CreateBehaviorTree():
    return bttree.CBehaviorTree()


def ClearBehaviorTree():
    oWorkSpace = btworkspace.GetInstance()
    lstTree = list(oWorkSpace.m_BehaviorTrees.keys())
    for sTree in lstTree:
        if sTree[:6] == 'Common':
            continue
        oWorkSpace.DestroyBehavior(sTree)
    

