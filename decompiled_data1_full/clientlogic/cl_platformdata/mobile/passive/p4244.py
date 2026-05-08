# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4244.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4244.pyc
# Source Generated with Decompyle++
# File: p4244.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import BUTTON_E, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_UNSEND_CGEVENT, -1, 1, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_UNSEND_CLIENTBUTTON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'RShield', 0, -10000)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'HPMax' }) // 2))
    cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'ShieldMax' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'RShield', 10, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckIsPointButton(oWarrior, oEventCB, BUTTON_E) and cl_evcon.CheckPerformCodeTime(oWarrior, oEventCB, 1302) == 0:
        cl_action.CommonPerformAddColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1302)


class CPerform(CCustomPerform):
    m_SID = 4244
    m_Name = '新手引导战场初始被动'
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

