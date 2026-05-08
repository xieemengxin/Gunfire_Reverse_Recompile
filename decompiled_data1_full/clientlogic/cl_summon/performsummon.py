# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/performsummon.pyc
# RelativePath: clientlogic/cl_summon/performsummon.pyc
# Source Generated with Decompyle++
# File: performsummon.pyc (Python 3.6)

from cl_commondefines import SIDE_TYPE_HERO, WARRIOR_PERFORM, ATTACKERSUBMSG_SUMMON
from cl_resmgr.resdata import CSummonData
from . import mobject

class CPerformSummon(mobject.CBaseSummon):
    m_Side = SIDE_TYPE_HERO
    m_FightType = WARRIOR_PERFORM
    m_ValidShowTips = 0
    m_SubAttackMsg = ATTACKERSUBMSG_SUMMON
    
    def OnInitAttr(self, clsData, dAddData):
        self.m_Shape = dAddData['ObjShape']
        self.m_ClientOwner = dAddData['ClientOwner']
        self.m_BuffData = dAddData['BuffData']
        self.m_NeglectAttack = dAddData['NeglectAttack']

    
    def GetBuffData(self):
        return self.m_BuffData

    
    def IsNeglectAttack(self, oSkill):
        return False



class CPerformSummonData(CSummonData):
    m_SID = 1001
    m_Name = 'Buff球'
    m_Shape = 0
    m_FightType = WARRIOR_PERFORM

