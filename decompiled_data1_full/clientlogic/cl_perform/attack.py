# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/attack.pyc
# RelativePath: clientlogic/cl_perform/attack.pyc
# Source Generated with Decompyle++
# File: attack.pyc (Python 3.6)

from cl_perform.mobject import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_ATTACK, FORBID_ATTACK, PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE, SKILLRET_CACHE, SKILLRET_FAIL, SKILLRET_SUCCESS, DEBUG_STATUS_NOCOSTBULLET
from cl_commondefines import DPSUBMSG_DEFAULT, PERFORM_POS_EXT, PERFORM_POS_MAIN, PERFORM_POS_MINOR, REASON_COSTBULLET_ATTACK, PFBULLET_SUBMSG_ADD_BEFORE
from cl_only import GAME_FRAME_TIME, Functor
import cl_msgcenter
import cl_war
from cl_object.logging import SkillLog

class CAttack(CCustomPerform):
    m_Name = '普通攻击'
    m_PFType = PF_TYPE_ATTACK
    m_CheckForbid = FORBID_ATTACK
    m_DPSubMsg = DPSUBMSG_DEFAULT
    
    def __init__(self, oOwner, iLevel):
        super(CAttack, self).__init__(oOwner, iLevel)
        self.m_CurAttPerform = self.m_SID
        self.m_NextAttackFrame = 0

    
    def PerformEnd(cls, oSkill):
        oWarrior = oSkill.GetAttack()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTACK_END, oWarrior, {
            'Skill': oSkill }, iSub = cls.m_DPSubMsg)
        cls.DoEndAction(oSkill)

    PerformEnd = classmethod(PerformEnd)
    
    def GetCDTime(self, oWarrior):
        return 10000 // oWarrior.QueryAttr('AttSpeed') * GAME_FRAME_TIME

    
    def GetSteadyCD(self, obj):
        oGame = self.m_Game
        iNowFrame = oGame.GetFrameNum() * 100
        iNextAttFrame = self.m_NextAttackFrame
        iCD = 100 * (10000 // obj.QueryAttr('AttSpeed') * GAME_FRAME_TIME)
        if iNextAttFrame <= iNowFrame - min(iCD * 3, 400):
            iNextAttFrame = iNowFrame
        self.m_NextAttackFrame = iNextAttFrame + iCD
        return (self.m_NextAttackFrame + 99 - iNowFrame) // 100

    
    def AddAttColdTime(self, oWarrior):
        oWarrior.m_Perform.AddColdTimeNoSend(self.m_SID, self.GetSteadyCD(oWarrior))

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        return dData



class CPerform(CAttack):
    m_Name = '射击'
    m_PFType = PF_TYPE_SHOOT
    m_BulletUse = 1
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_CurBulletUse = self.m_BulletUse
        self.m_CurPFBullet = 0
        self.m_CanAddPFBullet = 1

    
    def SetBulletUse(self, iCnt):
        self.m_CurBulletUse = iCnt
        self.GS2CPerformPropChange('BulletUse', self.m_CurBulletUse)

    
    def ResetBulletUse(self):
        self.m_CurBulletUse = self.m_BulletUse
        self.GS2CPerformPropChange('BulletUse', self.m_BulletUse)

    
    def BulletUse(self):
        return self.m_CurBulletUse

    
    def GetPerformPos(self):
        if self.m_MainPerform:
            return PERFORM_POS_EXT
        if self.m_IsMinor:
            return PERFORM_POS_MINOR
        return PERFORM_POS_MAIN

    
    def CanUse(self, oWarrior, dData):
        if not self.m_Enable:
            return SKILLRET_FAIL
        if not oWarrior.m_Scene:
            return SKILLRET_FAIL
        if oWarrior.IsDead():
            return SKILLRET_FAIL
        iCache = 0
        if 'CacheAttack' in dData:
            iCache = dData['CacheAttack']
        if oWarrior.IsForbid(self.m_CheckForbid, self.m_PassRule, dData['Weapon'], iCache):
            return SKILLRET_FAIL
        if 'PFBulletUse' in self.m_Attr:
            iPFBulletUse = self.CalAttr('PFBulletUse')
            if 'NoPFBulletUse' not in dData and iPFBulletUse and iPFBulletUse > self.m_CurPFBullet:
                return SKILLRET_FAIL
        iColdTime = self.m_Container.GetColdTime(self.m_SID)
        if iColdTime:
            if not oWarrior.WaitToAttack(self.m_SID, dData, iColdTime):
                return SKILLRET_FAIL
            return SKILLRET_CACHE
        return SKILLRET_SUCCESS

    
    def GetCDTime(self, oWarrior):
        oWeapon = self.GetMyItem()
        oPerformCom = oWeapon.GetComponent('Perform')
        iCD = oPerformCom.GetSteadyAttCDNoFire(self.m_IsMinor)
        if self.m_IsMinor and iCD == -1:
            return self.CalAttr('ColdTime') // GAME_FRAME_TIME
        return iCD // 100

    
    def GetSteadyCD(self, obj):
        iCD = obj.GetSteadyAttCD(self.m_IsMinor)
        if self.m_IsMinor:
            if iCD == -1:
                iPFCDTime = self.CalAttr('ColdTime')
                if iPFCDTime:
                    return iPFCDTime // GAME_FRAME_TIME
            return iCD // 100
        oGame = self.m_Game
        iNowFrame = oGame.GetFrameNum() * 100
        iNextAttFrame = self.m_NextAttackFrame
        if iNextAttFrame <= iNowFrame - min(iCD * 3, 400):
            iNextAttFrame = iNowFrame
        self.m_NextAttackFrame = iNextAttFrame + iCD
        return (self.m_NextAttackFrame + 99 - iNowFrame) // 100

    
    def ModifyNextAttackFrame(self, iFrame):
        self.m_NextAttackFrame += iFrame * 100

    
    def AddAttColdTime(self, oWarrior):
        oItem = self.GetMyItem()
        oPerformCom = oItem.GetComponent('Perform')
        oPerformCom.m_Perform.AddColdTimeNoSend(self.m_SID, self.GetSteadyCD(oPerformCom))

    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = self.m_CurBulletUse
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET == DEBUG_STATUS_NOCOSTBULLET:
            self.SendUseMsg(oWarrior, oSkill)
        else:
            self.AddAttColdTime(oWarrior)
            self.SendUseMsg(oWarrior, oSkill)
            self.CostBullet(oWarrior, oSkill)
        self.WeaponFire(oWarrior, oSkill)
        self.DoAction(oSkill)

    
    def CostBullet(self, oWarrior, oSkill):
        oWeapon = self.GetMyItem()
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom:
            iHasBullet = oBulletCom.Bullet()
            oSkill.m_Collect['CurBullet'] = iHasBullet
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTBULLET, oWarrior, {
                'Skill': oSkill,
                'ItemID': oWeapon.m_ID })
            iExtBulletUse = oSkill.m_Collect['ExtBulletUse'] if 'ExtBulletUse' in oSkill.m_Collect else 0
            iNeedBulletUse = oSkill.m_Collect['BaseBullet'] + iExtBulletUse
            iBulletSID = oBulletCom.BulletType()
            oBulletCon = oWarrior.m_BulletCon
            iBagBullet = oBulletCon.Bullet(iBulletSID)
            if 'FirstCostBulletFromContainer' in oSkill.m_Collect:
                iBagBulletUse = min(iNeedBulletUse, iBagBullet)
                iNeedBulletUse -= iBagBulletUse
                iComBulletUse = min(iNeedBulletUse, iHasBullet)
            else:
                iComBulletUse = min(iNeedBulletUse, iHasBullet)
                iNeedBulletUse -= iComBulletUse
                iBagBulletUse = min(iNeedBulletUse, iBagBullet)
            iRealBulletUse = iBagBulletUse + iComBulletUse
            oSkill.m_Collect['BulletUse'] = iRealBulletUse
            if 'NoBulletUse' not in oSkill.m_Collect:
                iActNum = oSkill.m_Base['ActNum']
                oBulletCon.BulletModify(iBulletSID, -iBagBulletUse, REASON_COSTBULLET_ATTACK, iSync = 0, bNotTrueModify = oWeapon.IsInitWeapon(), iActNum = iActNum)
                oBulletCom.BulletModify(-iComBulletUse, 0, sReason = REASON_COSTBULLET_ATTACK, iActNum = iActNum)
                oSkill.m_Collect['TotalBullet'] = iRealBulletUse
                oSkill.m_Collect['RealBullet'] = iRealBulletUse
        if 'PFBulletUse' in self.m_Attr:
            iPFBulletUse = self.CalAttr('PFBulletUse')
            if iPFBulletUse and self.CalAttr('CostPFBulletDuringUse') and 'NoPFBulletUse' not in oSkill.m_Collect:
                self.CostPFBullet(iPFBulletUse, oSkill.m_Collect['Sync'] if 'Sync' in oSkill.m_Collect else 1)

    
    def AddPFBullet(self, iAdd, iSync = 1, iMaxBulletSync = 0, iCalRecoverMul = 1):
        if not self.m_CanAddPFBullet:
            return None
        if iCalRecoverMul:
            iRecoverMul = self.CalAttr('PFBulletRecoverMul')
            iAdd = iAdd * iRecoverMul // 10000
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dInfo = {
            'pfid': self.m_SID,
            'ItemID': self.m_Item,
            'BulletNum': iAdd }
        if iSync and oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONPFBULLETCHANGE, oOwner, dInfo, iSub = PFBULLET_SUBMSG_ADD_BEFORE)
        iAdd = dInfo['BulletNum']
        iNew = self.m_CurPFBullet + iAdd
        iMax = self.MaxPFBullet()
        if iMax and iNew > iMax:
            iNew = iMax
        if self.m_CurPFBullet != iNew:
            iRealAdd = iNew - self.m_CurPFBullet
            self.m_CurPFBullet = iNew
            if iSync:
                self.RefreshCurPFBullet()
            if oOwner:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDPFBULLET, oOwner, {
                    'pfid': self.m_SID,
                    'ItemID': self.m_Item,
                    'RealAdd': iRealAdd })
            elif iMaxBulletSync and self.m_CurPFBullet == iMax:
                self.RefreshCurPFBullet()

    
    def CostPFBullet(self, iPFBulletUse, iSync = 1):
        iOldValue = self.m_CurPFBullet
        iCostMul = self.CalAttr('PFBulletCostMul')
        self.m_CurPFBullet -= iPFBulletUse * iCostMul // 10000
        if self.m_CurPFBullet < 0:
            self.m_CurPFBullet = 0
        if iSync:
            self.RefreshCurPFBullet()
        iRealCost = iOldValue - self.m_CurPFBullet
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner and iRealCost:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTPFBULLET, oOwner, {
                'pfid': self.m_SID,
                'ItemID': self.m_Item,
                'RealCost': iRealCost })

    
    def CurPFBullet(self):
        return self.m_CurPFBullet

    
    def MaxPFBullet(self):
        if 'MaxPFBullet' not in self.m_Attr:
            return 0
        return self.CalAttr('MaxPFBullet')

    
    def RefreshCurPFBullet(self):
        self.GS2CPerformPropChange('CurPFBullet', self.m_CurPFBullet)

    
    def SetCanAddPFBullet(self, iCanAdd):
        self.m_CanAddPFBullet = iCanAdd

    
    def GetCanAddPFBullet(self):
        return self.m_CanAddPFBullet

    
    def SendUseMsg(self, oWarrior, oSkill):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DP, oWarrior, {
            'Skill': oSkill }, iSub = self.m_DPSubMsg)

    
    def WeaponFire(self, oWarrior, oSkill):
        oWeapon = self.GetMyItem()
        oWeapon.Fire()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONFIRE, oWarrior, {
            'Skill': oSkill }, iSub = self.m_DPSubMsg)



class CContinuousPerform(CPerform):
    m_Name = '持续射击'
    m_PFType = PF_TYPE_CONSHOOT
    
    def CanUse(self, oWarrior, dData):
        if oWarrior.GetCastingByPF(self.m_SID, self.m_Item):
            return SKILLRET_FAIL
        return super(CContinuousPerform, self).CanUse(oWarrior, dData)

    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = self.m_CurBulletUse
        oSkill.m_Collect['TotalBullet'] = 0
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)



class CChargePerform(CPerform):
    m_Name = '蓄力射击'
    m_PFType = PF_TYPE_CHARGE
    
    def CanUse(self, oWarrior, dData):
        if oWarrior.GetCastingByPF(self.m_SID, self.m_Item):
            return SKILLRET_FAIL
        return super(CChargePerform, self).CanUse(oWarrior, dData)

    
    def UsePerform(self, oWarrior, oSkill):
        self.DoAction(oSkill)

    
    def TrueUsePerform(self, oWarrior, oSkill):
        self.AddAttColdTime(oWarrior)
        self.SendUseMsg(oWarrior, oSkill)


