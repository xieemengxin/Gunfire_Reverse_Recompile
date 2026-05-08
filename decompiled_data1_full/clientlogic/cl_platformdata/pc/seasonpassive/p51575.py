# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51575.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51575.pyc
# Source Generated with Decompyle++
# File: p51575.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func332, Func717, Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12040)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 20000 + Func332(*a) * 7500))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttTimes', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12040)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 30000 + Func332(*a) * 10000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttTimes', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12040)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 40000 + Func332(*a) * 10000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttTimes', 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12040)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 50000 + Func332(*a) * 15000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttTimes', 7)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12040)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 60000 + Func332(*a) * 15000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttTimes', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12040, '', 0, 1, {
            'Att': (lambda *a: Func717(*a, **{
'sArg': 'Att' })),
            'AttTimes': (lambda *a: Func717(*a, **{
'sArg': 'AttTimes' })) })
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51575,
            'Item': (lambda *a: Func804(*a)),
            'TriggerPerformID': 12040 })


class CPerform(CCustomPerform):
    m_SID = 51575
    m_Name = '#NT#腐蚀尖刺'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

