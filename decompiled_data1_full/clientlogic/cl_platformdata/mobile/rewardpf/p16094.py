# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16094.pyc
# Source Generated with Decompyle++
# File: p16094.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction16094 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_BUYGOODS
from cl_newformula import Func207, Func441

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        'iGroup': 0,
        'iPerform': 16094 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a))) < 400 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func441(*a))) > 1:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: 400 - Func207(*a)), 0, JUMPFIGURE_BUYGOODS, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 16094
    m_Name = '破产津贴'
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

