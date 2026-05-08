# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season8/gemitem.pyc
# RelativePath: clientlogic/cl_seasonplay/season8/gemitem.pyc
# Source Generated with Decompyle++
# File: gemitem.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
from cl_cscommondef import GEMITEM_MASK

class CS8GemItemData(object):
    m_SID = 0
    m_Name = ''
    m_Type = GEMITEM_MASK
    m_PassivePerform = 0
    
    def Create(cls, oGame, dItemData, iPointID = 0, dTmp = None):
        oItem = CS8GemItem(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oItem)
        oItem.Init()
        if dItemData:
            oItem.Load(dItemData)
        return oItem

    Create = classmethod(Create)
    
    def Load(cls, oGame, dItemData, iPointID = 0, dTmp = None):
        oItem = CS8GemItem(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oItem)
        oItem.Init()
        if dItemData:
            oItem.Load(dItemData)
        return oItem

    Load = classmethod(Load)
    
    def InitItemData(cls, oItem):
        oItem.m_SID = cls.m_SID
        oItem.m_Name = cls.m_Name
        oItem.m_Type = cls.m_Type
        oItem.m_PassivePerform = cls.m_PassivePerform

    InitItemData = classmethod(InitItemData)


class CS8GemItem(CBaseItem):
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_GameID = oGame.m_ID
        self.m_Quality = 0
        self.m_PassivePerform = 0

    
    def __str__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.__class__.__name__, self.m_SID, self.m_ID, self.m_Quality, self.m_PassivePerform)

    
    def __repr__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.__class__.__name__, self.m_SID, self.m_ID, self.m_Quality, self.m_PassivePerform)

    
    def Load(self, dData):
        super().Load(dData)
        self.m_SID = dData.get('SID', 0)
        self.m_Quality = dData.get('QL', 0)

    
    def Save(self):
        dData = super().Save()
        dData['SID'] = self.m_SID
        dData['QL'] = self.m_Quality
        return dData

    
    def Init(self, iGrade = 1):
        super().Init(iGrade)


