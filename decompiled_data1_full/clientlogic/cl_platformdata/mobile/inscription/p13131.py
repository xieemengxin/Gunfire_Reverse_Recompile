# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13131.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13131.pyc
# Source Generated with Decompyle++
# File: p13131.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM
from cl_newformula import Func751, Func823

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9400: 1,
        1029: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetInSkillCollect(oWarrior, oEventCB, 'PF9400_VID'):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1908, 1, 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExplodePos', cl_evact.EventCBGetTargetPos(oWarrior, oEventCB))
            cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 2004, {
                'vStart': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExplodePos') }, {
                'RemainDamTimes': (lambda *a: Func823(*a, **{
'sAttr': 'RemainDamTimes' })),
                'Att': (lambda *a: Func823(*a, **{
'sAttr': 'Att' })),
                'BaseRadius': 200,
                'ExtraRadius': 400 }, (lambda *a: Func751(*a)))


class CPerform(CCustomPerform):
    m_SID = 13131
    m_Name = '#NT#迭代锯轮专属1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = (2004,)
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1316,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

