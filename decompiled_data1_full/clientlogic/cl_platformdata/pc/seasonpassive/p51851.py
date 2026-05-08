# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51851.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51851.pyc
# Source Generated with Decompyle++
# File: p51851.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD
from cl_newformula import Func304, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDis', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 5)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2006)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDis', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 10)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2006)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDis', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttDam', 20)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2006)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 39739):
        if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
            cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 2006, {
                'Att': (lambda *a: Func717(*a, **{
'sArg': 'AttDam' }) * Func304(*a, **{
'sAttr': 'ArmorMax' })),
                'AttDis': (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })) })
        elif cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
            cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 2006, {
                'Att': (lambda *a: Func717(*a, **{
'sArg': 'AttDam' }) * Func304(*a, **{
'sAttr': 'ShieldMax' })),
                'AttDis': (lambda *a: Func717(*a, **{
'sArg': 'AttDis' })) })


class CPerform(CCustomPerform):
    m_SID = 51851
    m_Name = '护盾伤害（近战护盾专属）'
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

