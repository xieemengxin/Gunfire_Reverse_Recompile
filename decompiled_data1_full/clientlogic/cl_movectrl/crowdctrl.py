# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/crowdctrl.pyc
# RelativePath: clientlogic/cl_movectrl/crowdctrl.pyc
# Source Generated with Decompyle++
# File: crowdctrl.pyc (Python 3.6)

from C_component import ComNavMove
from cl_only import GAME_FRAME_SECOND, Time2Frame, Functor, Second2Frame, GAME_FRAME, PY_FLAG_DEAD, GAME_FRAME_TIME, PythonError, OutputPos
from cl_commondefines import OP_DIRYAW, OP_JUMPSTART, OP_JUMPPOS, FACE_STATUS_PATH, FACE_STATUS_CROSSPATH, OP_NEWPATH, OP_NOFINDPATH, OP_FAILPATH, OP_ENDPATH, OP_SHOVE, OP_JUMPEND, FORBID_MOVE, STATUS_AIRLINE, STATUS_LINE, STATUS_JUMP, STATUS_PUSH, STATUS_DASH, STATUS_MOVE, MOVE_TYPE_FLY, PATHMODE_COLLISIONLESS, MOVE_TYPE_WINK, FORBID_PUSHED, WINK_PATHEND, PATHMODE_CROWDPUSH, PATHMODE_CROWDNORMAL, STATUS_AIRSTOP, PATHMODE_GHOST, STATUS_STOP, MOVE_TYPE_NORMAL, MOVE_TYPE_JUMP, STATUS_AIRCURVE, WARRIOR_SERVANT
from cl_commondefines import SAMEARRIVE_RETRY, SAMEARRIVE_RESET, PATHMODE_CROWDWINK, FORBID_DASH
from cl_commondefines import WARRIOR_BOSS
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_OBJECT, PXMASK_BLOCK
from cl_object.logging import CrowdLog
import cl_movectrl.mobject as base
import cl_movectrl.net as movenet
import cl_forbid
import cl_math
import cl_modeldefine
import cl_msgcenter
import cl_gamedebug as debug
import cl_snetwar
import cllib.lib_flag
import cllib.lib_only
from . import crowdpathparam
MAX_Acceleration = 10000
g_BagSummary = [
    0,
    0]

class CStopStatus(base.CActorStop):
    m_DefPathMode = PATHMODE_CROWDNORMAL
    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CStopStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        if oOwner.m_MoveMode == MOVE_TYPE_JUMP:
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner):
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        oCtrl.E_Stop()
        oCtrl.m_FollowTarget = 0
        oCtrl.OverArrive(oOwner, 0)
        if oCtrl.m_CurStatus == STATUS_STOP:
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return True



class CAirStopStatus(base.CActorStop):
    
    def OnEnter(self, oOwner):
        super(CAirStopStatus, self).OnEnter(oOwner)
        oOwner.m_MoveCtrl.SetPathMode('AirLineMove', PATHMODE_GHOST)

    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CAirStopStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner):
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        oCtrl.OverArrive(oOwner, 0)
        if oCtrl.m_CurStatus == STATUS_AIRSTOP:
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return True



class CMoveStatus(base.CActorMove):
    
    def OnEnter(self, oOwner):
        super(CMoveStatus, self).OnEnter(oOwner)
        iPathMode = oOwner.m_MoveCtrl.m_DefPathMode
        oOwner.m_MoveCtrl.SetPathMode('NormalMove', iPathMode)

    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CMoveStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        if oOwner.m_MoveMode == MOVE_TYPE_JUMP:
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner, tPos, cbFunc):
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        idx = oCtrl.GetCallBackIdx()
        if oCtrl.E_MovePos(idx, tPos):
            oCtrl.m_ArriveInfo = (idx, tPos, cbFunc)
            return 1
        return 0

    
    def OnExit(self, oOwner):
        super(CMoveStatus, self).OnExit(oOwner)
        oOwner.m_MoveCtrl.ClearPathMode('NormalMove')



