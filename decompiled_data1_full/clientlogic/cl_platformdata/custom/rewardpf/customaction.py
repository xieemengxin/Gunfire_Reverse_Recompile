# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/rewardpf/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/rewardpf/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import DISABLE_TYPE_MSG, VIRTUAL_ITEM_RELIC, MG_SOURCE_SEASONSUIT, FOURSEASON_ROLLRELIC, STATE_SUBSPD_LIST, STATE_TIME_LIMIT, STATE_TIME_FOREVER, DISABLE_TYPE_STATE, SUIT_HANDLE_TALENT2RELIC, RELIC_LIFECYCLE_TEMPLEVEL, SUIT_HANDLE_INTENSIFY
from cl_only import Functor, ChooseKey
from cl_object.logging import WarrelicLog, SeasonsuitLog
import cl_msgcenter
import cl_reward
import cl_notify
import cl_perform
import cl_snetwar
import cl_state
import cl_object
import cl_action
import cl_evact

def CustomAction16092(oListener, oLifeCycle, dInfo):
    ListenMsgCallBackFunc(oListener, oLifeCycle, dInfo, 0)


def CustomAction16094(oListener, oLifeCycle, dInfo):
    ListenMsgCallBackFunc(oListener, oLifeCycle, dInfo, 1)


def ListenMsgCallBackFunc(oListener, oLifeCycle, dInfo, iPriority):
    
    def ClearFunc(oTarget, oLifeCycle):
        oElement = oTarget.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oElement:
            cl_msgcenter.DoneEvent(oElement, iMsg, sKey, -1)

    if 'iGroup' not in dInfo or 'iPerform' not in dInfo:
        return None
    oElement = oListener.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
    if not oElement:
        return None
    iGroup = dInfo['iGroup']
    iPerform = dInfo['iPerform']
    sKey = oLifeCycle.Key()
    iMsg = cl_msgcenter.MSG_WARMSG_PHASESTART
    func = Functor(EventCBFunc, iGroup, iPerform, oListener.m_ID)
    cl_msgcenter.AddFunction(oElement, iMsg, func, sKey, -1, 0, iPriority)
    oLifeCycle.AddDisableFunc(ClearFunc)


def EventCBFunc(iGroup, iPerform, iListener, oTarget, dMsgInfo):
    oGame = oTarget.m_Game
    oListener = oGame.GetObject(iListener)
    if not oListener:
        return None
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    oLifeCycle = oPerform.m_LifeCycle
    if not oLifeCycle:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    oEventCB = oLifeCycle.GetObject().m_EventCB
    oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)


def CustomAction15090(oTarget, oEventCB, dInfo):
    sReason = oEventCB.m_Key
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Reason' in dMsgInfo and dMsgInfo['Reason'] == sReason:
        return None
    iIsCurse = dInfo['IsCurse']
    dCurse = oTarget.m_RelicCon.GetChooseCurseRelic()
    dChooseRelic = { }
    setUnlockRelic = oTarget.Query('Illus')['Relic']
    lstHasRelic = oTarget.m_RelicCon.GetAllPerformSID()
    if iIsCurse:
        dChooseRelic = dCurse
    else:
        for iRelic in setUnlockRelic:
            if iRelic in lstHasRelic:
                continue
            if iRelic in dCurse:
                continue
            dChooseRelic[iRelic] = 1
        
    if not dChooseRelic:
        WarrelicLog.Debug('%d %d no enoughrelic %s %s' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, setUnlockRelic, lstHasRelic))
        return None
    iRelic = ChooseKey(oTarget.m_Game, dChooseRelic)
    dReward = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iRelic,
            'level': dInfo['Level'] } }
    cl_reward.RewardItem(oTarget.m_Game, oTarget, [
        dReward], sReason)
    clsPerform = cl_perform.GetPerformModule(iRelic)
    cl_notify.SendCommonNotify(oTarget.m_Game, [
        oTarget.m_PlayerID], 2393, {
        '$name': clsPerform.m_Name })
    oState = oTarget.m_State.GetItemBySID(dInfo['StateSID'])
    oState.AddCount(oTarget, dInfo['Count'])
    sKey = '%d-StateCount-%d' % (dInfo['Pfid'], dInfo['StateSID'])
    iCurCount = oState.GetCount()
    oTarget.SetSavedData(sKey, iCurCount)


