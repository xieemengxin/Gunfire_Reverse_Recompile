# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1012.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1012.pyc
# Source Generated with Decompyle++
# File: s1012.pyc (Python 3.6)

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
        0: 1,
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1 })


class CAchieveStat(CCustom):
    m_SID = 1012
    m_Name = '老板大气'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo or 'Pos' not in dMsgInfo:
        return None
    iPos = dMsgInfo['Pos']
    if iPos not in dArgs:
        return None
    dAll = oListener.Query('BuyGoods', { })
    iNpc = dMsgInfo['ShopNpc']
    dShop = dAll.setdefault(iNpc, { })
    iOld = dShop[iPos] if iPos in dShop else 0
    dShop[iPos] = iOld + dMsgInfo['Amount']
    oListener.Set('BuyGoods', dAll)
    for iTargetPos, iTarget in dArgs.items():
        if iTargetPos not in dShop:
            return None
        if dShop[iTargetPos] < iTarget:
            return None
    
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)

