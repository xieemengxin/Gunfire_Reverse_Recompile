# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51212.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51212.pyc
# Source Generated with Decompyle++
# File: p51212.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func598, Func651
from cl_commondefines import FIGHT_KEY_WUDI, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33619, 0, {
        'StateCount': (lambda *a: Func598(*a, **{
'sKey': 'ST_33619' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 9, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33619, 0, {
        'StateCount': (lambda *a: Func598(*a, **{
'sKey': 'ST_33619' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 9, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33619, 0, {
        'StateCount': (lambda *a: Func598(*a, **{
'sKey': 'ST_33619' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 9, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33542):
        if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'Die'):
            cl_evact.EventCBAddWandCount(oWarrior, oEventCB, 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33619, 1, 0)
        if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) >= 60:
            cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'ST_33619', 0)
            cl_evact.PassiveCBReplaceSourceWand(oWarrior, oEventCB, 1010)
        elif cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
            if cl_action.PassiveGetLiteCDRemainTime(oWarrior, oEventCB.GetCBLifeCycle()):
                cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 1, 1, cl_action.PassiveGetLiteCDRemainTime(oWarrior, oEventCB.GetCBLifeCycle()), 0, 1, { })
            else:
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 10)
                cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 30, 0, 60, 1, 1, FIGHT_KEY_WUDI, 0, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
                if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
                else:
                    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 1, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
                    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
                    else:
                        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 4, 1, 100, 0, 1, { })
        else:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 10)
            cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 30, 0, 60, 1, 1, FIGHT_KEY_WUDI, 0, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
            else:
                cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 1, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
                if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
                else:
                    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 4, 1, 100, 0, 1, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 10)
    cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 30, 0, 60, 1, 1, FIGHT_KEY_WUDI, 0, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
    else:
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 1, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
        else:
            cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 4, 1, 100, 0, 1, { })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 1, 1, 0, 0, { }, 0, FIGHT_KEY_WUDI, 1, 1, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33542, 0, { }, 1, 1, 0)
    else:
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 4, 1, 100, 0, 1, { })


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'ST_33619' })))


class CPerform(CCustomPerform):
    m_SID = 51212
    m_Name = '#NT#印记法杖前身被动'
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
        4: DoCallBackAction4,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0

