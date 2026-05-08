# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13560.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13560.pyc
# Source Generated with Decompyle++
# File: p13560.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func598, Func651
from cl_commondefines import CREATE_PLANT, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'CreatePlantNum' }))) >= 250:
        cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1333, 'EvolveNum', 3, 1)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 4, 0, 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 33727) < 250:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33876, 0, { }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'CreatePlantNum' }))) >= 250:
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 1333, 'EvolveNum', 3, 1)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'P8506_HitPlant' }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33739, (lambda *a: Func651(*a, **{
'sKey': 'AddStateTime' })), { }, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13560
    m_Name = '森意灌注'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 119

