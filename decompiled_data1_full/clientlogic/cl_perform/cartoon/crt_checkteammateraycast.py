# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_checkteammateraycast.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_checkteammateraycast.pyc
# Source Generated with Decompyle++
# File: crt_checkteammateraycast.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, WARRIOR_MECH
from cl_object.logging import SkillLog
from .crt_raycast import RayCastCartoon
from .mobject import CBaseCartoon

class CheckTeammateRaycastCartoon(RayCastCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if dCartoon['TargetType'] != OBJ_ALL:
            SkillLog.Alert('checkteammate parame err')
            return None
        super(CheckTeammateRaycastCartoon, cls).Trace(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def GetVictimPierceCost(cls, oSkill, iVictim, dCartoon = None):
        iCost = CBaseCartoon.GetVictimPierceCost(oSkill, iVictim)
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if iCost and dCartoon and oVictim:
            if 'NoCostServant' in dCartoon and oVictim.m_FightType == WARRIOR_MECH:
                iCost = 0
            if 'SkillCheckState' in oSkill.m_Collect and oVictim.m_State.GetItemBySID(oSkill.m_Collect['SkillCheckState']):
                iCost = 0
        return iCost

    GetVictimPierceCost = classmethod(GetVictimPierceCost)