class CJumpStatus(base.CActorJump):
    m_ForbidRule = cl_forbid.MONSJUMP_RULE
    
    def OnEnter(self, oOwner):
        super(CJumpStatus, self).OnEnter(oOwner)

    
    def Do(self, oCtrl, oOwner, *lstArgs):
        oOwner.m_MoveMode = MOVE_TYPE_JUMP
        if oOwner.m_FaceCtrl:
            vEnd = lstArgs[0]
            oOwner.m_FaceCtrl.LockFace(oOwner, cl_math.Vec3Minus(vEnd, oOwner.GetPos()), 'JumpLock')
        if len(lstArgs) == 2:
            vStart = lstArgs[1]
            oCtrl.m_JumpStart = vStart
            return None
        (vEnd, fSpeed, fHeight, tJumpTimeConfig, cbfunc) = lstArgs
        vStart = oOwner.GetPos()
        oCtrl.m_JumpStart = vStart
        if cl_math.IsZero(tJumpTimeConfig):
            tJumpTimeConfig = oCtrl.m_JumpTimeConfig
        (iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime) = tJumpTimeConfig
        idx = oCtrl.GetCallBackIdx()
        oCtrl.m_ArriveInfo = (idx, vEnd, cbfunc)
        oOwner.m_MoveCtrl.SetPathMode('JumpMove', PATHMODE_GHOST)
        lstPos = cl_math.CalJumpPath(vStart, vEnd, fSpeed * GAME_FRAME_SECOND, fHeight, Time2Frame(iJumpStartBufTime), Time2Frame(iJumpEndBufTime), Time2Frame(iJumpUpTime))
        movenet.GS2CMapJumpTrack(oOwner, vStart, vEnd, fSpeed, fHeight, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime)
        self.JumpStep(oOwner, lstPos[::-1], idx)

    
    def JumpStep(self, oOwner, lstPos, idx):
        oCtrl = oOwner.m_MoveCtrl
        if oOwner.IsDead():
            return None
        if not (oCtrl.m_ArriveInfo) or oCtrl.m_ArriveInfo[0] != idx:
            return None
        vPos = lstPos.pop(-1)
        oOwner.m_Game.Scene_Walk(oOwner.m_ID, vPos)
        oOwner.RefreshPos()
        if lstPos:
            oOwner.Call_Out_Lockable(Functor(self.JumpStep, oOwner, lstPos, idx), 1, 'JumpStep')
        else:
            (_, tTar, cbfunc) = oCtrl.m_ArriveInfo
            oCtrl.m_ArriveInfo = None
            oCtrl.m_MoveFrame = 0
            oOwner.m_MoveMode = MOVE_TYPE_NORMAL
            oCtrl.ChangeStatus(oOwner, STATUS_STOP)
            if cbfunc:
                cbfunc(oOwner, tTar, iFail = 0)

    
    def OnExit(self, oOwner):
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        super(CJumpStatus, self).OnExit(oOwner)
        if oOwner.m_FaceCtrl:
            oOwner.m_FaceCtrl.UnLockFace(oOwner, 'JumpLock')
        oOwner.Remove_Call_Out_Lockable('JumpStep')
        oOwner.m_MoveCtrl.ClearPathMode('JumpMove')
        cbfunc = oOwner.m_MoveCtrl.m_JumpEndCB
        if cbfunc:
            oOwner.m_MoveCtrl.m_JumpEndCB = None
            cbfunc()



class CWinkStatus(base.CActorWinkMove):
    m_DefPathMode = PATHMODE_CROWDWINK
    
    def OnEnter(self, oOwner):
        super(CWinkStatus, self).OnEnter(oOwner)
        oOwner.m_MoveCtrl.SetPathMode('WinkMove', self.m_DefPathMode)

    
    def WinkMovePathEnd(self, oOwner, tPos, iFail):
        oCtrl = oOwner.m_MoveCtrl
        if oCtrl.m_WinkMoveCB:
            cbFunc = oCtrl.m_WinkMoveCB
            oCtrl.m_WinkMoveCB = None
            cbFunc(oOwner, WINK_PATHEND)

    
    def WinkMoveTimeOut(self, oOwner):
        oCtrl = oOwner.m_MoveCtrl
        oCtrl.Stop(oOwner)

    
    def OnExit(self, oOwner):
        super(CWinkStatus, self).OnExit(oOwner)
        oCtrl = oOwner.m_MoveCtrl
        oOwner.m_WinkSpeed = 0
        oOwner.Remove_Call_Out_Lockable('WinkMove')
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        oOwner.m_MoveCtrl.ClearPathMode('WinkMove')
        oCtrl.E_SetSpeed(oOwner.MoveSpeed())
        oOwner.GS2CPropChange('Speed')
        oCtrl.OverArrive(oOwner, 0)



class CPushStatus(CWinkStatus):
    m_ForbidRule = cl_forbid.PUSHED_RULE
    m_CheckForbid = FORBID_PUSHED
    m_DefPathMode = PATHMODE_CROWDPUSH
    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CPushStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        oCtrl = oOwner.m_MoveCtrl
        if oCtrl.m_CurStatus == STATUS_PUSH:
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner, tDir, fSpeed, fSecond, iClientAni, iFace2Dir, cbFunc):
        if cl_math.IsPlaneZero(tDir):
            return 0
        tDir = (tDir[0], 0, tDir[2])
        idx = oCtrl.GetCallBackIdx()
        oOwner.m_WinkSpeed = fSpeed
        oOwner.m_MoveMode = MOVE_TYPE_WINK
        oCtrl.E_SetSpeed(fSpeed)
        oCtrl.E_MoveDir(idx, tDir)
        iFrame = Second2Frame(fSecond)
        oOwner.Call_Out_Lockable(Functor(self.WinkMoveTimeOut, oOwner), iFrame + 1, 'WinkMove')
        vStart = oOwner.GetPos()
        vPos = cl_math.Vec3DisplaceDir(vStart, tDir, fSpeed * fSecond)
        oCtrl.m_ArriveInfo = (idx, vPos, self.WinkMovePathEnd)
        oCtrl.m_WinkMoveCB = cbFunc
        oOwner.GS2CPropChange('Speed')
        if oOwner.m_FaceCtrl:
            if iFace2Dir:
                (x, _, z) = cl_math.Vec3Normalize((tDir[0], 0, tDir[2]))
            else:
                (x, _, z) = cl_math.Vec3Normalize((-tDir[0], 0, -tDir[2]))
            vFace = (int(x * 127) + 128, 128, int(z * 127) + 128)
            cl_snetwar.GS2CFace(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, vFace, 10)
        oCtrl.m_CurPath = [
            vStart,
            vPos]
        movenet.GS2CMapPushTrack(oOwner, fSpeed, vStart, vPos, iClientAni)
        return 1

    
    def OnExit(self, oOwner):
        super(CPushStatus, self).OnExit(oOwner)
        if oOwner.m_Agent:
            oOwner.m_Agent.ResumeFaceStatus()



