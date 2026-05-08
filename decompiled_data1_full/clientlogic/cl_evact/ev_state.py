# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_state.pyc
# RelativePath: clientlogic/cl_evact/ev_state.pyc
# Source Generated with Decompyle++
# File: ev_state.pyc (Python 3.6)

from cl_only import SendAlert, Time2Frame, PY_FLAG_DEAD, ShufferList, Functor
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, DAM_MASK_ELEMENT, DAM_MASK_PART, DISABLE_TYPE_STATE
from cl_commondefines import DAM_TYPE_PERFORM
from cl_item.defines import MAIN_HOLD
from cl_container.statecon import GS2CStateRefreshExtraInfo
from cl_cscommondef import EQUIP_TYPE_MAINWEAPON
from cl_object.logging import TaskLog
import cl_formula
import cl_state
import cl_action
import cl_war
import cl_container
import cl_msgcenter

def StateCBAddVictimState(oListener, oEventCB, iState, iTime, iWithState, dArgs, iSrcAID = 0, iUseMsgRS = 0, iCount = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dArgs = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, dMsgInfo)
    iStateID = dEventInfo['StateID']
    oGame = oListener.m_Game
    oScrState = oEventCB.GetObject()
    if iSrcAID >= 2:
        iAttack = oScrState.m_Attacker
    elif iSrcAID == 1:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iAttack = dMsgInfo['AID'] if 'AID' in dMsgInfo else oListener.m_ID
    else:
        iAttack = oListener.m_ID
    if iUseMsgRS and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
    else:
        oReason = oEventCB.CBReason()
    if iCount:
        iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    if oScrState:
        dArgs['ForceSrcPF'] = oScrState.m_StateInfo['pfid'] if 'pfid' in oScrState.m_StateInfo else 0
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        iLimitFrame = 0
        if iTime:
            iLimitTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
            if iLimitTime:
                iLimitFrame = Time2Frame(iLimitTime)
                if iLimitFrame <= 0:
                    SendAlert('err', '%d %s limittime:%d' % (oGame.m_ID, oEventCB.m_Key, iLimitTime))
                    iLimitFrame = 1
        iTimeType = STATE_TIME_LIMIT if iLimitFrame else STATE_TIME_FOREVER
        dData = {
            'AID': iAttack,
            'RS': oReason,
            'arg': dArgs }
        oNewState = cl_state.AddState(oTarget, iState, iTimeType, iLimitFrame, dData)
        if oNewState:
            oNewState.Enable(oTarget)
            if iCount:
                oNewState.AddCount(oTarget, iCount)
            if iWithState:
                oState = oListener.m_State.GetItem(iStateID)
                iNewState = oNewState.m_ID
                if oState:
                    oState.m_LifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
                        iTarget: iNewState })
                    continue
                oTarget.m_State.RemoveItem(iNewState)
    


def StateCBRemoveStateFromSelf(oListener, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.m_State.RemoveItemBySource(iState, oListener.m_ID)
    


def StateCBRemoveState(oListener, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iState)
        for oTarState in lstState:
            oTarget.m_State.RemoveItem(oTarState.m_ID)
        
    


def StateCBRefreshStateFromSelf(oListener, oEventCB, iState, iTime, iRefreshDealy):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo)
    iFrame = Time2Frame(iTime)
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iState)
        for oTarState in lstState:
            if oTarState.m_Attacker == oListener.m_ID or iTime:
                oTarState.SetTime(oTarget, iFrame, iRefreshDealy)
                continue
            oTarState.SetForever(oTarget)
        
    


def StateCBAddTargetStateTime(oListener, oEventCB, iState, iTime, iMaxTime, iFromAttacker = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo)
    iFrame = Time2Frame(iTime)
    iMaxTime = cl_formula.GetResultByData(oListener, iMaxTime, dEventInfo)
    iMaxFrame = Time2Frame(iMaxTime)
    if iFromAttacker:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        if 'AID' in dMsgInfo:
            iAttack = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iAttack = dMsgInfo['Skill'].m_Base['AID']
        else:
            return None
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iState)
        for oTarState in lstState:
            if iFromAttacker and oTarState.m_Attacker != iAttack:
                continue
            cl_state.AddTime(oTarState, oTarget, iFrame, iMaxFrame)
        
    


