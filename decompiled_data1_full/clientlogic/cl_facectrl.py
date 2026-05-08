# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_facectrl.pyc
# RelativePath: clientlogic/cl_facectrl.pyc
# Source Generated with Decompyle++
# File: cl_facectrl.pyc (Python 3.6)

from cl_only import Functor, WeakProxy, Time2Frame, Frame2Time, PerSecond2PerFrame
from cl_object.status import CStatusMgr, CStatus
from cl_commondefines import FACE_STATUS_TARGET, FACE_STATUS_PATH, FACE_STATUS_DIR, FACE_STATUS_POS, FACE_STATUS_CROSSPATH
import cl_math
import cl_snetwar
TURN_STEP = 2
TURN_TIME = Frame2Time(TURN_STEP)

class CFaceMovePath(CStatus):
    
    def ChangeFace(self, oCtrl, oOwner, mx, mz):
        oCtrl.TurnChangeFace(oOwner, (mx, 0, mz), oCtrl.m_TurnSpeed)



class CFaceCrossMovePath(CStatus):
    m_Clockwise = 0
    
    def OnEnter(self, oOwner):
        self.m_Clockwise = 0

    
    def DecideClockWise(self, oOwner, mx, mz):
        vMoveDir = (mx, 0, mz)
        oTarget = oOwner.m_Agent.GetLockEnemy()
        if oTarget:
            vOwner = oOwner.GetPos()
            vTarget = oTarget.GetPos()
            vCompareDir = cl_math.Vec3Minus(vTarget, vOwner)
        else:
            vCompareDir = oOwner.m_FaceCtrl.GetFacing(oOwner)
        if cl_math.VectorCross2D(vMoveDir, vCompareDir) < 0:
            self.m_Clockwise = 1
        else:
            self.m_Clockwise = -1

    
    def ChangeFace(self, oCtrl, oOwner, mx, mz):
        if not mx and not mz:
            return None
        if not self.m_Clockwise:
            self.DecideClockWise(oOwner, mx, mz)
        vPath = (mx, 0, mz)
        (x, _, z) = cl_math.RotateAroundVector(vPath, (0, 1, 0), 90 * self.m_Clockwise)
        oCtrl.TurnChangeFace(oOwner, (x, 0, z), oCtrl.m_TurnSpeed)



class CFacePos(CStatus):
    
    def ChangeFace(self, oCtrl, oOwner, tPos, fSpeed):
        (tx, ty, tz) = tPos
        (ox, oy, oz) = oOwner.GetPos()
        mx = tx - ox
        mz = tz - oz
        fTurnSpeed = fSpeed if fSpeed >= 0 else oCtrl.m_TurnSpeed
        oCtrl.TurnChangeFace(oOwner, (mx, 0, mz), fTurnSpeed)



class CFaceDir(CStatus):
    
    def ChangeFace(self, oCtrl, oOwner, vDir, fSpeed = 0, iTurnTime = 0):
        if not iTurnTime and not fSpeed:
            fTurnSpeed = oCtrl.m_TurnSpeed
        else:
            fTurnSpeed = fSpeed
        oCtrl.TurnChangeFace(oOwner, vDir, fTurnSpeed, iTurnTime)