def CustomAction15121(oListener, oLifeCycle, dInfo):
    iPerform = dInfo['Perform']
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    cl_snetwar.GS2CNotifyStartSkill(oListener.m_Game, oListener.m_PlayerID, iPerform, oPerform.m_ID, 0, { })


def CustomAction15192(oListener, oEventCB, dInfo):
    oRelicCon = oListener.m_RelicCon
    if not oRelicCon.IsOpenTempRelicPlayType(FOURSEASON_ROLLRELIC):
        return None
    lstNewTempRemoveRelic = list(oRelicCon.m_TempRemoveRelic[FOURSEASON_ROLLRELIC])
    if not lstNewTempRemoveRelic:
        return None
    oGame = oListener.m_Game
    oSeasonSuit = oGame.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    sKey = 'pf15192-RewardLevel'
    iSuit = dInfo['Suit']
    iRewardLevelID = oSeasonSuit.GetSavedSuitArg(oListener, iSuit, sKey)
    iLevelID = oScene.m_Level
    if iRewardLevelID and iRewardLevelID == iLevelID:
        return None
    oSeasonSuit.SetSavedSuitArg(oListener, iSuit, sKey, iLevelID)
    SeasonsuitLog.Info('%s %s roll temprelic %s %s' % (oGame.m_ID, oListener.m_PlayerID, iLevelID, lstNewTempRemoveRelic))
    iNowRelic = lstNewTempRemoveRelic[0]
    oNowPerform = oRelicCon.GetTempRemoveRelic(FOURSEASON_ROLLRELIC, iNowRelic)
    iLevel = oNowPerform.m_Level
    for iRelic in lstNewTempRemoveRelic:
        oRelicCon.RemoveTempRemoveRelic(FOURSEASON_ROLLRELIC, iRelic, 'CustomAction15192')
    
    dReward = { }
    iMiniGameSID = dInfo['MiniGame']
    dReward[iMiniGameSID] = (10000, 1)
    iHeroID = oListener.m_ID
    dExtInfo = {
        'OnlyRewardAttack': 1,
        'Abandoner': iHeroID,
        'RepeatReward': 1,
        'Source': MG_SOURCE_SEASONSUIT,
        'Level': iLevel,
        'TempRelic': 1,
        'GamePlayType': FOURSEASON_ROLLRELIC,
        'Exclude': lstNewTempRemoveRelic }
    cl_reward.RewardItemByMiniGame(oListener, iHeroID, dReward, 'CustomAction15192-%d' % iHeroID, MG_SOURCE_SEASONSUIT, dExtInfo)


def AddUpSpeedState(oListener, oLifeCycle, iState, iTimeType, iFrame, dArg):
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
    iHeroID = oListener.m_ID
    dStateArgs = {
        'AID': iHeroID,
        'RS': oReason,
        'arg': dArg }
    oState = cl_state.AddState(oListener, iState, iTimeType, iFrame, dStateArgs)
    if oState:
        oState.Enable(oListener)
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            iHeroID: oState.m_ID })


def CustomAction152081(oListener, oLifeCycle, dInfo):
    pfobj = oLifeCycle.GetObject()
    dRewardStateInfo = pfobj.SetArgValueDefault('p15208_RewardStateInfo', { })
    oStateCon = oListener.m_State
    iLimitState = dInfo['LimitStateSID']
    iForeverMoveSpeedMul = 0
    for oState in list(oStateCon.Values()):
        if oState.m_SID in STATE_SUBSPD_LIST:
            iMoveSpeedMul = oState.GetArgValue('MoveSpeedMul')
            dRewardStateInfo[oState.m_ID] = iMoveSpeedMul
            if oState.m_TimeType == STATE_TIME_LIMIT:
                AddUpSpeedState(oListener, oLifeCycle, iLimitState, STATE_TIME_LIMIT, oState.GetRemainTime(), {
                    'MoveSpeedMul': -iMoveSpeedMul })
                continue
            iForeverMoveSpeedMul += -oState.GetArgValue('MoveSpeedMul')
    
    AddUpSpeedState(oListener, oLifeCycle, dInfo['ForeverStateSID'], STATE_TIME_FOREVER, 0, {
        'MoveSpeedMul': iForeverMoveSpeedMul })


