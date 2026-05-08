# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51659.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51659.pyc
# Source Generated with Decompyle++
# File: p51659.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJECT_SERVANT, PF_TYPE_THROW, S7_MODULE_POINT_CHANGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeTargetTypePerformAttr(oWarrior, oLifeCycle, PF_TYPE_THROW, 'Att', 500, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oLifeCycle, 7144, 'Att', 0, 500, OBJECT_SERVANT, 1)
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oLifeCycle, 7151, 'Att', 0, 500, OBJECT_SERVANT, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeTargetTypePerformAttr(oWarrior, oLifeCycle, PF_TYPE_THROW, 'Att', 1000, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oLifeCycle, 7144, 'Att', 0, 1000, OBJECT_SERVANT, 1)
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oLifeCycle, 7151, 'Att', 0, 1000, OBJECT_SERVANT, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeTargetTypePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), PF_TYPE_THROW, 'Att', 1500, min(6000, cl_evcon.EventCBGetEquipS7ModulePoint(oWarrior, oEventCB, { }, 1) * 200))
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 217):
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oEventCB.GetCBLifeCycle(), 7144, 'Att', min(6000, cl_evcon.EventCBGetEquipS7ModulePoint(oWarrior, oEventCB, { }, 1) * 200), 1500, OBJECT_SERVANT, 1)
        cl_action.CommonChangePerformAttrFromOwn(oWarrior, oEventCB.GetCBLifeCycle(), 7151, 'Att', min(6000, cl_evcon.EventCBGetEquipS7ModulePoint(oWarrior, oEventCB, { }, 1) * 200), 1500, OBJECT_SERVANT, 1)


class CPerform(CCustomPerform):
    m_SID = 51659
    m_Name = '基础增伤'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

