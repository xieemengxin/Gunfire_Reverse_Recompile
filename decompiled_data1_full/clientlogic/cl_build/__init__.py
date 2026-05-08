# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_build/__init__.pyc
# RelativePath: clientlogic/cl_build/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import WARRIOR_TRAP_ROTATEPILLAR, WARRIOR_STONEPILLAR, WARRIOR_PROTEGE_NORMAL, WARRIOR_AIRWALL_PHY, WARRIOR_TRAP_VENT, WARRIOR_TRAP_SMASH, WARRIOR_TRAP_UPSTONE, WARRIOR_TRAP_STONE, WARRIOR_TRAP_NORMAL, WARRIOR_OBSTACLE_LVTRIDESTORY, WARRIOR_OBSTACLE_BROKENPILLAR, WARRIOR_OBSTACLE_SLIDEDOOR, WARRIOR_OBSTACLE_STATICTRAN, WARRIOR_OBSTACLE_TRIDESTROY, WARRIOR_OBSTACLE_TRANGATE, WARRIOR_OBSTACLE_SIMCTRL, WARRIOR_OBSTACLE_VICCTRL, WARRIOR_OBSTACLE_CTRLGATE, WARRIOR_TRAP_MOVEPLANE, WARRIOR_OBSTACLE_HINDER, WARRIOR_TRAP_FAKERPLANK, WARRIOR_SUMMON_STELE, WARRIOR_MONSTERBUILD, WARRIOR_GEYSER, WARRIOR_TRAP_THUNDERBUCKET, WARRIOR_MONSTERHINDER, WARRIOR_MONSTENOPHYRHINDER, WARRIOR_MOVEBUILD
from . import mobject
from . import obstacle
from . import trap
g_BuildCls = {
    WARRIOR_MOVEBUILD: mobject.CMoveBuild,
    WARRIOR_MONSTENOPHYRHINDER: mobject.CMonsterNoPhyHinder,
    WARRIOR_MONSTERHINDER: mobject.CMonsterHinder,
    WARRIOR_GEYSER: mobject.CGeyserBuild,
    WARRIOR_MONSTERBUILD: mobject.CMonsterBuild,
    WARRIOR_TRAP_FAKERPLANK: trap.CFakerPlanKTrap,
    WARRIOR_OBSTACLE_HINDER: obstacle.CHinder,
    WARRIOR_TRAP_MOVEPLANE: trap.CMovePlaneTrap,
    WARRIOR_SUMMON_STELE: mobject.CSummonStele,
    WARRIOR_STONEPILLAR: mobject.CStonePillar,
    WARRIOR_PROTEGE_NORMAL: mobject.CProtege,
    WARRIOR_AIRWALL_PHY: mobject.CPhyWall,
    WARRIOR_TRAP_THUNDERBUCKET: trap.CThunderBucket,
    WARRIOR_TRAP_VENT: trap.CVentTrap,
    WARRIOR_TRAP_ROTATEPILLAR: trap.CRotatePillar,
    WARRIOR_TRAP_SMASH: trap.CMashTrap,
    WARRIOR_TRAP_UPSTONE: trap.CUpStoneTrap,
    WARRIOR_TRAP_STONE: trap.CStoneTrap,
    WARRIOR_TRAP_NORMAL: trap.CTrap,
    WARRIOR_OBSTACLE_LVTRIDESTORY: obstacle.CLevelTriggerDestory,
    WARRIOR_OBSTACLE_BROKENPILLAR: obstacle.CBrokenPillar,
    WARRIOR_OBSTACLE_SLIDEDOOR: obstacle.CSlidingDoorTransfer,
    WARRIOR_OBSTACLE_STATICTRAN: obstacle.CStaticGateTransfer,
    WARRIOR_OBSTACLE_TRIDESTROY: obstacle.CTriggerDestroy,
    WARRIOR_OBSTACLE_TRANGATE: obstacle.CGateTransfer,
    WARRIOR_OBSTACLE_SIMCTRL: obstacle.CSimcontrol,
    WARRIOR_OBSTACLE_VICCTRL: obstacle.CGatecontrol,
    WARRIOR_OBSTACLE_CTRLGATE: obstacle.CGatecontrol }

def NewBuild(oGame, clsData, dAddData):
    nid = oGame.NewNPCID()
    clsBuild = g_BuildCls.get(clsData.m_FightType, obstacle.CObstacle)
    oBuild = clsBuild(oGame, nid)
    oBuild.InitBuild(clsData, dAddData)
    return oBuild

