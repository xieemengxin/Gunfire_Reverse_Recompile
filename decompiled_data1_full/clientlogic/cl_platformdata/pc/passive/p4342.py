# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4342.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4342.pyc
# Source Generated with Decompyle++
# File: p4342.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func303, Func341, Func565

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a))) == 1 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func565(*a, **{
'sAttr': 'ElementType' }))) != cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'ElementType' }))):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'ElementType', (lambda *a: Func565(*a, **{
'sAttr': 'ElementType' })), 0)
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', (lambda *a: Func565(*a, **{
'sAttr': 'DebuffProb' })), 0)


class CPerform(CCustomPerform):
    m_SID = 4342
    m_Name = '御灵师仆从E1'
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

