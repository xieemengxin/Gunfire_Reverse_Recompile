# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5787.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5787.pyc
# Source Generated with Decompyle++
# File: p5787.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_USE_ARMOR, DAM_USE_SHIELD, OBJ_SELF, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1169, 1, None, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1169, 1000, { }, 1, None, None)
        cl_evact.EventCBRecoverDam(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 40 / 100 + 0), DAM_USE_SHIELD)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1169, 1, None, None) == 0:
        cl_evact.EventCBRecoverDam(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }) * 40 / 100 + 0), DAM_USE_ARMOR)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1169, 1000, { }, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1169, 1, None, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1169, 500, { }, 1, None, None)
        cl_evact.EventCBRecoverDam(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 100 / 100 + 0), DAM_USE_SHIELD)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1169, 1, None, None) == 0:
        cl_evact.EventCBRecoverDam(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }) * 100 / 100 + 0), DAM_USE_ARMOR)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1169, 500, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 5787
    m_Name = '备用护盾'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

