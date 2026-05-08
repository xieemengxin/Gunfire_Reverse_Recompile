# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p50250.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p50250.pyc
# Source Generated with Decompyle++
# File: p50250.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX
from cl_newformula import Func302, Func641

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7209: 1 }, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * Func641(*a) * 0.0015), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
        elif cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * Func641(*a) * 0.003), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
        else:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * Func641(*a) * 0.01), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


class CPerform(CCustomPerform):
    m_SID = 50250
    m_Name = '#NT#毒气专属1装置被动'
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

