# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1040.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1040.pyc
# Source Generated with Decompyle++
# File: s1040.pyc (Python 3.6)

import cl_abnormalconf
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_GOTDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1040
    m_Name = '多灾多难'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateSID' not in dMsgInfo:
        return None
    iSID = dEventInfo['AchieveStatSID']
    iStateSID = dMsgInfo['StateSID']
    sKey = 'achieve%d' % iSID
    dGot = oListener.QuerySavedData(sKey, { })
    if iStateSID in dGot:
        return None
    dGot[iStateSID] = 1
    if len(dGot) >= len(cl_abnormalconf.g_AllAbnormalStateSID):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        return None
    oListener.SetSavedData(sKey, dGot)

