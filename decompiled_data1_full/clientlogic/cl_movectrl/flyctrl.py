# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/flyctrl.pyc
# RelativePath: clientlogic/cl_movectrl/flyctrl.pyc
# Source Generated with Decompyle++
# File: flyctrl.pyc (Python 3.6)

from C_component import ComFlyNavMove
from cl_commondefines import STATUS_STOP, FACE_STATUS_PATH, OP_NEWPATH, OP_ENDPATH, STATUS_MOVE, STATUS_PUSH, PATHMODE_GHOST, MOVE_TYPE_FLY, MOVE_TYPE_NORMAL, STATUS_AIRLINE, STATUS_AIRSTOP
from cl_commondefines import FORBID_MOVE, OP_SHOVE, OP_FAILPATH
from cl_commondefines import PATHMODE_CROWDNORMAL
from cl_only import Second2Frame, Functor, PY_FLAG_DEAD, GAME_FRAME_SECOND
from . import flypathparam
import cl_movectrl.mobject as base
import cl_movectrl.net as movenet
import cl_modeldefine
import cl_math
import cl_forbid
MAX_ACCELERATION = 10000

class CStopStatus(base.CActorStop):
    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CStopStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner):
        oCtrl.E_Stop()
        oCtrl.m_FollowTarget = 0
        oCtrl.OverArrive(oOwner, 0)
        if oCtrl.m_CurStatus == STATUS_STOP:
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return True



class CMoveStatus(base.CActorMove):
    
    def OnEnter(self, oOwner):
        super().OnEnter(oOwner)
        oOwner.m_MoveCtrl.SetPathMode('NormalMove', PATHMODE_CROWDNORMAL)

    
    def Do(self, oCtrl, oOwner, tPos, cbFunc):
        idx = oCtrl.GetCallBackIdx()
        if oCtrl.E_MovePos(idx, tPos):
            oCtrl.m_ArriveInfo = (idx, tPos, cbFunc)
            return 1
        return 0

    
    def OnExit(self, oOwner):
        super().OnExit(oOwner)
        oOwner.m_MoveCtrl.ClearPathMode('NormalMove')



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
            oOwner.m_MoveCtrl.ClearPathMode('AirLineMove')
            oCtrl.OverArrive(oOwner, 0)



class CAirStopStatus(base.CActorStop):
    
    def OnEnter(self, oOwner):
        super(CAirStopStatus, self).OnEnter(oOwner)

    
    def OnCheck(self, oOwner, *lstArgs):
        if not super(CAirStopStatus, self).OnCheck(oOwner, *lstArgs):
            return 0
        return 1

    
    def Do(self, oCtrl, oOwner):
        oCtrl.OverArrive(oOwner, 0)
        if oCtrl.m_CurStatus == STATUS_AIRSTOP:
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return True



