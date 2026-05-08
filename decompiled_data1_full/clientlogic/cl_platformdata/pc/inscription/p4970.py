# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4970.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4970.pyc
# Source Generated with Decompyle++
# File: p4970.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK, OBJ_VICTIM, PF_TYPE_CAREERPF
from cl_newformula import Func751, Func756

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9407, 1, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33587, 0, {
            'ActNum': cl_evact.EventGetSkillActNum(oWarrior, oEventCB),
            'ExplodePos': cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'CurPos') }, 1, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1971, 1, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_WEAPON, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'h214_Hit', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'h214_Hit') >= 3:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExplodePos', cl_evact.EventCBGetTargetPos(oWarrior, oEventCB))
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'h214_InCD') == 0:
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'h214_InCD', 1)
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'h214_Hit', 0)
                cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1971, {
                    'vStart': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExplodePos') }, {
                    'Radius': (lambda *a: Func756(*a, **{
'sAttr': 'Radius' }) * 100 + 400) }, (lambda *a: Func751(*a)))
                cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, 50, 0, 1, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'h214_InCD', 0)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'h214_Hit') >= 3 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'h214_InCD') == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'h214_InCD', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'h214_Hit', 0)
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1971, {
            'vStart': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExplodePos') }, {
            'Radius': (lambda *a: Func756(*a, **{
'sAttr': 'Radius' }) * 100 + 400) }, (lambda *a: Func751(*a)))
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, 50, 0, 1, { })


class CPerform(CCustomPerform):
    m_SID = 4970
    m_Name = '狱裂骨龙2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (1971,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1407,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

