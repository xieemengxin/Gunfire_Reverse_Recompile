# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51665.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51665.pyc
# Source Generated with Decompyle++
# File: p51665.pyc (Python 3.6)

from cl_platformdata.custom.passive.customaction import CustomAction51665_1 as CustomAction1, CustomAction51665_2 as CustomAction2
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7ITEM_REFRESH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, S7ITEM_REFRESH, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, S7ITEM_REFRESH, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, S7ITEM_REFRESH, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction1(oWarrior, oEventCB, {
        'TarPoint': 6 })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction2(oWarrior, oEventCB, {
        'TarPoint': 6 })


class CPerform(CCustomPerform):
    m_SID = 51665
    m_Name = '通用-双生模仿'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

