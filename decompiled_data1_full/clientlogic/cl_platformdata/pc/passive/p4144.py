# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4144.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4144.pyc
# Source Generated with Decompyle++
# File: p4144.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_SCENE, DAM_USE_HP, OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALCURE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.HP() < oWarrior.QueryAttr('HPMax'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 0, 2, 0, 1, 1, None)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 9 / 100), CURE_TYPE_SCENE | DAM_USE_HP, 1, 1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1230, 50, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.HP() < oWarrior.QueryAttr('HPMax'):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1207, 0, { }, 1, None, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1207, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4144
    m_Name = '移花接木'
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
    m_BaseArgData = { }
    m_DieDisable = 1