class CDashStatus(CWinkStatus):
    m_ForbidRule = cl_forbid.DASH_RULE
    m_CheckForbid = FORBID_DASH
    m_DefPathMode = PATHMODE_COLLISIONLESS
    
    def Do(self, oCtrl, oOwner, tDir, fSpeed, fSecond, cbFunc, fSlideTime):
        idx = oCtrl.GetCallBackIdx()
        oOwner.m_WinkSpeed = fSpeed
        oOwner.m_MoveMode = MOVE_TYPE_WINK
        oCtrl.E_SetSpeed(oOwner.m_WinkSpeed)
        vStart = oOwner.GetPos()
        fDistance = fSpeed * fSecond
        iSlideFrame = Second2Frame(fSlideTime)
        if cl_math.IsPlaneZero(tDir):
            bSuccess = False
        else:
            bSuccess = oCtrl.E_MoveDir(idx, tDir, iSlideFrame)
        if not bSuccess:
            oCtrl.m_WinkMoveCB = cbFunc
            oCtrl.m_ArriveInfo = (idx, vStart, self.WinkMovePathEnd)
            oOwner.Call_Out_Lockable(Functor(self.WinkMoveTimeOut, oOwner), 1, 'WinkMove')
            return 1
        vPos = cl_math.Vec3DisplaceDir(vStart, tDir, fDistance)
        oCtrl.m_WinkMoveCB = cbFunc
        oCtrl.m_ArriveInfo = (idx, vPos, self.WinkMovePathEnd)
        oCtrl.m_CurPath = [
            vStart,
            vPos]
        movenet.GS2CMapDashTrack(oOwner, oOwner.m_WinkSpeed, vStart, vPos)
        iFrame = Second2Frame(fSecond)
        self.DashStep(oOwner, vStart, tDir, idx, iFrame)
        oOwner.Call_Out_Lockable(Functor(self.WinkMoveTimeOut, oOwner), iFrame + 1, 'WinkMove')
        return 1

    
    def DashStep(self, oOwner, lpos, ldir, idx, iWaitFrame):
        oCtrl = oOwner.m_MoveCtrl
        if oOwner.IsDead():
            return None
        if not (oCtrl.m_ArriveInfo) or oCtrl.m_ArriveInfo[0] != idx:
            return None
        vNow = oOwner.GetPos()
        tDir = cl_math.Vec3Minus(vNow, lpos)
        if not cl_math.IsPlaneZero(tDir) and not cl_math.IsPlaneEqual(tDir, ldir):
            fDistance = oOwner.m_WinkSpeed * iWaitFrame * GAME_FRAME_SECOND
            vPos = cl_math.Vec3DisplaceDir(vNow, tDir, fDistance)
            oCtrl.m_ArriveInfo = (idx, vPos, self.WinkMovePathEnd)
            oCtrl.m_CurPath = [
                vNow,
                vPos]
            dis = cl_math.CalDistance3D(lpos, vNow)
            oOwner.m_WinkSpeed = dis * GAME_FRAME
            movenet.GS2CMapDashTrack(oOwner, oOwner.m_WinkSpeed, vNow, vPos)
        iWaitFrame -= 1
        if iWaitFrame > 0:
            func = Functor(self.DashStep, oOwner, vNow, tDir, idx, iWaitFrame)
            oOwner.Call_Out_Lockable(func, 1, 'DashStep')

    
    def OnExit(self, oOwner):
        oOwner.Remove_Call_Out_Lockable('DashStep')
        super().OnExit(oOwner)



class CLineStatus(base.CActorMove):
    
    def OnEnter(self, oOwner):
        super(CLineStatus, self).OnEnter(oOwner)
        oOwner.m_MoveCtrl.SetPathMode('LineMove', PATHMODE_GHOST)

    
    def Do(self, oCtrl, oOwner, lstPath, fSpeed, cbFunc, iGround):
        idx = oCtrl.GetCallBackIdx()
        oCtrl.m_ArriveInfo = (idx, lstPath[-1], cbFunc)
        lstSend = [
            oOwner.GetPos()]
        lstSend.extend(lstPath)
        movenet.GS2CMapTrack(oOwner, lstSend)
        if not fSpeed or fSpeed <= 0:
            fSpeed = oOwner.MoveSpeed()
        fFrameSpeed = fSpeed * GAME_FRAME_SECOND
        oCtrl.m_CurPath = lstSend
        oOwner.Call_Out_Lockable(Functor(self.MoveStep, oOwner, lstPath, fFrameSpeed, idx, iGround), 1, 'MoveStep')
        return 1

    
    def OnExit(self, oOwner):
        super(CLineStatus, self).OnExit(oOwner)
        oOwner.m_MoveCtrl.ClearPathMode('LineMove')
        oOwner.Remove_Call_Out_Lockable('MoveStep')
        oOwner.m_MoveCtrl.OverArrive(oOwner, iFail = 1)

    
    def MoveStep(self, oOwner, lstPath, fFrameSpeed, idx, iGround):
        oCtrl = oOwner.m_MoveCtrl
        if oOwner.IsDead():
            return None
        if not (oCtrl.m_ArriveInfo) or oCtrl.m_ArriveInfo[0] != idx:
            return None
        vNow = oOwner.GetPos()
        bContinue = True
        fStepDis = fFrameSpeed
        for i, vNext in enumerate(lstPath):
            fDis = cl_math.CalDistance(vNow, vNext)
            if fDis > fStepDis:
                vMove = cl_math.Vec3DisplacePos(vNow, vNext, fStepDis)
                if i:
                    lstPath = lstPath[i:]
                break
            fStepDis -= fDis
            vNow = vNext
        else:
            vMove = lstPath[-1]
            bContinue = False
        if iGround:
            fGroundDis = oOwner.m_Game.Scene_GroundDistance(oOwner.m_Scene, (vMove[0], vMove[1] + 1.8, vMove[2]), 5, PXMASK_MOVEBLK | PXMASK_OBJECT, oOwner.m_ID)
            vMove = (vMove[0], (vMove[1] - fGroundDis) + 1.8, vMove[2])
        if oOwner.m_FaceCtrl:
            (x, _, z) = cl_math.Vec3Minus(vMove, vNow)
            oOwner.m_FaceCtrl.OnNextPath(oOwner, x, z)
        oOwner.m_Game.Scene_Walk(oOwner.m_ID, vMove)
        vNow = oOwner.RefreshPos()
        oCtrl.m_MoveFrame += 1
        movenet.GS2CMapTickPos(oOwner, oCtrl.m_MoveFrame, vNow)
        if bContinue:
            oOwner.Call_Out_Lockable(Functor(self.MoveStep, oOwner, lstPath, fFrameSpeed, idx, iGround), 1, 'MoveStep')
        else:
            oCtrl.OverArrive(oOwner, 0)



