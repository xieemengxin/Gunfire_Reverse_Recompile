# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39761.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39761.pyc
# Source Generated with Decompyle++
# File: st39761.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_THROW, FIGHT_KEY_WUDI, LEVEL_TYPE_BOSS, OBJ_SELF, PICK_BULLET, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404, Func429, Func437, Func529, Func598, Func850, Func861

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': '39761Cnt' })))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ActiveCnt': (lambda *a: Func429(*a, **{
'sArg': 'TiggerCnt' })) })
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('CntMax'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_BULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, '39761Cnt', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'PickNum', (lambda *a: Func861(*a, **{
'iBulletSID': 4508 })))
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'PickNum') > 0:
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'PickNum' }) * Func429(*a, **{
'sArg': 'PickAddCnt' })), None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromThrowPerform(oTarget, oEventCB, 1):
        if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 99, 100, 1, 1, FIGHT_KEY_WUDI, 1, 0, 0, None)
        else:
            cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, (lambda *a: Func429(*a, **{
'sArg': 'AttDis' })), 99, 100, 1, 1, FIGHT_KEY_WUDI, 1, 0, 0, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TiggerCnt'):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func429(*a, **{
'sArg': 'CostCnt' })), 0)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 39762, (lambda *a: Func429(*a, **{
'sArg': 'SuperTime' }) + Func429(*a, **{
'sArg': 'ExtAddTime' }) * Func850(*a)), {
                'DelayTime': (lambda *a: Func429(*a, **{
'sArg': 'DelayTime' })),
                'AttDis': (lambda *a: Func429(*a, **{
'sArg': 'AttDis' })) }, 0)


def CallBack4(oEventCB, oTarget):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonClearBulletPickIgnoreMax(oTarget, oEventCB.GetCBLifeCycle(), 4508)
    else:
        cl_action.CommonSetBulletPickIgnoreMax(oTarget, oEventCB.GetCBLifeCycle(), 4508)


def CallBack5(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UseThrowCnt') >= 2:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurAddCnt', (lambda *a: Func437(*a, **{
'sKey': 'UseThrowCnt' }) // 2))
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'CurAddCnt' }) * 2), 'UseThrowCnt')
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'CurAddCnt' })), 0)


def CallBack6(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func529(*a)), 'UseThrowCnt')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'UseThrowCnt') >= 2:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurAddCnt', (lambda *a: Func437(*a, **{
'sKey': 'UseThrowCnt' }) // 2))
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'CurAddCnt' }) * 2), 'UseThrowCnt')
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'CurAddCnt' })), 0)


class CState(cl_state.CState):
    m_SID = 39761
    m_Name = '次要技能-超载'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 24
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

