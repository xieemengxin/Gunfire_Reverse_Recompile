# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/careerpf.pyc
# RelativePath: clientlogic/cl_perform/careerpf.pyc
# Source Generated with Decompyle++
# File: careerpf.pyc (Python 3.6)

from cl_perform.mobject import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_CAREERPF, FORBID_USECAREERPF, DAM_TYPE_NORMAL, PF_SUBMSG_CAREERPF, DEBUG_STATUS_NOPFCD, DPSUBMSG_DEFAULT, SKILLRET_FAIL, DEBUG_STATUS_NOCOSTBULLET, PFBULLET_SUBMSG_ADD, PFBULLET_SUBMSG_COST, PFBULLET_SUBMSG_ADD_BEFORE
import cl_object.elementtype as elementtype
import cl_msgcenter
import cl_item.defines as itemdef

class CPerform(CCustomPerform):
    m_Name = '职业技能'
    m_PFType = PF_TYPE_CAREERPF
    m_SubMsg = PF_SUBMSG_CAREERPF
    m_CheckForbid = FORBID_USECAREERPF
    m_ElementType = DAM_TYPE_NORMAL
    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)
        self.m_CurPFBullet = 0

    
    def CurPFBullet(self):
        return self.m_CurPFBullet

    
    def MaxPFBullet(self):
        if 'MaxPFBullet' not in self.m_Attr:
            return 0
        return self.CalAttr('MaxPFBullet')

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        dData['ElementType'] = self.m_ElementType
        return dData



class CWeaponPerform(CPerform):
    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = 0
        oWeapon = oWarrior.m_WieldCon.GetCurWeapon()
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            oWarrior.m_Perform.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = oSkill.m_Base['ActNum'])
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.SendCostBulletMsg(oWarrior, oSkill, oWeapon)
        self.SendWeaponFireMsg(oWarrior, oSkill, oWeapon)
        self.DoAction(oSkill)

    
    def GetMyItem(self):
        oWarrior = self.m_Game.GetObject(self.m_Owner)
        return oWarrior.m_WieldCon.GetCurWeapon()

    
    def SendUseMsg(self, oWarrior, oSkill):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, oWarrior, {
            'Skill': oSkill })
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DP, oWarrior, {
            'Skill': oSkill,
            'UnCrtByOwnerSign': self.m_UnCrtByOwnerSign }, iSub = DPSUBMSG_DEFAULT)

    
    def SendCostBulletMsg(self, oWarrior, oSkill, oWeapon):
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom:
            iHasBullet = oBulletCom.Bullet()
            oSkill.m_Collect['CurBullet'] = iHasBullet
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTBULLET, oWarrior, {
                'Skill': oSkill,
                'ItemID': oWeapon.m_ID })
            oSkill.m_Collect['BulletUse'] = 0

    
    def SendWeaponFireMsg(self, oWarrior, oSkill, oWeapon):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONFIRE, oWarrior, {
            'Skill': oSkill }, iSub = DPSUBMSG_DEFAULT)



class CPFBulletPerform(CPerform):
    
    def CanUse(self, oWarrior, dInfo):
        if not (oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET) and 'PFBulletUse' in self.m_Attr and 'NoPFBulletUse' not in dInfo:
            iPFBulletUse = self.CalAttr('PFBulletUse')
            if iPFBulletUse and iPFBulletUse > self.m_CurPFBullet:
                return SKILLRET_FAIL
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            oWarrior.m_Perform.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = oSkill.m_Base['ActNum'])
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        if self.CalAttr('CostPFBulletDuringUse'):
            self.CostBullet(oWarrior, oSkill)
        self.DoAction(oSkill)

    
    def CostBullet(self, oWarrior, oSkill):
        if not (oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET) and 'PFBulletUse' in self.m_Attr:
            iPFBulletUse = self.CalAttr('PFBulletUse')
            if iPFBulletUse:
                self.CostPFBullet(iPFBulletUse)

    
    def AddPFBullet(self, iAdd):
        dMsgInfo = {
            'AddCount': iAdd }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PFBULLETCHANGE, self.GetOwner(), dMsgInfo, iSub = PFBULLET_SUBMSG_ADD_BEFORE)
        iAdd = dMsgInfo['RealAddCount'] if 'RealAddCount' in dMsgInfo else iAdd
        iNew = self.m_CurPFBullet + iAdd
        iMax = self.CalAttr('MaxPFBullet')
        if iMax and iNew > iMax:
            iNew = iMax
        if self.m_CurPFBullet != iNew:
            iRealAdd = iNew - self.m_CurPFBullet
            self.m_CurPFBullet = iNew
            self.GS2CPerformPropChange('CurPFBullet', self.m_CurPFBullet)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PFBULLETCHANGE, self.GetOwner(), {
                'pfid': self.m_SID,
                'RealAdd': iRealAdd }, iSub = PFBULLET_SUBMSG_ADD)

    
    def CostPFBullet(self, iPFBulletUse):
        iOld = self.m_CurPFBullet
        self.m_CurPFBullet -= iPFBulletUse
        if self.m_CurPFBullet < 0:
            self.m_CurPFBullet = 0
        self.GS2CPerformPropChange('CurPFBullet', self.m_CurPFBullet)
        iRealCost = iOld - self.m_CurPFBullet
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PFBULLETCHANGE, self.GetOwner(), {
            'pfid': self.m_SID,
            'RealCost': iRealCost }, iSub = PFBULLET_SUBMSG_COST)

    
    def RefreshCurPFBullet(self):
        if 'PFBulletUse' in self.m_Attr:
            self.GS2CPerformPropChange('CurPFBullet', self.m_CurPFBullet)



class CPFEnergyPerform(CPerform):
    
    def CanUse(self, oWarrior, dInfo):
        if not self.CheckMinUseEnergy(oWarrior):
            return SKILLRET_FAIL
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            oWarrior.m_Perform.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = oSkill.m_Base['ActNum'])
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.CostEnergy(oWarrior, oSkill)
        self.DoAction(oSkill)


