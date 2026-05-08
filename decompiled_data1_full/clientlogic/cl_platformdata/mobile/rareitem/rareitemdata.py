# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rareitem/rareitemdata.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rareitem/rareitemdata.pyc
# Source Generated with Decompyle++
# File: rareitemdata.pyc (Python 3.6)

import cl_item.rareitem as rareitem
import cl_item.defines as itemdef

class CRareItemData(object):
    m_SID = 0
    m_Shape = 0
    m_Type = itemdef.RAREITEM_MASK
    m_Name = ''
    m_MaxGroup = 0
    m_UseNotify = 0
    m_UseAction = None
    
    def InitItemData(cls, oItem):
        oItem.m_SID = cls.m_SID
        oItem.m_Type = cls.m_Type
        oItem.m_Shape = cls.m_Shape
        oItem.m_Name = cls.m_Name
        oItem.m_MaxGroup = cls.m_MaxGroup
        oItem.m_UseNotify = cls.m_UseNotify
        oItem.m_UseAction = cls.m_UseAction

    InitItemData = classmethod(InitItemData)
    
    def Create(cls, oGame, iTemp = 0, iGrade = 1):
        clsItem = rareitem.CRareItem
        oItem = clsItem(oGame, iTemp)
        cls.InitItemData(oItem)
        oItem.Init(iGrade)
        return oItem

    Create = classmethod(Create)

