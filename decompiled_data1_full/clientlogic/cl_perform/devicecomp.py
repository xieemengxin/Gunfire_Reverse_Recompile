# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/devicecomp.pyc
# RelativePath: clientlogic/cl_perform/devicecomp.pyc
# Source Generated with Decompyle++
# File: devicecomp.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_DEVICECOMP, PERFORM_POS_MAIN

class CDeviceComp(CPerform):
    m_Pos = 0
    m_PFType = PF_TYPE_DEVICECOMP
    m_ExclusiveDevice = ()
    m_ExclusiveHero = ()
    m_ExcludeComp = ()
    m_DropShape = 0
    m_Type = 0
    m_DeployActive = 0
    m_FirstChooseExtWeight = 0
    
    def OnEnableComponent(self, oWarrior):
        if not self.m_DeployActive:
            self.Enable(oWarrior)
        else:
            oDevice = oWarrior.GetDevice()
            if oDevice and oDevice.DeployStatus():
                self.Enable(oWarrior)

    
    def OnDisableComponent(self, oWarrior):
        self.Disable(oWarrior)

    
    def OnDeploy(self, oWarrior):
        if self.m_DeployActive:
            self.Enable(oWarrior)

    
    def OnRecycle(self, oWarrior):
        if self.m_DeployActive:
            self.Disable(oWarrior)

    
    def GetPerformPos(self):
        return PERFORM_POS_MAIN


