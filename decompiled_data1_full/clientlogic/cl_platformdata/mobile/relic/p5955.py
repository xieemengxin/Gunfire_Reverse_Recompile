# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5955.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5955.pyc
# Source Generated with Decompyle++
# File: p5955.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, DPSUBMSG_DEFAULT, OBJ_SELF, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_DEFAULT, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9212: 1,
        9295: 1,
        9702: 1,
        9291: 1,
        9490: 1,
        9491: 1 }, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > 100:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, 100, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 1, 0, 0, None, None, None, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, 0, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 1, 0, 0, None, None, None, None, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9293, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'CollectHitTarget', 1) == 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > 100:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, 100, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 1, 0, 0, None, None, None, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, 0, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 1, 1, 0, 0, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5955
    m_Name = '谨慎射击'
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
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'StateSID': 33362 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

