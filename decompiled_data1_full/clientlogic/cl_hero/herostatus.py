# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/herostatus.pyc
# RelativePath: clientlogic/cl_hero/herostatus.pyc
# Source Generated with Decompyle++
# File: herostatus.pyc (Python 3.6)

from cl_object.status import CStatusMgr, CStatus
from cl_commondefines import SNIPE_STATUS_CLOSE, CURWEAPON_SWITCH, DUAL_STATE_END, DUAL_STATE_BEGIN, FORBID_OPENSNIPE, PF_SUBMSG_FILLBULLET, SNIPE_STATUS_OPEN
import cl_forbid
import cl_msgcenter
import cl_cscommondef.cs_itemdef as itemdef

class CShootStatus(CStatus):
    
    def ValidSwitchSnipe(self, oOwner, iStatus):
        if iStatus != SNIPE_STATUS_CLOSE and iStatus != SNIPE_STATUS_OPEN:
            return False
        if iStatus == oOwner.m_ShootStatusMgr.m_SnipeStatus:
            return False
        return True

    
    def SwitchSnipe(self, oOwner, iStatus):
        pass

    
    def OnSwitchSnipe(self, oOwner):
        oCurWeapon = oOwner.m_WieldCon.GetCurWeapon()
        dMsgInfo = {
            'ItemID': oCurWeapon.m_ID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_CMD_SWITCHSNIPE, oOwner, dMsgInfo)

    
    def ValidSwitchWeapon(self, oOwner, iPos):
        return False

    
    def SwitchWeapon(self, oOwner, iPos):
        pass



class CNormalStatus(CShootStatus):
    
    def OnEnter(self, oOwner):
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnFillBullet, 'ShootSTFill', PF_SUBMSG_FILLBULLET, 0)

    
    def OnExit(self, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PERFORM_START, 'ShootSTFill', PF_SUBMSG_FILLBULLET)
        self.TryCloseSnipe(oOwner)

    
    def ValidSwitchSnipe(self, oOwner, iStatus):
        if not super(CNormalStatus, self).ValidSwitchSnipe(oOwner, iStatus):
            return False
        oWeapon = oOwner.m_WieldCon.GetCurWeapon()
        if not oWeapon:
            return False
        oComSnipe = oWeapon.GetComponent('Snipe')
        if not oComSnipe or not oComSnipe.IsSupport():
            return False
        if iStatus == SNIPE_STATUS_OPEN and oOwner.IsForbid(FORBID_OPENSNIPE):
            return False
        return True

    
    def SwitchSnipe(self, oOwner, iStatus):
        oWeapon = oOwner.m_WieldCon.GetCurWeapon()
        oComSnipe = oWeapon.GetComponent('Snipe')
        oMgr = oOwner.m_ShootStatusMgr
        if iStatus == SNIPE_STATUS_OPEN:
            oOwner.Forbid(cl_forbid.SNIPE_RULE, 'Snipe')
            oComSnipe.Snipe()
            oMgr.m_SnipeStatus = SNIPE_STATUS_OPEN
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_CMD_OPENSNIPE, oOwner, { })
        elif iStatus == SNIPE_STATUS_CLOSE:
            oOwner.UnForbid(cl_forbid.SNIPE_RULE, 'Snipe')
            oComSnipe.UnSnipe()
            oMgr.m_SnipeStatus = SNIPE_STATUS_CLOSE
        self.OnSwitchSnipe(oOwner)
        oOwner.SyncSnipeChange()

    
    def TryCloseSnipe(self, oOwner):
        if oOwner.m_ShootStatusMgr.m_SnipeStatus != SNIPE_STATUS_OPEN:
            return None
        if self.ValidSwitchSnipe(oOwner, SNIPE_STATUS_CLOSE):
            self.SwitchSnipe(oOwner, SNIPE_STATUS_CLOSE)

    
    def ValidSwitchWeapon(self, oOwner, iPos):
        if iPos >> 4 & 15:
            return False
        oWieldCon = oOwner.m_WieldCon
        iMainPos = iPos & 15
        if not oWieldCon.IsCanHoldPos(iMainPos):
            return False
        oNewWeapon = oWieldCon.GetItemByPos(iMainPos)
        if not oNewWeapon or oNewWeapon.GetComponent('Hold').IsHold():
            return False
        return True

    
    def SwitchWeapon(self, oOwner, iPos):
        self.TryCloseSnipe(oOwner)
        iMainPos = iPos & 15
        oOwner.m_WieldCon.SetCurWeapon(iMainPos, CURWEAPON_SWITCH)

    
    def OnFillBullet(self, oOwner, dInfo):
        self.TryCloseSnipe(oOwner)



