# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/clientctrl.pyc
# RelativePath: clientlogic/cl_movectrl/clientctrl.pyc
# Source Generated with Decompyle++
# File: clientctrl.pyc (Python 3.6)

from C_component import ComNavStay
from cl_only import OutputPos, Second2Frame, GAME_FRAME
from cl_commondefines import STATUS_MOVE, STATUS_JUMP, STATUS_PUSH, STATUS_DASH, STATUS_STOP, STATUS_SERVSTOP, STATUS_HOOKROPE, STATUS_GEYSER, STATYS_FLY
from cl_commondefines import MOVE_TYPE_NORMAL, MOVE_TYPE_WINK, MOVE_TYPE_JUMP, STATE_PUSHCTRL, STATE_TIME_LIMIT, FORBID_PUSHED, WINK_OVER
from cl_pxlayer import PXMASK_BLOCK, PXMASK_MOVEBLK
from cl_object.logging import MoveLog
import cl_math
import cl_forbid
import cl_state
import cl_movectrl.mobject as base
import cl_movectrl.net as movenet
import cl_object.reason as reason
import cl_modeldefine
import cl_msgcenter
import cl_notify
STAT_MOVE_SUCC = 0
STAT_MOVE_SIDES = 1
STAT_MOVE_UP = 2
STAT_MOVE_BELOW = 4
STAT_MOVE_ERROR = 8
STAT_MOVE_BLOCK = STAT_MOVE_SIDES | STAT_MOVE_UP
CLIENT_FRAME_TIME = 0.02
USE_MOVETO = 0

class CCtrlInterface(object):
    m_MoveTolerance = 1.5
    m_SpeedTolerance = 1.2
    m_ContactOffset = 0.08
    m_ServerUpdate = False
    
    def ValidLeaveCtrl(self, oOwner):
        return True

    
    def OnCheckMoveAttr(self, oCtrl, oOwner, dCtrl):
        return True

    
    def CheckMoveAttr(self, oCtrl, oOwner, dCtrl):
        vStart = dCtrl['Pos']
        vDisp = dCtrl['TotDisp']
        vCurPos = oOwner.GetPos()
        if not oOwner.m_Game.Scene_IsSafePos(oOwner.m_Scene, vStart, vDisp):
            return False
        if not cl_math.CheckDistance3D(vStart, vCurPos, self.m_MoveTolerance):
            oCtrl.Stop(oOwner, 'startfail %s %s' % (OutputPos(vCurPos), OutputPos(vStart)))
            return False
        return self.OnCheckMoveAttr(oCtrl, oOwner, dCtrl)



class CMoveStatus(base.CActorMove, CCtrlInterface):
    
    def OnEnter(self, oOwner):
        super().OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL

    if USE_MOVETO:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            iFrame = dCtrl['Frame']
            fDeltaTime = dCtrl['Delta'] * len(dCtrl['Disp'])
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            fDis = oCtrl.CalDownDisp(fDeltaTime)
            vPosTo = (vStart[0] + vDisp[0], vStart[1] + fDis, vStart[2] + vDisp[2])
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            vCurPos = oOwner.GetPos()
            if vCurPos == vPosTo:
                return True
            (_stat, vAfterPos) = oOwner.m_MoveCtrl.MoveTo(oOwner, vPosTo, iFrame)
            if not cl_math.CheckDistance3D(vClientTo, vAfterPos, self.m_MoveTolerance):
                oCtrl.Stop(oOwner, 'endfail %s' % (OutputPos(vClientTo),))
                return False
            if not oCtrl.m_CutForSingleGame:
                oCtrl.SendPacket(movenet.GS2CMapPosCtrl, iFrame, vAfterPos)
            return True

    else:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            vCurPos = oOwner.GetPos()
            if vCurPos == vClientTo:
                return True
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            if not oCtrl.m_CutForSingleGame:
                oCtrl.SendPacket(movenet.GS2CMapPosCtrl, dCtrl['Frame'], vAfterPos)
            return True