class CAirLineStatus(base.CActorMove):
    m_ForbidRule = cl_forbid.AIRLINE_RULE
    
    def OnEnter(self, oOwner):
        super(CAirLineStatus, self).OnEnter(oOwner)
        oOwner.m_MoveCtrl.SetPathMode('AirLineMove', PATHMODE_GHOST)

    
    def Do(self, oCtrl, oOwner, vEnd, fSpeed, bUseFlyMode, cbFunc):
        idx = oCtrl.GetCallBackIdx()
        oCtrl.m_ArriveInfo = (idx, vEnd, cbFunc)
        vStart = oOwner.GetPos()
        if bUseFlyMode:
            oOwner.m_MoveMode = MOVE_TYPE_FLY
        movenet.GS2CMapAirTrack(oOwner, fSpeed, vStart, vEnd)
        fFrameSpeed = fSpeed * GAME_FRAME_SECOND
        oOwner.Remove_Call_Out_Lockable('MoveStep')
        oOwner.Call_Out_Lockable(Functor(self.MoveStep, oOwner, vEnd, fFrameSpeed, idx), 1, 'MoveStep')
        return 1

    
    def OnExit(self, oOwner):
        super(CAirLineStatus, self).OnExit(oOwner)
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        oOwner.m_MoveCtrl.ClearPathMode('AirLineMove')
        oOwner.Remove_Call_Out_Lockable('MoveStep')
        oOwner.m_MoveCtrl.OverArrive(oOwner, iFail = 1)

    
    def MoveStep(self, oOwner, vEnd, fFrameSpeed, idx):
        oCtrl = oOwner.m_MoveCtrl
        if oOwner.IsDead():
            return None
        if not (oCtrl.m_ArriveInfo) or oCtrl.m_ArriveInfo[0] != idx:
            return None
        vNow = oOwner.GetPos()
        fStepDis = fFrameSpeed
        fDis = cl_math.CalDistance3D(vNow, vEnd)
        if fDis > fStepDis:
            vMove = cl_math.Vec3DisplacePos(vNow, vEnd, fStepDis)
            bContinue = True
        else:
            vMove = vEnd
            bContinue = False
        oOwner.m_Game.Scene_Walk(oOwner.m_ID, vMove)
        oOwner.RefreshPos()
        if bContinue:
            oOwner.Call_Out_Lockable(Functor(self.MoveStep, oOwner, vEnd, fFrameSpeed, idx), 1, 'MoveStep')
        else:
            oCtrl.OverArrive(oOwner, 0)



class CAirCurveStatus(CAirLineStatus):
    
    def Do(self, oCtrl, oOwner, fSpeed, cbFunc):
        idx = oCtrl.GetCallBackIdx()
        oCurve = oOwner.m_CurveCompute
        oOwner.m_MoveMode = MOVE_TYPE_FLY
        oCtrl.m_CustomData['AirMoveSpeed'] = fSpeed
        oCtrl.m_ArriveInfo = (idx, oCurve.m_End, cbFunc)
        fAllLength = oCurve.GetBezierLength()
        iAllFrame = int(fAllLength / (fSpeed * GAME_FRAME_SECOND))
        self.CurveMove(oOwner, 1, iAllFrame, idx)
        movenet.GS2CCurveTrack(oOwner, fSpeed, 0, (oCurve.m_Start, oCurve.m_Mid, oCurve.m_End))
        return 1

    
    def CurveMove(self, oOwner, iStep, iTotalStep, idx):
        oCtrl = oOwner.m_MoveCtrl
        if oOwner.IsDead():
            return None
        if not (oCtrl.m_ArriveInfo) or oCtrl.m_ArriveInfo[0] != idx:
            return None
        if iStep < iTotalStep:
            bContinue = True
            vMove = oOwner.m_CurveCompute.GetPos(iStep / iTotalStep)
        else:
            bContinue = False
            vMove = oOwner.m_CurveCompute.m_End
        oCtrl.m_CustomData['AirCurveMovedTime'] = iStep * GAME_FRAME_TIME
        oOwner.m_Game.Scene_Walk(oOwner.m_ID, vMove)
        oOwner.RefreshPos()
        if bContinue:
            oOwner.Call_Out_Lockable(Functor(self.CurveMove, oOwner, iStep + 1, iTotalStep, idx), 1, 'CurveMove')
        else:
            oCtrl.OverArrive(oOwner, 0)



