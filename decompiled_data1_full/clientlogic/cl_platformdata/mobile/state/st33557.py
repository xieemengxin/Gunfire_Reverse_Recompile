# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33557.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33557.pyc
# Source Generated with Decompyle++
# File: st33557.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func332, Func402, Func429, Func781

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 40, 40, 120, 0, 1, 0, 1, 1, 0, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) > 0:
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func402(*a))) == 3:
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1974, {
                'Att': (lambda *a: 320000 + 120000 * Func332(*a)),
                'fragile': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'),
                'StateTime': (lambda *a: 150 + Func781(*a, **{
'iItem': Func429(*a, **{
'sArg': 'Wand' }),
'sKey': 'AbilityAddLast' })) }, None)
        else:
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1974, {
                'Att': (lambda *a: 160000 + 60000 * Func332(*a)),
                'fragile': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'),
                'StateTime': (lambda *a: 150 + Func781(*a, **{
'iItem': Func429(*a, **{
'sArg': 'Wand' }),
'sKey': 'AbilityAddLast' })) }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33557
    m_Name = '#NT#法杖模块-落雷术'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

