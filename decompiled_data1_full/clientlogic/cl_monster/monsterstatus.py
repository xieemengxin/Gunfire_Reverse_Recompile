# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterstatus.pyc
# RelativePath: clientlogic/cl_monster/monsterstatus.pyc
# Source Generated with Decompyle++
# File: monsterstatus.pyc (Python 3.6)

from cl_commondefines import STATUS_DEFAULT, STATUS_PATROL, STATUS_RUN, STATUS_SPRINT, MONSTER_STATUS_DEFAULT, MONSTER_STATUS_ATTACK
from cl_object.status import CStatusMgr, CStatus
from cl_only import CELL_SPACESIZE

class CMoveStatus(CStatus):
    
    def ChangeBaseAttr(self, oOwner, sAttr, iAdd, iMul, iPositive):
        iOldBase = oOwner.m_PrivateAttr[sAttr].m_BaseValue
        if iPositive:
            iNewBase = (iOldBase + iAdd) * (iMul + 10000) * 0.0001
        else:
            iNewBase = (iOldBase - iAdd) * 10000 / (iMul + 10000)
        if sAttr in ('MoveSpeed',):
            iNewBase *= CELL_SPACESIZE
        oOwner.m_PrivateAttr[sAttr].ChangeBase(oOwner, iNewBase)



class CMoveRunStatus(CMoveStatus):
    
    def OnEnter(self, oOwner):
        iRunMul = oOwner.m_RunSpeedUpMul
        if iRunMul:
            self.ChangeBaseAttr(oOwner, 'MoveSpeed', 0, iRunMul, 1)

    
    def OnExit(self, oOwner):
        iRunMul = oOwner.m_RunSpeedUpMul
        if iRunMul:
            self.ChangeBaseAttr(oOwner, 'MoveSpeed', 0, iRunMul, 0)



class CMoveSprintStatus(CMoveStatus):
    
    def OnEnter(self, oOwner):
        iSprintMul = oOwner.m_SprintSpeedUpMul
        if iSprintMul:
            self.ChangeBaseAttr(oOwner, 'MoveSpeed', 0, iSprintMul, 1)

    
    def OnExit(self, oOwner):
        iSprintMul = oOwner.m_SprintSpeedUpMul
        if iSprintMul:
            self.ChangeBaseAttr(oOwner, 'MoveSpeed', 0, iSprintMul, 0)



class CMoveStatusMgr(CStatusMgr):
    m_InitStatus = STATUS_DEFAULT
    m_Status = {
        STATUS_SPRINT: CMoveSprintStatus(),
        STATUS_RUN: CMoveRunStatus(),
        STATUS_PATROL: CMoveStatus(),
        STATUS_DEFAULT: CMoveStatus() }
    
    def OnChangeStatus(self, oOwner):
        oOwner.GS2CPropChange('MoveStatus', self.GetCurStatus())



class CFightStatus(CStatus):
    pass


class CFightStatusMgr(CStatusMgr):
    m_InitStatus = MONSTER_STATUS_DEFAULT
    m_Status = {
        MONSTER_STATUS_ATTACK: CFightStatus(),
        MONSTER_STATUS_DEFAULT: CFightStatus() }
    
    def OnChangeStatus(self, oOwner):
        oOwner.GS2CPropChange('FightStatus', self.GetCurStatus())


