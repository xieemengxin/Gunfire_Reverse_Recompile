# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6735.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6735.pyc
# Source Generated with Decompyle++
# File: p6735.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import JUMPFIGURE_BUYGOODS, JUMPFIGURE_UPGRADEWEAPON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetOwnerWeaponUpgradeGenCash(oWarrior, oLifeCycle)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECASTWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_INSCRIPTION, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, 0, 1, JUMPFIGURE_BUYGOODS, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, 0, 1, JUMPFIGURE_UPGRADEWEAPON, 0, None)


class CPerform(CCustomPerform):
    m_SID = 6735
    m_Name = '商品和强化装备获取对应的铜币'
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

