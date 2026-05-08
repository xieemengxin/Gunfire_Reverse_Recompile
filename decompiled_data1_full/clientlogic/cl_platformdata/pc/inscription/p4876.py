# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4876.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4876.pyc
# Source Generated with Decompyle++
# File: p4876.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1183, 0, { }, 1, None, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1183, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4876
    m_Name = '透视瞄准'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((11,), (), ())
    m_ExcludeList = ((), (), (1016,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

