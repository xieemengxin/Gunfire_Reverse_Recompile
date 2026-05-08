# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_achieve.pyc
# RelativePath: clientlogic/cl_evact/ev_achieve.pyc
# Source Generated with Decompyle++
# File: ev_achieve.pyc (Python 3.6)

from cl_only import SendAlert
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, DAM_MASK_ELEMENT, DAM_MASK_PART
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, VIRTUAL_ITEM_CHEEK
from cl_only import Time2Frame, PY_FLAG_DEAD
import cl_item.defines as itemdef
import cl_formula
import cl_war
import cl_object.reason
import cl_state
import cllib.lib_flag

def AchieveCBAddStat(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.m_Achievement.AddStat(dEventInfo['AchieveStatSID'], iAdd)


def AchieveCBAddWarStat(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    sKey = 'achieve%s' % dEventInfo['AchieveStatSID']
    iCur = oListener.QuerySavedData(sKey, 0)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.SetSavedData(sKey, iCur + iAdd)


def AchieveCBResetWarStat(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    sKey = 'achieve%s' % dEventInfo['AchieveStatSID']
    oListener.SetSavedData(sKey, 0)


def AchieveCBStartCounting(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    sKey = 'achieve%sCountStart' % dEventInfo['AchieveStatSID']
    if oListener.Query(sKey, 0):
        return None
    oListener.Set(sKey, oListener.m_Game.GetFrameNum())


def AchieveCBStopCounting(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    oGame = oListener.m_Game
    iSID = dEventInfo['AchieveStatSID']
    sKey = 'achieve%sCountStart' % iSID
    iStartFrame = oListener.Query(sKey, 0)
    if iStartFrame:
        oListener.Delete(sKey)
    else:
        return None
    iCurFrame = oGame.GetFrameNum()
    sCountKey = 'achieve%sCount' % iSID
    oListener.Set(sCountKey, iCurFrame - iStartFrame)


def AchieveCBAddState(oListener, oEventCB, iState, iTime, dArgs, iCloseFollowSkill = 0):
    
    def ClearStateWithLifeCycle(oListener, oLifeCycle):
        oListener.m_State.RemoveItem(iStateID)

    
    def ClearStateWithSkill(oSkill):
        oListener.m_State.RemoveItem(iStateID)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dRet = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, dMsgInfo)
    dData = {
        'AID': oListener.m_ID,
        'RS': oEventCB.CBReason(),
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oListener, iState, iTimeType, Time2Frame(iTime), dData)
    if not oState:
        return None
    oState.Enable(oListener)
    oLifeCycle = dEventInfo['LifeCycle']
    iStateID = oState.m_ID
    if oLifeCycle.m_Enable:
        oLifeCycle.AddDisableFunc(ClearStateWithLifeCycle)
    else:
        oListener.m_State.RemoveItem(iStateID)
    if iCloseFollowSkill and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        oSkill.AddEndFunc(ClearStateWithSkill)


def AchieveAddFollowState(oListener, oEventCB, iState, iMainState, dArgs, iCloseRemove):
    
    def ClearState(oListener, oLifeCycle):
        oListener.m_State.RemoveItem(iStateID)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dRet = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, dMsgInfo)
    dData = {
        'AID': oListener.m_ID,
        'RS': oEventCB.CBReason(),
        'arg': dRet }
    oMainState = oListener.m_State.GetItemBySID(iMainState)
    if not oMainState:
        return None
    iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddFollowState(oListener, oMainState, iState, iTimeType, 0, dData)
    if not oState:
        return None
    if iCloseRemove:
        oLifeCycle = dEventInfo['LifeCycle']
        iStateID = oState.m_ID
        if oLifeCycle.m_Enable:
            oLifeCycle.AddDisableFunc(ClearState)
        else:
            oListener.m_State.RemoveItem(iStateID)


def AchieveRewardCheek(oTarget, oEventCB, iCheek):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    if not cllib.lib_flag.g_IsStandalone:
        return None
    oCon = oTarget.m_CheekCon
    oCon.AddCheek(iCheek, 'achieve%d' % dEventInfo['AchieveStatSID'])

