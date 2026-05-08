# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/inscription/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/inscription/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import STATE_SPORE, PF_TYPE_CONSHOOT, WARRIOR_MONSTER, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, SKILLCACHE_INT, DISABLE_TYPE_STATE, STATE_TIME_FOREVER, USEPERFORM_POSTYPE_DEFAULT, OBJ_ATTACK, OBJ_VICTIM
from cl_only import PY_FLAG_DEAD, SendAlert
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
import cl_object
import cl_war
import cl_snetwar
import cl_perform
import cl_state
import cl_evcon
import cl_evact

def CustomAction4841(oWarrior, oEventCB, dInfo):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oGame = oWarrior.m_Game
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    lstWeapon = oAttack.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    if len(lstWeapon) < 2:
        return None
    iAttack = oWarrior.m_ID
    oState = oTarget.m_State.GetItemBySource(STATE_SPORE, iAttack)
    dEventInfo = oEventCB.GetCBEventInfo()
    if not oState:
        dStatArgs = {
            'AID': iAttack,
            'RS': cl_object.reason.CPerformReason(dEventInfo['pfid'], iAttack, oWarrior.m_SID, oWarrior.m_FightType, None, { }) }
        oState = cl_state.AddState(oTarget, STATE_SPORE, STATE_TIME_FOREVER, 0, dStatArgs)
        if not oState:
            return None
        oLifeCycle = dEventInfo['LifeCycle']
        dTargetState = {
            iTarget: oState.m_ID }
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, dTargetState)
    iCount = 1 + oState.GetCount()
    oSkill = dMsgInfo['Skill']
    dCartoon = oSkill.GetCurCartoon()
    dEventHit = oSkill.m_Collect.setdefault('HitCartoon', { })
    dHitCartoon = dEventHit.setdefault(oEventCB.Key(), { })
    iCartoon = dCartoon['ID'] if 'ID' in dCartoon else 0
    dHitCartoon[iCartoon] = 1
    if len(dHitCartoon) == 1 or oSkill.m_Base['PFType'] == PF_TYPE_CONSHOOT:
        iWeapon = oSkill.m_Base['Weapon']
        oWeapon = GetOtherWeapon(oWarrior, iWeapon)
        if not oWeapon:
            return None
        iCount += oWeapon.QueryAttr('Trajectory') // 100
    iTriggerNum = dInfo['TriggerNum']
    iRepeat = iCount // iTriggerNum
    iCount = iCount % iTriggerNum
    if iCount:
        oState.SetCount(oTarget, iCount)
    else:
        oTarget.m_State.RemoveItem(oState.m_ID)
    for _ in range(iRepeat):
        oEventCB.CBFuncAction(oWarrior, 3, dEventInfo, dMsgInfo)
    


def GetOtherWeapon(oWarrior, iWeapon):
    oOtherWeapon = None
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        if oWeapon.m_ID != iWeapon:
            oOtherWeapon = oWeapon
            break
    
    return oOtherWeapon


def CustomAction13043(oWarrior, oEventCB, dInfo):
    if 'CtrlSkill' not in dInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    oSkillMgr = oWarrior.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(dInfo['CtrlSkill'])
    for oCurSkill in lstSkill:
        if oCurSkill.m_Base['AID'] != oWarrior.m_ID:
            continue
        if oCurSkill.m_Base['Weapon'] != dEventInfo['ItemID']:
            continue
        if 'DamList' not in oCurSkill.m_Collect:
            oCurSkill.m_Collect['DamList'] = []
        lstDam = oCurSkill.m_Collect['DamList']
        iCurVID = dMsgInfo['CurVID']
        if iCurVID not in lstDam:
            lstDam.append(iCurVID)
        dTransInfo['TargetList'] = list(lstDam)
    


def CustomAction4914(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or not dMsgInfo['Skill']:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = dInfo['PerformSID']
    dCurCartoon = oSkill.GetCurCartoon()
    dHitInfo = dCurCartoon.setdefault('p4914HitInfo', { })
    if 'Kill' in dInfo:
        if 'VID' not in dMsgInfo or dMsgInfo['VID'] in dHitInfo:
            return None
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, iFlow = 0):
            cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, iPerform, { }, USEPERFORM_POSTYPE_DEFAULT)
        elif 'CurVID' not in dMsgInfo:
            return None
    if None.CheckHitWeakness(oWarrior, oEventCB, iFlow = 0) and oWarrior.m_Game.Random(100) + 1 <= dInfo['Prob']:
        dHitInfo[dMsgInfo['CurVID']] = 1
        cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, iPerform, { }, USEPERFORM_POSTYPE_DEFAULT)


