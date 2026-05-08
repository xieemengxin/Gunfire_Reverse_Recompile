# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40003.pyc
# Source Generated with Decompyle++
# File: p40003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF
from math import ceil
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: ceil((Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.1)), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 40003
    m_Name = '天降大任-闪转腾挪1奖励'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

