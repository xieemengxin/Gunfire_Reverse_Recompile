# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1227.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1227.pyc
# Source Generated with Decompyle++
# File: s1227.pyc (Python 3.6)

from cl_commondefines import OBJ_VICTIM, TRIGGER_PARASITIC
from cl_newformula import Func643, Func651, Func828
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, TRIGGER_PARASITIC, 0, 0, 0)
        cl_action.CommonDirectEventCBFunc(oListener, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    cl_evact.EventGetTargetByType(oListener, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oListener, oEventCB, 33712, 0, 1, 0, 0) and cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ParasiticCount' }))) >= cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func828(*a, **{
'iState': 33712 }))):
        cl_evact.AchieveCBAddWarStat(oListener, oEventCB, 1)
        if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 2000):
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
            cl_evact.AchieveRewardCheek(oListener, oEventCB, 1023)
        cl_action.CommonSetStateCount(oListener, oEventCB.GetCBLifeCycle(), 33882, (lambda *a: Func643(*a, **{
'sKey': 'achieve1227' })), 0)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.AchieveCBCheckWarStat(oListener, oEventCB, 2000):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1023)


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.AchieveCBAddState(oListener, oEventCB, 33882, 0, { }, 0)
    cl_action.CommonSetStateCount(oListener, oEventCB.GetCBLifeCycle(), 33882, (lambda *a: Func643(*a, **{
'sKey': 'achieve1227' })), 0)


def DoCallBackAction3(oEventCB, oListener):
    cl_action.CommonSetStateCount(oListener, oEventCB.GetCBLifeCycle(), 33882, (lambda *a: Func643(*a, **{
'sKey': 'achieve1227' })), 0)


class CAchieveStat(CCustom):
    m_SID = 1227
    m_Name = '荒野祭仪'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }

