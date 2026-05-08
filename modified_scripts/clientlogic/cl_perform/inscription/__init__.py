# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/inscription/__init__.pyc
# RelativePath: clientlogic/cl_perform/inscription/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

# 取消铭刻对武器类型、武器 SID、已有铭刻的全部限制
# 所有铭刻默认视为可在所有武器上生效

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
        return 1

    CheckValidItem = classmethod(CheckValidItem)
    
    def CheckValidItemByWeapon(cls, oItem):
        return 1

    CheckValidItemByWeapon = classmethod(CheckValidItemByWeapon)
    
    def CheckValidItemByInscription(cls, lstHas):
        return 1

    CheckValidItemByInscription = classmethod(CheckValidItemByInscription)
