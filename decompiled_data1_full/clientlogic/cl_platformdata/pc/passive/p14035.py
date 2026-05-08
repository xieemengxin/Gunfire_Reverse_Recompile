# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14035.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14035.pyc
# Source Generated with Decompyle++
# File: p14035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 5000, 0, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -5000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 14035
    m_Name = '轮回9-雪山守卫非弱点伤害抗性增加50%'
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

