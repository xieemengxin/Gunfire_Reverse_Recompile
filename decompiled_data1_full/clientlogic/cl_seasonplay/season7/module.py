# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season7/module.pyc
# RelativePath: clientlogic/cl_seasonplay/season7/module.pyc
# Source Generated with Decompyle++
# File: module.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
from cl_cscommondef import MODULE_MASK
from cl_container.backpackcon import BACKPACKCON_EMPTY_POS

class CModuleData(object):
    m_SID = 0
    m_Name = ''
    m_Type = MODULE_MASK
    m_QualityConfig = { }
    m_PointMax = { }
    m_EquipNumMax = 0
    m_DefaultPoint = 0
    
    def Create(cls, oGame, oModuleCon, dModule, iPointID = 0, dTmp = None):
        oModule = CModule(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oModule)
        if oModuleCon:
            oModule.AddToContainer(oModuleCon)
        if dModule:
            oModule.Load(dModule)
        oModule.Init()
        return oModule

    Create = classmethod(Create)
    
    def InitItemData(cls, oModule):
        oModule.m_SID = cls.m_SID
        oModule.m_Name = cls.m_Name
        oModule.m_Type = cls.m_Type
        oModule.m_QualityConfig = dict(cls.m_QualityConfig)
        oModule.m_PointMax = dict(cls.m_PointMax)
        oModule.m_EquipNumMax = cls.m_EquipNumMax

    InitItemData = classmethod(InitItemData)


class CModule(CBaseItem):
    m_QualityConfig = { }
    m_PointMax = { }
    m_EquipNumMax = 0
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_GameID = oGame.m_ID
        self.m_Quality = 0
        self.m_Point = 0
        self.m_DefaultPoint = 0

    
    def Load(self, dData):
        super().Load(dData)
        self.m_SID = dData.get('SID', 0)
        self.m_Quality = dData.get('QL', 0)
        self.m_Point = dData.get('SP', 0)
        self.m_DefaultPoint = dData.get('DP', 0)

    
    def Save(self):
        dData = super().Save()
        dData['SID'] = self.m_SID
        dData['QL'] = self.m_Quality
        dData['SP'] = self.m_Point
        dData['DP'] = self.m_DefaultPoint
        return dData

    
    def __str__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-s7module%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Quality, self.m_ID)

    
    def __repr__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-s7module%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Quality, self.m_ID)

    
    def GetAbilityByPoint(self, iPoint):
        if self.m_Quality not in self.m_QualityConfig:
            return []
        dAbility = { }
        for iTakeEffectPoint, (iAbility, iLevel) in self.m_QualityConfig[self.m_Quality].items():
            if iTakeEffectPoint > iPoint:
                continue
            if not iAbility not in dAbility:
                if iLevel > dAbility[iAbility]:
                    dAbility[iAbility] = iLevel
                    continue
        
        return dAbility

    
    def GetPointMax(self):
        if self.m_Quality not in self.m_PointMax:
            return 0
        return self.m_PointMax[self.m_Quality]

    
    def GetQuality(self):
        return self.m_Quality

    
    def AddPoint(self, iAdd):
        self.m_Point += iAdd

    
    def SubPoint(self, iRefund):
        self.m_Point -= iRefund

    
    def GetPoint(self):
        return self.m_Point + self.m_DefaultPoint

    
    def GetLock(self):
        return self.Query('Lock')


