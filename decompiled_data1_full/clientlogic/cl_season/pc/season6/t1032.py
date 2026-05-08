# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season6/t1032.pyc
# RelativePath: clientlogic/cl_season/pc/season6/t1032.pyc
# Source Generated with Decompyle++
# File: t1032.pyc (Python 3.6)

from cl_commondefines import DICESPECIAL_PASSIVE_TAKEEFFECT, SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_SPECIALITEM
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
    cl_action.CommonAddWarSeasonSonTaskValueByCarrySpecialItem(oListener, oLifeCycle, SEASONTASK_EXTINFO_TYPE_SPECIALITEM, DICESPECIAL_PASSIVE_TAKEEFFECT, 1, SEASONSUBTASK_TYPE_ADD)


class CSeasonTask(CCustom):
    m_SID = 1032
    m_TargetValue = 7
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = { }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_SPECIALITEM]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_SPECIALITEM: {
            1006: 1,
            1010: 1,
            1012: 1,
            1013: 1,
            1015: 1,
            1016: 1,
            1017: 1 } }

