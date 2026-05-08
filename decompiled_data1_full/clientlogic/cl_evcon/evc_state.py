# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/evc_state.pyc
# RelativePath: clientlogic/cl_evcon/evc_state.pyc
# Source Generated with Decompyle++
# File: evc_state.pyc (Python 3.6)

from cl_only import SendAlert
from cl_commondefines import DAM_MASK_ELEMENT
import cl_math
import cl_formula

def StateCBGetSelfCount(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return 0
    return oState.GetCount()


def StateCheckFromSameItem(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oReason = dEventInfo['RS']
    iPFItem = oReason.Query('Item', 0)
    if not iPFItem:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo:
        iItem = dMsgInfo['RS'].Query('Item', 0)
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo:
        iItem = dMsgInfo['Skill'].m_Base['Weapon']
    elif 'ReplaceID' in dMsgInfo:
        iItem = dMsgInfo['ReplaceID']
    else:
        return 0
    return iPFItem == iItem


def StateCheckFromSameAttacker(oListener, oEventCB, iCalOwnerObj = 0, iObjectType = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'StateID' not in dEventInfo:
        return 0
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return 0
    iTarget = dMsgInfo['AID']
    if not iTarget:
        return 0
    iAttacker = oState.m_Attacker
    if iTarget == iAttacker:
        return 1
    if iCalOwnerObj:
        if not iObjectType:
            oTarget = oListener.m_Game.GetObject(iTarget)
            if not oTarget:
                return 0
            return oTarget.m_Owner == iAttacker
        oStateAttack = oListener.m_Game.GetObject(iAttacker)
        if not oStateAttack:
            return 0
        iObjectID = oStateAttack.GetOwnObjectID(iObjectType)
        return iTarget == iObjectID
    return 0


def StateCheckWeaponFireCnt(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'FireCnt' not in oSkill.m_Cache:
        return 0
    iWeapon = oSkill.m_Base['Weapon']
    iFireCnt = oSkill.m_Cache['FireCnt']
    dFireCnt = oState.m_StateInfo.get('FireCnt', { })
    iStartCnt = dFireCnt.get(iWeapon, -1)
    if iStartCnt == -1:
        iRet = 0
    else:
        iRet = (iFireCnt - iStartCnt) + 1
    return iRet


def StateCheckTargetStatistics(oListener, oEventCB, sAttr):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if len(dTrans['TargetList']) != 1:
        SendAlert('err', '%s事件目标数量有误' % oEventCB.m_Key)
        return None
    iTarget = dTrans['TargetList'][0]
    sKey = '%s-%d' % (sAttr, iTarget)
    return oState.m_Data.get(sKey, 0)


def StateCBCheckHasSelf(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return False
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oTarget.m_State.GetItem(iStateID)
    if not oState:
        return False
    return True


def StateCheckFromSameSkill(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return False
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'StateInfo' not in dEventInfo:
        return False
    dStateInfo = dEventInfo['StateInfo']
    if 'ActNum' not in dStateInfo:
        return False
    oSkill = dMsgInfo['Skill']
    return oSkill.m_Base['ActNum'] == dStateInfo['ActNum']


def StateCBCheckTargetIsStateAttacker(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return False
    return lstTar[0] == oState.m_Attacker

