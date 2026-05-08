# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1015.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1015.pyc
# Source Generated with Decompyle++
# File: s1015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    CustomCBAction(oListener, oEventCB, {
        'Target': 3 })


class CAchieveStat(CCustom):
    m_SID = 1015
    m_Name = '不劳而获'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo or 'Cost' not in dMsgInfo:
        return None
    iCost = dMsgInfo['Cost']
    iNpc = dMsgInfo['ShopNpc']
    dAll = oListener.Query('FreeShop', { })
    if iCost == 0:
        dAll[iNpc] = 1
    else:
        dAll.pop(iNpc, 0)
    if len(dAll) >= dArgs['Target']:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
    else:
        oListener.Set('FreeShop', dAll)

