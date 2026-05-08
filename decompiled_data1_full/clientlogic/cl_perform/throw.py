# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/throw.pyc
# RelativePath: clientlogic/cl_perform/throw.pyc
# Source Generated with Decompyle++
# File: throw.pyc (Python 3.6)

from cl_only import GAME_FRAME_TIME
from cl_commondefines import PF_TYPE_THROW, FORBID_THROW, DAM_TYPE_NORMAL, PF_SUBMSG_THROW, DEBUG_STATUS_NOCOSTBULLET, SKILLRET_FAIL
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype

class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_THROW
    m_SubMsg = PF_SUBMSG_THROW
    m_CheckForbid = FORBID_THROW
    m_ElementType = DAM_TYPE_NORMAL
    m_BulletUse = 1
    m_ClientNeed = 1
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_CurBulletUse = self.m_BulletUse
        self.m_BulletUseDict = { }
        self.m_BulletExtraUseDict = { }
        self.m_IgnoreBulletJudge = 0

    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def GetCDTime(self, oWarrior):
        iCDTime = self.CalAttr('ColdTime')
        return iCDTime // GAME_FRAME_TIME

    
    def AddAttColdTime(self, oWarrior, iActNum):
        oWarrior.m_Perform.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = iActNum)

    
    def CanUse(self, oWarrior, dInfo):
        if not (self.m_IgnoreBulletJudge) and oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET and 'PerformUseNoCost' not in dInfo:
            iBulletSID = self.CalAttr('BulletSID')
            if iBulletSID and oWarrior.m_BulletCon.Bullet(iBulletSID) < self.m_CurBulletUse:
                return 0
        return super(CPerform, self).CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = self.m_CurBulletUse
        self.SendUseMsg(oWarrior, oSkill)
        iActNum = oSkill.m_Base['ActNum']
        self.AddAttColdTime(oWarrior, iActNum)
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET:
            iBulletSID = self.CalAttr('BulletSID')
            if iBulletSID:
                oBulletCon = oWarrior.m_BulletCon
                iBagBullet = oBulletCon.Bullet(iBulletSID)
                iBulletUse = self.CalBulletUse(oSkill)
                iBulletUse = min(iBulletUse, iBagBullet)
                iCost = oWarrior.m_BulletCon.BulletModify(iBulletSID, -iBulletUse, 'throw')
                oSkill.m_Collect['RealBullet'] = -iCost
        self.DoAction(oSkill)

    
    def CalBulletUse(self, oSkill):
        if 'NoBulletUse' not in oSkill.m_Collect:
            iExtBulletUse = oSkill.m_Collect['ExtBulletUse'] if 'ExtBulletUse' in oSkill.m_Collect else 0
            iCurBulletUse = oSkill.m_Collect['BaseBullet'] if 'BaseBullet' in oSkill.m_Collect else 0
            iFinalUse = iCurBulletUse + iExtBulletUse
            if 'FinalMulBulletUse' in oSkill.m_Collect:
                iFinalUse = iFinalUse * (oSkill.m_Collect['FinalMulBulletUse'] + 10000) // 10000
            return iFinalUse
        return 0

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        dData['ElementType'] = self.m_ElementType
        return dData

    
    def BulletUse(self):
        return self.m_CurBulletUse

    
    def SetBulletUseByKey(self, iCnt, sKey):
        self.m_BulletUseDict[sKey] = iCnt
        self.AfterChangeBulletUse()

    
    def ClearBulletUseByKey(self, sKey):
        if sKey not in self.m_BulletUseDict:
            return None
        self.m_BulletUseDict.pop(sKey)
        self.AfterChangeBulletUse()

    
    def SetBulletExtraUseByKey(self, iCnt, sKey):
        self.m_BulletExtraUseDict[sKey] = iCnt
        self.AfterChangeBulletUse()

    
    def ClearBulletExtraUseByKey(self, sKey):
        if sKey not in self.m_BulletExtraUseDict:
            return None
        self.m_BulletExtraUseDict.pop(sKey)
        self.AfterChangeBulletUse()

    
    def AfterChangeBulletUse(self):
        iNewBulletUse = self.GetRealCnt()
        if iNewBulletUse == self.m_CurBulletUse:
            return None
        self.m_CurBulletUse = iNewBulletUse
        self.GS2CPerformPropChange('BulletUse', iNewBulletUse)

    
    def GetRealCnt(self):
        iMaxTemp = 0
        for iCnt in self.m_BulletUseDict.values():
            if iCnt == 0:
                return 0
            iMaxTemp = max(iMaxTemp, iCnt)
        
        iMaxTemp = self.m_BulletUse if not self.m_BulletUseDict else iMaxTemp
        for iExtra in self.m_BulletExtraUseDict.values():
            iMaxTemp += iExtra
        
        return iMaxTemp



class CUseCountPerform(CPerform):
    
    def __init__(self, oOwner, iLevel):
        super().__init__(oOwner, iLevel)
        self.m_CanUseCount = 0

    
    def AddCanUseCount(self, iAdd = 1):
        self.m_CanUseCount += iAdd

    
    def CanUse(self, oWarrior, dInfo):
        if self.m_CanUseCount < 1:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        self.m_CanUseCount -= 1
        super().UsePerform(oWarrior, oSkill)



class CEnergyPerform(CPerform):
    
    def CanUse(self, oWarrior, dInfo):
        if not self.CheckMinUseEnergy(oWarrior) and 'PerformUseNoCost' not in dInfo:
            return SKILLRET_FAIL
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = self.m_CurBulletUse
        self.SendUseMsg(oWarrior, oSkill)
        iActNum = oSkill.m_Base['ActNum']
        self.AddAttColdTime(oWarrior, iActNum)
        self.CostEnergy(oWarrior, oSkill)
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET:
            iBulletSID = self.CalAttr('BulletSID')
            if iBulletSID:
                oBulletCon = oWarrior.m_BulletCon
                iBagBullet = oBulletCon.Bullet(iBulletSID)
                iBulletUse = self.CalBulletUse(oSkill)
                iBulletUse = min(iBulletUse, iBagBullet)
                iCost = oWarrior.m_BulletCon.BulletModify(iBulletSID, -iBulletUse, 'throw')
                oSkill.m_Collect['RealBullet'] = -iCost
        self.DoAction(oSkill)


