# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_passive.pyc
# RelativePath: clientlogic/cl_condition/con_passive.pyc
# Source Generated with Decompyle++
# File: con_passive.pyc (Python 3.6)

from cl_item.defines import MAIN_HOLD, EQUIP_MASK_WEAPON
from cl_only import Frame2Time

def PassiveCheckTaskStatus(oOwner, oLifeCycle, iStatus):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return False
    return oTask.m_Status == iStatus


def PassiveCheckFromMainHoldWeapon(oOwner, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    return oWeapon.GetComponent('Hold').HoldPos() == MAIN_HOLD


def PassiveCheckSourceWeaponHasInscription(oOwner, oLifeCycle, iInscription):
    oPerform = oLifeCycle.GetObject()
    oItem = oPerform.GetMyItem()
    if oItem and oItem.Type() & EQUIP_MASK_WEAPON:
        oWeaponCom = oItem.GetComponent('Perform')
        if not oWeaponCom:
            return 0
        if oWeaponCom.GetPerform(iInscription):
            return 1
    return 0


def PassiveCheckSourceWandSaveData(oOwner, oLifeCycle, sKey):
    oPerform = oLifeCycle.GetObject()
    oWand = oOwner.m_WandCon.GetWandByID(oPerform.m_Item)
    if not oWand:
        return 0
    return oWand.Query(sKey, 0)


def PassiveGetSourceWandRemainCD(oOwner, oEventCB):
    oPerform = oEventCB.GetObject()
    oWand = oOwner.m_WandCon.GetWandByID(oPerform.m_Item)
    if not oWand:
        return 0
    iRemainCD = oWand.m_CDDownFrame - oOwner.m_Game.GetFrameNum()
    if iRemainCD <= 0:
        return 0
    return Frame2Time(iRemainCD)


def PassiveCheckHasCycleTime(oOwner, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    return pfobj.HasCycleTime(oOwner)

