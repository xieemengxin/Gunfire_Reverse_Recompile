# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15191.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15191.pyc
# Source Generated with Decompyle++
# File: p15191.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15191 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import MG_SOURCE_SEASONSUIT, SUIT_HANDLE_TALENT2RELIC
from cl_newformula import Func651, Func726

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_TALENT2RELIC, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTalent(oWarrior, oEventCB, (lambda *a: Func726(*a))):
        cl_evact.EventCBReduceTalentLevel(oWarrior, oEventCB, (lambda *a: Func726(*a)), 1)
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2430, {
            2: 100 }, MG_SOURCE_SEASONSUIT, 1, 1, 1, 1)
        CustomAction(oWarrior, oEventCB, {
            'Key': 'NewRewardpf15191' })
        cl_evact.PassiveCBSetPFArgsDict(oWarrior, oEventCB, 'NewRewardpf15191', { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameFromSelf(oWarrior, oEventCB):
        cl_evact.PassiveCBUpdatePFArgsDict(oWarrior, oEventCB, 'NewRewardpf15191', (lambda *a: Func651(*a, **{
'sKey': 'iPerform' })), (lambda *a: Func651(*a, **{
'sKey': 'Level' })))


class CPerform(CCustomPerform):
    m_SID = 15191
    m_Name = '灵气流转套装'
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

