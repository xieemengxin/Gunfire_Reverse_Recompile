# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6914.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6914.pyc
# Source Generated with Decompyle++
# File: p6914.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponHasMinorPeform(oWarrior, oEventCB):
        cl_evact.EventCBTempAddWeaponInsPropByType(oWarrior, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 60)


class CPerform(CCustomPerform):
    m_SID = 6914
    m_Name = '水墨画师lv.4'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

