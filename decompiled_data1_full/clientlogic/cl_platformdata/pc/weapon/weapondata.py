# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/weapondata.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/weapondata.pyc
# Source Generated with Decompyle++
# File: weapondata.pyc (Python 3.6)

from cl_platformdata.pc import GetWeaponExtInscription
from cl_only import DeepCopy
import cl_item.defines as itemdef
import cl_item.weapon as itemweapon

class CWeaponData(object):
    m_SID = 0
    m_Shape = 0
    m_Name = 0
    m_Type = 0
    m_ElementType = 0
    m_ItemAttr = { }
    m_ComponentAttr = { }
    m_ClassifyTag = ()
    m_bCanSell = 0
    m_Quality = 0
    m_ShopCash = 0
    m_CanDoubleHold = 0
    m_ExtItemAttr = { }
    m_ExtInscriptionWeight = { }
    m_RevertPFBullet = { }
    m_SpecialAttr = { }
    m_AIWeaponDam = 0
    m_AIAccuracyRate = 0
    m_Action = (None, None)
    m_UnlockInscription = []
    m_AutoChangeAttPf = 0
    
    def InitItemData(cls, oItem):
        oItem.m_SID = cls.m_SID
        oItem.m_Shape = cls.m_Shape
        oItem.m_Name = cls.m_Name
        oItem.m_Type = cls.m_Type
        oItem.m_ElementType = cls.m_ElementType
        oItem.m_ItemAttr = cls.m_ItemAttr
        oItem.m_ComponentAttr = cls.m_ComponentAttr
        oItem.m_ClassifyTag = cls.m_ClassifyTag
        oItem.m_bCanSell = cls.m_bCanSell
        oItem.m_Quality = cls.m_Quality
        oItem.m_ShopCash = cls.m_ShopCash
        oItem.m_CanDoubleHold = cls.m_CanDoubleHold
        oItem.m_ExtItemAttr = cls.m_ExtItemAttr
        oItem.m_ExtInscriptionWeight = GetWeaponExtInscription()[cls.m_SID] if cls.m_SID in GetWeaponExtInscription() else { }
        oItem.m_CBFuncAction = cls.m_CBFuncAction
        if cls.m_RevertPFBullet:
            oItem.m_RevertPFBullet = cls.m_RevertPFBullet
        if cls.m_SpecialAttr:
            oItem.m_SpecialAttr = DeepCopy(cls.m_SpecialAttr)
        oItem.m_AIWeaponDam = cls.m_AIWeaponDam
        oItem.m_AIAccuracyRate = cls.m_AIAccuracyRate
        oItem.m_Action = cls.m_Action
        oItem.m_AutoChangeAttPf = cls.m_AutoChangeAttPf

    InitItemData = classmethod(InitItemData)
    
    def Create(cls, oGame, iTemp = 0, iGrade = 1, iPointID = 0, dTmp = None):
        if cls.m_Type & itemdef.EQUIP_TYPE_MAINWEAPON == itemdef.EQUIP_TYPE_MAINWEAPON:
            clsItem = itemweapon.CGun
        elif cls.m_Type & itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            clsItem = itemweapon.CFundamentalWeapon
        else:
            clsItem = itemweapon.CWeapon
        oItem = clsItem(oGame, iTemp, iPointID, dTmp)
        cls.InitItemData(oItem)
        oItem.Init(iGrade)
        return oItem

    Create = classmethod(Create)
    
    def GetBulletType(cls):
        if 'Bullet' not in cls.m_ComponentAttr:
            return 0
        return cls.m_ComponentAttr['Bullet']['BulletType']

    GetBulletType = classmethod(GetBulletType)

