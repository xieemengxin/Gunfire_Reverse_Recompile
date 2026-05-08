# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13561.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13561.pyc
# Source Generated with Decompyle++
# File: p13561.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import FUNCMODE_TYPE_GARDENERPICKSEED, PICK_SEED

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_GARDENERPICKSEED, 15, {
        'PickRange': 12 }, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33824, 0, {
        'DamRatio': 500,
        'MaxCount': 40 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, PICK_SEED, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33824, 1, 1000)


class CPerform(CCustomPerform):
    m_SID = 13561
    m_Name = '草木一芥'
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
    m_Career = 119

