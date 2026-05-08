# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5325.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5325.pyc
# Source Generated with Decompyle++
# File: p5325.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CREATE_PLANT, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'E1AttSpeed', 5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 99)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33727, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'CreatePlantNum', 1)
    if cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'PF1436'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33815, 0, { }, 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027):
        cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'CauseCorrisionNum', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 5325
    m_Name = '#NT#园丁被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

