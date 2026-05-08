# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_task.pyc
# RelativePath: clientlogic/cl_evact/ev_task.pyc
# Source Generated with Decompyle++
# File: ev_task.pyc (Python 3.6)

import cl_formula

def TaskCBAddStat(oListener, oEventCB, iStatIdx, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'TaskID' not in dEventInfo:
        return None
    iTaskID = dEventInfo['TaskID']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oTask = oListener.m_TaskCon.GetTaskByID(iTaskID)
    if oTask:
        oTask.AddStat(iStatIdx, iAdd)
    elif oListener.m_TaskCon.CheckSubTaskRunning(iTaskID) and 'LifeCycle' in dEventInfo and dEventInfo['LifeCycle']:
        oLifeCycle = dEventInfo['LifeCycle']
        oTask = oLifeCycle.GetObject()
        if oTask:
            oTask.AddStat(iStatIdx, iAdd)


def TaskCBDirectTaskStatus(oListener, oEventCB, iStatus):
    if iStatus < 1 and iStatus > 3:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'LifeCycle' not in dEventInfo:
        return None
    oLifeCycle = dEventInfo['LifeCycle']
    oTask = oLifeCycle.GetObject()
    oEventCB.m_CBSelf = 0
    oTask.ChangeStatus(iStatus)


def TaskCBAddDataDict(oListener, oEventCB, sKey, iKey, iValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'LifeCycle' not in dEventInfo:
        return None
    oLifeCycle = dEventInfo['LifeCycle']
    oTask = oLifeCycle.GetObject()
    dArg = oTask.GetData(sKey, None)
    if dArg is None:
        dArg = { }
        oTask.SetData(sKey, dArg)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iKey = cl_formula.GetResultByData(oListener, iKey, dEventInfo, dMsgInfo)
    dArg.update({
        iKey: iValue })

