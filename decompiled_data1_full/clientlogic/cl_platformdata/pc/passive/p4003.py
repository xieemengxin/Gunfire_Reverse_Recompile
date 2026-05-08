# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4003.pyc
# Source Generated with Decompyle++
# File: p4003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, WARRIOR_BOSS, WARRIOR_ELITE
from cl_newformula import Func589, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REDUCESPEEDED, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REDUCESPEEDEDEND, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEEDED, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEEDEDEND, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDIMMOBILIZE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CLEARIMMOBILIZE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BOSS):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BaseDam', 50)
    elif cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BaseDam', 150)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BaseDam', 300)
    if cl_condition.CheckIsReducingSpeed(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SourceCnt', 1)
    if cl_condition.CheckIsReducingActionSpeed(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SourceCnt', 1)
    if cl_condition.CheckAddImmobilize(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SourceCnt', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SourceCnt') > 0:
        if cl_condition.CheckAddImmobilize(oWarrior, oEventCB.GetCBLifeCycle()):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' }) * 2))
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' })))
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 5)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SourceCnt', 1)
    if cl_condition.CheckAddImmobilize(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' }) * 2))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' })))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SourceCnt') == 1:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 5)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SourceCnt', -1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SourceCnt') == 0:
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
    elif cl_condition.CheckAddImmobilize(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' }) * 2))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' })))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBSetAttackTargetBySceneAureoleOwner(oWarrior, oEventCB, 'seasonsuit15209')
    cl_evact.EventCBTriggerGroupByAttackTarget(oWarrior, oEventCB, 6)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func717(*a, **{
'sArg': 'Dam' }) // 10000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4003
    m_Name = '#NT#雪上加霜光环'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

