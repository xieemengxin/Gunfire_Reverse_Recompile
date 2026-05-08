# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50016.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50016.pyc
# Source Generated with Decompyle++
# File: p50016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CLIENTACTIVE, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddClientActivePrformUseCountMax(oWarrior, oLifeCycle, 12019, 5)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 0, 0, 0)
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddClientActivePrformUseCountMax(oWarrior, oLifeCycle, 12019, 10)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 2, 0, 0)
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddClientActivePrformUseCountMax(oWarrior, oLifeCycle, 12019, 15)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 4, 0, 0)
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 4, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1424: 1,
        12008: 1 }, 0, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 20):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if (not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        8011: 1,
        8001: 1,
        8012: 1,
        1413: 1,
        8013: 1,
        8014: 1,
        1430: 1,
        8007: 1,
        8009: 1 }, 0, 0)) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 30):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1424: 1,
        12008: 1 }, 0, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 30):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if (not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        8011: 1,
        8001: 1,
        8012: 1,
        1413: 1,
        8013: 1,
        8014: 1,
        1430: 1,
        8007: 1,
        8009: 1 }, 0, 0)) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 40):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1424: 1,
        12008: 1 }, 0, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 40):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if (not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        8011: 1,
        8001: 1,
        8012: 1,
        1413: 1,
        8013: 1,
        8014: 1,
        1430: 1,
        8007: 1,
        8009: 1 }, 0, 0)) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 50):
        cl_action.CommonAddClientActivePrformUseCount(oWarrior, oEventCB.GetCBLifeCycle(), 12019, 1)


class CPerform(CCustomPerform):
    m_SID = 50016
    m_Name = '荆棘箭袋'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

