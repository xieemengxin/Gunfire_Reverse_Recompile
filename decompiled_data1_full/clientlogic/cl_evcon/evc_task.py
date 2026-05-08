# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/evc_task.pyc
# RelativePath: clientlogic/cl_evcon/evc_task.pyc
# Source Generated with Decompyle++
# File: evc_task.pyc (Python 3.6)

import cl_formula

def TaskCBCheckKeyInDataDict(oListener, oEventCB, sKey, iKey):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'LifeCycle' not in dEventInfo:
        return 0
    oLifeCycle = dEventInfo['LifeCycle']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oTask = oLifeCycle.GetObject()
    iKey = cl_formula.GetResultByData(oListener, iKey, dEventInfo, dMsgInfo)
    dArg = oTask.GetData(sKey, { })
    if iKey not in dArg:
        return 0
    return 1

