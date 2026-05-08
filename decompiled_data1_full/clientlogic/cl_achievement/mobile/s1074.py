# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1074.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1074.pyc
# Source Generated with Decompyle++
# File: s1074.pyc (Python 3.6)

from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDWEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.GetWeaponExclusiveInscriptionNum(oListener, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE) >= 2:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1074
    m_Name = '洪福齐天'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

