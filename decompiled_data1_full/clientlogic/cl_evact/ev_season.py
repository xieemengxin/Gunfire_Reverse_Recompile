# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_season.pyc
# RelativePath: clientlogic/cl_evact/ev_season.pyc
# Source Generated with Decompyle++
# File: ev_season.pyc (Python 3.6)

from cl_commondefines import SEASONTASK_EXTINFO_TYPE_BENE
import cl_formula

def CBAddSeasonTaskValue(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iAdd <= 0:
        return None
    iSeasonTask = dEventInfo['SeasonTaskSID']
    oListener.m_SeasonTaskMgr.AddTaskValue(iSeasonTask, iAdd)


def CBSetSeasonTaskValue(oListener, oEventCB, iNewValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iNewValue = cl_formula.GetResultByData(oListener, iNewValue, dEventInfo, dMsgInfo)
    iSeasonTask = dEventInfo['SeasonTaskSID']
    oListener.m_SeasonTaskMgr.SetTaskValue(iSeasonTask, iNewValue)


def CBAddWarSeasonTaskValue(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return None
    sKey = oEventCB.m_Key
    iCur = oListener.QuerySavedData(sKey, 0)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.SetSavedData(sKey, iCur + iAdd)


def CBSetWarSeasonTaskValue(oListener, oEventCB, iValue):
    sKey = oEventCB.m_Key
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    oListener.SetSavedData(sKey, iValue)


def CBAddSeasonTaskCustomData(oListener, oEventCB, sAttr, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    sKey = oEventCB.m_Key + sAttr
    oGame = oListener.m_Game
    iCurFrame = oGame.GetFrameNum()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dCustomData = oListener.Query(sKey, { })
    if iCurFrame not in dCustomData:
        dCustomData[iCurFrame] = iAdd
    else:
        dCustomData[iCurFrame] += iAdd
    oListener.Set(sKey, dCustomData)


def CBRecoverSeasonTaskCustomData(oListener, oEventCB, sAttr):
    sKey = oEventCB.m_Key + sAttr
    oListener.Set(sKey, { })


def CBAddWarSeasonTaskDictData(oListener, oEventCB, sAttr, sKey, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    sNewAttr = oEventCB.m_Key + sAttr
    sKey = cl_formula.GetResultByData(oListener, sKey, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dCustomData = oListener.Query(sNewAttr, { })
    if sKey not in dCustomData:
        dCustomData[sKey] = iAdd
    else:
        dCustomData[sKey] += iAdd
    oListener.Set(sNewAttr, dCustomData)


def CBAddWarSeasonTaskValueByDifferentID(oListener, oEventCB, sAttr, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if sAttr not in dMsgInfo or not dMsgInfo[sAttr]:
        return None
    oSeasonTaskMgr = oListener.m_SeasonTaskMgr
    if sAttr not in oSeasonTaskMgr.m_ShowExtInfoType:
        return None
    iType = oSeasonTaskMgr.m_ShowExtInfoType[sAttr]
    iSID = dMsgInfo[sAttr]
    iTaskSID = dEventInfo['SeasonTaskSID']
    dTaskExtInfo = oSeasonTaskMgr.GetSeasonTaskExtInfo(iTaskSID)
    if iType not in dTaskExtInfo or iSID not in dTaskExtInfo[iType]:
        oSeasonTask = oEventCB.GetObject()
        iMaxVal = oSeasonTask.m_TargetValue
        if iMaxVal and oSeasonTask.m_CurValue + iAdd >= iMaxVal:
            oSeasonTaskMgr.SetTaskValue(iTaskSID, iMaxVal)
        else:
            oSeasonTaskMgr.AddTaskValue(iTaskSID, iAdd)
        oSeasonTaskMgr.SetSeasonTaskExtInfo(iTaskSID, iType, iSID)


def CBAddWarSeasonSonTaskValue(oListener, oEventCB, iType, iSubTask, iAdd, iAddType, iUsesAttr):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'SeasonTaskSID' not in dEventInfo:
        return None
    oSeasonTaskMgr = oListener.m_SeasonTaskMgr
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iUsesAttr:
        lstAttr = oSeasonTaskMgr.GetKeyListByIntKey(iType)
        if not lstAttr:
            return None
        for sAttr in lstAttr:
            if sAttr not in dMsgInfo or not dMsgInfo[sAttr]:
                continue
            iSubTask = dMsgInfo[sAttr]
        
    if not iSubTask:
        return None
    oSeasonTask = oEventCB.GetObject()
    iSubTask = cl_formula.GetResultByData(oListener, iSubTask, dEventInfo, dMsgInfo)
    if not oSeasonTask or iType not in oSeasonTask.m_SubTaskInfo or iSubTask not in oSeasonTask.m_SubTaskInfo[iType]:
        return None
    oSeasonTaskMgr.AddTaskVauleBySubTask(oSeasonTask, iType, iSubTask, iAdd, iAddType)