class CJumpStatus(base.CActorJump, CCtrlInterface):
    m_JumpStartSpeed = 5.24
    m_StepOffset = 0.35
    
    def OnEnter(self, oOwner):
        super().OnEnter(oOwner)
        oOwner.m_MoveCtrl.m_CurDownSpeed = self.m_JumpStartSpeed
        oOwner.m_PhyModel.E_SetStepOffset(0.001)
        oOwner.m_MoveMode = MOVE_TYPE_JUMP

    
    def OnExit(self, oOwner):
        super().OnExit(oOwner)
        oOwner.m_PhyModel.E_SetStepOffset(self.m_StepOffset)
        if not oOwner.m_Game.m_WarMgr.IsSingleGame():
            movenet.GS2CMapExitJump(oOwner)

    
    def ValidLeaveCtrl(self, oOwner):
        return True

    if USE_MOVETO:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            iFrame = dCtrl['Frame']
            fDeltaTime = dCtrl['Delta']
            vStart = dCtrl['Pos']
            lstDisp = dCtrl['Disp']
            vPosTo = (vStart[0], oOwner.GetPos()[1], vStart[2])
            vClientTo = vStart
            lstDis = []
            for vDisp in lstDisp:
                fDis = oCtrl.CalDownDisp(fDeltaTime)
                lstDis.append(fDis)
                vPosTo = (vPosTo[0] + vDisp[0], vPosTo[1] + fDis, vPosTo[2] + vDisp[2])
                vClientTo = cl_math.Vec3Add(vClientTo, vDisp)
            
            (stat, vAfterPos) = oOwner.m_MoveCtrl.MoveTo(oOwner, vPosTo, iFrame)
            if not cl_math.CheckDistance3D(vClientTo, vAfterPos, self.m_MoveTolerance):
                oCtrl.Stop(oOwner, 'endfail %s' % (OutputPos(vClientTo),))
                return False
            oCtrl.SendPacket(movenet.GS2CMapJumpCtrl, iFrame, vAfterPos)
            return True

    else:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            oCtrl.SendPacket(movenet.GS2CMapJumpCtrl, dCtrl['Frame'], vAfterPos)
            return True



class CStopStatus(base.CActorStop, CCtrlInterface):
    m_DownTolerance = -0.05
    
    def OnEnter(self, oOwner):
        super(CStopStatus, self).OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL

    if USE_MOVETO:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            iFrame = dCtrl['Frame']
            vPos = cl_math.Vec3Add(dCtrl['Pos'], dCtrl['TotDisp'])
            vPos = (vPos[0], vPos[1] + oCtrl.CalDownDisp(dCtrl['Delta']) + self.m_DownTolerance, vPos[2])
            (stat, vAfterPos) = oCtrl.MoveTo(oOwner, vPos, iFrame)
            oCtrl.SendPacket(movenet.GS2CMapStopCtrl, iFrame, vAfterPos, 0)
            return True

    else:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vClientTo = cl_math.Vec3Add(dCtrl['Pos'], dCtrl['TotDisp'])
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            oCtrl.SendPacket(movenet.GS2CMapStopCtrl, dCtrl['Frame'], vAfterPos, 0)
            return True



class CServerStopStatus(base.CActorStop, CCtrlInterface):
    m_ServerUpdate = True
    
    def OnEnter(self, oOwner):
        super(CServerStopStatus, self).OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL

    
    def Do(self, oCtrl, oOwner, dCtrl):
        iFrame = oCtrl.m_Game.GetFrameNum()
        vCurPos = oOwner.GetPos()
        if dCtrl['Force']:
            MoveLog.Info('%d move %d back cur %s %s' % (oOwner.m_PlayerID, iFrame, OutputPos(vCurPos), dCtrl['Force']))
            oCtrl.m_MoveBackCheck = iFrame
            movenet.GS2CMapBackCtrl(oOwner, iFrame, vCurPos)
        else:
            movenet.GS2CMapStopCtrl(oOwner, iFrame, vCurPos, 1)
        oCtrl.ClearPacket()
        oCtrl.ClearBuffer()
        return True

    
    def ClearCtrl(self, oOwner):
        return True

    
    def ServerUpdate(self, oCtrl, oOwner, iFrame):
        if oCtrl.IsGround():
            return None
        vStart = oOwner.GetPos()
        fDownDis = oCtrl.CalDownDisp(CLIENT_FRAME_TIME * 2)
        vTarget = (vStart[0], vStart[1] + fDownDis, vStart[2])
        (stat, vAfterPos) = oCtrl.MoveTo(oOwner, vTarget, iFrame)
        oCtrl.SendPacket(movenet.GS2CMapStopCtrl, iFrame, vAfterPos, 0)



