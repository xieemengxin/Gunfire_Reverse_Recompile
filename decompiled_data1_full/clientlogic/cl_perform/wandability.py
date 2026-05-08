# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/wandability.pyc
# RelativePath: clientlogic/cl_perform/wandability.pyc
# Source Generated with Decompyle++
# File: wandability.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_WANDABILITY, FLOATING_ABILITY_QUALITY, ABILITY_TYPE_NEGATIVE, ABILITY_TYPE_EXCLUSIVE

class CWandAbility(CPerform):
    m_PFType = PF_TYPE_WANDABILITY
    m_QualityValue = { }
    m_AbilityType = 0
    m_BaseValue = 0
    m_IsReverseFloting = 0
    m_Quality = 0
    m_FloatingRange = 0
    m_FinalValue = 0
    
    def Enable(self, oWarrior, iNotify = 0):
        oGame = self.m_Game
        oWandElement = oGame.m_WarMgr.GetWandElement()
        if not oWandElement or not (oWandElement.m_Enable):
            return None
        self.m_FinalValue = self.m_BaseValue
        iQuality = self.m_Quality
        if self.CheckCanFloating():
            self.m_FinalValue = self.m_BaseValue * (100 + self.m_FloatingRange) / 100
        elif self.m_QualityValue and iQuality in self.m_QualityValue:
            self.m_FinalValue = self.m_QualityValue[iQuality]
        super().Enable(oWarrior, iNotify)

    
    def CheckCanFloating(cls):
        if cls.m_AbilityType in (ABILITY_TYPE_NEGATIVE, ABILITY_TYPE_EXCLUSIVE):
            return 0
        if cls.m_QualityValue:
            return 0
        return 1

    CheckCanFloating = classmethod(CheckCanFloating)
    
    def SetQuality(self, iQuality, iFloatingRange):
        if self.m_Quality or iQuality not in FLOATING_ABILITY_QUALITY:
            return None
        self.m_Quality = iQuality
        self.m_FloatingRange = iFloatingRange

    
    def GetQuality(self):
        return self.m_Quality

    
    def GetFloatingRange(self):
        return self.m_FloatingRange

    
    def GetFinalValue(self):
        return self.m_FinalValue

    
    def GetFlotingType(cls):
        return cls.m_IsReverseFloting

    GetFlotingType = classmethod(GetFlotingType)

