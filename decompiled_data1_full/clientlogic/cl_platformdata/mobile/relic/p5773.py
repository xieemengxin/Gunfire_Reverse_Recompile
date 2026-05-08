# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5773.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5773.pyc
# Source Generated with Decompyle++
# File: p5773.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }))) > 0 or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) > 0 or cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'Add', -1):
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
        cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Minus', None, None)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Add', 1)
    elif not cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'Minus', -1):
        pass
    if not oWarrior.GetShieldStatus():
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), -1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
        cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Add', None, None)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Minus', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }))) > 0 or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) > 0 or cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'Add', -1):
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
        cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Minus', None, None)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Add', 1)
    elif not cl_evcon.CheckTargetHasMark(oWarrior, oEventCB, 'Minus', -1):
        pass
    if not oWarrior.GetShieldStatus():
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
        cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Add', None, None)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Minus', None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }))) == 0:
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
        cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Minus', None, None)
        cl_evact.EventSetTargetMark(oWarrior, oEventCB, 'Add', 1)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Add', None, None)
    cl_evact.EventClearTargetMark(oWarrior, oEventCB, 'Minus', None, None)


class CPerform(CCustomPerform):
    m_SID = 5773
    m_Name = '强化蛋壳'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

