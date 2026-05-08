# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15173.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15173.pyc
# Source Generated with Decompyle++
# File: p15173.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func361, Func449

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonoDisableTalent(oWarrior, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamageFactor', (lambda *a: Func449(*a) * 40))
    cl_action.PassiveSendSuitDamageFactor(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 15173,
'sArgs': 'DamageFactor' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 15173,
'sArgs': 'DamageFactor' }) * 100), 0, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveSendSuitDamageFactor(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 15173,
'sArgs': 'DamageFactor' })))


class CPerform(CCustomPerform):
    m_SID = 15173
    m_Name = '#NT#登峰造极套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

