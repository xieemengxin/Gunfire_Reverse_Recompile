# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/status.pyc
# RelativePath: clientlogic/cl_object/status.pyc
# Source Generated with Decompyle++
# File: status.pyc (Python 3.6)


class CStatusMgr(object):
    m_Status = { }
    m_InitStatus = 0
    
    def __init__(self, oOwner):
        self.m_CurStatus = 0
        self.Init(oOwner)

    
    def Init(self, oOwner):
        self.m_CurStatus = self.m_InitStatus
        oStatus = self.m_Status[self.m_CurStatus]
        oStatus.OnEnter(oOwner)

    
    def ChangeStatus(self, oOwner, iStatus):
        if iStatus not in self.m_Status:
            return None
        if iStatus == self.m_CurStatus:
            return None
        oOldStatu = self.m_Status[self.m_CurStatus]
        oNewStatu = self.m_Status[iStatus]
        oOldStatu.OnExit(oOwner)
        self.m_CurStatus = iStatus
        oNewStatu.OnEnter(oOwner)
        self.OnChangeStatus(oOwner)

    
    def OnChangeStatus(self, oOwner):
        pass

    
    def GetCurStatus(self):
        return self.m_CurStatus

    
    def GetCurStatusObject(self):
        if not self.m_CurStatus:
            return None
        return self.m_Status[self.m_CurStatus]

    
    def GetStatus(self, iStatus):
        if iStatus in self.m_Status:
            return self.m_Status[iStatus]



class CStatus(object):
    
    def OnEnter(self, oOwner):
        pass

    
    def OnExit(self, oOwner):
        pass


