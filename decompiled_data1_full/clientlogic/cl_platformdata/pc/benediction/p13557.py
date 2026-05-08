# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13557.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13557.pyc
# Source Generated with Decompyle++
# File: p13557.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33287, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'Trigger', None) == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1918: 1,
        1921: 1 }, 1, 0):
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'Trigger', 300, None)
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 900 * (100 + Func410(*a, **{
'sid': 33287 }))), 0, '')
        cl_action.CommonModifyInkValue(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 2 * (100 + Func410(*a, **{
'sid': 33287 })) // 100), '', { })


class CPerform(CCustomPerform):
    m_SID = 13557
    m_Name = '驰墨涤魂'
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
    m_Career = 117

