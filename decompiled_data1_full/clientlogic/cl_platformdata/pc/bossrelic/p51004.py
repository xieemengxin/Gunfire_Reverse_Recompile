# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51004.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51004.pyc
# Source Generated with Decompyle++
# File: p51004.pyc (Python 3.6)

from cl_platformdata.custom.monsterrelic.customaction import CustomActionBossSummon as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 1000, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHasLockEnemy(oWarrior, oEventCB.GetCBLifeCycle()):
        CustomAction(oWarrior, oEventCB, {
            'sid': 1076,
            'min': 8,
            'max': 15,
            'gap': 5,
            'maxnum': 6,
            'Radius': 0.5,
            'num': 1,
            'height': 1.5,
            'delay': 100,
            'effect': 1036 })


class CPerform(CCustomPerform):
    m_SID = 51004
    m_Name = '夜姬丸试炼'
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
    m_DieDisable = 1
    m_HeroRelic = 0
    m_LimitMonster = { }
    m_ExcludeMonster = {
        3905: 1,
        3906: 1 }