class CFlyCtrlMgr(base.CActorCtrlMgr, ComFlyNavMove):
    m_Status = {
        STATUS_AIRSTOP: CAirStopStatus(),
        STATUS_AIRLINE: CAirLineStatus(),
        STATUS_STOP: CStopStatus(),
        STATUS_MOVE: CMoveStatus() }
    m_InitStatus = STATUS_STOP
    
    def __init__(self, oOwner):
        base.CActorCtrlMgr.__init__(self, oOwner)
        ComFlyNavMove.__init__(self, oOwner.m_Game.m_ID, oOwner.m_ID, 'FlyNavMove')
        self.m_Owner = oOwner
        self.m_ArriveInfo = ()
        self.m_CallBackIdx = 0
        self.m_MoveFrame = 0
        self.m_FollowTarget = 0
        self.m_PathMode = 0
        self.m_PathModeList = []
        self.m_FollowDeflexion = { }
        self.InitParams(oOwner)

    
    def InitParams(self, oOwner):
        (fNavRadius, fNavHeight) = cl_modeldefine.GetModelDefine(oOwner.m_Shape, 'NavMesh')
        self.m_NavRadius = fNavRadius
        fSpeed = oOwner.MoveSpeed()
        self.E_SetParams(fNavRadius, fNavHeight, fSpeed, MAX_ACCELERATION)

    
    def Release(self, oOwner):
        super().Release(oOwner)
        self.m_Owner = None

    
    def SeekPath(self, oOwner, tPos, func = None):
        return self.CtrlOP(oOwner, STATUS_MOVE, tPos, func)

    
    def AirMove(self, oOwner, vEnd, fSpeed, bUseFlyMode, func = None):
        return self.CtrlOP(oOwner, STATUS_AIRLINE, vEnd, fSpeed, bUseFlyMode, func)

    
    def AirStop(self, oOwner):
        return self.CtrlOP(oOwner, STATUS_AIRSTOP)

    
    def FollowMove(self, oOwner, iTarget, fStopDis, fHeight, func = None, idx = 0, iAppointFrame = 0, iPyFlag = PY_FLAG_DEAD):
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
        vTarget = oTarget.GetPos()
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
        vTarget = (vTarget[0], vTarget[1] + fHeight, vTarget[2])
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
            oOwner.Call_Out(Functor(self.FollowMove, oOwner, iTarget, fStopDis, fHeight, func, idx, iAppointFrame, iPyFlag), iRefreshFrame, 'FollowMove')
        if not iRet:
            self.E_Stop()
            self.m_FollowTarget = 0
            self.OverArrive(oOwner, iFail = 1)
            movenet.GS2CStop(oOwner, oOwner.GetPos())
        return iRet == 1

    
    def PushMove(self, oOwner, tDir, fSpeed, fSecond, iClientAni = 1, iFace2Dir = 0, func = None):
        return self.CtrlOP(oOwner, STATUS_PUSH, tDir, fSpeed, fSecond, iClientAni, func)

    
    def GetPathDir(self):
        (x, y, z) = self.E_GetPathDir()
        return (x, z)

    
    def Stop(self, oOwner):
        return self.CtrlOP(oOwner, STATUS_STOP)

    
    def IsStop(self, oOwner):
        return self.E_IsStop()

    
    def HasSameArriveInfo(self, tPos):
        (x, _, z) = tPos
        if self.m_ArriveInfo and x == self.m_ArriveInfo[1][0] and z == self.m_ArriveInfo[1][2]:
            return True
        return False

    
    def HasSameArriveTarget(self, iTarget):
        if self.m_ArriveInfo:
            pass
        return self.m_FollowTarget == iTarget

    
    def SetSpeed(self, oOwner, fSpeed):
        self.E_SetSpeed(fSpeed)
        movenet.GS2CFlyTrack(oOwner, self.E_GetPathData())

    
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
        dParam = flypathparam.GetCrowdPathModeParam(iFirstMode)
        self.E_SetPathMode(dParam)

    
    def C_UpdatePos(self, idx, tPos, iOP):
        obj = self.m_Owner
        obj.m_Pos = tPos
        if iOP == OP_SHOVE:
            movenet.GS2CMapCrowdPos(obj, tPos)
        elif iOP & (OP_FAILPATH | OP_ENDPATH):
            self.Stop(obj)
            iFail = 1 if iOP & OP_FAILPATH else 0
            self.OverArrive(obj, iFail)
        elif iOP & OP_NEWPATH:
            if obj.m_FaceCtrl and obj.m_FaceCtrl.m_CurStatus in (FACE_STATUS_PATH,):
                (dx, _, dz) = self.E_GetPathDir()
                obj.m_FaceCtrl.OnNextPath(obj, dx, dz)
            lstPath = self.E_GetPathData()
            self.m_CurPath = lstPath
            movenet.GS2CFlyTrack(obj, lstPath)
        else:
            self.m_MoveFrame += 1
            movenet.GS2CFlyPos(obj, self.m_MoveFrame, tPos)

    
    def PushMove(self, oOwner, tDir, fSpeed, fSecond, iClientAni = 1, iFace2Dir = 0, func = None):
        pass


