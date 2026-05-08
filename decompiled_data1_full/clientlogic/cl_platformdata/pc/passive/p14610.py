# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14610.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14610.pyc
# Source Generated with Decompyle++
# File: p14610.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE, FIGHT_KEY_WUDI, WARRIOR_MONSTER
from cl_newformula import Func423, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) or cl_evcon.CheckIsShareDamage(oWarrior, oEventCB):
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 2, 0, 0, { }, 0, FIGHT_KEY_WUDI, 0, 0, None)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'MinorVal' })))
            cl_evact.EventTargetShareDamage(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectVal') * 100, (lambda *a: Func423(*a)), 1, DAM_TYPE_TRUE, 1)
            if not cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, 0):
                cl_evact.EventCBReducePredictDam(oWarrior, oEventCB, (lambda *a: Func423(*a) * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectVal') // 100), None)


class CPerform(CCustomPerform):
    m_SID = 14610
    m_Name = '骰子挑战5技能'
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

