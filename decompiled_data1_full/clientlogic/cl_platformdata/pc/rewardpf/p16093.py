# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16093.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16093.pyc
# Source Generated with Decompyle++
# File: p16093.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, OBTAIN_WARCASH, VIRTUAL_ITEM_GOLDENCUP
from cl_newformula import Func441

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32739, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHOPREFRESH, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INITGOODS, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanUse', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32739, 1, -1) < 10 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Times') < 3 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanUse'):
        if cl_evcon.EventCBCheckGoodsTypeInReward(oWarrior, oEventCB, VIRTUAL_ITEM_GOLDENCUP):
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32739, 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanUse', 0)
        else:
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32739, 1, 1, -1, None)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32739, 1, -1) >= 10:
            cl_evact.EventCBChangeShopGoods(oWarrior, oEventCB, 5, 1019, (lambda *a: 700 + Func441(*a) * 50), OBTAIN_WARCASH, 1, 0, None)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32739, 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Times') + 1)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanUse', 0)


class CPerform(CCustomPerform):
    m_SID = 16093
    m_Name = '保底大师'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'Times': 0,
        'CanUse': 0 }
    m_DieDisable = 0

