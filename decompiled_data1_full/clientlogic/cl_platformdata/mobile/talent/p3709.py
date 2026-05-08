# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3709.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3709.pyc
# Source Generated with Decompyle++
# File: p3709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3709 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func557, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H2AttMultiple', 12, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H3AttMultiple', 18, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H4AttMultiple', 24, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'AttDistance', 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 6, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H2AttMultiple', 15, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H3AttMultiple', 24, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H4AttMultiple', 32, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'AttDistance', 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Normal', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Elite', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Boss', 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H2AttMultiple', 20, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H3AttMultiple', 36, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1336, 'H4AttMultiple', 48, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'AttDistance', 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Normal', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Elite', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Boss', 1.5)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'Radius', 0, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1336, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Heavy4', 0) and cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33827) >= 30:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * Func717(*a, **{
'sArg': 'Normal' }) / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, None)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * Func717(*a, **{
'sArg': 'Elite' }) / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, None)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * Func717(*a, **{
'sArg': 'Boss' }) / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33827) and cl_evcon.CBGetPFArgs(oWarrior, oEventCB, 1336, 'SkillCount') == 2:
        if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33827) >= 30:
            cl_action.CommonSetPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy', 0)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'EnergyCostH4', 0, 0)
        else:
            cl_action.CommonSetPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy', 3000)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'EnergyCostH4', -3000, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonClearPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy')
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33827) and cl_evcon.CBGetPFArgs(oWarrior, oEventCB, 1336, 'SkillCount') == 2:
        if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33827) >= 30:
            cl_action.CommonSetPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy', 0)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'EnergyCostH4', 0, 0)
        else:
            cl_action.CommonSetPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy', 3000)
            cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'EnergyCostH4', -3000, 0)


class CPerform(CCustomPerform):
    m_SID = 3709
    m_Name = '千钧破障'
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
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 118

