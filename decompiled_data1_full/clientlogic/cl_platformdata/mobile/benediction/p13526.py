# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13526.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13526.pyc
# Source Generated with Decompyle++
# File: p13526.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_SELF
from cl_newformula import Func336, Func361, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', -5000, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0) and cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'TriggerCost', None) == 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32775 }) * 75 // 100 - Func410(*a, **{
'sid': 32775 }) * Func410(*a, **{
'sid': 32775 }) * 5 // 1000 - Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }))) >= 0:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'EnergyCost', (lambda *a: Func410(*a, **{
'sid': 32775 }) * 15 // 100 + Func410(*a, **{
'sid': 32775 }) * Func410(*a, **{
'sid': 32775 }) * 5 // 1000), None)
        else:
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'EnergyCost', (lambda *a: Func410(*a, **{
'sid': 32775 }) - Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' })), None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: 8000 * (Func410(*a, **{
'sid': 32775 }) * 15 // 100 + Func410(*a, **{
'sid': 32775 }) * Func410(*a, **{
'sid': 32775 }) * 5 // 1000)), 0, DAM_TYPE_PERFORM, None, None)
        cl_evact.EventReduceTargetStateEffectiveCount(oWarrior, oEventCB, 32775, (lambda *a: Func336(*a, **{
'sKey': 'EnergyCost' })))
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32775, (lambda *a: -Func336(*a, **{
'sKey': 'EnergyCost' })), -1)
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'TriggerCost', 1, None)


class CPerform(CCustomPerform):
    m_SID = 13526
    m_Name = '覆海极渊'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 110

