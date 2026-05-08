# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1105.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1105.pyc
# Source Generated with Decompyle++
# File: s1105.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_BOSS, OBJ_VICTIM, SIDE_TYPE_MONSTER
from cl_newformula import Func595, Func598
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckOpenElement(oListener, oLifeCycle, {
        'EndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func595(*a))) == 4 and cl_evcon.CheckLevelType(oListener, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonListenGlobalMsgCallBack(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_MONSTER, 1)
    else:
        cl_action.CommonDoneGlobalMsg(oListener, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_MONSTER)


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3925: 1,
        3924: 1 }) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1105yaowang' }))) == 0:
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 's1105yaowang', 1)
    elif cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3902: 1,
        3904: 1 }) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1105luohou' }))) == 0:
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 's1105luohou', 1)
    if cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1105yaowang' }))) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1105luohou' }))):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckTargetPointBaseMonsters(oListener, oEventCB, {
        3902: 1,
        3904: 1 }) and cl_condition.CalFormula(oListener, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 's1105luohou' }))) == 0:
        cl_action.CommonSetSavedData(oListener, oEventCB.GetCBLifeCycle(), 's1105luohou', 1)


class CAchieveStat(CCustom):
    m_SID = 1105
    m_Name = '手下败将'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }

