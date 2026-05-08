# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7064.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7064.pyc
# Source Generated with Decompyle++
# File: st7064.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE, WARRIOR_HERO
from cl_newformula import Func403, Func404, Func410, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CheckAddImmobilize(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 10, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, None, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) <= 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7065, 0, 1, { }, 0, None, None)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7066, 0, 0, { }, 0, None, None)
        cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 1000, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 17 }, 0, 1, 3, 1)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7065, 0, 1, { }, 0, None, None)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7066, 0, 0, { }, 0, None, None)
        cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 1000, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 13 }, 0, 1, 3, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_HERO):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1046, 0, 1, { }, 0, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'AiNum')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_HERO):
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1046, 0, 1, { }, 0, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'AiNum')


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_HERO):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'AiNum')


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_HERO):
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'AiNum')


def CallBack5(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            if cl_evcon.CheckHasState(oTarget, oEventCB, 8099):
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: ((Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * 0.5 / 100 + 0.01) * Func403(*a, **{
'sAttr': 'HPMax' }) + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
                cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
                if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                    cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
                
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
            
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), 0)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
            cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckHasState(oTarget, oEventCB, 8099):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: ((Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * 0.5 / 100 + 0.01) * Func403(*a, **{
'sAttr': 'HPMax' }) + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
            
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
            cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), 0)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)


def CallBack7(oEventCB, oTarget):
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckHasState(oTarget, oEventCB, 8099):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: ((Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * 0.5 / 100 + 0.01) * Func403(*a, **{
'sAttr': 'HPMax' }) + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
            
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
            cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), 0)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7065, 0, 1, { }, 0, None, None)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7066, 0, 0, { }, 0, None, None)
        cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 1000, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 17 }, 0, 1, 3, 1)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7065, 0, 1, { }, 0, None, None)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7066, 0, 0, { }, 0, None, None)
        cl_evact.EventCBAddSceneEvent(oTarget, oEventCB, 1000, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 13 }, 0, 1, 3, 1)


def CallBack10(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32245, 0, 1, { }, 0, None, None)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 17, OBJ_ENEMY, 1)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)
    else:
        cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 13, OBJ_ENEMY, 1)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)


def CallBack11(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 17, OBJ_ENEMY, 1)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)
    else:
        cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 13, OBJ_ENEMY, 1)
        cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 1046)


def CallBack12(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 8099):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: ((Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * 0.5 / 100 + 0.01) * Func403(*a, **{
'sAttr': 'HPMax' }) + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
        cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
            cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func404(*a) - Func437(*a, **{
'sKey': 'AiNum' })) * Func403(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 0, None)
            cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 7066, (lambda *a: Func404(*a) * 1 + Func410(*a, **{
'sid': 7066 }) * 1 + 0), None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 7066, None, None) >= 40:
                cl_evact.StateCBRemoveStateFromSelf(oTarget, oEventCB, 7066)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7067, 0, 0, { }, 0, None, None)


def CallBack13(oEventCB, oTarget):
    if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'AiNum')


def CallBack14(oEventCB, oTarget):
    if cl_evcon.EventCBCheckTargetIsAIHero(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'AiNum')


class CState(cl_state.CState):
    m_SID = 7064
    m_Name = '#NT#吸血怪吸血关联状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 25,
        'firsttime': 4 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9,
        10: CallBack10,
        11: CallBack11,
        12: CallBack12,
        13: CallBack13,
        14: CallBack14 }

