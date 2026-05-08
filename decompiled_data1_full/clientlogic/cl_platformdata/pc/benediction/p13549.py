# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13549.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13549.pyc
# Source Generated with Decompyle++
# File: p13549.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_ROLL_RELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 1, 0, 0)
    cl_action.CommonChangeMaxRelicRollNum(oWarrior, oLifeCycle, 1)
    cl_action.CommonChangeRollRelicCnt(oWarrior, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 32917 })))
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 32917, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'Level', 2)
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'UpGrade', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'load', 0) == 0 and cl_evcon.CheckReason(oWarrior, oEventCB, 'ExchangeRewardChooseTalentGame', 1) == 0:
        cl_action.CommonChangeRollRelicCnt(oWarrior, oEventCB.GetCBLifeCycle(), 1)


class CPerform(CCustomPerform):
    m_SID = 13549
    m_Name = '险中求富'
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
    m_Career = 113

