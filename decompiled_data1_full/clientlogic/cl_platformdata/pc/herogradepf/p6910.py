# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6910.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6910.pyc
# Source Generated with Decompyle++
# File: p6910.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, PF_SUBMSG_CAREERPF, SKILLCACHE_PERFORMMODE
from cl_newformula import Func336, Func611, Func677

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1324, 'SlaySubCD', 1, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'OverFlowDam', (lambda *a: Func611(*a)), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'OverFlowDam', (lambda *a: Func677(*a)), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0) and cl_evcon.EventCBCheckSkillCache(oWarrior, oEventCB, SKILLCACHE_PERFORMMODE) == 2:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func336(*a, **{
'sKey': 'OverFlowDam' }) * 0.75), 0, '')


class CPerform(CCustomPerform):
    m_SID = 6910
    m_Name = '#NT#处决大师lv.5'
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

