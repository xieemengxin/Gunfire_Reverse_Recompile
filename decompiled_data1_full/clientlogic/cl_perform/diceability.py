# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/diceability.pyc
# RelativePath: clientlogic/cl_perform/diceability.pyc
# Source Generated with Decompyle++
# File: diceability.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_DICEABILITY

class CDiceAbility(CPerform):
    m_PFType = PF_TYPE_DICEABILITY
    m_Tag = ()
    m_PutOutPoolType = 0
    
    def GetMyItem(self):
        oOwner = self.GetOwner()
        if oOwner and self.m_Item:
            return oOwner.m_DiceCon.GetDiceByID(self.m_Item)


