# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/deviceactive.pyc
# RelativePath: clientlogic/cl_perform/deviceactive.pyc
# Source Generated with Decompyle++
# File: deviceactive.pyc (Python 3.6)

from cl_object import elementtype
from cl_perform.mobject import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_DEVICEACTIVE, PF_SUBMSG_DEVICEACTIVE, FORBID_DEVICE_ACTIVE, DAM_TYPE_NORMAL, DEVICE_PERFORM_POS_ARRANGE, PF_TYPE_MONSTERACT, FORBID_MONSTERPF
import cl_msgcenter

class CPerform(CCustomPerform):
    m_Name = '英雄装置主动'
    m_PFType = PF_TYPE_DEVICEACTIVE
    m_SubMsg = PF_SUBMSG_DEVICEACTIVE
    m_CheckForbid = FORBID_DEVICE_ACTIVE
    m_Pos = DEVICE_PERFORM_POS_ARRANGE
    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        for sAttr, iValue in self.m_BaseArgData.items():
            dData[sAttr] = iValue
        
        return dData

    
    def CanUse(self, oWarrior, dInfo):
        iEnergyCost = self.GetEnergyCost()
        if iEnergyCost and oWarrior.DeviceEnergy() < iEnergyCost:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        iEnergyCost = self.GetEnergyCost()
        if iEnergyCost:
            iEnergyCost = oWarrior.DeviceEnergyModify(-iEnergyCost)
        oSkill.m_Collect['EnergyCost'] = iEnergyCost
        return super().UsePerform(oWarrior, oSkill)

    
    def GetEnergyCost(self):
        if 'EnergyCost' not in self.m_Attr:
            return 0
        return self.CalAttr('EnergyCost')

    
    def GetPerformPos(self):
        return self.m_Pos



class CDeviceActive(CCustomPerform):
    m_Name = '装置召唤物主动'
    m_PFType = PF_TYPE_DEVICEACTIVE
    m_SubMsg = PF_SUBMSG_DEVICEACTIVE
    m_CheckForbid = FORBID_MONSTERPF
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 0
    m_CostEnergy = 0
    
    def OnInit(self):
        self.m_CurCostEnergy = self.m_CostEnergy
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

    
    def CanUse(self, oWarrior, dInfo):
        if 'Custom' not in dInfo:
            dInfo['Custom'] = { }
        dCustom = dInfo['Custom']
        iExtraUse = dCustom['ExtraUse'] if 'ExtraUse' in dCustom else 0
        dMsgInfo = {
            'pfid': self.m_SID,
            'ExtraUse': iExtraUse }
        oOwner = oWarrior.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEVICEACTIVE_COST_BEFORE, oOwner, dMsgInfo)
        if 'Custom' in dMsgInfo:
            dCustom.update(dMsgInfo['Custom'])
        if self.m_SID in oWarrior.SetDefault('IgnoreCost', { }):
            iEnergyCost = 0
        elif 'EnergyCost' in dMsgInfo:
            iEnergyCost = dMsgInfo['EnergyCost']
        elif 'IgnoreCost' in dCustom:
            iEnergyCost = 0
        else:
            iEnergyCost = self.CalAttr('EnergyCost')
        dCustom['PreEnergyCost'] = iEnergyCost
        if iEnergyCost and oOwner.DeviceEnergy() < iEnergyCost:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oOwner = oWarrior.GetOwner()
        iPreEnergyCost = oSkill.m_Custom['PreEnergyCost']
        iEnergyCost = oOwner.DeviceEnergyModify(-iPreEnergyCost)
        oSkill.m_Collect['EnergyCost'] = iEnergyCost
        super().UsePerform(oWarrior, oSkill)