class CPushStatus(base.CActorWinkMove, CCtrlInterface):
    m_ForbidRule = cl_forbid.PUSHCTRL_RULE
    m_CheckForbid = FORBID_PUSHED
    m_AddState = STATE_PUSHCTRL
    m_WinkFrameOut = 12
    m_ServerUpdate = True
    m_WinkEndCallBack = None
    
    def OnEnter(self, oOwner):
        super(CPushStatus, self).OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_WINK
        if self.m_AddState:
            oState = cl_state.AddState(oOwner, self.m_AddState, STATE_TIME_LIMIT, 10 * GAME_FRAME, {
                'AID': oOwner.m_ID,
                'RS': reason.CStrReason('玩家击退') })
            if oState:
                oState.Enable(oOwner)
        oOwner.m_MoveCtrl.ClearBuffer()
        MoveLog.Info('%d push start %s' % (oOwner.m_PlayerID, OutputPos(oOwner.GetPos())))

    
    def OnExit(self, oOwner):
        super(CPushStatus, self).OnExit(oOwner)
        oOwner.m_MoveCtrl.SetGravaty(0)
        if self.m_AddState:
            oState = oOwner.m_State.GetItemBySID(self.m_AddState)
            if oState:
                oOwner.m_State.RemoveItem(oState.m_ID)
        if self.m_WinkEndCallBack:
            cbfunc = self.m_WinkEndCallBack
            self.m_WinkEndCallBack = None
            cbfunc(oOwner, WINK_OVER)
        MoveLog.Info('%d push end %s' % (oOwner.m_PlayerID, OutputPos(oOwner.GetPos())))

    
    def Do(self, oCtrl, oOwner, dCtrl):
        if self.m_WinkEndCallBack:
            cbfunc = self.m_WinkEndCallBack
            self.m_WinkEndCallBack = None
            cbfunc(oOwner, WINK_OVER)
        tDir = dCtrl['Dir']
        fSpeed = dCtrl['Speed']
        fSecond = dCtrl['Second']
        self.m_WinkDir = cl_math.Vec3Normalize((tDir[0], 0, tDir[2]))
        self.m_StartWinkSpeed = fSpeed
        self.m_WinkSpeed = fSpeed
        oCtrl.SetDownSpeed(dCtrl['DownSpeed'])
        oCtrl.SetGravaty(dCtrl['Gravaty'])
        self.m_WinkEndFrame = dCtrl['SFrame'] + Second2Frame(fSecond)
        self.m_WinkEndCallBack = dCtrl['CallBackFunc']
        vStart = oOwner.GetPos()
        vSpeed = (self.m_WinkDir[0] * self.m_WinkSpeed, dCtrl['DownSpeed'], self.m_WinkDir[2] * self.m_WinkSpeed)
        movenet.GS2CMapPushCtrl(dCtrl['SFrame'], oOwner, vSpeed, int(dCtrl['Second'] * 100), dCtrl['Gravaty'], vStart)
        return True

    
    def ValidLeaveCtrl(self, oOwner):
        if not oOwner.m_MoveCtrl.IsGround() or self.m_WinkSpeed:
            return False
        return True

    
    def ServerUpdate(self, oCtrl, oOwner, iFrame):
        oGame = oOwner.m_Game
        vPos = oOwner.GetPos()
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene.ValidWarningPos(vPos):
            sMsg = 'Push 玩家%d %d在场景%d位置%s非法(Min%s,Max%s)' % (oOwner.m_PlayerID, oOwner.m_ID, oScene.m_Level, OutputPos(vPos), OutputPos(oScene.m_BoundMin), OutputPos(oScene.m_BoundMax))
            MoveLog.Error(sMsg)
            cl_notify.GS2CDebugMsg(oGame, oOwner.m_PlayerID, sMsg)
            self.m_WinkSpeed = 0
            oCtrl.SetDownSpeed(0)
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
            tBornInfo = oLevelNode.GetBornPos()
            vBornPos = cl_math.Vec3Add(tBornInfo[0]['Pos'], (0, 0.2, 0))
            oCtrl.Stop(oOwner, 'invalidpos')
            oOwner.WalkTo(vBornPos)
            oCtrl.Stop(oOwner, 'invalidpos')
            return False
        vDisp = cl_math.Vec3MulF(self.m_WinkDir, self.m_WinkSpeed * CLIENT_FRAME_TIME * 2)
        vDisp = (vDisp[0], oCtrl.CalDownDisp(CLIENT_FRAME_TIME) + oCtrl.CalDownDisp(CLIENT_FRAME_TIME), vDisp[2])
        (stat, vAfterPos) = oCtrl.MoveDisp(oOwner, vDisp, iFrame)
        iOldSpeed = self.m_WinkSpeed
        if stat & STAT_MOVE_SIDES:
            self.m_WinkSpeed = 0
            oCtrl.SendPacket(movenet.GS2CSysWinkSpeed, self.m_WinkSpeed)
        if iFrame >= self.m_WinkEndFrame and self.m_WinkSpeed > 0:
            iLessFrame = max(self.m_WinkFrameOut + self.m_WinkEndFrame - iFrame, 0)
            self.m_WinkSpeed = iLessFrame * self.m_StartWinkSpeed / self.m_WinkFrameOut
        if (stat & STAT_MOVE_UP or iOldSpeed) and self.m_WinkSpeed == 0 and oCtrl.m_CurDownSpeed > 0:
            oCtrl.SetDownSpeed(0)
        if stat & STAT_MOVE_BELOW:
            if not (self.m_WinkSpeed) or iFrame >= self.m_WinkEndFrame:
                self.m_WinkSpeed = 0
                oOwner.m_MoveCtrl.Stop(oOwner)
        if not oCtrl.m_CutForSingleGame:
            oCtrl.SendPacket(movenet.GS2CMapPosCtrl, iFrame, vAfterPos)
        return True



