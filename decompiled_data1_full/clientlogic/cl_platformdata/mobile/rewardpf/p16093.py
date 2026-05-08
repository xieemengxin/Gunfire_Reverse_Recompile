# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16093.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16093.pyc
# Source Generated with Decompyle++
# File: p16093.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func240, Func441
from cl_commondefines import OBTAIN_WARCASH, VIRTUAL_ITEM_GOLDENCUP, VIRTUAL_ITEM_SHOPREFRESH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHOPREFRESH, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREINTERACTSHOP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'CurTarget', (lambda *a: Func240(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Times') < 3 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue(cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget')) >= 0:
        if cl_evcon.EventCBCheckGoodsTypeInReward(oWarrior, oEventCB, VIRTUAL_ITEM_GOLDENCUP):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget'), -1)
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget'), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget')) + 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget')) >= 8:
            if cl_evact.EventCBChangeShopGoods(oWarrior, oEventCB, cl_evact.EventCBGetUnLockedPosByDir(oWarrior, oEventCB, 0, 5), 1019, (lambda *a: 700 + Func441(*a) * 50), OBTAIN_WARCASH, 1, 0, VIRTUAL_ITEM_SHOPREFRESH):
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'CurTarget'), -1)
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Times') + 1)
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Times') >= 3:
                cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_SHOPREFRESH, -1)
                cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFOREINTERACTSHOP, -1)


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
        'Times': 0 }
    m_DieDisable = 0