def StateCBSelfRemove(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oListener.m_State.RemoveItem(iStateID)


def StateCBAddSelfTime(oListener, oEventCB, iTime, iMaxTime):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    cl_state.AddTime(oState, oListener, Time2Frame(iTime), Time2Frame(iMaxTime))


def StateAddSelfCount(oListener, oEventCB, iCount, iCountTime = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    if iCountTime:
        iCountTime = cl_formula.GetResultByData(oListener, iCountTime, dEventInfo, dMsgInfo)
        oState.AddCount(oListener, iCount, Time2Frame(iCountTime))
    else:
        oState.AddCount(oListener, iCount)


def StateRefreshCountToClinet(oListener, oEventCB):
    oStateCon = oListener.m_State
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return None
    iCnt = oState.GetCount()
    cl_container.statecon.GS2CStateRefreshCnt(oListener, oStateCon.m_GameBroadcast, oState, iCnt)


def StateAddSelfCountByFinalDamage(oListener, oEventCB, iCountFactor, iCalExcess = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TotalDam' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iTotalDamage = sum(dMsgInfo['TotalDam'])
    if iCalExcess and 'ExcessChange' in dMsgInfo:
        for iChange, _oReason in dMsgInfo['ExcessChange']:
            iTotalDamage += iChange
        
    iCount = iTotalDamage * iCountFactor // 100
    oState.AddCount(oListener, iCount)


def StateAddSelfCountByPredictPartDamage(oListener, oEventCB, iTargetDamType, iCountFactor):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return None
    oReason = dMsgInfo.get('RS', None)
    if not oReason:
        return None
    iDamType = oReason.Query('DamType')
    if iDamType & DAM_MASK_PART != iTargetDamType:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iTotalDamage = 0
    for _idx, iChange in enumerate(dMsgInfo['PredictChange']):
        iTotalDamage += iChange
    
    iCount = iTotalDamage * iCountFactor // 100
    oState.AddCount(oListener, iCount)


def StateImmuneDamageByType(oListener, oEventCB, iImmuneDamType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo and 'FlowDam' not in dMsgInfo:
        return None
    for sDamKey in ('MainDam', 'FlowDam'):
        lstNewDam = []
        for iDam, oReason in dMsgInfo[sDamKey]:
            iDamType = oReason.Query('DamType', 0)
            if iDamType & DAM_MASK_ELEMENT & iImmuneDamType == 0:
                lstNewDam.append((iDam, oReason))
        
        dMsgInfo[sDamKey] = lstNewDam
    


def StateSetSelfCount(oListener, oEventCB, iCount):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    iNowCount = oState.GetCount()
    oState.AddCount(oListener, iCount - iNowCount)


def StateCBAddSkillCollectInfo(oListener, oEventCB, sAttr, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iOldValue = oSkill.m_Collect[sAttr] if sAttr in oSkill.m_Collect else 0
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oSkill.m_Collect[sAttr] = iOldValue + iValue


def StateCBUsePerform(oListener, oEventCB, iPerform, iCustom, dCustom, iCalFormula = 0):
    oPerform = oListener.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iCustom and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dCartoon = oSkill.GetCurCartoon()
        vDefaultStart = oListener.GetPos()
        if 'CartoonPos' in oSkill.m_Collect:
            (vEnd, vStart) = oSkill.m_Collect['CartoonPos'][-1]
            if vEnd == vStart:
                vStart = vDefaultStart
            else:
                vStart = vDefaultStart
                if 'CurPos' in dCartoon:
                    vEnd = dCartoon['CurPos']
                elif 'ID' in dCartoon:
                    pass
                
                iCartoon = 0
                SendAlert('err', '%s 技能PF%s cartoonID:%s 缺失当前坐标' % (oEventCB.m_Key, oSkill.m_Base['pfid'], iCartoon))
                vDefaultEnd = oSkill.m_Base['vEnd']
                oAttack = oSkill.GetAttack()
                if oAttack:
                    vDefaultEnd = oAttack.GetPos()
                vEnd = vDefaultEnd
        if None in dCustom or 'vStart' in dCustom:
            SendAlert('err', '状态回调释放技能传入的字典不能有vStart/vEnd %s' % oEventCB.m_Key)
            return None
        dCustom['vEnd'] = vEnd
        dCustom['vStart'] = vStart
        cl_war.UsePerform(oListener, oPerform, {
            'Custom': dCustom })
        return None
    if dCustom:
        if iCalFormula:
            dEventInfo = oEventCB.GetCBEventInfo()
            dCustom = cl_formula.CalArgsFormula(oListener, dCustom, dEventInfo, dMsgInfo)
        dData = {
            'Custom': dCustom }
    else:
        dData = { }
    cl_war.UsePerform(oListener, oPerform, dData)


def StateCBUsePerform2EvtTarget(oWarrior, oEventCB, iPerform, dCustomData):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if not oWarrior.GetPerform(iPerform):
        oWarrior.AddPerform(iPerform, 1)
    oPerform = oWarrior.GetPerform(iPerform)
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dCustomData = cl_formula.CalArgsFormula(oWarrior, dCustomData, dEventInfo, dMsgInfo)
    for iVictim in dTrans['TargetList']:
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            continue
        dData = {
            'Custom': dCustomData }
        dData['VID'] = iVictim
        cl_war.UsePerform(oWarrior, oPerform, dData)
    


def StateCBSelfAttackerUsePerform(oListener, oEventCB, iPerform, dData, iUseSelf):
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iAttack = oState.m_Attacker
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oPerform = oAttack.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    dPerform = {
        'Custom': {
            'vEnd': oListener.GetPos(),
            'vStart': oListener.GetPos(),
            'LockTarget': [
                oListener.m_ID] } }
    if 'pfid' in dEventInfo['StateInfo']:
        dPerform['Custom']['pfid'] = dEventInfo['StateInfo']['pfid']
    dPerform['Custom'].update(dData)
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' in dTrans:
        dPerform['Custom'].update({
            'TargetList': dTrans['TargetList'] })
    if iUseSelf:
        dPerform['VID'] = oListener.m_ID
    cl_war.UsePerform(oAttack, oPerform, dPerform)


def StateCBSelfAttackerUsePerformByHitPos(oListener, oEventCB, iPerform, dExtCustom):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    oAttack = oListener.m_Game.GetObject(oState.m_Attacker, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oSkill = dMsgInfo['Skill']
    oPerform = oAttack.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    for sKey, lstFormula in dExtCustom.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dExtCustom[sKey] = iRet
    
    if 'DirectHitCurPos' in oSkill.m_Collect:
        vCurPos = oSkill.m_Collect['DirectHitCurPos']
    elif 'CurHitPos' in oSkill.m_Update:
        vCurPos = oSkill.m_Update['CurHitPos']
    else:
        dCartoon = oSkill.GetCurCartoon()
        vCurPos = dCartoon['CurPos']
    iTarget = oListener.m_ID
    dData = {
        'Custom': {
            'vEnd': vCurPos,
            'vStart': vCurPos,
            'LockTarget': [
                iTarget] },
        'VID': iTarget }
    dData['Custom'].update(dExtCustom)
    cl_war.UsePerform(oAttack, oPerform, dData)


def StateCBSelfAttackerUseWeaponPerform(oListener, oEventCB, iPerform, dData, iUseSelf):
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iAttack = oState.m_Attacker
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oWeapon = oAttack.m_WieldCon.GetCurWeapon()
    if not oWeapon:
        return None
    oPerform = cl_action.GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    dPerform = {
        'Custom': {
            'vEnd': oListener.GetPos(),
            'vStart': oListener.GetPos(),
            'LockTarget': [
                oListener.m_ID] },
        'Weapon': oWeapon.m_ID }
    dPerform['Custom'].update(dData)
    if iUseSelf:
        dPerform['VID'] = oListener.m_ID
    cl_war.UsePerform(oAttack, oPerform, dPerform)


def StateCBHaltAttackerPerform(oListener, oEventCB, iPerform):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    oGame = oListener.m_Game
    iAttack = oState.m_Attacker
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    sKey = oState.Key()
    for iActNum, dCasting in oAttack.GetAllCasting():
        if dCasting['pfid'] != iPerform:
            continue
        cl_action.HaltCasting(oAttack, iActNum, sKey)
    


def StateCBFormula(oListener, oEventCB, tFormu):
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, tFormu, dEventInfo)
    return iVal


def StateCBReceiveDam(oListener, oEventCB, iDamVal, iDamType, iShowTips):
    dEventInfo = oEventCB.GetCBEventInfo()
    oStateReason = dEventInfo['RS']
    iAttack = dEventInfo['StateInfo']['AID']
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if iAttack:
        oAttack = oListener.m_Game.GetObject(iAttack)
        if not oAttack:
            return None
        iAttack = oAttack
    oReason = oStateReason.ExtInfo({
        'DamType': iDamType,
        'ShowTips': 1,
        'ActNum': 0 })
    iVal = cl_formula.GetResultByData(oListener, iDamVal, dEventInfo)
    lstMainDam = [
        [
            iVal,
            oReason]]
    dDamFactor = oState.GetEventDamFactor()
    dState = {
        'MainDam': lstMainDam,
        'RS': oReason,
        'DamFactor': dDamFactor }
    oListener.ReceiveState(iAttack, dState)


def StateCBChangeWeaponAttr(oTarget, oEventCB, sAttr, iVal, iMul, iFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oTarget.m_State.GetItem(iStateID)
    if not oState:
        return None
    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    sKey = dEventInfo['StateKey']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMul = cl_formula.GetResultByData(oTarget, iMul, dEventInfo, dMsgInfo)
    iVal = cl_formula.GetResultByData(oTarget, iVal, dEventInfo, dMsgInfo)
    oLifeCycle = dEventInfo['LifeCycle']
    for oWeapon in lstAdd:
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
        oWeapon.AttrChange(sAttr, iMul, iVal, sKey, iRemoveClear = 1)
    


def StateCBChangeSourceWeaponAttr(oTarget, oEventCB, sAttr, iAdd, iMul):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    sKey = oState.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dArgs = {
        'Weapon': oWeapon }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dEventInfo, dMsgInfo, dArgs)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dEventInfo, dMsgInfo, dArgs)
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    else:
        oWeapon.AttrClear(sAttr, sKey)


def StateCBChangeSkillDamFactor(oWarrior, oEventCB, iAdd, iMul, iMask, iTransmit = 0, iClearTransmit = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearTransFactorInState(tStateUseTransFactor, sKey)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    sKey = dEventInfo['StateKey']
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo)
    dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
    dFactor[sKey] = (iAdd, iMul, iMask)
    oSkill.m_Collect['DamFactor'] = dFactor
    if iTransmit == 1:
        dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
        dTransFactor[sKey] = (iAdd, iMul, iMask)
        oSkill.m_Custom['TransDamFactor'] = dTransFactor
        if iClearTransmit == 1:
            tStateUseTransFactor = oWarrior.GetStateUseTransFactor()
            if not tStateUseTransFactor:
                return None
            oLifeCycle = dEventInfo['LifeCycle']
            oLifeCycle.AddUniqueDisableFunc('StateCBChangeSkillDamFactor', ClearFunc, iCover = 0)


def StateCBClearWeaponForceAttr(oWarrior, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo and dMsgInfo['Skill'].m_Base['Weapon']:
        iItem = dMsgInfo['Skill'].m_Base['Weapon']
    else:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItem)
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['StateKey']
    oWeapon.ItemAttrForceClear(sAttr, sKey)


def StateCBSetWeaponForceAttr(oWarrior, oEventCB, sAttr, iValue, iFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oWarrior.m_State.GetItem(iStateID)
    if not oState:
        return None
    lstWeapon = oWarrior.m_WieldCon.GetWeapons(iFlag)
    iValue = cl_formula.GetResultByData(oWarrior, iValue, dEventInfo)
    sKey = oState.Key()
    oLifeCycle = dEventInfo['LifeCycle']
    for oWeapon in lstWeapon:
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
        oWeapon.ItemAttrForceSet(sAttr, iValue, sKey)
    


def StateCBSetPosToStateAttacker(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    oAttacker = oListener.m_Game.GetObject(oState.m_Attacker)
    if not oAttacker:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    dTrans['EPFPos'] = oAttacker.GetPos()


def StateCBAddSelfStateStatistics(oListener, oEventCB, iValue, sAttr):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo, dEventInfo)
    if sAttr in oState.m_Data:
        oState.m_Data[sAttr] += iValue
    else:
        oState.m_Data[sAttr] = iValue


def StateCBGetSelfStateStatistics(oListener, oEventCB, sAttr):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    if sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def StateCBSetSelfStateStatistics(oListener, oEventCB, sAttr, iValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo, dEventInfo)
    oState.m_Data[sAttr] = iValue


def StateCBAddTargetStatistics(oListener, oEventCB, sAttr, iVal):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oStateCon = oListener.m_State
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return None
    for iTarget in dTrans['TargetList']:
        sKey = '%s-%d' % (sAttr, iTarget)
        iOldCnt = oState.m_Data.get(sKey, 0)
        oState.m_Data[sKey] = iOldCnt + iVal
    


def StateCBSetSelfTime(oListener, oEventCB, iTime, iRefreshDelay):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    if iTime:
        cl_state.SetTime(oState, oListener, Time2Frame(iTime), iRefreshDelay)
    else:
        oState.SetForever(oListener)


def StateCBAddTargetWeaponSpecialAttrBase(oListener, oEventCB, sAttr, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oListener.m_Game
    iAttack = oState.m_Attacker
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    else:
        return None
    oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oAttack, iAdd, dEventInfo, dMsgInfo, {
        'Weapon': oWeapon })
    oWeapon.AddSpecialAttrBase(sAttr, iAdd)


def StateCBAddSelfState(oListener, oEventCB, iState, iTime, dArgs, iUseMsgAID, iUseMsgRS, iCount):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dArgs = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, dMsgInfo)
    iTarget = oListener.m_ID
    iAttack = dMsgInfo['AID'] if iUseMsgAID and 'AID' in dMsgInfo else iTarget
    oReason = dMsgInfo['RS'] if iUseMsgRS and 'RS' in dMsgInfo else oEventCB.CBReason()
    if iCount:
        iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    oScrState = oEventCB.GetObject()
    if oScrState:
        dArgs['ForceSrcPF'] = oScrState.m_StateInfo['pfid'] if 'pfid' in oScrState.m_StateInfo else 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    iLimitFrame = 0
    if iTime:
        iLimitTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
        if iLimitTime:
            iLimitFrame = Time2Frame(iLimitTime)
            if iLimitFrame <= 0:
                SendAlert('err', '%d %s limittime:%d' % (oGame.m_ID, oEventCB.m_Key, iLimitTime))
                iLimitFrame = 1
    iTimeType = STATE_TIME_LIMIT if iLimitFrame else STATE_TIME_FOREVER
    dData = {
        'AID': iAttack,
        'RS': oReason,
        'arg': dArgs }
    oNewState = cl_state.AddState(oTarget, iState, iTimeType, iLimitFrame, dData)
    if not oNewState:
        return None
    oNewState.Enable(oTarget)
    if iCount:
        oNewState.AddCount(oTarget, iCount)


def StateCBSelfAttackerUsePerformEvtTarget(oListener, oEventCB, iPerform, dData):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    iVictim = lstTarget[0]
    oVictim = oListener.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    iAttack = oState.m_Attacker
    oAttack = oListener.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oPerform = oAttack.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    dCustom = {
        'LockTarget': lstTarget,
        'LockTrigger': iVictim,
        'pfid': dEventInfo['StateInfo']['pfid'] if 'pfid' in dEventInfo['StateInfo'] else 0 }
    dCustom.update(dData)
    dPerform = {
        'Custom': dCustom,
        'VID': iVictim }
    cl_war.UsePerform(oAttack, oPerform, dPerform)


def StateCBTempDisableInscription(oListener, oEventCB, iType, iNum):
    
    def ClearTempDisableInscription(oListener, oLifeCycle):
        lstWeapon = oListener.m_WieldCon.GetWeapons(MAIN_HOLD)
        oWeapon = lstWeapon[0]
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            return None
        sKey = 'DisableInscription-%s-%s' % (oLifeCycle.Key(), oWeapon.m_ID)
        oInscriptionCom.RemoveTempDisbleInscription(sKey)

    lstWeapon = oListener.m_WieldCon.GetWeapons(MAIN_HOLD)
    if not lstWeapon:
        return None
    oWeapon = lstWeapon[0]
    if oWeapon.IsInitWeapon():
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = 'DisableInscription-%s-%s' % (oLifeCycle.Key(), oWeapon.m_ID)
    if oInscriptionCom.GetTempDisbleInscription(sKey):
        return None
    iInscriptionNum = oInscriptionCom.GetEnableInscriptionNumByType(iType)
    if not iInscriptionNum:
        return None
    if iInscriptionNum < iNum:
        iNum = iInscriptionNum
    dDisable = { }
    lstDisable = []
    lstAlreadyDisable = oInscriptionCom.GetDisableInscription()
    lstInscription = oInscriptionCom.GetInscriptionByType(iType)
    for iInscription in lstInscription:
        if iInscription not in lstAlreadyDisable:
            lstDisable.append(iInscription)
    
    lstDisable = ShufferList(oListener.m_Game, lstDisable)
    lstDisable = lstDisable[:iNum]
    dDisable = dict.fromkeys(lstDisable, 1)
    oInscriptionCom.TempDisableInscription(sKey, dDisable, iCover = 0)
    oLifeCycle.AddDisableFunc(ClearTempDisableInscription)


def StateCBChangeSkillDamFactorBySelfTransDamFactor(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dTransDamFactor = oState.GetArgValue('TransDamFactor', { })
    if not dTransDamFactor:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect['DamFactor'] = dTransDamFactor


def StateCBChangeDamageByStatistics(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if sAttr not in oState.m_Data:
        SendAlert('err', '%s状态没有该统计键 %s' % (oEventCB.m_Key, sAttr))
        return None
    iTotalChange = oState.m_Data[sAttr]
    iChangeBefore = iTotalChange
    for idx, iChange in enumerate(dMsgInfo['PredictChange']):
        if iTotalChange >= iChange:
            dMsgInfo['PredictChange'][idx] = 0
            iTotalChange -= iChange
            continue
        dMsgInfo['PredictChange'][idx] = iChange - iTotalChange
        iTotalChange = 0
    
    oState.m_Data[sAttr] = iTotalChange
    dMsgInfo['DeductionDamage'] = iChangeBefore - iTotalChange


def StateCBRecorvyInscriptionAndGrade(oListener, oEventCB, iTaskID, iGrade):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if oState.GetArgValue('ClearPunishEnd', 0):
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTaskID = cl_formula.GetResultByData(oListener, iTaskID, dEventInfo, dMsgInfo)
    iGrade = cl_formula.GetResultByData(oListener, iGrade, dEventInfo, dMsgInfo)
    if not iTaskID or not iGrade or iGrade < 0:
        SendAlert('err', '%s arg err %d %d ' % (oEventCB.m_Key, iTaskID, iGrade))
        return None
    oTask = oListener.m_TaskCon.GetTaskByID(iTaskID)
    if not oTask:
        SendAlert('err', '%s no task instance %d' % (oEventCB.m_Key, iTaskID))
        return None
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    sKey = 'DisableInscription-%s-' % iTaskID
    for oWeapon in lstWeapon:
        sTempKey = sKey + '%s' % oWeapon.m_ID
        dInscription = oTask.GetSaveData(sTempKey, { })
        if dInscription:
            iBaseGrade = oWeapon.m_BaseGrade
            oWeapon.SetBaseGrade(iBaseGrade + iGrade)
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            for iSID, _ in dInscription.items():
                oInscriptionCom.OnRemoveDisableInscription(iSID)
            
        oState.SetArgValue('ClearPunishEnd', 1)
        TaskLog.Debug('%d %d task clear punish %d %d' % (oListener.m_Game.m_ID, oListener.m_PlayerID, oTask.m_SID, oWeapon.m_SID))
    


def StateCBSendInvisibleEndMsg(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INVISIBLE_END, oListener, dMsgInfo)


def StateCBSelfAttackerUseOnlyServerPerform(oListener, oEventCB, iPerform, dData):
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    oGame = oListener.m_Game
    iAttack = oState.m_Attacker
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    dPerform = {
        'Custom': dData,
        'VID': oListener.m_ID }
    cl_war.UseOnlyServerPerform(oAttack, oPerform, dPerform)


def StateCBRecordSkillTransDamFactor(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dTransDamFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    oState.SetArgValue('TransDamFactor', dTransDamFactor)


def StateCBSetHeroSidePetAttr(oListener, oEventCB, iPetSID, sAttr, iVal):
    
    def ClearFunc(oListener, oLifeCycle):
        oHeroSidePetCon = oListener.m_HeroSidePetCon
        oPet = oHeroSidePetCon.GetHeroSidePetByID(iPetID)
        oPet.AttrClear(sAttr, sKey, 1)

    oHeroSidePetCon = oListener.m_HeroSidePetCon
    oPet = oHeroSidePetCon.GetHeroSidePetBySID(iPetSID)
    if not oPet:
        return None
    iPetID = oPet.m_ID
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    sKey = oState.Key()
    oAttr = oPet.GetAttr(sAttr)
    if not oAttr:
        oPet.SetAttr(sAttr, 0, 1)
        oPet.AttrChange(sAttr, 0, iVal, sKey)
    else:
        oPet.AttrClear(sAttr, sKey, 1)
        iCurVal = oPet.QueryAttr(sAttr)
        iAdd = iVal - iCurVal
        oPet.AttrChange(sAttr, 0, iAdd, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)