class CHeroPushStatus(CPushStatus):
    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CHeroPushStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        if oOwner.m_MoveMode == MOVE_TYPE_JUMP:
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner, tDir, fSpeed, fSecond, iClientAni, cbFunc):
        if cl_math.IsPlaneZero(tDir):
            return 0
        tDir = (tDir[0], 0, tDir[2])
        idx = oCtrl.GetCallBackIdx()
        oOwner.m_WinkSpeed = fSpeed
        oOwner.m_MoveMode = MOVE_TYPE_WINK
        oCtrl.E_SetSpeed(fSpeed)
        oCtrl.E_MoveDir(idx, tDir)
        iFrame = Second2Frame(fSecond)
        oOwner.Call_Out_Lockable(Functor(self.WinkMoveTimeOut, oOwner), iFrame + 1, 'WinkMove')
        vStart = oOwner.GetPos()
        vPos = cl_math.Vec3DisplaceDir(vStart, tDir, fSpeed * fSecond)
        oCtrl.m_ArriveInfo = (idx, vPos, self.WinkMovePathEnd)
        oCtrl.m_WinkMoveCB = cbFunc
        oOwner.GS2CPropChange('Speed')
        oCtrl.m_CurPath = [
            vStart,
            vPos]
        movenet.GS2CMapPushTrack(oOwner, fSpeed, vStart, vPos, iClientAni)
        return 1



