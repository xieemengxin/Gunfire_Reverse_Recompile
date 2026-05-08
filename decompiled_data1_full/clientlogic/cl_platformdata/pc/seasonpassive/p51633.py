# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51633.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51633.pyc
# Source Generated with Decompyle++
# File: p51633.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddDam', 4000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubFillTime', 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddDam', 8000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubFillTime', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddDam', 12000, 0)
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddAttSpeed', 600, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubFillTime', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddDam', 16000, 0)
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, '51633AddAttSpeed', 1500, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubFillTime', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39691, 300, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'FillTime', 0, (lambda *a: -Func717(*a, **{
'sArg': 'SubFillTime' })), 0)


class CPerform(CCustomPerform):
    m_SID = 51633
    m_Name = '充能弹夹'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

