# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6535.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6535.pyc
# Source Generated with Decompyle++
# File: p6535.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_AMULET, OBJ_ATTACK, SUBLIME_DOUBLE_DAMAGE
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('6535Cnt') >= 30 or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func308(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '6535Cnt', 0)
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, 0, '')
        cl_evact.EventCBAddShowTipsEffect(oWarrior, oEventCB, SUBLIME_DOUBLE_DAMAGE)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '6535Cnt', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET):
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('6535Cnt') >= 30 or cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func308(*a))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '6535Cnt', 0)
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, 0, '')
            cl_evact.EventCBAddShowTipsEffect(oWarrior, oEventCB, SUBLIME_DOUBLE_DAMAGE)
        else:
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '6535Cnt', 1)


class CPerform(CCustomPerform):
    m_SID = 6535
    m_Name = '秘能大师'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

