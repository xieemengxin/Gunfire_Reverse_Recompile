# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/combullet.pyc
# RelativePath: clientlogic/cl_item/component/combullet.pyc
# Source Generated with Decompyle++
# File: combullet.pyc (Python 3.6)

from cl_only import GAME_FRAME, Functor, Time2Frame
from cl_commondefines import BASEATTR_REFRESH, DEBUG_STATUS_NOCOSTBULLET, PF_SUBMSG_SWITCHWEAPON, BASEATTR_CLIENT, PF_SUBMSG_FILLBULLET, FORBID_AUTO_FILLBULLET, AUTOFILL_RULE_NONE, AUTOFILL_RULE_EMPTYCLIP, AUTOFILL_RULE_REPEATEND
from .mobject import CItemComponent
from cl_object.status import CStatusMgr, CStatus
import math
import cl_item.defines as itemdef
import cl_object.baseattr
import cl_war
import cl_formula
import cl_msgcenter

class CBulletComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CBulletComponent, self).__init__(oItem, dParser)
        self.m_BulletType = dParser['BulletType']
        self.m_ChamberPerform = dParser['Chamber']
        self.m_FillPerform = dParser['Fill']
        self.m_FillPerformID = 0
        self.m_DualFillPerform = dParser['DualFill']
        self.m_CurBullet = 0
        for sAttr in ('MaxBullet', 'FillTime', 'BulletVerticalAcc', 'FillBulletCnt'):
            iValue = cl_formula.GetFormulaResultByLV(oItem, dParser[sAttr], self.m_Item.m_Grade)
            self.m_Item.m_PrivateAttr[sAttr] = cl_object.baseattr.NewAttr(oItem, sAttr, iValue, BASEATTR_REFRESH | BASEATTR_CLIENT)
        
        if dParser['DelayAutoFillFrame'] > 0:
            self.m_DelayAutoFillFrame = dParser['DelayAutoFillFrame']
            oFillBulletStatusMgr = GetFillBulletStatusMgr(dParser.get('AutoFillSpecialType', AUTOFILL_RULE_NONE))
            self.m_FillBulletStatusMgr = oFillBulletStatusMgr(self.m_Item)
        else:
            self.m_FillBulletStatusMgr = None
        self.m_Item.AddAttention(itemdef.MSG_ITEM_ADD, self.OnAddInit, 'BulletCom')

    
    def Release(self):
        oItem = self.m_Item
        if self.m_FillBulletStatusMgr and oItem:
            oOwner = oItem.GetOwner()
            self.m_FillBulletStatusMgr.Exit(oItem, oOwner)
        super(CBulletComponent, self).Release()

    
    def Save(self):
        dData = {
            'BT': self.m_CurBullet }
        return dData

    
    def Load(self, dData):
        if 'BT' in dData:
            self.m_CurBullet = dData['BT']

    
    def OnAddInit(self, oItem, oOwner):
        oComPerform = oItem.GetComponent('Perform')
        if not oComPerform:
            return None
        if self.m_FillPerform:
            oPerform = oComPerform.AddPerform(self.m_FillPerform, 1)
            if oPerform:
                self.m_FillPerformID = oPerform.m_ID
                self.m_Item.GS2CItemPropChange('FillPerformID', self.m_FillPerformID)
        if self.m_DualFillPerform:
            oComPerform.AddPerform(self.m_DualFillPerform, 1)
        self.MaxBulletChange()

    
    def BulletType(self):
        return self.m_BulletType

    
    def Bullet(self):
        return self.m_CurBullet

    
    def BulletState(self):
        if not self.m_FillBulletStatusMgr:
            return 0
        return self.m_FillBulletStatusMgr.m_CurStatus

    
    def MaxBullet(self):
        return self.QueryAttr('MaxBullet')

    
    def BulletModify(self, iCnt, iSync = 1, iSendMsg = 1, sReason = '', iActNum = 0):
        iCnt = math.ceil(iCnt) if iCnt > 0 else math.floor(iCnt)
        if iCnt == 0:
            return iCnt
        iMaxBullet = self.QueryAttr('MaxBullet')
        iNewBullet = self.m_CurBullet + iCnt
        if iNewBullet < 0:
            iCnt = iCnt - iNewBullet
            self.m_CurBullet = 0
        elif iNewBullet > iMaxBullet:
            iCnt = iMaxBullet - self.m_CurBullet
            self.m_CurBullet = iMaxBullet
        else:
            self.m_CurBullet = iNewBullet
        if iSync:
            self.m_Item.GS2CItemPropChange('CurBullet', self.m_CurBullet)
        self.m_Item.SendMsg(itemdef.MSG_ITEM_BULLETMODIFY)
        oOwner = self.m_Item.GetOwner()
        if oOwner and iSendMsg:
            if iCnt < 0:
                iMsgCost = -iCnt
                iMsg = cl_msgcenter.MSG_WAR_COMCOSTBULLET
            else:
                iMsgCost = iCnt
                iMsg = cl_msgcenter.MSG_WAR_COMADDBULLET
            cl_msgcenter.SendMsg(iMsg, oOwner, {
                'Cost': iMsgCost,
                'MaxBullet': iMaxBullet,
                'ItemID': self.m_Item.m_ID,
                'AID': oOwner.m_ID,
                'SID': self.m_BulletType,
                'Reason': sReason,
                'ActNum': iActNum,
                'NewBullet': iNewBullet })
        return iCnt

    
    def MaxBulletChange(self):
        oItem = self.m_Item
        oOwner = oItem.GetOwner()
        iMaxBullet = self.QueryAttr('MaxBullet')
        if self.m_CurBullet > iMaxBullet:
            iCnt = iMaxBullet - self.m_CurBullet
            iCnt = -self.BulletModify(iCnt, iSendMsg = 0)
            if oOwner:
                self.GiveBack(oItem, oOwner, iCnt)
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MAXBULLETCHANGE, oOwner, {
                'Item': oItem.m_ID,
                'MaxBullet': iMaxBullet })

    
    def AttrCache(self):
        return {
            'CurBullet': self.m_CurBullet }

    
    def GiveBack(self, oItem, oOwner, iCnt = 0):
        if not iCnt:
            iCnt = self.m_CurBullet
            self.m_CurBullet = 0
        iBulletSID = self.m_BulletType
        if iCnt:
            oOwner.m_BulletCon.BulletModify(iBulletSID, iCnt, '归还子弹')

    
    def ChamberFrame(self):
        return GAME_FRAME * 100 // self.m_Item.QueryAttr('AttSpeed')

    
    def ListenFill(self, oItem, oOwner):
        self.FillBullet()
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_ATTACK_END, Functor(AutoFillBullet, self.m_Item.m_ID), 'AutoFill', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PERFORM_END, Functor(AutoFillBullet, self.m_Item.m_ID), 'AutoFill', PF_SUBMSG_SWITCHWEAPON, 0)

    
    def DoneListenFill(self, oItem, oOwner):
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_ATTACK_END, 'AutoFill', -1)
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PERFORM_END, 'AutoFill', PF_SUBMSG_SWITCHWEAPON)

    
    def GetFillPerform(self):
        return self.m_FillPerform

    
    def GetFillPerformID(self):
        return self.m_FillPerformID

    
    def FillBullet(self):
        if self.m_CurBullet:
            return 0
        oOwner = self.m_Item.GetOwner()
        if oOwner.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET == DEBUG_STATUS_NOCOSTBULLET:
            self.BulletModify(self.QueryAttr('MaxBullet'))
            return 1
        oPerformCom = self.m_Item.GetComponent('Perform')
        if not oPerformCom:
            return 0
        iFillPerform = self.m_FillPerform
        if oOwner.Query('DualState'):
            iFillPerform = self.m_DualFillPerform
        pfobj = oPerformCom.GetPerform(iFillPerform)
        if not pfobj:
            return 0
        return cl_war.UsePerform(oOwner, pfobj, {
            'Weapon': self.m_Item.m_ID })

    
    def Chamber(self):
        if not self.m_ChamberPerform:
            return 0
        oOwner = self.m_Item.GetOwner()
        oPerformCom = self.m_Item.GetComponent('Perform')
        if not oPerformCom:
            return 0
        pfobj = oPerformCom.GetPerform(self.m_ChamberPerform)
        if not pfobj:
            pfobj = oPerformCom.AddPerform(self.m_ChamberPerform, 1)
        return cl_war.UsePerform(oOwner, pfobj, {
            'Weapon': self.m_Item.m_ID })

    
    def RefreshCurBullet(self):
        self.m_Item.GS2CItemPropChange('CurBullet', self.m_CurBullet)



