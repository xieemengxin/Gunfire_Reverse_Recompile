# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6915.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6915.pyc
# Source Generated with Decompyle++
# File: p6915.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import FUNCMODE_TYPE_TALENTLEVELUP
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '6915Reward'):
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADDTALENT, -1)
    elif not cl_evcon.CheckReason(oWarrior, oEventCB, 'load', 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'p6915_TalentCount' }))) >= 5:
            cl_evact.EventCBSetSavedData(oWarrior, oEventCB, '6915Reward', 1, 0)
            cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADDTALENT, -1)
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2383, { })
            cl_action.CommonSwitchMode(oWarrior, oEventCB.GetCBLifeCycle(), FUNCMODE_TYPE_TALENTLEVELUP, 1, { }, 1)
        else:
            cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'p6915_TalentCount', (lambda *a: Func598(*a, **{
'sKey': 'p6915_TalentCount' }) + 1), 1)


class CPerform(CCustomPerform):
    m_SID = 6915
    m_Name = '水墨画师lv.5'
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

