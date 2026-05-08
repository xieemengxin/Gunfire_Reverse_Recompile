# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5790.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5790.pyc
# Source Generated with Decompyle++
# File: p5790.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, PF_SUBMSG_THROW, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 15)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 6)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 15)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 7)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8001, 0, None):
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_evact.PassiveSetFinalBulletUse(oWarrior, oEventCB, 10000)
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8001, 0, None):
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_evact.PassiveSetFinalBulletUse(oWarrior, oEventCB, -10000)
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)


class CPerform(CCustomPerform):
    m_SID = 5790
    m_Name = '事功各半'
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
        3: DoCallBackAction3,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