def AutoFillBullet(iItemID, oOwner, dMsgInfo):
    oItem = oOwner.m_WieldCon.GetItemByID(iItemID)
    if not oItem:
        return None
    oBulletCom = oItem.GetComponent('Bullet')
    if not oBulletCom.FillBullet():
        oBulletCom.Chamber()


class CFillBulletStatus(CStatus):
    
    def GetAutoFillBulletTime(self, oItem):
        oBulletCom = oItem.GetComponent('Bullet')
        iFillTime = oBulletCom.QueryAttr('FillTime')
        iMaxBullet = oBulletCom.MaxBullet()
        iAutoFillFrame = int(Time2Frame(iFillTime / iMaxBullet))
        return max(1, iAutoFillFrame)

    
    def GetDelayAutoFill(self, oItem):
        return oItem.GetComponent('Bullet').m_DelayAutoFillFrame

    
    def GetFillBulletCnt(self, oItem, iNeedFillBullet):
        iFillBulletCnt = oItem.QueryAttr('FillBulletCnt')
        if iFillBulletCnt <= 0:
            return 1
        if iFillBulletCnt <= iNeedFillBullet:
            return iFillBulletCnt
        return iNeedFillBullet

    
    def Refresh(self, oItem):
        self.OnExit(oItem)
        self.OnEnter(oItem)



