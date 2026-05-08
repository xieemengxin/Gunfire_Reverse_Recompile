# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/buildsummon.pyc
# RelativePath: clientlogic/cl_summon/buildsummon.pyc
# Source Generated with Decompyle++
# File: buildsummon.pyc (Python 3.6)

import cl_war
from . import mobject

class CBuildSummon(mobject.CBaseSummon):
    m_ValidShowTips = 0
    
    def TriggerSummon(self, dTrigger):
        iPerform = dTrigger['Perform']
        oPerform = self.m_Perform.GetPerform(iPerform)
        if not oPerform:
            self.AddPerform(iPerform, 1)
        oPerform = self.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform = self.m_Perform.GetPerform(iPerform)
        cl_war.UsePerform(self, oPerform, { })


