# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50012.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50012.pyc
# Source Generated with Decompyle++
# File: p50012.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, PF_SUBMSG_COMMON
from cl_newformula import Func361, Func410, Func609

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'CountTime', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level1Time' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'Dam', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level1Dam' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50014, 'element', 0, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'CountTime', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level2Time' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'Dam', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level2Dam' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50014, 'element', 0, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'CountTime', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level3Time' })), None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50012, 'Dam', (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Level3Dam' })), None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 5, 0, 2)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50014, 'element', 0, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 1) and cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32993):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32993, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32993, 0, { }, 1, -1, 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32993, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0) and cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33008):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33008, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33008, 0, { }, 1, -1, 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33008, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0) and cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33009):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33009, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33009, 0, { }, 1, -1, 1)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33009, 1, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'CountTime' })))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32993):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Dam' }) * Func410(*a, **{
'sid': 32993 })), 0, DAM_TYPE_FIRE, None, None)
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33008):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Dam' }) * Func410(*a, **{
'sid': 33008 })), 0, DAM_TYPE_CORRISION, None, None)
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33009):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 50012,
'sArgs': 'Dam' }) * Func410(*a, **{
'sid': 33009 })), 0, DAM_TYPE_THUNDER, None, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'Element', (lambda *a: Func609(*a)))


class CPerform(CCustomPerform):
    m_SID = 50012
    m_Name = '元素亲和'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'Level1Time': 1200,
        'Level2Time': 1200,
        'Level3Time': 1200,
        'Level1Dam': 1000,
        'Level2Dam': 1500,
        'Level3Dam': 2000 }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