class CNormalFillBulletStatus(CFillBulletStatus):
    
    def OnEnter(self, oItem):
        self.AutoFillBulletHeartBeat(oItem.GetOwner(), oItem.m_ID)

    
    def OnExit(self, oItem):
        oHero = oItem.GetOwner()
        if oHero:
            oHero.Remove_Call_Out('AutoFillBulletHeartBeat%s' % oItem.m_ID)

    
    def RepeatHeartBeat(self, oItem):
        oHero = oItem.GetOwner()
        pFunc = Functor(self.AutoFillBulletHeartBeat, oHero, oItem.m_ID)
        oHero.Call_Out(pFunc, self.GetAutoFillBulletTime(oItem), 'AutoFillBulletHeartBeat%s' % oItem.m_ID)

    
    def AutoFillBulletHeartBeat(self, oHero, iItemID):
        oItem = oHero.m_WieldCon.GetItemByID(iItemID)
        bIsInitWeapon = oItem.IsInitWeapon()
        oBulletCom = oItem.GetComponent('Bullet')
        if not oBulletCom:
            return None
        iMaxBullet = oBulletCom.MaxBullet()
        iNowBullet = oBulletCom.Bullet()
        if iNowBullet >= iMaxBullet:
            return None
        iBulletSID = oBulletCom.BulletType()
        iBagBullet = oHero.m_BulletCon.Bullet(iBulletSID)
        if not iBagBullet and not bIsInitWeapon:
            self.RepeatHeartBeat(oItem)
            return None
        iNeedBullet = iMaxBullet - iNowBullet
        iFillBulletCnt = self.GetFillBulletCnt(oItem, iNeedBullet)
        if iFillBulletCnt > iBagBullet:
            iFillBulletCnt = iBagBullet
        if not bIsInitWeapon:
            oHero.m_BulletCon.BulletModify(iBulletSID, -iFillBulletCnt, 'fillbullet')
        iHoldPos = oItem.GetComponent('Hold').HoldPos()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AUTOFILLBULLET, oHero, {
            'OldBullet': iNowBullet,
            'AID': oHero.m_ID,
            'ItemID': oItem.m_ID,
            'HoldType': iHoldPos })
        oBulletCom.BulletModify(iFillBulletCnt)
        self.RepeatHeartBeat(oItem)



class CHaltFillBulletStatus(CFillBulletStatus):
    
    def OnEnter(self, oItem):
        oHero = oItem.GetOwner()
        oBulletCom = oItem.GetComponent('Bullet')
        oStatusMgr = oBulletCom.m_FillBulletStatusMgr
        pFunc = Functor(oStatusMgr.CallBackChangeStatus, oHero, oItem.m_ID, oStatusMgr.STATUS_NORMAL)
        oHero.Call_Out(pFunc, self.GetDelayAutoFill(oItem), 'DelayAutoFillBullet%s' % oItem.m_ID)

    
    def OnExit(self, oItem):
        oHero = oItem.GetOwner()
        if oHero:
            oHero.Remove_Call_Out('DelayAutoFillBullet%s' % oItem.m_ID)



