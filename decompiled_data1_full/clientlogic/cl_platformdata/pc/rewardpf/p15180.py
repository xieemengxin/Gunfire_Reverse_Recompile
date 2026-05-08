# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15180.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15180.pyc
# Source Generated with Decompyle++
# File: p15180.pyc (Python 3.6)

from cl_platformdata.custom.rewardpf.customaction import CustomAction152081, CustomAction152082, CustomAction152083
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERSISTENCE, OBJ_ENEMY, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.ImmunitySubSpdState(oWarrior, oLifeCycle)
    CustomAction152081(oWarrior, oLifeCycle, {
        'ForeverStateSID': 33514,
        'LimitStateSID': 33515 })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_REDUCESPEEDSTATE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVE_REDUCESPEEDSTATE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ENEMY) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33481, 300, {
            'MoveSpeedMul': -3000 }, 0, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction152082(oWarrior, oEventCB, {
        'ForeverStateSID': 33514,
        'LimitStateSID': 33515 })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction152083(oWarrior, oEventCB, {
        'ForeverStateSID': 33514 })


class CPerform(CCustomPerform):
    m_SID = 15180
    m_Name = '致残打击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

