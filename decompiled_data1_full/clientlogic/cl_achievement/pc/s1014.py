# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1014.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1014.pyc
# Source Generated with Decompyle++
# File: s1014.pyc (Python 3.6)

from cl_commondefines import OBTAIN_WARCASH
from cl_commondefines import LEVEL_TYPE_BOSS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_GETGOODSLIST, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
    else:
        cl_evact.AchieveCBResetWarStat(oListener, oEventCB)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 1):
        CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1014
    m_Name = '穷困潦倒'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'GoodsList' not in dMsgInfo or 'ShopNpc' not in dMsgInfo:
        return None
    iShopNpc = dMsgInfo['ShopNpc']
    sKey = 'VisitShop%d' % iShopNpc
    if oListener.Query(sKey, 0):
        return None
    oListener.Set(sKey, 1)
    iCash = oListener.m_WarCash
    for lstGoodsInfo in dMsgInfo['GoodsList']:
        (_pos, _sid, _goodstype, iCanBuy, iHasBought, cashtype, cash, _lock, _allattr) = lstGoodsInfo
        if cashtype != OBTAIN_WARCASH:
            continue
        if iCash >= cash and iCanBuy > iHasBought:
            return None
    
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)

