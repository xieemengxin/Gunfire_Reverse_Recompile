# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13726.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13726.pyc
# Source Generated with Decompyle++
# File: p13726.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import NORMAL_REDUCENUM_UI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonTriggerReduceSuitTakeEffectAmount(oWarrior, oLifeCycle, {
        'Key': 'save.bened13726',
        'MapLoadOKCb': 1,
        'CheckCondiReduce': 1,
        'ReduceNum': 1,
        'ChooseNum': 3,
        'UIType': NORMAL_REDUCENUM_UI })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, -1, 0, 0, 0)
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, 'BossDropBlankRelic', 1, None)
    cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'BossFuseTimes', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'BossFuseTimes', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CBCheckFromBenediction(oWarrior, oEventCB, 13726):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'bened13726', 0)


class CPerform(CCustomPerform):
    m_SID = 13726
    m_Name = '未雨绸缪'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

