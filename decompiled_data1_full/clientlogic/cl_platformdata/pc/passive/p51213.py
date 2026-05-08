# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51213.pyc
# Source Generated with Decompyle++
# File: p51213.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_ATTACK, PF_TYPE_CONSHOOT, WAND_SUBMSG_FINISHCONDITION, WAND_SUBMSG_TRIGGERACTION
from cl_newformula import Func361, Func451

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INVISIBLE_END, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 4, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'Speed', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level1Speed' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'BaseAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level1BaseDamAdd' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'ConAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level1DamAdd' })), None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INVISIBLE_END, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 4, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'Speed', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level2Speed' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'BaseAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level2BaseDamAdd' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'ConAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level2DamAdd' })), None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INVISIBLE_END, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_FINISHCONDITION, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 4, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'Speed', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level3Speed' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'BaseAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level3BaseDamAdd' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51213, 'ConAdd', (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'Level3DamAdd' })), None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 0) or cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'DamFactor'):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func451(*a, **{
'sid': 33556,
'sAttr': 'Dam' })), 0, DAM_MASK_ELEMENT, '')
    else:
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func451(*a, **{
'sid': 33556,
'sAttr': 'Dam' })), 0, DAM_MASK_ELEMENT, 1, None)
    if cl_condition.CommonCheckItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51272'):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33558, (lambda *a: 200 + min(400, Func361(*a, **{
'sid': 51213,
'sArgs': 'ConNum' }) * 10)), {
            'Dam': (lambda *a: Func451(*a, **{
'sid': 33556,
'sAttr': 'Dam' })) }, 0, 0, 0)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33558, 200, {
            'Dam': (lambda *a: Func451(*a, **{
'sid': 33556,
'sAttr': 'Dam' })) }, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'ConNum', 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamAdd', (lambda *a: min(30000, Func361(*a, **{
'sid': 51213,
'sArgs': 'ConNum' }) * Func361(*a, **{
'sid': 51213,
'sArgs': 'ConAdd' }) + Func361(*a, **{
'sid': 51213,
'sArgs': 'BaseAdd' }))))
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33556) == 0 and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33558) == 0:
        cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'DamAdd' }) // 100))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamAdd', (lambda *a: min(30000, Func361(*a, **{
'sid': 51213,
'sArgs': 'ConNum' }) * Func361(*a, **{
'sid': 51213,
'sArgs': 'ConAdd' }) + Func361(*a, **{
'sid': 51213,
'sArgs': 'BaseAdd' }))))
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33556) == 0 and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33558) == 0:
        cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'DamAdd' }) // 100))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ConNum', 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamAdd', (lambda *a: min(30000, Func361(*a, **{
'sid': 51213,
'sArgs': 'ConNum' }) * Func361(*a, **{
'sid': 51213,
'sArgs': 'ConAdd' }) + Func361(*a, **{
'sid': 51213,
'sArgs': 'BaseAdd' }))))
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33556) == 0 and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33558) == 0:
        cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'DamAdd' }) // 100))


class CPerform(CCustomPerform):
    m_SID = 51213
    m_Name = '#NT#隐身法杖被动'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'Level1Speed': 3000,
        'Level2Speed': 4000,
        'Level3Speed': 5000,
        'Level1BaseDamAdd': 4000,
        'Level2BaseDamAdd': 6000,
        'Level3BaseDamAdd': 9000,
        'Level1DamAdd': 2000,
        'Level2DamAdd': 3000,
        'Level3DamAdd': 4500 }
    m_DieDisable = 0

