# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50021.pyc
# Source Generated with Decompyle++
# File: p50021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_newformula import Func600

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12019)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 'AttRatio', (lambda *a: Func600(*a) * 20), None)


class CPerform(CCustomPerform):
    m_SID = 50021
    m_Name = '荆棘外壳'
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
    m_GrowPF = [
        50015,
        50016,
        50017,
        50018,
        50019,
        50020]
    m_DamagePF = [
        12019]

