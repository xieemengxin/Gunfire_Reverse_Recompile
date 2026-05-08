# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40022.pyc
# Source Generated with Decompyle++
# File: p40022.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_FIGHT, TYPE_RELIFE_TASK, WARRIOR_ELITE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.EventCBGetTargetByEventMonster(oWarrior, oEventCB)
        if cl_evcon.EventCBCheckIsMonsterGroup(oWarrior, oEventCB, {
            20041: 1,
            20042: 1,
            22022: 1,
            22211: 1,
            22212: 1,
            22221: 1,
            22222: 1,
            22231: 1,
            22232: 1,
            22241: 1,
            22242: 1,
            23411: 1,
            23412: 1,
            23421: 1,
            23422: 1,
            23431: 1,
            23432: 1,
            30041: 1,
            32822: 1,
            32824: 1,
            31651: 1,
            31652: 1 }) == 0:
            if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
                cl_evact.EventCBSetTargetRelifeInfo(oWarrior, oEventCB, TYPE_RELIFE_TASK, 230, 1, 3, 15, 15, 15, 1, {
                    'Elite': 10,
                    'Normal': 50 })
            else:
                cl_evact.EventCBSetTargetRelifeInfo(oWarrior, oEventCB, TYPE_RELIFE_TASK, 230, 1, 3, 30, 30, 30, 1, {
                    'Elite': 10,
                    'Normal': 50 })
            if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32927, 0, 0, 0):
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32927, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 40022
    m_Name = '天降大任-轮回不止2特殊效果'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

