# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51562.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51562.pyc
# Source Generated with Decompyle++
# File: p51562.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, JUMPFIGURE_BUYGOODS
from cl_newformula import Func529, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseCash', 2)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 3000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseCash', 4)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 4000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseCash', 6)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 5000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: Func529(*a) * Func717(*a, **{
'sArg': 'BaseCash' })), 0, JUMPFIGURE_BUYGOODS, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51562
    m_Name = '#NT#上限提升'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

