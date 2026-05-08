# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13603.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13603.pyc
# Source Generated with Decompyle++
# File: p13603.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import MG_SOURCE_RELIC, NWARRIOR_DROP_PETEGG, PET_EGG_NORMAL, PET_EGG_RARE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORECREATEDEMON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HATCH_PET, PET_EGG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HATCH_PET, PET_EGG_RARE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'ConquerChallenge') and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 50):
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 50):
            cl_evact.EventAddDemonReward(oWarrior, oEventCB, NWARRIOR_DROP_PETEGG, {
                'SID': 5535,
                'Type': 1 })
        else:
            cl_evact.EventAddDemonReward(oWarrior, oEventCB, NWARRIOR_DROP_PETEGG, {
                'SID': 5536,
                'Type': 2 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'LeaveGame', 0) == 0 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 30):
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2421, {
            1: 10 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'LeaveGame', 0) == 0 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 70):
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2422, {
                1: 10 }, MG_SOURCE_RELIC, 1, 1, 1, None)
        else:
            cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2422, {
                1: 10 }, MG_SOURCE_RELIC, 1, 1, 2, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'MiniGame2421') or cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'MiniGame2422'):
        cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2137, {
            '$name': cl_evact.EventCBGetRelicName(oWarrior, oEventCB) })


class CPerform(CCustomPerform):
    m_SID = 13603
    m_Name = '妖灵馈赠'
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
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