class CRepeatHaltFillBulletStatus(CFillBulletStatus):
    
    def OnEnter(self, oItem):
        oBulletCom = oItem.GetComponent('Bullet')
        oStatusMgr = oBulletCom.m_FillBulletStatusMgr
        if not self.OnCheckChangeStatus(oItem, oStatusMgr):
            return None
        oStatusMgr.ChangeStatus(oItem, oStatusMgr.STATUS_NORMAL)

    
    def OnCheckChangeStatus(self, oItem, oStatusMgr):
        oHero = oItem.GetOwner()
        if not oHero:
            return False
        if not oStatusMgr.CheckFillBullet(oItem, oHero):
            return False
        oComPerform = oItem.GetComponent('Perform')
        if not oComPerform:
            return False
        if oComPerform.m_RepeatCnt <= 1:
            return False
        if oComPerform.m_TempFireCnt % oComPerform.m_RepeatCnt != 0:
            return False
        return True



class CStopFillBulletStatus(CFillBulletStatus):
    pass


class CEmptyClipNormalFillBulletStatus(CNormalFillBulletStatus):
    
    def OnEnter(self, oItem):
        oBulletCom = oItem.GetComponent('Bullet')
        if not oBulletCom:
            return None
        if not oBulletCom.Bullet():
            oHero = oItem.GetOwner()
            dAutoFillLimitWeapon = oHero.Query('AutoFillLimitWeapon', { })
            if oItem.m_SID in dAutoFillLimitWeapon:
                oItem.AddAttention(itemdef.MSG_ITEM_BULLETMODIFY, self.OnAutoFillBullet, 'OnAutoFillBullet')
                return None
        super().OnEnter(oItem)

    
    def OnAutoFillBullet(self, oItem, oWarrior):
        oBulletCom = oItem.GetComponent('Bullet')
        if not oBulletCom:
            return None
        if not oBulletCom.Bullet():
            return None
        oItem.DoneAttention(itemdef.MSG_ITEM_BULLETMODIFY, 'OnAutoFillBullet')
        oStatusMgr = oBulletCom.m_FillBulletStatusMgr
        if not oStatusMgr or not oStatusMgr.IsNormal():
            return None
        self.AutoFillBulletHeartBeat(oWarrior, oItem.m_ID)



