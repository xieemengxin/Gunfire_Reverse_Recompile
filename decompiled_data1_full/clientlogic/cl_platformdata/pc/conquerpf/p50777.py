# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/conquerpf/p50777.pyc
# RelativePath: clientlogic/cl_platformdata/pc/conquerpf/p50777.pyc
# Source Generated with Decompyle++
# File: p50777.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERSISTENCE, OBJ_VICTIM
from cl_newformula import Func223

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'PF50777') == 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1935, 0, 0) == 0 and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'PF50777', 300)
        cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1935, 1, {
            'ExtraDamage': (lambda *a: 5000 * Func223(*a)) })


class CPerform(CCustomPerform):
    m_SID = 50777
    m_Name = '玩家增益2'
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