class CCrowdCtrlMgr(base.CActorCtrlMgr, ComNavMove):
    m_Status = {
        STATUS_AIRCURVE: CAirCurveStatus(),
        STATUS_AIRSTOP: CAirStopStatus(),
        STATUS_AIRLINE: CAirLineStatus(),
        STATUS_LINE: CLineStatus(),
        STATUS_JUMP: CJumpStatus(),
        STATUS_STOP: CStopStatus(),
        STATUS_PUSH: CPushStatus(),
        STATUS_DASH: CDashStatus(),
        STATUS_MOVE: CMoveStatus() }
    m_InitStatus = STATUS_STOP
    
    def __init__(self, oOwner):
        base.CActorCtrlMgr.__init__(self, oOwner)
        ComNavMove.__init__(self, oOwner.m_Game.m_ID, oOwner.m_ID, 'NavMove')
        self.m_Owner = oOwner
        self.m_ArriveInfo = ()
        self.m_CurPath = []
        self.m_MoveFrame = 0
        self.m_WinkMoveCB = None
        self.m_JumpEndCB = None
        self.m_JumpStart = None
        self.m_CallBackIdx = 0
        self.m_FollowTarget = 0
        self.m_PathMode = 0
        self.m_PathModeList = []
        self.m_FollowDeflexion = { }
        self.InitParams(oOwner)
        self.m_CustomData = { }
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'CrowdCtrlDie', -1, 0)
        oGame = oOwner.m_Game
        oGame.AddGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'CrowdPlayerLoadMapOk%d' % self.m_Owner.m_ID)

    
    def InitParams(self, oOwner):
        (fNavRadius, fNavHeight) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'NavMesh')
        self.SetNavParams(oOwner, fNavRadius, fNavHeight)

    
    def SetNavParams(self, oOwner, fNavRadius, fNavHeight):
        self.m_NavRadius = fNavRadius
        (self.m_JumpSpeed, self.m_JumpHeight, self.m_JumpTimeConfig) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'Jump')
        fSpeed = oOwner.MoveSpeed()
        tJumpTimeConfig = cl_math.Vec3MulF(self.m_JumpTimeConfig, 0.01)
        self.E_SetParams(fNavRadius, fNavHeight, fSpeed, MAX_Acceleration, self.m_JumpSpeed, self.m_JumpHeight, tJumpTimeConfig)

    
    def Release(self, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_DIE, 'CrowdCtrlDie')
        oGame = oOwner.m_Game
        oGame.DoneGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'CrowdPlayerLoadMapOk%d' % self.m_Owner.m_ID)
        super().Release(oOwner)
        self.m_Owner = None
        self.m_WinkMoveCB = None
        self.m_JumpEndCB = None

    
    def OnDie(self, oOwner, dInfo):
        self.E_Disable()

    
    def GetCallBackIdx(self):
        self.m_CallBackIdx += 1
        if self.m_CallBackIdx >= 2147483647:
            self.m_CallBackIdx = 1
        return self.m_CallBackIdx

    
    def OverArrive(self, oOwner, iFail, iCallBack = 1):
        if not self.m_ArriveInfo:
            return None
        (_, tPos, cbfunc) = self.m_ArriveInfo
        self.m_ArriveInfo = None
        self.m_CurPath = []
        self.m_MoveFrame = 0
        if cbfunc and iCallBack:
            cbfunc(oOwner, tPos, iFail)

    
    def HasSameArriveInfo(self, tPos):
        (x, _, z) = tPos
        if self.m_ArriveInfo and x == self.m_ArriveInfo[1][0] and z == self.m_ArriveInfo[1][2]:
            return True
        return False

    
    def HasSameArriveTarget(self, iTarget):
        if self.m_ArriveInfo:
            pass
        return self.m_FollowTarget == iTarget

    
    def SeekPath(self, oOwner, tPos, func = None):
        return self.CtrlOP(oOwner, STATUS_MOVE, tPos, func)

    
    def FollowMove(self, oOwner, iTarget, fStopDis, func = None, idx = 0, iAppointFrame = 0, iPyFlag = PY_FLAG_DEAD):
        oOwner.Remove_Call_Out('FollowMove')
        if idx:
            if not (self.m_ArriveInfo) or self.m_ArriveInfo[0] != idx:
                self.m_FollowTarget = 0
                return False
        if oOwner.IsForbid(FORBID_MOVE):
            self.m_FollowTarget = 0
            return False
        oGame = oOwner.m_Game
        oTarget = oGame.GetObject(iTarget, iPyFlag)
        if not oTarget:
            self.m_FollowTarget = 0
            return False
        vTarget = oTarget.GetGroundPos()
        vOwner = oOwner.GetPos()
        fDis = cl_math.CalDistance3D(vOwner, vTarget)
        fRestDis = fDis - fStopDis
        if fRestDis <= 0 and abs(vOwner[1] - vTarget[1]) <= 1.5:
            self.Stop(oOwner)
            return True
        iRet = 1
        if iTarget not in self.m_FollowDeflexion:
            self.m_FollowDeflexion[iTarget] = (oGame.Random(6) - 3) * 10 + 5
        (fTargetRadius, _) = cl_modeldefine.GetModelDefine(oTarget.m_Shape, 'NavMesh')
        vEnd = cl_math.Vec3DestPosDirPlane(vTarget, cl_math.Vec3Minus(vOwner, vTarget), self.m_NavRadius + fTargetRadius, self.m_FollowDeflexion[iTarget])
        if not self.HasSameArriveInfo(vEnd):
            iRet = self.SeekPath(oOwner, vEnd, func)
        if iRet:
            if iAppointFrame:
                iRefreshFrame = iAppointFrame
            else:
                fSpeed = oOwner.MoveSpeed()
                iRefreshFrame = max(Second2Frame(fRestDis * 0.5 / fSpeed), 5)
                if iRefreshFrame > 15:
                    iRefreshFrame = 15
            idx = self.m_ArriveInfo[0]
            self.m_FollowTarget = iTarget
            oOwner.Call_Out(Functor(self.FollowMove, oOwner, iTarget, fStopDis, func, idx, iAppointFrame, iPyFlag), iRefreshFrame, 'FollowMove')
        elif oOwner.m_MoveMode == MOVE_TYPE_JUMP:
            self.m_JumpEndCB = Functor(self.FollowMove, oOwner, iTarget, fStopDis, func, idx, iAppointFrame, iPyFlag)
            return True
        if not iRet:
            self.E_Stop()
            self.m_FollowTarget = 0
            self.OverArrive(oOwner, iFail = 1)
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return iRet == 1

    
    def DashMove(self, oOwner, tDir, fSpeed, fSecond, func = None, fSlideTime = 0):
        return self.CtrlOP(oOwner, STATUS_DASH, tDir, fSpeed, fSecond, func, fSlideTime)

    
    def PushMove(self, oOwner, tDir, fSpeed, fSecond, iClientAni = 1, iFace2Dir = 0, func = None):
        return self.CtrlOP(oOwner, STATUS_PUSH, tDir, fSpeed, fSecond, iClientAni, iFace2Dir, func)

    
    def DirectMove(self, oOwner, lstPath, fSpeed, func, iGround):
        return self.CtrlOP(oOwner, STATUS_LINE, lstPath, fSpeed, func, iGround)

    
    def AirMove(self, oOwner, vEnd, fSpeed, bUseFlyMode, func = None):
        return self.CtrlOP(oOwner, STATUS_AIRLINE, vEnd, fSpeed, bUseFlyMode, func)

    
    def AirCurveMove(self, oOwner, fSpeed, func):
        return self.CtrlOP(oOwner, STATUS_AIRCURVE, fSpeed, func)

    
    def JumpMove(self, oOwner, vEnd, fSpeed, fHeight, tJumpTimeConfig, func = None):
        return self.CtrlOP(oOwner, STATUS_JUMP, vEnd, fSpeed, fHeight, tJumpTimeConfig, func)

    
    def Stop(self, oOwner):
        return self.CtrlOP(oOwner, STATUS_STOP)

    
    def AirStop(self, oOwner):
        return self.CtrlOP(oOwner, STATUS_AIRSTOP)

    
    def StopJump(self):
        pass

    
    def IsStop(self, oOwner):
        return self.E_IsStop()

    
    def SetSpeed(self, oOwner, fSpeed):
        self.E_SetSpeed(fSpeed)
        if not (oOwner.m_MoveMode & (MOVE_TYPE_WINK | MOVE_TYPE_JUMP)) and self.m_ArriveInfo:
            movenet.GS2CMapTrack(oOwner, self.E_GetPathData())

    
    def SetPathMode(self, sKey, iMode):
        self.m_PathModeList.append((sKey, iMode))
        self.UpdatePathMode()

    
    def ClearPathMode(self, sKey):
        lstNew = []
        for _key, _mode in self.m_PathModeList:
            if _key != sKey:
                lstNew.append((_key, _mode))
        
        self.m_PathModeList = lstNew
        self.UpdatePathMode()

    
    def UpdatePathMode(self):
        if not self.m_PathModeList:
            iFirstMode = self.m_DefPathMode
        else:
            (_, iFirstMode) = self.m_PathModeList[-1]
        self.m_PathMode = iFirstMode
        dParam = crowdpathparam.GetCrowdPathModeParam(iFirstMode)
        if self.m_Owner.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            dParam['rvo'] = 0
            dParam['sep'] = 0
        self.E_SetPathMode(dParam)

    
    def GetPathDir(self):
        (x, y, z) = self.E_GetPathDir()
        return (x, z)

    
    def OnPlayerMapLoadOK(self, oOwner, oTarget, dInfo):
        if self.m_CurStatus == STATUS_MOVE:
            pid = dInfo['pid']
            lstPath = self.E_GetPathData()
            movenet.GS2CRefreshTrack(self.m_Owner, pid, self.m_MoveFrame, lstPath)
        elif self.m_CurStatus == STATUS_AIRLINE or self.m_ArriveInfo:
            vStart = oOwner.GetPos()
            vEnd = self.m_ArriveInfo[1]
            fSpeed = self.m_CustomData.get('AirMoveSpeed')
            if not fSpeed:
                fSpeed = oOwner.MoveSpeed()
            movenet.GS2CMapAirTrack(oOwner, fSpeed, vStart, vEnd)
        elif self.m_CurStatus == STATUS_AIRCURVE and self.m_ArriveInfo and oOwner.m_CurveCompute:
            vStart = oOwner.GetPos()
            vEnd = self.m_ArriveInfo[1]
            fSpeed = self.m_CustomData.get('AirMoveSpeed')
            if not fSpeed:
                fSpeed = oOwner.MoveSpeed()
            iTime = self.m_CustomData.get('AirCurveMovedTime', 0)
            oCurve = oOwner.m_CurveCompute
            movenet.GS2CCurveTrack(oOwner, fSpeed, iTime, (oCurve.m_Start, oCurve.m_Mid, oCurve.m_End))

    
    def C_UpdatePos(self, idx, tPos, iOP):
        obj = self.m_Owner
        obj.m_Pos = tPos
        if iOP & OP_JUMPEND:
            obj.m_MoveMode = MOVE_TYPE_NORMAL
            self.ChangeStatus(obj, STATUS_MOVE)
        if not (self.m_ArriveInfo) or idx != self.m_ArriveInfo[0]:
            if iOP == OP_SHOVE:
                movenet.GS2CMapCrowdPos(obj, tPos)
            return None
        if iOP & (OP_FAILPATH | OP_ENDPATH):
            movenet.GS2CStop(obj, tPos)
            iFail = 1 if iOP & (OP_FAILPATH | OP_NOFINDPATH) else 0
            self.OverArrive(obj, iFail)
        elif iOP & OP_NEWPATH:
            if self.m_CurStatus not in (STATUS_PUSH, STATUS_DASH):
                if obj.m_FaceCtrl and obj.m_FaceCtrl.m_CurStatus in (FACE_STATUS_PATH, FACE_STATUS_CROSSPATH):
                    (dx, _, dz) = self.E_GetPathDir()
                    obj.m_FaceCtrl.OnNextPath(obj, dx, dz)
                lstPath = self.E_GetPathData()
                self.m_CurPath = lstPath
                movenet.GS2CMapTrack(obj, lstPath)
        elif iOP & OP_JUMPPOS:
            if iOP & OP_JUMPSTART:
                (tStart, tEnd) = self.E_GetPathData()
                self.CtrlOP(obj, STATUS_JUMP, tEnd, tStart)
                (iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime) = self.m_JumpTimeConfig
                movenet.GS2CMapJumpTrack(obj, tStart, tEnd, self.m_JumpSpeed, self.m_JumpHeight, iJumpStartBufTime, iJumpEndBufTime, iJumpUpTime)
        else:
            self.m_MoveFrame += 1
            if cllib.lib_flag.g_IsMobileRun and cllib.lib_only.GetServerGroup() not in ('sh',):
                if iOP & OP_DIRYAW:
                    g_BagSummary[0] += 1
                    movenet.GS2CMapTickPos(obj, self.m_MoveFrame, tPos)
                g_BagSummary[1] += 1
                if g_BagSummary[1] % 10000 == 0:
                    CrowdLog.Info('bag summary %s %f' % (g_BagSummary, g_BagSummary[0] / g_BagSummary[1]))
                else:
                    movenet.GS2CMapTickPos(obj, self.m_MoveFrame, tPos)
        return 1



