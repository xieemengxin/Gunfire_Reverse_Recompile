# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25851.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25851.pyc
# Source Generated with Decompyle++
# File: p25851.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE, QUALITY_TYPE_HIGH
from cl_newformula import Func423, Func425, Func557

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBReduceExcessDamage(oWarrior, oEventCB, (lambda *a: Func557(*a)))
    if not cl_evcon.CheckIsShareDamage(oWarrior, oEventCB) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1605: 1,
        1606: 1 }, 1, 1):
        cl_evact.EventGetTargetByMonsterRelic(oWarrior, oEventCB, 25851, 1)
        cl_evact.EventTargetShareDamage(oWarrior, oEventCB, 5000, (lambda *a: Func425(*a)), 0, DAM_TYPE_TRUE, 1)
        if not cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
            cl_evact.EventCBReducePredictDam(oWarrior, oEventCB, (lambda *a: Func423(*a) * 0.5), None)


class CPerform(CCustomPerform):
    m_SID = 25851
    m_Name = '铁索连环'
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
    m_RelicType = 0
    m_HeroRelic = 5851
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

