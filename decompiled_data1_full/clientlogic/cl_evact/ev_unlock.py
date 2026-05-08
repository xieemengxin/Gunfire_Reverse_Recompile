# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_unlock.pyc
# RelativePath: clientlogic/cl_evact/ev_unlock.pyc
# Source Generated with Decompyle++
# File: ev_unlock.pyc (Python 3.6)

import cl_formula

def CBAddUnlockProgress(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'UnlockProgressSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.m_NewUnlockProgressMgr.UpdateProgress(dEventInfo['UnlockProgressSID'], iAdd)


def CBAddWarUnlockProgress(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'UnlockProgressSID' not in dEventInfo:
        return None
    sKey = 'unlockprogress%s' % dEventInfo['AchieveStatSID']
    iCur = oListener.QuerySavedData(sKey, 0)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.SetSavedData(sKey, iCur + iAdd)

