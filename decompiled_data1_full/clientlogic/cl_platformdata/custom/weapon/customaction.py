# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/weapon/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/weapon/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
from cl_container.statecon import GS2CStateAdd

def CustomActionWeapon1709(oWarrior, oEventCB, dInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oWeapon = oLifeCycle.GetObject()
    if not oWeapon:
        return None
    dFlagTarget = oWeapon.QueryTmp('PF_5316', { })
    oGame = oWarrior.m_Game
    iStateSID = dInfo['StateSID']
    for iTarget in dFlagTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iStateSID)
        for oState in lstState:
            if oState.m_Item != oWeapon.m_ID:
                continue
            GS2CStateAdd(oTarget, oTarget.m_State.m_GameBroadcast, oState, { })
        
    