class CFaceTarget(CStatus):
    m_RecoverLimitSpeed = PerSecond2PerFrame(180)
    
    def ChangeFace(self, oCtrl, oOwner, iVictim, iTurnTime, iKeep):
        if iVictim == oCtrl.m_FaceVictim and iKeep:
            return None
        oCtrl.ClearTurn()
        self.UpdateFace(oOwner, iVictim)
        if iKeep:
            oCtrl.m_FaceVictim = iVictim
            cl_snetwar.GS2CFaceTarget(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, iVictim, iTurnTime)
            oOwner.AddExtPacket('FaceTarget', FaceTargetReEnterPacket)
        else:
            oCtrl.m_FaceVictim = 0
            cl_snetwar.GS2CFace(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, oOwner.GetNetFacing(), iTurnTime)

    
    def UpdateFace(self, oOwner, iVictim):
        oVictim = oOwner.m_Game.GetObject(iVictim)
        if oVictim:
            (ox, _, oz) = oOwner.GetPos()
            (tx, _, tz) = oVictim.GetPos()
            mx = tx - ox
            my = 0
            mz = tz - oz
            oOwner.m_Game.SetFacing(oOwner.m_ID, (mx, my, mz))
        return oOwner.m_Game.GetFacing(oOwner.m_ID)

    
    def Recover(self, oCtrl, oOwner):
        iVictim = oCtrl.m_FaceVictim
        if not iVictim:
            return None
        iSpeed = oCtrl.m_TurnSpeed
        vStart = oOwner.m_Game.GetFacing(oOwner.m_ID)
        vTarget = self.UpdateFace(oOwner, iVictim)
        iAngle = cl_math.CalAngle2D(vStart, vTarget) if vStart != vTarget else 0
        iTurnFrame = iAngle // iSpeed
        cl_snetwar.GS2CFaceTarget(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, iVictim, Frame2Time(iTurnFrame))
        if iTurnFrame and oOwner.m_Agent and iSpeed <= self.m_RecoverLimitSpeed:
            if vStart[0] * vTarget[2] - vStart[2] * vTarget[0] > 0:
                iAngle = -iAngle
            iStartFrame = oOwner.m_Game.GetFrameNum()
            self.m_Turn = [
                vTarget,
                iAngle,
                iStartFrame,
                iTurnFrame]
            oOwner.m_Agent.PauseAgent('FaceRecover')
            oOwner.Call_Out(Functor(self.KeepRecovering, oOwner, iVictim), 1, 'FaceRecover')

    
    def KeepRecovering(self, oOwner, iVictim):
        oOwner.Remove_Call_Out('FaceRecover')
        iCurFrame = oOwner.m_Game.GetFrameNum()
        (vRecoverTarget, iAngle, iStartFrame, iTurnFrame) = self.m_Turn
        bFinished = False
        if iCurFrame >= iStartFrame + iTurnFrame:
            bFinished = True
        else:
            oVictim = oOwner.m_Game.GetObject(iVictim)
            if oVictim:
                vTarget = self.UpdateFace(oOwner, iVictim)
                iTurnedAngle = iAngle * (iCurFrame - iStartFrame) // iTurnFrame
                iDifAngle = cl_math.CalAngle2D(vRecoverTarget, vTarget)
                iDifAngle = iDifAngle if vRecoverTarget[0] * vTarget[2] - vRecoverTarget[2] * vTarget[0] > 0 else -iDifAngle
                if abs(iDifAngle + iTurnedAngle) >= abs(iAngle):
                    bFinished = True
                else:
                    bFinished = True
        if None:
            self.FinishRecover(oOwner)
            return None
        oOwner.Call_Out(Functor(self.KeepRecovering, oOwner, iVictim), 1, 'FaceRecover')

    
    def FinishRecover(self, oOwner):
        oAgent = oOwner.m_Agent
        if oAgent:
            oAgent.ResumeAgent('FaceRecover')
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)
            oOwner.Remove_Call_Out('FaceRecover')

    
    def OnExit(self, oOwner):
        self.FinishRecover(oOwner)
        oOwner.RemoveExtPacket('FaceTarget')
        oOwner.m_FaceCtrl.m_FaceVictim = 0



def FaceTargetReEnterPacket(oOwner, dPlayer):
    if not (oOwner.m_FaceCtrl) or not (oOwner.m_FaceCtrl.m_FaceVictim):
        return None
    cl_snetwar.GS2CFaceTarget(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, oOwner.m_FaceCtrl.m_FaceVictim, 0, dPlayer)


