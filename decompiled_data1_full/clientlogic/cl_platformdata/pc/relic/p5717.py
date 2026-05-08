# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5717.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5717.pyc
# Source Generated with Decompyle++
# File: p5717.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_MASK_CLASS, DAM_MASK_ELEMENT, DAM_USE_HP, OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 5000, 0, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, -5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 5000, 0, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckAttackIsVictim(oWarrior, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 30 // 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 4)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckAttackIsVictim(oWarrior, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 30 // 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 4)


class CPerform(CCustomPerform):
    m_SID = 5717
    m_Name = '鲜血圣物'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

