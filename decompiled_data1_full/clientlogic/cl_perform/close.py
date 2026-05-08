# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/close.pyc
# RelativePath: clientlogic/cl_perform/close.pyc
# Source Generated with Decompyle++
# File: close.pyc (Python 3.6)

from cl_perform.attack import CAttack as CCustomPerform
from cl_commondefines import PF_TYPE_CLOSE, FORBID_ATTACK, DEBUG_STATUS_NOPFCD
from cl_only import GAME_FRAME_TIME

class CPerform(CCustomPerform):
    m_Name = '近战攻击'
    m_PFType = PF_TYPE_CLOSE
    m_ComboPerform = ()
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)

    
    def GetCDTime(self, oWarrior):
        oWeapon = self.GetMyItem()
        return 10000 // oWeapon.QueryAttr('AttSpeed') * GAME_FRAME_TIME

    
    def AddAttColdTime(self, oWarrior):
        oItem = self.GetMyItem()
        oPerformCom = oItem.GetComponent('Perform')
        iCDTime = self.GetCDTime(oWarrior)
        lstCDPerform = []
        lstCDPerform.append(self.m_SID)
        lstCDPerform.extend(self.m_ExtPerform)
        if self.m_MainPerform:
            lstCDPerform.append(self.m_MainPerform)
            oMainPerform = oPerformCom.GetPerform(self.m_MainPerform)
            lstCDPerform.extend(oMainPerform.m_ExtPerform)
        for iPerform in set(lstCDPerform):
            oPerformCom.m_Perform.AddColdTimeNoSend(iPerform, iCDTime)
        

    
    def UsePerform(self, oWarrior, oSkill):
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            self.AddAttColdTime(oWarrior)
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)


