# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/s8thirdactive.pyc
# RelativePath: clientlogic/cl_perform/s8thirdactive.pyc
# Source Generated with Decompyle++
# File: s8thirdactive.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_NORMAL, PF_TYPE_S8THIRDACTIVE, PF_SUBMSG_S8THIRDACTIVE
from cl_object.logging import SeasoneightLog
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype

class CPerform(CCustomPerform):
    m_Name = 'S8第三技能主动'
    m_PFType = PF_TYPE_S8THIRDACTIVE
    m_SubMsg = PF_SUBMSG_S8THIRDACTIVE
    m_ElementType = DAM_TYPE_NORMAL
    m_UnCrtByOwnerSign = 1
    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        for sAttr, iValue in self.m_BaseArgData.items():
            dData[sAttr] = iValue
        
        dData['ArgData'] = { }
        for sAttr, iValue in self.m_ArgData.items():
            dData['ArgData'][sAttr] = iValue
        
        dData['ElementType'] = self.m_ElementType
        return dData

    
    def GetMyItem(self):
        oOwner = self.GetOwner()
        if not (self.m_Item) or not oOwner or not (oOwner.m_S8Con):
            return None
        return oOwner.m_S8Con.GetItemByID(self.m_Item)

    
    def CanUse(self, oWarrior, dInfo):
        oItem = self.GetMyItem()
        if not oItem:
            return 0
        if not oItem.CheckCanUseActive():
            SeasoneightLog.Error('%s %s use thirdactive err %s %s %s' % (self.m_Game.m_ID, oWarrior.m_PlayerID, oItem, oItem.m_Energy, oItem.QueryAttr('EnergyCost')))
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oItem = self.GetMyItem()
        if not oItem:
            return None
        iCost = oItem.UseActiveCost()
        oSkill.m_Collect['ThirdActiveCost'] = -iCost
        super().UsePerform(oWarrior, oSkill)


