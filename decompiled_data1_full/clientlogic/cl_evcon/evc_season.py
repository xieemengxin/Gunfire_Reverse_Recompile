# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/evc_season.pyc
# RelativePath: clientlogic/cl_evcon/evc_season.pyc
# Source Generated with Decompyle++
# File: evc_season.pyc (Python 3.6)

from cl_only import GAME_FRAME
import cl_formula

def SeasonTaskCBCheckWarValue(oListener, oEventCB, iTarget):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return False
    sKey = oEventCB.m_Key
    iCur = oListener.QuerySavedData(sKey)
    return iCur >= iTarget


def SeasonTaskCBGetWarValue(oListener, oEventCB):
    sKey = oEventCB.m_Key
    return oListener.QuerySavedData(sKey, 0)


def SeasonTaskCBGetWarDictData(oListener, oEventCB, sAttr, sKey):
    sNewAttr = oEventCB.m_Key + sAttr
    dCustomData = oListener.Query(sNewAttr, { })
    if not dCustomData:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    sKey = cl_formula.GetResultByData(oListener, sKey, dEventInfo, dMsgInfo)
    if sKey not in dCustomData:
        return 0
    return dCustomData[sKey]


def SeasonTaskCBGetCustomData(oListener, oEventCB, sAttr, iSecond):
    sKey = oEventCB.m_Key + sAttr
    dCustomData = oListener.Query(sKey, { })
    if not dCustomData:
        return 0
    oGame = oListener.m_Game
    iCurFrame = oGame.GetFrameNum()
    iMinFrame = iCurFrame - iSecond * GAME_FRAME
    iTotalValue = 0
    dNewCustomData = { }
    for iFrame, iValue in dCustomData.items():
        if iFrame < iMinFrame:
            continue
        dNewCustomData[iFrame] = iValue
        iTotalValue += iValue
    
    oListener.Set(sKey, dNewCustomData)
    return iTotalValue

