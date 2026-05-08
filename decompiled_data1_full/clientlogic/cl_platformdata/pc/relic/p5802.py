# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5802.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5802.pyc
# Source Generated with Decompyle++
# File: p5802.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func548

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSkillCopyWeaponTrajectoryDamage(oWarrior, oEventCB, (lambda *a: 10000 - Func548(*a) * 350), 0, -5000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSkillCopyWeaponTrajectoryDamage(oWarrior, oEventCB, (lambda *a: 10000 - Func548(*a) * 350), 0, -2000)


class CPerform(CCustomPerform):
    m_SID = 5802
    m_Name = '福无双至'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

