# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2915.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2915.pyc
# Source Generated with Decompyle++
# File: p2915.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func331

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32908, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, -1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32908, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, -1, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32908, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, -1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32908, (lambda *a: Func331(*a, **{
'sid': 2915 }) * 2 + 4), -1, None)


class CPerform(CCustomPerform):
    m_SID = 2915
    m_Name = '绵延不绝'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 110

