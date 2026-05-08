# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13515.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13515.pyc
# Source Generated with Decompyle++
# File: p13515.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func303, Func361, Func410, Func443

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32547, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1312, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1468, 500, { }, 1, 1, None)
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: Func443(*a)), 1468, 'ParentActnum')
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1468, (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * Func303(*a, **{
'sAttr': 'BulletSpeed' })), 0, None, None)
        cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32505, (lambda *a: -Func361(*a, **{
'sid': 13515,
'sArgs': 'AddStateCount' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddStateCount', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 32505):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 1468) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32505 }))) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 13515,
'sArgs': 'LastNum' }))):
            cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, 1, 1468, 'Num')
            if cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 1468, 'Num') >= 2 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 13515,
'sArgs': 'AddStateCount' }))) < 3:
                cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, -2, 1468, 'Num')
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddStateCount', (lambda *a: Func361(*a, **{
'sid': 13515,
'sArgs': 'AddStateCount' }) + 1))
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32505, 1)
                cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 1, 32505, 'NotSend')
                cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32505, 1, -1, -1, None)
                cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 32505, 'NotSend')
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastNum', (lambda *a: Func410(*a, **{
'sid': 32505 })))


class CPerform(CCustomPerform):
    m_SID = 13515
    m_Name = '剑术精研'
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
    m_Career = 109

