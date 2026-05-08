# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/t1037.pyc
# RelativePath: clientlogic/cl_season/pc/season6/t1037.pyc
# Source Generated with Decompyle++
# File: t1037.pyc (Python 3.6)

from cl_commondefines import DICE_SUBMSG_ADD, SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_DICE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    pass


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBGetDiceAbilityQuality(oListener, oEventCB) == 5:
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_DICE, 0, 1, SEASONSUBTASK_TYPE_ADD, 1)


class CSeasonTask(CCustom):
    m_SID = 1037
    m_TargetValue = 20
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_DICE]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_DICE: {
            51301: 1,
            51302: 1,
            51303: 1,
            51304: 1,
            51305: 1,
            51306: 1,
            51307: 1,
            51308: 1,
            51309: 1,
            51310: 1,
            51311: 1,
            51312: 1,
            51313: 1,
            51314: 1,
            51315: 1,
            51316: 1,
            51317: 1,
            51318: 1,
            51319: 1,
            51320: 1,
            51321: 1,
            51322: 1,
            51323: 1,
            51324: 1,
            51325: 1,
            51326: 1,
            51327: 1,
            51328: 1,
            51329: 1,
            51330: 1,
            51331: 1,
            51332: 1,
            51333: 1,
            51334: 1,
            51335: 1,
            51336: 1,
            51337: 1,
            51338: 1,
            51339: 1,
            51340: 1,
            51341: 1,
            51342: 1,
            51343: 1,
            51344: 1,
            51345: 1,
            51346: 1,
            51347: 1,
            51348: 1,
            51349: 1,
            51350: 1,
            51351: 1,
            51352: 1,
            51353: 1,
            51354: 1,
            51355: 1,
            51356: 1,
            51357: 1,
            51358: 1,
            51359: 1,
            51360: 1,
            51361: 1,
            51362: 1,
            51363: 1,
            51364: 1,
            51365: 1,
            51366: 1,
            51367: 1,
            51368: 1,
            51369: 1,
            51370: 1,
            51371: 1,
            51372: 1,
            51733: 1,
            51374: 1,
            51375: 1,
            51376: 1,
            51377: 1,
            51378: 1,
            51379: 1,
            51380: 1,
            51381: 1,
            51382: 1,
            51383: 1,
            51384: 1,
            51385: 1,
            51386: 1 } }