class CServantCrowCtrlMgr(CCrowdCtrlMgr):
    
    def __init__(self, oOwner):
        super().__init__(oOwner)
        self.m_SameArriveTimes = 0

    
    def StopJump(self):
        oOwner = self.m_Owner
        if oOwner.m_MoveMode == MOVE_TYPE_JUMP:
            self.E_Disable()
            self.E_Enable()
            oOwner.m_MoveMode = MOVE_TYPE_NORMAL
            self.ChangeStatus(oOwner, STATUS_STOP)

    
    def HasSameArriveInfo(self, tPos):
        (x, _, z) = tPos
        if self.m_ArriveInfo and x == self.m_ArriveInfo[1][0] and z == self.m_ArriveInfo[1][2]:
            self.m_SameArriveTimes += 1
            return self.m_SameArriveTimes <= SAMEARRIVE_RETRY
        self.m_SameArriveTimes = 0
        return False

    
    def CheckResetArriveInfo(self):
        if self.m_SameArriveTimes <= SAMEARRIVE_RESET:
            return False
        oOwner = self.m_Owner
        tPos = self.m_ArriveInfo[1] if self.m_ArriveInfo else ()
        CrowdLog.Info('%d %d reset arrive %d %s' % (oOwner.m_Game.m_ID, oOwner.m_OwnerPlayerID, oOwner.m_MoveMode, OutputPos(tPos)))
        return True

    
    def OverArrive(self, oOwner, iFail, iCallBack = 1):
        self.m_SameArriveTimes = 0
        super().OverArrive(oOwner, iFail, iCallBack)

    
    def C_UpdatePos(self, idx, tPos, iOP):
        obj = self.m_Owner
        if iOP & OP_ENDPATH and self.m_ArriveInfo and obj.m_MoveMode != MOVE_TYPE_WINK:
            (_, tTargetPos, _) = self.m_ArriveInfo
            if not cl_math.CheckDistance(tPos, tTargetPos, 5) and obj.m_Agent:
                bAnyHit = obj.m_Game.Scene_RaycastAnyHit(obj.m_Scene, tPos, tTargetPos, PXMASK_MOVEBLK)
                if bAnyHit:
                    CrowdLog.Info('%d %d seravnt 0x%x %d %s inaccessible %s' % (obj.m_Game.m_ID, obj.m_OwnerPlayerID, obj.m_MoveMode, self.m_CurStatus, OutputPos(tPos), OutputPos(tTargetPos)))
                    self.OverArrive(obj, iFail = 1, iCallBack = 1)
                    oAgent = obj.m_Agent
                    oAgent.ChooseOwnerAroundPos(3, 5, 0, 180, oAgent)
                    oAgent.FlashToPos(oAgent)
                    return None
        super().C_UpdatePos(idx, tPos, iOP)



