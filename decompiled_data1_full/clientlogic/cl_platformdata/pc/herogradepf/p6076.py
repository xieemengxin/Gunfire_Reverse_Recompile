# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6076.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6076.pyc
# Source Generated with Decompyle++
# File: p6076.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func336, Func430

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, -1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf6079', (lambda *a: (Func430(*a, **{
'sid': 32774 }) // 100) * 100), None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf6079', None) > 0:
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func336(*a, **{
'sKey': 'pf6079' }) * 0.1))


class CPerform(CCustomPerform):
    m_SID = 6076
    m_Name = '改版卫士lv.1'
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

