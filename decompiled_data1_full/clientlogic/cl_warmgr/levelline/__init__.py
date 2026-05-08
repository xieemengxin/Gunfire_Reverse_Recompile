# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/__init__.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_cscommondef.cs_fight import LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE, LEVEL_TYPE_BOSS, LEVEL_TYPE_HALL, HIDELV_TYPE_TRAP, HIDELV_TYPE_SIGHT, GAMETYPE_LIMITDEFEND, GAMETYPE_DEFEND, GAMETYPE_CONVOY, HIDELV_TYPE_CASH, HIDELV_TYPE_ELITE, HIDELV_TYPE_JUMP, HIDELV_TYPE_PETROCHEMICAL, HIDELV_TYPE_DEFEND, HIDELV_TYPE_NORMAL
from . import mainlevelnode
from . import hidelevelnode
from . import leveltrigger
from . import levelminimap
g_HideLevelNode = {
    HIDELV_TYPE_CASH: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_PETROCHEMICAL: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_JUMP: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_TRAP: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_SIGHT: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_ELITE: hidelevelnode.CHideLevelNode,
    HIDELV_TYPE_DEFEND: hidelevelnode.CDefendLevelNode,
    HIDELV_TYPE_NORMAL: hidelevelnode.CHideLevelNode }
g_MainLevelNode = {
    GAMETYPE_LIMITDEFEND: mainlevelnode.CLimitDefendNode,
    GAMETYPE_DEFEND: mainlevelnode.CDefendLevelNode,
    GAMETYPE_CONVOY: mainlevelnode.CConvoyLevelNode }

def GetLevelNode(oCtrlMgr, iLevelType, iGameType, iLevel, *args):
    oNode = None
    if iLevelType == LEVEL_TYPE_HALL:
        oNode = mainlevelnode.CHallLevelNode(oCtrlMgr, iLevel)
    elif iLevelType == LEVEL_TYPE_BOSS:
        oNode = mainlevelnode.CBossLevelNode(oCtrlMgr, iLevel)
    elif iLevelType == LEVEL_TYPE_HIDE:
        iHideLvType = args[0]
        if iHideLvType in g_HideLevelNode:
            oNode = g_HideLevelNode[iHideLvType](oCtrlMgr, iLevel)
            oNode.m_GameType = iGameType
        elif iLevelType == LEVEL_TYPE_FIGHT:
            if iGameType in g_MainLevelNode:
                oNode = g_MainLevelNode[iGameType](oCtrlMgr, iLevel)
            else:
                oNode = mainlevelnode.CMainLevelNode(oCtrlMgr, iLevel)
                oNode.m_GameType = iGameType


def NewLevelTrigger(oLevelCtrl):
    return leveltrigger.CLevelTriggerMgr(oLevelCtrl)


def NewMiniMapMgr(oLevelCtrl):
    return levelminimap.CSceneMiniMapMgr(oLevelCtrl)

