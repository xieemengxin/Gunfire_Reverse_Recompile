# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/__init__.pyc
# RelativePath: clientlogic/cl_betree/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib
import cl_behavior
from . import fsm
if 'g_AgentMoudle' not in globals():
    g_AgentMoudle = { }

def InitBetreeAI(oMonster, sTree, dConfig = None):
    if not sTree:
        return None
    oGame = oMonster.m_Game
    oWorkSpace = cl_behavior.GetWorkSpace()
    oTree = oWorkSpace.LoadBehaviorTree(sTree)
    if not oTree:
        return None
    if not dConfig:
        dConfig = { }
    sAgent = oTree.GetAgentType()
    oAgent = oGame.m_Betree.CreateAgent(GetAgentClass(sAgent), '%s%s' % (sAgent, oMonster.m_ID))
    oAgent.Config(oMonster, dConfig)
    oAgent.BTSetCurrent(sTree)
    return oAgent


def InitFsmAI(oTarget, sAgent, sTree, dConfig = None):
    oGame = oTarget.m_Game
    oFsmTask = oGame.m_Betree.CreateFsmTask(sTree)
    if not oFsmTask:
        return None
    if not dConfig:
        dConfig = { }
    oAgent = oGame.m_Betree.CreateAgent(GetAgentClass(sAgent), '%s%s' % (sAgent, oTarget.m_ID))
    oAgent.Config(oTarget, dConfig)
    oAgent.SetFsm(oFsmTask)
    return oAgent


def GetAgentClass(sAgent):
    if sAgent not in g_AgentMoudle:
        
        try:
            sImport = sAgent
            mod = importlib.import_module(sImport)
            g_AgentMoudle[sAgent] = mod
        except:
            PythonError()
            return None

    return g_AgentMoudle[sAgent].CAgent


def NewAISceneData(oGame, iScene):
    import cl_betree.scenedata
    iID = oGame.NewNPCID()
    obj = cl_betree.scenedata.CAISceneDataBeTree(oGame, iID, iScene)
    oGame.CreateObject(iID, obj)
    return obj


def HotReload(sTree):
    cl_behavior.HotReload(sTree)
    fsm.HotReload(sTree)


def ClearBetree():
    cl_behavior.ClearBehaviorTree()
    fsm.g_AllFsm.clear()


def MyInit():
    from . import producttools
    oFunc = producttools.CProductFunc()
    cl_behavior.BaseStart(oFunc)