class CFillBulletStatusMgr(CStatusMgr):
    STATUS_NORMAL = 1
    STATUS_HALT = 2
    STATUS_STOP = 3
    m_Status = {
        STATUS_STOP: CStopFillBulletStatus(),
        STATUS_HALT: CHaltFillBulletStatus(),
        STATUS_NORMAL: CNormalFillBulletStatus() }
    m_HaltMsg = []
    m_InitStatus = STATUS_STOP
    
    def __init__(self, oItem):
        super().__init__(oItem)
        self.m_Item = oItem.m_ID
        oItem.AddAttention(itemdef.MSG_ITEM_ADD, self.Enable, 'EnableFillBullet')
        oItem.AddAttention(itemdef.MSG_ITEM_FIRE, self.Halt, 'FillBulletSTHalt')
        oItem.AddAttention(itemdef.MSG_ITEM_REMOVE, self.Exit, 'ExitFillBullet')
        oItem.AddAttention(itemdef.MSG_ITEM_FILLBULLET, self.Halt, 'FillBulletSTHalt')
        oItem.AddAttention(itemdef.MSG_ITEM_HOLD, self.Halt, 'FillBulletSTHalt')
        oItem.AddAttention(itemdef.MSG_ITEM_REFRESHATTRIBUTE, self.OnMaxBulletChange, 'FillBulletOnMaxBulletChange')
        self.OnExtendAttention(oItem)

    
    def OnExtendAttention(self, oItem):
        for iMsg in self.m_HaltMsg:
            oItem.AddAttention(iMsg, self.Halt, 'FillBulletSTHalt')
        

    
    def Enable(self, oItem, oWarrior):
        if not self.CheckFillBullet(oItem, oWarrior):
            return None
        sKey = 'ActiveFillBullet%d' % oItem.m_ID
        sKeyEnd = 'ActiveFillBulletEnd%d' % oItem.m_ID
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnActiveFillBullet, sKey, PF_SUBMSG_FILLBULLET, 0)
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_END, self.OnActiveFillBulletEnd, sKeyEnd, PF_SUBMSG_FILLBULLET, 0)
        self.Halt(oItem, oWarrior)

    
    def ChangeOrRefreshrStatus(self, oItem, oWarrior, iStatus):
        if not self.CheckFillBullet(oItem, oWarrior):
            return None
        if iStatus == self.m_CurStatus:
            self.GetCurStatusObject().Refresh(oItem)
        else:
            self.ChangeStatus(oItem, iStatus)

    
    def Halt(self, oItem, oWarrior):
        self.ChangeOrRefreshrStatus(oItem, oWarrior, self.STATUS_HALT)

    
    def Normal(self, oItem, oWarrior):
        self.ChangeOrRefreshrStatus(oItem, oWarrior, self.STATUS_NORMAL)

    
    def IsNormal(self):
        return self.m_CurStatus == self.STATUS_NORMAL

    
    def CheckFillBullet(self, oItem, oWarrior):
        dAutoFillLimitTag = oWarrior.Query('AutoFillLimitTag', { })
        for iTag in dAutoFillLimitTag:
            if iTag in oItem.m_ClassifyTag and oWarrior.IsForbid(FORBID_AUTO_FILLBULLET):
                return False
        
        if not oWarrior.m_WieldCon.GetItemByID(oItem.m_ID):
            return False
        oBulletCom = oItem.GetComponent('Bullet')
        if oBulletCom.Bullet():
            oComPerform = oItem.GetComponent('Perform')
            if oComPerform and oComPerform.CheckRepeat():
                return False
        return True

    
    def OnActiveFillBullet(self, oWarrior, dInfo):
        oSkill = dInfo['Skill']
        if self.m_Item != oSkill.m_Base['Weapon']:
            return None
        oItem = oWarrior.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
        self.ChangeStatus(oItem, self.STATUS_HALT)

    
    def OnActiveFillBulletEnd(self, oWarrior, dInfo):
        oSkill = dInfo['Skill']
        if self.m_Item != oSkill.m_Base['Weapon']:
            return None
        oItem = oWarrior.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
        self.ChangeStatus(oItem, self.STATUS_NORMAL)

    
    def CallBackChangeStatus(self, oHero, iItemID, iStatus):
        oItem = oHero.m_WieldCon.GetItemByID(iItemID)
        if not oItem:
            return None
        self.ChangeStatus(oItem, iStatus)

    
    def Exit(self, oItem, oWarrior):
        if oWarrior:
            sKey = 'ActiveFillBullet%d' % oItem.m_ID
            sKeyEnd = 'ActiveFillBulletEnd%d' % oItem.m_ID
            cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_START, sKey, PF_SUBMSG_FILLBULLET)
            cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_END, sKeyEnd, PF_SUBMSG_FILLBULLET)
        self.ChangeStatus(oItem, self.STATUS_STOP)

    
    def ChangeStatus(self, oOwner, iStatus):
        super().ChangeStatus(oOwner, iStatus)
        oOwner.GS2CItemPropChange('BulletState', self.m_CurStatus)

    
    def OnMaxBulletChange(self, oOwner, dMsgInfo):
        if not dMsgInfo['RefreshAttribute'] == 'MaxBullet':
            return None
        oItem = oOwner.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
        if not oItem:
            return None
        oBulletCom = oItem.GetComponent('Bullet')
        iMaxBullet = oBulletCom.MaxBullet()
        iNowBullet = oBulletCom.Bullet()
        if iNowBullet < iMaxBullet:
            self.Halt(oItem, oOwner)



class CEmptyClipFillBulletStatusMgr(CFillBulletStatusMgr):
    STATUS_NORMAL = 1
    STATUS_HALT = 2
    STATUS_STOP = 3
    m_Status = {
        STATUS_STOP: CStopFillBulletStatus(),
        STATUS_HALT: CHaltFillBulletStatus(),
        STATUS_NORMAL: CEmptyClipNormalFillBulletStatus() }
    
    def Exit(self, oItem, oWarrior):
        oItem.DoneAttention(itemdef.MSG_ITEM_BULLETMODIFY, 'OnAutoFillBullet')
        super().Exit(oItem, oWarrior)



class CRepeatShootFillBulletStatusMgr(CFillBulletStatusMgr):
    STATUS_NORMAL = 1
    STATUS_HALT = 2
    STATUS_STOP = 3
    m_Status = {
        STATUS_STOP: CStopFillBulletStatus(),
        STATUS_HALT: CRepeatHaltFillBulletStatus(),
        STATUS_NORMAL: CNormalFillBulletStatus() }
    m_HaltMsg = [
        itemdef.MSG_ITEM_REPEAT_END]

TYPE2FILLBULLETSTATUS = {
    AUTOFILL_RULE_REPEATEND: CRepeatShootFillBulletStatusMgr,
    AUTOFILL_RULE_EMPTYCLIP: CEmptyClipFillBulletStatusMgr,
    AUTOFILL_RULE_NONE: CFillBulletStatusMgr }

def GetFillBulletStatusMgr(iType):
    return TYPE2FILLBULLETSTATUS.get(iType, CFillBulletStatusMgr)

