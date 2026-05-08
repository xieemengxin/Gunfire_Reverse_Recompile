# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6092.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6092.pyc
# Source Generated with Decompyle++
# File: p6092.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_SUBMSG_CAREERPF
from cl_newformula import Func3, Func711

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_USEPERFORM_BEFORE, -1, 2, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 1):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'p6092', 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p6092', None) == 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1317, 1, 0) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32885) == 0:
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 100)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32885, 1500, { }, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddRatio', (lambda *a: Func711(*a, **{
'iQuality': 'QUALITY_TYPE_LOW' }) * 15 + Func711(*a, **{
'iQuality': 'QUALITY_TYPE_NORMAL' }) * 20 + Func711(*a, **{
'iQuality': 'QUALITY_TYPE_HIGH' }) * 25 + Func711(*a, **{
'iQuality': 'QUALITY_TYPE_CURSE' }) * 30))
        cl_evact.EventCBAddComb(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddRatio') // 100)
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func3(*a, **{
'a': int(oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddRatio')),
'b': 100 }))):
            cl_evact.EventCBAddComb(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 6092
    m_Name = '赌侠lv.2'
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

