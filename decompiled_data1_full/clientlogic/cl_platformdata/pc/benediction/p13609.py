# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13609.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13609.pyc
# Source Generated with Decompyle++
# File: p13609.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_DICE
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventRecycleDropType(oWarrior, oEventCB, NWARRIOR_DROP_DICE) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 30):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'QL' }))) == 1:
            cl_evact.EventCBAddUpQualityDice(oWarrior, oEventCB, 1, 1, 9723)
        else:
            cl_evact.EventCBAddUpQualityDice(oWarrior, oEventCB, 1, 1, 9724)


class CPerform(CCustomPerform):
    m_SID = 13609
    m_Name = '强化回收'
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
    m_Career = None

