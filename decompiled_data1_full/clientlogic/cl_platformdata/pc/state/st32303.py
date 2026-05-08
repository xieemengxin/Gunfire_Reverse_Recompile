# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32303.pyc
# Source Generated with Decompyle++
# File: st32303.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
from cl_commondefines import WARRIOR_PROTEGE_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func518

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))) == 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1301003):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 70, WARRIOR_MONSTER, 1, 0, 1, 0, None, None, None)
        if cl_evcon.CheckTargetDist(oTarget, oEventCB, 25, 0, None):
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
                'TransDamFactor': cl_action.CommonGetStateTransDamFactor(oTarget, oEventCB.GetCBLifeCycle(), 32006) }, None)
        elif cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1403001):
            cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 25, OBJ_ENEMY, 0)
            CustomAction(oTarget, oEventCB, {
                'State': 1009 })
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
                'TransDamFactor': cl_action.CommonGetStateTransDamFactor(oTarget, oEventCB.GetCBLifeCycle(), 32006) }, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 25, WARRIOR_MONSTER, 1, 0, 1, 0, None, None, None)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1670, {
                'TransDamFactor': cl_action.CommonGetStateTransDamFactor(oTarget, oEventCB.GetCBLifeCycle(), 32006) }, None)


class CState(cl_state.CState):
    m_SID = 32303
    m_Name = '#NT#雷神之怒3-惊雷'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        'delay': 150,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oWarrior, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo or len(dTransInfo['TargetList']) <= 1:
        return None
    lstTarget = []
    lstMonsterTarget = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oWarrior.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & WARRIOR_PROTEGE_NORMAL != WARRIOR_PROTEGE_NORMAL:
            lstMonsterTarget.append(iTarget)
            continue
        if oTarget.m_State.GetItemBySID(dInfo['State']):
            continue
        lstTarget.append(iTarget)
    
    if lstTarget:
        dTransInfo['TargetList'] = lstTarget
    else:
        dTransInfo['TargetList'] = lstMonsterTarget

