# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4155.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4155.pyc
# Source Generated with Decompyle++
# File: p4155.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, HP_RADIO_SUB
from cl_newformula import Func205

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func205(*a) * 5 + 25), HP_RADIO_SUB, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonSetSkillCheckArgs(oWarrior, oLifeCycle, 30, 70)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 4)


class CPerform(CCustomPerform):
    m_SID = 4155
    m_Name = '石巨人-阶段3'
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

