# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50701.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50701.pyc
# Source Generated with Decompyle++
# File: p50701.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_ATTACK, WARRIOR_BOSS, WARRIOR_BUILD_TRAP, WARRIOR_PET_HEROSIDE, WARRIOR_PET_MINICLONE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 5)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 2, 0, 0)
    if not cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINICLONE) or cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_HEROSIDE):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 50701, 3, None, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetNavMeshSize(oWarrior, oEventCB.GetCBLifeCycle(), 0.2, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP) or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1060) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39027: 1,
        39030: 1 }, 1, 0):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    elif cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
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
        3283: 1,
        2002: 1,
        2003: 1,
        3001: 1,
        3004: 1 }):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -5000, DAM_MASK_ELEMENT, '')
    elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -2000, DAM_MASK_ELEMENT, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'RHP', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2 / 100), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33208, (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })), { }, 0, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33208, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.ImmunitySubSpdState(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 50701
    m_Name = '#NT#妖灵初始被动'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

