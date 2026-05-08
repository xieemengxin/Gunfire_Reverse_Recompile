# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50010.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50010.pyc
# Source Generated with Decompyle++
# File: p50010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, PF_SUBMSG_COMMON
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 0, 0, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 4, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0):
        if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'pf50010MaxExtra'):
            cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'Element', cl_action.CommonGetRandomCustomValue(oWarrior, oEventCB.GetCBLifeCycle(), {
                DAM_TYPE_THUNDER: 1,
                DAM_TYPE_FIRE: 1,
                DAM_TYPE_CORRISION: 1 }))
        else:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                2: 8000,
                3: 2000 }, None)
            cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'pf50010Extra', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'pf50010MaxExtra'):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'Element', cl_action.CommonGetRandomCustomValue(oWarrior, oEventCB.GetCBLifeCycle(), {
            DAM_TYPE_THUNDER: 1,
            DAM_TYPE_FIRE: 1,
            DAM_TYPE_CORRISION: 1 }))
    else:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 8000,
            3: 2000 }, None)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'pf50010Extra', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'pf50010MaxExtra', 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'pf50010MaxExtra', 2)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf50010Att', (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.5))
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1908, 'Att', (lambda *a: Func361(*a, **{
'sid': 1908,
'sArgs': 'Att' }) * 0.5), None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 1908, 'Att', (lambda *a: Func361(*a, **{
'sid': 50010,
'sArgs': 'pf50010Att' })), None)


class CPerform(CCustomPerform):
    m_SID = 50010
    m_Name = '元素涟漪'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

