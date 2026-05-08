# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/bullet/bulletdata.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/bullet/bulletdata.pyc
# Source Generated with Decompyle++
# File: bulletdata.pyc (Python 3.6)

import cl_item.bullet as itembullet
import cl_item.defines as itemdef

class CBulletData(object):
    m_SID = 0
    m_Shape = 0
    m_Type = itemdef.ITEM_TYPE_NONE
    m_Name = ''
    m_MaxAmount = 0
    
    def InitItemData(cls, oItem):
        oItem.m_SID = cls.m_SID
        oItem.m_Shape = cls.m_Shape
        oItem.m_Name = cls.m_Name
        oItem.m_MaxAmount = cls.m_MaxAmount

    InitItemData = classmethod(InitItemData)
    
    def Create(cls, oGame, iTemp = 0, iGrade = 1):
        clsItem = itembullet.CBullet
        oItem = clsItem(oGame, iTemp)
        cls.InitItemData(oItem)
        oItem.Init(iGrade)
        return oItem

    Create = classmethod(Create)