class CDualStatus(CShootStatus):
    
    def ValidSwitchSnipe(self, oOwner, iStatus):
        return False

    
    def ValidSwitchWeapon(self, oOwner, iPos):
        oWieldCon = oOwner.m_WieldCon
        if not oWieldCon.IsWeaponPosHolded(itemdef.ALL_HOLD):
            return False
        iDeuptyPos = iPos >> 4 & 15
        if iDeuptyPos:
            if not oWieldCon.IsCanHoldPos(iDeuptyPos, itemdef.DEPUTY_HOLD):
                return False
            oDeuptyWeapon = oWieldCon.GetItemByPos(iDeuptyPos)
            if not oDeuptyWeapon or oDeuptyWeapon.GetComponent('Hold').IsHold():
                return False
        iMainPos = iPos & 15
        if not oWieldCon.IsCanHoldPos(iMainPos):
            return False
        oMainWeapon = oWieldCon.GetItemByPos(iMainPos)
        if not oMainWeapon or oMainWeapon.GetComponent('Hold').IsHold():
            return False
        return True

    
    def SwitchWeapon(self, oOwner, iPos):
        oWieldCon = oOwner.m_WieldCon
        iMainPos = iPos & 15
        oWieldCon.SetCurWeapon(iMainPos, CURWEAPON_SWITCH)
        iDeuptyPos = iPos >> 4 & 15
        if iDeuptyPos:
            oDeputy = oWieldCon.GetItemByPos(iDeuptyPos)
            oWieldCon.SetDeputyWeapon(oDeputy.m_ID, CURWEAPON_SWITCH)
        else:
            self.HaltSelf(oOwner)

    
    def OnEnter(self, oOwner):
        oWieldCon = oOwner.m_WieldCon
        oDeputy = oWieldCon.GetDeputyPosWeapon()
        oWieldCon.SetDeputyWeapon(oDeputy.m_ID, CURWEAPON_SWITCH)
        oOwner.Set('DualState', 1)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DUALSTATE, oOwner, { }, iSub = DUAL_STATE_BEGIN)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeWeapon, 'DualChangeWeapon', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_REPLACEWEAPON, self.OnReplaceWeapon, 'DualReplaceWeapon', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_ACREMOVEWEAPON, self.OnRemoveWeapon, 'DualRemoveWeapon', -1, 0)

    
    def OnExit(self, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, 'DualChangeWeapon')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_REPLACEWEAPON, 'DualReplaceWeapon')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_ACREMOVEWEAPON, 'DualRemoveWeapon')
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DUALSTATE, oOwner, { }, iSub = DUAL_STATE_END)
        oOwner.m_WieldCon.ClearDeputyWeapon()
        oOwner.Set('DualState', 0)

    
    def HaltSelf(self, oOwner):
        oOwner.HaltDualWieldState()

    
    def OnChangeWeapon(self, oOwner, dInfo):
        oWieldCon = oOwner.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon.m_CanDoubleHold:
            return None
        self.HaltSelf(oOwner)

    
    def OnReplaceWeapon(self, oOwner, dInfo):
        oWieldCon = oOwner.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon.m_CanDoubleHold:
            oDeputy = oWieldCon.GetDeputyPosWeapon()
            if not oDeputy:
                return None
            oWieldCon.SetDeputyWeapon(oDeputy.m_ID, CURWEAPON_SWITCH)
            return None
        self.HaltSelf(oOwner)

    
    def OnRemoveWeapon(self, oOwner, dInfo):
        self.HaltSelf(oOwner)



class CShootStatusMgr(CStatusMgr):
    STATUS_NORMAL = 1
    STATUS_DUAL = 2
    m_Status = {
        STATUS_DUAL: CDualStatus(),
        STATUS_NORMAL: CNormalStatus() }
    m_InitStatus = STATUS_NORMAL
    
    def __init__(self, oOwner):
        super(CShootStatusMgr, self).__init__(oOwner)
        self.m_SnipeStatus = SNIPE_STATUS_CLOSE

    
    def GetSnipeStatus(self):
        return self.m_SnipeStatus

    
    def ValidDualWield(self, oOwner):
        iStatus = self.GetCurStatus()
        if iStatus != self.STATUS_NORMAL:
            return False
        return oOwner.m_WieldCon.ValidOpenDualWield()

    
    def IsDualWield(self, oOwner):
        iStatus = self.GetCurStatus()
        if iStatus == self.STATUS_DUAL:
            return True
        return False

    
    def DualWield(self, oOwner):
        self.ChangeStatus(oOwner, self.STATUS_DUAL)

    
    def CloseDualWield(self, oOwner):
        self.ChangeStatus(oOwner, self.STATUS_NORMAL)

    
    def SwitchSnipe(self, oOwner, iOpen):
        oStatus = self.GetCurStatusObject()
        if not oStatus:
            return 0
        iStatus = SNIPE_STATUS_OPEN if iOpen else SNIPE_STATUS_CLOSE
        if not oStatus.ValidSwitchSnipe(oOwner, iStatus):
            return 0
        oStatus.SwitchSnipe(oOwner, iStatus)
        return 1

    
    def ValidSwitchWeapon(self, oOwner, iPos):
        oStatus = self.GetCurStatusObject()
        if not oStatus:
            return 0
        return oStatus.ValidSwitchWeapon(oOwner, iPos)

    
    def SwitchWeapon(self, oOwner, iPos):
        oStatus = self.GetCurStatusObject()
        if not oStatus:
            return 0
        if not oStatus.ValidSwitchWeapon(oOwner, iPos):
            return 0
        oStatus.SwitchWeapon(oOwner, iPos)
        return 1