class CHeroCrowdCtrl(CCrowdCtrlMgr):
    m_Status = {
        STATUS_AIRCURVE: CAirCurveStatus(),
        STATUS_AIRSTOP: CAirStopStatus(),
        STATUS_AIRLINE: CAirLineStatus(),
        STATUS_LINE: CLineStatus(),
        STATUS_JUMP: CJumpStatus(),
        STATUS_STOP: CStopStatus(),
        STATUS_PUSH: CHeroPushStatus(),
        STATUS_DASH: CDashStatus(),
        STATUS_MOVE: CMoveStatus() }
    
    def __init__(self, oOwner):
        super().__init__(oOwner)
        self.m_SameArriveTimes = 0
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'CrowdCtrlDie', -1, 0)

    
    def Release(self, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RELIFE, 'CrowdCtrlDie')
        super().Release(oOwner)

    
    def InitParams(self, oOwner):
        (fNavRadius, fNavHeight) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'NavMesh')
        fNavRadius -= 0.3
        self.m_NavRadius = fNavRadius
        (self.m_JumpSpeed, self.m_JumpHeight, self.m_JumpTimeConfig) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'Jump')
        fSpeed = oOwner.MoveSpeed()
        tJumpTimeConfig = cl_math.Vec3MulF(self.m_JumpTimeConfig, 0.01)
        self.E_SetParams(fNavRadius, fNavHeight, fSpeed, MAX_Acceleration, self.m_JumpSpeed, self.m_JumpHeight, tJumpTimeConfig)

    
    def OnRelife(self, _oOwner, _dInfo):
        self.E_Enable()

    
    def UpdateCtrlFrame(self, *args):
        pass

    
    def PushMove(self, oOwner, vDir, fSpeed, fSecond, _fDownSpeed, _fGravaty, cbFunc = None):
        iClientAni = 1
        return self.CtrlOP(oOwner, STATUS_PUSH, vDir, fSpeed, fSecond, iClientAni, cbFunc)

    
    def C_UpdatePos(self, idx, tPos, iOP):
        obj = self.m_Owner
        obj.m_Pos = tPos
        if iOP & OP_ENDPATH and self.m_ArriveInfo and obj.m_MoveMode != MOVE_TYPE_WINK:
            (_, tTargetPos, _) = self.m_ArriveInfo
            if not cl_math.CheckDistance(tPos, tTargetPos, 5) and obj.m_Agent:
                bAnyHit = obj.m_Game.Scene_RaycastAnyHit(obj.m_Scene, tPos, tTargetPos, PXMASK_MOVEBLK)
                if bAnyHit:
                    CrowdLog.Info('%d %d aiteammate 0x%x %d %s inaccessible %s' % (obj.m_Game.m_ID, obj.m_OwnerPlayerID, obj.m_MoveMode, self.m_CurStatus, OutputPos(tPos), OutputPos(tTargetPos)))
                    self.OverArrive(obj, iFail = 1, iCallBack = 1)
                    oAgent = obj.m_Agent
                    oAgent.ChooseLeaderPos(oAgent)
                    oAgent.FlashToPos(oAgent)
                    return None
        if iOP & OP_JUMPSTART and obj.IsForbid(cl_forbid.FORBID_JUMP):
            self.StopJump()
            return None
        if iOP & OP_NEWPATH and self.m_CurStatus not in (STATUS_PUSH, STATUS_DASH) and obj.m_FaceCtrl and obj.m_FaceCtrl.m_CurStatus in (FACE_STATUS_PATH,):
            (dx, _, dz) = self.E_GetPathDir()
            obj.m_FaceCtrl.OnNextPath(obj, dx, dz)
        movenet.GS2CMapPosCtrl(obj, obj.m_Game.GetFrameNum(), tPos)

    
    def StopJump(self):
        oOwner = self.m_Owner
        self.E_Disable()
        self.E_Enable()
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        self.OverArrive(oOwner, iFail = 1)
        self.ChangeStatus(oOwner, STATUS_STOP)

    
    def HasSameArriveInfo(self, tPos):
        (x, _, z) = tPos
        if self.m_ArriveInfo and x == self.m_ArriveInfo[1][0] and z == self.m_ArriveInfo[1][2]:
            self.m_SameArriveTimes += 1
            return self.m_SameArriveTimes <= SAMEARRIVE_RETRY
        self.m_SameArriveTimes = 0
        return False

    
    def CheckResetArriveInfo(self):
        if self.m_SameArriveTimes <= SAMEARRIVE_RESET:
            return False
        oOwner = self.m_Owner
        tPos = self.m_ArriveInfo[1] if self.m_ArriveInfo else ()
        CrowdLog.Debug('%d %d aiteammate reset %d %s' % (oOwner.m_Game.m_ID, oOwner.m_PlayerID, oOwner.m_MoveMode, OutputPos(tPos)))
        return True

    
    def OverArrive(self, oOwner, iFail, iCallBack = 1):
        self.m_SameArriveTimes = 0
        super().OverArrive(oOwner, iFail, iCallBack)


