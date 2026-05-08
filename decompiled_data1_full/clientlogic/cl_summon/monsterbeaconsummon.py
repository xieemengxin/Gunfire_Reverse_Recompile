# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/monsterbeaconsummon.pyc
# RelativePath: clientlogic/cl_summon/monsterbeaconsummon.pyc
# Source Generated with Decompyle++
# File: monsterbeaconsummon.pyc (Python 3.6)

from . import mobject

class CMonsterBeaconSummon(mobject.CBaseSummon):
    
    def SetAttachTarget(self, iAttachTarget):
        self.m_AttachTarget = iAttachTarget

    
    def ClearAttachTarget(self):
        self.m_AttachTarget = 0


