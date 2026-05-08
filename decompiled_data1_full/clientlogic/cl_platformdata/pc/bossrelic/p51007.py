# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51007.pyc
# Source Generated with Decompyle++
# File: p51007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform
from cl_newformula import Func201, Func304, Func341, Func361
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39140: 1,
        39141: 1,
        39153: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33473, 0, { }, 1, 0, 0)
    elif cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39065: 1 }, 1, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func341(*a))) >= 4:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33473, 0, { }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3904: 1,
        3902: 1 }):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CommonCheckGameReleaseFlag(oWarrior, oEventCB.GetCBLifeCycle()) == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39030: 1,
        39027: 1 }, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33473, 1200, { }, 1, 0, 0)
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51007,
'sArgs': '33473_AddShield' })), 33473, 'AddShield')


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39030: 1,
        39027: 1 }, 1, 0):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33473)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '33473_AddShield', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 / (20 + 10 * (Func361(*a, **{
'sid': 51007,
'sArgs': 'Count' }) * 1.5 - min(int(Func201(*a)), 4) - 1)) / 30))


class CPerform(CCustomPerform):
    m_SID = 51007
    m_Name = '陆吾试炼'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'Count': 1 }
    m_DieDisable = 1
    m_HeroRelic = 0
    m_LimitMonster = {
        3903: 1,
        3905: 1,
        3913: 1,
        3914: 1,
        3915: 1,
        3902: 1,
        3904: 1 }
    m_ExcludeMonster = { }

