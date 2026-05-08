# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4381.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4381.pyc
# Source Generated with Decompyle++
# File: p4381.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 3000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4381
    m_Name = '玉追龙新迭代被动'
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

