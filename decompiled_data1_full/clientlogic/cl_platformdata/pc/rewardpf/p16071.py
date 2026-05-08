# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16071.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16071.pyc
# Source Generated with Decompyle++
# File: p16071.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PLAY_TYPE_MULTI
from cl_newformula import Func522

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'SaveTime', -6000, 0, -1)
    if cl_condition.CheckWarPlayType(oWarrior, oLifeCycle, PLAY_TYPE_MULTI):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.CheckHasSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Rewardpf16071'):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Rewardpf16071', 1)
        cl_action.CommonSetDyingSecond(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func522(*a) * 130 / 100))


class CPerform(CCustomPerform):
    m_SID = 16071
    m_Name = '战地医生'
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

