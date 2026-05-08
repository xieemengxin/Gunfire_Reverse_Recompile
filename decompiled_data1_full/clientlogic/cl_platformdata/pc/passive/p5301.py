# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5301.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5301.pyc
# Source Generated with Decompyle++
# File: p5301.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction5301 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func331, Func336, Func360, Func361, Func433

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33068, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33249, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_INTERACTTRANSFER, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1431: 1,
        12030: 1 }, 1, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'CartoonFlag' }))) == 0:
        CustomAction(oWarrior, oEventCB, {
            'FullX': (lambda *a: Func360(*a, **{
'sid': 1431,
'sAttr': 'Radius' })),
            'HalfY': 2,
            'HeroStateTime': 0,
            'MonsterStateTime': 0,
            'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
            'StayTime': (lambda *a: Func360(*a, **{
'sid': 1431,
'sAttr': 'KeepTime' })),
            'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })) })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'TalentLevel' }))) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' }))):
        if cl_evcon.CheckPerformIsInkPerform(oWarrior, oEventCB):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'InkDamCount', 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('InkDamCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ThresholdCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'InkDamCount', 0)
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TalentLevel', 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33274, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33044):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '33044RemainRatio', (lambda *a: Func433(*a, **{
'sid': 33044 }) * 10000 // 100))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsReturn', 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsReturn'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsReturn', 0)
        cl_action.CommonSubCareerPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': '33044RemainRatio' })))


class CPerform(CCustomPerform):
    m_SID = 5301
    m_Name = '水墨大师被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'InkDamCount': 0,
        'ThresholdCount': 8,
        'MaxLevel': 400 }
    m_DieDisable = 1

