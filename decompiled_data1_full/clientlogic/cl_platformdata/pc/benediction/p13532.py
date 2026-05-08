# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13532.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13532.pyc
# Source Generated with Decompyle++
# File: p13532.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func518

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33688, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, -1, 1, 0, 0)
    if not cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, '13532Bene'):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, '13532Bene', 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func518(*a, **{
'sAttr': 'AddLuckyHit' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '13532Bene', 0)


class CPerform(CCustomPerform):
    m_SID = 13532
    m_Name = '抱元守一'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 111

