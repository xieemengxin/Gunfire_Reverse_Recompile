# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p6951.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p6951.pyc
# Source Generated with Decompyle++
# File: p6951.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction6951 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import BOX_DOUBLE_DAMAGE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, RESCUE_SUBMSG_END, RESCUE_SUBMSG_START, WARRIOR_BUILD_TRAP
from cl_newformula import Func326, Func361, Func588

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_START, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RESCUE, RESCUE_SUBMSG_END, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 10, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 10, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33323, 5000, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP) or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1060) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39027: 1,
        39030: 1 }, 1, 0):
        CustomAction(oWarrior, oEventCB, { })
        if cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
            2004: 1,
            2221: 1,
            2222: 1,
            2223: 1,
            2224: 1,
            2201: 1,
            3083: 1,
            3201: 1,
            2381: 1,
            2382: 1,
            2385: 1,
            3381: 1,
            3382: 1,
            3384: 1,
            2421: 1,
            3421: 1,
            2422: 1,
            2041: 1,
            2042: 1,
            2044: 1,
            2061: 1,
            2062: 1,
            2063: 1,
            2064: 1,
            2065: 1,
            2205: 1,
            2241: 1,
            2242: 1,
            2243: 1,
            2244: 1,
            2281: 1,
            2282: 1,
            2283: 1,
            2423: 1,
            3281: 1,
            3282: 1,
            3283: 1 }):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min((1 + 0.8 * Func588(*a, **{
'iTime': 30000 })) * 50, 10 * (1 + 0.8 * Func588(*a, **{
'iTime': 30000 })) * 50 - cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1856, 1)) * max(0, 100 - Func361(*a, **{
'sid': 6951,
'sArgs': 'DamReduction' })) // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 1, 0, 0, BOX_DOUBLE_DAMAGE, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min((1 + 0.8 * Func588(*a, **{
'iTime': 18000 })) * 100, 10 * (1 + 0.8 * Func588(*a, **{
'iTime': 18000 })) * 100 - cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 1856, 1)) * max(0, 100 - Func361(*a, **{
'sid': 6951,
'sArgs': 'DamReduction' })) // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 1, 0, 0, 0, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1856):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1856, (lambda *a: Func326(*a)), 1, 0, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1856, 100, {
            'Damage': (lambda *a: Func326(*a)) }, 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1009, 5000, { }, 1, -1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1009, None, 6951, None)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101006):
        cl_action.CommonForbid(oWarrior, oEventCB.GetCBLifeCycle(), 1023)
    else:
        cl_action.CommonUnForbid(oWarrior, oEventCB.GetCBLifeCycle(), 1023)


class CPerform(CCustomPerform):
    m_SID = 6951
    m_Name = '队友AI承伤'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        10: DoCallBackAction10 }
    m_BaseArgData = {
        'DamReduction': 0 }
    m_DieDisable = 0

