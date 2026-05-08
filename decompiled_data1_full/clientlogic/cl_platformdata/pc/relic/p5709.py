# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5709.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5709.pyc
# Source Generated with Decompyle++
# File: p5709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DROP_BULLETPICK_BULLETCLIP, NWARRIOR_DROP_BULLET, OBJ_SELF, PF_SUBMSG_FILLBULLET, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetBulletPickModule(oWarrior, oLifeCycle, DROP_BULLETPICK_BULLETCLIP)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetBulletPickModule(oWarrior, oLifeCycle, DROP_BULLETPICK_BULLETCLIP)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_BULLET):
        cl_evact.PassiveCBFillEventBullet(oWarrior, oEventCB)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1107, 0, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1107, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_BULLET):
        cl_evact.PassiveCBFillEventBullet(oWarrior, oEventCB)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1462, 0, { }, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1462, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5709
    m_Name = '改良弹夹'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

