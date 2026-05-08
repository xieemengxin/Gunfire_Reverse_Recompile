# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3610.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3610.pyc
# Source Generated with Decompyle++
# File: p3610.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3610 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func308, Func331, Func360, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'ThresholdCount', 8, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'MaxLevel', 400, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33274, 0, {
        'StateCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'TalentLevel' })),
        'MaxCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'ThresholdCount', 6, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'MaxLevel', 500, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33274, 0, {
        'StateCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'TalentLevel' })),
        'MaxCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'ThresholdCount', 4, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 5301, 'MaxLevel', 500, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33274, 0, {
        'StateCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'TalentLevel' })),
        'MaxCount': (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1921, 'Radius', 0, (lambda *a: Func308(*a) * 2))
    CustomAction(oWarrior, oEventCB, {
        'OuterRadius': (lambda *a: Func360(*a, **{
'sid': 1921,
'sAttr': 'Radius' })),
        'InnerRadius': 8,
        'HeroStateTime': 0,
        'MonsterStateTime': 0,
        'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
        '1921_DefaultRadius': 16,
        'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })),
        '1918_DefaultRadius': 5 })
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33044):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1918, 'Radius', 0, (lambda *a: Func308(*a)))
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1326, 'Radius', 0, (lambda *a: Func308(*a)))
        CustomAction(oWarrior, oEventCB, {
            'OuterRadius': (lambda *a: Func360(*a, **{
'sid': 1918,
'sAttr': 'Radius' })),
            'HeroStateTime': 0,
            'MonsterStateTime': 0,
            'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
            '1921_DefaultRadius': 16,
            'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })),
            '1918_DefaultRadius': 5 })
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'TalentLevel' }))) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' }))):
        cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 5301, 'TalentLevel', (lambda *a: Func361(*a, **{
'sid': 5301,
'sArgs': 'MaxLevel' })), None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1325: 1 }, 1, 0):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1918, 'Radius', 0, (lambda *a: Func308(*a)))
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1326, 'Radius', 0, (lambda *a: Func308(*a)))
        CustomAction(oWarrior, oEventCB, {
            'OuterRadius': (lambda *a: Func360(*a, **{
'sid': 1918,
'sAttr': 'Radius' })),
            'HeroStateTime': 0,
            'MonsterStateTime': 0,
            'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
            '1921_DefaultRadius': 16,
            'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })),
            '1918_DefaultRadius': 5 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33044):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1918, 'Radius', 0, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1326, 'Radius', 0, 0)
        CustomAction(oWarrior, oEventCB, {
            'OuterRadius': (lambda *a: Func360(*a, **{
'sid': 1918,
'sAttr': 'Radius' })),
            'HeroStateTime': 0,
            'MonsterStateTime': 0,
            'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
            '1921_DefaultRadius': 16,
            'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })),
            '1918_DefaultRadius': 5 })


class CPerform(CCustomPerform):
    m_SID = 3610
    m_Name = '墨域扩张'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 117

