# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50008.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50008.pyc
# Source Generated with Decompyle++
# File: p50008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK
from cl_newformula import Func361, Func599

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'FinalBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level1FinalBonus' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'OneElementBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level1OneElementBonus' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'FinalBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level2FinalBonus' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'OneElementBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level2OneElementBonus' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'FinalBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level3FinalBonus' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50008, 'OneElementBonus', (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'Level3OneElementBonus' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func599(*a))) == 3:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 3 * Func361(*a, **{
'sid': 50008,
'sArgs': 'OneElementBonus' }) + Func361(*a, **{
'sid': 50008,
'sArgs': 'FinalBonus' })), DAM_TYPE_PERFORM, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func361(*a, **{
'sid': 50008,
'sArgs': 'OneElementBonus' }) * Func599(*a)), DAM_TYPE_PERFORM, '')


class CPerform(CCustomPerform):
    m_SID = 50008
    m_Name = '元素交融'
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
    m_BaseArgData = {
        'Level1FinalBonus': 5000,
        'Level2FinalBonus': 8000,
        'Level3FinalBonus': 12000,
        'Level1OneElementBonus': 5000,
        'Level2OneElementBonus': 8000,
        'Level3OneElementBonus': 12000 }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

