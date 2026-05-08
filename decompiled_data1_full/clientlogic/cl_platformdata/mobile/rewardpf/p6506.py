# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6506.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6506.pyc
# Source Generated with Decompyle++
# File: p6506.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func308(*a) * 500 + 0), None)


class CPerform(CCustomPerform):
    m_SID = 6506
    m_Name = '基础护盾'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

