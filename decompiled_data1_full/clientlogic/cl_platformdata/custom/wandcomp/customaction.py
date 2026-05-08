# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/wandcomp/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/wandcomp/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import STATE_TIME_FOREVER
from cl_only import SendAlert
import cl_state
import cl_action
import cl_formula

def CustomAction2050(oWarrior, oEventCB, dInfo):
    
    def RemoveState(oSkill):
        iState = oSkill.m_Collect[sKey]
        oWarrior.m_State.RemoveItem(iState)

    if 'StateSID' not in dInfo or 'RecordKey' not in dInfo or 'AddCount' not in dInfo or 'AddDamRatio' not in dInfo:
        return None
    oWandComp = oEventCB.GetObject()
    if not oWandComp:
        return None
    iShowCount = 0
    bShowCount = True
    oGame = oWarrior.m_Game
    iAttack = oWarrior.m_ID
    iStateSID = dInfo['StateSID']
    sRecordKey = dInfo['RecordKey']
    iAddCount = dInfo['AddCount']
    iMaxCount = dInfo['MaxCount'] if 'MaxCount' in dInfo else 999
    sKey = f'''{oEventCB.m_Key}_{sRecordKey}'''
    oCBReason = oEventCB.CBReason()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAddCount = cl_formula.GetResultByData(oWarrior, iAddCount, dEventInfo, dMsgInfo)
    iAddDamRatio = cl_formula.GetResultByData(oWarrior, dInfo['AddDamRatio'], dEventInfo, dMsgInfo)
    dActNum = oWandComp.GetArgValue(sRecordKey, { })
    for iActNum in list(dActNum):
        oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
        if not oSkill:
            dActNum.pop(iActNum)
            continue
        if sKey not in oSkill.m_Collect:
            oReason = oCBReason.GetCopyReason({
                'Item': dEventInfo['ItemID'] })
            dArgs = {
                'AID': iAttack,
                'RS': oReason,
                'PFLV': dEventInfo['PFLV'],
                'arg': { } }
            oState = cl_state.AddState(oWarrior, iStateSID, STATE_TIME_FOREVER, 0, dArgs)
            if not oState:
                continue
            oState.Enable(oWarrior)
            oSkill.m_Collect[sKey] = oState.m_ID
            oSkill.AddEndFunc(RemoveState)
        else:
            oState = oWarrior.m_State.GetItem(oSkill.m_Collect[sKey])
            if not oState:
                continue
            continue
        iOldCount = oState.GetCount()
        if iOldCount >= iMaxCount:
            iShowCount = iMaxCount
            bShowCount = False
            continue
        oState.AddCount(oWarrior, iAddCount)
        iCount = oState.GetCount()
        if iCount > iShowCount:
            iShowCount = iCount
        dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
        dFactor[sKey] = (iAddDamRatio * iCount, 0, 0)
        oSkill.m_Collect['DamFactor'] = dFactor
        dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
        dTransFactor[sKey] = dFactor[sKey]
        oSkill.m_Custom['TransDamFactor'] = dTransFactor
    
    if bShowCount:
        oLifeCycle = dEventInfo['LifeCycle']
        cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, iShowCount, 0)


def CustomActionCostBullet(oWarrior, oEventCB, dInfo):
    if 'Divisor' not in dInfo:
        SendAlert('err', '参数缺失 %s' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cost' not in dMsgInfo or 'ItemID' not in dMsgInfo:
        return None
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    iDivisor = dInfo['Divisor']
    dEventInfo = oEventCB.GetCBEventInfo()
    iDivisor = cl_formula.GetResultByData(oWarrior, iDivisor, dEventInfo, dMsgInfo)
    iCost = dMsgInfo['Cost']
    iMaxBullet = oWeapon.QueryAttr('MaxBullet')
    fAddPercent = (iCost / (iMaxBullet * iDivisor)) * 100
    oWandComp = oEventCB.GetObject()
    fRecordValue = oWandComp.GetArgValue('RecordValue', 0)
    fRecordValue += fAddPercent
    if fRecordValue >= 1:
        iAdd = int(fRecordValue)
        oWandComp.AddConditionCount(iAdd)
        fRecordValue -= iAdd
    oWandComp.SetArgValue('RecordValue', fRecordValue)


def CustomActionCostBagBullet(oWarrior, oEventCB, dInfo):
    if 'Divisor' not in dInfo:
        SendAlert('err', '参数缺失 %s' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Amount' not in dMsgInfo or 'ActNum' not in dMsgInfo:
        return None
    iCost = -dMsgInfo['Amount']
    oSkill = oWarrior.m_Game.m_SkillMgr.GetSkill(oWarrior.m_ID, dMsgInfo['ActNum'])
    if not oSkill:
        return None
    iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    iDivisor = dInfo['Divisor']
    dEventInfo = oEventCB.GetCBEventInfo()
    iDivisor = cl_formula.GetResultByData(oWarrior, iDivisor, dEventInfo, dMsgInfo)
    iMaxBullet = oWeapon.QueryAttr('MaxBullet')
    fAdd = (iCost / (iMaxBullet * iDivisor)) * 100
    oWandComp = oEventCB.GetObject()
    fRecordValue = oWandComp.GetArgValue('RecordValue', 0)
    fRecordValue += fAdd
    if fRecordValue >= 1:
        iAdd = int(fRecordValue)
        oWandComp.AddConditionCount(iAdd)
        fRecordValue -= iAdd
    oWandComp.SetArgValue('RecordValue', fRecordValue)

