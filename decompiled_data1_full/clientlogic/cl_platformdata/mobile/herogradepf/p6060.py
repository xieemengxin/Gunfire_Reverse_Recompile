# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6060.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6060.pyc
# Source Generated with Decompyle++
# File: p6060.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, WARRIOR_BARRIER
from cl_newformula import Func204, Func205, Func221, Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'EnergyMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * ((Func205(*a) - 1) * 10 / 100 + Func221(*a) * 5 / 100)), None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventGetTargetBySummonType(oWarrior, oEventCB, WARRIOR_BARRIER)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func221(*a))) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32465, 0, {
            'DamReduce': (lambda *a: ((Func205(*a) - 1) * 10 / 100) * (1 + (Func204(*a) - 1) * 5 / 100) * 10000) }, 1, 0, None)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32465, 0, {
            'DamReduce': (lambda *a: min(((Func205(*a) - 1) * 10 / 100 + (1 - pow(0.95, Func221(*a)))) * (1 + (Func204(*a) - 1) * 5 / 100) * 10000, 9000)) }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6060
    m_Name = '卫士lv.5'
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