def CustomAction152082(oListener, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateID' not in dMsgInfo:
        return None
    iStateID = dMsgInfo['StateID']
    oStateCon = oListener.m_State
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    dRewardStateInfo = pfobj.GetArgValue('p15208_RewardStateInfo', { })
    if iStateID in dRewardStateInfo:
        return None
    iMoveSpeedMul = oState.GetArgValue('MoveSpeedMul')
    dRewardStateInfo[iStateID] = iMoveSpeedMul
    if oState.m_TimeType == STATE_TIME_LIMIT:
        AddUpSpeedState(oListener, oLifeCycle, dInfo['LimitStateSID'], STATE_TIME_LIMIT, oState.GetRemainTime(), {
            'MoveSpeedMul': -iMoveSpeedMul })
    else:
        oForeverUpSpeedState = oStateCon.GetItemBySID(dInfo['ForeverStateSID'])
        if not oForeverUpSpeedState:
            return None
        oForeverUpSpeedState.AddArgValue('MoveSpeedMul', -iMoveSpeedMul)
        oForeverUpSpeedState.m_LifeCycle.CallFunc('Refresh', oListener)


def CustomAction152083(oListener, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TimeType' not in dMsgInfo or 'StateID' not in dMsgInfo:
        return None
    iStateID = dMsgInfo['StateID']
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    dRewardStateInfo = pfobj.GetArgValue('p15208_RewardStateInfo', { })
    if iStateID not in dRewardStateInfo:
        return None
    iMoveSpeedMul = dRewardStateInfo.pop(iStateID)
    if dMsgInfo['TimeType'] == STATE_TIME_LIMIT:
        return None
    oForeverUpSpeedState = oListener.m_State.GetItemBySID(dInfo['ForeverStateSID'])
    if not oForeverUpSpeedState:
        return None
    oForeverUpSpeedState.AddArgValue('MoveSpeedMul', iMoveSpeedMul)
    oForeverUpSpeedState.m_LifeCycle.CallFunc('Refresh', oListener)


def CustomAction15191(oListener, oEventCB, dInfo):
    iHandleType = SUIT_HANDLE_TALENT2RELIC
    lstResult = []
    pfobj = oEventCB.GetObject()
    sArgs = dInfo['Key']
    dInfo = pfobj.GetArgValue(sArgs, { })
    for key, value in dInfo.items():
        lstResult.append(key)
        lstResult.append(value)
    
    cl_snetwar.GS2CSeasonSuitOptionInfo(iHandleType, lstResult, oListener.m_Game, oListener)


def CustomAction15204(oListener, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Result' not in dMsgInfo:
        return None
    lstResult = dMsgInfo['Result']
    if len(lstResult) < 2:
        SeasonsuitLog.Alert('%s %s resultdata err %s' % (oListener.m_Game.m_ID, oListener.m_PlayerID, lstResult))
        return None
    oWeapon = oListener.GetWeaponByID(lstResult[0])
    oOtherWeapon = oListener.GetWeaponByID(lstResult[1])
    if not oWeapon or not oOtherWeapon:
        return None
    iTempWeaponGrade = oWeapon.m_BaseGrade
    oWeapon.SetBaseGrade(oOtherWeapon.m_BaseGrade, iSendMsg = 1)
    oOtherWeapon.SetBaseGrade(iTempWeaponGrade, iSendMsg = 1)


def CustomAction15108(oListener, oEventCB, dInfo):
    lstRelic = oListener.QuerySavedData('SeasonSuit_NowRelic', [
        0])
    if not lstRelic:
        return None
    oRelicCon = oListener.m_RelicCon
    oRelic = oRelicCon.GetPerform(lstRelic[0])
    if not oRelic:
        cl_action.CommonListenMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDRELICPERFORM, iSub = -1, iGroup = dInfo['Group'], iOnce = 0, iPriority = 0)
        return None
    dRelicInfo = {
        'TempLevel': dInfo['TempLevel'] }
    oRelic.SetOtherLifeCycle(oListener, RELIC_LIFECYCLE_TEMPLEVEL, dRelicInfo)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, lstRelic, oListener.m_Game, oListener)

