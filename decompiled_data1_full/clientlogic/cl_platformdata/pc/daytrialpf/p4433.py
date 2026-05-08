# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4433.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4433.pyc
# Source Generated with Decompyle++
# File: p4433.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_KILLMONSTER
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= 10:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, -10, 0, JUMPFIGURE_KILLMONSTER, 0, None)
    else:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 0, JUMPFIGURE_KILLMONSTER, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4433
    m_Name = '每触发一次元素异常扣10铜币'
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

