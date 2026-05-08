# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51727.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51727.pyc
# Source Generated with Decompyle++
# File: p51727.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_NORMAL, OBJECT_OWNER, OBJECT_SERVANT, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_S8THIRDACTIVE, PF_TYPE_THROW
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_S8THIRDACTIVE, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })), 0, DAM_TYPE_FIRE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 2)
    if not cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_S8THIRDACTIVE, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })), 0, DAM_TYPE_FIRE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 2)
    if not cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_S8THIRDACTIVE, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })), 0, DAM_TYPE_FIRE, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_THROW, 2)
    if not cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oLifeCycle, PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'FireAbnormalFactor', 3000, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBPerformDamType(oWarrior, oEventCB, OBJECT_OWNER, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oWarrior, oEventCB, OBJECT_OWNER)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBPerformDamType(oWarrior, oEventCB, OBJECT_SERVANT, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, OBJECT_SERVANT, DAM_TYPE_FIRE, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oWarrior, oEventCB, OBJECT_SERVANT)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBPerformDamType(oWarrior, oEventCB, OBJECT_OWNER, DAM_TYPE_NORMAL, 1):
        cl_action.CommonChangePerformDamTypeByPerformType(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_CAREERPF, OBJECT_OWNER, DAM_TYPE_FIRE, 1, 1)
    else:
        cl_evact.EventCBClearPerformDamType(oWarrior, oEventCB, OBJECT_OWNER)


class CPerform(CCustomPerform):
    m_SID = 51727
    m_Name = '火焰转化'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'DamRate': 3000 },
        2: {
            'DamRate': 6000 },
        3: {
            'DamRate': 12000 } }