class CFaceStatusMgr(CStatusMgr):
    m_InitStatus = FACE_STATUS_PATH
    m_Status = {
        FACE_STATUS_POS: CFacePos(),
        FACE_STATUS_DIR: CFaceDir(),
        FACE_STATUS_TARGET: CFaceTarget(),
        FACE_STATUS_CROSSPATH: CFaceCrossMovePath(),
        FACE_STATUS_PATH: CFaceMovePath() }
    
    def __init__(self, oOwner):
        super(CFaceStatusMgr, self).__init__(oOwner)
        self.m_OwnerObj = WeakProxy(oOwner)
        self.RefreshTurnSpeed()
        self.m_Lock = []
        self.m_Turn = []
        self.m_TurnCache = { }
        self.m_FaceVictim = 0
        self.m_CurReason = ''

    
    def RefreshTurnSpeed(self, iTurnSpeed = None):
        if iTurnSpeed is None:
            iTurnSpeed = self.m_OwnerObj.TurnSpeed()
        if iTurnSpeed < 1:
            iTurnSpeed = 1
        self.m_TurnSpeed = iTurnSpeed

    
    def TurnChangeFace(self, oOwner, vTarget, fTurnSpeed = 0, iTurnTime = 0):
        if self.m_Lock:
            return None
        if cl_math.IsPlaneZero(vTarget):
            return None
        vStart = self.GetFacing(oOwner)
        iAngle = cl_math.CalAngle2D(vStart, vTarget)
        if not iAngle:
            return None
        if fTurnSpeed:
            iTurnFrame = int(iAngle // fTurnSpeed)
        else:
            iTurnFrame = Time2Frame(iTurnTime)
        if vStart[0] * vTarget[2] - vStart[2] * vTarget[0] > 0:
            iAngle = -iAngle
        if iTurnFrame:
            iStartFrame = oOwner.m_Game.GetFrameNum()
            self.m_Turn = [
                vStart,
                iAngle,
                iStartFrame,
                iTurnFrame]
        oOwner.m_Game.SetFacing(oOwner.m_ID, (vTarget[0], 0, vTarget[2]))
        vFace = oOwner.GetNetFacing()
        cl_snetwar.GS2CFace(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, vFace, Frame2Time(iTurnFrame))

    
    def GetFacing(self, oOwner):
        oGame = oOwner.m_Game
        iCurFrame = oGame.GetFrameNum()
        if self.m_Lock:
            return oGame.GetFacing(oOwner.m_ID)
        if self.UpdateTurn(iCurFrame):
            return self.m_TurnCache[iCurFrame]
        if self.m_CurStatus == FACE_STATUS_TARGET:
            oStatus = self.GetStatus(FACE_STATUS_TARGET)
            return oStatus.UpdateFace(oOwner, self.m_FaceVictim)
        return oGame.GetFacing(oOwner.m_ID)

    
    def UpdateTurn(self, iCurFrame):
        if not self.m_Turn:
            return False
        (vStart, iAngle, iStartFrame, iTurnFrame) = self.m_Turn
        if iCurFrame == iStartFrame:
            self.m_TurnCache[iCurFrame] = vStart
            return True
        if iStartFrame + iTurnFrame < iCurFrame:
            self.m_Turn = []
            self.m_TurnCache = { }
            return False
        if iCurFrame not in self.m_TurnCache:
            vCurFace = cl_math.RotateAroundVector(vStart, (0, 1, 0), iAngle * (iCurFrame - iStartFrame) // iTurnFrame)
            self.m_TurnCache[iCurFrame] = vCurFace
        return True

    
    def ClearTurn(self):
        self.m_Turn = []
        self.m_TurnCache = { }

    
    def FaceForce(self, oOwner, vTarget):
        self.ClearTurn()
        oOwner.m_Game.SetFacing(oOwner.m_ID, (vTarget[0], 0, vTarget[2]))
        vFace = oOwner.GetNetFacing()
        cl_snetwar.GS2CFace(oOwner.m_Game, oOwner.m_Scene, oOwner.m_ID, vFace, 0)

    
    def _CtrlOP(self, oOwner, iStatus, sReason, *lstArgs):
        if self.m_Lock:
            return None
        self.m_CurReason = sReason
        self.ChangeStatus(oOwner, iStatus)
        oStatus = self.GetStatus(iStatus)
        oStatus.ChangeFace(self, oOwner, *lstArgs)

    
    def FaceTarget(self, oOwner, iTarget, sReason, iTurnTime, iKeep):
        self._CtrlOP(oOwner, FACE_STATUS_TARGET, sReason, iTarget, iTurnTime, iKeep)

    
    def FacePath(self, oOwner, sReason):
        (mx, mz) = oOwner.GetPathDir()
        self._CtrlOP(oOwner, FACE_STATUS_PATH, sReason, mx, mz)

    
    def FaceCrossPath(self, oOwner, sReason):
        (mx, mz) = oOwner.GetPathDir()
        self._CtrlOP(oOwner, FACE_STATUS_CROSSPATH, sReason, mx, mz)

    
    def FacePos(self, oOwner, tPos, sReason, fSpeed = -1):
        self._CtrlOP(oOwner, FACE_STATUS_POS, sReason, tPos, fSpeed)

    
    def FaceDir(self, oOwner, tDir, sReason, fSpeed = 0, iTurnTime = 0):
        self._CtrlOP(oOwner, FACE_STATUS_DIR, sReason, tDir, fSpeed, iTurnTime)

    
    def FaceStop(self, oOwner, sReason):
        if self.m_CurReason != sReason:
            return None
        vCurFace = self.GetFacing(oOwner)
        self.FaceForce(oOwner, vCurFace)

    
    def LockFace(self, oOwner, vDir, sReason, bForece = True):
        self.m_Lock.append((vDir, sReason))
        if len(self.m_Lock) == 1 and bForece:
            self.FaceForce(oOwner, vDir)

    
    def UnLockFace(self, oOwner, sReason, bKeep = False):
        lstLock = []
        for _dir, _reason in self.m_Lock:
            if _reason == sReason:
                continue
            lstLock.append((_dir, _reason))
        
        self.m_Lock = lstLock
        if bKeep:
            return None
        if self.m_Lock:
            (vDir, _) = self.m_Lock[0]
            self.FaceForce(oOwner, vDir)
        elif self.m_CurStatus == FACE_STATUS_TARGET:
            oStatus = self.GetStatus(FACE_STATUS_TARGET)
            oStatus.Recover(self, oOwner)

    
    def OnNextPath(self, oOwner, dx, dz):
        if self.m_CurStatus not in (FACE_STATUS_PATH, FACE_STATUS_CROSSPATH):
            return None
        oNowStatus = self.GetStatus(self.m_CurStatus)
        oNowStatus.ChangeFace(self, oOwner, dx, dz)

    
    def IsRotating(self):
        self.UpdateTurn(self.m_OwnerObj.m_Game.GetFrameNum())
        if self.m_Turn:
            return True
        return False

    
    def Release(self):
        self.m_OwnerObj = None


