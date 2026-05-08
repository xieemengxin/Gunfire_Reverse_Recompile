# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_passive.pyc
# RelativePath: clientlogic/cl_evact/ev_passive.pyc
# Source Generated with Decompyle++
# File: ev_passive.pyc (Python 3.6)

from cl_only import Time2Frame, PY_FLAG_DEAD, Functor, SendAlert, ChooseKey, GAME_FRAME, Frame2Time, ShufferList, ChooseMulKeys
from cl_pxlayer import PXMASK_LIVEOBJ
from cl_commondefines import PF_TYPE_INSCRIPTION, TYPE_RELIFE_RELIC, WARRIOR_HERO, DAM_USE_ARMOR, SCENE_EVT_SHAPE_SPHERE, PF_TYPE_RELIC, DAM_USE_SHIELD, SCENE_EVT_SHAPE_RECTANGLE, NWARRIOR_DROP_COOKIES
from cl_commondefines import DAM_USE_ALL, BASEATTR_REFRESH, FIGHT3_KEY_IGNOREKNOCKBACK, CURE_TYPE_PERFORM, DAM_USE_HP, NWARRIOR_DROP_BULLET, PF_TYPE_BULLETCHANGE, PASSIVE_SENDMESSAGE
from cl_commondefines import ATT_SHAPE_SPHERE, OBJ_VICTIM, WARRIOR_MONSTER, OBJ_ATTACK, STATE_TIME_FOREVER, STATE_TIME_LIMIT, DAM_MASK_SIDE, DISABLE_TYPE_STATE, DISABLE_TYPE_RELIC, RELIC_TYPE_CURSE
from cl_commondefines import FIGHT3_KEY_IGNELBEEXECUTED, STATE_DUALWIELD, MINOR_DEBUFF, USEPERFORM_POSTYPE_DEFAULT, USEPERFORM_POSTYPE_CARTOONSTART, USEPERFORM_POSTYPE_CARTOONEND, SKILLCACHE_PARENTACTNUM, WAND_COMP_TYPE_CONDITION
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_object.logging import OtherLog
import cl_formula
import cl_state
import cl_object.reason
import cl_msgcenter
import cl_item
import cl_item.defines as itemdef
import cl_math
import cl_action
import cl_war
import cl_abnormalconf
import cl_perform
import cl_snetwar
import cl_dlcdata
import cl_notify
import cl_reward

def PassiveCallBackChangDam(oWarrior, oEventCB, iChangeDamType, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if iMul:
        iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
    if 'MainDam' not in dMsgInfo:
        return None
    for idx, lstDam in enumerate(dMsgInfo['MainDam']):
        (iDam, oReason) = lstDam
        iDamType = oReason.Query('DamType', 0)
        iDamType &= ~DAM_MASK_SIDE
        if iDamType & iChangeDamType == 0:
            continue
        iDam = iDam * (10000 + iMul) // 10000 + iAdd
        dMsgInfo['MainDam'][idx] = [
            iDam,
            oReason]
    


def PassiveCallBackChangeCure(oWarrior, oEventCB, iChangeCureType, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainCure' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if iMul:
        iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
    for idx, lstCure in enumerate(dMsgInfo['MainCure']):
        (iCure, oReason) = lstCure
        iCureType = oReason.Query('DamType', 0)
        if not iChangeCureType & iCureType:
            continue
        iCure = iCure * (10000 + iMul) // 10000 + iAdd
        dMsgInfo['MainCure'][idx][0] = iCure
    


def PassiveCBChangeWeaponBulletUse(oWarrior, oEventCB, iNewBulletUse):
    
    def ClearChangeWeaponBulletUse(oWarrior, pfobj):
        for iWeapon in lstClear:
            oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oPerformCom = oWeapon.GetComponent('Perform')
            lstAttPerform = oPerformCom.GetAllAttPerform()
            for iAttPerform in lstAttPerform:
                oPerform = oPerformCom.GetPerform(iAttPerform)
                if oPerform:
                    oPerform.ResetBulletUse()
            
            oMinorPerform = oPerformCom.GetPerform(oPerformCom.GetMinorPerform())
            if oMinorPerform:
                oMinorPerform.ResetBulletUse()
        

    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    iOwnPfid = dEventInfo.get('OwnPfid', 0)
    pfobj = oWarrior.GetPerform(iPerform, iItemID, iOwnPfid)
    if not pfobj:
        return None
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    lstWeapon.extend(oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON))
    tHoldType = (itemdef.MAIN_HOLD, itemdef.DEPUTY_HOLD)
    lstAdd = [ oWeapon for oWeapon in lstWeapon if oWeapon.GetComponent('Hold').HoldPos() in tHoldType ]
    lstClear = { }
    for oWeapon in lstAdd:
        oPerformCom = oWeapon.GetComponent('Perform')
        if not oPerformCom:
            continue
        lstAttPerform = oPerformCom.GetAllAttPerform()
        for iAttPerform in lstAttPerform:
            oPerform = oPerformCom.GetPerform(iAttPerform)
            if oPerform:
                oPerform.SetBulletUse(iNewBulletUse)
        
        oMinorPerform = oPerformCom.GetPerform(oPerformCom.GetMinorPerform())
        if oMinorPerform:
            oMinorPerform.SetBulletUse(iNewBulletUse)
    
    if lstAdd:
        lstClear = [ oWeapon.m_ID for oWeapon in lstAdd ]
        pfobj.m_LifeCycle.AddDisableFunc(ClearChangeWeaponBulletUse)


def PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, sAttr, iAdd, iMul):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj or not (pfobj.m_Enable):
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not iItemID and 'ItemID' in dMsgInfo:
        iItemID = dMsgInfo['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    sKey = pfobj.Key()
    dArgs = {
        'Weapon': oWeapon }
    iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo, dArgs)
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo, dArgs)
    oLifeCycle = pfobj.m_LifeCycle
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    elif (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
        oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
    oWeapon.AttrClear(sAttr, sKey)


def PassCBChangeSourceWeaponPerformAttr(oWarrior, oEventCB, iPerformSID, sAttr, iAdd, iMul):
    
    def ClearChange(oWarrior, pfobj):
        oPerform.AttrClear(sAttr, sKey)

    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(dEventInfo['pfid'], iItemID)
    if not pfobj or not (pfobj.m_Enable):
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerformSID)
    if not oPerform:
        return None
    sKey = pfobj.Key()
    iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo)
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo)
    oLifeCycle = pfobj.m_LifeCycle
    if iMul or iAdd:
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        oLifeCycle.AddDisableFunc(ClearChange)
    else:
        oPerform.AttrClear(sAttr, sKey)


def PassiveCBChangeWeaponAttr(oWarrior, oEventCB, sAttr, iAdd, iMul, iFlag, dClassifyTag = None):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    lstAdd = oWarrior.m_WieldCon.GetWeapons(iFlag)
    sKey = pfobj.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo, dEventInfo)
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo, dEventInfo)
    oLifeCycle = pfobj.m_LifeCycle
    if dClassifyTag:
        setClassifyTag = set(dClassifyTag)
    else:
        setClassifyTag = set()
    for oWeapon in lstAdd:
        if setClassifyTag and not (setClassifyTag & set(oWeapon.m_ClassifyTag)):
            continue
        if iMul or iAdd:
            oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
            oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
            continue
        if (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
            oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
        oWeapon.AttrClear(sAttr, sKey)
    


def PassiveCBAddState(oWarrior, oEventCB, iState, iTime, dArgs, iCloseRemove, iUseMsgAID = 0, iCloseFollowSkill = 0):
    
    def RemoveState(oSkill):
        oWarrior.m_State.RemoveItem(oState.m_ID)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dRet = cl_formula.CalArgsFormula(oWarrior, dArgs, dEventInfo, dMsgInfo)
    iPFItem = dEventInfo['ItemID']
    iPerform = dEventInfo['pfid']
    dData = {
        'Item': iPFItem } if iPFItem else { }
    oReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
    if iUseMsgAID:
        iAttack = dMsgInfo['AID'] if 'AID' in dMsgInfo else oWarrior.m_ID
    else:
        iAttack = oWarrior.m_ID
    dArgs = {
        'AID': iAttack,
        'RS': oReason,
        'pfid': iPerform,
        'PFLV': dEventInfo['PFLV'],
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oWarrior, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oWarrior)
    if iCloseRemove:
        oLifeCycle = dEventInfo['LifeCycle']
        iStateID = oState.m_ID
        if oLifeCycle.m_Enable:
            oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
                oWarrior.m_ID: iStateID })
        else:
            oWarrior.m_State.RemoveItem(iStateID)
    if iCloseFollowSkill and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        oSkill.AddEndFunc(RemoveState)


def PassiveAddCustomDamage(oWarrior, oEventCB, iDamage):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['Att'] = iDamage


