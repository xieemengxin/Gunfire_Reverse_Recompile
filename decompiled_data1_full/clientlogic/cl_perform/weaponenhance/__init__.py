# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/weaponenhance/__init__.pyc
# RelativePath: clientlogic/cl_perform/weaponenhance/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_WEAPONENHANCE

class CWeaponEnhance(CPerform):
    m_MaxUpgradeTimes = 0
    m_PFType = PF_TYPE_WEAPONENHANCE
    m_EnhanceAttr = { }
    m_LimitList = ((), ())
    m_ExcludeList = ((), (), ())
    
    def CheckValidItem(cls, oItem, lstHas):
        (lstLimitTag, lstWeaponSID) = cls.m_LimitList
        if lstWeaponSID and oItem.m_SID not in lstWeaponSID:
            return 0
        for iTag in lstLimitTag:
            if iTag not in oItem.m_ClassifyTag:
                return 0
        
        (lstExcTag, lstOhter, lstExcWeaponSID) = cls.m_ExcludeList
        for iTag in lstExcTag:
            if iTag in oItem.m_ClassifyTag:
                return 0
        
        for iSID in lstHas:
            if iSID in lstOhter:
                return 0
        
        if oItem.m_SID in lstExcWeaponSID:
            return 0
        return 1

    CheckValidItem = classmethod(CheckValidItem)

