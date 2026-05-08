# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13501.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13501.pyc
# Source Generated with Decompyle++
# File: p13501.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT
from cl_newformula import Func379

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32046, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 5000 - Func379(*a) * 50), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 13501
    m_Name = '百战伤疤'
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
    m_Career = None

