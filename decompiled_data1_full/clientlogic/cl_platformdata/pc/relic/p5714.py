# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5714.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5714.pyc
# Source Generated with Decompyle++
# File: p5714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1526, -1, -1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: max(100, Func305(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0)), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
        cl_evact.PassiveAddHoldWeaponBagBullet(oWarrior, oEventCB, 5, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1526, 100, { }, 1, -1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1526, -1, -1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: max(100, Func305(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0)), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: max(100, Func305(*a, **{
'sAttr': 'ShieldMax' }) * 1 / 100 + 0)), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, -1, None)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: max(100, Func305(*a, **{
'sAttr': 'ArmorMax' }) * 1 / 100 + 0)), CURE_TYPE_PERFORM | DAM_USE_ARMOR, 0, -1, None)
        cl_evact.PassiveFillBullet(oWarrior, oEventCB, 5, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1526, 100, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 5714
    m_Name = '元素馈赠'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

