# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/inscription/__init__.pyc
# RelativePath: clientlogic/cl_perform/inscription/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_INSCRIPTION, INSCRIPTION_TYPE_NORMAL

class CInscription(CPerform):
    m_MaxUpgradeTimes = 0
    m_PFType = PF_TYPE_INSCRIPTION
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    
    def CheckValidItem(cls, oItem, lstHas):
        if not cls.CheckValidItemByWeapon(oItem):
            return 0
        if not cls.CheckValidItemByInscription(lstHas):
            return 0
        return 1

    CheckValidItem = classmethod(CheckValidItem)
    
    def CheckValidItemByWeapon(cls, oItem):
        (lstLimitTag, lstWeaponSID, lstAngTag) = cls.m_LimitList
        if lstWeaponSID and oItem.m_SID not in lstWeaponSID:
            return 0
        for iTag in lstLimitTag:
            if iTag not in oItem.m_ClassifyTag:
                return 0
        
        (lstExcTag, _, lstWeaponSID) = cls.m_ExcludeList
        for iTag in lstExcTag:
            if iTag in oItem.m_ClassifyTag:
                return 0
        
        if oItem.m_SID in lstWeaponSID:
            return 0
        if lstAngTag:
            for iTag in lstAngTag:
                if iTag in oItem.m_ClassifyTag:
                    break
            else:
                return 0
        return 1

    CheckValidItemByWeapon = classmethod(CheckValidItemByWeapon)
    
    def CheckValidItemByInscription(cls, lstHas):
        (_, lstInscription, _) = cls.m_ExcludeList
        for iSID in lstHas:
            if iSID in lstInscription:
                return 0
        
        return 1

    CheckValidItemByInscription = classmethod(CheckValidItemByInscription)

