# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_movectrl_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_movectrl_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_movectrl_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_movectrl.net

def DN_GS2CMapTrack(iTarget, lstPath, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(66)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(len(lstPath), 1)
    for pos in lstPath:
        cl_duonet.netfunc.PacketPosFloat(pos)
    
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapTickPos(iTarget, frame, pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(67)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketVarInt(frame)
    cl_duonet.netfunc.PacketPosFloat(pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapStop(iTarget, pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(68)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketPosFloat(pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapJumpTrack(iTarget, fSpeed, fHeight, Start, End, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketFloat(fSpeed, 4)
    cl_duonet.netfunc.PacketFloat(fHeight, 4)
    cl_duonet.netfunc.PacketPosFloat(Start)
    cl_duonet.netfunc.PacketPosFloat(End)
    cl_duonet.netfunc.PacketAddI(iJumpStartBufTime, 2)
    cl_duonet.netfunc.PacketAddI(iJumpEndBufTime, 2)
    cl_duonet.netfunc.PacketAddI(iJumpUpTime, 2)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapPushTrack(iTarget, fSpeed, Start, End, iClientAni, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketFloat(fSpeed, 4)
    cl_duonet.netfunc.PacketPosFloat(Start)
    cl_duonet.netfunc.PacketPosFloat(End)
    cl_duonet.netfunc.PacketAddI(iClientAni, 1)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapDashTrack(iTarget, fSpeed, Start, End, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketFloat(fSpeed, 4)
    cl_duonet.netfunc.PacketPosFloat(Start)
    cl_duonet.netfunc.PacketPosFloat(End)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapAirTrack(iTarget, fSpeed, Start, End, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketFloat(fSpeed, 4)
    cl_duonet.netfunc.PacketPosFloat(Start)
    cl_duonet.netfunc.PacketPosFloat(End)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CFlyTrack(iTarget, lstPath, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(len(lstPath), 1)
    for pos in lstPath:
        cl_duonet.netfunc.PacketPosFloat(pos)
    
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CFlyPos(iTarget, frame, pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketVarInt(frame)
    cl_duonet.netfunc.PacketPosFloat(pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CRefreshTrack(iTarget, frame, lstPath, pid):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketVarInt(frame)
    cl_duonet.netfunc.PacketAddI(len(lstPath), 1)
    for pos in lstPath:
        cl_duonet.netfunc.PacketPosFloat(pos)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CCurveTrack(iTarget, fSpeed, Time, lstPath, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(69)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketFloat(fSpeed, 4)
    cl_duonet.netfunc.PacketAddI(Time, 4)
    cl_duonet.netfunc.PacketAddI(len(lstPath), 1)
    for pos in lstPath:
        cl_duonet.netfunc.PacketPosFloat(pos)
    
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapCrowdPos(iTarget, pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(75)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketPosFloat(pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapPosCtrl(Frame, Target, Pos, oGame, iScene, pid):
    cl_duonet.netfunc.PacketPrepare(70)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketPosFloat(Pos)
    cl_duonet.netfunc.DGameSceneBroadCastExclude(oGame, iScene, pid)


def DN_GS2CMapStopCtrl(Frame, Target, Pos, Server, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(71)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketPosFloat(Pos)
    cl_duonet.netfunc.PacketAddI(Server, 1)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapBackCtrl(Frame, Target, Pos, pid):
    cl_duonet.netfunc.PacketPrepare(72)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketPosFloat(Pos)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMapEnterHookRopeCtrl(iTarget, iHookRope, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(72)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iHookRope, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapHookRopeCtrl(iTarget, Frame, Pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(72)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketPosFloat(Pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapExitHookRopeCtrl(iTarget, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(72)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapPushCtrl(Frame, Target, Speed, Time, Gravaty, Start, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(73)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketPosFloat(Speed)
    cl_duonet.netfunc.PacketAddI(Time, 4)
    cl_duonet.netfunc.PacketFloat(Gravaty, 4)
    cl_duonet.netfunc.PacketPosFloat(Start)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CSysWinkSpeed(Target, Speed, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(73)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketFloat(Speed, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapJumpCtrl(Target, Frame, Pos, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(76)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketVarInt(Frame)
    cl_duonet.netfunc.PacketPosFloat(Pos)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CMapExitJump(Target, oGame, iScene, pid):
    cl_duonet.netfunc.PacketPrepare(78)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.DGameSceneBroadCastExclude(oGame, iScene, pid)


def DN_C2GSMove(who):
    Frame = cl_duonet.netfunc.UnpackVarInt()
    Start = cl_duonet.netfunc.UnpackPosFloat()
    lstDisp = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        Disp = cl_duonet.netfunc.UnpackPosFloat()
        Status = cl_duonet.netfunc.UnpackInt(1)
        lstDisp.append((Disp, Status))
    
    cl_movectrl.net.C2GSMove(who, Frame, Start, lstDisp)


def DN_C2GSDashExtInfo(who):
    Frame = cl_duonet.netfunc.UnpackVarInt()
    lstActNum = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iActNum = cl_duonet.netfunc.UnpackInt(2)
        lstActNum.append(iActNum)
    
    cl_movectrl.net.C2GSDashExtInfo(who, Frame, lstActNum)


def DN_C2GSEscape(who):
    iScene = cl_duonet.netfunc.UnpackInt(4)
    pos = cl_duonet.netfunc.UnpackPosFloat()
    cl_movectrl.net.C2GSEscape(who, iScene, pos)


def DN_C2GSMoveBack(who):
    Frame = cl_duonet.netfunc.UnpackVarInt()
    cl_movectrl.net.C2GSMoveBack(who, Frame)

