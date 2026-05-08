# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16084.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16084.pyc
# Source Generated with Decompyle++
# File: p16084.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func304, Func347

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })))
    cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' })))
    cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' })))
    cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4502, (lambda *a: Func347(*a, **{
'sid': 4502 })), 0)
    cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4503, (lambda *a: Func347(*a, **{
'sid': 4503 })), 0)
    cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4504, (lambda *a: Func347(*a, **{
'sid': 4504 })), 0)


class CPerform(CCustomPerform):
    m_SID = 16084
    m_Name = '满血复活'
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

