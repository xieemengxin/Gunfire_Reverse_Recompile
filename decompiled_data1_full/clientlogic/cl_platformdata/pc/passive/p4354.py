# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4354.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4354.pyc
# Source Generated with Decompyle++
# File: p4354.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF
from cl_newformula import Func304, Func311

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7152, 1, -1) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })), 0, 0, '')
    elif cl_evcon.CheckStateStatistics(oWarrior, oEventCB, 32850, 'HpBeforeDie'):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, cl_evact.EventCBGetStateStatistics(oWarrior, oEventCB, 32850, 'HpBeforeDie'), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.EventCBCheckTriggerOwner(oWarrior, oEventCB):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func311(*a) - 100))


class CPerform(CCustomPerform):
    m_SID = 4354
    m_Name = '心有灵犀'
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

