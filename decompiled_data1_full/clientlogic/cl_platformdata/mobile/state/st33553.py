# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33553.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33553.pyc
# Source Generated with Decompyle++
# File: st33553.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func343, Func429, Func437, Func763

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func763(*a))) > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'thrownum', (lambda *a: min(Func343(*a, **{
'sid': 4508 }), Func429(*a, **{
'sArg': 'StatusEffect' }))))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'throwcost', (lambda *a: Func437(*a, **{
'sKey': 'thrownum' })))
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'thrownum') > 0:
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, (lambda *a: Func437(*a, **{
'sKey': 'thrownum' })), FIGHT_KEY_WUDI, 0, 0, 0, None)
            if cl_evcon.GetThisTargetNum(oTarget, oEventCB) > 0:
                cl_action.CommonAddThrowBagBullet(oTarget, oEventCB.GetCBLifeCycle(), -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'throwcost'), 0)
                cl_evact.EventTargetListSortBySelfDis(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'thrownum'))
                cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func763(*a))) == 0:
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'thrownum', (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' })))
                cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'throwcost', 0)
                if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'thrownum') > 0:
                    cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, (lambda *a: Func437(*a, **{
'sKey': 'thrownum' })), FIGHT_KEY_WUDI, 0, 0, 0, None)
                    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) > 0:
                        cl_action.CommonAddThrowBagBullet(oTarget, oEventCB.GetCBLifeCycle(), -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'throwcost'), 0)
                        cl_evact.EventTargetListSortBySelfDis(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'thrownum'))
                        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
                        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33617, 20, 0, { }, 0, 0, None)
    cl_evact.EventCBTriggerMinorByHeroSID(oTarget, oEventCB, 0, {
        'CardNum': 3,
        'QualityNum': 1,
        'AssignEndPos': {
            206: 1,
            207: 1,
            213: 1,
            217: 1,
            218: 1 },
        'CustomData': {
            217: {
                'DamMul': 1,
                'pf7009_throw': 1 } },
        'HalfHeight': {
            206: 1 } })


class CState(cl_state.CState):
    m_SID = 33553
    m_Name = '裂空秘法'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

