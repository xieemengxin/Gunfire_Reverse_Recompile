# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5340.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5340.pyc
# Source Generated with Decompyle++
# File: p5340.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func451, Func717

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ParentActNum', (lambda *a: Func451(*a, **{
'sid': 32006,
'sAttr': 'ParentActNum' })))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TransDamFactor', cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB))
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '9795AttachThunder', 0):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'IgnoreFirstHit', 1, 0)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'IgnoreFirstHit', 0) > 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1670, {
                'ParentActNum': (lambda *a: Func717(*a, **{
'sArg': 'ParentActNum' })),
                'CareerPf': 0,
                'TransDamFactor': cl_evact.PassiveCBGetPFArgsDict(oWarrior, oEventCB, 'TransDamFactor'),
                '5340ExtraAddition': 1 }, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9795, 1, 0):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, '9795AttachThunder', 1, 0)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_DP, -1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, '5340ExtraAddition'):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, DAM_TYPE_PERFORM, '')


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_DP, -1)


class CPerform(CCustomPerform):
    m_SID = 5340
    m_Name = '#NT#速射弓右键雷洛专属加成'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

