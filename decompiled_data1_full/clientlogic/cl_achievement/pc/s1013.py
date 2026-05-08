# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1013.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1013.pyc
# Source Generated with Decompyle++
# File: s1013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_RECASTWEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    CustomCBAction(oListener, oEventCB, {
        'Target': 2000 })


class CAchieveStat(CCustom):
    m_SID = 1013
    m_Name = '再洗一次'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cost' not in dMsgInfo or 'NpcID' not in dMsgInfo:
        return None
    iNpc = dMsgInfo['NpcID']
    dAll = oListener.Query('SmithRecast', { })
    iOld = dAll[iNpc] if iNpc in dAll else 0
    iNew = iOld + dMsgInfo['Cost']
    if iNew >= dArgs['Target']:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
    else:
        dAll[iNpc] = iNew
        oListener.Set('SmithRecast', dAll)

