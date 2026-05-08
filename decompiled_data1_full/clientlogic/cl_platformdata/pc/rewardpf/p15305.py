# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15305.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15305.pyc
# Source Generated with Decompyle++
# File: p15305.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ENERGY_RS_LIONENHANCETHROW
from cl_newformula import Func538

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChangeEnergyReason(oWarrior, oEventCB, ENERGY_RS_LIONENHANCETHROW):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func538(*a))) >= 18000:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'AddKeepTimeRatio', 100, 0)
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func538(*a))) >= 12000:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'AddKeepTimeRatio', 50, 0)


class CPerform(CCustomPerform):
    m_SID = 15305
    m_Name = '缚影长续'
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

