# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_state.pyc
# RelativePath: clientlogic/cl_condition/con_state.pyc
# Source Generated with Decompyle++
# File: con_state.pyc (Python 3.6)

from cl_item.defines import MAIN_HOLD
from cl_commondefines.cd_other import INKMASTER_HERO

def StateGetSelfCount(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if oState:
        return oState.GetCount()
    return 0


def StateCheckSourceWeaponHasInscription(oTarget, oLifeCycle, iSID):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if oWeapon:
        oPerformCom = oWeapon.GetComponent('Perform')
        if oPerformCom and oPerformCom.GetPerform(iSID):
            return 1
    return 0


def StateCheckFromMainHoldWeapon(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if oWeapon:
        return oWeapon.GetComponent('Hold').HoldPos() == MAIN_HOLD
    return 0


def StateCheckLiteCDInColdTime(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 1
    return oState.CheckLiteCD()


def StateCheckSelfAttackerHasTalent(oTarget, oLifeCycle, iTalent):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    iAttack = oState.m_Attacker
    oAttack = oTarget.m_Game.GetObject(iAttack)
    if not oAttack:
        return 0
    return iTalent in oAttack.m_TalentCon.m_Perform


def StateCheckInAttackerInkArea(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    iAttack = oState.m_Attacker
    oAttack = oTarget.m_Game.GetObject(iAttack)
    if not oAttack or oAttack.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = oAttack.m_InkCon
    return oInkCon.CheckTargetInInkArea(oTarget.m_ID)


def StateCheckUsedUpDelayCnt(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    if 'DelayCnt' in oState.m_DelayInfo:
        iCnt = oState.GetDelayCnt(oTarget)
        if iCnt and iCnt <= oState.m_DelayInfo['DelayCnt']:
            return 1
    return 0


def StateCheckStatistics(oTarget, oLifeCycle, sAttr):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    if sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def StateCheckNowCountEqualMaxCount(oListener, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return False
    return oState.GetCount() == oState.m_MaxCount


def StateCheckReason(oListener, oLifeCycle, sReason):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    if oState.m_Reason.GetStrReason() == sReason:
        return 1
    return 0

