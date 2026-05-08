# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4316.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4316.pyc
# Source Generated with Decompyle++
# File: p4316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4316 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'MonsterGroup': (39021, 39022, 39023),
        'OnlyPerform': (9514, 0),
        'Key': 'passive-4316',
        'OnlyObject': (1315, 1319, 8503),
        'IgnoreSkill': (9795, 0) })


class CPerform(CCustomPerform):
    m_SID = 4316
    m_Name = '罗睺和弱点伤害管理'
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

