# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13510.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13510.pyc
# Source Generated with Decompyle++
# File: p13510.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1305, 'ColdTime', -5000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, 1, 1):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1469, (lambda *a: 1000 + Func410(*a, **{
'sid': 1567 })), { }, 1, -1, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1469, 1, -1)


class CPerform(CCustomPerform):
    m_SID = 13510
    m_Name = '电光神曜'
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
    m_Career = 104

