# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6526.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6526.pyc
# Source Generated with Decompyle++
# File: p6526.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import BUYRULE_REFRESHFREE
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_REFRESHFREE, (lambda *a: Func308(*a) * 1 + 0))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_REFRESHFREE, (lambda *a: Func308(*a) * 1 + 0))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddHeroBuyRule(oWarrior, oLifeCycle, BUYRULE_REFRESHFREE, (lambda *a: Func308(*a) * 1 + 0))


class CPerform(CCustomPerform):
    m_SID = 6526
    m_Name = '商品刷新'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

