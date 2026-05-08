# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6737.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6737.pyc
# Source Generated with Decompyle++
# File: p6737.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import MG_CASH, MG_SOURCE_KILLMONSTER, MG_SOURCE_KILLMONSTEREXT, MG_SOURCE_KILLSUMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if (cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTER) or cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLSUMMON) or cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_KILLMONSTEREXT)) and cl_evcon.CheckMiniGameType(oWarrior, oEventCB, MG_CASH):
        cl_evact.EventCBChangeMiniGameTimesCal(oWarrior, oEventCB, 0, 0, -10000, 0)


class CPerform(CCustomPerform):
    m_SID = 6737
    m_Name = '怪物不掉落金币'
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

