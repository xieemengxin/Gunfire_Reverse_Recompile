# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13734.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13734.pyc
# Source Generated with Decompyle++
# File: p13734.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import S7_MODULE_POINT_CHANGE

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'PF13734'):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'PF13734', 1)
        cl_action.CommonRewardS7Crystal(oWarrior, oLifeCycle, 0, {
            1001: 1 }, 3)
    CustomAction1(oWarrior, oLifeCycle, {
        'OriginalDamMul': 20,
        'EachOverflowDecrease': 5,
        'MinimumDamMul': 5 })
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'OriginalDamMul': 2000,
        'EachOverflowDecrease': 500,
        'MinimumDamMul': 500 })


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction1(oWarrior, oEventCB.GetCBLifeCycle(), {
        'OriginalDamMul': 20,
        'EachOverflowDecrease': 5,
        'MinimumDamMul': 5 })
    if cl_evcon.EventCBCheckReenter(oWarrior, oEventCB):
        CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
            'OriginalDamMul': 2000,
            'EachOverflowDecrease': 500,
            'MinimumDamMul': 500 })


class CPerform(CCustomPerform):
    m_SID = 13734
    m_Name = '充能超载'
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
    m_Career = None

