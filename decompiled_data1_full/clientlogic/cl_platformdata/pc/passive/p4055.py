# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4055.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4055.pyc
# Source Generated with Decompyle++
# File: p4055.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNOREIMMOBILIZE, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREIMMOBILIZE)
    cl_action.ImmunitySubSpdState(oWarrior, oLifeCycle)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'GuerrillaInterval', 3000)


class CPerform(CCustomPerform):
    m_SID = 4055
    m_Name = '二幕Boss血量切权重-全身'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'Threshold1': 60,
        'Threshold2': 1,
        'Threshold3': 50 }
    m_DieDisable = 0

