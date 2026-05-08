# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4089.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4089.pyc
# Source Generated with Decompyle++
# File: p4089.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
from cl_commondefines import WARRIOR_BOSSDM, FIGHT_KEY_WUDI
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_math
from cl_platformdata.custom.passive.customaction import CustomAction4089 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func341

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, { })
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 39065, { })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7076, 0, { }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetPhase(oWarrior, oLifeCycle, (lambda *a: Func341(*a) + 1))
    cl_action.CommonUsePerform(oWarrior, oLifeCycle, 39065, { })


class CPerform(CCustomPerform):
    m_SID = 4089
    m_Name = '三幕Boss无敌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