def PassiveAddTargetStateWithCache(oWarrior, oEventCB, iState, iTime, dArgs, iCloseRemove, iDamageType, bSendSkill = True):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if iCloseRemove and not (oLifeCycle.m_Enable):
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iState:
        iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo)
    elif 'StateSID' in dMsgInfo:
        pass
    
    iState = 0
    if not iState:
        SendAlert('err', '%s事件回调没有状态信息,请检查监听消息是否正确' % oEventCB.m_Key)
        return None
    iTime = Frame2Time(dMsgInfo['DebuffFrame'])
    iPerform = dEventInfo['pfid']
    oReason = dEventInfo['RS']
    if 'StateInfo' in dMsgInfo and 'RS' in dMsgInfo['StateInfo']:
        iSrcDamType = dMsgInfo['StateInfo']['RS'].Query('DamType', 0)
        oReason = oReason.ExtInfo({
            'DamType': iSrcDamType })
    dTargetState = { }
    oGame = oWarrior.m_Game
    dRet = cl_formula.CalArgsFormula(oWarrior, dArgs, dEventInfo, dMsgInfo)
    if bSendSkill:
        oSkill = dMsgInfo['Skill'] if 'Skill' in dMsgInfo else None
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dStateInfo = {
            'AID': oWarrior.m_ID,
            'RS': oReason,
            'pfid': iPerform,
            'PFLV': dEventInfo['PFLV'],
            'arg': dRet }
        if 'StateInfo' in dMsgInfo and 'arg' in dMsgInfo['StateInfo'] and 'Cache' in dMsgInfo['StateInfo']['arg']:
            dStateInfo['arg']['Cache'] = dMsgInfo['StateInfo']['arg']['Cache']
        dStateInfo['arg']['DamFactor'] = {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } }
        if 'AbnormalSourceDam' not in dRet:
            dStateInfo['arg']['AbnormalSourceDam'] = dMsgInfo.get('StateInfo', { }).get('arg', { }).get('AbnormalSourceDam', 0)
        dDebuffInfo = {
            'DebuffTime': iTime,
            'DebuffState': iState,
            'DebuffType': iDamageType }
        dSendData = {
            'Debuff': dDebuffInfo,
            'AID': oWarrior.m_ID,
            'StateInfo': dStateInfo,
            'VID': iTarget,
            'StateSID': iState,
            'RS': oReason }
        if bSendSkill and oSkill:
            dSendData['Skill'] = oSkill
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEDEBUFF, oWarrior, dSendData, iSub = MINOR_DEBUFF)
        iFrame = Time2Frame(dDebuffInfo['DebuffTime'])
        if iFrame <= 0:
            continue
        oState = cl_state.AddState(oTarget, iState, STATE_TIME_LIMIT, iFrame, dStateInfo)
        if not oState:
            continue
        oState.Enable(oTarget)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GOTDEBUFF, oTarget, {
            'StateSID': iState })
        dFinalSendData = {
            'VID': oTarget.m_ID,
            'StateSID': iState,
            'DebuffFrame': iFrame,
            'StateInfo': dStateInfo,
            'RS': oReason,
            'Debuff': dSendData['Debuff'] }
        if bSendSkill and oSkill:
            dFinalSendData['Skill'] = oSkill
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, oWarrior, dFinalSendData, iSub = PASSIVE_SENDMESSAGE)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GOTDEFINALDEBUFF, oTarget, dFinalSendData, iSub = PASSIVE_SENDMESSAGE)
        dTargetState[iTarget] = oState.m_ID
    
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, dTargetState)


def PassiveCBCopyAllAbnormalState(oWarrior, oEventCB, fRadius, iProb, iNearestOnly = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    iPerform = dEventInfo['pfid']
    dData = {
        'Item': iPFItem } if iPFItem else { }
    dBaseState = {
        'AID': oWarrior.m_ID,
        'pfid': iPerform,
        'PFLV': dEventInfo['PFLV'] }
    lstStateSID = list(cl_abnormalconf.g_AllEleAbnormalState.keys())
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            continue
        lstState = []
        for iState in lstStateSID:
            lstState.extend(oTarget.m_State.GetItems(iState))
        
        if not lstState:
            continue
        vPos = oTarget.GetPos()
        lstTarget = []
        lstHit = cl_math.GetAttackTargetList(oGame, oWarrior.m_Scene, ATT_SHAPE_SPHERE, (vPos, fRadius), {
            'Mask': PXMASK_LIVEOBJ,
            'PassID': oTarget.m_ID })
        fMinDis = 999
        oNearest = None
        for iVictim in lstHit:
            oVictim = oGame.GetObject(iVictim)
            if not oVictim or oVictim.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
                continue
            if iNearestOnly:
                fDis = cl_math.CalDistance3D(vPos, oVictim.GetPos())
                if fDis < fMinDis:
                    fMinDis = fDis
                    oNearest = oVictim
                    continue
            if oGame.Random(100) < iProb:
                lstTarget.append(oVictim)
        
        if oNearest:
            lstTarget.append(oNearest)
        if not lstTarget:
            continue
        for oState in lstState:
            iTimeType = oState.m_TimeType
            iFrame = oState.GetRemainTime()
            dCache = oState.GetArgValue('Cache')
            iDam = oState.GetArgValue('AbnormalSourceDam')
            for oVictim in lstTarget:
                dInfo = {
                    'arg': {
                        'AbnormalSourceDam': iDam } }
                if dCache and 'Att' in dCache:
                    dInfo['arg']['Cache'] = {
                        'Att': dCache['Att'] }
                dInfo.update(dBaseState)
                oReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
                dInfo['RS'] = oReason
                oCopyState = cl_state.AddState(oVictim, oState.m_SID, iTimeType, iFrame, dInfo)
                if oCopyState:
                    oCopyState.Enable(oVictim)
            
        
    


def PassiveAddTargetState(oWarrior, oEventCB, iState, iTime, dArgs, iCloseRemove, iUseMsgAID = 0, iCalTimeByTarget = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if iCloseRemove and not (oLifeCycle.m_Enable):
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAddTime = iTime
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        if not iCalTimeByTarget:
            iAddTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo)
        else:
            iTimeType = STATE_TIME_FOREVER
    iPFItem = None['ItemID']
    iPerform = dEventInfo['pfid']
    dTargetState = { }
    oGame = oWarrior.m_Game
    iCache = 1 if 'Cache' in dArgs else 0
    if iUseMsgAID:
        iAttack = dMsgInfo['AID'] if 'AID' in dMsgInfo else oWarrior.m_ID
    else:
        iAttack = oWarrior.m_ID
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if iCalTimeByTarget:
            dTempMsgInfo = dict(dMsgInfo)
            dTempMsgInfo['VID'] = iTarget
            iAddTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dTempMsgInfo)
        dRet = cl_formula.CalArgsFormula(oWarrior, dArgs, dEventInfo, dMsgInfo)
        dData = {
            'Item': iPFItem } if iPFItem else { }
        oReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
        if iCache and 'Skill' in dMsgInfo:
            dRet['Cache'] = { }
            dRet['Cache'].update(dMsgInfo['Skill'].m_Cache)
        dStatArgs = {
            'AID': iAttack,
            'RS': oReason,
            'pfid': iPerform,
            'PFLV': dEventInfo['PFLV'],
            'arg': dRet }
        oState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iAddTime), dStatArgs)
        if not oState:
            continue
        oState.Enable(oTarget)
        dTargetState[iTarget] = oState.m_ID
    
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, dTargetState)


def PassiveCBTargetAddRandomCurseRelicToState(oWarrior, oEventCB, iCount, iTime, iCloseRemove, dExcludeState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dLog = { }
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        setAllCurseRelic = set(oGame.m_WarData.GetAllCurseRelic())
        setCurseRelic = { iKey for iKey in setAllCurseRelic if iKey not in dExcludeState }
        setRelic = set(oTarget.m_RelicCon.GetAllRelicSIDByType(RELIC_TYPE_CURSE))
        setFilter = set()
        for iSID in setRelic:
            if oTarget.m_RelicCon.IsEnabled(iSID):
                setFilter.add(iSID)
        
        setRelic = setCurseRelic - setFilter
        dRelic = { 1: iKey for iKey in setRelic }
        if not dRelic:
            for iRelic in setCurseRelic:
                clsRelic = cl_perform.GetPerformModule(iRelic)
                if not clsRelic:
                    continue
                if 'StateSID' not in clsRelic.m_BaseArgData:
                    continue
                iState = clsRelic.m_BaseArgData['StateSID']
                oState = oTarget.m_State.GetEnableItemBySID(iState)
                if not oState:
                    dRelic[iRelic] = 1
            
            if not dRelic:
                dRelic = { 1: iKey for iKey in setCurseRelic }
        lstRelic = ChooseMulKeys(oGame, dRelic, iCount)
        lstAddState = []
        for iRelic in lstRelic:
            clsRelic = cl_perform.GetPerformModule(iRelic)
            if not clsRelic:
                continue
            if 'StateSID' not in clsRelic.m_BaseArgData:
                continue
            iState = clsRelic.m_BaseArgData['StateSID']
            lstAddState.append(iState)
            PassiveCBAddState(oTarget, oEventCB, iState, iTime, { }, iCloseRemove)
        
        if lstAddState:
            dLog[oTarget.m_PlayerID] = lstAddState
    
    if dLog:
        OtherLog.Debug('%s add curserelicstate %s' % (oGame.m_ID, dLog))


def PassiveAddFollowState(oWarrior, oEventCB, iState, iMainState, dArgs, iCloseRemove, iToTarget = None, iCheckHasFollowState = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if iCloseRemove and not (oLifeCycle.m_Enable):
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMainState = cl_formula.GetResultByData(oWarrior, iMainState, dEventInfo, dMsgInfo)
    dRet = cl_formula.CalArgsFormula(oWarrior, dArgs, dEventInfo, dMsgInfo)
    iPFItem = dEventInfo['ItemID']
    iPerform = dEventInfo['pfid']
    iPerformLv = dEventInfo['PFLV']
    iWarrior = oWarrior.m_ID
    dData = {
        'Item': iPFItem } if iPFItem else { }
    if not iToTarget:
        AddTargetFollowState(oWarrior, oLifeCycle, iWarrior, iPerform, iPerformLv, iState, iMainState, iCloseRemove, dData, dRet, iCheckHasFollowState)
        return None
    oGame = oWarrior.m_Game
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        AddTargetFollowState(oTarget, oLifeCycle, iWarrior, iPerform, iPerformLv, iState, iMainState, iCloseRemove, dData, dRet, iCheckHasFollowState)
    


def AddTargetFollowState(oTarget, oLifeCycle, iAttacker, iPerform, iPerformLv, iState, iMainState, iCloseRemove, dData, dRet, iCheckHasFollowState):
    oMainState = oTarget.m_State.GetItemBySID(iMainState)
    if not oMainState:
        return None
    if iCheckHasFollowState and iState in oMainState.m_FollowState.values():
        return None
    oReason = cl_object.reason.CPerformReason(iPerform, oTarget.m_ID, oTarget.m_SID, oTarget.m_FightType, None, dData)
    dArgs = {
        'AID': iAttacker,
        'RS': oReason,
        'pfid': iPerform,
        'PFLV': iPerformLv,
        'arg': dRet }
    oState = cl_state.AddFollowState(oTarget, oMainState, iState, STATE_TIME_FOREVER, 0, dArgs)
    if not oState:
        return None
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            oTarget.m_ID: oState.m_ID })


