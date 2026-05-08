# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15186.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15186.pyc
# Source Generated with Decompyle++
# File: p15186.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func410, Func651
from cl_commondefines import NWARRIOR_NPC_LIMITGOLDENCUP

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33483, 0, { }, 1)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if (cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'NPC' }))) == 1027 or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'NPC' }))) == 1028) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventCBReplaceCreateNpc(oWarrior, oEventCB, 30011061)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_LIMITGOLDENCUP):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 33483 }))) > 0:
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33483, 0)
            cl_action.CommonAddTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1, 1)
        else:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33483, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 15186
    m_Name = '以小博大'
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

