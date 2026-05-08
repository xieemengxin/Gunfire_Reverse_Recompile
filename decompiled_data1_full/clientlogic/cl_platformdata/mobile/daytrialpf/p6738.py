# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6738.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6738.pyc
# Source Generated with Decompyle++
# File: p6738.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_PASSLEVEL, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        if cl_evcon.CheckLayerAndLevel(oWarrior, oEventCB, 1, 1) or cl_evcon.CheckLayerAndLevel(oWarrior, oEventCB, 1, 2) or cl_evcon.CheckLayerAndLevel(oWarrior, oEventCB, 1, 3) or cl_evcon.CheckLayerAndLevel(oWarrior, oEventCB, 1, 4):
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) + 0)) >= 450:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, -450, 1, JUMPFIGURE_PASSLEVEL, -450, None)
            else:
                cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_PASSLEVEL, -450, None)
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) + 0)) >= 600:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, -600, 1, JUMPFIGURE_PASSLEVEL, -600, None)
        else:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_PASSLEVEL, -600, None)
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) + 0)) >= 900:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, -900, 1, JUMPFIGURE_PASSLEVEL, -900, None)
        else:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_PASSLEVEL, -900, None)


class CPerform(CCustomPerform):
    m_SID = 6738
    m_Name = '关卡目标达成获得铜币'
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

