# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6933.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6933.pyc
# Source Generated with Decompyle++
# File: p6933.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import HATCH_SEED, MAIN_HOLD, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, HATCH_SEED, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1333, 1, 0):
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, MAIN_HOLD, 2000, 0)


class CPerform(CCustomPerform):
    m_SID = 6933
    m_Name = '#NT#天袭占位lvl.3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