def CustomAction4930(oWarrior, oEventCB, dInfo):
    if 'CtrlSkill' not in dInfo:
        return None
    iDamageRatio = dInfo['DamageRatio'] if 'DamageRatio' in dInfo else 100
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    sKey = oEventCB.m_Key
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Collect:
        return None
    dCollect = oSkill.m_Collect[sKey]
    oGame = oWarrior.m_Game
    iAttack = oWarrior.m_ID
    for iTarget in dCollect:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            continue
        oReason = cl_object.reason.CStrReason('pf%d' % dInfo['CtrlSkill'], None, {
            'DamType': DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL })
        iDamage = dCollect[iTarget] * iDamageRatio // 100
        dDamage = {
            'AID': iAttack,
            'CurVID': iTarget,
            'MainDam': [
                (iDamage, oReason)],
            'FlowDam': [],
            'RS': oReason,
            'DamFactor': {
                OBJ_VICTIM: { },
                OBJ_ATTACK: { } } }
        oTarget.ReceiveDamage(iAttack, dDamage, iSendMsg = 0)
    


def CustomAction4852(oWarrior, oEventCB, dExtInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    oSkill = oEventCB.GetCBMsgInfo()['Skill']
    iWeapon = oSkill.m_Base['Weapon']
    iItemID = dEventInfo['ItemID']
    if iWeapon != iItemID:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oAttr = oWeapon.m_PrivateAttr['FillTime']
    oAttr.UpdateRefresh(oWeapon, 2)


def CustomAction4885(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    sKey = oEventCB.m_Key
    if sKey not in oSkill.m_Collect:
        return None
    oPerform = oWarrior.GetPerformIfNoThenNew(dInfo['PerformID'])
    lstVictim = []
    lstPos = []
    lstDamage = []
    iRatio = dInfo['Ratio'] if 'Ratio' in dInfo else 100
    for iVictim, dInfo in oSkill.m_Collect[sKey].items():
        iDamage = dInfo['Damage']
        iDamage = int(iDamage * iRatio / 100)
        lstVictim.append(iVictim)
        lstPos.append(dInfo['Pos'])
        lstDamage.append(iDamage)
    
    dData = {
        'vStart': oWarrior.GetCenter(),
        'Custom': {
            'Victim': lstVictim,
            'Pos': lstPos,
            'Damage': lstDamage } }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def CustomAction4965(oWarrior, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    if 'CurHitPos' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iTimes = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_INT)
    if iTimes >= dInfo['MaxTimes']:
        return None
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iWeapon = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    oPerform = oComPerform.GetPerform(dInfo['Perform'])
    if not oPerform:
        return None
    vStart = dMsgInfo['CurHitPos']
    iTarget = lstTar[0]
    dArgs = {
        'StartX': int(vStart[0] * 100),
        'StartY': int(vStart[1] * 100),
        'StartZ': int(vStart[2] * 100),
        'Target': iTarget,
        'Times': iTimes + 1,
        'Victim': dMsgInfo['CurVID'] }
    cl_snetwar.GS2CNotifyStartSkill(oGame, oWarrior.m_PlayerID, dInfo['Perform'], oPerform.m_ID, iWeapon, dArgs)


def CustomAction4966(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    oSkill = oGame.m_SkillMgr.GetSkillBySource(dInfo['Perform'], oWarrior.m_ID, dEventInfo['ItemID'])
    if not oSkill:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVictim = dMsgInfo['CurVID']
    dCollect = oSkill.m_Collect
    sKey = dInfo['Key']
    if sKey not in dCollect:
        dCollect[sKey] = { }
    dRecordData = dCollect[sKey]
    iMax = dInfo['MaxValue']
    if iVictim in dRecordData:
        iTemp = dRecordData[iVictim] + dInfo['AddValue']
    else:
        iTemp = dInfo['AddValue']
    if iMax < iTemp:
        iTemp = iMax
    dRecordData[iVictim] = iTemp

