# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/mobject.pyc
# RelativePath: clientlogic/cl_movectrl/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import STATUS_STOP, STATUS_MOVE, STATUS_JUMP, STATUS_WINK, STATUS_PUSH, PATHMODE_CROWDNORMAL
from cl_object.status import CStatusMgr, CStatus
import cl_msgcenter
import cl_forbid

class CActorBaseStatus(CStatus):
    m_ForbidKey = 'ActorCtrl'
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_CmdMsg = 0
    
    def OnEnter(self, oOwner):
        if self.m_ForbidRule:
            oOwner.Forbid(self.m_ForbidRule, self.m_ForbidKey)
        if self.m_CmdMsg:
            cl_msgcenter.SendMsg(self.m_CmdMsg, oOwner, {
                'Target': oOwner.m_ID })

    
    def OnExit(self, oOwner):
        if self.m_ForbidRule:
            oOwner.UnForbid(self.m_ForbidRule, self.m_ForbidKey)

    
    def Check(self, oOwner, *lstArgs):
        if oOwner.IsForbid(self.m_CheckForbid):
            return 0
        return self.OnCheck(oOwner, *lstArgs)

    
    def OnCheck(self, oOwner, *lstArgs):
        return 1

    
    def Do(self, oOwner, *lstArgs):
        raise Exception('Abc')



class CActorStop(CActorBaseStatus):
    pass


class CActorMove(CActorBaseStatus):
    m_CheckForbid = cl_forbid.FORBID_MOVE
    m_CmdMsg = cl_msgcenter.MSG_CMD_MOVE


class CActorJump(CActorBaseStatus):
    m_ForbidRule = cl_forbid.JUMP_RULE
    m_CheckForbid = cl_forbid.FORBID_JUMP
    m_CmdMsg = cl_msgcenter.MSG_CMD_JUMP


class CActorWinkMove(CActorBaseStatus):
    pass


class CActorCtrlMgr(CStatusMgr):
    m_Status = { }
    m_InitStatus = STATUS_STOP
    m_DefPathMode = PATHMODE_CROWDNORMAL
    
    def IsClientCtrl(self):
        return False

    
    def Release(self, oOwner):
        pass

    
    def Reset(self, oOwner):
        self.ChangeStatus(oOwner, self.m_InitStatus)

    
    def CtrlOP(self, oOwner, iStatus, *args):
        oStatus = self.GetStatus(iStatus)
        if oStatus.Check(oOwner, *args):
            self.ChangeStatus(oOwner, iStatus)
            return oStatus.Do(self, oOwner, *args)
        return 0

    
    def SetSpeed(self, oOwner, fSpeed):
        pass

    
    def IsStop(self, oOwner):
        return self.m_CurStatus == STATUS_STOP

    
    def OnWalkTo(self, oOwner, tPos):
        pass

    
    def Stop(self, oOwner):
        pass

    
    def SeekPath(self, oOwner, *args):
        pass

    
    def DashMove(self, oOwner, *args):
        pass

    
    def PushMove(self, oOwner, *args):
        pass

    
    def FollowMove(self, oOwner, *args):
        pass


