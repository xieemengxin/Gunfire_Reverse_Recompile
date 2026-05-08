# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/triggerpf/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/triggerpf/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

import cl_action

def CanUse1801(oWarrior):
    iHPMax = oWarrior.QueryAttr('HPMax')
    if oWarrior.Query('AlwaysCure'):
        return True
    if cl_action.CommonGetSavedData(oWarrior, None, 'CanCureAll'):
        iShieldMax = oWarrior.QueryAttr('ShieldMax')
        iArmorMax = oWarrior.QueryAttr('ArmorMax')
        if iShieldMax == oWarrior.Shield() and iArmorMax == oWarrior.Armor() and iHPMax == oWarrior.HP():
            return False
    if iHPMax == oWarrior.HP():
        return False
    return True


def CanUse1802(oWarrior):
    iShieldMax = oWarrior.QueryAttr('ShieldMax')
    if iShieldMax == oWarrior.Shield():
        return False
    return True


def CanUse1803(oWarrior):
    pfobj = oWarrior.GetCareerPerform()
    iPerform = pfobj.m_SID
    iColdTimeFrame = oWarrior.m_Perform.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return False
    return True


def CanUse1809(oWarrior):
    if oWarrior.DeviceEnergy() >= oWarrior.QueryAttr('MaxDeviceEnergy'):
        return False
    return True

TRIGGERPF_CANUSE = {
    1801: CanUse1801,
    1802: CanUse1802,
    1803: CanUse1803,
    1809: CanUse1809 }

def CheckTriggerPFCanUse(oWarrior, iTriggerPFID):
    if iTriggerPFID not in TRIGGERPF_CANUSE:
        return True
    cFun = TRIGGERPF_CANUSE[iTriggerPFID]
    return cFun(oWarrior)

