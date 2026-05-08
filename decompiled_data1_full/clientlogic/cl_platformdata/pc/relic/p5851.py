# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5851.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5851.pyc
# Source Generated with Decompyle++
# File: p5851.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func574

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1809, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1809, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckIsShareDamage(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1809, 1, 1) >= 1 and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'PF5851-1', None) == 0:
            cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'PF5851-1', 500, None)
            cl_evact.EventGetTargetByRelic(oWarrior, oEventCB, 5851, 0)
            cl_evact.EventTargetShareDamage(oWarrior, oEventCB, 3000, None, 0, None, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -3000, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckIsShareDamage(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -10000, 0, '')
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func574(*a, **{
'sid': 5851 }))) >= 2 and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'PF5851-2', None) == 0:
            cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'PF5851-2', 500, None)
            cl_evact.EventGetTargetByRelic(oWarrior, oEventCB, 5851, 0)
            cl_evact.EventTargetShareDamage(oWarrior, oEventCB, 3000, None, 0, None, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -3000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 5851
    m_Name = '铁索连环'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

