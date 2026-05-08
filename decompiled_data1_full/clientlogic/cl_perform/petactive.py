# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/petactive.pyc
# RelativePath: clientlogic/cl_perform/petactive.pyc
# Source Generated with Decompyle++
# File: petactive.pyc (Python 3.6)

from cl_object import elementtype
from cl_only import Time2Frame, PY_FLAG_DEAD
from cl_perform.mobject import CPerform as CCustomPerform
from cl_commondefines import PF_TYPE_PETACTIVE, PF_SUBMSG_PETACTIVE, DAM_TYPE_NORMAL, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SLIP_SPELL, PETPF_ACTIVE_SPELL

class CPerform(CCustomPerform):
    m_Name = '妖灵主动'
    m_PFType = PF_TYPE_PETACTIVE
    m_SubMsg = PF_SUBMSG_PETACTIVE
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 0
    m_PFSubType = 0
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ClientNeed = 1
    
    def OnInit(self):
        self.m_ExtCover = 0
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
        dData['PFSubType'] = self.m_PFSubType
        return dData

    
    def AddExtCover(self):
        if self.m_ExtCover:
            return None
        self.m_ExtCover = 1
        self.m_Container.PerformMaxCoverChange(self.m_SID, 'MaxCover')

    
    def GetMaxCover(self, oWarrior):
        iMaxCover = super().GetMaxCover(oWarrior) + self.m_ExtCover
        return iMaxCover

    
    def UsePerform(self, oWarrior, oSkill):
        if self.m_ExtCover:
            super().UsePerform(oWarrior, oSkill)
            self.m_ExtCover = 0
            self.m_Container.PerformMaxCoverChange(self.m_SID, 'MaxCover')
        else:
            super().UsePerform(oWarrior, oSkill)

    
    def GetCDTime(self, oWarrior):
        if self.m_PFSubType == PETPF_ACTIVE_ATTACK:
            return Time2Frame(oWarrior.QueryAttr('AttSpeed'))
        if self.m_PFSubType == PETPF_ACTIVE_SLIP_SPELL:
            return super().GetCDTime(oWarrior)
        if not self.m_SpellPower:
            iSpellPower = oWarrior.QueryAttr('AttSpeed')
        else:
            iSpellPower = self.m_SpellPower
        return Time2Frame(oWarrior.QueryAttr('SkillInterval') * iSpellPower // 100)

    
    def CanUse(self, oWarrior, dInfo):
        if self.m_NeedTarget:
            if 'VID' not in dInfo:
                return 0
            oTarget = oWarrior.m_Game.GetObject(dInfo['VID'], PY_FLAG_DEAD)
            if not oTarget:
                return 0
        return super().CanUse(oWarrior, dInfo)

    
    def CheckIsSpell(self):
        if self.m_PFSubType == PETPF_ACTIVE_SPELL:
            return 1
        return 0

    
    def Enable(self, oWarrior, iNotify = 0):
        if self.m_Enable:
            return None
        if self.CheckIsSpell():
            oWarrior.AddEnableSpell(self.m_SID)
        super().Enable(oWarrior, iNotify)

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        if not self.m_Enable:
            return None
        if self.CheckIsSpell():
            oWarrior.RemoveEnableSpell(self.m_SID)
        super().Disable(oWarrior, iNotify, iReleaseFlag)


