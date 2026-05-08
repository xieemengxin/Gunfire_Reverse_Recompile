# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6628.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6628.pyc
# Source Generated with Decompyle++
# File: p6628.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, SEASONSHOP_INITGOODSBEFORE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONSHOP, SEASONSHOP_INITGOODSBEFORE, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'S7DropModuleProp', {
        1: 40,
        2: 50,
        3: 50,
        4: 50,
        5: 30 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.EventCBSetCrystalPacketInfo(oWarrior, oEventCB, {
            1: {
                5: {
                    1212: 100 } } })


class CPerform(CCustomPerform):
    m_SID = 6628
    m_Name = '赛季7天赋25级'
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