def PassiveAddStateTime(oWarrior, oEventCB, iState, iTime, iMaxTime):
    oState = oWarrior.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo, dEventInfo)
    iMaxTime = cl_formula.GetResultByData(oWarrior, iMaxTime, dEventInfo, dMsgInfo, dEventInfo)
    cl_state.AddTime(oState, oWarrior, Time2Frame(iTime), Time2Frame(iMaxTime))


def PassiveReduceStateTime(oWarrior, oEventCB, iState, iTime, iOnce):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo, dEventInfo)
    lstState = oWarrior.m_State.GetItems(iState)
    if not lstState:
        return None
    for oState in lstState:
        if iOnce and 'AlreadyReduceTime' in oState.m_Data:
            continue
        cl_state.AddTime(oState, oWarrior, -Time2Frame(iTime), 20 * GAME_FRAME)
        oState.m_Data['AlreadyReduceTime'] = 1
    


def PassiveDealExtraDamage(oWarrior, oEventCB, iDamage, iDamageType, iMaxDamage, dExtraInfo = None):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    iPerform = dEventInfo['pfid']
    dData = {
        'Item': iPFItem } if iPFItem else { }
    dData['DamType'] = iDamageType
    if dExtraInfo:
        dData.update(dExtraInfo)
    iDamage = cl_formula.GetResultByData(oWarrior, iDamage, dEventInfo, dMsgInfo)
    iMaxDamage = cl_formula.GetResultByData(oWarrior, iMaxDamage, dEventInfo, dMsgInfo)
    if iMaxDamage and iDamage > iMaxDamage:
        iDamage = iMaxDamage
    oReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
    lstDam = [
        iDamage,
        oReason]
    dMsgInfo['FlowDam'].append(lstDam)


def PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, iAdd, iMul, iMask, iTransmit = 0, iClearTransmit = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearTransFactorInState(tStateUseTransFactor, sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    oSkill = dMsgInfo['Skill']
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
            oLifeCycle.AddUniqueDisableFunc('PassiveCBChangeSkillDamFactor', ClearFunc, iCover = 0)


def PassiveCBChangeElementDam(oWarrior, oEventCB, iDamType, dRule):
    dElemenFatctor = oWarrior.m_ElemenFatctor
    for ikey, ivalue in dRule.items():
        dElemenFatctor[iDamType][ikey] = ivalue
    


def PassiveExtBulletUse(oWarrior, oEventCB, iExtBulletUse):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oSkill = dMsgInfo['Skill']
    iExtBulletUse = cl_formula.GetResultByData(oWarrior, iExtBulletUse, dEventInfo, dMsgInfo)
    if 'ExtBulletUse' not in oSkill.m_Collect:
        oSkill.m_Collect['ExtBulletUse'] = 0
    oSkill.m_Collect['ExtBulletUse'] += iExtBulletUse


def PassiveSetFinalBulletUse(oWarrior, oEventCB, iMulBulletUse):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oSkill = dMsgInfo['Skill']
    iMulBulletUse = cl_formula.GetResultByData(oWarrior, iMulBulletUse, dEventInfo, dMsgInfo)
    if 'FinalMulBulletUse' not in oSkill.m_Collect:
        oSkill.m_Collect['FinalMulBulletUse'] = 0
    oSkill.m_Collect['FinalMulBulletUse'] += iMulBulletUse


def PassiveSubPerformCD(oWarrior, oEventCB, iPerform, iTime):
    iColdTime = oWarrior.m_Perform.GetColdTime(iPerform)
    if not iColdTime:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo, dMsgInfo, dEventInfo)
    iTime = Time2Frame(iTime)
    oWarrior.m_Perform.ModifyColdTime(iPerform, -iTime)


