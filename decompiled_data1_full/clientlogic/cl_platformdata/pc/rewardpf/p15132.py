# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15132.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15132.pyc
# Source Generated with Decompyle++
# File: p15132.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import SUIT_HANDLE_ROLLTALENT
from cl_newformula import Func717, Func726, Func727, Func729

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_ROLLTALENT, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33502, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'NowCount', (lambda *a: Func729(*a) // 2 - Func727(*a, **{
'iSuit': 15158,
'sKey': 'UseRollCount' })))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'NowCount' }))) > 0 and cl_evcon.CheckTalent(oWarrior, oEventCB, (lambda *a: Func726(*a))):
        cl_action.CommonChangeSeasonSuitArg(oWarrior, oEventCB.GetCBLifeCycle(), 15158, 'UseRollCount', 1, 1)
        cl_evact.EventCBReduceTalentLevel(oWarrior, oEventCB, (lambda *a: Func726(*a)), 1)
        cl_evact.EventCBRewardTalent(oWarrior, oEventCB, 0, (lambda *a: Func726(*a)), 0, 0)
        cl_action.CommonSendSuitHandleInfo(oWarrior, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_ROLLTALENT, {
            1: (lambda *a: Func717(*a, **{
'sArg': 'NowCount' }) - 1) }, None)


class CPerform(CCustomPerform):
    m_SID = 15132
    m_Name = '#NT#奇门遁甲套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'MaxRollCount': 100,
        'GetRollCond': 2 }
    m_DieDisable = 0