class CDashStatus(base.CActorWinkMove, CCtrlInterface):
    
    def OnEnter(self, oOwner):
        super(CDashStatus, self).OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_WINK
        self.m_MoveSecond = 0

    
    def OnExit(self, oOwner):
        super().OnExit(oOwner)
        self.m_MoveSecond = 0
        dCtrlCheck = oOwner.m_MoveCtrl.m_DashCtrlCheck
        oOwner.m_MoveCtrl.m_DashCtrlCheck = { }
        cbFunc = dCtrlCheck['ExitCB'] if 'ExitCB' in dCtrlCheck else None
        if cbFunc:
            cbFunc(oOwner, dCtrlCheck)

    
    def OnCheckMoveAttr(self, oCtrl, oOwner, dCtrl):
        if 'ActNum' not in dCtrl:
            oCtrl.Stop(oOwner, 'client data err %s %s %s' % (dCtrl, oCtrl.m_MoveBuffer, oCtrl.m_DashExtBuffer))
            return False
        iActNum = dCtrl['ActNum']
        if iActNum in oCtrl.m_DashCache:
            oCtrl.m_DashCtrlCheck = oCtrl.m_DashCache.pop(iActNum)
            self.m_MoveSecond = 0
        if not oCtrl.m_DashCtrlCheck:
            oCtrl.Stop(oOwner, 'no dash data')
            return False
        if iActNum != oCtrl.m_DashCtrlCheck['ActNum']:
            oCtrl.Stop(oOwner, 'err cash data')
            return False
        if self.m_MoveSecond > oCtrl.m_DashCtrlCheck['Second']:
            if oCtrl.m_DashCtrlCheck['UpSpeed']:
                pass
            else:
                oCtrl.Stop(oOwner, 'dashtime %s' % oCtrl.m_DashCtrlCheck['Second'])
                return False
        self.m_MoveSecond += dCtrl['Delta'] * len(dCtrl['Disp'])
        return True

    if USE_MOVETO:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            iFrame = dCtrl['Frame']
            _fDeltaTime = dCtrl['Delta']
            vClientTo = dCtrl['Pos']
            lstDisp = dCtrl['Disp']
            for vDisp in lstDisp:
                vClientTo = (vClientTo[0] + vDisp[0], vClientTo[1] + vDisp[1], vClientTo[2] + vDisp[2])
                (_stat, vAfterPos) = oOwner.m_MoveCtrl.MoveTo(oOwner, vClientTo, iFrame)
            
            if not cl_math.CheckDistance3D(vClientTo, vAfterPos, self.m_MoveTolerance):
                oCtrl.Stop(oOwner, 'endfail %s' % (OutputPos(vClientTo),))
                return False
            if not oCtrl.m_CutForSingleGame:
                oCtrl.SendPacket(movenet.GS2CMapPosCtrl, iFrame, vAfterPos)
            return True

    else:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            if not oCtrl.m_CutForSingleGame:
                oCtrl.SendPacket(movenet.GS2CMapPosCtrl, dCtrl['Frame'], vAfterPos)
            return True