def PassiveCBFillBullet(oWarrior, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oBulletContainer = oWarrior.m_BulletCon
    for oWeapon, _ in oWarrior.m_WieldCon.GetHoldWeapon():
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        iAmount = oBulletCom.MaxBullet() - oBulletCom.Bullet()
        iBulletSID = oBulletCom.BulletType()
        iHasBullet = oBulletContainer.Bullet(iBulletSID)
        if oWeapon.m_Type != EQUIP_TYPE_FUNDAMENTALWEAPON:
            iAmount = min(iAmount, iHasBullet)
            oBulletContainer.BulletModify(iBulletSID, -iAmount, 'fillbullet')
        iSend = 0 if dEventInfo['PFType'] == PF_TYPE_BULLETCHANGE else 1
        oBulletCom.BulletModify(iAmount, iSend)
    


def PassiveCBFillSourceWeaponBullet(oWarrior, oEventCB, iFillValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iFillValue = cl_formula.GetResultByData(oWarrior, iFillValue, dEventInfo, dMsgInfo)
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    iBulletSID = oBulletCom.BulletType()
    iBagBullet = oWarrior.m_BulletCon.Bullet(iBulletSID)
    iFillValue = min(iFillValue, iBagBullet, iMaxBullet - iNowBullet)
    if iFillValue <= 0:
        return None
    oWarrior.m_BulletCon.BulletModify(iBulletSID, -iFillValue, 'fillbullet')
    iSend = 0 if dEventInfo['PFType'] == PF_TYPE_BULLETCHANGE else 1
    oBulletCom.BulletModify(iFillValue, iSend)


def PassiveCBFillEventBullet(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_BULLET:
        return None
    dBullet = dMsgInfo['Item']
    lstRemove = []
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        for iBulletSID, iAmount in dBullet.items():
            if iAmount <= 0 or oBulletCom.BulletType() != iBulletSID:
                continue
            iNeed = oBulletCom.MaxBullet() - oBulletCom.Bullet()
            iUsed = min(iNeed, iAmount)
            dBullet[iBulletSID] -= iUsed
            oBulletCom.BulletModify(iUsed)
            if dBullet[iBulletSID] <= 0:
                lstRemove.append(iBulletSID)
        
    
    for iBulletSID in lstRemove:
        if iBulletSID in dBullet:
            dBullet.pop(iBulletSID)
    


def PassiveCBChangeBulletWieldType(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_BULLET:
        return None
    dBullet = dMsgInfo['Item']
    oBulletCon = oWarrior.m_BulletCon
    if oWarrior.m_State.GetItemBySID(STATE_DUALWIELD):
        lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
        fMinRadio = 1
        oBulletCom = None
        for oWeapon in lstWeapon:
            oTmpBulletCom = oWeapon.GetComponent('Bullet')
            if not oTmpBulletCom:
                continue
            iTransBulletSID = oTmpBulletCom.BulletType()
            fRadio = oBulletCon.Bullet(iTransBulletSID) / oBulletCon.GetMaxBullet(iTransBulletSID)
            if fRadio <= fMinRadio:
                fMinRadio = fRadio
                oBulletCom = oTmpBulletCom
        
        if not oBulletCom:
            return None
    oCurWeapon = oWarrior.m_WieldCon.GetCurWeapon()
    if not oCurWeapon:
        return None
    oBulletCom = oCurWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iTransBulletSID = oBulletCom.BulletType()
    iMaxTrans = oBulletCon.GetMaxBullet(iTransBulletSID) - oBulletCon.Bullet(iTransBulletSID)
    iMaxTrans += oBulletCom.MaxBullet() - oBulletCom.Bullet()
    iTransCnt = 0
    oThrowPerform = oWarrior.GetThrowPerform()
    iThrowBulletSID = oThrowPerform.CalAttr('BulletSID')
    lstRemove = []
    for iBulletSID, iCnt in dBullet.items():
        if iBulletSID == iThrowBulletSID:
            continue
        iTmpCnt = min(iMaxTrans, iCnt)
        iTransCnt += iTmpCnt
        iMaxTrans -= iTmpCnt
        if iBulletSID == iTransBulletSID:
            continue
        if iCnt <= iTmpCnt:
            lstRemove.append(iBulletSID)
            continue
        dBullet[iBulletSID] = iCnt - iTmpCnt
    
    for iBulletSID in lstRemove:
        dBullet.pop(iBulletSID)
    
    dBullet[iTransBulletSID] = iTransCnt


def PassiveAddHoldWeaponBagBullet(oWarrior, oEventCB, iAmount, iClientBehavior):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for oWeapon, _iHoldPos in oWarrior.m_WieldCon.GetHoldWeapon():
        iAddAmount = cl_formula.GetResultByData(oWarrior, iAmount, dEventInfo, dMsgInfo, {
            'Weapon': oWeapon })
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        iBulletSID = oBulletCom.BulletType()
        iBagBullet = oWarrior.m_BulletCon.Bullet(iBulletSID)
        iMaxBagBullet = oWarrior.m_BulletCon.GetMaxBullet(iBulletSID)
        if iBagBullet + iAddAmount > iMaxBagBullet:
            iAddAmount = iMaxBagBullet - iBagBullet
        if not iAddAmount:
            continue
        oWarrior.m_BulletCon.BulletModify(iBulletSID, iAddAmount, sKey)
    
    if iClientBehavior:
        cl_snetwar.GS2CTriggerBehavior(oWarrior.m_Game, oWarrior.m_ID, iClientBehavior, [
            oWarrior.m_PlayerID], 0)


def PassiveReduceFillBulletUse(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect['NoFillBulletUse'] = 1


def PassiveCureByFinalDam(oWarrior, oEventCB, iCureFactor, dArgs, iShowTips):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return None
    lstDamage = dMsgInfo['TrueChange']
    iTotalCure = 0
    dEventInfo = oEventCB.GetCBEventInfo()
    for iTrueChange, oReason in lstDamage:
        iDamType = oReason.Query('DamType')
        iFactor = iCureFactor
        for iExtDamType, iExtFactor in dArgs.items():
            if iDamType & iExtDamType == iExtDamType:
                iFactor = iExtFactor
                break
        
        iCure = iTrueChange * iFactor // 10000
        iTotalCure += iCure
    
    if not iTotalCure:
        return None
    iPerform = dEventInfo['pfid']
    dData = {
        'ShowTips': iShowTips,
        'DamType': CURE_TYPE_PERFORM | DAM_USE_HP }
    oMainReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
    lstMainCure = [
        [
            iTotalCure,
            oMainReason]]
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        dPerform = {
            'MainCure': lstMainCure,
            'FlowCure': [],
            'RS': oMainReason }
        oTarget.ReceiveCure(oTarget.m_ID, dPerform)
    


def PassiveSetStateCount(oWarrior, oEventCB, iState, iCount):
    oState = oWarrior.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dArgs = { }
    if 'Weapon' in dMsgInfo:
        oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['Weapon'])
        if oWeapon:
            dArgs['Weapon'] = oWeapon
    dEventInfo = oEventCB.GetCBEventInfo()
    iCount = cl_formula.GetResultByData(oWarrior, iCount, dEventInfo, dMsgInfo, dArgs)
    iNowCount = oState.GetCount()
    iAddCount = iCount - iNowCount
    oState.AddCount(oWarrior, iAddCount)


def PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, iState, iCount):
    lstState = oWarrior.m_State.GetItems(iState)
    if not lstState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    if not iPFItem:
        return None
    iCount = cl_formula.GetResultByData(oWarrior, iCount, dEventInfo, dMsgInfo)
    for oState in lstState:
        iStateItem = oState.m_Item
        if iStateItem == iPFItem:
            oState.AddCount(oWarrior, iCount)
    


def PassiveCBAddTargetStateCount(oWarrior, oEventCB, iState, iCount, iFromSelf = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iCount = cl_formula.GetResultByData(oWarrior, iCount, dEventInfo, dMsgInfo)
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if not iFromSelf:
            oState = oTarget.m_State.GetItemBySID(iState)
            if not oState:
                return None
            oState.AddCount(oTarget, iCount)
            continue
        lstState = oTarget.m_State.GetItems(iState)
        for oState in lstState:
            iAttacker = oState.m_Attacker
            if iAttacker != oWarrior.m_ID:
                continue
            oState.AddCount(oTarget, iCount)
        
    


def PassiveCBPullVictimToPos(oWarrior, oEventCB, fSpeed, fMaxDis):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    iVictim = oSkill.m_Update['CurVID']
    oGame = oWarrior.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
        return None
    if oVictim.CheckLogicKey(FIGHT3_KEY_IGNOREKNOCKBACK):
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'EPFPos' not in dTrans:
        raise Exception('未设置位置')
    vEnd = dTrans['EPFPos']
    vTar = oVictim.GetPos()
    fCurDis = cl_math.CalDistance3D(vTar, vEnd)
    fDis = min(fCurDis, fMaxDis)
    fSecondOut = fDis / fSpeed
    vDir = cl_math.Vec3Minus(vEnd, vTar)
    if oVictim.m_MoveCtrl:
        oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fSecondOut)


def PassiveChangeAttr(oWarrior, oEventCB, sAttr, iAdd, iMul):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iMul:
        iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    sKey = pfobj.Key()
    pfobj.m_LifeCycle.m_Apply[sAttr] = 1
    oWarrior.AttrChange(sAttr, iMul, iAdd, sKey)


def PassiveSetPosToBead(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTrans = oEventCB.GetCBTransInfo()
    if 'DropPos' not in dMsgInfo:
        return None
    dTrans['EPFPos'] = dMsgInfo['DropPos']


def PassiveSetPosToTargetPos(oWarrior, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    oTarget = oWarrior.m_Game.GetObject(lstTar[0])
    if not oTarget:
        return None
    dTrans['EPFPos'] = oTarget.GetPos()


def PassiveSetPosToCartoon(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTrans = oEventCB.GetCBTransInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dInfo = oSkill.m_Update
    if 'CurPos' in dInfo:
        dTrans['EPFPos'] = dInfo['CurPos']
    elif 'End' in dInfo:
        dTrans['EPFPos'] = dInfo['End']
    elif 'EPFPos' in dInfo:
        dTrans['EPFPos'] = dInfo['EPFPos']


def PassiveSetPosToSkillCollect(oWarrior, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Collect:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    dTrans['EPFPos'] = oSkill.m_Collect[sKey]


def PassiveCBAddSceneEvent(oWarrior, oEventCB, iTime, iShape, dEffArgs, iYOffset, iEnterGroup, iLeaveGroup):
    
    def ClearSceneEvt(oGame, iScene):
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oScene.RemoveSceneEvent(iSceneEvtID)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEvent = oEventCB.GetCBEventInfo()
    dData = {
        'AID': oWarrior.m_ID,
        'RS': oSkill.m_Base['RS'] }
    dData.update(oSkill.m_Cache)
    dTrans = oEventCB.GetCBTransInfo()
    if 'EPFPos' not in dTrans:
        raise Exception('未设置位置')
    (x, y, z) = dTrans['EPFPos']
    y += iYOffset
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        lstArgs = [
            (x, y, z),
            dEffArgs['Radius']]
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        lstArgs = [
            (x, y, z),
            (dEffArgs['HalfX'], dEffArgs['HalfY'], dEffArgs['HalfZ'])]
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    (enterfunc, leavefunc) = (None, None)
    if iEnterGroup:
        enterfunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iEnterGroup, dEvent)
    if iLeaveGroup:
        leavefunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iLeaveGroup, dEvent)
    iSceneEvtID = oScene.AddSceneEvent(oWarrior, enterfunc, leavefunc, iShape, lstArgs, dData)
    oGame.m_Timer.Call_Out(Functor(ClearSceneEvt, oGame, iScene), Time2Frame(iTime), 'PassiveCBClearSceneEvt')


def PassiveCBRemoveTargetState(oWarrior, oEventCB, iStateSID, iClearAll = 0, iFromPF = 0, iFromSelf = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    for iTarget in dTrans['TargetList']:
        oTarget = oWarrior.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iClearAll:
            lstStateObj = oTarget.m_State.GetItems(iStateSID)
            for oState in lstStateObj:
                if not oState:
                    continue
                oTarget.m_State.RemoveItem(oState.m_ID)
            
        if iFromPF or iFromSelf:
            lstStateObj = oTarget.m_State.GetItems(iStateSID)
            for oState in lstStateObj:
                if iFromPF:
                    if 'pfid' in oState.m_StateInfo:
                        pass
                    if not (oState.m_StateInfo['pfid'] == iFromPF):
                        continue
                    continue
                if iFromSelf and oState.m_Attacker != oWarrior.m_ID:
                    continue
                oTarget.m_State.RemoveItem(oState.m_ID)
            
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if not oState:
            continue
        oTarget.m_State.RemoveItem(oState.m_ID)
    


def PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.m_State.RemoveItemBySource(iState, oWarrior.m_ID)
    


def PassiveCBRemoveStateFromSameItem(oWarrior, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iItem = dEventInfo['ItemID']
    oGame = oWarrior.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetStateBySource(iState, 0, iItem)
        if oState:
            oTarget.m_State.RemoveItem(oState.m_ID)
    


def PassiveCBSettleStateDelayDamage(oWarrior, oEventCB, iStateSID, iPerDamage, iDamageType):
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    iVictim = oSkill.m_Update['CurVID']
    oTarget = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oTarget:
        return None
    oStateCon = oTarget.m_State
    oTargetState = oStateCon.GetItemBySID(iStateSID)
    if not oTargetState or 'delay' not in oTargetState.m_DelayAction:
        return None
    iTotalDamage = 0
    iIntervalFrame = Time2Frame(oTargetState.m_DelayAction['delay'])
    iStateFirstFrame = -1
    iPreStateStartFrame = 0
    lstState = oStateCon.m_StateBySid[iStateSID][:]
    for _ in range(len(lstState)):
        oState = None
        lstRemove = []
        for oTmpState in lstState:
            if not oTmpState:
                continue
            if oTmpState.m_TimeType == STATE_TIME_LIMIT and oTmpState.GetRemainTime() <= 0:
                lstRemove.append(oTmpState)
                oTmpState.Disable(oTarget, 0)
                oStateCon.RemoveItem(oTmpState.m_ID)
                continue
            if not oState:
                oState = oTmpState
                continue
            if oTmpState.CheckHighAttr(oTarget, oState):
                oState = oTmpState
        
        if not oState:
            break
        for oRemoveState in lstRemove:
            lstState.remove(oRemoveState)
        
        if iStateFirstFrame == -1:
            iNextFrame = oState.CalNextDelay(0)
            iRemainFrame = oState.GetRemainTime()
        else:
            iNextFrame = iStateFirstFrame
            iRemainFrame = oState.m_StartTime + oState.m_Time - iPreStateStartFrame
        iRestFrame = iRemainFrame - iNextFrame
        iTimes = iRestFrame // iIntervalFrame
        if iNextFrame < iRemainFrame:
            iTimes += 1
        if iRestFrame >= iIntervalFrame and iRestFrame % iIntervalFrame == 0:
            iTimes -= 1
        if iTimes > 0:
            iTotalDamage += cl_formula.GetResultByData(oTarget, iPerDamage, oState.AttrCache()) * iTimes
        iStateFirstFrame = iIntervalFrame - iRestFrame % iIntervalFrame
        iPreStateStartFrame = oState.m_StartTime + oState.m_Time
        oState.Disable(oTarget, 0)
        oStateCon.RemoveItem(oState.m_ID)
        lstState.remove(oState)
        if not lstState:
            break
    
    if not iTotalDamage:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iDamageType |= DAM_USE_ALL
    dData = {
        'Item': dEventInfo['ItemID'],
        'DamType': iDamageType,
        'ShowTips': 1 }
    oReason = cl_object.reason.CPerformReason(dEventInfo['pfid'], oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, dData)
    lstDam = [
        iTotalDamage,
        oReason]
    dMsgInfo['FlowDam'].append(lstDam)


def PassiveCBSetAttackIgnoreShield(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    for lstDam in dMsgInfo['MainDam']:
        (iDam, oReason) = lstDam
        iDamType = oReason.Query('DamType', 0)
        iDamType &= ~DAM_USE_SHIELD
        lstDam[1] = oReason.ExtInfo({
            'DamType': iDamType })
    


def PassiveCBAddSourceWeaponBagBullet(oWarrior, oEventCB, iAmount):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = dEventInfo['pfid']
    iItem = dEventInfo['ItemID']
    oUsePF = oWarrior.GetPerform(iPerform, iItem)
    if not oUsePF:
        return None
    oWeapon = oUsePF.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & cl_item.EQUIP_MASK_WEAPON):
        return None
    iAddAmount = cl_formula.GetResultByData(oWarrior, iAmount, dEventInfo, dMsgInfo, {
        'Weapon': oWeapon })
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iBulletSID = oBulletCom.BulletType()
    oWarrior.m_BulletCon.BulletModify(iBulletSID, iAddAmount, sKey)


def PassiveCBAddWeaponBagBullet(oWarrior, oEventCB, iAmount):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItemID = dEventInfo['ItemID']
    if not iItemID and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItemID = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    iAddAmount = cl_formula.GetResultByData(oWarrior, iAmount, dEventInfo, dMsgInfo, {
        'Weapon': oWeapon })
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iBulletSID = oBulletCom.BulletType()
    oWarrior.m_BulletCon.BulletModify(iBulletSID, iAddAmount, sKey)


def PassiveCBUsePerform(oWarrior, oEventCB, iPerform, bInherit, dInfo = None):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    if not iPFItem:
        oPerform = oWarrior.m_Perform.GetPerform(iPerform)
        if not oPerform:
            oWarrior.AddPerform(iPerform, 1)
    oPerform = oWarrior.GetPerform(iPerform, iPFItem)
    if not oPerform:
        return None
    dCustom = { }
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if bInherit and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dCustom['dCache'] = dict(oSkill.m_Cache)
    if dInfo:
        dInfo = cl_formula.CalArgsFormula(oWarrior, dInfo, dEventInfo, dMsgInfo)
        dCustom.update(dInfo)
    dData = {
        'Custom': dCustom }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, iPerform, dData, iChoosePosType = USEPERFORM_POSTYPE_DEFAULT):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = dEventInfo['ItemID']
    oPerform = oWarrior.GetPerform(iPerform, iPFItem)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    for sKey, lstFormula in dData.items():
        if isinstance(lstFormula, dict):
            dData[sKey] = lstFormula
            continue
        iRet = cl_formula.GetResultByData(oWarrior, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    dPerform = {
        'Custom': dData }
    oSkill = dMsgInfo['Skill']
    if iChoosePosType == USEPERFORM_POSTYPE_DEFAULT:
        if 'DirectHitCurPos' in oSkill.m_Collect:
            vCurPos = oSkill.m_Collect['DirectHitCurPos']
        elif 'CurHitPos' in oSkill.m_Update:
            vCurPos = oSkill.m_Update['CurHitPos']
        else:
            dCartoon = oSkill.GetCurCartoon()
            vCurPos = dCartoon['CurPos']
    elif iChoosePosType == USEPERFORM_POSTYPE_CARTOONSTART:
        dCartoon = oSkill.GetCurCartoon()
        vCurPos = dCartoon['Start']
    elif iChoosePosType == USEPERFORM_POSTYPE_CARTOONEND:
        dCartoon = oSkill.GetCurCartoon()
        vCurPos = dCartoon['End']
    dPerform['Custom']['vEnd'] = vCurPos
    cl_war.UsePerform(oWarrior, oPerform, dPerform)


def PassiveCBCalPFRelifeTimes(oWarrior, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    pfobj = oWarrior.GetPerform(iPerform)
    if pfobj.m_PFType == PF_TYPE_RELIC:
        sKey = pfobj.m_LifeCycle.GetStableKey()
        iLeftTimes = oWarrior.GetRelifeTimes(TYPE_RELIFE_RELIC, sKey)
        if not iLeftTimes:
            oWarrior.ClearRelifeInfo(TYPE_RELIFE_RELIC, sKey)
            oWarrior.m_RelicCon.RemoveRelic(iPerform, 'passiveCBRemoveRelic', 1)
            if oWarrior.m_FightType & WARRIOR_HERO:
                lstPlayer = [
                    oWarrior.m_PlayerID]
                cl_notify.SendCommonNotify(oWarrior.m_Game, lstPlayer, 2418, {
                    '$name': pfobj.m_Name })


def PassiveFillBullet(oWarrior, oEventCB, iFillValue, iClientBehavior):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItemID = dEventInfo['ItemID']
    if not iItemID and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItemID = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    if iNowBullet >= iMaxBullet:
        return None
    iFillValue = cl_formula.GetResultByData(oWarrior, iFillValue, dEventInfo, dMsgInfo, {
        'Weapon': oWeapon })
    if iNowBullet + iFillValue > iMaxBullet:
        iFillValue = iMaxBullet - iNowBullet
    iSend = 0 if dEventInfo['PFType'] == PF_TYPE_BULLETCHANGE else 1
    oBulletCom.BulletModify(iFillValue, iSend)
    if iClientBehavior:
        cl_snetwar.GS2CTriggerBehavior(oWarrior.m_Game, oWarrior.m_ID, iClientBehavior, [
            oWarrior.m_PlayerID], 0)


def PassiveCBSetCollectInfo(oWarrior, oEventCB, sAttr, iAdd, iMul):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iOldValue = 0
    if sAttr in oSkill.m_Collect:
        iOldValue = oSkill.m_Collect[sAttr]
    if iMul:
        iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
    iValue = iOldValue * (10000 + iMul) // 10000 + iAdd
    oSkill.m_Collect[sAttr] = iValue


def PassiveCBSetCollectHitNumInfo(oWarrior, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or 'CurVID' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    sAttrList = str(sAttr) + 'list'
    if sAttrList not in oSkill.m_Collect:
        oSkill.m_Collect[sAttrList] = { }
    oSkill.m_Collect[sAttrList][dMsgInfo['CurVID']] = 1
    oSkill.m_Collect[sAttr] = len(oSkill.m_Collect[sAttrList])


def PassiveCBSetValidCartoon(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    oSkill = dMsgInfo['Skill']
    dCartoon = oSkill.GetCurCartoon()
    if not dCartoon:
        return None
    dValid = oSkill.m_Collect['ValidCartoon'] if 'ValidCartoon' in oSkill.m_Collect else { }
    dValid[sKey] = dCartoon['ID']
    oSkill.m_Collect['ValidCartoon'] = dValid


def PassiveChangeMiniGameInfo(oWarrior, oEventCB, iRatioMul, iRatioAdd, iTimesMul, iTimesAdd, iCalOverflowTimes = 0, iChangeZeroRatio = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Ratio' not in dMsgInfo or 'OriTimes' not in dMsgInfo:
        return None
    iRatio = dMsgInfo['Ratio']
    if iRatio <= 0 and not iChangeZeroRatio:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iRatioMul = cl_formula.GetResultByData(oWarrior, iRatioMul, dEventInfo)
    iRatioAdd = cl_formula.GetResultByData(oWarrior, iRatioAdd, dEventInfo)
    iTimesMul = cl_formula.GetResultByData(oWarrior, iTimesMul, dEventInfo)
    iTimesAdd = cl_formula.GetResultByData(oWarrior, iTimesAdd, dEventInfo)
    iOriTimes = dMsgInfo['OriTimes']
    iRatio += iRatio * iRatioMul // 10000 + iRatioAdd
    iOriTimes += iOriTimes * iTimesMul // 10000 + iTimesAdd
    dMsgInfo['Ratio'] = iRatio
    dMsgInfo['OriTimes'] = iOriTimes
    if iCalOverflowTimes and iRatio > 10000:
        iOverflowTimes = (iRatio // 10000 - 1) * iOriTimes
        iRemainRatio = iRatio % 10000
        for _ in range(iOriTimes):
            if oWarrior.m_Game.Random(10000) < iRemainRatio:
                iOverflowTimes += 1
        
        dMsgInfo['OverflowTimes'] = iOverflowTimes


def PassiveCBClearWeaponForceAttr(oWarrior, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo and dMsgInfo['Skill'].m_Base['Weapon']:
        iItem = dMsgInfo['Skill'].m_Base['Weapon']
    else:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItem)
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    oWeapon.ItemAttrForceClear(sAttr, sKey)


def PassiveCBSetWeaponForceAttr(oWarrior, oEventCB, sAttr, iValue, iFlag, iSourceOnly = 0):
    
    def ClearWeaponForceAttr(oWarrior, pfobj):
        sKey = pfobj.Key()
        for iWeapon in lstClear:
            oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oWeapon.ItemAttrForceClear(sAttr, sKey)
        

    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    lstWeapon = oWarrior.m_WieldCon.GetWeapons(iFlag)
    sKey = pfobj.Key()
    dData = pfobj.AttrCache()
    iValue = cl_formula.GetResultByData(oWarrior, iValue, dData)
    lstAdd = []
    for oWeapon in lstWeapon:
        if iSourceOnly and iItemID != oWeapon.m_ID:
            continue
        oWeapon.ItemAttrForceSet(sAttr, iValue, sKey)
        lstAdd.append(oWeapon)
    
    if lstAdd:
        lstClear = [ oWeapon.m_ID for oWeapon in lstAdd ]
        pfobj.m_LifeCycle.AddDisableFunc(ClearWeaponForceAttr)


def PassiveCBSetAttackIgnoreArmor(oWarrior, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    for lstDam in dMsgInfo['MainDam']:
        (iDam, oReason) = lstDam
        iDamType = oReason.Query('DamType', 0)
        iDamType &= ~DAM_USE_ARMOR
        lstDam[1] = oReason.ExtInfo({
            'DamType': iDamType })
    


def PassiveCBDisableSelf(oWarrior, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if pfobj:
        pfobj.Disable(oWarrior)


def PassiveCBSetPFArgs(oWarrior, oEventCB, sArgs, val):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    val = cl_formula.GetResultByData(oWarrior, val, dEventInfo, dMsgInfo)
    pfobj.SetArgValue(sArgs, val)


def PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, key, val):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    key = cl_formula.GetResultByData(oWarrior, key, dEventInfo, dMsgInfo)
    val = cl_formula.GetResultByData(oWarrior, val, dEventInfo, dMsgInfo)
    pfobj.SetArgValue(key, val)


def PassiveCBAddPFArgs(oWarrior, oEventCB, sArgs, val):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oPerform = oLifeCycle.GetObject()
    if not oPerform:
        return None
    val = cl_formula.GetResultByData(oWarrior, val, dEventInfo, dMsgInfo)
    oPerform.AddArgValue(sArgs, val)


def PassiveCBAddPFArgsValue(oWarrior, oEventCB, iKey, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo)
    pfobj.AddArgValue(iKey, iAdd)


def PassiveCBSetPFArgsNoFormula(oWarrior, oEventCB, sArgs, val):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    pfobj.SetArgValue(sArgs, val)


def PassiveCBClearWeaponAttrTimes(oWarrior, oEventCB, sAttr):
    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oWeapon.Set(sAttr, [])


def PassiveCBDisableRelicByType(oWarrior, oEventCB, iType, iAddCon):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dPerform = { }
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' in dMsgInfo:
        iRelic = dMsgInfo['iPerform']
        iAddingRelicType = cl_perform.GetPerformClassAttr(iRelic, 'm_RelicType')
        if iAddingRelicType == iType:
            dMsgInfo['Enable'] = 0
            dPerform[iRelic] = 1
    if iAddCon:
        oRelicCon = oWarrior.m_RelicCon
        sDisableKey = oEventCB.m_Key
        for oPerform in oRelicCon.GetAllRelicByType(iType):
            oPerform.SetDisableSource(sDisableKey)
            oPerform.Disable(oWarrior)
            dPerform[oPerform.m_SID] = 1
        
    if dPerform:
        pfobj.m_LifeCycle.AddDisableType(DISABLE_TYPE_RELIC, dPerform)


def PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, iPerform, iAssignEndPos = 0, dCustomData = None, iObjectType = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if iObjectType:
        oAttack = oWarrior.GetOwnObject(iObjectType)
        if not oAttack:
            return None
    oAttack = oWarrior
    if not oAttack.GetPerform(iPerform):
        oAttack.AddPerform(iPerform, 1)
    oPerform = oAttack.GetPerform(iPerform)
    oGame = oAttack.m_Game
    dCustom = { }
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SkillCustom' in dMsgInfo:
        dCustom = dMsgInfo['SkillCustom']
    iGetVictimPos = 0
    if iAssignEndPos:
        if 'CurHitPos' in dMsgInfo:
            dCustom['vEnd'] = dMsgInfo['CurHitPos']
        else:
            iGetVictimPos = 1
    if dCustomData:
        dEventInfo = oEventCB.GetCBEventInfo()
        dCustomData = cl_formula.CalArgsFormula(oAttack, dCustomData, dEventInfo, dMsgInfo)
        dCustom.update(dCustomData)
    for iVictim in dTrans['TargetList']:
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            continue
        if iGetVictimPos:
            if 'HalfHeight' in dCustom and dCustom['HalfHeight']:
                dCustom['vEnd'] = oVictim.GetCenter()
            else:
                dCustom['vEnd'] = oVictim.GetPos()
        dData = {
            'Custom': dCustom }
        dData['VID'] = iVictim
        cl_war.UsePerform(oAttack, oPerform, dData)
    


def PassiveCBOwnerUsePerform2EvtTarget(oWarrior, oEventCB, iPerform, iAssignEndPos, dCustomData):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iOwner = oWarrior.m_Owner
    if not iOwner:
        return None
    oOwner = oWarrior.m_Game.GetObject(iOwner)
    if not oOwner:
        return None
    oPerform = oOwner.GetPerform(iPerform)
    if not oPerform:
        oPerform = oOwner.AddPerform(iPerform, 1)
    oGame = oOwner.m_Game
    dCustom = { }
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SkillCustom' in dMsgInfo:
        dCustom = dMsgInfo['SkillCustom']
    if iAssignEndPos and 'CurHitPos' in dMsgInfo:
        dCustom['vEnd'] = dMsgInfo['CurHitPos']
    dCustom.update(dCustomData)
    for iVictim in dTrans['TargetList']:
        dData = {
            'Custom': dCustom }
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            continue
        dData['VID'] = iVictim
        cl_war.UsePerform(oOwner, oPerform, dData)
    


def PassiveCBHitWeaknessUsePerform(oWarrior, oEventCB, iPerform, iRatio = 100):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return None
    oVictim = oWarrior.m_Game.GetObject(iVictim)
    if not oWarrior.GetPerform(iPerform):
        oWarrior.AddPerform(iPerform, 1)
    oPerform = oWarrior.GetPerform(iPerform)
    iDamage = 0
    for lstDam in dMsgInfo['MainDam']:
        iDamage += lstDam[0]
    
    iDamage = iDamage * iRatio // 100
    tPos = dMsgInfo['CurHitPos'] if 'CurHitPos' in dMsgInfo else oVictim.GetPos()
    dData = {
        'vStart': tPos,
        'Custom': {
            'LockTrigger': oVictim.m_ID,
            'TransmitAtt': iDamage } }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def PassiveCBUsePerformWithMonsterCenter(oWarrior, oEventCB, iPerform, tPos, iRatio = 100):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return None
    oVictim = oWarrior.m_Game.GetObject(iVictim)
    if not oVictim:
        return None
    iDamage = 0
    if 'PredictChange' in dMsgInfo:
        iDamage += sum(dMsgInfo['PredictChange'])
    vPos = oVictim.GetPos()
    vPos = (vPos[0] + tPos[0], vPos[1] + tPos[1] + oVictim.m_ModelHeight / 2, vPos[2] + tPos[2])
    dData = {
        'vStart': vPos,
        'Custom': {
            'TransmitAtt': iDamage * iRatio // 100 } }
    oPerform = oWarrior.GetPerformIfNoThenNew(iPerform)
    cl_war.UsePerform(oWarrior, oPerform, dData)


def PassiveCBUsePerformWithKillMonster(oWarrior, oEventCB, iPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return None
    iAttack = dMsgInfo['AID']
    oAttack = oWarrior.m_Game.GetObject(iAttack)
    if not oAttack:
        return None
    oPerform = oAttack.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    dData = {
        'vStart': oWarrior.GetPos(),
        'Custom': { } }
    if oAttack.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    lstAdd = oAttack.m_WieldCon.GetWeapons(itemdef.MAIN_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        iCrazyEff = oWeapon.QueryAttr('CrazyEff')
        dData['Custom']['CrazyEff'] = iCrazyEff / 10000
    
    if 'TotalDam' in dMsgInfo:
        dData['Custom']['Damage'] = sum(dMsgInfo['TotalDam'])
    if 'FinalDam' in dMsgInfo:
        dData['Custom']['Damage'] = dMsgInfo['FinalDam']
    cl_war.UsePerform(oAttack, oPerform, dData)


def PassiveCBAttackerUsePerform(oWarrior, oEventCB, iPerform, iRatio):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return None
    iAttack = dMsgInfo['AID']
    oAttacker = oWarrior.m_Game.GetObject(iAttack)
    if not oAttacker:
        return None
    if not oAttacker.GetPerform(iPerform):
        oAttacker.AddPerform(iPerform, 1)
    oPerform = oAttacker.GetPerform(iPerform)
    iDamage = 0
    for lstDam in dMsgInfo['MainDam']:
        iDamage += lstDam[0]
    
    iDamage = iDamage * iRatio // 100
    tPos = oWarrior.GetPos()
    if 'CurHitPos' in dMsgInfo:
        tPos = dMsgInfo['CurHitPos']
    dData = {
        'vStart': tPos,
        'Custom': {
            'TransmitAtt': iDamage } }
    cl_war.UsePerform(oAttacker, oPerform, dData)


def PassiveCBGetRandomWeapon(oWarrior, oEventCB, dWeaponInfo, dWeightInfo):
    oGame = oWarrior.m_Game
    dValid = oWarrior.Query('Illus')['Weapon']
    dChooseWeaponInfo = { }
    dWeapon2Dlc = cl_dlcdata.GetWeapon2Dlc()
    for indx, sWeapnInfo in dWeaponInfo.items():
        lstCheckWeaponInfo = sWeapnInfo.split('|')
        iSID = int(lstCheckWeaponInfo[0])
        if iSID in dWeapon2Dlc and iSID not in dValid:
            dWeightInfo.pop(indx)
            continue
        dChooseWeaponInfo[indx] = lstCheckWeaponInfo
    
    if not dWeightInfo:
        SendAlert('err', '%s事件可抽取武器数不足，请检查对应配置' % oEventCB.m_Key)
        return None
    iWeaponInfo = ChooseKey(oGame, dWeightInfo)
    lstWeaponInfo = dChooseWeaponInfo[iWeaponInfo]
    for i in range(len(lstWeaponInfo)):
        lstWeaponInfo[i] = int(lstWeaponInfo[i])
    
    lstInscription = lstWeaponInfo[3:]
    iSID = lstWeaponInfo[0]
    iGrade = lstWeaponInfo[1]
    iInscriptionNum = lstWeaponInfo[2]
    clsEquip = cl_item.GetItemCls(iSID)
    if not clsEquip:
        return None
    if clsEquip.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
        return None
    iMaxGrade = oGame.m_WarData.GetMaxWeaponGrade(oGame)
    if iMaxGrade and iGrade > iMaxGrade:
        iGrade = iMaxGrade
    oItem = cl_item.CreateEquip(oGame, iSID, iGrade, oOwner = oWarrior)
    oInscriptionCom = oItem.GetComponent('Inscription')
    oWarMgr = oGame.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return None
    iLayer = oLevelCtrl.m_LayerNum
    iLevel = oLevelCtrl.m_LevelNum
    iNum = oGame.m_WarData.GetInscriptionNum(iLayer, iLevel, oLevelCtrl)
    for iSID in oInscriptionCom.m_Inscription[:iNum]:
        oInscriptionCom.RemoveInscription(iSID)
    
    oInscriptionCom.m_InscriptionNum = iInscriptionNum
    if iInscriptionNum and lstInscription:
        lstPerform = lstInscription
        if len(lstPerform) > iInscriptionNum:
            lstPerform = lstPerform[:iInscriptionNum]
        oInscriptionCom = oItem.GetComponent('Inscription')
        for iSID in lstPerform:
            clsPerform = cl_perform.GetPerformModule(iSID)
            if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
                continue
            oInscriptionCom.AppendInscription(iSID)
        
    oInscriptionCom.AddInscription()
    oBulletCom = oItem.GetComponent('Bullet')
    oItem.PutToContainer(oItem.GetTargetContainer(oWarrior), 'HeroGradepf')
    oBulletCom.BulletModify(oBulletCom.MaxBullet())


def PassiveCBUsePerformAtCenterPos(oWarrior, oEventCB, iPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Start' not in dMsgInfo or 'Radius' not in dMsgInfo:
        return None
    if not oWarrior.GetPerform(iPerform):
        oWarrior.AddPerform(iPerform, 1)
    oPerform = oWarrior.GetPerform(iPerform)
    iRadius = dMsgInfo['Radius']
    dData = {
        'vStart': dMsgInfo['Start'],
        'Custom': {
            'Radius': iRadius } }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def PassiveCBSetThumpMark(oWarrior, oEventCB, iThump):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if iThump:
        oSkill.m_Cache['IsThump'] = 1
        return None
    if 'CurVID' not in dMsgInfo:
        return None
    iVID = dMsgInfo['CurVID']
    if 'ThumpInfo' not in oSkill.m_Cache:
        oSkill.m_Cache['ThumpInfo'] = { }
    if iVID not in oSkill.m_Cache['ThumpInfo']:
        oSkill.m_Cache['ThumpInfo'][iVID] = 0


def PassiveCBSetLiteCD(oWarrior, oEventCB, iTime):
    pfobj = oEventCB.GetObject()
    if not pfobj:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iTime = cl_formula.GetResultByData(oWarrior, iTime, {
        'LifeCycle': oLifeCycle })
    pfobj.SetLiteCD(iTime)


def PassiveCBModifyLiteCD(oWarrior, oEventCB, iTime):
    pfobj = oEventCB.GetObject()
    if not pfobj:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iTime = cl_formula.GetResultByData(oWarrior, iTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    pfobj.ModifyLiteCD(iFrame)


def PassiveCBTaskTempDisableInscription(oWarrior, oEventCB, iNum):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    oCurWeapon = oWarrior.m_WieldCon.GetCurWeapon()
    if not oCurWeapon or oCurWeapon.IsInitWeapon():
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
        if oWeapon != oCurWeapon:
            return None
    iNum = cl_formula.GetResultByData(oWarrior, iNum, {
        'LifeCycle': oLifeCycle })
    oInscriptionCom = oCurWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    iTask = oTask.m_ID
    sKey = 'DisableInscription-%s-%s' % (iTask, oCurWeapon.m_ID)
    dInscription = oTask.GetSaveData(sKey, { })
    if dInscription:
        iLack = iNum - len(dInscription)
        if iLack > 0:
            dInscription = oInscriptionCom.ReplaceTempDisableInscription(sKey, [], iLack)
            if dInscription:
                oTask.SetSaveData(sKey, dInscription, iCover = 1)
            
        dInscription = dict.fromkeys(dInscription, 1)
        oInscriptionCom.TempDisableInscription(sKey, dInscription)
    else:
        dUpgrade = oTask.GetSaveData('ChooseUpgradeInscription', { })
        dInscription = oInscriptionCom.RandomTempDisableInscription(sKey, iNum, list(dUpgrade))
        if dInscription:
            oTask.SetSaveData(sKey, dInscription)


def PassiveCBRefreshTaskDisableInscription(oWarrior, oEventCB, iNum):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon or oWeapon != oWarrior.m_WieldCon.GetCurWeapon():
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    sKey = 'DisableInscription-%s-%s' % (oTask.m_ID, oWeapon.m_ID)
    oInscriptionCom.RemoveTempDisbleInscription(sKey, iRefresh = 0)
    iNum = cl_formula.GetResultByData(oWarrior, iNum, dEventInfo, dMsgInfo)
    dInscription = oInscriptionCom.RandomTempDisableInscription(sKey, iNum)
    oTask.SetSaveData(sKey, dInscription, iCover = 1)


def PassiveCBReplaceTaskDisableInscription(oWarrior, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon or oWeapon.IsInitWeapon() or oWeapon != oWarrior.m_WieldCon.GetCurWeapon():
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    sKey = 'DisableInscription-%s-%s' % (oTask.m_ID, oWeapon.m_ID)
    dInscription = oTask.GetSaveData(sKey, { })
    if not dInscription:
        return None
    lstOldInsciption = dMsgInfo['OldInscription']
    setReplace = set(lstOldInsciption) & set(dInscription)
    if not setReplace:
        return None
    dInscription = oInscriptionCom.ReplaceTempDisableInscription(sKey, setReplace)
    oTask.SetSaveData(sKey, dInscription, iCover = 1)


def PassiveCBExtraExecuteTarget(oWarrior, oEventCB, iPerform, iState, iStateTime):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.DelPassLayerClearKey(sKey)

    oPerform = oWarrior.GetPerform(iPerform)
    if not oPerform:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    sKey = oEventCB.m_Key
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['pfid'] == iPerform:
        iParentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    else:
        iParentActNum = oSkill.m_Base['ActNum']
    oWarrior.AddPassLayerClearKey(sKey)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, 0)
    dAllHit = oWarrior.SetDefault(sKey, { })
    dHitTarget = dAllHit.setdefault('%s-%s' % (sKey, iParentActNum), { })
    dHitTarget[dMsgInfo['CurVID']] = 1
    oFlawCon = oWarrior.m_FlawCon
    iExecute = 0
    iCurMaxKillValue = 0
    iFinalTarget = 0
    lstTar = ShufferList(oGame, lstTar)
    for iTarget in lstTar:
        if iTarget in dHitTarget:
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iKillValue = 0
        if oTarget.m_State.GetItemBySID(iState):
            continue
        if oFlawCon.CheckMonsterBeExecuted(oTarget):
            iKillValue += 2
            iExecute = 1
        if oTarget.IsUnbalance():
            iKillValue += 1
        if iKillValue >= iCurMaxKillValue:
            iFinalTarget = iTarget
            iCurMaxKillValue = iKillValue
    
    if not iFinalTarget:
        return None
    oPerform.AddCanUseCount()
    cl_snetwar.GS2CNotifyStartSkill(oGame, oWarrior.m_PlayerID, oPerform.m_SID, oPerform.m_ID, 0, {
        'Target': iFinalTarget,
        'Execute': iExecute,
        'ParentActNum': iParentActNum })
    if iExecute:
        oReason = cl_object.reason.CStrReason(f'''ExtraExecute-{oEventCB.m_Key}''')
        dStateArgs = {
            'AID': oWarrior.m_ID,
            'RS': oReason,
            'arg': { } }
        oFinalTarget = oGame.GetObject(iFinalTarget)
        oState = cl_state.AddState(oFinalTarget, iState, STATE_TIME_LIMIT, Time2Frame(iStateTime), dStateArgs)
        if oState:
            oState.Enable(oFinalTarget)


def PassiveCBRecordParentActNum(oWarrior, oEventCB):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.DelPassLayerClearKey(sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    sKey = oEventCB.m_Key + 'ParentActNum'
    dParentActNum = oWarrior.SetDefault(sKey, { })
    dParentActNum[oSkill.m_Base['ActNum']] = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, 0)


def PassiveCBExplodeRangeFlaw(oWarrior, oEventCB, iPerform):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.DelPassLayerClearKey(sKey)

    oPerform = oWarrior.GetPerform(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dCartoon = dMsgInfo['Cartoon']
    lstTar = dCartoon['AllVLST']
    if not lstTar:
        return None
    dFlawTar = { }
    oFlawCon = oWarrior.m_FlawCon
    for iTarget in lstTar:
        if oFlawCon.GetFlaw(iTarget):
            dFlawTar[iTarget] = 10
    
    oGame = oWarrior.m_Game
    iFinalTarget = ChooseKey(oGame, dFlawTar)
    if not iFinalTarget:
        return None
    dFlaw = oFlawCon.GetFlaw(iFinalTarget)
    iFlaw = ChooseKey(oGame, dict.fromkeys(dFlaw, 10))
    iActNum = dMsgInfo['ActNum']
    dParentActNum = oWarrior.Query(oEventCB.m_Key + 'ParentActNum', { })
    if iActNum in dParentActNum:
        iParentActNum = dParentActNum[iActNum]
    else:
        iParentActNum = iActNum
    sKey = oEventCB.m_Key + 'TriggerCnt'
    dTriggerCnt = oWarrior.SetDefault(sKey, { })
    if iParentActNum in dTriggerCnt:
        dTriggerCnt[iParentActNum] += 1
    else:
        dTriggerCnt[iParentActNum] = 1
    pfobj = oEventCB.GetObject()
    iTriggerCnt = dTriggerCnt[iParentActNum]
    oPerform.AddCanUseCount()
    cl_snetwar.GS2CNotifyStartSkill(oGame, oWarrior.m_PlayerID, oPerform.m_SID, oPerform.m_ID, 0, {
        'Target': iFinalTarget,
        'Flaw': iFlaw,
        'ParentActNum': iParentActNum,
        'TriggerCnt': iTriggerCnt,
        'Prob': pfobj.GetArgValue('Prob', 200) })
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, 0)


def PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, sArgs, iKey, iValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    iValue = cl_formula.GetResultByData(oWarrior, iValue, dEventInfo, dMsgInfo)
    dArgs = pfobj.SetArgValueDefault(sArgs, { })
    dArgs[iKey] = iValue


def PassiveCBGetPFArgsDict(oWarrior, oEventCB, sArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return { }
    return pfobj.GetArgValue(sArgs, { })


def PassiveCBSetPFArgsDict(oWarrior, oEventCB, sArgs, dInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    pfobj.SetArgValue(sArgs, dInfo)


def PassiveCBDelTarKeyInPFArgsDict(oWarrior, oEventCB, iKey, sArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iItemID = dEventInfo['ItemID']
    pfobj = oWarrior.GetPerform(iPerform, iItemID)
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oWarrior, iKey, dEventInfo, dMsgInfo)
    dArgs = pfobj.GetArgValue(sArgs, { })
    dArgs.pop(iKey, 0)


def PassiveCBAddSourceWandSaveData(oWarrior, oEventCB, sKey, iVal):
    oPerform = oEventCB.GetObject()
    iWandID = oPerform.m_Item
    oWand = oWarrior.m_WandCon.GetWandByID(iWandID)
    if not oWand:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iAddVal = cl_formula.GetResultByData(oWarrior, iVal, dEventInfo, dMsgInfo)
    iOldVal = oWand.Query(sKey, 0)
    oWand.Set(sKey, iOldVal + iAddVal)


def PassiveCBReplaceSourceWand(oWarrior, oEventCB, iNewSID):
    oPerform = oEventCB.GetObject()
    oWarrior.m_WandCon.ReplaceWand(oPerform.m_Item, iNewSID)


def PassiveCBChangeWandAttr(oWarrior, oEventCB, sAttr, iAdd, iMul, iDropClear):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oWand = oLifeCycleOwner.GetMyItem()
        if not oWand:
            return None
        oWand.AttrClear(sAttr, sKey)

    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle:
        return None
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return None
    oWand = oWarrior.m_WandCon.GetWandByID(pfobj.m_Item)
    if not oWand:
        return None
    sKey = pfobj.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMul = cl_formula.GetResultByData(oWarrior, iMul, dEventInfo, dMsgInfo, { })
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, dEventInfo, dMsgInfo, { })
    if iMul or iAdd:
        oWand.AttrChange(sAttr, iMul, iAdd, sKey)
    else:
        oWand.AttrClear(sAttr, sKey)
    if iDropClear:
        oLifeCycle.AddUniqueDisableFunc('ClearAttr', ClearFunc, 0)


def PassiveCBResetWandComp(oWarrior, oEventCB, iCompSID, iOnlyResetArg, iSendToClient):
    if not iCompSID:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle:
        return None
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return None
    oWand = pfobj.GetMyItem()
    if not oWand:
        return None
    iCompSID = cl_formula.GetResultByData(oWarrior, iCompSID, {
        'LifeCycle': oLifeCycle }, oEventCB.GetCBMsgInfo())
    oCondComp = None
    for oComp in oWand.m_Comp[WAND_COMP_TYPE_CONDITION].values():
        if oComp.m_SID == iCompSID:
            oCondComp = oComp
            break
    
    if not oCondComp:
        return None
    oCondComp.ResetCondition(iOnlyResetArg)
    if iSendToClient:
        oWand.WandCastingConditionsRefresh()


def PassiveEventCBDropCookiesDrop(oWarrior, oEventCB, iTriggerPos):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return None
    oVictim = oWarrior.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim:
        return None
    oPerform = oEventCB.GetObject()
    vPos = cl_reward.GetDropBasePos(oVictim)
    lstDropInfo = [
        {
            'Item': oPerform.m_Item,
            'TriggerPos': iTriggerPos }]
    oWarrior.m_Game.GetResMgr().CreateDrop(oVictim.m_Scene, NWARRIOR_DROP_COOKIES, vPos, lstDropInfo, { }, iOwner = oWarrior.m_ID)


def PassiveEventCBChangeFinishCondition(oWarrior, oEventCB, iChangeRatio, iClearConditionCount):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oWand = oLifeCycleOwner.GetMyItem()
        if not oWand:
            return None
        dComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION]
        for oConditionComp in dComp.values():
            dChangeFactor = oConditionComp.GetKeepValue('ChangeFinishCountFactor', { })
            if sKey in dChangeFactor:
                dChangeFactor.pop(sKey)
                oConditionComp.SetKeepValue('ChangeFinishCountFactor', dChangeFactor)
                oConditionComp.m_ChangeFinishConditionCountFactor = sum(dChangeFactor.values())
                iBaseFinshCount = oConditionComp.GetKeepValue('BaseFinshCount', 0)
                if iBaseFinshCount:
                    oConditionComp.SetFinishConditionCount(iBaseFinshCount)
        

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CompType' not in dMsgInfo or dMsgInfo['CompType'] != WAND_COMP_TYPE_CONDITION or 'CompPos' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if not oLifeCycle:
        return None
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    iWandCompPos = dMsgInfo['CompPos']
    if iWandCompPos not in oWand.m_Comp[WAND_COMP_TYPE_CONDITION]:
        return None
    oConditionComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION][iWandCompPos]
    dChangeFactor = oConditionComp.GetKeepValue('ChangeFinishCountFactor', { })
    sKey = oEventCB.m_Key
    iChangeRatio = cl_formula.GetResultByData(oWarrior, iChangeRatio, dEventInfo, dMsgInfo, { })
    dChangeFactor[sKey] = iChangeRatio
    iBaseFinishCount = oConditionComp.GetKeepValue('BaseFinshCount', 0)
    if not iBaseFinishCount:
        iBaseFinishCount = oConditionComp.m_FinishConditionCount
    oConditionComp.m_ChangeFinishConditionCountFactor = sum(dChangeFactor.values())
    oConditionComp.SetKeepValue('ChangeFinishCountFactor', dChangeFactor)
    if iClearConditionCount:
        oConditionComp.m_ConditionCount = 0
    oConditionComp.SetFinishConditionCount(iBaseFinishCount)
    oLifeCycle.AddUniqueDisableFunc('ClearFinishCountFactor', ClearFunc, iCover = 0)


def PassiveEventCBAddTargetStateTime(oWarrior, oEventCB, iState, iTime, iMaxTime, iFromAttacker = 0, iOnlyMinTime = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oWarrior, iTime, dEventInfo)
    iFrame = Time2Frame(iTime)
    iMaxTime = cl_formula.GetResultByData(oWarrior, iMaxTime, dEventInfo)
    iMaxFrame = Time2Frame(iMaxTime)
    if iFromAttacker:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        if 'AID' in dMsgInfo:
            iAttack = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iAttack = dMsgInfo['Skill'].m_Base['AID']
        else:
            return None
    if not iOnlyMinTime:
        for iTarget in dTrans['TargetList']:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget:
                continue
            lstState = oTarget.m_State.GetItems(iState)
            for oTarState in lstState:
                if iFromAttacker and oTarState.m_Attacker != iAttack:
                    continue
                cl_state.AddTime(oTarState, oTarget, iFrame, iMaxFrame)
            
        
    else:
        iMinRemainTime = 1000000
        oTargetResult = None
        oTarStateResult = None
        for iTarget in dTrans['TargetList']:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget:
                continue
            lstState = oTarget.m_State.GetItems(iState)
            for oTarState in lstState:
                if iFromAttacker and oTarState.m_Attacker != iAttack:
                    continue
                iRemainTime = oTarState.GetRemainTime()
                if not iRemainTime:
                    continue
                if iRemainTime < iMinRemainTime:
                    iMinRemainTime = iRemainTime
                    oTargetResult = oTarget
                    oTarStateResult = oTarState
            
        
        if oTargetResult:
            cl_state.AddTime(oTarStateResult, oTargetResult, iFrame, iMaxFrame)

