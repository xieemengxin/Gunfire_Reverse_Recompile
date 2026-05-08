# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6097.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6097.pyc
# Source Generated with Decompyle++
# File: p6097.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func229

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) >= 36:
        cl_action.CommonChangeQualityProb(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_CURSE, 2000)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) >= 26 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) < 36:
        cl_action.CommonChangeQualityProb(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_NORMAL, -8000)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) >= 16 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) < 26:
        cl_action.CommonChangeQualityProb(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_LOW, -5000)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) >= 2 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func229(*a))) < 16:
        cl_action.CommonChangeQualityProb(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_LOW, -5000)


class CPerform(CCustomPerform):
    m_SID = 6097
    m_Name = '赌侠lv.5'
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