class CHookRopeStatus(base.CActorMove, CCtrlInterface):
    m_HookRopeID = 0
    
    def OnEnter(self, oOwner):
        super().OnEnter(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        oOwner.Set('CurHookRopeNpc', self.m_HookRopeID)
        movenet.GS2CMapEnterHookRopeCtrl(oOwner, self.m_HookRopeID)

    
    def OnExit(self, oOwner):
        super().OnExit(oOwner)
        oOwner.Delete('CurHookRopeNpc')
        movenet.GS2CMapExitHookRopeCtrl(oOwner)

    
    def Do(self, oCtrl, oOwner, dCtrl):
        vStart = dCtrl['Pos']
        vDisp = dCtrl['TotDisp']
        vClientTo = cl_math.Vec3Add(vStart, vDisp)
        vCurPos = oOwner.GetPos()
        if vCurPos == vClientTo:
            return True
        oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
        vAfterPos = oOwner.RefreshPos()
        if not oCtrl.m_CutForSingleGame:
            oCtrl.SendPacket(movenet.GS2CMapHookRopeCtrl, dCtrl['Frame'], vAfterPos)
        return True

    
    def SetHookRopeID(self, iHookRopeID):
        self.m_HookRopeID = iHookRopeID



class CGeyserStatus(CJumpStatus):
    if USE_MOVETO:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            oCtrl.SendPacket(movenet.GS2CMapJumpCtrl, dCtrl['Frame'], vAfterPos)
            return True

    else:
        
        def Do(self, oCtrl, oOwner, dCtrl):
            vStart = dCtrl['Pos']
            vDisp = dCtrl['TotDisp']
            vClientTo = cl_math.Vec3Add(vStart, vDisp)
            oOwner.m_Game.Scene_Walk(oOwner.m_ID, vClientTo)
            vAfterPos = oOwner.RefreshPos()
            oCtrl.SendPacket(movenet.GS2CMapJumpCtrl, dCtrl['Frame'], vAfterPos)
            return True



class CFlyStatus(CMoveStatus):
    pass


class CClientCtrlMgr(base.CActorCtrlMgr):
    m_InitStatus = STATUS_STOP
    m_Gravaty = 11.65
    m_DashCacheAlert = 2
    
    def __init__(self, oOwner):
        self.m_Status = {
            STATYS_FLY: CFlyStatus(),
            STATUS_GEYSER: CGeyserStatus(),
            STATUS_HOOKROPE: CHookRopeStatus(),
            STATUS_SERVSTOP: CServerStopStatus(),
            STATUS_DASH: CDashStatus(),
            STATUS_STOP: CStopStatus(),
            STATUS_PUSH: CPushStatus(),
            STATUS_JUMP: CJumpStatus(),
            STATUS_MOVE: CMoveStatus() }
        self.m_Game = oOwner.m_Game
        self.m_Owner = oOwner.m_ID
        self.m_MoveBuffer = []
        self.m_DashExtBuffer = { }
        self.m_SpeedList = []
        self.m_IsGround = 0
        self.m_CurDownSpeed = 0
        self.m_CurGravaty = 0
        self.m_MoveBackCheck = 0
        self.m_ClientFrame = 0
        self.m_ClientRtt = 0
        self.m_DashCtrlCheck = { }
        self.m_DashCache = { }
        self.m_PacketBuffer = None
        super(CClientCtrlMgr, self).__init__(oOwner)
        self.m_ComNav = CClientCtrlNavStay(oOwner)
        self.m_CutForSingleGame = self.m_Game.m_WarMgr.IsSingleGame()

    
    def Init(self, oOwner):
        super(CClientCtrlMgr, self).Init(oOwner)
        oOwner.m_PhyModel.E_SetMoveBlockMask(PXMASK_MOVEBLK)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnReady, 'ClientCtrlReady', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnLoadOK, 'ClientCtrlEnterScene', -1, 0)

    
    def Release(self, oOwner):
        self.m_Game = None
        if self.m_ComNav:
            self.m_ComNav.Release(oOwner)
        self.m_ComNav = None
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'ClientCtrlReady')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'ClientCtrlEnterScene')

    
    def IsClientCtrl(self):
        return True

    
    def IsGround(self):
        return self.m_IsGround

    
    def IsStop(self, oOwner):
        return self.m_CurStatus in (STATUS_STOP, STATUS_SERVSTOP)

    
    def OnReady(self, oOwner, dInfo):
        if dInfo['reenter']:
            self.m_MoveBackCheck = 0

    
    def OnLoadOK(self, oOwner, dInfo):
        self.m_ClientFrame = 0
        self.m_MoveBackCheck = 0

    
    def SetSpeed(self, oOwner, fSpeed):
        pass

    
    def CalCheckSpeed(self, iFrame):
        fCheckSpeed = 0
        for idx in range(len(self.m_SpeedList) - 1, -1, -1):
            (iCheckFrame, fSpeed) = self.m_SpeedList[idx]
            if iCheckFrame < iFrame - GAME_FRAME and fCheckSpeed:
                self.m_SpeedList[:] = self.m_SpeedList[max(0, idx - 1):]
                break
            if iCheckFrame < iFrame + GAME_FRAME:
                fCheckSpeed = max(fCheckSpeed, fSpeed)
        
        return fCheckSpeed

    
    def SetDownSpeed(self, fDownSpeed):
        self.m_CurDownSpeed = fDownSpeed

    
    def SetGravaty(self, fGravaty):
        self.m_CurGravaty = fGravaty

    
    def CalDownDisp(self, fDeltaTime):
        fGravaty = self.m_CurGravaty if self.m_CurGravaty else self.m_Gravaty
        self.m_CurDownSpeed -= fDeltaTime * fGravaty
        return fDeltaTime * self.m_CurDownSpeed

    
    def MoveTo(self, oOwner, vPos, iFrame):
        stat = oOwner.m_PhyModel.E_MoveTo(vPos)
        vAfterPos = oOwner.RefreshPos()
        if stat & STAT_MOVE_BELOW:
            self.m_IsGround = 1
            self.m_CurDownSpeed = 0
        else:
            self.m_IsGround = 0
        return (stat, vAfterPos)

    
    def MoveDisp(self, oOwner, vDisp, iFrame):
        stat = oOwner.m_PhyModel.E_MoveDisp(vDisp, STAT_MOVE_BLOCK)
        vAfterPos = oOwner.RefreshPos()
        if stat & STAT_MOVE_BELOW:
            self.m_IsGround = 1
            self.m_CurDownSpeed = 0
        else:
            self.m_IsGround = 0
        return (stat, vAfterPos)

    
    def ContinueStatus(self, oOwner, iStatus, dCtrl):
        if self.m_CurStatus != iStatus:
            oCurStatus = self.GetCurStatusObject()
            oStatus = self.GetStatus(iStatus)
            if not (oStatus.m_ServerUpdate) and not oCurStatus.ValidLeaveCtrl(oOwner):
                if not oCurStatus.m_ServerUpdate:
                    self.Stop(oOwner, 'changefail %s %s %s' % (self.m_CurStatus, iStatus, dCtrl))
                return False
            if not oStatus.Check(oOwner, dCtrl):
                return False
            iLastStatus = self.m_CurStatus
            self.ChangeStatus(oOwner, iStatus)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MOVESTATUSCHANGE, oOwner, {
                'MoveStatus': iStatus,
                'LastMoveStatus': iLastStatus })
        else:
            oStatus = self.m_Status[iStatus]
            if not oStatus.Check(oOwner, dCtrl):
                return False
        if not (oStatus.m_ServerUpdate) and not oStatus.CheckMoveAttr(self, oOwner, dCtrl):
            return False
        return oStatus.Do(self, oOwner, dCtrl)

    
    def Move(self, oOwner, iFrame, vStart, lstDisp):
        if self.m_MoveBackCheck:
            MoveLog.Warn('%d %s client pass1 %d %d %s disp %s' % (oOwner.m_PlayerID, oOwner.m_Scene, iFrame, self.m_MoveBackCheck, OutputPos(vStart), [ (OutputPos(v[0]), v[1]) for v in lstDisp ]))
            return None
        if iFrame <= self.m_ClientFrame:
            MoveLog.Warn('%d %s client pass2 %d %d %s disp %s' % (oOwner.m_PlayerID, oOwner.m_Scene, iFrame, self.m_ClientFrame, OutputPos(vStart), [ (OutputPos(v[0]), v[1]) for v in lstDisp ]))
            return None
        self.m_ClientFrame = iFrame
        self.m_ClientRtt = self.m_Game.GetFrameNum() - iFrame
        self.m_MoveBuffer.append((iFrame, vStart, lstDisp))

    
    def AddDashExtInfo(self, iFrame, lstActNum):
        if iFrame in self.m_DashExtBuffer:
            return None
        self.m_DashExtBuffer[iFrame] = lstActNum

    
    def MoveBackAnswer(self, oOwner, iFrame):
        MoveLog.Info('%d back ans %d ' % (oOwner.m_PlayerID, iFrame))
        if self.m_MoveBackCheck != iFrame:
            return None
        self.m_ClientFrame = iFrame
        self.m_ClientRtt = self.m_Game.GetFrameNum() - iFrame
        self.m_MoveBackCheck = 0
        self.ClearBuffer()

    
    def UpdateCtrlFrame(self, oOwner, iServerFrame):
        if self.m_MoveBuffer:
            self.ClientUpdate(oOwner, iServerFrame)
        oStatus = self.m_Status[self.m_CurStatus]
        if oStatus.m_ServerUpdate:
            oStatus.ServerUpdate(self, oOwner, iServerFrame)
        elif not (self.m_MoveBackCheck) and not self.IsGround() and self.m_ClientFrame + self.m_ClientRtt < self.m_Game.GetFrameNum() - 15:
            self.Stop(oOwner, 'noclient')
        self.PushPacket(oOwner)

    
    def ClientUpdate(self, oOwner, iServerFrame):
        for idx, (iFrame, vStart, lstDisp) in enumerate(self.m_MoveBuffer):
            dCtrl = {
                'Frame': iFrame,
                'Pos': vStart,
                'Delta': 0.02 }
            if lstDisp[0][1] != STATUS_DASH:
                if len(lstDisp) == 1 or lstDisp[0][1] == lstDisp[1][1]:
                    iStatus = lstDisp[0][1]
                    dCtrl['Disp'] = [ data[0] for data in lstDisp ]
                    dCtrl['TotDisp'] = cl_math.Vec3Sum(dCtrl['Disp'])
                    bRet = self.ContinueStatus(oOwner, iStatus, dCtrl)
            bRet = True
            for iOffset, (vDisp, iStatus) in enumerate(lstDisp):
                dCtrl['Disp'] = [
                    vDisp]
                dCtrl['TotDisp'] = vDisp
                if iStatus == STATUS_DASH and iFrame in self.m_DashExtBuffer and iOffset < len(self.m_DashExtBuffer[iFrame]):
                    dCtrl['ActNum'] = self.m_DashExtBuffer[iFrame][iOffset]
                if not self.ContinueStatus(oOwner, iStatus, dCtrl):
                    bRet = False
                    break
                vStart = cl_math.Vec3Add(vStart, vDisp)
                dCtrl['Pos'] = vStart
            
            if not bRet:
                self.ClearBuffer()
                break
            self.PushPacket(oOwner)
        

    
    def ClearBuffer(self):
        if self.m_DashExtBuffer:
            dRestDash = { }
            for iFrame, lstActNum in self.m_DashExtBuffer.items():
                if iFrame > self.m_ClientFrame:
                    dRestDash[iFrame] = lstActNum
            
            self.m_DashExtBuffer = dRestDash
        self.m_MoveBuffer.clear()

    
    def SendPacket(self, func, *args):
        self.m_PacketBuffer = (func, args)

    
    def PushPacket(self, oOwner):
        if not self.m_PacketBuffer:
            return None
        (func, args) = self.m_PacketBuffer
        self.m_PacketBuffer = None
        func(oOwner, *args)

    
    def ClearPacket(self):
        self.m_PacketBuffer = None

    
    def Stop(self, oOwner, sForceReason = ''):
        return self.ContinueStatus(oOwner, STATUS_SERVSTOP, {
            'Force': sForceReason })

    
    def PushMove(self, oOwner, vDir, fSpeed, fSecond, fDownSpeed, fGravaty, cbFunc = None):
        iFrame = self.m_Game.GetFrameNum()
        dCtrl = {
            'SFrame': iFrame,
            'Dir': vDir,
            'Speed': fSpeed,
            'Second': fSecond,
            'DownSpeed': fDownSpeed,
            'Gravaty': fGravaty,
            'CallBackFunc': cbFunc }
        return self.ContinueStatus(oOwner, STATUS_PUSH, dCtrl)

    
    def AddDashCtrlCheck(self, oOwner, dCtrl):
        if len(self.m_DashCache) >= self.m_DashCacheAlert:
            MoveLog.Debug('%d cache too more' % oOwner.m_PlayerID)
            self.m_DashCache.clear()
        iActNum = dCtrl['ActNum']
        self.m_DashCache[iActNum] = dCtrl



class CClientCtrlNavStay(ComNavStay):
    
    def __init__(self, oOwner):
        super().__init__(oOwner.m_Game.m_ID, oOwner.m_ID, 'NavStay')
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_DIEDIST, self.DieDist, 'ClientCtrlDie', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'ClientCtrlRelife', -1, 0)
        self.InitParams(oOwner)

    
    def Release(self, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_DIEDIST, 'ClientCtrlDie', -1)
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RELIFE, 'ClientCtrlRelife', -1)

    
    def InitParams(self, oOwner):
        (fNavRadius, fNavHeight) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'NavMesh')
        self.E_SetParams(fNavRadius, fNavHeight)

    
    def DieDist(self, oOwner, dInfo):
        self.E_Disable()

    
    def OnRelife(self, oOwner, dInfo):
        self.E_Enable()


