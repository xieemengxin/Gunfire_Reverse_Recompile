# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3808.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3808.pyc
# Source Generated with Decompyle++
# File: p3808.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import CREATE_SEED, PLANT_PHASE_ANGRY
from cl_newformula import Func308, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CreateRatio', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CreateRatio', 45)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CreateRatio', 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, CREATE_SEED, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CreateRatio')):
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SeedID' })))
        cl_evact.EventCBCreatePlantByTargetPos(oWarrior, oEventCB, {
            'Dis': 1,
            'Dir': (1, 0, 0) }, 100, 0, PLANT_PHASE_ANGRY, (lambda *a: Func308(*a)), 1)


class CPerform(CCustomPerform):
    m_SID = 3808
    m_Name = '呼朋引伴'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 119

