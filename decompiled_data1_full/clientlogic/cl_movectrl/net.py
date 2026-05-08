# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/net.pyc
# RelativePath: clientlogic/cl_movectrl/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from cl_only import OutputPos, GAME_FRAME
from cl_commondefines import HMS_BeatBack, HMS_Move, HMS_Back, HMS_Jump, HMS_Stop, HMS_SlowMove, HMS_Charge, HMS_Down, HMS_HookRope, HMS_Geyser, HMS_Fly
from cl_commondefines import PLAYMODE_ROGUELIKE, PLAYMODE_SURVIVOR, STATUS_JUMP, STATUS_STOP, STATUS_DASH, STATUS_MOVE, HMS_UP, STATUS_PUSH, STATUS_HOOKROPE, STATUS_GEYSER, STATYS_FLY
from cl_object.logging import MoveLog
from cl_math import Vec3MulF
import cl_duonet.dn_cl_movectrl_net as duonet
import cl_warrior
import cllib.lib_flag

def GS2CFlyTrack(oTarget, lstPath):
    if not lstPath:
        return None
    duonet.DN_GS2CFlyTrack(oTarget.m_ID, lstPath, oTarget.m_Game, oTarget.m_Scene)


def GS2CFlyPos(oTarget, iFrame, tPos):
    duonet.DN_GS2CFlyPos(oTarget.m_ID, iFrame, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapTrack(oTarget, lstPath):
    if not lstPath:
        return None
    duonet.DN_GS2CMapTrack(oTarget.m_ID, lstPath, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapCrowdPos(oTarget, tPos):
    duonet.DN_GS2CMapCrowdPos(oTarget.m_ID, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapTickPos(oTarget, iFrame, tPos):
    duonet.DN_GS2CMapTickPos(oTarget.m_ID, iFrame, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CStop(oTarget, tPos):
    duonet.DN_GS2CMapStop(oTarget.m_ID, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapJumpTrack(oTarget, tStart, tEnd, fSpeed, fHeight, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime):
    duonet.DN_GS2CMapJumpTrack(oTarget.m_ID, fSpeed, fHeight, tStart, tEnd, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapPushTrack(oTarget, fSpeed, vStart, vEnd, iClientAni):
    duonet.DN_GS2CMapPushTrack(oTarget.m_ID, fSpeed, vStart, vEnd, iClientAni, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapDashTrack(oTarget, fSpeed, vStart, vEnd):
    duonet.DN_GS2CMapDashTrack(oTarget.m_ID, fSpeed, vStart, vEnd, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapAirTrack(oTarget, fSpeed, vStart, vEnd):
    duonet.DN_GS2CMapAirTrack(oTarget.m_ID, fSpeed, vStart, vEnd, oTarget.m_Game, oTarget.m_Scene)


def GS2CRefreshTrack(oTarget, pid, iFrame, lstPath):
    if not lstPath:
        return None
    duonet.DN_GS2CRefreshTrack(oTarget.m_ID, iFrame, lstPath, pid)


def GS2CCurveTrack(oTarget, fSpeed, iTime, lstPath):
    duonet.DN_GS2CCurveTrack(oTarget.m_ID, fSpeed, iTime, lstPath, oTarget.m_Game, oTarget.m_Scene)


def C2GSMoveCheck(oTarget):
    if not (oTarget.m_MoveCtrl) or oTarget.IsDeadNoDying():
        return False
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return False
    if oTarget.m_ID not in oScene.GetHeros():
        return False
    return True


def C2GSMove(oTarget, iFrame, vStart, lstDisp):
    if not C2GSMoveCheck(oTarget):
        return None
    if not lstDisp or len(lstDisp) > 2:
        return None
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene.ValidWarningPos(vStart):
        MoveLog.Debug('%d C2GSMove 玩家%d %d在关卡%d位置%s非法(Min%s,Max%s)' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oTarget.m_ID, oScene.m_Level, OutputPos(vStart), OutputPos(oScene.m_BoundMin), OutputPos(oScene.m_BoundMax)))
        vBornPos = GetSceneBornPos(oScene)
        oTarget.WalkTo(vBornPos)
        GS2CMapStopCtrl(oTarget, oTarget.m_Game.GetFrameNum(), oTarget.GetPos(), 1)
        return None
    lstTrueDisp = []
    for vDisp, iStatus in lstDisp:
        if iStatus in g_ServerStatus:
            continue
        if iStatus not in g_StatusChange:
            MoveLog.Alert('%d 玩家%d %d客户端状态%d转换失败 frame%d start%s disp%s' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oTarget.m_ID, iStatus, iFrame, OutputPos(vStart), lstDisp))
            continue
        lstTrueDisp.append((Vec3MulF(vDisp, 0.001), g_StatusChange[iStatus]))
    
    if lstTrueDisp:
        oTarget.m_MoveCtrl.Move(oTarget, iFrame, vStart, lstTrueDisp)


def C2GSDashExtInfo(oTarget, iFrame, lstActNum):
    if not C2GSMoveCheck(oTarget):
        return None
    if not lstActNum or len(lstActNum) > 2:
        return None
    oTarget.m_MoveCtrl.AddDashExtInfo(iFrame, lstActNum)


def C2GSMoveBack(oTarget, iFrame):
    if not oTarget.m_MoveCtrl:
        return None
    oTarget.m_MoveCtrl.MoveBackAnswer(oTarget, iFrame)


def C2GSEscape(oHero, iTargetScene, vTargetPos):
    oGame = oHero.m_Game
    if cllib.lib_flag.g_IsStandalone and oGame.m_WarMgr.m_PlayMode not in (PLAYMODE_ROGUELIKE, PLAYMODE_SURVIVOR):
        MoveLog.Alert('%s %s escape invalid mode %s' % (oGame.m_ID, oHero.m_PlayerID, oGame.m_WarMgr.m_PlayMode))
        return None
    iCurScene = oHero.m_Scene
    vCurPos = oHero.GetPos()
    MoveLog.Info('%s %s %s tryescape %s %s to %s %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_ID, iCurScene, vCurPos, iTargetScene, vTargetPos))
    if oHero.IsDead():
        MoveLog.Error('%s %s %s escape dead' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_ID))
        return None
    if iCurScene != iTargetScene:
        MoveLog.Debug('%s %s %s escape diffscene %s %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_ID, iCurScene, iTargetScene))
        return None
    oScene = oGame.m_SceneMgr.GetScene(iCurScene)
    if not oScene:
        MoveLog.Error('%s %s %s escape noscene %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_ID, iCurScene))
        return None
    if not oScene.ValidWarningPos(vTargetPos):
        MoveLog.Error('%d C2GSEscape 玩家%d %d在关卡%d脱离目标位置%s非法(Min%s,Max%s)' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_ID, oScene.m_Level, OutputPos(vTargetPos), OutputPos(oScene.m_BoundMin), OutputPos(oScene.m_BoundMax)))
        vTargetPos = GetSceneBornPos(oScene)
    iCurFrame = oGame.GetFrameNum()
    oHero.Set('LastEscapeFrame', iCurFrame)
    oHero.Stop()
    oHero.WalkTo(vTargetPos)


def GetSceneBornPos(oScene):
    iLevel = oScene.m_Level
    oLevelCtrl = oScene.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    tBornInfo = oLevelNode.GetBornPos()
    vBornPos = tBornInfo[0]['Pos']
    return vBornPos

g_ServerStatus = {
    HMS_BeatBack: STATUS_PUSH }
g_StatusChange = {
    HMS_Fly: STATYS_FLY,
    HMS_Geyser: STATUS_GEYSER,
    HMS_HookRope: STATUS_HOOKROPE,
    HMS_Jump: STATUS_JUMP,
    HMS_Back: STATUS_STOP,
    HMS_Charge: STATUS_DASH,
    HMS_Stop: STATUS_STOP,
    HMS_SlowMove: STATUS_MOVE,
    HMS_Down: STATUS_MOVE,
    HMS_Move: STATUS_MOVE,
    HMS_UP: STATUS_MOVE }

def GS2CMapPosCtrl(oTarget, iFrame, tPos):
    duonet.DN_GS2CMapPosCtrl(iFrame, oTarget.m_ID, tPos, oTarget.m_Game, oTarget.m_Scene, oTarget.m_PlayerID)


def GS2CMapJumpCtrl(oTarget, iFrame, tPos):
    duonet.DN_GS2CMapJumpCtrl(oTarget.m_ID, iFrame, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapStopCtrl(oTarget, iFrame, tPos, iServer):
    duonet.DN_GS2CMapStopCtrl(iFrame, oTarget.m_ID, tPos, iServer, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapBackCtrl(oTarget, iFrame, tPos):
    duonet.DN_GS2CMapBackCtrl(iFrame, oTarget.m_ID, tPos, oTarget.m_PlayerID)


def GS2CMapPushCtrl(iFrame, oTarget, vSpeed, iTime, fGravaty, tStart):
    duonet.DN_GS2CMapPushCtrl(iFrame, oTarget.m_ID, vSpeed, iTime, fGravaty, tStart, oTarget.m_Game, oTarget.m_Scene)


def GS2CSysWinkSpeed(oTarget, vSpeed):
    duonet.DN_GS2CSysWinkSpeed(oTarget.m_ID, vSpeed, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapExitJump(oTarget):
    duonet.DN_GS2CMapExitJump(oTarget.m_ID, oTarget.m_Game, oTarget.m_Scene, oTarget.m_PlayerID)


def GS2CMapEnterHookRopeCtrl(oTarget, iHookRope):
    duonet.DN_GS2CMapEnterHookRopeCtrl(oTarget.m_ID, iHookRope, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapHookRopeCtrl(oTarget, iFrame, tPos):
    duonet.DN_GS2CMapHookRopeCtrl(oTarget.m_ID, iFrame, tPos, oTarget.m_Game, oTarget.m_Scene)


def GS2CMapExitHookRopeCtrl(oTarget):
    duonet.DN_GS2CMapExitHookRopeCtrl(oTarget.m_ID, oTarget.m_Game, oTarget.m_Scene)

