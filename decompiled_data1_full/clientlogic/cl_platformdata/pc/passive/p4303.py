# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4303.pyc
# Source Generated with Decompyle++
# File: p4303.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717, Func762

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckWarCycle(oWarrior, oLifeCycle) >= 10:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Energy() >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('pf_4303') * 6000 + 6000 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('pf_4303') < 4:
        cl_action.CommonRandomAddStateAndSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), '7997|7998|7999|8000', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_4303'))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_4303', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_4303') + 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf4303') >= 4:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func762(*a, **{
'iPFSID': 14415,
'sKey': 'Wily_Boss_S',
'iSuperNum': Func717(*a, **{
'sArg': 'pf_4303' }) }) * 100)):
        cl_action.CommonRandomAddStateAndSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), '7997|7998|7999|8000|8136|8137|8138', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_4303'))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_4303', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_4303') + 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_4303') >= 7:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1)


class CPerform(CCustomPerform):
    m_SID = 4303
    m_Name = '【诡谲雪山】妖王强化技能被动'
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

