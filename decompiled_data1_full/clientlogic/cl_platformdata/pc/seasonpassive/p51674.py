# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51674.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51674.pyc
# Source Generated with Decompyle++
# File: p51674.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, PF_SUBMSG_CAREERPF, S7_ALL_PERFORM_ENABLE, WARRIOR_MONSTER
from cl_newformula import Func14, Func360, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1757)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1757)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1757)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1757)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'Interval' }))):
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFrame') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - Func717(*a, **{
'sArg': 'LastFrame' }))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'Interval' }) * 25 // 100)):
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCnt', (lambda *a: Func859(*a, **{
'sAttr': 'ExtraCnt' })))
            else:
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCnt', 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFrame', (lambda *a: Func14(*a)))
            cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Range'), 10, 120, 0, 1, FIGHT_KEY_WUDI, 0, 1, 0, None)
            if not cl_evcon.GetTargetNum(oWarrior, oEventCB):
                cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Range'), WARRIOR_MONSTER, 0, 0, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 0, 0, None)
            if cl_evcon.GetTargetNum(oWarrior, oEventCB):
                cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1757, {
                    'vEnd': cl_evact.EventCBGetTargetPos(oWarrior, oEventCB) }, {
                    'Cnt': (lambda *a: Func859(*a, **{
'sAttr': 'Cnt' }) + Func717(*a, **{
'sArg': 'AddCnt' })),
                    'Att': (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' }) * Func360(*a, **{
'sid': 1991,
'sAttr': 'Att' }) // 10000) }, 0)
            else:
                cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Range'), 10, 120, 0, 1, FIGHT_KEY_WUDI, 0, 1, 0, None)
                if not cl_evcon.GetTargetNum(oWarrior, oEventCB):
                    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Range'), WARRIOR_MONSTER, 0, 0, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 0, 0, None)
                if cl_evcon.GetTargetNum(oWarrior, oEventCB):
                    cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1757, {
                        'vEnd': cl_evact.EventCBGetTargetPos(oWarrior, oEventCB) }, {
                        'Cnt': (lambda *a: Func859(*a, **{
'sAttr': 'Cnt' })),
                        'Att': (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' }) * Func360(*a, **{
'sid': 1991,
'sAttr': 'Att' }) // 10000) }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1991):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddFunc', 1)
    else:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddFunc', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 3, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1991) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFunc') == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddFunc', 1)
    elif cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1991) == 0 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddFunc') == 1:
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddFunc', 0)


class CPerform(CCustomPerform):
    m_SID = 51674
    m_Name = '流星-闪焰冲锋'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'Range': 20 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'AttRatio': 300,
            'Cnt': 1 },
        2: {
            'AttRatio': 300,
            'Cnt': 2 },
        3: {
            'AttRatio': 300,
            'Cnt': 3,
            'ExtraCnt': 2,
            'Interval': 70 },
        4: {
            'AttRatio': 300,
            'Cnt': 4,
            'ExtraCnt': 2,
            'Interval': 70 } }

